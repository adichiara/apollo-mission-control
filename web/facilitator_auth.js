// Shared facilitator-token storage for validation pages.
// localStorage intentionally shares the token between /admin and /contingency
// tabs on the same deployment origin. sessionStorage is retained as a migration
// fallback for tokens entered before this helper existed.
(function () {
  'use strict';

  const KEY = 'apollo_facilitator_token';

  function migrate() {
    const local = localStorage.getItem(KEY);
    const legacy = sessionStorage.getItem(KEY);
    if (!local && legacy) localStorage.setItem(KEY, legacy);
  }

  function get() {
    migrate();
    return localStorage.getItem(KEY) || '';
  }

  function set(value) {
    const token = String(value || '').trim();
    if (token) {
      localStorage.setItem(KEY, token);
      sessionStorage.setItem(KEY, token);
    } else {
      localStorage.removeItem(KEY);
      sessionStorage.removeItem(KEY);
    }
    return token;
  }

  window.ApolloFacilitatorAuth = { key: KEY, get, set, migrate };
  migrate();
})();
