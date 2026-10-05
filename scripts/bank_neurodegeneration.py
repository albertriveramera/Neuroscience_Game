# scripts/bank_neurodegeneration.py
"""
Brain Aging & Neurodegeneration Question Bank (172 Curated Questions)
"""

QUESTIONS = [
  {
    "id": "nd-001",
    "mode": "neurodegeneration",
    "level": 1,
    "type": "choice",
    "topic": "Alzheimer's Neuropathological Hallmarks",
    "prompt": "The two definitive, post-mortem neuropathological hallmarks required for a definitive diagnosis of Alzheimer's disease are:",
    "options": [
      "Extracellular amyloid-beta (Aβ) senile plaques and intracellular neurofibrillary tangles (NFTs) of hyperphosphorylated tau",
      "Intranuclear huntingtin inclusions and ballooned cortical neurons",
      "Cytoplasmic alpha-synuclein Lewy bodies and glial cytoplasmic inclusions",
      "Prion protein plaques and spongiform vacuolation"
    ],
    "answer": 0,
    "explain": "Alzheimer's disease neuropathology is defined by the coexistence of extracellular amyloid-beta plaques (predominantly fibrillar Aβ42/Aβ40 peptides) and intracellular neurofibrillary tangles composed of hyperphosphorylated microtubule-associated protein tau.",
    "example": "Silver staining and immunohistochemistry reveal dense-core amyloid plaques surrounded by dystrophic neurites and tau tangles throughout the neocortex."
  },
  {
    "id": "nd-002",
    "mode": "neurodegeneration",
    "level": 1,
    "type": "choice",
    "topic": "Parkinson's Disease Pathology",
    "prompt": "The classical motor symptoms of Parkinson's disease (resting tremor, rigidity, bradykinesia) are primarily caused by degeneration of dopaminergic neurons in which brain nucleus?",
    "options": [
      "Substantia nigra pars compacta (SNc)",
      "Locus coeruleus",
      "Ventral tegmental area (VTA)",
      "Globus pallidus internus"
    ],
    "answer": 0,
    "explain": "Motor parkinsonism manifests when ~50-70% of dopaminergic neurons in the substantia nigra pars compacta (SNc) have degenerated, resulting in severe dopamine depletion in the dorsal striatum (caudate and putamen).",
    "example": "Gross macroscopic examination of the Parkinsonian midbrain shows striking loss of dark neuromelanin pigmentation in the substantia nigra."
  },
  {
    "id": "nd-003",
    "mode": "neurodegeneration",
    "level": 1,
    "type": "choice",
    "topic": "Lewy Body Composition",
    "prompt": "The primary structural protein constituent of Lewy bodies and Lewy neurites in Parkinson's disease is:",
    "options": [
      "Alpha-synuclein",
      "Beta-amyloid",
      "Superoxide dismutase 1 (SOD1)",
      "Huntingtin"
    ],
    "answer": 0,
    "explain": "In 1997, Spillantini et al. discovered that Lewy bodies (the pathological intracytoplasmic inclusions found in Parkinson's disease and Dementia with Lewy Bodies) consist predominantly of filamentous, aggregated alpha-synuclein.",
    "example": "Immunostaining for alpha-synuclein phosphorylated at Ser129 is the diagnostic gold standard for visualizing Lewy pathology."
  },
  {
    "id": "nd-004",
    "mode": "neurodegeneration",
    "level": 1,
    "type": "choice",
    "topic": "Anatomical Progression in Early AD",
    "prompt": "Which brain structure exhibits the earliest neurofibrillary tangle pathology and synaptic degeneration, leading to the hallmark deficit in episodic memory in early Alzheimer's disease?",
    "options": [
      "Transentorhinal / Entorhinal cortex and Hippocampus",
      "Primary visual cortex (Brodmann area 17)",
      "Cerebellar Purkinje cell layer",
      "Ventral striatum and nucleus accumbens"
    ],
    "answer": 0,
    "explain": "According to Braak staging, tau neurofibrillary tangles consistently appear first in the transentorhinal and entorhinal cortices before spreading into the CA1 and subiculum of the hippocampus, causing severe impairment in the encoding and consolidation of new episodic memories.",
    "example": "Structural MRI scans of mild cognitive impairment (MCI) patients frequently show progressive atrophy of the entorhinal cortex and hippocampus."
  },
  {
    "id": "nd-005",
    "mode": "neurodegeneration",
    "level": 1,
    "type": "choice",
    "topic": "Amyotrophic Lateral Sclerosis (ALS)",
    "prompt": "Amyotrophic Lateral Sclerosis (ALS) is clinically characterized by the progressive, selective loss of:",
    "options": [
      "Both upper motor neurons in the motor cortex and lower motor neurons in the brainstem and spinal cord",
      "Strictly sensory neurons in the dorsal root ganglia",
      "Cerebellar granule cells exclusively",
      "Hypothalamic orexinergic neurons"
    ],
    "answer": 0,
    "explain": "ALS causes progressive spasticity, hyperreflexia (upper motor neuron signs) along with progressive muscle atrophy, fasciculations, and flaccid weakness (lower motor neuron signs) due to dual degeneration of corticospinal projection neurons and spinal anterior horn alpha-motor neurons.",
    "example": "Denervation of diaphragmatic neuromuscular junctions ultimately leads to fatal respiratory failure in ALS patients."
  },
  {
    "id": "nd-006",
    "mode": "neurodegeneration",
    "level": 2,
    "type": "choice",
    "topic": "APP Secretase Processing",
    "prompt": "In the non-amyloidogenic processing pathway of APP, which enzyme cleaves APP within the Aβ sequence, thereby precluding the formation of intact Aβ peptides?",
    "options": [
      "Alpha-secretase (predominantly ADAM10)",
      "Beta-secretase (BACE1)",
      "Gamma-secretase (Presenilin)",
      "Caspase-3"
    ],
    "answer": 0,
    "explain": "Alpha-secretase (ADAM10) cleaves APP between Lys16 and Leu17 of the Aβ domain, releasing neuroprotective soluble sAPPα and generating the membrane-tethered C83 (CTFα) fragment. Subsequent gamma-cleavage of C83 produces benign p3 peptide instead of toxic Aβ.",
    "example": "Overexpression of ADAM10 in AD transgenic mice enhances sAPPα release and reduces amyloid plaque burden."
  },
  {
    "id": "nd-007",
    "mode": "neurodegeneration",
    "level": 2,
    "type": "choice",
    "topic": "Gamma-Secretase Complex Stoichiometry",
    "prompt": "The intramembrane-cleaving protease gamma-secretase is an obligate tetrameric complex composed of Presenilin (catalytic subunit) and which three non-catalytic cofactor proteins?",
    "options": [
      "Nicastrin, APH-1, and PEN-2",
      "ADAM10, BACE1, and BACE2",
      "ApoE, Clusterin, and PICALM",
      "Syntaxin, SNAP-25, and Synaptobrevin"
    ],
    "answer": 0,
    "explain": "Active gamma-secretase requires 1:1:1:1 assembly of: 1) Presenilin-1 or -2 (contains the two catalytic aspartate residues); 2) Nicastrin (glycosylated substrate recognition subunit); 3) Anterior pharynx-defective 1 (APH-1); and 4) Presenilin enhancer 2 (PEN-2, which triggers Presenilin endoproteolysis into active NTF/CTF heterodimers).",
    "example": "Genetic deletion of any one of the four subunits completely abolishes gamma-secretase activity and embryonic Notch signaling in mice."
  },
  {
    "id": "nd-008",
    "mode": "neurodegeneration",
    "level": 2,
    "type": "choice",
    "topic": "Tau Physiological Function",
    "prompt": "Under physiological conditions in healthy neurons, what is the primary cellular function of the microtubule-associated protein tau (encoded by MAPT)?",
    "options": [
      "Binding to and stabilizing axonal microtubules to promote tubulin assembly and fast axonal transport",
      "Degrading misfolded cytosolic proteins in the proteasome",
      "Pumping calcium into synaptic vesicles",
      "Acting as a transcription factor in the nucleolus"
    ],
    "answer": 0,
    "explain": "Tau is predominantly localized to axons where its C-terminal microtubule-binding repeats bind alpha/beta-tubulin heterodimers, promoting microtubule polymerization, maintaining axonal structural stability, and facilitating motor protein-driven axonal transport.",
    "example": "In Alzheimer's disease, hyperphosphorylation causes tau to detach from microtubules, resulting in axonal microtubule disassembly and cytoskeletal collapse."
  },
  {
    "id": "nd-009",
    "mode": "neurodegeneration",
    "level": 2,
    "type": "choice",
    "topic": "Aβ42 vs Aβ40 Hydrophobicity",
    "prompt": "Although Aβ40 is produced in much higher quantities in the human brain, Aβ42 is far more pathogenic and prone to nucleate amyloid plaques because:",
    "options": [
      "The two additional C-terminal residues (Ile41 and Ala42) are highly hydrophobic, dramatically increasing beta-sheet aggregation propensity",
      "Aβ42 binds covalently to DNA",
      "Aβ40 is actively destroyed by astrocytic ribosomes",
      "Aβ42 is completely resistant to all endocytosis"
    ],
    "answer": 0,
    "explain": "The C-terminus of Aβ42 terminates in Ala42 and Ile41. These two hydrophobic residues confer a much higher propensity to adopt an unstable beta-hairpin conformation that rapidly nucleates soluble oligomers, protofibrils, and insoluble cross-beta fibrillar plaques compared to the shorter, less hydrophobic Aβ40.",
    "example": "FAD mutations in APP and Presenilins selectively shift the cleavage ratio to increase relative production of Aβ42 over Aβ40."
  },
  {
    "id": "nd-010",
    "mode": "neurodegeneration",
    "level": 3,
    "type": "choice",
    "topic": "Braak Staging of Tau Pathology",
    "prompt": "In the neuropathological staging of Alzheimer's disease defined by Heiko and Eva Braak, Stages III and IV are characterized by tau tangles extending into:",
    "options": [
      "The limbic system (hippocampal formation, amygdala, and entorhinal cortex)",
      "Strictly the transentorhinal cortex without hippocampal involvement (clinically silent)",
      "The entire isocortex, including primary sensory and motor areas",
      "The spinal cord motor neurons"
    ],
    "answer": 0,
    "explain": "Braak stages I-II represent transentorhinal/entorhinal stages (usually asymptomatic). Stages III-IV represent the 'limbic stage', where neurofibrillary tangles involve the hippocampus, entorhinal cortex, and amygdala (typically corresponding to Mild Cognitive Impairment or early dementia). Stages V-VI represent widespread neocortical involvement.",
    "example": "Tau PET tracers (such as Flortaucipir) track Braak staging in living patients and correlate much more tightly with clinical cognitive decline than amyloid PET."
  },
  {
    "id": "nd-011",
    "mode": "neurodegeneration",
    "level": 3,
    "type": "choice",
    "topic": "Disease-Associated Microglia (DAM / MGnD)",
    "prompt": "During progression of amyloid pathology, microglia transition from a homeostatic state to the 'Disease-Associated Microglia' (DAM) phenotype. This transition is characterized by:",
    "options": [
      "Downregulation of homeostatic markers (P2ry12, Tmem119, Cx3cr1) and TREM2-dependent upregulation of lipid metabolism and phagocytic genes (Apoe, Clec7a, Trem2, Lpl)",
      "Complete apoptotic loss of all microglia in the cortex",
      "Conversion into mature oligodendrocytes that synthesize peripheral myelin",
      "Inhibition of all phagocytic activity toward amyloid fibrils"
    ],
    "answer": 0,
    "explain": "Keren-Shaul et al. (Cell 2017) discovered DAM (also termed MGnD by Butovsky). Homeostatic genes (P2ry12, Tmem119) are suppressed while lipid metabolism and phagocytic markers (Apoe, Clec7a, Trem2, Lpl, Cst7) are upregulated. Stage 1 DAM is TREM2-independent, while transition to full Stage 2 DAM requires functional TREM2-DAP12 signaling to compact amyloid plaques.",
    "example": "In Trem2-knockout AD mice, microglia fail to transition to Stage 2 DAM, leaving amyloid plaques diffuse, naked, and surrounded by exacerbated dystrophic neurites."
  },
  {
    "id": "nd-012",
    "mode": "neurodegeneration",
    "level": 3,
    "type": "choice",
    "topic": "TDP-43 Pathology in ALS and FTD",
    "prompt": "In the majority of sporadic ALS and tau-negative Frontotemporal Lobar Degeneration (FTLD-TDP) brains, the nuclear protein TDP-43 undergoes:",
    "options": [
      "Loss of normal nuclear localization (nuclear clearance) accompanied by accumulation of hyperphosphorylated, ubiquitinated cytoplasmic aggregates",
      "Overexpression inside the mitochondrial matrix causing Complex IV activation",
      "Direct secretion into the synaptic cleft as a monomeric neurotransmitter",
      "Conversion into extracellular amyloid plaques staining positive for Congo Red"
    ],
    "answer": 0,
    "explain": "Normally, TDP-43 resides in the nucleus where it binds UG-rich RNA to repress cryptic exons and regulate splicing. In disease, pathological post-translational modifications (phosphorylation at Ser409/410, C-terminal fragmentation) drive TDP-43 mislocalization into toxic cytoplasmic inclusions, causing dual loss of nuclear splicing function and cytoplasmic proteotoxicity.",
    "example": "Over 95% of all ALS cases and ~50% of all FTD cases exhibit prominent TDP-43 proteinopathy at autopsy."
  },
  {
    "id": "nd-013",
    "mode": "neurodegeneration",
    "level": 3,
    "type": "choice",
    "topic": "3R vs 4R Tauopathies",
    "prompt": "Alternative splicing of MAPT exon 10 determines the ratio of 3-repeat (3R) to 4-repeat (4R) tau isoforms. Which primary neurodegenerative diseases are classified as pure 4R tauopathies?",
    "options": [
      "Progressive Supranuclear Palsy (PSP) and Corticobasal Degeneration (CBD)",
      "Pick's disease",
      "Classic Alzheimer's disease",
      "Huntington's disease"
    ],
    "answer": 0,
    "explain": "Inclusion of exon 10 adds a fourth microtubule-binding repeat (4R tau). In healthy adult brains, 3R and 4R tau exist in an equimolar 1:1 ratio. Alzheimer's features both 3R and 4R. Progressive Supranuclear Palsy (PSP) and Corticobasal Degeneration (CBD) feature exclusive accumulation of 4R tau in neurons and glia (tufted astrocytes and astrocytic plaques), whereas Pick's disease is predominantly a 3R tauopathy.",
    "example": "Exon 10 splicing mutations in MAPT (such as +16 or Delta-280K) force exon 10 inclusion, producing pure 4R tau pathology in familial frontotemporal dementia."
  },
  {
    "id": "nd-014",
    "mode": "neurodegeneration",
    "level": 4,
    "type": "choice",
    "topic": "TDP-43 Loss of Function & Cryptic Exons",
    "prompt": "Recent landmark studies (Ling et al., Klim et al., Melamed et al.) demonstrated that loss of nuclear TDP-43 in ALS/FTD causes missplicing and incorporation of a premature stop codon-containing cryptic exon in which essential axonal outgrowth transcript?",
    "options": [
      "STMN2 (Stathmin-2)",
      "SNCA (Alpha-synuclein)",
      "MAP2",
      "GAP-43"
    ],
    "answer": 0,
    "explain": "TDP-43 normally binds a cryptic splice site in intron 1 of STMN2 (encoding Stathmin-2, a tubulin-binding protein critical for axonal outgrowth and regeneration). Loss of nuclear TDP-43 allows aberrant inclusion of a cryptic exon with a premature termination codon, triggering nonsense-mediated decay and depleting Stathmin-2 protein.",
    "example": "Restoring Stathmin-2 expression in human motor neurons lacking TDP-43 rescues axonal outgrowth and regeneration deficits."
  },
  {
    "id": "nd-015",
    "mode": "neurodegeneration",
    "level": 4,
    "type": "choice",
    "topic": "ApoE4-Mediated BBB Disruption",
    "prompt": "Berislav Zlokovic and colleagues demonstrated that APOE ε4 destabilizes the blood-brain barrier independently of amyloid by activating which inflammatory signaling cascade in capillary pericytes?",
    "options": [
      "The Cyclophilin A (CypA) - NF-kappaB - Matrix Metalloproteinase-9 (MMP-9) pathway",
      "The Notch1 - Hes1 transcriptional repressor cascade",
      "The JAK2 - STAT3 astrocytic differentiation axis",
      "The Wnt - beta-catenin survival pathway"
    ],
    "answer": 0,
    "explain": "ApoE3 and ApoE2 bind LRP1 on brain capillary pericytes to suppress the Cyclophilin A (CypA) pathway. In contrast, ApoE4 fails to suppress this cascade, causing hyperactivation of CypA, nuclear translocation of NF-κB, and secretion of MMP-9. MMP-9 enzymatically degrades endothelial tight junctions and basement membrane proteins, leading to microvascular leakage and neurovascular uncoupling.",
    "example": "Pharmacological inhibition of Cyclophilin A with Debio-025 rescues pericyte coverage and tight junction integrity in APOE4-targeted replacement mice."
  },
  {
    "id": "nd-016",
    "mode": "neurodegeneration",
    "level": 4,
    "type": "choice",
    "topic": "Cellular Senescence in the Aging Brain",
    "prompt": "Senescent glial cells that accumulate in the aging brain are characterized by irreversible cell cycle arrest driven by p16INK4a and secretion of a Senescence-Associated Secretory Phenotype (SASP) enriched in:",
    "options": [
      "Pro-inflammatory cytokines (IL-6, IL-1beta, TNF-alpha), chemokines (MCP-1), and matrix metalloproteinases",
      "Neurotrophic factors (BDNF, GDNF, NGF)",
      "Anti-inflammatory cytokines (IL-10, TGF-beta)",
      "High levels of acetylcholine and dopamine"
    ],
    "answer": 0,
    "explain": "Cellular senescence is accompanied by loss of nuclear Lamin B1, increased senescence-associated beta-galactosidase (SA-β-gal), and sustained production of the SASP. SASP factors (IL-6, IL-1β, TNF-α, MMPs) cause chronic low-grade neuroinflammation, degrade the extracellular matrix, and induce paracrine senescence in neighboring neurons and glia.",
    "example": "Clearing p16INK4a-positive senescent cells in MAPT P301S mice using senolytic drugs (Dasatinib + Quercetin) reduces tau phosphorylation and prevents brain atrophy."
  },
  {
    "id": "nd-017",
    "mode": "neurodegeneration",
    "level": 4,
    "type": "choice",
    "topic": "Soluble Oligomer Synaptotoxicity Receptors",
    "prompt": "Soluble Aβ oligomers (AβOs) trigger synaptotoxicity and LTP impairment by binding with nanomolar affinity to which postsynaptic receptors?",
    "options": [
      "Cellular Prion Protein (PrPC) and Leukocyte Immunoglobulin-Like Receptor B2 (LilrB2 / mouse PirB), which recruit Fyn kinase",
      "Voltage-gated sodium channels directly",
      "Dopamine D2 receptors strictly",
      "GABA-B receptors exclusively"
    ],
    "answer": 0,
    "explain": "Soluble Aβ oligomers (not insoluble fibril cores) bind Cellular Prion Protein (PrPC) and LilrB2/PirB at postsynaptic densities. This complex activates Fyn tyrosine kinase, which phosphorylates NMDA receptor GluN2B subunits, triggers cofilin dephosphorylation/rod formation, and drives excessive AMPA receptor endocytosis.",
    "example": "Ablation of Prnp or treatment with Fyn kinase inhibitors (such as saracatinib) blocks Aβ oligomer-mediated inhibition of hippocampal LTP in vitro."
  },
  {
    "id": "nd-018",
    "mode": "neurodegeneration",
    "level": 5,
    "type": "choice",
    "topic": "UNC13A Cryptic Exon Missplicing",
    "prompt": "In ALS and FTD, how do common non-coding risk variants in UNC13A identified by GWAS interact with nuclear TDP-43 loss of function?",
    "options": [
      "The risk SNPs reside in an intron and directly promote inclusion of a cryptic nonsense exon upon even partial TDP-43 nuclear depletion, drastically accelerating neurodegeneration",
      "The risk SNPs completely prevent transcription of tau protein",
      "The variants introduce a dominant gain-of-function mutation in the synaptic vesicle release machinery",
      "The SNPs prevent microglial activation entirely"
    ],
    "answer": 0,
    "explain": "Brown et al. and Ma et al. (Nature 2022) solved a decade-long genetic mystery: GWAS risk variants in UNC13A (rs12608932 and rs12973192) fall directly inside an unannotated intron. The risk alleles lower the affinity of TDP-43 binding to the region, drastically exacerbating cryptic exon inclusion and loss of UNC13A protein (critical for vesicle priming) when TDP-43 starts leaving the nucleus.",
    "example": "Patients homozygous for the UNC13A risk allele display significantly shorter survival times in both sporadic ALS and FTLD-TDP."
  },
  {
    "id": "nd-019",
    "mode": "neurodegeneration",
    "level": 5,
    "type": "choice",
    "topic": "Microglial Plaques Barrier Function",
    "prompt": "Multiphoton imaging in living Alzheimer's transgenic mice (Condello et al., Yuan et al.) demonstrated that the primary physiological function of microglial clustering around amyloid plaques is:",
    "options": [
      "Forming a protective physical barrier that compacts fibrillar amyloid and seals off neurotoxic soluble Aβ42 oligomers from damaging adjacent neuronal processes",
      "Phagocytosing and completely eliminating 100% of plaques from the parenchyma within 24 hours",
      "Secreting high concentrations of hydrogen peroxide to dissolve fibril cores",
      "Differentiating into pericytes to restore local capillary blood flow"
    ],
    "answer": 0,
    "explain": "Microglia do not simply clear established plaques; rather, through TREM2-dependent processes, they form a tight, insulating cellular halo around fibrillar amyloid cores. This barrier compacts diffuse amyloid and shields surrounding neurites from highly toxic soluble Aβ42 oligomers shedding from plaque surfaces. When microglial coverage fails, naked plaques induce severe axonal dystrophy and synaptic collapse.",
    "example": "Loss of TREM2 or microglial ablation converts compact, benign plaques into ragged, diffuse deposits exhibiting severe local axonal swelling and phospho-tau accumulation."
  },
  {
    "id": "nd-020",
    "mode": "neurodegeneration",
    "level": 5,
    "type": "choice",
    "topic": "LRRK2-Rab GTPase Phosphorylation Substrates",
    "prompt": "In Parkinson's disease, hyperactive LRRK2 kinase (e.g. G2019S, R1441C) selectively phosphorylates which conserved threonine/serine residue in the switch II domain of its downstream physiological substrates?",
    "options": [
      "Rab10 (at Thr73) and Rab8a (at Thr72), disrupting their binding to GDI and effector proteins",
      "Histone H2AX at Ser139",
      "Alpha-synuclein at Ser129 directly",
      "Tau at Thr231"
    ],
    "answer": 0,
    "explain": "Dario Alessi's group (Steger et al. eLife 2016) discovered that LRRK2 directly phosphorylates a specific subset of Rab GTPases (Rab10, Rab8a, Rab29) at a conserved site (Thr73 of Rab10, Thr72 of Rab8a) in their switch II domain. Hyperphosphorylation traps Rabs on intracellular membranes, blocking interaction with GDP-dissociation inhibitors (GDIs) and causing severe lysosomal trafficking and primary ciliogenesis deficits.",
    "example": "Measuring phospho-Thr73 Rab10 via mass spectrometry or specific monoclonal antibodies serves as the primary pharmacodynamic readout for clinical LRRK2 kinase inhibitors."
  },
  {
    "id": "nd-021",
    "mode": "neurodegeneration",
    "level": 2,
    "type": "choice",
    "topic": "Cerebral Amyloid Angiopathy (CAA)",
    "prompt": "Cerebral Amyloid Angiopathy (CAA) is present in up to 85-90% of Alzheimer's patients and is characterized by the preferential deposition of which peptide in the media and adventitia of cortical and leptomeningeal arteries?",
    "options": [
      "Aβ40 (the shorter, more soluble amyloid-beta peptide)",
      "Alpha-synuclein",
      "Transthyretin",
      "Prion protein Scrapie"
    ],
    "answer": 0,
    "explain": "While parenchymal senile plaques consist predominantly of Aβ42, vascular amyloid in CAA is composed overwhelmingly of Aβ40. Aβ40 drains along periarterial interstitial fluid pathways, depositing within vascular smooth muscle layers, causing vessel brittleness, microaneurysms, and lobar intracerebral hemorrhages.",
    "example": "T2*-gradient echo and susceptibility-weighted MRI (SWI) reveal cortical microbleeds strictly localized to lobar territories in patients with advanced CAA."
  },
  {
    "id": "nd-022",
    "mode": "neurodegeneration",
    "level": 3,
    "type": "choice",
    "topic": "Multiple System Atrophy (MSA) Pathology",
    "prompt": "Multiple System Atrophy (MSA) is an atypical alpha-synucleinopathy clinically characterized by parkinsonism, cerebellar ataxia, and autonomic failure, whose pathognomonic hallmark is:",
    "options": [
      "Glial Cytoplasmic Inclusions (GCIs, Papp-Lantos bodies) of alpha-synuclein inside mature oligodendrocytes",
      "Tau neurofibrillary tangles inside microglia",
      "Intranuclear beta-amyloid inclusions in astrocytes",
      "Loss of myelin basic protein without any proteinaceous aggregates"
    ],
    "answer": 0,
    "explain": "Unlike Parkinson's disease and Dementia with Lewy Bodies (where alpha-synuclein forms neuronal Lewy bodies), MSA is characterized by the accumulation of hyperphosphorylated alpha-synuclein inside oligodendrocytes as flame-shaped Glial Cytoplasmic Inclusions (GCIs), causing widespread primary demyelination and neurodegeneration.",
    "example": "Recent cryo-EM studies revealed that oligodendroglial alpha-synuclein filaments in MSA adopt an entirely different atomic conformation from neuronal Lewy body filaments."
  },
  {
    "id": "nd-023",
    "mode": "neurodegeneration",
    "level": 4,
    "type": "choice",
    "topic": "A1 vs A2 Reactive Astrocytes",
    "prompt": "Liddelow et al. (Nature 2017) demonstrated that 'A1' neurotoxic reactive astrocytes are induced in the presence of acute neuroinflammation when activated microglia simultaneously secrete which three factors?",
    "options": [
      "IL-1alpha, TNF-alpha, and C1q",
      "IL-4, IL-10, and TGF-beta",
      "BDNF, GDNF, and VEGF",
      "Acetylcholine, dopamine, and GABA"
    ],
    "answer": 0,
    "explain": "Microglia activated by systemic LPS or neurodegeneration secrete interleukin-1alpha (IL-1α), tumor necrosis factor-alpha (TNF-α), and complement component C1q. This specific cocktail converts resting astrocytes into neurotoxic 'A1' astrocytes, which upregulate complement component C3, lose normal synaptogenic and phagocytic functions, and secrete a lipid neurotoxin that kills axotomized neurons and oligodendrocytes.",
    "example": "A1 astrocytes marked by C3 immunoreactivity are abundantly present in post-mortem tissue from patients with Alzheimer's, Parkinson's, ALS, and MS."
  },
  {
    "id": "nd-024",
    "mode": "neurodegeneration",
    "level": 5,
    "type": "choice",
    "topic": "Lipid-Droplet-Accumulating Microglia (LDAM)",
    "prompt": "In the aging brain, a dysfunctional microglial state termed 'Lipid-Droplet-Accumulating Microglia' (LDAM, Marschallinger et al. Nature Neuroscience 2020) is characterized by:",
    "options": [
      "Accumulation of neutral lipid droplets, severe impairment in amyloid and apoptotic clearance, elevated basal ROS, and sustained secretion of pro-inflammatory cytokines",
      "Spontaneous differentiation into neural stem cells that repopulate the dentate gyrus",
      "Complete resistance to oxidative stress and enhanced phagocytosis",
      "Hypersecretion of nerve growth factor into the lateral ventricles"
    ],
    "answer": 0,
    "explain": "During physiological brain aging, ~50% of hippocampal microglia accumulate intracellular neutral lipid droplets (BODIPY-positive). These LDAM cells show marked transcriptional downregulation of phagocytosis machinery, defective clearance of Aβ and myelin debris, high baseline levels of lipid peroxidation and reactive oxygen species, and persistent secretion of neurotoxic factors.",
    "example": "Defective lipophagy and chronic exposure to lipid peroxidation products accelerate the transition of homeostatic microglia into the exhausted LDAM phenotype."
  },
  {
    "id": "nd-025",
    "mode": "neurodegeneration",
    "level": 2,
    "type": "choice",
    "topic": "Frontotemporal Dementia: Progranulin",
    "prompt": "Loss-of-function mutations in the Progranulin (GRN) gene cause familial Frontotemporal Lobar Degeneration (FTLD-TDP) via which pathogenic genetic mechanism?",
    "options": [
      "Haploinsufficiency leading to a ~50% reduction in secreted progranulin and severe lysosomal dysfunction",
      "Dominant gain-of-function aggregation of progranulin filaments",
      "Trinucleotide repeat expansion in exon 1",
      "Complete failure of mitochondrial ATP synthesis"
    ],
    "answer": 0,
    "explain": "Heterozygous nonsense, frameshift, or splice-site mutations in GRN lead to nonsense-mediated decay of the mutant transcript, causing progranulin haploinsufficiency. Progranulin is cleaved into granulin peptides in lysosomes; its deficiency causes lysosomal enzyme dysfunction, lipofuscinosis, and cytoplasmic TDP-43 aggregation.",
    "example": "Serum or plasma progranulin levels are reduced by >50% in asymptomatic carriers of GRN mutations, serving as an absolute predictive biomarker."
  },
  {
    "id": "nd-026",
    "mode": "neurodegeneration",
    "level": 3,
    "type": "choice",
    "topic": "Soluble TREM2 (sTREM2) in Biofluids",
    "prompt": "In human cerebrospinal fluid (CSF), soluble TREM2 (sTREM2) is generated by proteolytic cleavage of full-length cell-surface TREM2 by which sheddase enzyme?",
    "options": [
      "ADAM10 and ADAM17 (TACE)",
      "BACE1",
      "Gamma-secretase",
      "Caspase-1"
    ],
    "answer": 0,
    "explain": "Surface TREM2 undergoes ectodomain shedding mediated by the metalloproteases ADAM10 and ADAM17, releasing soluble sTREM2 into the interstitial fluid and CSF. In clinical cohorts, CSF sTREM2 peaks during early symptomatic stages of Alzheimer's disease, reflecting protective microglial activation and plaque engagement.",
    "example": "Elevated CSF sTREM2 in early AD correlates with slower cognitive decline and reduced future brain atrophy."
  },
  {
    "id": "nd-027",
    "mode": "neurodegeneration",
    "level": 4,
    "type": "choice",
    "topic": "Tau Acetylation Dynamics",
    "prompt": "In Alzheimer's disease and other tauopathies, pathological acetylation of tau at Lys280 and Lys174 (mediated by p300/CBP) promotes disease by:",
    "options": [
      "Directly impairing tau's ability to bind microtubules and preventing its degradation by the ubiquitin-proteasome system",
      "Targeting tau for instant lysosomal destruction",
      "Converting tau into an active tyrosine kinase",
      "Directing tau to the inner mitochondrial membrane"
    ],
    "answer": 0,
    "explain": "Min et al. and Cohen et al. demonstrated that acetylation of tau at Lys280 (within the second microtubule-binding repeat) neutralizes positive charges essential for tubulin interaction, causing tau detachment and promoting fibril formation. Acetylation also blocks polyubiquitination, preventing proteasomal clearance of toxic tau species.",
    "example": "SIRT1 is a histone/protein deacetylase that removes acetyl groups from tau; SIRT1 downregulation in aging brains exacerbates tau acetylation and accumulation."
  },
  {
    "id": "nd-028",
    "mode": "neurodegeneration",
    "level": 5,
    "type": "choice",
    "topic": "Asparagine Endopeptidase (AEP / Legumain) Cleavage",
    "prompt": "Keqiang Ye and colleagues demonstrated that age-dependent activation of the lysosomal cysteine protease Asparagine Endopeptidase (AEP / legumain) drives Alzheimer's pathogenesis by:",
    "options": [
      "Cleaving both Tau (at Asn368) and APP (at Asn585), generating highly fibrillogenic fragments that accelerate both amyloid and tau pathologies",
      "Selectively degrading alpha-synuclein into harmless monomers",
      "Synthesizing new myelin sheaths in aged axons",
      "Dephosphorylating NMDA receptors"
    ],
    "answer": 0,
    "explain": "With aging and acidosis, AEP translocates from lysosomes to the cytoplasm. AEP cleaves tau at Asn368, releasing a truncated tau(1-368) fragment that is exceptionally prone to hyperphosphorylation and aggregation. Simultaneously, AEP cleaves APP at Asn585, facilitating BACE1 cleavage and Aβ generation.",
    "example": "AEP-resistant Tau (N368A) knock-in mice exhibit marked reductions in neurofibrillary pathology and preserved cognitive function."
  },
  {
    "level": 1,
    "topic": "Amyloid Precursor Protein Cleavage Pathways",
    "prompt": "In the non-amyloidogenic pathway of APP processing, which enzyme cleaves within the A-beta domain, precluding the formation of intact neurotoxic A-beta peptide?",
    "options": [
      "Alpha-secretase (ADAM10)",
      "Beta-secretase (BACE1)",
      "Gamma-secretase complex",
      "Meprin beta"
    ],
    "answer": 0,
    "explain": "Alpha-secretase (predominantly ADAM10) cleaves APP between Lys16 and Leu17 of the A-beta sequence. This cleavage bisects the A-beta region, releasing neuroprotective soluble APP-alpha (sAPPalpha) and preventing toxic A-beta generation.",
    "example": "Upregulation of ADAM10 activity shifts APP processing away from amyloidogenic A-beta production in transgenic Alzheimer models.",
    "id": "nd-029",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Amyloidogenic Pathway Rate-Limiting Protease",
    "prompt": "Which aspartyl protease initiates the amyloidogenic cleavage of APP by cutting at the N-terminus of the A-beta sequence (between Met671 and Asp672)?",
    "options": [
      "Beta-site APP cleaving enzyme 1 (BACE1)",
      "ADAM17 / TACE",
      "Presenilin-1",
      "Cathepsin D"
    ],
    "answer": 0,
    "explain": "BACE1 is a membrane-bound aspartyl protease that cleaves APP at the Asp+1 site, liberating soluble APP-beta (sAPPbeta) and leaving the membrane-tethered 99-amino acid C-terminal fragment (C99 / CTF-beta).",
    "example": "BACE1 knockout mice are completely devoid of cerebral A-beta peptide production, demonstrating that BACE1 is the obligate beta-secretase in vivo.",
    "id": "nd-030",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Gamma-Secretase Complex Catalytic Core",
    "prompt": "The catalytic subunit responsible for intramembrane aspartyl protease cleavage within the gamma-secretase complex is:",
    "options": [
      "Presenilin (PSEN1 or PSEN2)",
      "Nicastrin",
      "Anterior pharynx-defective 1 (APH-1)",
      "Presenilin enhancer 2 (PEN-2)"
    ],
    "answer": 0,
    "explain": "Presenilin-1 (PSEN1) or Presenilin-2 (PSEN2) contains the two catalytic aspartate residues (Asp257 and Asp385 in PSEN1) within adjacent transmembrane domains that execute intramembrane water-dependent peptide bond hydrolysis.",
    "example": "Autosomal dominant missense mutations in PSEN1 are the most common cause of early-onset familial Alzheimer's disease.",
    "id": "nd-031",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "A-beta 42 vs A-beta 40 Pathogenicity",
    "prompt": "Why is the 42-amino acid amyloid-beta peptide (A-beta-42) significantly more neurotoxic than the shorter A-beta-40 isoform?",
    "options": [
      "The two additional hydrophobic amino acids (Ile41 and Ala42) dramatically accelerate oligomerization, nucleation, and fibril assembly kinetics",
      "A-beta-42 is an active serine protease that degrades cell membranes",
      "A-beta-42 cannot be cleared by microglia due to lack of charge",
      "A-beta-42 binds covalently to DNA to block transcription"
    ],
    "answer": 0,
    "explain": "The C-terminal hydrophobic residues (Ile41-Ala42) destabilize the random coil conformation and promote rapid transition into a beta-hairpin structure, lowering the critical nucleation barrier and accelerating assembly into toxic oligomers and fibrils.",
    "example": "Familial AD mutations invariably shift the A-beta-42/40 ratio toward the longer, highly aggregation-prone 42-residue peptide.",
    "id": "nd-032",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "APOE Alleles in Alzheimer's Disease Risk",
    "prompt": "Which apolipoprotein E (APOE) allele confers the greatest genetic risk for developing late-onset sporadic Alzheimer's disease?",
    "options": [
      "APOE epsilon 4 (APOE4)",
      "APOE epsilon 3 (APOE3)",
      "APOE epsilon 2 (APOE2)",
      "APOE epsilon 1 (APOE1)"
    ],
    "answer": 0,
    "explain": "APOE4 is the primary genetic risk factor for late-onset AD. Carrying one epsilon-4 allele increases lifetime risk ~3-4 fold, while homozygous epsilon-4/4 carriers face a 12-15 fold increase in risk and an earlier age of onset.",
    "example": "In contrast to APOE4, the rare APOE2 allele is neuroprotective, lowering AD risk and delaying the onset of cognitive decline.",
    "id": "nd-033",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Neurofibrillary Tangle Composition",
    "prompt": "Neurofibrillary tangles (NFTs), a cardinal histopathological hallmark of Alzheimer's disease, are intracellular aggregations composed of:",
    "options": [
      "Hyperphosphorylated microtubule-associated protein tau",
      "Misfolded alpha-synuclein filaments",
      "Beta-amyloid core fibrils",
      "Ubiquitinated Huntingtin polyglutamine tracts"
    ],
    "answer": 0,
    "explain": "NFTs are intraneuronal filamentous inclusions made of hyperphosphorylated tau. In healthy neurons, tau stabilizes axonal microtubules; hyperphosphorylation causes tau detachment, cytoplasmic mislocalization, and aggregation into paired helical filaments (PHFs).",
    "example": "The anatomical spread of neurofibrillary tangles across cortical circuits correlates closely with cognitive decline in Alzheimer's disease.",
    "id": "nd-034",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Braak Staging of Alzheimer's Tau Pathology",
    "prompt": "In the Braak staging scheme for Alzheimer's neurofibrillary pathology, where do the earliest neurofibrillary lesions consistently appear (Stages I-II)?",
    "options": [
      "Transentorhinal and entorhinal cortex",
      "Primary visual cortex (V1)",
      "Prefrontal cortex",
      "Cerebellar Purkinje cell layer"
    ],
    "answer": 0,
    "explain": "Braak Stages I-II (transentorhinal stages) are characterized by neurofibrillary lesions confined to the transentorhinal and entorhinal cortices. Stages III-IV spread into the hippocampus (limbic stages), and Stages V-VI invade extensive neocortical areas.",
    "example": "Tau-PET imaging using tracers like flortaucipir validates the transentorhinal-to-limbic progression pattern described by Heiko and Eva Braak.",
    "id": "nd-035",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Lewy Body Principal Protein Component",
    "prompt": "Lewy bodies and Lewy neurites, the pathological hallmarks of Parkinson's disease and Dementia with Lewy Bodies, are primarily composed of aggregated:",
    "options": [
      "Alpha-synuclein",
      "Beta-amyloid",
      "Tau protein",
      "TDP-43"
    ],
    "answer": 0,
    "explain": "Lewy bodies are round eosinophilic intracytoplasmic inclusions composed predominantly of aggregated alpha-synuclein, along with ubiquitin, p62/sequestosome-1, and neurofilament proteins.",
    "example": "Immunohistochemical staining for alpha-synuclein is the diagnostic gold standard for identifying Lewy body pathology in post-mortem brain tissue.",
    "id": "nd-036",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Alpha-Synuclein Pathological Phosphorylation",
    "prompt": "Within Lewy bodies, over 90% of aggregated alpha-synuclein is pathologically phosphorylated at which specific amino acid residue?",
    "options": [
      "Serine 129 (pS129)",
      "Threonine 181",
      "Tyrosine 39",
      "Serine 87"
    ],
    "answer": 0,
    "explain": "In healthy brain tissue, less than 4% of alpha-synuclein is phosphorylated. In Lewy bodies, >90% is phosphorylated at Ser129 by kinases like polo-like kinase 2 (PLK2) and casein kinase 2 (CK2), making pS129 the definitive diagnostic biomarker of synucleinopathy.",
    "example": "Antibodies specific for pS129-alpha-synuclein selectively stain pathological Lewy pathology while sparing normal physiological presynaptic alpha-synuclein.",
    "id": "nd-037",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Parkinson's Disease Cardinal Motor Symptoms",
    "prompt": "The clinical diagnosis of Parkinson's disease requires bradykinesia combined with which other classical motor sign?",
    "options": [
      "Rest tremor (4-6 Hz), muscular rigidity, or postural instability",
      "Chorea and athetosis",
      "Intention tremor during voluntary reaching",
      "Lower motor neuron fasciculations"
    ],
    "answer": 0,
    "explain": "Parkinsonian motor signs stem from the loss of dopaminergic neurons in the substantia nigra pars compacta. Diagnostic criteria mandate bradykinesia (slowness of movement) accompanied by rest tremor, cogwheel rigidity, or postural instability.",
    "example": "Clinical motor symptoms first manifest only after ~50-70% of substantia nigra dopamine neurons and ~80% of striatal dopamine terminals have degenerated.",
    "id": "nd-038",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "TDP-43 in ALS and FTD",
    "prompt": "TAR DNA-binding protein 43 (TDP-43) is the primary pathological aggregate protein found in over 95% of sporadic cases of which motor neuron disease?",
    "options": [
      "Amyotrophic lateral sclerosis (ALS)",
      "Huntington's disease",
      "Multiple sclerosis",
      "Spinocerebellar ataxia type 1"
    ],
    "answer": 0,
    "explain": "In 2006, Neumann et al. identified TDP-43 as the major pathological protein in both sporadic ALS and frontotemporal lobar degeneration with ubiquitin-positive inclusions (FTLD-TDP), establishing them as parts of a shared disease spectrum.",
    "example": "Pathological hallmark features include clearance of normal TDP-43 from the nucleus and formation of hyperphosphorylated, polyubiquitinated cytoplasmic inclusions.",
    "id": "nd-039",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "C9orf72 Hexanucleotide Repeat Expansion",
    "prompt": "The most common known genetic cause of both familial Amyotrophic Lateral Sclerosis (ALS) and Frontotemporal Dementia (FTD) is a GGGGCC repeat expansion in which gene?",
    "options": [
      "C9orf72",
      "SOD1",
      "TARDBP",
      "FUS"
    ],
    "answer": 0,
    "explain": "A massive hexanucleotide (GGGGCC / G4C2) repeat expansion in the non-coding first intron/promoter region of C9orf72 accounts for ~40% of familial ALS and ~25% of familial FTD cases.",
    "example": "Normal individuals have fewer than 20-30 hexanucleotide repeats, whereas affected patients carry hundreds to thousands of pathogenic GGGGCC repeats.",
    "id": "nd-040",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Huntington's Disease Triplet Repeat and Threshold",
    "prompt": "Huntington's disease is an autosomal dominant neurodegenerative disorder caused by an expanded CAG trinucleotide repeat in the HTT gene. Full penetrance occurs at repeat lengths of:",
    "options": [
      "40 repeats or greater",
      "10 to 20 repeats",
      "27 to 35 repeats",
      "Exactly 100 repeats"
    ],
    "answer": 0,
    "explain": "Normal individuals have 10-26 CAG repeats. Repeats between 27-35 are intermediate (unaffected but can expand in offspring); 36-39 show reduced penetrance; and 40 or more repeats confer full penetrance, with longer repeats correlating with earlier age of onset.",
    "example": "Juvenile Huntington's disease (Westphal variant) typically manifests in individuals with CAG repeat expansions exceeding 60 repeats.",
    "id": "nd-041",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Striatal Neuron Vulnerability in Huntington's",
    "prompt": "Which specific neuronal population in the striatum undergoes early and catastrophic neurodegeneration in Huntington's disease?",
    "options": [
      "GABAergic medium spiny projection neurons (MSNs)",
      "Choline acetyltransferase (ChAT)-positive giant interneurons",
      "Parvalbumin-positive fast-spiking interneurons",
      "Calretinin-positive GABAergic interneurons"
    ],
    "answer": 0,
    "explain": "GABAergic medium spiny neurons (MSNs), which constitute ~95% of striatal neurons, are selectively vulnerable to mutant huntingtin toxicity, particularly MSNs of the indirect pathway expressing dopamine D2 receptors and enkephalin.",
    "example": "Loss of indirect pathway MSNs disinhibits the external globus pallidus, leading to the uncontrolled choreiform motor movements characteristic of early HD.",
    "id": "nd-042",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Prion Protein (PrP) Conformational Conversion",
    "prompt": "The infectious etiology of transmissible spongiform encephalopathies (prion diseases) involves the conversion of normal host cellular prion protein (PrPC) into:",
    "options": [
      "A beta-sheet-rich, protease-resistant, self-propagating conformer termed PrPSc",
      "A truncated nuclear transcription factor",
      "An extracellular lipid bicelle",
      "A soluble monomeric alpha-helical peptide"
    ],
    "answer": 0,
    "explain": "Prusiner's 'protein-only' hypothesis demonstrated that PrPC (rich in alpha-helices and sensitive to proteinase K) converts into PrPSc (scrapie conformer), which adopts a predominantly beta-sheet architecture that resists protease digestion and autocatalytically seeds further PrPC misfolding.",
    "example": "Creutzfeldt-Jakob disease (CJD) tissue displays rapid, widespread spongiform vacuolation and astrogliosis driven by PrPSc propagation.",
    "id": "nd-043",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Multiple System Atrophy Glial Inclusions",
    "prompt": "Multiple System Atrophy (MSA) is distinguished from Parkinson's disease by the presence of alpha-synuclein-positive inclusions predominantly inside which cell type?",
    "options": [
      "Oligodendrocytes (forming Glial Cytoplasmic Inclusions / Papp-Lantos bodies)",
      "Astrocytes (forming Rosenthal fibers)",
      "Microglia (forming rod cells)",
      "Ependymal cells"
    ],
    "answer": 0,
    "explain": "Glial cytoplasmic inclusions (GCIs / Papp-Lantos bodies) located within oligodendrocytes are the defining diagnostic hallmark of MSA. Although oligodendrocytes express little endogenous alpha-synuclein in healthy brains, MSA oligodendrocytes accumulate massive, toxic alpha-synuclein fibrils.",
    "example": "Cryo-EM structures revealed that alpha-synuclein filaments from MSA patients have a unique structural fold distinct from Lewy body filaments in Parkinson's disease.",
    "id": "nd-044",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Progressive Supranuclear Palsy Hallmark Pathology",
    "prompt": "Progressive Supranuclear Palsy (PSP) is a classical 4R-tauopathy characterized neuropathologically by the presence of:",
    "options": [
      "Tufted astrocytes and globose neurofibrillary tangles composed of 4-repeat tau",
      "Pick bodies composed strictly of 3-repeat tau",
      "Lewy bodies in the cerebral cortex",
      "Amyloid plaques in the cerebellum"
    ],
    "answer": 0,
    "explain": "PSP is defined by tau inclusions containing exclusively 4 microtubule-binding repeats (4R tau). Characteristic lesions include tufted astrocytes in the motor cortex and striatum, coiled bodies in oligodendrocytes, and globose tangles in brainstem nuclei.",
    "example": "Clinically, PSP patients present with early postural instability, frequent backward falls, and a vertical supranuclear gaze palsy (inability to look down).",
    "id": "nd-045",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Pick's Disease Neuropathology",
    "prompt": "Pick's disease, a clinical subtype of frontotemporal dementia, is defined by frontotemporal lobar atrophy and round, silver-staining neuronal inclusions composed of:",
    "options": [
      "3-repeat (3R) tau isoforms devoid of exon 10",
      "4-repeat (4R) tau isoforms exclusively",
      "Aggregated TDP-43",
      "Polyglutamine huntingtin"
    ],
    "answer": 0,
    "explain": "Pick bodies are spherical, argyrophilic neuronal inclusions that lack Alzheimer-type paired helical filaments. Biochemical immunoblotting shows they consist almost exclusively of 3-repeat (3R) tau isoforms lacking exon 10.",
    "example": "Severe knife-edge gyral atrophy of the frontal and temporal poles with sparing of the precentral gyrus is pathognomonic for Pick's disease.",
    "id": "nd-046",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Glymphatic System and Sleep Clearance",
    "prompt": "The glymphatic system facilitates the convective clearance of interstitial waste products (such as A-beta and tau) from the brain parenchyma primarily during:",
    "options": [
      "Slow-wave (non-REM) deep sleep, when the interstitial space volume expands by ~60%",
      "High-intensity cardiovascular exercise",
      "Active daytime cognitive engagement",
      "Hyperventilation-induced respiratory alkalosis"
    ],
    "answer": 0,
    "explain": "Maiken Nedergaard's group showed that during slow-wave sleep, locus coeruleus noradrenergic tone declines, allowing interstitial space volume fraction to increase by over 60%. This drastically lowers hydraulic resistance, accelerating CSF-interstitial fluid bulk exchange.",
    "example": "Chronic sleep deprivation significantly reduces glymphatic clearance, driving accelerated accumulation of cortical A-beta and tau pathology.",
    "id": "nd-047",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Aquaporin-4 in Glymphatic Clearance",
    "prompt": "Convective cerebrospinal fluid-interstitial fluid exchange through the glymphatic pathway depends critically on which water channel polarized at astrocytic endfeet?",
    "options": [
      "Aquaporin-4 (AQP4)",
      "Aquaporin-1 (AQP1)",
      "Aquaporin-9 (AQP9)",
      "Glucose transporter 1 (GLUT1)"
    ],
    "answer": 0,
    "explain": "AQP4 is densely concentrated in the perivascular endfoot membranes of astrocytes encircling cerebral capillaries and arterioles. AQP4 channels provide low-resistance water conduits that facilitate macroscopic CSF influx and interstitial solute flushing.",
    "example": "Aqp4 knockout mice display an ~65% reduction in the parenchymal clearance of radiolabeled amyloid-beta.",
    "id": "nd-048",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Cellular Senescence Markers in Brain Aging",
    "prompt": "Senescent cells that accumulate in the aging and neurodegenerating brain are characterized by permanent cell-cycle arrest mediated by:",
    "options": [
      "Elevated expression of cyclin-dependent kinase inhibitors p16^INK4a (CDKN2A) and p21^CIP1 (CDKN1A)",
      "Constitutive activation of telomerase",
      "Downregulation of lysosomal beta-galactosidase",
      "Hyperactivation of mitochondrial respiration"
    ],
    "answer": 0,
    "explain": "Senescent cells permanently exit the cell cycle via induction of tumor suppressors p16^INK4a and p21^CIP1. They display senescence-associated beta-galactosidase (SA-beta-gal) activity and secrete a pro-inflammatory cocktail called the SASP.",
    "example": "Genetic clearance of p16-positive senescent cells using INK-ATTAC transgenic mice prevents tau aggregation and preserves cognitive function in tauopathy models.",
    "id": "nd-049",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Senescence-Associated Secretory Phenotype (SASP)",
    "prompt": "Senescent glia and endothelial cells damage surrounding healthy brain tissue by releasing the Senescence-Associated Secretory Phenotype (SASP), which consists of:",
    "options": [
      "Pro-inflammatory cytokines (IL-6, IL-1beta, TNF-alpha), chemokines, and matrix metalloproteinases (MMPs)",
      "Neurotrophic factors like BDNF and NGF exclusively",
      "Inhibitory neurotransmitters GABA and glycine",
      "Antioxidant enzymes superoxide dismutase and catalase"
    ],
    "answer": 0,
    "explain": "The SASP is an inflammatory secretome driven by persistent DNA damage response and NF-kappa-B activation. Senescent microglia and astrocytes secrete high levels of IL-6, IL-1beta, CXCL10, and MMPs, which degrade the extracellular matrix and spread senescence to bystander cells.",
    "example": "Senolytic therapies (e.g., dasatinib plus quercetin) selectively eliminate senescent cells, attenuating neuroinflammation and restoring hippocampal neurogenesis in aged mice.",
    "id": "nd-050",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Microglial TREM2 R47H Risk Variant",
    "prompt": "The rare R47H missense variant in Triggering Receptor Expressed on Myeloid Cells 2 (TREM2) confers a 2- to 4-fold increased risk of Alzheimer's disease by:",
    "options": [
      "Disrupting microglial recognition of lipid and apolipoprotein ligands, impairing microglial barrier formation around amyloid plaques",
      "Hyperactivating microglial phagocytosis to cause excessive destruction of healthy synapses",
      "Directly cleaving APP into toxic A-beta peptides",
      "Preventing microglial entry into the central nervous system during development"
    ],
    "answer": 0,
    "explain": "TREM2 binds anionic lipids, APOE, and A-beta oligomers. The R47H mutation resides in the extracellular immunoglobulin-like domain, crippling ligand binding. Consequently, microglia fail to polarize into disease-associated microglia (DAM) and cannot form a protective halo around plaques.",
    "example": "Without a compact microglial barrier, naked amyloid plaques shed toxic A-beta oligomers that inflict severe local synaptic and neuritic damage.",
    "id": "nd-051",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "SOD1 in Familial ALS",
    "prompt": "Mutations in Cu/Zn superoxide dismutase 1 (SOD1) cause familial ALS not through a loss of dismutase enzymatic activity, but via:",
    "options": [
      "A toxic gain-of-function associated with misfolding, non-native oligomerization, and aberrant oxidative chemistry",
      "Total depletion of copper from the brain",
      "Failure to degrade hydrogen peroxide",
      "Premature apoptosis of all sensory neurons"
    ],
    "answer": 0,
    "explain": "Over 180 mutations spanning the entire SOD1 polypeptide trigger structural destabilization and misfolding. Mutant SOD1 forms toxic aggregates, impairs axonal transport, jams the proteasome, and damages mitochondrial membranes via a toxic gain-of-function.",
    "example": "Sod1 knockout mice do not develop ALS, proving that loss of dismutase activity is not the pathogenic driver.",
    "id": "nd-052",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "FUS Nuclear Clearance in ALS/FTD",
    "prompt": "Fused in Sarcoma (FUS) is an RNA-binding protein that causes severe familial ALS when mutations in its nuclear localization signal (NLS) lead to:",
    "options": [
      "Failure of Transportin-1-mediated nuclear import, resulting in cytoplasmic accumulation and aberrant phase transition into liquid/solid aggregates",
      "Constitutive transcription of oncogenes",
      "Loss of ribonuclease activity inside lysosomes",
      "Disruption of the inner mitochondrial electron transport chain"
    ],
    "answer": 0,
    "explain": "FUS has an extreme C-terminal non-canonical PY-NLS recognized by Transportin-1 (Karyopherin-beta2). Mutations in this region (e.g., P525L, R521C) prevent nuclear import. The resulting cytoplasmic FUS phase-separates into stress granules that convert into pathological fibrillar inclusions.",
    "example": "FUS mutations causing the most severe nuclear import defects (such as P525L) result in highly aggressive juvenile-onset ALS.",
    "id": "nd-053",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Friedreich's Ataxia GAA Triplet Expansion",
    "prompt": "Friedreich's ataxia is an autosomal recessive neurodegenerative disorder caused by a GAA triplet repeat expansion in intron 1 of the FXN gene, resulting in:",
    "options": [
      "Transcriptional silencing of frataxin, causing mitochondrial iron accumulation and iron-sulfur cluster assembly failure",
      "Production of a toxic polyalanine peptide",
      "Premature degradation of mitochondrial DNA",
      "Constitutive activation of voltage-gated calcium channels"
    ],
    "answer": 0,
    "explain": "The GAA repeat forms sticky triplex DNA and R-loop structures that recruit repressive chromatin marks, silencing frataxin transcription. Frataxin is an essential mitochondrial chaperone for iron-sulfur (Fe-S) cluster assembly; its loss causes mitochondrial iron overload and oxidative stress.",
    "example": "Patients suffer from progressive sensory ataxia, loss of deep tendon reflexes, hypertrophic cardiomyopathy, and diabetes mellitus.",
    "id": "nd-054",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Spinocerebellar Ataxia Type 1 (SCA1) Ataxin-1 Expansion",
    "prompt": "Spinocerebellar Ataxia Type 1 (SCA1) is an autosomal dominant polyglutamine disease characterized by Purkinje cell loss caused by CAG expansion in the gene encoding:",
    "options": [
      "Ataxin-1 (ATXN1)",
      "Ataxin-3 (ATXN3)",
      "Huntingtin (HTT)",
      "Androgen receptor (AR)"
    ],
    "answer": 0,
    "explain": "SCA1 is caused by a polyglutamine (polyQ) tract expansion in Ataxin-1. Expanded Ataxin-1 accumulates in cerebellar Purkinje cell nuclei, where phosphorylation at Ser776 by PKA regulates its incorporation into toxic transcriptional repressor complexes with Capicua (CIC).",
    "example": "Mutating Ser776 to alanine in SCA1 transgenic mice completely abolishes neurodegeneration despite the presence of the expanded polyglutamine tract.",
    "id": "nd-055",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Dementia with Lewy Bodies vs Parkinson's Disease Dementia",
    "prompt": "Clinically, Dementia with Lewy Bodies (DLB) is distinguished from Parkinson's Disease Dementia (PDD) using the 'one-year rule', which dictates that:",
    "options": [
      "In DLB, cognitive impairment and dementia precede or develop within one year of the onset of parkinsonian motor signs; in PDD, dementia occurs well after established motor disease",
      "DLB lasts only one year before remission",
      "DLB patients never experience motor symptoms",
      "PDD patients respond exclusively to acetylcholinesterase inhibitors"
    ],
    "answer": 0,
    "explain": "The consensus 'one-year rule' states that if dementia occurs before or concurrently with motor parkinsonism (or within 12 months), the diagnosis is Dementia with Lewy Bodies. If motor symptoms are established for more than a year before cognitive decline emerges, it is classified as Parkinson's Disease Dementia.",
    "example": "DLB is clinically characterized by visual hallucinations, marked cognitive fluctuations in attention/alertness, and REM sleep behavior disorder.",
    "id": "nd-056",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "BACE1 Cleavage Specificity and Substrates",
    "prompt": "Beyond APP, BACE1 cleaves several critical physiological substrates in the nervous system, including which transmembrane protein essential for axonal myelination?",
    "options": [
      "Neuregulin-1 (NRG1)",
      "Myelin basic protein (MBP)",
      "Proteolipid protein 1 (PLP1)",
      "Contactin-1"
    ],
    "answer": 0,
    "explain": "BACE1 processes the 'stalk' region of type I and type III Neuregulin-1 (NRG1). NRG1 cleavage exposes an EGF-like signaling domain that binds ErbB receptor tyrosine kinases on Schwann cells and oligodendrocytes to dictate myelin sheath thickness.",
    "example": "Pharmacological BACE1 inhibitors tested in clinical trials caused unexpected hypomyelination and motor coordination side effects partly due to off-target inhibition of NRG1 processing.",
    "id": "nd-057",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Nicastrin Molecular Ruler Function",
    "prompt": "Within the tetrameric gamma-secretase complex, the heavily glycosylated subunit Nicastrin functions primarily as:",
    "options": [
      "A substrate receptor that binds the free N-terminus of ectodomain-cleaved substrates (C99 and C83) via a conserved DAP domain",
      "The catalytic intramembrane aspartyl protease core",
      "A proton channel that acidifies the complex lumen",
      "An anchor tethering the complex to the actin cytoskeleton"
    ],
    "answer": 0,
    "explain": "Nicastrin possesses an extracellular domain containing a conserved DYIGS/DAP motif. It acts as a 'molecular ruler' that recognizes and binds the newly formed amino-terminal stubs of substrates generated by prior alpha- or beta-secretase shedding, guiding them to the presenilin catalytic pore.",
    "example": "Substrates with large intact ectodomains sterically clash with Nicastrin, preventing premature cleavage of full-length APP.",
    "id": "nd-058",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Carboxy-Terminal Fragments: C99 vs C83",
    "prompt": "Cleavage of APP by BACE1 and ADAM10 yields membrane-tethered C-terminal fragments designated C99 and C83, respectively. Subsequent gamma-secretase cleavage of C83 produces:",
    "options": [
      "p3 peptide (A-beta 17-40 or 17-42) and APP intracellular domain (AICD)",
      "Full-length A-beta 1-42",
      "Soluble APP-beta",
      "Prion-like amyloid fibrils"
    ],
    "answer": 0,
    "explain": "Because alpha-secretase cuts between Lys16 and Leu17, the remaining C-terminal stub (C83) is cleaved by gamma-secretase to yield the non-amyloidogenic 'p3' peptide and the APP intracellular domain (AICD). In contrast, gamma-cleavage of C99 yields intact A-beta and AICD.",
    "example": "In Alzheimer's cerebrospinal fluid, elevated C99-derived A-beta fragments reflect increased amyloidogenic flux relative to p3.",
    "id": "nd-059",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Sequential Carboxypeptidase Cleavage by Gamma-Secretase",
    "prompt": "Gamma-secretase processes C99 through sequential, processive tri- and tetrapeptide trimming steps following initial endopeptidase cleavage at the cytoplasmic membrane boundary. The primary pathway generating A-beta-42 proceeds along:",
    "options": [
      "C99 -> A-beta 49 -> A-beta 46 -> A-beta 43 -> A-beta 42",
      "C99 -> A-beta 48 -> A-beta 45 -> A-beta 42 -> A-beta 39",
      "C99 -> A-beta 40 -> A-beta 42 directly",
      "C99 -> A-beta 55 -> A-beta 42 in a single cut"
    ],
    "answer": 0,
    "explain": "Gamma-secretase cleaves C99 at either the epsilon-site 49 or 48. Cleavage at Thr48 initiates the 48 -> 45 -> 42 -> 38 product line. Familial Alzheimer's mutations in PSEN1 cause premature substrate dissociation from presenilin, halting trimming at A-beta-42 instead of trimming further to benign A-beta-38.",
    "example": "Gamma-secretase modulators (GSMs) do not inhibit the enzyme but enhance processivity, shifting cleavage to complete trimming into short, soluble A-beta-38 and A-beta-37 peptides.",
    "id": "nd-060",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "A-beta Oligomer Synaptotoxicity Receptors",
    "prompt": "Soluble A-beta oligomers disrupt synaptic transmission and drive spine loss by binding as high-affinity ligands to which cell-surface receptor complex?",
    "options": [
      "Cellular prion protein (PrPC) coupled to metabotropic glutamate receptor 5 (mGluR5)",
      "GABAA receptor beta-3 subunits",
      "Dopamine D1 receptors",
      "Voltage-gated potassium channels Kv1.2"
    ],
    "answer": 0,
    "explain": "Soluble A-beta oligomers bind with high nanomolar affinity to the N-terminal polybasic domain of cellular prion protein (PrPC). PrPC acts as a scaffold that recruits mGluR5, activating Fyn tyrosine kinase, which phosphorylates GluN2B to cause excitotoxic Ca2+ deregulation and AMPA receptor endocytosis.",
    "example": "Antibodies blocking the PrPC/mGluR5 interaction rescue synaptic plasticity and prevent memory loss in Alzheimer transgenic mouse models.",
    "id": "nd-061",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "APOE4 Blood-Brain Barrier Pericyte Toxicity",
    "prompt": "APOE4 accelerates neurodegeneration independently of A-beta clearance by triggering blood-brain barrier breakdown through which signaling pathway in pericytes?",
    "options": [
      "Binding LRP1 to activate the Cyclophilin A - NF-kappa-B - Matrix Metalloproteinase 9 (MMP-9) pathway, degrading tight junction proteins",
      "Directly phosphorylating claudin-5 to dissolve endothelial junctions",
      "Cleaving astrocytic aquaporin-4 channels",
      "Inhibiting endothelial glucose transporter GLUT1 completely"
    ],
    "answer": 0,
    "explain": "In pericytes, APOE3 suppresses the pro-inflammatory Cyclophilin A (CypA) pathway via LRP1. APOE4 fails to suppress this cascade, causing unchecked CypA-NF-kappa-B signaling that upregulates MMP-9. Secreted MMP-9 degrades endothelial tight junctions and basement membranes, leaking neurotoxins into the parenchyma.",
    "example": "Post-mortem and dynamic contrast MRI studies confirm that APOE4 carriers exhibit widespread microvascular pericyte degeneration and early blood-brain barrier breakdown.",
    "id": "nd-062",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Microglial Disease-Associated Microglia (DAM) Phenotype",
    "prompt": "Single-cell RNA sequencing of microglia surrounding amyloid plaques identified the transition into 'Disease-Associated Microglia' (DAM), characterized by:",
    "options": [
      "Downregulation of homeostatic markers (P2ry12, Tmem119, Cx3cr1) and upregulation of lipid metabolism and phagocytic genes (Trem2, Apoe, Clec7a, Spp1)",
      "Exclusive upregulation of resting potassium channels",
      "Total loss of lysosomal enzymes and cessation of phagocytosis",
      "Differentiation into mature oligodendrocytes"
    ],
    "answer": 0,
    "explain": "Under chronic plaque pathology, microglia transition from a homeostatic state to a DAM (or neurodegenerative 'MGnD') phenotype in a two-step process: a Trem2-independent initial step followed by a Trem2-dependent program that activates Apoe, Lpl, Cst7, and Clec7a to clear lipid debris.",
    "example": "Mice lacking Trem2 stall at the intermediate DAM stage and fail to fully upregulate protective plaque-compacting phagocytic programs.",
    "id": "nd-063",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Tau Alternative Splicing: 3R vs 4R Isoforms",
    "prompt": "Alternative splicing of exon 10 in the human MAPT gene generates tau isoforms with either three or four microtubule-binding repeats (3R or 4R tau). In the healthy adult human brain, the ratio of 3R to 4R tau is approximately:",
    "options": [
      "1:1",
      "10:1 (predominantly 3R)",
      "1:10 (predominantly 4R)",
      "Zero 3R tau is expressed in adulthood"
    ],
    "answer": 0,
    "explain": "Alternative splicing of exon 10 (which encodes the second 31-amino-acid microtubule-binding repeat) produces equal amounts of 3R and 4R tau (~1:1 ratio) in the healthy human adult brain. Disrupting this balance is sufficient to drive neurodegeneration.",
    "example": "Intronic mutations near the 5' splice site of exon 10 increase exon 10 inclusion, causing familial frontotemporal dementia with parkinsonism linked to chromosome 17 (FTDP-17).",
    "id": "nd-064",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Fluid Biomarkers: Phospho-Tau Sites",
    "prompt": "Which blood plasma biomarker has demonstrated exceptional diagnostic accuracy, rising during early preclinical stages of Alzheimer's disease before tau-PET scans become positive?",
    "options": [
      "Phospho-tau217 (p-tau217)",
      "Total alpha-synuclein",
      "Glial fibrillary acidic protein (GFAP) exclusively",
      "Dopamine beta-hydroxylase"
    ],
    "answer": 0,
    "explain": "Plasma p-tau217 (and p-tau181/231) rises in response to cortical amyloid plaque deposition, even before substantial tau tangles form. High-precision mass spectrometry assays for plasma p-tau217 achieve >95% accuracy in distinguishing AD from other neurodegenerative dementias.",
    "example": "Clinical trials for anti-amyloid monoclonal antibodies use plasma p-tau217 as a rapid, accessible screening tool to identify eligible amyloid-positive patients.",
    "id": "nd-065",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Braak Lewy Body Staging Hypothesis",
    "prompt": "According to the Braak hypothesis for Parkinson's disease, sporadic Lewy pathology originates outside the motor system, first appearing in which two anatomical locations?",
    "options": [
      "The dorsal motor nucleus of the vagus nerve (brainstem) and the anterior olfactory nucleus / olfactory bulb",
      "The substantia nigra pars compacta and subthalamic nucleus",
      "The dentate gyrus of the hippocampus and entorhinal cortex",
      "The primary motor cortex and internal capsule"
    ],
    "answer": 0,
    "explain": "Braak Stages 1-2 propose that Lewy pathology enters the central nervous system via retrograde axonal transport from the enteric nervous system along the vagus nerve (dorsal motor nucleus) and via nasal inhalation (olfactory bulb), explaining early anosmia and gastrointestinal constipation.",
    "example": "Pathology ascends in Stage 3 to the substantia nigra, producing classic motor symptoms, before spreading to limbic (Stage 4) and neocortical areas (Stages 5-6).",
    "id": "nd-066",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Alpha-Synuclein Seeding and LAG3 Receptor",
    "prompt": "Exogenous alpha-synuclein pre-formed fibrils (PFFs) enter recipient neurons to template endogenous alpha-synuclein aggregation primarily by binding to which cell-surface receptor?",
    "options": [
      "Lymphocyte activation gene 3 (LAG3)",
      "Transferrin receptor 1 (TfR1)",
      "Insulin-like growth factor receptor 1 (IGF-1R)",
      "Cannabinoid receptor 2 (CB2)"
    ],
    "answer": 0,
    "explain": "LAG3 binds alpha-synuclein fibrils with high affinity (Kd ~77 nM) through its extracellular domain. Binding triggers endocytosis of the fibrils into recipient neurons, where they escape lysosomes and seed recruitment of soluble endogenous alpha-synuclein into insoluble Lewy pathology.",
    "example": "Genetic deletion or antibody blockade of LAG3 significantly reduces PFF transmission and preserves dopaminergic neuron survival in mouse seeding models.",
    "id": "nd-067",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "SNCA Gene Dosage Effects",
    "prompt": "Genomic triplication of the wild-type SNCA locus (encoding alpha-synuclein) leads to which clinical phenotype compared to SNCA duplication?",
    "options": [
      "A markedly earlier age of onset (often in the 30s) and rapid progression to severe Parkinson's disease dementia with prominent autonomic failure",
      "Complete resistance to neurodegeneration due to gene buffering",
      "A pure choreiform disorder identical to Huntington's disease",
      "Isolated sensory neuropathy with normal motor function"
    ],
    "answer": 0,
    "explain": "SNCA triplication produces a 2-fold increase in wild-type alpha-synuclein protein levels (4 copies of the gene), resulting in highly aggressive early-onset parkinsonism and rapid-onset dementia. SNCA duplication (3 copies) produces typical late-onset sporadic-like Parkinson's disease.",
    "example": "This direct gene-dosage effect proves that elevated concentration of unmutated wild-type alpha-synuclein is sufficient to cause fulminant neurodegeneration.",
    "id": "nd-068",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "TDP-43 Nuclear Clearance and Cryptic Exon Splicing",
    "prompt": "When nuclear TDP-43 is depleted in motor neurons, what is the primary consequence on RNA processing that triggers axonal dysfunction?",
    "options": [
      "Unrepressed inclusion of non-conserved 'cryptic exons' that introduce premature termination codons, causing nonsense-mediated decay of essential transcripts like STMN2 and UNC13A",
      "Complete cessation of all RNA polymerase II transcription",
      "Failure to splice out constitutive introns across all ribosomal protein genes",
      "Over-expression of histone deacetylases"
    ],
    "answer": 0,
    "explain": "A major normal function of nuclear TDP-43 is binding UG-rich repeats to suppress cryptic exons. When TDP-43 mislocalizes to cytoplasmic aggregates, cryptic exons are aberrantly spliced into stathmin-2 (STMN2, necessary for microtubule regeneration) and UNC13A (critical for presynaptic vesicle priming), destroying both proteins.",
    "example": "Restoring full-length STMN2 expression in TDP-43-depleted motor neurons rescues axonal regrowth and neuromuscular junction innervation.",
    "id": "nd-069",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "RAN Translation of C9orf72 Dipeptide Repeats",
    "prompt": "The GGGGCC repeat expansion in C9orf72 undergoes Repeat-Associated Non-AUG (RAN) translation across all reading frames, generating which five dipeptide repeat (DPR) proteins?",
    "options": [
      "Poly-GA, Poly-GP, Poly-GR, Poly-PA, and Poly-PR",
      "Poly-glutamine, Poly-alanine, Poly-serine, Poly-threonine, and Poly-glycine",
      "Poly-lysine, Poly-arginine, Poly-histidine, Poly-aspartate, and Poly-glutamate",
      "Poly-methionine repeats exclusively"
    ],
    "answer": 0,
    "explain": "Bidirectional RAN translation of sense (GGGGCC) and antisense (GGCCCC) transcripts generates five distinct dipeptide repeat species: poly-glycine-alanine (poly-GA), poly-glycine-proline (poly-GP), poly-glycine-arginine (poly-GR), poly-proline-alanine (poly-PA), and poly-proline-arginine (poly-PR).",
    "example": "The basic arginine-rich DPRs (poly-GR and poly-PR) are exceptionally neurotoxic, binding to RNA and nucleoporins to paralyze nucleocytoplasmic transport.",
    "id": "nd-070",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Huntingtin Cleavage and Toxic N-Terminal Fragments",
    "prompt": "Proteolytic cleavage of full-length mutant huntingtin (mHTT) by which specific cysteine protease liberates short, highly aggregation-prone N-terminal fragments containing the expanded polyglutamine tract?",
    "options": [
      "Caspase-6 (cleaving at Asp586)",
      "Granzyme B",
      "Secretase gamma",
      "Presenilin-1"
    ],
    "answer": 0,
    "explain": "Caspase-6 cleaves mHTT at Asp586, releasing an N-terminal fragment that enters the nucleus and forms toxic nuclear inclusions. Cleavage by calpains also generates small N-terminal exon-1-like fragments that drive severe toxicity.",
    "example": "Mice expressing a mutant huntingtin construct with a mutated caspase-6 cleavage site (Caspase-6-resistant mHTT) are completely protected against striatal neurodegeneration.",
    "id": "nd-071",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Rhes Striatal Specificity in Huntington's Disease",
    "prompt": "The striatum-specific small G-protein Rhes (Ras homolog enriched in striatum) accounts for the selective striatal vulnerability in Huntington's disease by:",
    "options": [
      "Binding mutant huntingtin and acting as an E3 ligase for SUMO-1, sumoylating mHTT to promote its soluble monomeric toxicity",
      "Phosphorylating dopamine D2 receptors to prevent their activation",
      "Degrading BDNF in striatal projection neurons",
      "Inactivating complex IV in mitochondria"
    ],
    "answer": 0,
    "explain": "Rhes is selectively enriched in the striatum. It physically interacts with mutant huntingtin and acts as a SUMO E3 ligase, sumoylating mHTT. While insoluble mHTT aggregates are somewhat protective, sumoylation keeps mHTT in a toxic soluble monomeric/oligomeric conformation.",
    "example": "Genetic depletion of Rhes in Huntington's mouse models dramatically reduces striatal atrophy and motor deficits without changing mHTT expression.",
    "id": "nd-072",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Non-Cell-Autonomous Toxicity in ALS",
    "prompt": "Chimeric and cell-type-specific conditional knockout experiments in SOD1 mouse models have demonstrated that motor neuron death is non-cell-autonomous, meaning that:",
    "options": [
      "Mutant SOD1 expression inside motor neurons dictates disease onset, but expression in reactive astrocytes and microglia accelerates disease progression and death",
      "Motor neurons die strictly from peripheral muscle damage with zero spinal involvement",
      "Astrocytes remain completely healthy throughout the disease course",
      "Microglia are the sole cell type that undergoes degeneration"
    ],
    "answer": 0,
    "explain": "Pioneering studies by Cleveland and colleagues using Cre-lox mice showed that selectively removing mutant SOD1 from astrocytes or microglia significantly slowed disease progression and extended survival, demonstrating that glial neuroinflammation actively drives motor neuron demise.",
    "example": "Astrocytes differentiated from ALS patient iPSCs secrete toxic soluble factors that selectively kill healthy primary motor neurons in co-culture.",
    "id": "nd-073",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cerebral Amyloid Angiopathy (CAA) and ARIA",
    "prompt": "Cerebral Amyloid Angiopathy (CAA) involves the pathological deposition of amyloid-beta in which anatomical structure, predisposing patients to amyloid-related imaging abnormalities (ARIA)?",
    "options": [
      "The tunica media and adventitia of small to medium-sized cerebral and leptomeningeal arteries",
      "The lumen of major dural venous sinuses",
      "The ependymal lining of the lateral ventricles",
      "The perineuronal nets surrounding parvalbumin interneurons"
    ],
    "answer": 0,
    "explain": "In CAA, A-beta (predominantly A-beta-40) accumulates in the walls of cortical and leptomeningeal arteries, replacing smooth muscle cells and weakening vascular integrity. When anti-amyloid antibodies (e.g., lecanemab) mobilize vascular amyloid, patients can develop vasogenic edema (ARIA-E) or microhemorrhages (ARIA-H).",
    "example": "Lobar intracerebral hemorrhages in elderly non-hypertensive patients are classic clinical presentations of severe cerebral amyloid angiopathy.",
    "id": "nd-074",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "LATE: Limbic-predominant Age-related TDP-43 Encephalopathy",
    "prompt": "Limbic-predominant Age-related TDP-43 Encephalopathy (LATE) is an under-recognized dementia of the very old (>80 years) that mimics Alzheimer's clinical symptoms but is characterized neuropathologically by:",
    "options": [
      "TDP-43 proteinopathy in the amygdala, hippocampus, and middle frontal gyrus, often with hippocampal sclerosis, without significant A-beta plaques",
      "Extensive alpha-synuclein deposition across the cerebellum",
      "Pure 3-repeat tau tangles in the occipital lobe",
      "Spongiform encephalopathy caused by infectious prions"
    ],
    "answer": 0,
    "explain": "Defined in 2019, LATE affects up to 25% of individuals over age 85. It causes amnestic dementia mimicking AD, but autopsy reveals stereotypic stereociliary spread of phosphorylated TDP-43: Stage 1 (amygdala), Stage 2 (hippocampus), and Stage 3 (middle frontal gyrus).",
    "example": "LATE frequently co-exists with Alzheimer's pathology; patients with both A-beta/tau and TDP-43 exhibit significantly more rapid cognitive decline.",
    "id": "nd-075",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Corticobasal Degeneration Neuropathology",
    "prompt": "Corticobasal Degeneration (CBD) is a 4R-tauopathy distinguished neuropathologically from Progressive Supranuclear Palsy (PSP) by the presence of:",
    "options": [
      "Astrocytic plaques (annular tau clusters in distal astrocytic processes) and ballooned achromatic neurons",
      "Tufted astrocytes with proximal branching",
      "Spherical Pick bodies in the dentate gyrus",
      "Glial cytoplasmic inclusions in oligodendrocytes"
    ],
    "answer": 0,
    "explain": "CBD is defined by 'astrocytic plaques'—ring-like clusters of phosphorylated 4R-tau in the distal bush-like processes of astrocytes—along with ballooned, achromatic neurons (swollen with phosphorylated neurofilaments) in the frontoparietal cortex.",
    "example": "Clinically, CBD presents with asymmetric parkinsonism, limb apraxia, cortical sensory loss, and the 'alien limb' phenomenon.",
    "id": "nd-076",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Frontotemporal Lobar Degeneration Subtypes",
    "prompt": "Frontotemporal lobar degeneration (FTLD) is classified neuropathologically into three mutually exclusive molecular subgroups based on the predominant aggregate protein:",
    "options": [
      "FTLD-tau (~45%), FTLD-TDP (~50%), and FTLD-FUS (~5%)",
      "FTLD-amyloid, FTLD-synuclein, and FTLD-prion",
      "FTLD-dopamine, FTLD-serotonin, and FTLD-GABA",
      "FTLD-collagen, FTLD-elastin, and FTLD-laminin"
    ],
    "answer": 0,
    "explain": "FTLD cases are divided into FTLD-tau (Pick's, PSP, CBD, MAPT mutations), FTLD-TDP (C9orf72, GRN mutations, sporadic TDP-43), and rare FTLD-FUS (inclusions of FUS and other FET proteins), which together account for >98% of cases.",
    "example": "Mutations in Progranulin (GRN) cause haploinsufficiency, resulting in FTLD-TDP with ubiquitin- and p62-positive neuronal inclusions.",
    "id": "nd-077",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Progranulin (GRN) Haploinsufficiency Mechanism",
    "prompt": "Loss-of-function mutations in the Progranulin (GRN) gene cause frontotemporal lobar degeneration (FTLD-TDP) primarily through which pathogenic cellular mechanism?",
    "options": [
      "Lysosomal dysfunction and impaired protein degradation resulting from haploinsufficiency of progranulin/granulin peptides",
      "Excessive production of beta-amyloid peptides",
      "Direct inhibition of RNA polymerase II transcription",
      "Premature fusion of synaptic vesicles with the plasma membrane"
    ],
    "answer": 0,
    "explain": "Progranulin is a glycoprotein transported to lysosomes, where it is cleaved into functional granulin peptides that regulate lysosomal proteases (e.g., Cathepsin D) and lipid metabolism. GRN haploinsufficiency cripples lysosomal clearance, driving TDP-43 cytoplasmic accumulation.",
    "example": "Homozygous null mutations in GRN cause a completely different disease: neuronal ceroid lipofuscinosis (NCL11), a severe lysosomal storage disorder.",
    "id": "nd-078",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Subcortical Ischemic Vascular Dementia (Binswanger's Disease)",
    "prompt": "Subcortical ischemic vascular dementia (Binswanger's disease) is characterized neuropathologically by severe arteriolosclerosis of deep penetrating cerebral arteries, resulting in:",
    "options": [
      "Diffuse, confluent white matter rarefaction, demyelination, and multiple lacunar infarcts in the basal ganglia and centrum semiovale",
      "Extensive lobar hemorrhages localized to the occipital pole",
      "Selective degeneration of cerebellar Purkinje cells with intact white matter",
      "Calcification of the choroid plexus exclusively"
    ],
    "answer": 0,
    "explain": "Chronic systemic hypertension and arteriolosclerosis cause thickening of the walls and luminal narrowing of deep penetrating lenticulostriate and medullary arteries. This leads to chronic hypoperfusion, extensive white matter rarefaction (leukoaraiosis), loss of myelin and oligodendrocytes, and scattered lacunar infarcts.",
    "example": "On T2-weighted and FLAIR brain MRI, Binswanger's disease appears as bilateral, symmetrical hyperintensities spanning the periventricular and deep white matter.",
    "id": "nd-079",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Idiopathic Basal Ganglia Calcification (Fahr's Disease)",
    "prompt": "Idiopathic Basal Ganglia Calcification (Fahr's disease) is an autosomal dominant neurodegenerative disorder characterized by bilateral symmetrical brain calcification caused by mutations in:",
    "options": [
      "SLC20A2 (encoding the type III sodium-dependent inorganic phosphate transporter PiT2) and PDGFB / PDGFRB",
      "Presenilin-1 and Presenilin-2",
      "Superoxide dismutase 1 (SOD1)",
      "Tau MAPT exon 10"
    ],
    "answer": 0,
    "explain": "Mutations in SLC20A2 (PiT2), PDGFB, PDGFRB, or XPR1 impair cerebral phosphate homeostasis and pericyte recruitment, driving pathological hydroxyapatite calcium-phosphate precipitation in vessel walls of the globus pallidus, putamen, and dentate nucleus.",
    "example": "CT scans of patients with Fahr's disease reveal dense, striking, bilateral symmetrical 'stonelike' calcification of the basal ganglia and cerebellar dentate nuclei.",
    "id": "nd-080",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Rapidly Progressive Dementia: Creutzfeldt-Jakob Disease Diagnostics",
    "prompt": "In a patient presenting with rapidly progressive dementia, myoclonus, and ataxia, which clinical diagnostic combination provides the highest sensitivity and specificity for Creutzfeldt-Jakob disease (CJD)?",
    "options": [
      "Positive CSF RT-QuIC assay, accompanied by cortical ribboning and basal ganglia hyperintensity on diffusion-weighted (DWI) MRI",
      "Elevated serum cholesterol and abnormal liver function tests",
      "Normal EEG with absent sensory nerve action potentials",
      "Positive antinuclear antibody (ANA) titer exclusively"
    ],
    "answer": 0,
    "explain": "The real-time quaking-induced conversion (RT-QuIC) assay in CSF achieves >95% sensitivity and ~100% specificity for CJD prions. On brain MRI, diffusion-weighted imaging (DWI) reveals characteristic 'cortical ribboning' (hyperintensity in cortical gyri) and high signal in the caudate and putamen.",
    "example": "RT-QuIC replaced nonspecific CSF surrogate markers like 14-3-3 and total-tau in consensus international CJD diagnostic criteria.",
    "id": "nd-081",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Anti-NMDAR Encephalitis Target and Association",
    "prompt": "Anti-NMDA receptor encephalitis is a treatable autoimmune encephalopathy in young patients characterized by psychiatric symptoms, seizures, and autonomic instability, caused by antibodies targeting:",
    "options": [
      "The GluN1 amino-terminal domain (ATD), frequently triggered by an underlying ovarian teratoma expressing neural tissue",
      "The GluA2 subunit of AMPA receptors, triggered by lung adenocarcinoma",
      "GABAA receptor beta-3 subunits",
      "The intracellular carboxyl terminus of PSD-95"
    ],
    "answer": 0,
    "explain": "Josep Dalmau's group discovered that IgG antibodies bind a conformational epitope on the extracellular GluN1 amino-terminal domain. In young females, the disease is frequently triggered by an ectopic ovarian teratoma containing mature neural tissue expressing NMDA receptors.",
    "example": "Antibody binding crosslinks surface NMDA receptors, driving their endocytosis and depletion from synaptic membranes, which is fully reversible following immunotherapy and tumor resection.",
    "id": "nd-082",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cerebral Microbleeds: CAA vs Hypertensive Angiopathy",
    "prompt": "On susceptibility-weighted or gradient-echo brain MRI, how does the anatomical distribution of cerebral microbleeds differentiate Cerebral Amyloid Angiopathy (CAA) from hypertensive arteriolopathy?",
    "options": [
      "CAA microbleeds are strictly lobar (cortical and subcortical, sparing the basal ganglia and brainstem); hypertensive microbleeds involve deep structures (basal ganglia, thalamus, and pons)",
      "CAA microbleeds occur only in the cerebellum; hypertensive microbleeds occur only in the corpus callosum",
      "CAA microbleeds are always larger than 5 centimeters",
      "There is no anatomical difference between the two conditions"
    ],
    "answer": 0,
    "explain": "Under the Boston Criteria for CAA, cerebral amyloid angiopathy causes microbleeds and lobar intracerebral hemorrhages strictly in cortical/subcortical lobar regions (especially occipital and parietal lobes). Hypertensive lipohyalinosis preferentially damages deep perforating lenticulostriate and pontine arteries, yielding deep basal ganglia/thalamic microbleeds.",
    "example": "A strictly lobar pattern of microbleeds in a cognitively impaired elderly patient strongly supports a diagnosis of probable Cerebral Amyloid Angiopathy.",
    "id": "nd-083",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Pantothenate Kinase-Associated Neurodegeneration (PKAN)",
    "prompt": "Pantothenate Kinase-Associated Neurodegeneration (PKAN), the most common form of NBIA, is caused by PANK2 mutations and displays which pathognomonic sign on T2-weighted MRI?",
    "options": [
      "The 'eye-of-the-tiger' sign (bilateral central hyperintensity surrounded by severe hypointensity in the globus pallidus)",
      "The 'hummingbird' sign of midbrain atrophy",
      "The 'hot cross bun' sign in the pons",
      "Total absence of the corpus callosum"
    ],
    "answer": 0,
    "explain": "Mutations in mitochondrial pantothenate kinase 2 (PANK2) impair coenzyme A (CoA) biosynthesis, leading to massive pathological iron deposition in the globus pallidus. On T2-weighted MRI, central necrosis/edema appears hyperintense, encircled by intense iron-induced hypointensity, generating the iconic 'eye-of-the-tiger' appearance.",
    "example": "Patients present in childhood with progressive dystonia, parkinsonism, dysarthria, and retinitis pigmentosa.",
    "id": "nd-084",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Wilson's Disease: Molecular Genetics and Neuropathology",
    "prompt": "Wilson's disease is an autosomal recessive inborn error of copper metabolism caused by mutations in the ATP7B gene, leading to:",
    "options": [
      "Defective biliary copper excretion and failure to incorporate copper into ceruloplasmin, causing toxic copper accumulation in the liver, basal ganglia (lenticular nucleus), and cornea",
      "Excessive iron accumulation in motor neurons",
      "Complete absence of zinc in all tissues",
      "Inability to synthesize myelin basic protein"
    ],
    "answer": 0,
    "explain": "ATP7B is a copper-transporting P-type ATPase in hepatocytes. Mutations abolish biliary copper export; free copper accumulates in liver, spills into the bloodstream, and deposits in the putamen and globus pallidus (causing parkinsonism, tremor, and wing-beating) and in the corneal limbus (Kayser-Fleischer rings).",
    "example": "Treatment with copper chelators (D-penicillamine, trientine) or zinc acetate halts disease progression and reverses neurological symptoms.",
    "id": "nd-085",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "SOD1 A4V Mutation Aggressive Clinical Course",
    "prompt": "In North America, the A4V (Ala4Val) missense mutation is the most frequent SOD1 mutation in familial ALS, distinguished clinically by:",
    "options": [
      "An exceptionally rapid and aggressive clinical course, with median survival of less than 12 to 18 months from symptom onset",
      "A benign disease course spanning 30 to 40 years",
      "Prominent early dementia preceding motor weakness",
      "Exclusively upper motor neuron signs with normal electromyography"
    ],
    "answer": 0,
    "explain": "The A4V mutation in exon 1 severely destabilizes the SOD1 homodimer interface, dramatically accelerating misfolding and hydrophobic aggregation. Consequently, A4V patients suffer a rapidly progressive, fulminant motor neuron death with median survival under one year.",
    "example": "Clinical trials for gene therapies like tofersen monitor A4V patients with high frequency due to their rapid rate of axonal degeneration.",
    "id": "nd-086",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Cryo-EM Structure of Alzheimer's Tau Filaments",
    "prompt": "Cryo-electron microscopy structures of tau filaments isolated from Alzheimer's disease brain tissue (Fitzpatrick et al., 2017) revealed that paired helical filaments (PHFs) and straight filaments (SFs):",
    "options": [
      "Are composed of identical C-shaped protofilaments spanning residues 306-378 that pack against each other via different inter-protofilament interfaces",
      "Consist of full-length tau extending from residues 1 to 441 in a rigid alpha-helical barrel",
      "Are composed exclusively of 3R tau with zero 4R tau incorporation",
      "Are held together entirely by covalent transglutaminase crosslinks"
    ],
    "answer": 0,
    "explain": "High-resolution cryo-EM demonstrated that both PHFs and SFs share an identical C-shaped protofilament core encompassing both repeat 3 and repeat 4, plus 10 amino acids after repeat 4 (residues 306-378). In PHFs, two protofilaments pack symmetrically tip-to-tip; in SFs, they pack asymmetrically.",
    "example": "This landmark study proved that the filament core is identical across all Alzheimer's patients regardless of disease duration or clinical severity.",
    "id": "nd-087",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Pick's Disease Tau Filament Fold",
    "prompt": "Cryo-EM structures of tau filaments from Pick's disease brain tissue (Falcon et al., 2018) established that the Pick fold differs fundamentally from the Alzheimer fold because:",
    "options": [
      "It incorporates exclusively 3-repeat (3R) tau, forming a narrow, elongated J-shaped protofilament spanning residues 254-378",
      "It is composed entirely of the amino-terminal projection domain (residues 1-150)",
      "It forms a hollow spherical shell rather than a cross-beta fibril",
      "It contains equal amounts of 3R and 4R tau in alternating rungs"
    ],
    "answer": 0,
    "explain": "Pick's disease tau filaments contain solely 3R tau, adopting a unique J-shaped hairpin fold that begins in repeat 1 and spans into the C-terminal region (residues 254-378). This unique fold explains why first-generation tau-PET tracers (e.g., flortaucipir) bind Alzheimer's PHFs with high affinity but completely fail to bind Pick bodies.",
    "example": "Structural resolution of the Pick fold provided the structural basis for developing 3R-tau-specific diagnostic PET ligands.",
    "id": "nd-088",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "4R Tauopathy Cryo-EM Folds: PSP vs CBD",
    "prompt": "High-resolution cryo-EM comparisons of 4-repeat tauopathies demonstrated that the tau filament core in Corticobasal Degeneration (CBD):",
    "options": [
      "Adopts a wide, four-layered fold that encloses an internal non-proteinaceous density, whereas PSP adopts a distinct three-layered hairpin fold",
      "Is identical in all respects to the PSP fold",
      "Consists solely of 3-repeat tau",
      "Does not contain beta-sheets"
    ],
    "answer": 0,
    "explain": "CBD tau filaments adopt a four-layered protofilament fold (residues 274-380) with a central cavity enclosing a non-proteinaceous polyanionic cofactor. In contrast, PSP tau filaments adopt a distinct three-layered hairpin fold, proving that distinct clinical tauopathy phenotypes correspond to distinct, disease-specific filament structures.",
    "example": "Cryo-EM structural classification now allows definitive molecular subtyping of frontotemporal tauopathies that overlap clinically.",
    "id": "nd-089",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Alpha-Synuclein Cryo-EM Filaments in MSA vs PD",
    "prompt": "Cryo-EM structures of alpha-synuclein filaments isolated from Multiple System Atrophy (MSA) versus Parkinson's disease (PD) brains revealed that:",
    "options": [
      "MSA filaments consist of two distinct protofilament types packing around a non-proteinaceous density, forming a significantly more compact and potent seeding conformer than PD filaments",
      "MSA and PD filaments have identical atomic coordinates",
      "PD filaments are found exclusively inside oligodendrocytes",
      "Alpha-synuclein does not form cross-beta structures in human brain tissue"
    ],
    "answer": 0,
    "explain": "MSA-derived alpha-synuclein filaments feature an extensive, asymmetric inter-protofilament interface encompassing residues 1-140 that is completely distinct from the filament fold observed in Lewy body diseases, explaining the significantly higher seeding potency and aggressive clinical course of MSA.",
    "example": "Inoculation of MSA-derived alpha-synuclein fibrils into transgenic mice induces much faster, more widespread neurodegeneration than inoculation of PD-derived fibrils.",
    "id": "nd-090",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Heparan Sulfate Proteoglycans in Tau Seeding",
    "prompt": "Extracellular tau oligomers and fibrils enter recipient neurons to template prionic propagation by binding with high affinity to which cell-surface macromolecules?",
    "options": [
      "Heparan sulfate proteoglycans (HSPGs) with specific 6-O- and 2-O-sulfation patterns",
      "Phosphatidylcholine headgroups",
      "Voltage-gated potassium channels",
      "Myelin basic protein"
    ],
    "answer": 0,
    "explain": "Cell-surface HSPGs act as receptors for tau fibril endocytosis. Specifically, 6-O-sulfated and 2-O-sulfated glucosamine moieties on heparan sulfate chains electrostaticly engage basic residues in the tau microtubule-binding repeats, triggering macropinocytic uptake.",
    "example": "Enzymatic removal of cell-surface heparan sulfates with heparinase or competition with soluble heparin completely halts trans-neuronal tau spreading.",
    "id": "nd-091",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Tau Acetylation at Lys280 and Lys174",
    "prompt": "Pathological post-translational acetylation of tau at Lys280 (within the PHF6* hexapeptide) and Lys174 drives tauopathy by:",
    "options": [
      "Neutralizing the positive charge required for microtubule binding while dramatically accelerating tau fibrillization and impairing degradation",
      "Targeting tau to the proteasome for instant destruction",
      "Driving tau directly into the mitochondrial matrix",
      "Preventing tau phosphorylation by all protein kinases"
    ],
    "answer": 0,
    "explain": "Acetylation of Lys280 and Lys174 (catalyzed by p300/CBP) neutralizes the basic lysine charge, causing tau detachment from microtubules and stabilizing beta-sheet aggregation. Acetylated tau is also resistant to proteasomal clearance.",
    "example": "Inhibiting SIRT1 deacetylase activity increases tau acetylation and exacerbates neurodegeneration, whereas sirtuin activators promote tau deacetylation and clearance.",
    "id": "nd-092",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Diagnostic Phospho-Tau Epitopes: AT8, AT180, PHF-1",
    "prompt": "In neuropathological evaluation of Alzheimer's disease, the monoclonal antibody AT8 selectively detects paired helical filaments by binding to tau phosphorylated simultaneously at:",
    "options": [
      "Ser202 and Thr205",
      "Thr181 and Thr217",
      "Ser396 and Ser404",
      "Thr231 and Ser235"
    ],
    "answer": 0,
    "explain": "AT8 requires phosphorylation of both Ser202 and Thr205 (and is enhanced by pSer208) in the proline-rich domain of tau. It is the international standard antibody for Braak staging. PHF-1 recognizes pSer396/pSer404, and AT180 recognizes pThr231.",
    "example": "AT8 immunoreactivity reveals the earliest pretangle stages in locus coeruleus and entorhinal projection neurons before fibrillar tangles form.",
    "id": "nd-093",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "EphB2 Degradation by A-beta Oligomers",
    "prompt": "Soluble A-beta oligomers induce synaptic NMDA receptor deficits and impair long-term potentiation by directly binding and triggering the degradation of which receptor tyrosine kinase?",
    "options": [
      "EphB2",
      "TrkB",
      "EGFR",
      "Insulin receptor"
    ],
    "answer": 0,
    "explain": "A-beta oligomers bind directly to the extracellular fibronectin type III repeats of EphB2, inducing its endocytosis and proteasomal degradation. Because EphB2 normally phosphorylates GluN2B to anchor NMDA receptors at postsynaptic densities, EphB2 depletion causes massive loss of synaptic NMDA currents.",
    "example": "Overexpressing EphB2 in the hippocampus of Alzheimer's transgenic mice restores NMDA receptor surface expression and rescues cognitive deficits.",
    "id": "nd-094",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Fyn Kinase Activation by PrPC-mGluR5 Complex",
    "prompt": "Downstream of A-beta oligomer binding to cellular prion protein (PrPC) and mGluR5, synaptic spine collapse is mediated by activation of which Src-family non-receptor tyrosine kinase?",
    "options": [
      "Fyn kinase",
      "Abl kinase",
      "Janus kinase 2 (JAK2)",
      "Bruton's tyrosine kinase (BTK)"
    ],
    "answer": 0,
    "explain": "Binding of A-beta oligomers to PrPC clusters mGluR5, activating Fyn kinase. Active Fyn phosphorylates the GluN2B subunit of NMDA receptors at Tyr1472, causing transient excitotoxic Ca2+ influx followed by receptor endocytosis, calpain activation, and dendritic spine pruning.",
    "example": "Fyn knockout mice or Alzheimer models treated with the Fyn inhibitor saracatinib are protected against A-beta-induced synaptic loss and spatial learning deficits.",
    "id": "nd-095",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Presenilin Carboxypeptidase Processivity Deficit",
    "prompt": "The molecular mechanism uniting hundreds of diverse autosomal dominant familial Alzheimer's mutations in Presenilin-1 (PSEN1) is:",
    "options": [
      "A loss of sequential carboxypeptidase trimming processivity, causing premature dissociation of longer, highly amyloidogenic A-beta peptides (A-beta-42 and A-beta-43)",
      "A dramatic 10-fold increase in the total catalytic turnover rate of all substrates",
      "Complete failure of the gamma-secretase complex to assemble",
      "Selective cleavage of myelin basic protein instead of APP"
    ],
    "answer": 0,
    "explain": "Familial AD PSEN1 mutations destabilize the enzyme-substrate complex during processive carboxy-peptidase-like trimming. Instead of cleanly completing 4-5 successive trimming cycles down to harmless A-beta-38, mutant presenilin prematurely unbinds the substrate after only 2-3 cuts, elevating A-beta-42 and A-beta-43 production.",
    "example": "This carboxypeptidase processivity deficit increases the A-beta-42/40 ratio, driving early-onset plaque nucleation in mutation carriers.",
    "id": "nd-096",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Soluble TREM2 (sTREM2) Ectodomain Shedding",
    "prompt": "The extracellular ligand-binding domain of microglial TREM2 is shed into the cerebrospinal fluid as soluble TREM2 (sTREM2) following cleavage by which metalloproteinase?",
    "options": [
      "ADAM10",
      "MMP-9",
      "BACE1",
      "Gamma-secretase"
    ],
    "answer": 0,
    "explain": "ADAM10 cleaves human TREM2 at the His157-Ser158 peptide bond within the stalk region, releasing the soluble ectodomain (sTREM2) into the interstitial fluid and CSF. The p.H157Y mutation accelerates ADAM10 shedding, reducing functional full-length cell-surface TREM2 and increasing AD risk.",
    "example": "CSF sTREM2 levels rise in early clinical stages of Alzheimer's disease, reflecting a protective microglial activation response against amyloid and tau pathology.",
    "id": "nd-097",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "APOE Christchurch (R136S) Resilience Mutation",
    "prompt": "A rare heterozygous carrier of the PSEN1 E280A mutation remained cognitively unimpaired until her 70s (three decades beyond expected onset) due to carrying which homozygous protective APOE mutation?",
    "options": [
      "APOE3 Christchurch (R136S)",
      "APOE4 Jacksonville (V236E)",
      "APOE2 homozygous",
      "APOE-null knockout"
    ],
    "answer": 0,
    "explain": "The APOE3 Christchurch (R136S) mutation alters a basic arginine in the heparan sulfate proteoglycan (HSPG) and LRP1 binding region. Although this patient developed extensive cortical amyloid plaques, the lack of APOE-HSPG binding prevented tau tangle propagation and neurodegeneration.",
    "example": "This landmark case established that uncoupling amyloid pathology from downstream tau propagation is sufficient to preserve cognitive function in humans.",
    "id": "nd-098",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "TDP-43 Structural Architecture and Domains",
    "prompt": "TAR DNA-binding protein 43 (TDP-43) consists of 414 amino acids structured into which distinct functional domains?",
    "options": [
      "An N-terminal domain (NTD) mediating dimerization, two RNA-recognition motifs (RRM1 and RRM2), and an intrinsically disordered C-terminal glycine-rich domain",
      "A single central zinc finger and seven transmembrane helices",
      "An N-terminal kinase domain, a central SH2 domain, and a C-terminal PDZ domain",
      "A death domain, a caspase-recruitment domain (CARD), and ankyrin repeats"
    ],
    "answer": 0,
    "explain": "TDP-43 contains an NTD that forms physiological homodimers, RRM1 and RRM2 that recognize UG-rich single-stranded RNA, a nuclear localization signal (NLS), and an intrinsically disordered C-terminal domain (residues 274-414) where virtually all ALS-causing mutations cluster.",
    "example": "Pathological cleavage of TDP-43 by caspases and calpains generates C-terminal fragments (CTF-25 and CTF-35) that aggregate rapidly in motor neurons.",
    "id": "nd-099",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "TDP-43 Liquid-Liquid Phase Separation Helix",
    "prompt": "Within the intrinsically disordered C-terminal domain of TDP-43, reversible liquid-liquid phase separation (LLPS) is driven by a conserved, transiently populated structure spanning residues 320-340 that forms:",
    "options": [
      "A transient alpha-helix that mediates multivalent hydrophobic and aromatic intermolecular contacts",
      "A stable triple-beta sheet barrel",
      "A collagen-like polyproline type II helix",
      "A zinc-coordinating finger loop"
    ],
    "answer": 0,
    "explain": "Residues 320-340 form a transient alpha-helix within the otherwise disordered tail. Homotypic interactions between these transient helices drive phase separation into liquid droplets. ALS-linked mutations in this region (e.g., A321V, M337V) disrupt the helical balance, driving aberrant phase transitions into solid irreversible fibrils.",
    "example": "Disrupting this transient helix with helix-breaking proline mutations abolishes TDP-43 phase separation and prevents fibril nucleation.",
    "id": "nd-100",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "UNC13A Cryptic Exon and rs12973192 Risk SNP",
    "prompt": "Loss of nuclear TDP-43 causes aberrant inclusion of a cryptic exon in UNC13A transcripts. How does the common ALS/FTD risk single nucleotide polymorphism (rs12973192) exacerbate this pathology?",
    "options": [
      "The risk allele alters the intronic sequence to create a stronger consensus splice acceptor site, dramatically increasing cryptic exon inclusion upon TDP-43 reduction",
      "It mutates the UNC13A protein active site to block calcium binding",
      "It prevents transcription of the UNC13A promoter",
      "It duplicates the UNC13A gene locus"
    ],
    "answer": 0,
    "explain": "Studies in 2022 revealed that rs12973192 lies directly inside the cryptic exon region of UNC13A. The risk allele increases spliceosome affinity for the cryptic exon. When nuclear TDP-43 levels decline, patients homozygous for the risk allele suffer much faster UNC13A loss, accelerating disease progression.",
    "example": "UNC13A is essential for presynaptic vesicle priming and neurotransmitter release; its loss cripples neuromuscular junction and cortical synaptic transmission.",
    "id": "nd-101",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "STMN2 Loss Following Nuclear TDP-43 Depletion",
    "prompt": "In human motor neurons, nuclear depletion of TDP-43 leads to loss of Stathmin-2 (STMN2) protein through which specific molecular mechanism?",
    "options": [
      "TDP-43 fails to repress a cryptic polyadenylation site within intron 1, producing an aberrantly truncated, non-functional STMN2 mRNA",
      "TDP-43 acts as a transcription factor for the STMN2 promoter",
      "TDP-43 directly degrades stathmin-2 in the cytoplasm via its ribonuclease domain",
      "Loss of TDP-43 triggers hypermethylation of the STMN2 CpG island"
    ],
    "answer": 0,
    "explain": "TDP-43 normally binds a GU-rich element in intron 1 of STMN2, suppressing a cryptic splice acceptor and premature polyadenylation signal. Loss of nuclear TDP-43 causes premature termination and inclusion of cryptic exon 2a, destroying STMN2 expression.",
    "example": "Because Stathmin-2 is a critical microtubule-regulatory protein essential for axonal growth, its loss causes motor axon retraction and denervation in ALS.",
    "id": "nd-102",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "C9orf72 Complex in Autophagy and Endosomal Trafficking",
    "prompt": "Beyond repeat expansion toxicity, normal C9orf72 protein functions physiologically in a tripartite complex with SMCR8 and WDR41 to act as:",
    "options": [
      "A Guanine Nucleotide Exchange Factor (GEF) for small Rab GTPases (Rab8a and Rab39b) that regulates autophagy initiation and lysosome biogenesis",
      "An RNA helicase that unwinds G-quadruplexes in the nucleus",
      "An E3 ubiquitin ligase that degrades misfolded SOD1",
      "A subunit of the mitochondrial respiratory chain"
    ],
    "answer": 0,
    "explain": "C9orf72 forms an obligate heterodimer with SMCR8 that associates with WDR41, adopting a DENN-domain fold that functions as a GEF for Rab8a and Rab39b. This complex recruits ULK1 to autophagosome formation sites and regulates lysosomal trafficking.",
    "example": "C9orf72 knockout mice develop severe systemic immune dysregulation, splenomegaly, and lysosomal storage defects due to impaired autophagy.",
    "id": "nd-103",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "C9orf72 RNA G-Quadruplexes and Splicing Sequestration",
    "prompt": "Sense GGGGCC repeat expansion transcripts form highly stable secondary RNA structures known as G-quadruplexes that inflict neurotoxicity by:",
    "options": [
      "Forming nuclear RNA foci that physically sequester essential RNA-binding and splicing proteins such as hnRNP H and SRSF2, causing global alternative splicing defects",
      "Directly phosphorylating histone H3 at serine 10",
      "Exporting intact genomic DNA fragments into the cytoplasm",
      "Cleaving transfer RNAs at the anticodon loop"
    ],
    "answer": 0,
    "explain": "G-rich C9orf72 repeats fold into four-stranded G-quadruplexes and R-loops that resist degradation, accumulating into dense nuclear RNA foci. These foci avidly sequester splicing regulators (hnRNP H, ALYREF), stripping them from normal endogenous transcripts and causing widespread missplicing.",
    "example": "Antisense oligonucleotides (ASOs) targeting sense GGGGCC transcripts dissolve nuclear RNA foci and restore normal alternative splicing patterns.",
    "id": "nd-104",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Kinesin-1 Inhibition by Mutant SOD1",
    "prompt": "Mutant SOD1 impairs fast anterograde axonal transport in motor neurons through which aberrant biochemical signaling mechanism?",
    "options": [
      "Misfolded SOD1 exposes non-native hydrophobic surfaces that activate p38 MAPK, which phosphorylates kinesin light chain (KLC), releasing cargo from the motor complex",
      "Mutant SOD1 binds to dynein to force it to run forward toward the synapse",
      "Mutant SOD1 hydrolyzes all ATP in the axon shaft within seconds",
      "Mutant SOD1 dissolves axonal neurofilaments via transamination"
    ],
    "answer": 0,
    "explain": "Misfolded SOD1 forms toxic monomers that aberrantly bind and activate p38 MAPK. Activated p38 directly phosphorylates kinesin light chains (KLC), inducing cargo release and paralyzing anterograde transport of synaptic vesicles, choline acetyltransferase, and mitochondria.",
    "example": "Inhibitors of p38 MAPK restore fast anterograde axonal transport in isolated squid axoplasm and cultured ALS motor neurons.",
    "id": "nd-105",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Huntingtin-Mediated Retrograde BDNF Transport",
    "prompt": "Wild-type huntingtin promotes the vesicular transport of BDNF along microtubules from cortical neurons to striatal medium spiny neurons by scaffolding:",
    "options": [
      "Huntingtin-associated protein 1 (HAP1) to the p150Glued subunit of the dynein/dynactin retrograde motor complex",
      "Tau protein directly to the kinesin motor domain",
      "Clathrin light chain to the nuclear pore complex",
      "Synaptotagmin-1 to the postsynaptic density"
    ],
    "answer": 0,
    "explain": "Normal huntingtin acts as a molecular scaffold linking HAP1 to the p150Glued subunit of dynactin, optimizing microtubule-based motor velocity. In Huntington's disease, polyglutamine expansion disrupts this scaffold, crippling BDNF vesicular transport to the striatum and depriving MSNs of essential trophic support.",
    "example": "Restoring BDNF delivery to the striatum via viral vectors or TrkB agonists significantly attenuates striatal neurodegeneration in HD mouse models.",
    "id": "nd-106",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "LRRK2 G2019S Kinase Hyperactivation and Rab GTPases",
    "prompt": "The most common pathogenic mutation in Leucine-Rich Repeat Kinase 2 (LRRK2 G2019S) resides in the kinase domain activation loop (DYG motif), resulting in:",
    "options": [
      "Constitutive kinase hyperactivation, driving excessive phosphorylation of a conserved Thr/Ser residue in the switch-II domain of small Rab GTPases (Rab8a, Rab10, Rab29)",
      "Complete loss of GTPase activity in the ROC domain",
      "Failure of LRRK2 to localize to endolysosomal membranes",
      "Immediate dimerization with alpha-synuclein in the nucleus"
    ],
    "answer": 0,
    "explain": "G2019S increases LRRK2 kinase catalytic velocity by 2- to 3-fold. LRRK2 phosphorylates conserved residues (e.g., Thr73 on Rab10; Thr72 on Rab8a) in the switch-II loop of Rab GTPases. Hyperphosphorylated Rabs are trapped on membranes, impairing endolysosomal sorting, ciliogenesis, and autophagosome clearance.",
    "example": "Measuring phosphorylated Rab10 (pThr73-Rab10) in human peripheral blood neutrophils serves as a direct clinical biomarker for LRRK2 kinase activity.",
    "id": "nd-107",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "VPS35 D620N Retromer Dysfunction in Parkinson's",
    "prompt": "The D620N mutation in Vacuolar Protein Sorting 35 (VPS35) causes autosomal dominant Parkinson's disease by impairing the retromer complex's ability to:",
    "options": [
      "Recycle cargo proteins (such as the cation-independent mannose-6-phosphate receptor, CI-MPR) from endosomes back to the trans-Golgi network, depleting lysosomal hydrolases like Cathepsin D",
      "Assemble the nuclear pore basket",
      "Import mitochondrial precursor proteins through the TOM complex",
      "Degrade polyubiquitinated proteins in the 26S proteasome"
    ],
    "answer": 0,
    "explain": "VPS35 is the core cargo-recognition subunit of the retromer complex (VPS35-VPS26-VPS29). The D620N mutation alters retromer interactions with the FAM21/WASH complex, disrupting trafficking of CI-MPR. Without proper CI-MPR recycling, lysosomal proteases like Cathepsin D are missorted, impairing alpha-synuclein clearance.",
    "example": "Expression of VPS35 D620N in dopaminergic neurons causes alpha-synuclein accumulation, mitochondrial fragmentation, and progressive parkinsonism.",
    "id": "nd-108",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "TBK1 and Optineurin in Selective Mitophagy",
    "prompt": "Loss-of-function mutations in TANK-Binding Kinase 1 (TBK1) and its substrate Optineurin (OPTN) cause ALS/FTD by disrupting:",
    "options": [
      "Phosphorylation of OPTN at Ser177, which normally enhances its affinity for LC3-II to coordinate the autophagic engulfment of damaged mitochondria and ubiquitinated aggregates",
      "Nuclear transcription of ribosomal RNA",
      "Translation of kinesin heavy chain in axon terminals",
      "Depolarization-induced calcium influx through Cav2.1 channels"
    ],
    "answer": 0,
    "explain": "During selective autophagy and mitophagy, TBK1 phosphorylates the autophagy receptor Optineurin (OPTN) at Ser177 and the UBAN domain. This massively increases OPTN binding to LC3-II on autophagosomal isolation membranes, ensuring rapid engulfment of damaged mitochondria and polyubiquitinated protein assemblies.",
    "example": "TBK1 haploinsufficiency or OPTN E478G mutations impair autophagic clearance, leading to motor neuron death and TDP-43 aggregation.",
    "id": "nd-109",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Microglial Complement-Mediated Synapse Pruning in AD",
    "prompt": "In early Alzheimer's disease models, excessive elimination of excitatory synapses by microglia is initiated when which complement proteins aberrantly tag vulnerable dendritic spines?",
    "options": [
      "C1q and C3, which are recognized by microglial complement receptor 3 (CR3 / CD11b-CD18)",
      "C5b-9 membrane attack complexes exclusively",
      "Factor B and Factor D",
      "Perforin and granzyme B"
    ],
    "answer": 0,
    "explain": "Hong, Stevens, and colleagues showed that soluble A-beta oligomers induce deposition of the classical complement initiator C1q onto dendritic spines, which triggers downstream C3 cleavage. Microglia expressing CR3 (integrin alpha-M-beta-2) phagocytose C3-tagged spines, driving early synaptic loss before plaque deposition.",
    "example": "Blocking C1q or C3 with neutralizing antibodies or genetic deletion protects synapses from A-beta-induced pruning and preserves LTP.",
    "id": "nd-110",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Neurotoxic Reactive A1 Astrocytes (Liddelow & Barres)",
    "prompt": "Liddelow et al. (2017) demonstrated that microglia activated by LPS or injury secrete a cytokine triad that transforms quiescent astrocytes into neurotoxic 'A1' reactive astrocytes. What is this cytokine triad?",
    "options": [
      "IL-1alpha, TNF-alpha, and C1q",
      "IL-4, IL-10, and TGF-beta",
      "IFN-gamma, IL-6, and GM-CSF",
      "EGF, FGF-2, and PDGF"
    ],
    "answer": 0,
    "explain": "Activated microglia release interleukin-1alpha (IL-1alpha), tumor necrosis factor-alpha (TNF-alpha), and complement component C1q. Together, these three factors induce astrocytes to adopt an A1 reactive phenotype, wherein they lose normal synaptogenic functions and secrete saturated neurotoxic lipids that kill neurons and oligodendrocytes.",
    "example": "A1 astrocytes are abundant in post-mortem tissue from patients with Alzheimer's disease, Parkinson's disease, Huntington's disease, and ALS.",
    "id": "nd-111",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Meningeal Lymphatics and Waste Clearance",
    "prompt": "Louveau and Kipnis (2015) rediscovered functional meningeal lymphatic vessels running alongside dural venous sinuses that drain cerebrospinal fluid, macromolecules, and immune cells directly into:",
    "options": [
      "Deep cervical lymph nodes",
      "The thoracic duct directly without nodal filtration",
      "The axillary lymph nodes",
      "The splenic red pulp"
    ],
    "answer": 0,
    "explain": "Meningeal lymphatic vessels line the dural sinuses and exit the skull base alongside cranial nerves, draining interstitial fluid, A-beta, and immune cells into the deep cervical lymph nodes. Aging causes meningeal lymphatic vessel regression and decreased drainage capacity.",
    "example": "Pharmacological enhancement of meningeal lymphatic drainage via VEGF-C administration improves cognitive performance and accelerates A-beta clearance in aged mice.",
    "id": "nd-112",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Necroptosis Execution by RIPK1/RIPK3/MLKL in ALS",
    "prompt": "In ALS and Alzheimer's disease, receptor-interacting protein kinase 1 (RIPK1) and RIPK3 phosphorylate and activate which executioner pseudokinase that oligomerizes to perforate the plasma membrane during necroptosis?",
    "options": [
      "Mixed lineage kinase domain-like protein (MLKL)",
      "Gasdermin D",
      "Caspase-3",
      "Bcl-2-associated X protein (Bax)"
    ],
    "answer": 0,
    "explain": "When caspase-8 is inhibited or depleted, death receptor signaling activates the 'necrosome' complex: RIPK1 phosphorylates RIPK3, which in turn phosphorylates MLKL. Phospho-MLKL oligomerizes and translocates to the inner leaflet of the plasma membrane, disrupting membrane integrity and causing inflammatory necroptotic lysis.",
    "example": "RIPK1 inhibitors (e.g., necrostatin-1s) suppress necroptosis, dampening neuroinflammation and extending motor neuron survival in ALS animal models.",
    "id": "nd-113",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "TDP-43 Autoregulation via 3' UTR Binding",
    "prompt": "Under physiological conditions, nuclear TDP-43 tightly autoregulates its own protein abundance via a negative feedback loop wherein excess TDP-43:",
    "options": [
      "Binds to a conserved 34-nucleotide TDP-43-binding motif in its own pre-mRNA 3' UTR, triggering alternative splicing and nonsense-mediated decay (NMD)",
      "Directly phosphorylates its own promoter to repress transcription",
      "Ubiquitinates itself via an intrinsic E3 ligase domain",
      "Cleaves its own nascent polypeptide chain during ribosomal translation"
    ],
    "answer": 0,
    "explain": "Nuclear TDP-43 binds a dedicated CLIP-binding region in its own 3' UTR, inducing alternative splicing of an unannotated intron that triggers nuclear retention or nonsense-mediated decay (NMD). When TDP-43 aggregates in the cytoplasm, nuclear depletion breaks this negative feedback, driving runaway de novo synthesis of TDP-43 mRNA.",
    "example": "This breakdown in autoregulatory feedback fuels the continuous accumulation of pathological TDP-43 in ALS and FTLD-TDP.",
    "id": "nd-114",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Loss of Astrocytic EAAT2/GLT-1 in ALS",
    "prompt": "Selective focal loss of the astrocytic glutamate transporter EAAT2 (GLT-1) in the motor cortex and ventral horn of the spinal cord causes motor neuron death in ALS via:",
    "options": [
      "Sustained synaptic glutamate accumulation, excessive calcium influx through calcium-permeable AMPA and NMDA receptors, and excitotoxicity",
      "Starving motor neurons of neurotransmitter precursors",
      "Directly activating microglial phagocytosis of myelin",
      "Preventing potassium extrusion during the action potential"
    ],
    "answer": 0,
    "explain": "In >80% of sporadic ALS patients, astrocytic EAAT2 protein is lost from affected regions due to aberrant RNA splicing and cleavage by caspase-3. Impaired glutamate reuptake leaves synaptic glutamate elevated, driving continuous Ca2+ entry into motor neurons (which naturally express low levels of GluA2 and poor Ca2+ buffering).",
    "example": "Riluzole, the first approved drug for ALS, acts in part by enhancing astrocytic glutamate reuptake and inhibiting presynaptic glutamate release.",
    "id": "nd-115",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Microglial NLRP3 Inflammasome Activation by A-beta",
    "prompt": "Phagocytosis of fibrillar A-beta by microglia triggers NLRP3 inflammasome activation through which specific intracellular event?",
    "options": [
      "Frustrated phagocytosis causing lysosomal destabilization, leakage of Cathepsin B into the cytosol, and potassium efflux",
      "Direct binding of A-beta to mitochondrial DNA",
      "Caspase-3 cleavage of the nuclear envelope",
      "Depletion of intracellular cyclic AMP"
    ],
    "answer": 0,
    "explain": "Fibrillar A-beta cannot be easily degraded inside microglial phagolysosomes. The resulting lysosomal swelling causes membrane rupture and leakage of acidic Cathepsin B into the cytoplasm, which, accompanied by K+ efflux, triggers NLRP3 oligomerization with ASC and pro-caspase-1.",
    "example": "Active caspase-1 cleaves pro-IL-1beta and releases ASC specks into the extracellular space, where ASC specks bind A-beta and cross-seed further plaque aggregation.",
    "id": "nd-116",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Prion Strain Variation and Conformational Enciphering",
    "prompt": "Different strains of transmissible spongiform encephalopathies (e.g., vCJD vs sporadic CJD vs scrapie) exhibit distinct incubation times and neuropathological profiles because:",
    "options": [
      "Identical primary amino acid sequences fold into distinct, stable, self-propagating beta-sheet quaternary conformations that faithfully template their specific shape onto PrPC",
      "Each strain carries a unique viral RNA genome",
      "Prion strains are defined by different post-translational lipid glycosylations",
      "Different strains replicate in different organ systems exclusively"
    ],
    "answer": 0,
    "explain": "Prion strains demonstrate that protein structure alone can encipher heritable phenotypic information. Distinct quaternary conformations of PrPSc possess differing thermodynamic stabilities, fragmentation rates, and glycosylation site exposures, dictating specific incubation periods and selective anatomical targeting.",
    "example": "Limited proteinase K digestion followed by Western blot generates strain-specific migration patterns ('glycoform profiles') that differentiate variant CJD from sporadic CJD.",
    "id": "nd-117",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Intercellular Spreading via Tunneling Nanotubes (TNTs)",
    "prompt": "Tunneling nanotubes (TNTs) facilitate the direct, non-synaptic intercellular spreading of pathogenic aggregates (such as tau, alpha-synuclein, and huntingtin) between neurons and glia by:",
    "options": [
      "Providing continuous, thin, F-actin-rich membranous conduits that physically connect the cytoplasms of distant cells without exposing aggregates to the extracellular space",
      "Secreting exosomes into the systemic bloodstream",
      "Forming large gap junctions composed strictly of connexin-43",
      "Injecting proteins across the blood-brain barrier via pinocytosis"
    ],
    "answer": 0,
    "explain": "TNTs are thin (50-200 nm), F-actin-containing membrane protrusions that bridge cells over tens of microns. Pathological amyloidogenic aggregates travel inside these conduits by hitchhiking on endosomes and molecular motors, shielding them from extracellular immune surveillance and neutralizing antibodies.",
    "example": "Inhibition of actin polymerization with latrunculin B or TNT-cleaving peptides significantly reduces cell-to-cell propagation of alpha-synuclein fibrils.",
    "id": "nd-118",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Iron Accumulation in Parkinsonian Substantia Nigra",
    "prompt": "In the substantia nigra pars compacta of Parkinson's disease patients, excessive iron accumulation accelerates neurodegeneration primarily because:",
    "options": [
      "Neuromelanin saturation and ferritin light-chain downregulation increase the labile ferrous iron (Fe2+) pool, driving hydroxyl radical generation and alpha-synuclein oligomerization",
      "Iron directly cleaves dopamine into hydrogen cyanide",
      "Iron blocks all voltage-gated sodium channels in dopaminergic pacemakers",
      "Iron displaces copper from Cytochrome c oxidase completely"
    ],
    "answer": 0,
    "explain": "Substantia nigra dopamine neurons normally sequester iron in neuromelanin. With age and disease, neuromelanin becomes saturated and degenerating cells release free Fe2+. This labile iron catalyzes Fenton chemistry, oxidizes dopamine into toxic quinones, and directly accelerates alpha-synuclein fibrillization.",
    "example": "Quantitative susceptibility mapping (QSM) MRI detects significant iron accumulation in the substantia nigra of living Parkinson's patients, correlating with motor symptom severity.",
    "id": "nd-119",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Endogenous Biomarkers of Lipid Peroxidation: 4-HNE",
    "prompt": "4-Hydroxynonenal (4-HNE) is a toxic alpha,beta-unsaturated aldehyde produced in high quantities during neuronal lipid peroxidation that inflicts cellular damage by:",
    "options": [
      "Forming irreversible covalent Michael adducts with nucleophilic sulfhydryl groups of cysteine, imidazole rings of histidine, and amino groups of lysine residues",
      "Cleaving genomic DNA at telomeric repeat sequences",
      "Inactivating the nuclear envelope importin complex",
      "Acting as a direct agonist at GABAA receptors"
    ],
    "answer": 0,
    "explain": "4-HNE is generated by the oxidative breakdown of omega-6 polyunsaturated fatty acids (arachidonic and linoleic acids). Its electrophilic carbon-3 undergoes Michael addition with cysteine, histidine, and lysine residues, crosslinking and inactivating critical metabolic enzymes and transporters like EAAT2 and Na+/K+-ATPase.",
    "example": "High levels of 4-HNE-protein adducts are prominent in dystrophic neurites and Lewy bodies in post-mortem Alzheimer's and Parkinson's brain tissue.",
    "id": "nd-120",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Epigenetic Horvath Clock Acceleration in Neurodegeneration",
    "prompt": "Epigenetic clocks (such as the Horvath and Hannum clocks) calculate biological age and show accelerated aging in Alzheimer's disease brain tissue by analyzing:",
    "options": [
      "DNA methylation levels at specific, highly conserved CpG dinucleotides across the genome",
      "The length of telomeric repeat sequences in cortical neurons",
      "The total number of somatic mitochondrial DNA point mutations",
      "The concentration of lipofuscin granules in pyramidal neurons"
    ],
    "answer": 0,
    "explain": "Epigenetic clocks utilize elastic net regression to predict chronological and biological age based on DNA methylation fractions at specific CpG sites. In Alzheimer's frontal and temporal cortex, epigenetic age acceleration (biological age exceeding chronological age) correlates strongly with amyloid plaque load and cognitive decline.",
    "example": "Post-mortem analysis shows that the prefrontal cortex of patients with rapid cognitive decline displays up to 5-10 years of epigenetic age acceleration.",
    "id": "nd-121",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Anti-Amyloid Monoclonal Antibodies: Target Epitopes",
    "prompt": "The FDA-approved anti-amyloid monoclonal antibody lecanemab differs fundamentally from aducanumab and donanemab in its binding selectivity because it:",
    "options": [
      "Exhibits high selectivity for soluble A-beta protofibrils (75-300 kDa) over monomeric A-beta and insoluble fibrillar plaque cores",
      "Binds exclusively to monomeric A-beta-40 in the blood",
      "Selectively recognizes N-terminally truncated pyroglutamate-3 A-beta (pGlu3-A-beta) in dense-core plaques",
      "Binds to the C-terminal alanine-42 residue of all amyloid species equally"
    ],
    "answer": 0,
    "explain": "Lecanemab (BAN2401) was engineered to selectively target large, soluble A-beta protofibrils (75-300 kDa), which are considered the most neurotoxic intermediates. Aducanumab selectively binds the linear N-terminus (Asp1-His6) of aggregated A-beta, while donanemab targets pGlu3-A-beta localized to dense plaque cores.",
    "example": "In the Phase 3 Clarity AD trial, lecanemab significantly reduced brain amyloid plaque burden and slowed cognitive decline by 27% over 18 months.",
    "id": "nd-122",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Mechanism of ARIA (Amyloid-Related Imaging Abnormalities)",
    "prompt": "Amyloid-Related Imaging Abnormalities (ARIA-E for edema/sulcal effusion and ARIA-H for microhemorrhages) occur during anti-amyloid immunotherapy primarily because:",
    "options": [
      "Antibody-mediated clearance of amyloid from cerebral vessel walls (Cerebral Amyloid Angiopathy) causes transient focal disruption of vascular integrity, hyperpermeability, and microvascular leakage",
      "The monoclonal antibodies cross-react with endothelial cadherins and cleave them",
      "Complement activation dissolves all smooth muscle cells throughout the circle of Willis",
      "Microglia release excessive amounts of nitric oxide that dilates major dural sinuses"
    ],
    "answer": 0,
    "explain": "A-beta is deposited heavily in the walls of cortical and leptomeningeal vessels in cerebral amyloid angiopathy (CAA). Therapeutic antibodies bind vascular amyloid, recruiting microglia and complement to clear it. Removing vascular amyloid causes transient vessel wall hyperpermeability, leading to fluid extravasation (ARIA-E) or microhemorrhages (ARIA-H).",
    "example": "ARIA incidence is highest in APOE4 homozygous patients and during the first 3 to 6 months of titration, requiring routine safety monitoring by brain MRI.",
    "id": "nd-123",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "ASO Mechanism of Action: Tofersen in SOD1-ALS",
    "prompt": "Tofersen (Qalsody), an approved antisense oligonucleotide for SOD1-associated familial ALS, lowers mutant and wild-type SOD1 protein levels by:",
    "options": [
      "Binding to a complementary sequence in SOD1 mRNA and recruiting endogenous nuclear RNase H1 to cleave and degrade the transcript",
      "Altering pre-mRNA splicing to exclude exon 4",
      "Inactivating the catalytic copper atom inside the SOD1 active site",
      "Preventing translation elongation by sterically blocking ribosomal subunit joining"
    ],
    "answer": 0,
    "explain": "Tofersen is a gapmer antisense oligonucleotide containing 2'-O-(2-methoxyethyl) (MOE) modified flanking wings and a central 10-deoxynucleotide gap. It binds SOD1 mRNA and recruits nuclear RNase H1, which cleaves the RNA strand of the RNA-DNA duplex, halting synthesis of both wild-type and toxic mutant SOD1.",
    "example": "Intrathecal administration of tofersen significantly reduces CSF SOD1 protein and leads to sustained decreases in neurofilament light chain (NfL), stabilizing clinical decline.",
    "id": "nd-124",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "ASO Mechanism of Action: Nusinersen in SMA",
    "prompt": "Nusinersen (Spinraza) treats Spinal Muscular Atrophy (SMA) by altering SMN2 pre-mRNA splicing via which molecular mechanism?",
    "options": [
      "Binding to an intronic splicing silencer (ISS-N1) in intron 7, displacing hnRNP A1/A2 repressor proteins to promote exon 7 inclusion and full-length SMN protein synthesis",
      "Recruiting RNase H1 to destroy SMN2 transcripts",
      "Acting as an artificial transcription factor that binds the SMN1 promoter",
      "Inhibiting the ubiquitination of truncated SMNdelta7 protein"
    ],
    "answer": 0,
    "explain": "Nusinersen is a uniformly 2'-MOE-modified splice-switching phosphorothioate ASO. It sterically blocks the intronic splicing silencer element ISS-N1 in intron 7 of SMN2, displacing splicing repressors (hnRNP A1). This forces the spliceosome to include exon 7, converting truncated unstable SMNdelta7 into fully functional full-length SMN protein.",
    "example": "Nusinersen revolutionized pediatric neurology, allowing infants with SMA Type 1 to survive, breathe independently, and achieve motor milestones.",
    "id": "nd-125",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Selective Vulnerability of RORB+ Neurons in AD Entorhinal Cortex",
    "prompt": "Single-nucleus RNA-sequencing of the entorhinal cortex across early stages of Alzheimer's disease demonstrated that the earliest projecting neurons to degenerate are characterized by high expression of:",
    "options": [
      "The retinoic acid receptor-related orphan receptor B (RORB) transcription factor in layer II/III excitatory projection neurons",
      "Parvalbumin in inhibitory basket interneurons",
      "Tyrosine hydroxylase in locus coeruleus projections",
      "Somatostatin in Martinotti cells"
    ],
    "answer": 0,
    "explain": "Grubman et al. and Leng et al. showed that excitatory projection neurons in entorhinal cortex layer II/III expressing RORB are the most vulnerable neuronal population in early AD. These neurons accumulate early tau pathology, downregulate synaptic genes, and die, severing the perforant path to the hippocampus.",
    "example": "In contrast, neighboring non-RORB interneurons and deep-layer cortical neurons remain relatively resistant during early disease stages.",
    "id": "nd-126",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Spatial Transcriptomics of Plaque-Induced Genes (PIGs)",
    "prompt": "Spatial transcriptomic profiling of the microenvironment surrounding amyloid plaques (Chen et al., Cell 2020) identified a coordinated 'Plaque-Induced Gene' (PIG) network composed of:",
    "options": [
      "A ~100-micron diameter cellular niche enriched in microglial complement genes (C1qa/b/c), Apoe, Trem2, and astrocytic GFAP and Serpine2",
      "Exclusive upregulation of embryonic neural crest markers",
      "Total suppression of all immune signaling genes within 500 microns",
      "Upregulation of myelin proteolipid protein without glial activation"
    ],
    "answer": 0,
    "explain": "Spatial transcriptomics revealed that individual plaques act as epicenters for a stereotypic 100-micron microenvironment of multicellular activation. Microglia, astrocytes, and oligodendrocytes upregulate a coordinated network of 57 Plaque-Induced Genes (PIGs) focused on complement, phagocytosis, and oxidative stress.",
    "example": "The PIG gene network is conserved between Alzheimer mouse models and human post-mortem tissue, demonstrating a localized, synchronized multicellular response to amyloid cores.",
    "id": "nd-127",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Plasma Neurofilament Light Chain (NfL) Utility",
    "prompt": "Plasma neurofilament light chain (NfL), measured by Single Molecule Array (Simoa), has emerged as a revolutionary fluid biomarker in neurology because it:",
    "options": [
      "Quantifies active ongoing axonal damage and neuroaxonal degeneration across a broad range of neurodegenerative disorders, correlating with disease progression velocity",
      "Distinguishes specifically between Alzheimer's and frontotemporal dementia with 100% molecular specificity",
      "Rises only when amyloid plaques are present in the brain",
      "Is synthesized exclusively by reactive astrocytes"
    ],
    "answer": 0,
    "explain": "NfL is a structural cylindrical subunit of the axonal neurofilament core. When axons are injured or degenerate, NfL leaks into interstitial fluid, CSF, and systemic circulation. While not specific to any single disease, plasma NfL levels accurately reflect the instantaneous rate of active neuroaxonal loss in ALS, MS, FTD, and AD.",
    "example": "In clinical trials of neurodegenerative therapeutics, a rapid drop in plasma NfL serves as an objective pharmacodynamic biomarker of reduced axonal destruction.",
    "id": "nd-128",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Plasma Glial Fibrillary Acidic Protein (GFAP) in Preclinical AD",
    "prompt": "Unlike CSF GFAP, elevated blood plasma GFAP has emerged as a remarkably early biomarker in Alzheimer's disease because it:",
    "options": [
      "Rises in the blood in direct response to the initial accumulation of cortical amyloid-beta plaques, preceding detectable tau tangle pathology",
      "Reflects the total loss of all cortical neurons",
      "Decreases to zero whenever microglial activation occurs",
      "Is produced exclusively by perivascular pericytes"
    ],
    "answer": 0,
    "explain": "Astrocytic endfeet tightly wrap the cerebral microvasculature. Early amyloid deposition triggers astrogliosis, causing reactive astrocytes to release GFAP directly into the blood across perivascular channels. Blood plasma GFAP is more sensitive to early amyloid plaque pathology than CSF GFAP.",
    "example": "Elevated plasma GFAP in cognitively normal elderly individuals predicts subsequent amyloid accumulation and cognitive decline.",
    "id": "nd-129",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "TDP-43 Amyloid Core Cryo-EM Architecture",
    "prompt": "Cryo-EM structures of pathological TDP-43 filaments extracted from ALS and FTLD-TDP human brains (Arseni et al., Nature 2022) revealed that the fibril core:",
    "options": [
      "Spans residues 282-360 in the C-terminal domain, folding into a novel double-spiral cross-beta architecture that resembles a stylized question mark",
      "Is composed entirely of the folded RRM1 and RRM2 domains",
      "Consists of a hollow tube of alpha-helices with a central water channel",
      "Does not contain beta-sheets and is held together by lipid bilayers"
    ],
    "answer": 0,
    "explain": "Arseni et al. resolved the atomic structure of patient-derived TDP-43 filaments, demonstrating that residues 282-360 form a filamentous cross-beta core resembling a double-spiral or question mark. The fold encloses hydrophobic and aromatic residues while leaving phosphorylation sites (Ser409/410) accessible on the outer surface.",
    "example": "This breakthrough provides the exact structural template required for the rational design of TDP-43-specific PET imaging ligands and aggregate-dissolving small molecules.",
    "id": "nd-130",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "PrPC as a High-Affinity Oligomer Receptor for Alpha-Synuclein and A-beta",
    "prompt": "Beyond binding A-beta oligomers, cellular prion protein (PrPC) also binds which other pathological neurodegenerative oligomer to mediate synaptic dysfunction?",
    "options": [
      "Alpha-synuclein oligomers, triggering cofilin/actin rod formation and NMDA receptor hypofunction",
      "Insoluble collagen fibers",
      "Poly-glycine dipeptide repeats",
      "Monomeric dopamine molecules"
    ],
    "answer": 0,
    "explain": "PrPC binds alpha-synuclein oligomers through its N-terminal domain with high affinity. This binding couples to mGluR5 and LRP1, triggering cofilin dephosphorylation, F-actin rod formation, and synaptic NMDA receptor internalization, mimicking the synaptotoxic cascade induced by A-beta.",
    "example": "PrPC knockout mice are resistant to both A-beta-induced and alpha-synuclein-induced long-term potentiation deficits.",
    "id": "nd-131",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Cathepsin B and D in Lysosomal Degradation of Aggregates",
    "prompt": "Within neuronal lysosomes, the endopeptidase Cathepsin D (CTSD) plays a crucial protective role against synucleinopathy because it:",
    "options": [
      "Cleaves wild-type and mutant alpha-synuclein at multiple specific sites, degrading monomers and preventing fibril seeding",
      "Directly phosphorylates alpha-synuclein at Ser129",
      "Translocates alpha-synuclein into the mitochondrial intermembrane space",
      "Converts alpha-synuclein into insoluble neuromelanin granules"
    ],
    "answer": 0,
    "explain": "Cathepsin D is the primary lysosomal aspartyl protease responsible for alpha-synuclein degradation. CTSD cleaves alpha-synuclein between residues 40-41 and in the C-terminus, dismantling monomers and slowing aggregation. Loss of Cathepsin D leads to massive alpha-synuclein accumulation.",
    "example": "Deficiency of Cathepsin D causes severe congenital neuronal ceroid lipofuscinosis and early neurodegeneration with widespread synuclein pathology.",
    "id": "nd-132",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "SARM1 Small-Molecule Inhibitors in Neuroprotection",
    "prompt": "SARM1 executes Wallerian axonal degeneration via its NADase activity. Novel small-molecule SARM1 inhibitors under clinical development act by:",
    "options": [
      "Binding to an allosteric pocket within the catalytic TIR domain, competitively or allosterically blocking NAD+ hydrolysis and preserving axonal energy metabolism",
      "Inactivating the proteasome",
      "Inhibiting voltage-gated calcium influx",
      "Preventing neurofilament transcription"
    ],
    "answer": 0,
    "explain": "SARM1 inhibitors bind either to the allosteric NMN-sensing pocket in the ARM domain (preventing activation) or directly into the catalytic cleft of the TIR domain, preventing NAD+ cleavage. By preserving local axonal NAD+ and ATP, these compounds prevent axonal degeneration following traumatic, toxic, or genetic injury.",
    "example": "In preclinical models of paclitaxel-induced peripheral neuropathy and ALS, SARM1 inhibitors preserve distal axon integrity and maintain neuromuscular function.",
    "id": "nd-133",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "AAV-Mediated AADC Gene Therapy for Parkinson's Disease",
    "prompt": "AAV2-hAADC gene therapy delivers the gene for aromatic L-amino acid decarboxylase directly into the bilateral putamen of Parkinson's patients to:",
    "options": [
      "Enable striatal neurons to autonomously convert orally administered L-DOPA into dopamine, bypassing degenerated substantia nigra projection terminals",
      "Regenerate damaged dopamine axons back to the substantia nigra",
      "Block all dopamine degradation by MAO-B",
      "Prevent alpha-synuclein from entering the putamen"
    ],
    "answer": 0,
    "explain": "As Parkinson's progresses, the loss of striatal dopamine terminals depletes endogenous AADC, rendering oral L-DOPA ineffective and unpredictable. Delivering AAV2-hAADC to striatal neurons restores high-efficiency conversion of L-DOPA to dopamine directly at postsynaptic target sites, dramatically reducing motor fluctuations.",
    "example": "Long-term follow-up of AAV2-hAADC clinical trials demonstrated persistent transgene expression and sustained clinical improvements in motor 'on' time.",
    "id": "nd-134",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Deep Brain Stimulation (DBS) Electrophysiological Mechanism",
    "prompt": "High-frequency electrical stimulation (130-185 Hz) of the subthalamic nucleus (STN) in Parkinson's disease relieves motor symptoms primarily by:",
    "options": [
      "Disrupting pathologically synchronized beta-band (13-30 Hz) oscillatory activity throughout the cortico-basal ganglia-thalamocortical motor loop",
      "Stimulating the proliferation of endogenous neural stem cells in the subventricular zone",
      "Directly synthesizing dopamine within the internal globus pallidus",
      "Permanently destroying overactive glutamatergic neurons in the STN"
    ],
    "answer": 0,
    "explain": "Dopamine depletion causes neurons in the STN and globus pallidus to fire in pathologically synchronized bursts in the beta frequency range (13-30 Hz), which jams voluntary motor cortical throughput. High-frequency DBS regularizes and overrides this pathological rhythm, replacing it with high-frequency non-informational patterns that uncouple the motor loop.",
    "example": "Adaptive closed-loop DBS uses real-time local field potential (LFP) sensing to deliver stimulation pulses only when pathological beta-bursts emerge.",
    "id": "nd-135",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Cross-Seeding Between Misfolded Proteins",
    "prompt": "In neurodegenerative multimorbidities, 'cross-seeding' refers to the pathological phenomenon wherein:",
    "options": [
      "Aggregates of one misfolded protein (e.g., A-beta fibrils) act as a conformational heterologous template that nucleates the polymerization of a distinct protein (e.g., tau or alpha-synuclein)",
      "Neurons transfer mitochondria to astrocytes via tunneling nanotubes",
      "Microglia transfer lysosomes to oligodendrocytes",
      "Prion proteins are cleared through the choroid plexus"
    ],
    "answer": 0,
    "explain": "Cross-seeding occurs when structural motifs on the surface of pre-existing fibrils (such as A-beta plaques) interact with monomeric forms of another amyloidogenic protein (such as tau or alpha-synuclein), drastically lowering the critical nucleation energy barrier and triggering secondary heterologous aggregation.",
    "example": "A-beta plaques in AD frequently promote the rapid secondary nucleation and neocortical spread of tau and alpha-synuclein pathologies.",
    "id": "nd-136",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "cGAS-STING Innate Immunity in Neurodegeneration",
    "prompt": "In neurons and glia deficient in PINK1 or Parkin, severe mitochondrial stress activates the cGAS-STING pathway because:",
    "options": [
      "Damaged mitochondria leak circular mitochondrial DNA (mtDNA) into the cytoplasm, where the DNA sensor cGAS recognizes it and synthesizes cGAMP to activate STING",
      "STING binds directly to complex I of the electron transport chain",
      "cGAS degrades all cellular RNA in the nucleus",
      "Damaged mitochondria release lysosomes directly into the extracellular fluid"
    ],
    "answer": 0,
    "explain": "Impaired mitophagy leads to mitochondrial membrane rupture and release of oxidized mtDNA into the cytosol. Cyclic GMP-AMP synthase (cGAS) binds cytosolic mtDNA, synthesizing 2'3'-cGAMP, which binds STING on the ER. STING activates TBK1 and IRF3, driving sustained, destructive type-I interferon production.",
    "example": "Genetic knockout of Sting in Pink1- or Parkin-deficient mice completely prevents motor neurodegeneration and suppresses circulating pro-inflammatory cytokines.",
    "id": "nd-137",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "PET Radiotracers for Neuroinflammation: TSPO",
    "prompt": "Positron emission tomography (PET) imaging of neuroinflammation in living Alzheimer's and ALS patients commonly utilizes radioligands (e.g., 11C-PBR28, 18F-DPA-714) targeting:",
    "options": [
      "The 18 kDa translocator protein (TSPO) localized on the outer mitochondrial membrane of reactive microglia and reactive astrocytes",
      "Cannabinoid CB1 receptors on axon terminals",
      "Dopamine transporter DAT in the striatum",
      "Glucose transporter GLUT3 on pyramidal neurons"
    ],
    "answer": 0,
    "explain": "TSPO (formerly peripheral benzodiazepine receptor) is expressed at very low levels in healthy brain parenchyma but is dramatically upregulated on the outer mitochondrial membranes of activated microglia and reactive astrocytes during neuroinflammation.",
    "example": "TSPO-PET binding correlates inversely with cognitive scores and reveals focal microglial activation in regions showing active neurodegeneration.",
    "id": "nd-138",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Splice-Switching ASOs for UNC13A Cryptic Exons",
    "prompt": "To rescue motor neurons from TDP-43 loss-of-function in ALS, splice-switching antisense oligonucleotides (ASOs) are designed to target UNC13A pre-mRNA by:",
    "options": [
      "Sterically blocking the cryptic splice acceptor and donor sites, preventing cryptic exon inclusion and restoring full-length functional UNC13A protein synthesis",
      "Cleaving the UNC13A transcript using RNase H1",
      "Directly binding and dissolving cytoplasmic TDP-43 aggregates",
      "Phosphorylating Stathmin-2 at Ser25"
    ],
    "answer": 0,
    "explain": "Splice-switching ASOs hybridize directly over the cryptic splice junctions in UNC13A intron 20. By sterically preventing the spliceosome from accessing the cryptic splice sites, the ASO forces normal exon 20 to exon 21 splicing, completely restoring full-length UNC13A expression even in cells totally lacking nuclear TDP-43.",
    "example": "In TDP-43-depleted human iPSC-derived motor neurons, UNC13A-targeted splice-switching ASOs rescue synaptic vesicle release and extend neuronal survival.",
    "id": "nd-139",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Zinc and Copper in A-beta Oligomerization and Aggregation",
    "prompt": "At glutamatergic synapses, transition metals zinc (Zn2+) and copper (Cu2+) modulate amyloid plaque deposition because:",
    "options": [
      "Synaptically co-released Zn2+ (via vesicular transporter ZnT3) binds to histidine residues (His6, His13, His14) on A-beta, neutralizing negative charges and accelerating oligomer precipitation",
      "Zinc dissolves pre-formed amyloid fibrils into harmless water-soluble monomers",
      "Copper blocks all beta-secretase cleavage of APP",
      "Zinc and copper act as obligate cofactors for gamma-secretase"
    ],
    "answer": 0,
    "explain": "High concentrations of free Zn2+ (~100-300 uM) are released into the synaptic cleft from glutamatergic vesicles via ZnT3. Zn2+ coordinates three conserved histidine residues in the N-terminus of A-beta, driving rapid crosslinking and precipitation into amorphous plaques.",
    "example": "Genetic knockout of the vesicular zinc transporter ZnT3 in APP transgenic mice drastically reduces amyloid plaque deposition in the hippocampus.",
    "id": "nd-140",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "TREM2 Carboxy-Terminal Stub Cleavage by Gamma-Secretase",
    "prompt": "Following ADAM10-mediated shedding of soluble TREM2 (sTREM2), the remaining membrane-anchored carboxy-terminal fragment (CTF-TREM2) is degraded by:",
    "options": [
      "Intramembrane cleavage by the presenilin gamma-secretase complex, terminating intracellular signaling",
      "Direct retrotranslocation into the nucleus to act as a transcription factor",
      "Extracellular shedding via secretory lysosomes",
      "Covalent phosphorylation by LRRK2"
    ],
    "answer": 0,
    "explain": "Like APP and Notch, TREM2 is a physiological substrate for sequential regulated intramembrane proteolysis (RIP). After ADAM10 cleaves the ectodomain, the remaining 9 kDa CTF is cleaved within the membrane by gamma-secretase. Gamma-secretase inhibition leads to toxic accumulation of CTF-TREM2 in microglia.",
    "example": "This shared proteolytic processing links APP and TREM2 metabolism to the same intramembrane cleaving enzyme complex.",
    "id": "nd-141",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Hereditary Spastic Paraplegia: Spastin Microtubule Severing",
    "prompt": "Mutations in Spastin (SPAST), an ATP-dependent AAA-family microtubule-severing enzyme, cause the most common form of autosomal dominant Hereditary Spastic Paraplegia (SPG4) because:",
    "options": [
      "Impaired microtubule severing disrupts axonal endoplasmic reticulum morphogenesis and organelle transport along the longest corticospinal axons",
      "Spastin mutations cause rapid apoptosis of all upper motor neuron cell bodies in infancy",
      "Loss of spastin prevents neurotransmitter release at all GABAergic synapses",
      "Spastin mutations block the synthesis of myelin basic protein in Schwann cells"
    ],
    "answer": 0,
    "explain": "Spastin couples ATP hydrolysis to the mechanical pulling and severing of long stable microtubules into shorter pieces needed for transport. Corticospinal motor axons projecting up to one meter to the lumbar cord depend critically on spastin for ER network distribution; its loss triggers length-dependent dying-back axonopathy.",
    "example": "SPG4 patients develop slowly progressive spastic weakness and hyperreflexia confined predominantly to the lower extremities.",
    "id": "nd-142",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Tau PET Tracer Off-Target Binding to MAO-A/B",
    "prompt": "First-generation tau-PET radiotracers (such as 18F-Flortaucipir / AV-1451) exhibit problematic off-target binding in the basal ganglia, substantia nigra, and choroid plexus due to cross-reactivity with:",
    "options": [
      "Monoamine oxidases (MAO-A and MAO-B)",
      "Dopamine D2 receptors",
      "Voltage-gated sodium channels",
      "Glutamine synthetase in astrocytes"
    ],
    "answer": 0,
    "explain": "18F-Flortaucipir binds paired helical filament tau in cortical tangles with high affinity, but also binds off-target to MAO-A and MAO-B in the striatum and brainstem. Second-generation tracers (e.g., 18F-MK-6240, 18F-PI-2620) were engineered with structural modifications that completely eliminate MAO cross-reactivity.",
    "example": "Second-generation tau tracers allow clean, uncontaminated imaging of tau pathology in subcortical nuclei and early Braak stages.",
    "id": "nd-143",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Cofilin-Actin Rod Formation Downstream of A-beta",
    "prompt": "In Alzheimer's disease dendritic spines, soluble A-beta oligomers induce synaptic spine collapse by triggering the assembly of cofilin-actin rods through:",
    "options": [
      "Activation of the phosphatase Slingshot-1 (SSH1), which dephosphorylates and activates cofilin to crosslink F-actin into rigid pathological paracrystalline rods",
      "Direct covalent cleavage of beta-actin by beta-secretase",
      "Phosphorylation of cofilin by LIM kinase to shut off actin turnover",
      "Degradation of actin monomers by the 20S proteasome"
    ],
    "answer": 0,
    "explain": "A-beta activates calcineurin and Slingshot-1 (SSH1). SSH1 dephosphorylates Ser3 of cofilin, converting inactive cofilin into an active F-actin severing/binding protein. When active cofilin reaches an equimolar ratio with actin in dendritic shafts, it forms cofilin-actin bundles ('rods') that interrupt vesicle trafficking and spine maintenance.",
    "example": "Knockdown of cofilin or preventing cofilin dephosphorylation preserves dendritic spine density and rescues LTP in APP transgenic mice.",
    "id": "nd-144",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Nuclear RNA Buffering Prevents FUS Phase Transitions",
    "prompt": "Biophysical studies by Maharana et al. (Science 2018) demonstrated that FUS and other prion-like RNA-binding proteins remain soluble in the nucleus but aggregate in the cytoplasm because:",
    "options": [
      "The nucleus contains an exceptionally high concentration of diverse RNA molecules that acts as an electrostatic buffer, preventing homotypic FUS phase transitions into solid aggregates",
      "The nucleus contains no ATP to drive aggregation",
      "Cytoplasmic temperatures are 5 degrees warmer than the nucleus",
      "The nuclear pore complex actively degrades aggregated proteins"
    ],
    "answer": 0,
    "explain": "RNA acts as a natural macromolecular solubilizer. In the nucleus, the high RNA-to-protein ratio satisfies the multivalent binding capacity of FUS's RRM and zinc finger domains, keeping FUS in a dynamic soluble or liquid-like state. When mutant FUS mislocalizes to the cytoplasm where RNA concentrations are lower, the protein undergoes unconstrained homotypic interactions, condensing into solid amyloid fibrils.",
    "example": "Adding synthetic non-specific RNA oligonucleotides to phase-separated cytoplasmic FUS droplets disperses them back into soluble monomers.",
    "id": "nd-145",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Somatic Mutation Accumulation in Aging Single Neurons",
    "prompt": "Single-cell whole-genome sequencing of individual human post-mitotic cortical neurons (Lodato et al., Science 2018) revealed that throughout life, normal human neurons accumulate somatic single nucleotide variants (sSNVs) at a rate of approximately:",
    "options": [
      "15 to 25 novel somatic mutations per neuron per year ('genomic clock'), elevated in neurodegenerative repair disorders",
      "Zero mutations because post-mitotic cells never replicate their DNA",
      "Over 100,000 mutations per week",
      "Mutations occur exclusively in mitochondrial genes, never in nuclear DNA"
    ],
    "answer": 0,
    "explain": "Even though neurons are permanently post-mitotic, continuous oxidative damage and transcription-associated single-strand breaks drive somatic mutagenesis at a steady rate of ~15-20 sSNVs per year throughout life. In Cockayne syndrome and xeroderma pigmentosum, this somatic mutational burden is accelerated by more than two-fold.",
    "example": "By age 80, a typical healthy cortical neuron harbors over 2,500 unique somatic point mutations across its genome.",
    "id": "nd-146",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Microglial Complement Receptor CR3 vs Scavenger Receptor SR-A",
    "prompt": "In the amyloid plaque microenvironment, microglial clearance of fibrillar A-beta versus microglial destruction of dendritic spines is distinguished by:",
    "options": [
      "Scavenger receptors (e.g., SR-A / SCARA1 and CD36) mediate beneficial A-beta clearance; whereas Complement Receptor 3 (CR3 / CD11b) mediates pathogenic phagocytosis of C3-tagged synapses",
      "CR3 clears A-beta while SR-A destroys synapses",
      "Both receptors perform identical functions with 100% molecular redundancy",
      "Microglia never engulf synapses in the adult brain"
    ],
    "answer": 0,
    "explain": "Microglia utilize class A scavenger receptors (SR-A / SCARA1) to bind and endocytose fibrillar A-beta plaques for lysosomal degradation, conferring neuroprotection. In contrast, microglial CR3 (integrin alpha-M-beta-2) specifically binds C3b-opsonized dendritic spines, driving inappropriate synaptic pruning in Alzheimer's disease.",
    "example": "Pharmacological or genetic inhibition of CR3 halts synapse loss in Alzheimer's models without impairing microglial plaque clearance.",
    "id": "nd-147",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Perivascular Astrocytic Endfoot AQP4 Polarization Loss in AD",
    "prompt": "In human Alzheimer's disease and aged brain tissue, the breakdown of glymphatic amyloid clearance is caused not simply by reduced Aquaporin-4 expression, but primarily by:",
    "options": [
      "Loss of polarized AQP4 localization at perivascular astrocytic endfeet, with AQP4 redistributing aberrantly across parenchymal somatic membranes",
      "Complete destruction of the AQP4 gene via somatic deletion",
      "Endothelial cells blocking the AQP4 channel pore with albumin",
      "Conversion of AQP4 into an amyloid-forming peptide"
    ],
    "answer": 0,
    "explain": "In healthy brains, AQP4 is concentrated exclusively at perivascular endfeet facing microvessels via dystrophin-syntrophin complexes. In Alzheimer's and vascular cognitive impairment, astrogliosis causes loss of this perivascular polarization; AQP4 disperses to the entire astrocytic soma, destroying the hydraulic gradient needed for directional convective CSF flow.",
    "example": "Post-mortem analysis shows that the degree of perivascular AQP4 depolarization correlates directly with cortical amyloid-beta burden and Braak tangle stage.",
    "id": "nd-148",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Endothelial P-Glycoprotein (ABCB1) Downregulation at the BBB in AD",
    "prompt": "Efflux of amyloid-beta monomers from the brain interstitial fluid across the blood-brain barrier into the systemic circulation depends critically on which ATP-binding cassette transporter down-regulated in Alzheimer's disease?",
    "options": [
      "P-glycoprotein (ABCB1 / MDR1)",
      "ABCA1",
      "ABCG2 / BCRP",
      "Cystic fibrosis transmembrane conductance regulator (CFTR)"
    ],
    "answer": 0,
    "explain": "P-glycoprotein (ABCB1) is localized to the luminal membrane of brain capillary endothelial cells and actively pumps A-beta monomers from endothelial cytoplasm into the capillary lumen. Progressive downregulation of endothelial ABCB1 with age and amyloid accumulation impairs A-beta efflux, promoting parenchymal and vascular retention.",
    "example": "Pharmacological restoration of endothelial P-glycoprotein expression in APP transgenic mice reduces brain A-beta burden and restores cognitive performance.",
    "id": "nd-149",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Cryptic Exon in PTPRD and KALRN Splicing by TDP-43",
    "prompt": "Beyond STMN2 and UNC13A, loss of nuclear TDP-43 in human neurons also causes aberrant cryptic exon inclusion in which gene encoding a key postsynaptic guanine nucleotide exchange factor?",
    "options": [
      "Kalirin (KALRN)",
      "SynGAP1",
      "PSD-95",
      "Neuroligin-1"
    ],
    "answer": 0,
    "explain": "High-throughput cryptic exon profiling demonstrated that TDP-43 represses cryptic exons across several critical synaptic plasticity genes, including Kalirin (KALRN, a Rho-GEF essential for dendritic spine maintenance) and protein tyrosine phosphatase receptor type D (PTPRD). Splicing of these cryptic exons disrupts synaptic signaling.",
    "example": "Loss of Kalirin expression following TDP-43 depletion drives rapid dendritic spine pruning in cortical pyramidal neurons.",
    "id": "nd-150",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of Patient-Derived A-beta-42 Fibrils",
    "prompt": "Atomic-resolution cryo-EM structures of A-beta-42 fibrils extracted directly from the cerebral cortex of sporadic and familial Alzheimer's disease patients (Yang et al., Science 2022) revealed that:",
    "options": [
      "Filaments consist of two intertwined protofilaments with an S-shaped fold enclosing a hydrophilic core, differing profoundly from synthetic in vitro assembled fibrils",
      "Filaments are identical in all structural respects to synthetic peptides folded in detergent micelles",
      "A-beta-42 filaments are formed strictly of cross-alpha helices rather than cross-beta sheets",
      "Filaments contain zero water molecules within the inter-protofilament interface"
    ],
    "answer": 0,
    "explain": "Yang et al. solved the first atomic cryo-EM structures of native A-beta-42 fibrils from human AD brains, revealing two distinct polymorphs (Type I and Type II) characterized by an S-shaped protofilament fold. Crucially, the authentic human brain fibril folds differed markedly from synthetic fibrils grown in test tubes.",
    "example": "This structural discovery established that in vitro screening against synthetic A-beta fibrils likely failed because candidate drugs targeted non-physiological fibril polymorphs.",
    "id": "nd-151",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Atomic Cryo-EM Fold of Parkinson's Disease Alpha-Synuclein",
    "prompt": "Cryo-EM structures of alpha-synuclein filaments isolated from human brains with Lewy Body Dementia and Parkinson's Disease (Schweighauser et al., 2020) resolved that the protofilament core:",
    "options": [
      "Encompasses residues 31-100 in a serpentine beta-sheet fold with a hydrophobic cleft surrounding residues Val74-Val77, leaving the negatively charged C-terminus accessible",
      "Spans residues 1-30 exclusively in an unfolded random coil",
      "Is composed entirely of four symmetrical alpha-helices",
      "Forms a hollow double-walled cylinder resembling a nuclear pore"
    ],
    "answer": 0,
    "explain": "The core of human Lewy-derived alpha-synuclein fibrils consists of residues 31-100 organized in a serpentine arrangement of Greek-key beta-sheets. The non-amyloid-beta component (NAC) region forms the central hydrophobic spine, while the unstructured C-terminal tail (residues 101-140) projects outward where Ser129 is phosphorylated.",
    "example": "Familial PD mutations (e.g., A53T, E46K, H50Q) map directly onto stabilizing hydrogen bonds and salt bridges within this cryo-EM core fold.",
    "id": "nd-152",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Single-Molecule Tracking of Tau on Microtubules",
    "prompt": "Single-molecule total internal reflection fluorescence (TIRF) microscopy of individual fluorescently labeled tau molecules interacting with taxol-stabilized microtubules demonstrated that:",
    "options": [
      "Tau molecules bind transiently via a 'kiss-and-run' mechanism with a dwell time of only ~40 milliseconds, continuously hopping along the microtubule lattice",
      "Tau molecules bind irreversibly as a rigid, static polymer that permanently freezes microtubule dynamics",
      "Tau moves directionally toward the plus-end powered by ATP hydrolysis",
      "Tau binds exclusively inside the hollow lumen of the microtubule cylinder"
    ],
    "answer": 0,
    "explain": "High-speed single-molecule tracking revealed that tau does not coat microtubules statically. Instead, individual tau monomers bind for only ~40 milliseconds before unbinding and rebinding. This rapid equilibrium stabilizes the microtubule polymer while allowing kinesin and dynein motors to walk along the lattice unimpeded.",
    "example": "Hyperphosphorylation increases the off-rate and reduces the dwell time, causing tau to detach completely into the cytosolic pool where it nucleates oligomers.",
    "id": "nd-153",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Mechanisms of Cognitive Resilience in High-Pathology Brains",
    "prompt": "Single-nucleus multi-omic profiling of 'resilient' individuals—who die with high loads of amyloid plaques and tau tangles but maintained normal cognition until death—uncovered that cognitive resilience is characterized by:",
    "options": [
      "Maintained expression of synaptic plasticity, antioxidant, and bioenergetic genes in cortical neurons, coupled with microglial transition into a protective, non-inflammatory DAM state",
      "Complete absence of microglial cells in the cerebral cortex",
      "A rare mutation that makes all NMDA receptors completely insensitive to glutamate",
      "Total loss of all astrocytes with replacement by neural stem cells"
    ],
    "answer": 0,
    "explain": "Cognitive resilience studies show that resilient brains have similar plaque and tangle burdens to demented brains, but their neurons maintain high expression of mitochondrial ETC genes, dendritic spine scaffolds (e.g., PSD-95, Shank3), and anti-inflammatory microglial programs, preventing synaptic loss.",
    "example": "Preservation of dendritic spine density and synaptic protein levels distinguishes resilient individuals from demented patients with identical neuropathological loads.",
    "id": "nd-154",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "RT-QuIC Ultrasensitive Seed Amplification for Prions and Synuclein",
    "prompt": "Real-Time Quaking-Induced Conversion (RT-QuIC) achieves femtogram-level diagnostic detection of misfolded alpha-synuclein and PrPSc in living patient CSF and skin biopsies by:",
    "options": [
      "Incubating patient biospecimens with recombinant monomeric protein substrate, applying intermittent vigorous shaking to fragment growing fibrils, and monitoring Thioflavin T fluorescence in real time",
      "Sequencing circulating cell-free DNA using Illumina next-generation sequencing",
      "Using mass spectrometry to quantify total protein concentrations after boiling in urea",
      "Measuring radioactive decay of trace copper isotopes"
    ],
    "answer": 0,
    "explain": "RT-QuIC exploits the self-propagating seeding activity of amyloidogenic proteins. When a patient sample containing minute traces of misfolded seeds is mixed with recombinant substrate and subjected to automated shaking cycles, the seeds template rapid fibril elongation. Thioflavin T dye binds newly formed cross-beta fibrils, yielding an exponential fluorescence curve with >95% clinical specificity.",
    "example": "The CSF alpha-synuclein RT-QuIC assay is now integrated into consensus research diagnostic criteria for Parkinson's disease and Dementia with Lewy Bodies.",
    "id": "nd-155",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Biophysics of Tau Condensate Aging into Irreversible Fibrils",
    "prompt": "In vitro and cellular biophysical studies of liquid-liquid phase separation (LLPS) demonstrated that liquid droplets of phosphorylated tau undergo 'aging' or hardening into solid cross-beta fibrils through:",
    "options": [
      "Slow conformational rearrangement within the crowded droplet interior, where high local tau concentration (>100 uM) overcomes the nucleation barrier to form stable beta-sheet oligomers",
      "Rapid evaporation of water from the droplet interior",
      "Covalent transamination by cytoplasmic transglutaminases",
      "Enzymatic phosphorylation of every threonine residue inside the droplet"
    ],
    "answer": 0,
    "explain": "Phase separation concentrates tau by 100- to 1,000-fold inside liquid condensates. While nascent droplets are fluid and exhibit fast fluorescence recovery after photobleaching (FRAP), prolonged molecular crowding inside the droplet enables adjacent microtubule-binding repeats (PHF6/PHF6*) to align, nucleating irreversible cross-beta fibrils.",
    "example": "Compounds that disperse liquid tau condensates or prevent droplet hardening prevent the formation of neurofibrillary tangles in living neurons.",
    "id": "nd-156",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "LRRK2 Type I vs Type II Kinase Inhibitors and Microtubule Binding",
    "prompt": "Structural biology and cryo-electron tomography of the Parkinson's kinase LRRK2 revealed that certain small-molecule kinase inhibitors induce a paradoxical, adverse cellular phenotype wherein:",
    "options": [
      "Type I ATP-competitive inhibitors lock the kinase domain in a 'closed' conformation that drives LRRK2 oligomerization into continuous helical polymers around microtubules, impairing axonal transport",
      "The inhibitors activate the ROC GTPase domain to hydrolyze all cellular GTP",
      "The inhibitors cleave LRRK2 into cytotoxic fragments",
      "The inhibitors convert LRRK2 into an active transcription factor"
    ],
    "answer": 0,
    "explain": "Type I LRRK2 kinase inhibitors (e.g., MLi-2) stabilize the active-like 'closed' kinase conformation. This structural shift paradoxically promotes LRRK2 binding to and filament assembly around cytoplasmic microtubules, disrupting kinesin-mediated vesicle transport and causing lung and kidney vacuolation in animal models.",
    "example": "Developing Type II inhibitors that lock the kinase domain in an 'open' inactive conformation avoids this paradoxical microtubule polymerizing toxicity.",
    "id": "nd-157",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of Human Huntingtin-HAP40 Complex",
    "prompt": "The cryo-electron microscopy structure of full-length human huntingtin in complex with Huntingtin-Associated Protein 40 (HAP40) at 3.0 Å resolution (Guo et al., Nature 2018) revealed that:",
    "options": [
      "Huntingtin consists of three large alpha-solenoid HEAT-repeat domains that wrap completely around a single long continuous alpha-helix of HAP40, stabilizing huntingtin against aberrant aggregation",
      "Huntingtin is a flat beta-sheet sandwich containing zero alpha-helices",
      "The polyglutamine tract forms an invariant rigid pore through the center of the complex",
      "HAP40 is an active protease that degrades mutant huntingtin"
    ],
    "answer": 0,
    "explain": "Guo et al. solved the structure of the 3,144-amino-acid huntingtin monomer bound to HAP40. Huntingtin adopts a modular alpha-helical solenoid architecture with three domains connected by flexible bridges that physically envelop HAP40. HAP40 binding locks huntingtin in a stable, compact monomeric conformation.",
    "example": "In Huntington's disease, polyglutamine expansion destabilizes the huntingtin-HAP40 interface, promoting conformational opening, proteolysis, and aggregation.",
    "id": "nd-158",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Structural Basis of TREM2-Lipid Interactions",
    "prompt": "Crystallographic and hydrogen-deuterium exchange mass spectrometry (HDX-MS) analyses of the TREM2 extracellular domain demonstrated that AD risk variants (such as R47H and T66M):",
    "options": [
      "Map directly to an exposed, basic CDR2-like surface loop that binds negatively charged phospholipids (e.g., phosphatidylserine, phosphatidic acid) and sulfatides, collapsing this binding cleft",
      "Disrupt the intracellular immunoreceptor tyrosine-based activation motif (ITAM)",
      "Prevent TREM2 association with the DAP12 signaling adaptor",
      "Increase ligand-binding affinity to induce toxic microglial hyperactivation"
    ],
    "answer": 0,
    "explain": "The TREM2 Ig-like domain possesses a positively charged surface patch formed by Arg47, Arg62, and Lys48. This basic patch coordinates the negatively charged headgroups of microbial and apoptotic membrane lipids (PtdSer, cardiolipin, sulfatides). The R47H mutation neutralizes this charge and destabilizes the loop, abolishing ligand binding.",
    "example": "Mutating Arg47 to histidine reduces microglial binding to lipidated APOE discs by >80%, preventing plaque compaction.",
    "id": "nd-159",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Chorioallantoic / Meningeal B-Cell Niches in Aging Brain",
    "prompt": "Single-cell mapping of dural and leptomeningeal immune niches during healthy brain aging revealed an age-associated accumulation of clonal:",
    "options": [
      "IgA-secreting plasma cells and age-associated B cells (ABCs) that localize around dural venous sinuses to form an immunological barrier against circulating pathogens",
      "Cytotoxic CD8+ T cells that deliberately perforate the pial membrane",
      "Resting mast cells containing zero histamine granules",
      "Embryonic macrophages that migrate into the lateral ventricles"
    ],
    "answer": 0,
    "explain": "Recent immunology studies revealed that the meninges contain an active B-cell and plasma cell niche. With aging, gut-primed IgA-secreting plasma cells and ABCs accumulate in peri-sinusoidal dural niches, serving as an immunological shield that traps pathogens entering via cranial venous blood before they penetrate brain parenchyma.",
    "example": "Disrupting the dural IgA plasma cell barrier increases parenchymal vulnerability to systemic inflammatory challenges and accelerates neurodegenerative decline.",
    "id": "nd-160",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM Transition State of Gamma-Secretase with Substrate",
    "prompt": "Cryo-EM structures of the active human gamma-secretase complex captured in the act of cleaving C83 and C99 substrates at 2.6 Å resolution (Zhou et al., Science 2019) demonstrated that:",
    "options": [
      "Substrate binding induces presenilin-1 transmembrane helices 2, 3, and 6 to rearrange, unwinding the substrate's transmembrane alpha-helix into an extended beta-strand that inserts between catalytic aspartates 257 and 385",
      "The substrate remains a rigid alpha-helix during peptide bond hydrolysis",
      "Nicastrin cleaves the substrate directly using a catalytic zinc atom",
      "The catalytic aspartate residues are exposed to the extracellular fluid"
    ],
    "answer": 0,
    "explain": "Zhou et al. captured the atomic transition state of gamma-secretase. Substrate binding forces the C-terminal transmembrane helix of C83/C99 to partially unwind into an extended beta-sheet, which forms an intermolecular three-stranded beta-sheet with PSEN1. This aligns the scissile peptide bond directly between Asp257, Asp385, and an activated catalytic water molecule.",
    "example": "This atomic snapshot revealed the precise binding pocket occupied by transition-state analogue inhibitors and gamma-secretase modulators (GSMs).",
    "id": "nd-161",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Metabolic Flux of Lactate in Neurons Under Tau Toxicity",
    "prompt": "Dynamic 13C metabolic flux analysis in human iPSC tri-culture models exposed to pathological tau fibrils demonstrated that synaptic terminals:",
    "options": [
      "Suffer early glycolytic arrest and upregulate mitochondrial oxidation of astrocyte-derived [13C]-lactate to sustain basal ATP levels, making them acutely vulnerable to monocarboxylate transporter blockade",
      "Completely shut down all mitochondrial oxygen consumption",
      "Switch exclusively to oxidizing medium-chain fatty acids",
      "Excrete all glucose as free fructose into the synaptic cleft"
    ],
    "answer": 0,
    "explain": "Pathological tau fibrils dissociate hexokinase-1 from mitochondria and impair synaptic glycolysis. To survive, synapses become critically dependent on the Astrocyte-Neuron Lactate Shuttle, oxidizing astrocytic lactate via MCT2 and LDH1. Inhibiting MCT2 rapidly triggers catastrophic synaptic bioenergetic collapse.",
    "example": "These findings explain why cognitive impairment in tauopathies can be acutely rescued in preclinical models by exogenous ketone or lactate administration.",
    "id": "nd-162",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Down Syndrome (Trisomy 21) Tau Filament Cryo-EM Fold",
    "prompt": "Cryo-electron microscopy of tau filaments extracted from individuals with Down syndrome (Trisomy 21) who developed Alzheimer's neuropathology (Falcon et al., Nature 2018) demonstrated that:",
    "options": [
      "The paired helical filament and straight filament folds are atom-for-atom identical to those from idiopathic sporadic Alzheimer's disease, despite continuous 3-copy APP gene overexpression from birth",
      "Down syndrome tau forms a completely novel four-layered fold unlike any other tauopathy",
      "Filaments consist exclusively of 3-repeat tau",
      "Filaments do not contain cross-beta sheets"
    ],
    "answer": 0,
    "explain": "Individuals with Down syndrome carry three copies of APP on chromosome 21 and inevitably develop Alzheimer's neuropathology by age 40. High-resolution cryo-EM showed that Down syndrome tau filaments adopt the exact identical atomic C-shaped protofilament fold as sporadic AD, proving that genetically driven amyloid overproduction templates an identical downstream tau filament structure.",
    "example": "This structural identity confirms that sporadic AD and Down syndrome-associated AD share the identical molecular tauopathy mechanism.",
    "id": "nd-163",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "In Vivo Two-Photon Imaging of Plaque Nucleation Kinetics",
    "prompt": "Landmark in vivo two-photon imaging studies of transgenic mouse neocortex (Meyer-Luehmann et al., Nature 2008) revolutionized amyloid biology by demonstrating that individual plaques:",
    "options": [
      "Nucleate and form extraordinarily rapidly within 24 to 48 hours, followed by progressive local microglial recruitment and slow growth of dystrophic neurites over subsequent weeks",
      "Require at least 10 years of continuous linear aggregation before an initial 10-micron fibrillar plaque emerges",
      "Dissolve spontaneously every night during slow-wave sleep",
      "Form exclusively inside the lumen of cerebral blood vessels before bursting into the parenchyma"
    ],
    "answer": 0,
    "explain": "Using cranial window two-photon microscopy, Meyer-Luehmann et al. demonstrated that fibrillar amyloid plaques appear abruptly: an unseeded locus transitions into a dense, thioflavin-S-positive plaque within 24-48 hours. Once formed, local microglia cluster around the core within 1-2 days, while adjacent axonal swellings and dystrophic neurites develop over subsequent weeks.",
    "example": "This finding proved that plaque nucleation is a fast phase-transition event rather than a gradual decades-long accumulation.",
    "id": "nd-164",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM and Cryo-ET Architecture of Intact Lewy Bodies",
    "prompt": "Cryo-electron tomography and correlative light and electron microscopy (CLEM) of intact human brain tissue (Shahmoradian et al., Nature Neuroscience 2019) revealed that the core of Lewy bodies is composed of:",
    "options": [
      "A crowded, chaotic mixture of membrane fragments, disrupted mitochondria, vesicles, and lipid droplets densely decorated with non-fibrillar and fibrillar alpha-synuclein, rather than pure protein fibrils alone",
      "A crystal of pure alpha-synuclein without any lipid or organelle content",
      "Purely extracellular amyloid surrounded by normal healthy cytoplasm",
      "Unfolded genomic DNA crosslinked by histones"
    ],
    "answer": 0,
    "explain": "Shahmoradian et al. utilized cryo-CLEM to image Lewy bodies in their native unperturbed state. Contrary to the classical textbook view of Lewy bodies as purely proteinaceous filament bundles, the core is predominantly composed of membrane fragments, clustered dysmorphic organelles (especially fragmented mitochondria), and autophagosomes trapped within an alpha-synuclein matrix.",
    "example": "This structural insight highlights that impaired organellar clearance and vesicular trafficking arrest are central drivers of Lewy body formation.",
    "id": "nd-165",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Glymphatic Dynamics in Idiopathic Normal Pressure Hydrocephalus",
    "prompt": "Dynamic contrast-enhanced 3D T1 MRI with intrathecal gadobutrol in human patients with idiopathic normal pressure hydrocephalus (iNPH) demonstrated that iNPH is characterized by:",
    "options": [
      "Delayed glymphatic tracer influx into the cerebral cortex, delayed parenchymal tracer clearance, and abnormal reflux of CSF into the lateral ventricles",
      "A ten-fold increase in glymphatic bulk flow velocity",
      "Total absence of cerebrospinal fluid in the subarachnoid space",
      "Immediate complete clearance of tracer within 10 minutes"
    ],
    "answer": 0,
    "explain": "Intrathecal MRI tracer imaging in iNPH patients reveals marked glymphatic impairment: convective tracer enhancement throughout the cerebral cortex is profoundly delayed, and washout is markedly prolonged. Ventricular reflux occurs due to elevated CSF outflow resistance at the arachnoid villi and dural lymphatics.",
    "example": "CSF shunting procedures in iNPH patients restore glymphatic clearance rates, correlating with clinical improvement in gait, continence, and cognition.",
    "id": "nd-166",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Somatic LINE-1 Retrotransposition in Single Aging Neurons",
    "prompt": "Single-cell whole-genome sequencing and retrotransposon capture profiling in human aging brains demonstrated that somatic long interspersed nuclear element-1 (LINE-1 / L1) insertions:",
    "options": [
      "Occur mosaicly in individual post-mitotic cortical neurons, increasing in frequency in ATM-deficient and senescent cells to drive genomic mosaicism and transcriptional heterogeneity",
      "Replicate like bacteriophages to lyse neuronal membranes",
      "Are completely silenced by maternal imprinting with zero insertions in the nervous system",
      "Occur exclusively in microglial cells and never in neurons"
    ],
    "answer": 0,
    "explain": "Post-mitotic neurons retain somatic retrotransposition activity. While baseline rates are low (~0.1-1 novel insertion per cell), failure of heterochromatin maintenance or DNA repair (e.g., loss of ATM or SIRT6) allows active LINE-1 elements to escape repression, retrotransposing into protein-coding genes and generating somatic genomic mosaicism in aging brains.",
    "example": "Nucleoside reverse transcriptase inhibitors (NRTIs) that block LINE-1 reverse transcriptase are under clinical study to reduce retrotransposition-induced neuroinflammation.",
    "id": "nd-167",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Single-Molecule Optical Dimerization Transition of A-beta-42",
    "prompt": "Single-molecule fluorescence and nanoscopic spectroscopy of native A-beta-42 peptides diffusing on supported lipid bilayers demonstrated that the critical rate-limiting nucleation step for cytotoxicity is:",
    "options": [
      "The structural transition from an unstable, flexible monomeric state into a quasi-stable, membrane-bound homodimer with high beta-sheet character",
      "The formation of a 1,000-subunit fibril core",
      "The irreversible cleavage of the peptide by membrane lipases",
      "Phosphorylation of the C-terminal alanine residue"
    ],
    "answer": 0,
    "explain": "Single-molecule photobleaching and FCS studies revealed that monomeric A-beta-42 interacts dynamically with ganglioside-containing bilayers without pore formation. The critical nucleation barrier is the dimerization step: once a stable beta-sheet-rich dimer forms, subsequent addition of monomers proceeds rapidly without an additional nucleation lag phase.",
    "example": "Molecules that specifically stabilize the monomeric state or prevent the dimer transition block subsequent membrane permeabilization and synaptic dysfunction.",
    "id": "nd-168",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Microfluidic Modeling of ALS Dying-Back Axonopathy",
    "prompt": "Compartmentalized microfluidic devices seeded with human iPSC-derived motor neurons and skeletal muscle myotubes (Birkaya et al., 2021) demonstrated that mutant TDP-43 or SOD1 toxicity begins with:",
    "options": [
      "Local axonal translation failure and neuromuscular junction (NMJ) dismantlement that retrogradely propagates toward the soma ('dying-back' axonopathy) long before cell body apoptosis occurs",
      "Apoptotic caspase activation in the cell nucleus while distal axons remain perfectly functional",
      "Muscle cell detachment without any nerve terminal involvement",
      "Direct phagocytosis of the cell soma by microfluidic glass surfaces"
    ],
    "answer": 0,
    "explain": "Microfluidic separation of motor neuron cell bodies from their distal axons and muscle targets proved that ALS is fundamentally a distal axonopathy. Local loss of mitochondrial transport, STMN2 depletion, and local ribosome stalling at the NMJ cause synaptic detachment weeks before caspase cleavage or somatic nuclear pyknosis emerges.",
    "example": "Axon-specific application of neurotrophic factors or local SARM1 inhibitors preserves NMJ connectivity even when somatic pathology persists.",
    "id": "nd-169",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Centenarian Epigenomic Architecture: Heterochromatin Preservation",
    "prompt": "Single-nucleus epigenomic and ATAC-seq profiling of frontal cortex from non-demented centenarians (>100 years of age) revealed that extreme cognitive longevity is characterized by:",
    "options": [
      "Remarkable preservation of constitutive heterochromatin (H3K9me3) marks around repetitive elements, suppressing endogenous retroviruses and retrotransposons that trigger sterile inflammation in typical aging",
      "Total loss of all DNA methylation across all chromosomes",
      "Hyperactivation of microglial pro-inflammatory cytokine genes",
      "Complete silencing of mitochondrial electron transport chain genes"
    ],
    "answer": 0,
    "explain": "Typical brain aging involves 'heterochromatin loss'—the gradual erosion of repressive H3K9me3 and DNA methylation marks from pericentromeric repeats and retrotransposons (LINE-1, HERVs). In non-demented centenarians, heterochromatin architecture is tightly preserved, preventing retrotransposon derepression and keeping cGAS-STING sterile neuroinflammation silenced.",
    "example": "SIRT6 and SUV39H1 methyltransferase maintenance are critical molecular correlates of this preserved centenarian heterochromatin shield.",
    "id": "nd-170",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Structural Basis of Methylene Blue (LMTX) Tau Inhibition",
    "prompt": "Biochemical and biophysical studies of hydromethylthionine (LMTX, a reduced derivative of methylene blue) demonstrated that it inhibits tau aggregation by:",
    "options": [
      "Selectively oxidizing cysteine residues (Cys291 and Cys322) within the microtubule-binding repeat domain to form an intramolecular disulfide bond that locks tau in an aggregation-incompetent monomeric conformation",
      "Cleaving tau into small peptide fragments via an intrinsic protease activity",
      "Coating the entire microtubule surface to block tau binding",
      "Phosphorylating tau at Ser214 to detach it from ribosomes"
    ],
    "answer": 0,
    "explain": "Hydromethylthionine targets the two cysteine residues in tau's repeat domain (Cys291 in R2 and Cys322 in R3). By promoting a compact intramolecular disulfide loop (or capping free thiols), it prevents the intermolecular crosslinking and beta-sheet alignment required for protofilament nucleation.",
    "example": "Phase 3 clinical trials evaluated hydromethylthionine as a tau aggregation inhibitor in mild-to-moderate Alzheimer's disease.",
    "id": "nd-171",
    "mode": "neurodegeneration",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Single-Cell Lineage Tracing of CHIP Mutations in Brain Macrophages",
    "prompt": "Clonal hematopoiesis of indeterminate potential (CHIP), driven by somatic mutations in hematopoietic stem cells (e.g., in DNMT3A, TET2), accelerates neurodegeneration because:",
    "options": [
      "Mutant myeloid clones infiltrate the cerebral perivascular spaces and meninges as pro-inflammatory border-associated macrophages, exacerbating vascular inflammation and plaque deposition",
      "CHIP mutations transform microglia into malignant gliomas",
      "CHIP mutations block all antibody production by B cells",
      "Mutant red blood cells fail to carry oxygen across the blood-brain barrier"
    ],
    "answer": 0,
    "explain": "CHIP mutations in TET2 or DNMT3A give peripheral blood monocytes a competitive advantage and a hyper-inflammatory phenotype. These mutant myeloid cells infiltrate brain borders (perivascular spaces, leptomeninges), secreting excessive IL-1beta and IL-6 that damage the BBB and accelerate Alzheimer's and ischemic pathology.",
    "example": "Individuals with high-variant-allele-fraction CHIP mutations exhibit a significantly increased hazard ratio for Alzheimer's disease and stroke.",
    "id": "nd-172",
    "mode": "neurodegeneration",
    "type": "choice"
  }
]
