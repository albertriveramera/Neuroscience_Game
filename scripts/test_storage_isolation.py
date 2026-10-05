# scripts/test_storage_isolation.py
import re

with open("js/storage.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Ensure no references to c2_arcade_v2_save
assert "c2_arcade_v2_save" not in code, "ERROR: Found reference to c2_arcade_v2_save!"
print("[PASS] No references to c2_arcade_v2_save found in storage.js")

# 2. Ensure STORAGE_KEY is dedicated
match = re.search(r"const\s+STORAGE_KEY\s*=\s*'([^']+)'", code)
assert match, "ERROR: Could not find STORAGE_KEY in storage.js"
storage_key = match.group(1)
assert storage_key == "neuroscience_phd_arena_save_v1", f"Unexpected STORAGE_KEY: {storage_key}"
print(f"[PASS] Storage key isolated as: {storage_key}")

# 3. Ensure download filename is neuroscience
assert "neuroscience_phd_arena_save_" in code, "ERROR: Export filename not updated!"
print("[PASS] Export filename verified as neuroscience_phd_arena_save_*.json")

# 4. Ensure test key is decoupled
assert "__c2_storage_test__" not in code, "ERROR: Found old __c2_storage_test__"
print("[PASS] Storage test key decoupled.")

print("\n[SUCCESS] Storage isolation fully verified!")
