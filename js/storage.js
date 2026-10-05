// js/storage.js
// Storage management, schema isolation, and state persistence for Neuroscience PhD Arena
(function () {
  'use strict';

  // Dedicated, isolated storage key for Neuroscience PhD Arena
  // Completely decoupled from the C2 English game to prevent any cross-game data collisions.
  const STORAGE_KEY = 'neuroscience_phd_arena_save_v1';

  const DEFAULT_STATE = {
    version: 1,
    profile: {
      rankIndex: 0,
      streakDays: 0,
      lastPlayedDate: null,
      sessionsCompleted: 0,
      totalCorrect: 0,
      totalAnswered: 0
    },
    ratings: {
      neurobiology: 1400,
      neurogenetics: 1400,
      molecular: 1400,
      biochemistry: 1400,
      neurodegeneration: 1400,
      landmarks: 1400
    },
    globalRating: 1400,
    answersByMode: {
      neurobiology: { total: 0, correct: 0 },
      neurogenetics: { total: 0, correct: 0 },
      molecular: { total: 0, correct: 0 },
      biochemistry: { total: 0, correct: 0 },
      neurodegeneration: { total: 0, correct: 0 },
      landmarks: { total: 0, correct: 0 }
    },
    recentModes: [], // rolling window of up to 40 category responses for variety multiplier
    eloHistory: [],  // rolling log of up to 100 ELO changes
    items: {},       // id -> Leitner SRS record
    mistakesQueue: [], // list of question IDs pending redemption
    soundEnabled: true
  };

  let memoryFallback = null;

  function isLocalStorageAvailable() {
    try {
      const testKey = '__neuro_phd_storage_test__';
      window.localStorage.setItem(testKey, 'ok');
      window.localStorage.removeItem(testKey);
      return true;
    } catch (e) {
      return false;
    }
  }

  const hasStorage = isLocalStorageAvailable();

  // Validate that a loaded or imported state belongs strictly to Neuroscience PhD Arena
  function isNeuroscienceData(data) {
    if (!data || typeof data !== 'object') return false;
    if (data.ratings && typeof data.ratings === 'object') {
      const hasNeuroRatings = data.ratings.neurobiology !== undefined ||
                              data.ratings.neurogenetics !== undefined ||
                              data.ratings.molecular !== undefined ||
                              data.ratings.biochemistry !== undefined ||
                              data.ratings.neurodegeneration !== undefined ||
                              data.ratings.landmarks !== undefined;
      // Reject if it contains legacy C2 English categories
      const hasC2Ratings = data.ratings['use-of-english'] !== undefined ||
                           data.ratings.reading !== undefined ||
                           data.ratings.listening !== undefined ||
                           data.ratings.gapped !== undefined;
      return hasNeuroRatings && !hasC2Ratings;
    }
    return false;
  }

  function loadState() {
    if (!hasStorage) {
      if (!memoryFallback) {
        memoryFallback = JSON.parse(JSON.stringify(DEFAULT_STATE));
      }
      return memoryFallback;
    }

    try {
      // Clean up any old contaminated temporary key from earlier migration attempts
      try {
        window.localStorage.removeItem('neuro_phd_arcade_v1_save');
      } catch (e) {}

      let raw = window.localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);

        // Sanity check: verify that this save is genuine neuroscience data
        if (!isNeuroscienceData(parsed)) {
          console.warn('Contaminated or unrecognized save detected in storage. Resetting to clean Neuroscience state.');
          const fresh = JSON.parse(JSON.stringify(DEFAULT_STATE));
          saveState(fresh);
          return fresh;
        }

        // Sanity check on items: filter out any legacy non-neuroscience question IDs
        let cleanItems = {};
        if (parsed.items && typeof parsed.items === 'object') {
          for (let [id, val] of Object.entries(parsed.items)) {
            if (id.startsWith('nb-') || id.startsWith('ng-') || id.startsWith('mc-') ||
                id.startsWith('bc-') || id.startsWith('nd-') || id.startsWith('lm-')) {
              cleanItems[id] = val;
            }
          }
        }

        // Merge cleanly with defaults
        const merged = Object.assign({}, DEFAULT_STATE, parsed, {
          profile: Object.assign({}, DEFAULT_STATE.profile, parsed.profile || {}),
          ratings: Object.assign({}, DEFAULT_STATE.ratings, parsed.ratings || {}),
          answersByMode: Object.assign({}, DEFAULT_STATE.answersByMode, parsed.answersByMode || {}),
          recentModes: Array.isArray(parsed.recentModes) ? parsed.recentModes : [],
          eloHistory: Array.isArray(parsed.eloHistory) ? parsed.eloHistory : [],
          items: cleanItems,
          mistakesQueue: Array.isArray(parsed.mistakesQueue) ? parsed.mistakesQueue.filter(id =>
            id.startsWith('nb-') || id.startsWith('ng-') || id.startsWith('mc-') ||
            id.startsWith('bc-') || id.startsWith('nd-') || id.startsWith('lm-')
          ) : []
        });

        return merged;
      }

      // Fresh default state
      const fresh = JSON.parse(JSON.stringify(DEFAULT_STATE));
      saveState(fresh);
      return fresh;
    } catch (err) {
      console.warn('Failed to parse localStorage, resetting to defaults:', err);
      const fallback = JSON.parse(JSON.stringify(DEFAULT_STATE));
      saveState(fallback);
      return fallback;
    }
  }

  function saveState(state) {
    if (!hasStorage) {
      memoryFallback = state;
      return;
    }
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (err) {
      console.error('Failed to save to localStorage:', err);
    }
  }

  function resetProgress() {
    if (hasStorage) {
      try {
        window.localStorage.removeItem(STORAGE_KEY);
      } catch (e) { }
    }
    memoryFallback = null;
    return loadState();
  }

  function exportState(state) {
    const jsonStr = JSON.stringify(state, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    const dateStr = new Date().toISOString().split('T')[0];
    a.href = url;
    a.download = `neuroscience_phd_arena_save_${dateStr}.json`;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, 100);
  }

  function validateAndImport(jsonString) {
    try {
      const parsed = JSON.parse(jsonString);
      if (!parsed || typeof parsed !== 'object') {
        throw new Error('Invalid JSON format: save file must be an object.');
      }

      // Guard: strictly ensure the file is a Neuroscience save
      if (!isNeuroscienceData(parsed)) {
        throw new Error('Incompatible save file: This save belongs to another game (e.g. C2 English) or is missing neuroscience disciplines.');
      }

      // Filter items to neuroscience IDs only
      let cleanItems = {};
      if (parsed.items && typeof parsed.items === 'object') {
        for (let [id, val] of Object.entries(parsed.items)) {
          if (id.startsWith('nb-') || id.startsWith('ng-') || id.startsWith('mc-') ||
              id.startsWith('bc-') || id.startsWith('nd-') || id.startsWith('lm-')) {
            cleanItems[id] = val;
          }
        }
      }

      const validState = Object.assign({}, DEFAULT_STATE, parsed, {
        profile: Object.assign({}, DEFAULT_STATE.profile, parsed.profile || {}),
        ratings: Object.assign({}, DEFAULT_STATE.ratings, parsed.ratings || {}),
        answersByMode: Object.assign({}, DEFAULT_STATE.answersByMode, parsed.answersByMode || {}),
        recentModes: Array.isArray(parsed.recentModes) ? parsed.recentModes : [],
        eloHistory: Array.isArray(parsed.eloHistory) ? parsed.eloHistory : [],
        items: cleanItems,
        mistakesQueue: Array.isArray(parsed.mistakesQueue) ? parsed.mistakesQueue.filter(id =>
          id.startsWith('nb-') || id.startsWith('ng-') || id.startsWith('mc-') ||
          id.startsWith('bc-') || id.startsWith('nd-') || id.startsWith('lm-')
        ) : []
      });

      saveState(validState);
      return { success: true, state: validState };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }

  window.C2Storage = {
    loadState: loadState,
    saveState: saveState,
    resetProgress: resetProgress,
    exportState: exportState,
    validateAndImport: validateAndImport,
    DEFAULT_STATE: DEFAULT_STATE,
    STORAGE_KEY: STORAGE_KEY
  };
  window.NEURO_STORAGE = window.C2Storage;
})();
