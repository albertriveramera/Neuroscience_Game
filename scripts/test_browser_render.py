# scripts/test_browser_render.py
import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_path = os.path.abspath("index.html")
url = "file:///" + html_path.replace("\\", "/")

cmd = [
    edge_path,
    "--headless=new",
    "--virtual-time-budget=3000",
    "--dump-dom",
    url
]

try:
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=15)
    dom = proc.stdout
    print(f"Captured DOM length: {len(dom)} characters")

    # Check key dynamic elements rendered by JavaScript
    checks = [
        ('Global ELO pill rendered', '1400 ELO' in dom),
        ('Neurobiology card rendered', 'data-mode="neurobiology"' in dom),
        ('Neurogenetics card rendered', 'data-mode="neurogenetics"' in dom),
        ('Molecular Lab card rendered', 'data-mode="molecular"' in dom),
        ('Biochemistry card rendered', 'data-mode="biochemistry"' in dom),
        ('Neurodegeneration card rendered', 'data-mode="neurodegeneration"' in dom),
        ('Landmark Studies card rendered', 'data-mode="landmarks"' in dom),
        ('Variety chip rendered', 'variety-chip' in dom),
        ('Undergraduate Researcher badge', 'Undergraduate Researcher' in dom),
        ('Export Save button rendered', 'id="btn-export-progress"' in dom),
        ('Import Save button rendered', 'id="btn-import-progress"' in dom),
    ]

    all_passed = True
    for label, passed in checks:
        status = "[PASS]" if passed else "[FAIL]"
        print(f"  {status} {label}")
        if not passed:
            all_passed = False

    if all_passed:
        print("\n[SUCCESS] Browser rendered full DOM and executed JavaScript perfectly!")
    else:
        print("\n[FAIL] Some dynamic elements failed to render in the DOM.")
        exit(1)

except Exception as e:
    print(f"Error testing browser render: {e}")
    exit(1)
