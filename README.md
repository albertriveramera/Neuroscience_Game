# Neuroscience PhD Arena 🧠🎓
> **Adaptive ELO Browser Arena for Neuroscience Doctoral Mastery**

An offline-first, pure JavaScript browser application designed specifically to bridge the demanding gap between **Undergraduate Neurobiology** and **Advanced PhD Research Mastery** in cellular, molecular, genetic, biochemical, and translational brain science.

---

## 📖 Pedagogical Architecture & Concept

This project transforms the core adaptive gaming engine into an advanced training accelerator tailored for PhD students, postdocs, and qualifying exam candidates in neuroscience. It covers fundamental biophysics up to frontier debates in neurodegenerative disease mechanisms and clinical trials.

### The Six Neuroscience Pillars:
1. **Cellular & Systems Neurobiology (`neurobiology`)**: Action potentials, ion channel biophysics (Nav1.2/1.6, delayed rectifiers, K2P, Kir4.1, HCN), synaptic transmission (SNARE complex, synaptotagmin-1, quantal release), NMDA/AMPA subunit kinetics and RNA editing (GluA2 Q/R), GABA-A/B signaling, LTP/LTD molecular cascades (CaMKII Thr286, calcineurin), and microcircuit dynamics (PV+ basket cells, SST+ Martinotti cells, VIP disinhibition).
2. **Neurogenetics & Genomics (`neurogenetics`)**: Mendelian vs polygenic neurological disorders (Huntington's CAG repeats, Fragile X CGG, SMA SMN1/SMN2 splicing), Alzheimer's genetics (APP, PSEN1, PSEN2, APOE alleles ε2/ε3/ε4, APOE Christchurch R136S), Parkinson's loci (SNCA duplications/triplications, LRRK2 G2019S, PRKN, PINK1, GBA1), ALS/FTD (C9orf72 G4C2 hexanucleotide repeats, RAN translation into dipeptide repeats), Cre-loxP recombination and cell-type promoters (Camk2a, Syn1, Gad1, Gfap), and single-cell eQTL mapping.
3. **Molecular Biology & Wet Lab (`molecular`)**: Single-nucleus vs single-cell RNA-seq (snRNA-seq in frozen human brain tissue), spatial transcriptomics (MERFISH, seqFISH, 10x Visium), AAV capsid engineering (AAV-PHP.eB and LY6A receptor tropism), monosynaptic retrograde rabies tracing, optogenetics (ChR2, Chronos, NpHR, Arch), chemogenetics (DREADDs hM3Dq/hM4Di and DCZ agonist), proximity biotinylation (TurboID), ATAC-seq, Expansion Microscopy (ExM), and cryo-EM structures of patient-derived tau and amyloid fibrils.
4. **Neurochemistry & Bioenergetics (`biochemistry`)**: Brain fuel substrates (GLUT1 vs GLUT3, Astrocyte-Neuron Lactate Shuttle ANLS), mitochondrial respiration and OXPHOS complexes, the Ubiquitin-Proteasome System (UPS, K48 polyubiquitination), macroautophagy and TFEB nuclear translocation via the CLEAR network, PINK1-Parkin mediated mitophagy, brain cholesterol synthesis via astrocytic ABCA1 and ApoE lipidation, ferroptosis (GPX4 and System xc-), and liquid-liquid phase separation (LLPS) of RNA-binding proteins.
5. **Aging & Neurodegeneration (`neurodegeneration`)**:
   - **Alzheimer's Disease**: Amyloid precursor protein (APP) processing (ADAM10 vs BACE1 and γ-secretase complex PSEN1/Nicastrin/APH-1/PEN-2), Aβ42 oligomer toxicity, tau hyperphosphorylation and paired helical filaments, 3R vs 4R tauopathies (Pick's vs PSP/CBD), Disease-Associated Microglia (DAM / MGnD) and TREM2-DAP12 plaque compaction.
   - **Parkinson's Disease**: Nigrostriatal dopaminergic neurodegeneration, α-synuclein Lewy bodies (p-Ser129), Braak gut-to-brain staging, LRRK2 hyperphosphorylation of Rab GTPases (Rab10 Thr73), and lysosomal glucocerebrosidase deficiency.
   - **ALS & Frontotemporal Dementia**: TDP-43 nuclear clearance, cryptic exon missplicing (STMN2, UNC13A), C9orf72 DPR neurotoxicity, and cellular senescence (p16INK4a, SASP factors).
6. **Landmark Studies & Clinical Translation (`landmarks`)**:
   - Historical breakthroughs: Otto Loewi's dual frog hearts (acetylcholine), Hodgkin-Huxley squid giant axon voltage clamp, Scoville & Milner's Patient H.M. (episodic memory), Terje Lømo and Timothy Bliss (discovery of LTP), Eric Kandel's *Aplysia* sensitization, and the cloning of human APP on chromosome 21.
   - Clinical trials & therapeutics: Anti-amyloid monoclonal antibodies (Lecanemab CLARITY AD, Donanemab TRAILBLAZER-ALZ 2, Aducanumab), mechanism of Amyloid-Related Imaging Abnormalities (ARIA-E and ARIA-H), BACE1 inhibitor trial failures, Tofersen (SOD1 antisense oligonucleotide in ALS), tau-targeting ASOs (BIIB080), and fluid biomarkers (plasma p-tau217, p-tau181, Neurofilament Light NfL).

---

## 🌟 Progressive Academic Tiers & ELO Calibration

