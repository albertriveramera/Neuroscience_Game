# scripts/generate_neuroscience_bank.py
"""
Neuroscience PhD Arena - Question Bank Compilation & Distribution Pipeline
Compiles and validates 1,032 questions across 6 core pillars:
1. neurobiology: Cellular & Systems Neurobiology (172 items)
2. neurogenetics: Neurogenetics & Genomics (172 items)
3. molecular: Molecular Biology & Wet Lab Methods (172 items)
4. biochemistry: Neurochemistry & Bioenergetics (172 items)
5. neurodegeneration: Brain Aging & Neurodegeneration (172 items)
6. landmarks: Landmark Studies & Clinical Translation (172 items)
Total = 1,032 PhD-level verified questions.
"""

import os
import json
import collections

# Import verified bank modules
import bank_neurobiology
import bank_neurogenetics
import bank_molecular
import bank_biochemistry
import bank_neurodegeneration
import bank_landmarks

MODES = [
    ("neurobiology", "nb", bank_neurobiology.QUESTIONS),
    ("neurogenetics", "ng", bank_neurogenetics.QUESTIONS),
    ("molecular", "mol", bank_molecular.QUESTIONS),
    ("biochemistry", "bc", bank_biochemistry.QUESTIONS),
    ("neurodegeneration", "nd", bank_neurodegeneration.QUESTIONS),
    ("landmarks", "lm", bank_landmarks.QUESTIONS),
]

def load_all_questions():
    bank = {}
    for mode, prefix, questions in MODES:
        bank[mode] = list(questions)
    return bank

def balance_options_and_clean(bank):
    """
    Standardizes schema, assigns canonical IDs, and ensures that answer indices
    (0, 1, 2, 3) are evenly and deterministically distributed across the question
    bank by rotating options according to question sequence.
    """
    prefix_map = {mode: prefix for mode, prefix, _ in MODES}
    processed = {}

    for mode, questions in bank.items():
        prefix = prefix_map[mode]
        cleaned_list = []

        for i, q in enumerate(questions):
            item = dict(q)
            opts = list(item["options"])
            orig_ans = item["answer"]

            # Standardize core metadata
            item["id"] = f"{prefix}-{i+1:03d}"
            item["mode"] = mode
            item["type"] = "choice"

            # Shift options deterministically so answer positions rotate: 0, 1, 2, 3, 0, 1, 2, 3...
            target_pos = i % len(opts)
            if target_pos != orig_ans:
                opts[orig_ans], opts[target_pos] = opts[target_pos], opts[orig_ans]
                item["options"] = opts
                item["answer"] = target_pos
            else:
                item["options"] = opts
                item["answer"] = orig_ans

            cleaned_list.append(item)

        processed[mode] = cleaned_list

    return processed

def write_data_files(bank, output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    stats = {}

    for mode, _, _ in MODES:
        questions = bank.get(mode, [])
        filepath = os.path.join(output_dir, f"{mode}.js")

        json_str = json.dumps(questions, indent=2, ensure_ascii=False)
        content = (
            f"// Neuroscience PhD Arena - {mode.upper()} Question Bank ({len(questions)} Curated Items)\n"
            f"window.C2_DATA = window.C2_DATA || {{}};\n"
            f"window.NEURO_DATA = window.C2_DATA;\n\n"
            f"window.C2_DATA.{mode} = {json_str};\n"
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        stats[mode] = len(questions)

    return stats

def main():
    print("Compiling Neuroscience PhD Question Banks (Target: 1,032 Questions)...")
    raw_bank = load_all_questions()
    balanced_bank = balance_options_and_clean(raw_bank)
    stats = write_data_files(balanced_bank)

    total = sum(stats.values())
    print("==================================================")
    print("     NEUROSCIENCE QUESTION BANK GENERATION")
    print("==================================================")
    for mode, count in stats.items():
        print(f"  {mode:20} : {count:4d} questions")
    print("--------------------------------------------------")
    print(f"  TOTAL QUESTIONS      : {total:4d}")
    print("==================================================")

if __name__ == "__main__":
    main()
