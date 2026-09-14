from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.pc2_session import PC2Session, SessionStatus  # noqa: E402
from apollo_mission_control.realtime_clock import RealtimeSessionClock  # noqa: E402
from apollo_mission_control.session_runtime import SessionStatus as SharedSessionStatus  # noqa: E402


class FakeClock:
    def __init__(self, value=1000.0):
        self.value = float(value)

    def now(self):
        return self.value

    def advance(self, seconds):
        self.value += float(seconds)




class GenericState:
    def __init__(self, get_s=10.0):
        self.get_s = float(get_s)
        self.phase = "generic"


class GenericEvent:
    def __init__(self, get_s):
        self.get_s = float(get_s)


class GenericRuntime:
    """Minimal non-PC2 object proving realtime pacing is runtime-neutral."""

    def __init__(self):
        self.state = GenericState()
        self.events = [GenericEvent(20.0)]
        self.status = SharedSessionStatus.RUNNING

    def advance_to(self, target_get_s):
        self.state.get_s = float(target_get_s)
        if self.state.get_s >= self.events[-1].get_s:
            self.status = SharedSessionStatus.COMPLETE
        return self.state.get_s


class RealtimeSessionClockTests(unittest.TestCase):
    def _session(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        return PC2Session.create(fixture)


    def test_clock_accepts_non_pc2_runtime_contract(self):
        session = GenericRuntime()
        fake = FakeClock()
        clock = RealtimeSessionClock(session, now_fn=fake.now)
        clock.reanchor()

        fake.advance(3.5)
        self.assertAlmostEqual(clock.sync(), 13.5, places=6)

        fake.advance(20.0)
        self.assertEqual(clock.sync(), 20.0)
        self.assertEqual(session.status, SharedSessionStatus.COMPLETE)

    def test_running_session_accrues_get_at_one_to_one_rate(self):
        session = self._session()
        fake = FakeClock()
        clock = RealtimeSessionClock(session, now_fn=fake.now)
        session.start()
        clock.reanchor()

        start_get = session.state.get_s
        fake.advance(12.5)
        reached = clock.sync()

        self.assertAlmostEqual(reached, start_get + 12.5, places=6)

    def test_pending_controller_gate_does_not_stop_realtime_clock(self):
        session = self._session()
        session.assign_station("flight", "FLIGHT")
        fake = FakeClock()
        clock = RealtimeSessionClock(session, now_fn=fake.now)
        session.start()
        clock.reanchor()

        seconds_to_7918 = hms_to_seconds("79:18:00") - session.state.get_s
        fake.advance(seconds_to_7918)
        clock.sync()

        self.assertEqual(session.pending_gate, "flight_go")
        self.assertEqual(session.status, SessionStatus.RUNNING)
        self.assertEqual(session.state.get_s, hms_to_seconds("79:18:00"))

        fake.advance(60.0)
        clock.sync()
        self.assertEqual(session.state.get_s, hms_to_seconds("79:19:00"))

    def test_explicit_pause_stops_realtime_get_until_resume(self):
        session = self._session()
        fake = FakeClock()
        clock = RealtimeSessionClock(session, now_fn=fake.now)
        session.start()
        clock.reanchor()

        fake.advance(10.0)
        clock.sync()
        before_pause = session.state.get_s

        session.pause()
        clock.reanchor()
        fake.advance(120.0)
        self.assertEqual(clock.sync(), before_pause)

        session.resume()
        clock.reanchor()
        fake.advance(5.0)
        self.assertAlmostEqual(clock.sync(), before_pause + 5.0, places=6)

    def test_driver_caps_at_end_of_modeled_slice(self):
        session = self._session()
        fake = FakeClock()
        clock = RealtimeSessionClock(session, now_fn=fake.now)
        session.start()
        clock.reanchor()

        fake.advance(10000.0)
        reached = clock.sync()

        self.assertEqual(reached, session.events[-1].get_s)
        self.assertEqual(session.status, SessionStatus.COMPLETE)


if __name__ == "__main__":
    unittest.main()