Questions range across five calibrated difficulty tiers reflecting educational progression:
- **Level 1 (1100 ELO)**: Undergraduate Foundations (Core cell biology, Nernst equation, basic genetics, action potential phases).
- **Level 2 (1250 ELO)**: Advanced Undergrad / Post-Bacc (Channel biophysics, quantal analysis, standard wet-lab assays, basic neuropathology).
- **Level 3 (1400 ELO)**: Early Graduate / Master's (Qualifying exam curriculum, signal transduction, Cre-loxP transgenics, core disease mechanisms).
- **Level 4 (1550 ELO)**: Senior PhD Research (Cutting-edge single-cell omics, high-resolution imaging, pathogenic mutations, structural biology).
- **Level 5 (1700+ ELO)**: Principal Investigator / Defended PhD (Frontier translational research, cryo-EM fibril folds, Phase 3 trial mechanisms, complex mechanistic debates).

### Academic Rank Ladder:
- 🥉 **Undergraduate Researcher**: $\ge 1200\text{ ELO} \;\&\; 0\text{ correct answers}$
- 🥈 **Master's Fellow**: $\ge 1350\text{ ELO} \;\&\; 25\text{ correct answers}$
- 🥇 **PhD Candidate**: $\ge 1500\text{ ELO} \;\&\; 60\text{ correct answers}$
- 💎 **Postdoctoral Scholar**: $\ge 1650\text{ ELO} \;\&\; 120\text{ correct answers}$
- 👑 **Principal Investigator**: $\ge 1800\text{ ELO} \;\&\; 200\text{ correct answers}$

*Includes a 25-point hysteresis buffer to eliminate rank oscillation at border thresholds.*

---

## ⚙️ Core Technical Features

1. **Rigorous ELO Rating Architecture**:
   - Calibrated expected scores adjusted for 4-choice guess floor ($c = 0.25$).
   - Dynamic K-factor: Provisional ($K=40$, $<30$ answers), Calibrated ($K=28$, $30-99$ answers), Mastered ($K=20$, $\ge 100$ answers).
   - Anti-grinding variety multiplier: FIFO tracking over the player's last 40 answered categories penalizes overplayed disciplines (down to $0.50\times$) and rewards neglected disciplines (up to $1.20\times$), applied strictly to ELO gains to prevent gaming.
2. **Gaussian Proximal Development Sampling**:
   - Questions in practice sessions are sampled with a Gaussian kernel centered on the player's category rating ($\sigma = 180\text{ ELO}$).
3. **Spaced Repetition System (Leitner 5-Box)**:
   - Tracks intervals across expanding review schedules (1, 3, 7, 14, and 30 days) with an active Mistakes Redemption queue.
4. **Pedagogical Explanations & Literature Contexts**:
   - Every question features an in-depth mechanistic explanation and a concrete experimental scenario, lab observation, or landmark paper context.
5. **Zero Dependencies & Full Offline Support**:
   - Built in pure Vanilla JavaScript, HTML5, and CSS3.
   - Runs directly off the `file://` protocol with zero build steps or web servers required.
   - Built-in Web Audio synthesizer generates sound effects without external audio assets.
   - Pure canvas particle confetti engine for rank-up celebrations.
   - JSON data backup and transfer utilities.

---

## 📁 Repository Structure

```text
Neuroscience_Game/
├── index.html                   # Master single-page application structure
├── README.md                    # Project overview and academic curriculum
│
├── css/
│   └── styles.css               # Luxury dark glassmorphism design system & micro-animations
│
├── js/
│   ├── elo.js                   # ELO calculation, variety multiplier, and rank gating engine
│   ├── storage.js               # State persistence, default state, and backup import/export
│   ├── engine.js                # ELO-weighted session sampling and streak tracking
│   ├── srs.js                   # Leitner 5-box spaced repetition system logic
│   ├── ui.js                    # Web Audio synth, canvas confetti, header pills & modal analytics
│   └── app.js                   # Master application controller and session loop
│
├── data/
│   ├── neurobiology.js          # Cellular & Systems Neurobiology bank (172 curated items)
│   ├── neurogenetics.js         # Neurogenetics & Genomics bank (172 curated items)
│   ├── molecular.js             # Molecular Biology & Wet Lab bank (172 curated items)
│   ├── biochemistry.js          # Neurochemistry & Bioenergetics bank (172 curated items)
│   ├── neurodegeneration.js     # Brain Aging & Neurodegeneration bank (172 curated items)
│   └── landmarks.js             # Landmark Studies & Clinical Translation bank (172 curated items)
│
└── scripts/
    ├── audit_bank.py            # Quality auditor (validates uniqueness, examples, options, syntax)
    ├── simulate_elo.py          # Mathematical test suite for ELO, variety penalties, and rank gating
    ├── test_browser_render.py   # Headless browser validation verifying DOM rendering and JS execution
    ├── test_mobile_viewport.py  # Mobile responsiveness testing across device viewports
    ├── generate_neuroscience_bank.py # Master bank compilation and balance pipeline
    └── bank_*.py                # Standalone category question bank modules (172 items each)
```

---

## 🧪 Automated Testing & Verification

Run the test suite using Python:

```bash
# 1. Audit question bank uniqueness, schemas, and pedagogical examples (1,032 items)
python scripts/audit_bank.py

# 2. Mathematically simulate ELO curves, variety decay, and hysteresis demotion
python scripts/simulate_elo.py

# 3. Verify headless browser rendering and JavaScript execution via Edge
python scripts/test_browser_render.py

# 4. Verify mobile viewport rendering across phone screen resolutions
python scripts/test_mobile_viewport.py
```

---

## 🚀 How to Run

1. Open `index.html` in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).
2. Works 100% offline via local `file://` protocol.
3. Progress is saved automatically to browser `localStorage`.
