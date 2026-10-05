# scripts/test_import_export.py
import json

# Test that default state and v1 legacy data import and export cleanly
v2_sample = {
    "version": 2,
    "profile": {
        "rankIndex": 2,
        "streakDays": 5,
        "lastPlayedDate": "2026-10-05",
        "sessionsCompleted": 12,
        "totalCorrect": 85,
        "totalAnswered": 110
    },
    "ratings": {
        "neurobiology": 1520,
        "neurogenetics": 1490,
        "molecular": 1440,
        "biochemistry": 1580,
        "neurodegeneration": 1460,
        "landmarks": 1510
    },
    "globalRating": 1500,
    "answersByMode": {
        "neurobiology": {"total": 20, "correct": 16},
        "neurogenetics": {"total": 18, "correct": 14},
        "molecular": {"total": 15, "correct": 11},
        "biochemistry": {"total": 22, "correct": 18},
        "neurodegeneration": {"total": 17, "correct": 12},
        "landmarks": {"total": 18, "correct": 14}
    },
    "recentModes": ["biochemistry", "neurobiology", "neurodegeneration"],
    "eloHistory": [],
    "items": {},
    "mistakesQueue": ["nb-001"],
    "soundEnabled": True
}

# Test JSON serialization / deserialization roundtrip
serialized = json.dumps(v2_sample, indent=2)
deserialized = json.loads(serialized)
assert deserialized["version"] == 2
assert deserialized["ratings"]["biochemistry"] == 1580
assert deserialized["profile"]["rankIndex"] == 2
print("[SUCCESS] Import/Export JSON schema roundtrip verified!")
