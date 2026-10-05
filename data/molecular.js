// Neuroscience PhD Arena - MOLECULAR Question Bank (172 Curated Items)
window.C2_DATA = window.C2_DATA || {};
window.NEURO_DATA = window.C2_DATA;

window.C2_DATA.molecular = [
  {
    "id": "mol-001",
    "mode": "molecular",
    "level": 1,
    "type": "choice",
    "topic": "Polymerase Chain Reaction (PCR)",
    "prompt": "What are the three canonical temperature steps in a standard thermal cycling PCR cycle?",
    "options": [
      "Denaturation (~95°C), Annealing (~50-65°C), and Extension (~72°C)",
      "Lysis (~37°C), Elongation (~60°C), and Ligation (~95°C)",
      "Transcription (~42°C), Splicing (~55°C), and Translation (~70°C)",
      "Hybridization (~65°C), Quenching (~4°C), and Cleavage (~90°C)"
    ],
    "answer": 0,
    "explain": "A standard PCR cycle consists of: 1) Denaturation at ~94-98°C to melt dsDNA into single strands; 2) Annealing at ~50-65°C for primers to bind complementary sequences; and 3) Extension at ~68-72°C where thermostable DNA polymerase synthesizes nascent DNA.",
    "example": "Adjusting the annealing temperature is the critical variable to eliminate non-specific primer binding during mouse genotyping PCR."
  },
  {
    "id": "mol-002",
    "mode": "molecular",
    "level": 1,
    "type": "choice",
    "topic": "Western Blotting Principle",
    "prompt": "In SDS-PAGE, sodium dodecyl sulfate (SDS) is added to protein lysates to:",
    "options": [
      "Amplify intrinsic enzymatic activity",
      "Denature proteins and impart an approximately uniform negative charge-to-mass ratio",
      "Form covalent crosslinks between protein subunits",
      "Stain the gel blue for immediate visual inspection"
    ],
    "answer": 1,
    "explain": "SDS is an anionic detergent that denatures tertiary protein structures and coats the polypeptide chain with negative charges (~1.4 g SDS per g protein), allowing separation during electrophoresis based strictly on molecular weight (size).",
    "example": "Adding beta-mercaptoethanol or DTT alongside SDS breaks disulfide bridges, ensuring full linearization of multimeric protein complexes."
  },
  {
    "id": "mol-003",
    "mode": "molecular",
    "level": 1,
    "type": "choice",
    "topic": "Immunofluorescence Controls",
    "prompt": "When performing immunofluorescence on mammalian brain sections, autofluorescence that accumulates with age in lysosomes of neurons is primarily caused by:",
    "options": [
      "Green Fluorescent Protein (GFP)",
      "Glycogen granules",
      "Lipofuscin pigments",
      "Melatonin crystals"
    ],
    "answer": 2,
    "explain": "Lipofuscin ('age pigment') is an insoluble aggregate of oxidized, crosslinked proteins and peroxidized lipids that accumulates within post-mitotic neuronal lysosomes, emitting broad autofluorescence across green, red, and far-red spectra.",
    "example": "Treating aged human or mouse brain slices with Sudan Black B or TrueBlack reagent quenches lipofuscin autofluorescence prior to antibody labeling."
  },
  {
    "id": "mol-004",
    "mode": "molecular",
    "level": 1,
    "type": "choice",
    "topic": "Reverse Transcription PCR",
    "prompt": "In RT-qPCR, the enzyme responsible for synthesizing complementary DNA (cDNA) from a messenger RNA template is:",
    "options": [
      "DNA Polymerase I",
      "T4 Polynucleotide Kinase",
      "RNA Polymerase II",
      "Reverse Transcriptase (RNA-dependent DNA polymerase)"
    ],
    "answer": 3,
    "explain": "Reverse transcriptase converts extracted mRNA into stable single-stranded cDNA using either oligo(dT) primers targeting the poly(A) tail or random hexamer primers, enabling subsequent quantitative PCR amplification.",
    "example": "Engineered reverse transcriptases (such as SuperScript IV) exhibit reduced RNase H activity and increased thermostability for transcribing structured GC-rich transcripts."
  },
  {
    "id": "mol-005",
    "mode": "molecular",
    "level": 1,
    "type": "choice",
    "topic": "Agarose Gel Electrophoresis",
    "prompt": "During DNA agarose gel electrophoresis, nucleic acid fragments migrate toward the positive electrode (anode) because:",
    "options": [
      "The phosphodiester backbone carries a net negative charge at neutral pH",
      "Nitrogenous bases have strong positive charges",
      "Deoxyribose sugars carry net basic residues",
      "Agarose acts as a cationic surfactant"
    ],
    "answer": 0,
    "explain": "The phosphate groups in the DNA backbone are fully ionized at neutral electrophoresis pH (TAE or TBE buffer), giving DNA an invariant net negative charge that drives migration toward the positive anode.",
    "example": "Smaller DNA fragments navigate the porous agarose meshwork more rapidly than larger fragments, resolving by log molecular weight."
  },
  {
    "id": "mol-006",
    "mode": "molecular",
    "level": 2,
    "type": "choice",
    "topic": "Co-Immunoprecipitation (Co-IP)",
    "prompt": "To test whether two endogenous synaptic proteins form a physical complex in brain tissue via Co-IP, what type of lysis buffer must be used?",
    "options": [
      "A harsh denaturing buffer containing 2% SDS and 8 M urea",
      "A mild, non-denaturing buffer containing non-ionic detergents (e.g., 0.5-1% NP-40 or Triton X-100)",
      "Pure distilled water to induce hypotonic cell lysis",
      "Concentrated hydrochloric acid"
    ],
    "answer": 1,
    "explain": "Co-IP requires preserving native non-covalent protein-protein interactions. Non-ionic detergents like NP-40 or Triton X-100 solubilize cell and synaptic membranes without disrupting hydrophobic protein-protein binding interfaces.",
    "example": "Using 1% SDS or boiling lysates would disrupt the interaction between PSD-95 and NMDA receptor subunits, causing a false-negative Co-IP result."
  },
  {
    "id": "mol-007",
    "mode": "molecular",
    "level": 2,
    "type": "choice",
    "topic": "Viral Vector Packaging Limits",
    "prompt": "What is the approximate maximum functional packaging capacity for foreign genetic cargo in standard Adeno-Associated Viral (AAV) vectors?",
    "options": [
      "~1.5 kilobases (kb)",
      "~12.5 kilobases (kb)",
      "~4.7 kilobases (kb) between inverted terminal repeats (ITRs)",
      "~50 kilobases (kb)"
    ],
    "answer": 2,
    "explain": "Wild-type AAV has a genome of ~4.7 kb. Exceeding ~4.7-5.0 kb between the two 145-bp ITRs leads to incomplete capsid packaging, truncated genome delivery, and drastic drops in viral titer.",
    "example": "Large transgenes (such as SpCas9 fused to base editors or prime editors) exceed 4.7 kb and must be delivered using dual-AAV split-intein systems."
  },
  {
    "id": "mol-008",
    "mode": "molecular",
    "level": 2,
    "type": "choice",
    "topic": "In Situ Hybridization (RNAscope)",
    "prompt": "The high specificity and sensitivity of RNAscope in situ hybridization relies on pairing of which probe design to generate signal amplification?",
    "options": [
      "Direct hybridization of green fluorescent protein antibodies",
      "A single radioactive phosphorus-32 labeled nucleotide probe",
      "Biotinylated random nonamers that bind unspecifically to RNA hairpins",
      "Tandem 'ZZ' oligonucleotide probe pairs that must bind adjacent target regions to allow pre-amplifier binding"
    ],
    "answer": 3,
    "explain": "RNAscope uses 'ZZ' probe pairs. The bottom of each 'Z' binds target mRNA; only when two independent 'Z' probes hybridize immediately adjacent to each other do their upper halves create a contiguous binding site for the pre-amplifier, eliminating background off-target hybridization.",
    "example": "RNAscope allows multiplexed single-molecule visualization of low-copy transcripts like Trem2 and P2ry12 directly in frozen brain sections."
  },
  {
    "id": "mol-009",
    "mode": "molecular",
    "level": 2,
    "type": "choice",
    "topic": "Western Blot Loading Controls",
    "prompt": "Why can using GAPDH as a Western blot loading control yield misleading artifacts when studying brain ischemia or mitochondrial metabolic stress?",
    "options": [
      "GAPDH transcription and translation are dynamically modulated by cellular hypoxia, metabolic stress, and glycolysis shifts",
      "GAPDH is completely absent from all mammalian neurons",
      "GAPDH cannot be transferred onto PVDF membranes",
      "Antibodies against GAPDH cross-react irreversibly with beta-actin"
    ],
    "answer": 0,
    "explain": "GAPDH is a glycolytic enzyme whose expression is directly upregulated by hypoxia-inducible factor 1 (HIF-1α) and altered under metabolic stress. Using it as a normalizer in stroke, hypoxia, or neurodegeneration studies can obscure true changes in target protein levels; total protein normalization or cytoskeletal controls (e.g. β-tubulin) are preferred.",
    "example": "Total protein membrane stains (such as Ponceau S or REVERT) provide linear, unbiased normalization free from single-housekeeper expression shifts."
  },
  {
    "id": "mol-010",
    "mode": "molecular",
    "level": 3,
    "type": "choice",
    "topic": "Single-Nucleus vs Single-Cell RNA-seq",
    "prompt": "When profiling transcriptomes from frozen post-mortem human brain tissue, why is single-nucleus RNA-seq (snRNA-seq) universally preferred over single-cell RNA-seq (scRNA-seq)?",
    "options": [
      "Nuclei contain ten times more mature mRNA than the cytoplasm",
      "Intact human adult neurons with extensive axonal arbors cannot survive enzymatic and mechanical tissue dissociation without catastrophic cell lysis and loss of fragile populations",
      "Single-cell RNA-seq cannot detect transcription factors in any cell type",
      "Frozen tissue destroys the nuclear membrane while leaving the plasma membrane intact"
    ],
    "answer": 1,
    "explain": "Flash-frozen brain tissue ruptures plasma membranes. Moreover, complex adult neurons (e.g. Layer 5 pyramidal cells, Purkinje cells) are severely damaged during mechanical/enzymatic dissociation of intact cells. Extracting resilient nuclei (snRNA-seq) preserves unbiased representation of all neuronal and glial cell types without dissociation-induced transcriptional artifacts.",
    "example": "Droplet-based snRNA-seq (e.g. 10x Chromium) on isolated nuclei captures nascent nuclear pre-mRNA, accurately reflecting cellular transcriptomic states."
  },
  {
    "id": "mol-011",
    "mode": "molecular",
    "level": 3,
    "type": "choice",
    "topic": "Optogenetic Silencing Tools",
    "prompt": "Halorhodopsin (e.g. NpHR3.0) and Archaerhodopsin (e.g. ArchT) silence neuronal activity through which respective biophysical mechanisms?",
    "options": [
      "Both are non-selective cation channels that cause depolarization-block",
      "NpHR pumps potassium outward; Arch pumps sodium inward",
      "NpHR pumps chloride (Cl-) inward upon yellow light illumination; Arch pumps protons (H+) outward upon green/yellow light illumination",
      "NpHR cleaves synaptobrevin; Arch opens Cav2.2 channels"
    ],
    "answer": 2,
    "explain": "NpHR (from Natronomonas pharaonis) is an inward light-driven chloride pump (activated by ~590 nm yellow light), whereas Arch (from Halorubrum sodomense) is an outward proton pump (activated by ~566 nm green light). Both pump negative charge into or positive charge out of the cell, driving robust hyperpolarization to silence action potential generation.",
    "example": "Prolonged illumination of NpHR can alter the intracellular chloride equilibrium potential, whereas Arch avoids chloride shifts but can transiently alter intracellular pH."
  },
  {
    "id": "mol-012",
    "mode": "molecular",
    "level": 3,
    "type": "choice",
    "topic": "DREADD Chemogenetics Agonists",
    "prompt": "While Clozapine-N-oxide (CNO) was historically used to activate DREADD receptors, modern in vivo studies prefer Deschloroclozapine (DCZ) because:",
    "options": [
      "DCZ emits green fluorescence when bound to GPCRs",
      "CNO permanently binds and destroys DREADD receptors via covalent alkylation",
      "DCZ selectively excites microglia without affecting neurons",
      "CNO cannot cross the blood-brain barrier and undergoes back-metabolism in vivo to parent clozapine, which acts as a potent endogenous dopamine/serotonin antagonist"
    ],
    "answer": 3,
    "explain": "Gomez et al. (Science 2017) demonstrated that systemically administered CNO does not readily cross the BBB; instead, its behavioral effects are mediated by systemic back-conversion into clozapine, which binds endogenous D2, 5-HT2A, and histaminergic receptors. DCZ (Nagai et al. 2020) exhibits 100-fold higher potency, rapid BBB penetration, and high selectivity with negligible off-target binding at nanomolar doses.",
    "example": "Micro-doses of DCZ (1-3 μg/kg) rapidly recruit hM3Dq in primates and rodents without producing sedation or motor depression."
  },
  {
    "id": "mol-013",
    "mode": "molecular",
    "level": 3,
    "type": "choice",
    "topic": "Monosynaptic Retrograde Rabies Tracing",
    "prompt": "In the engineered rabies virus retrograde tracing system (Wickersham and Callaway), monosynaptic restriction is achieved by:",
    "options": [
      "Deleting the rabies glycoprotein (Delta-G), pseudotyping with avian EnvA, and providing glycoprotein (G) and TVA receptor strictly in trans via helper AAVs in target starter neurons",
      "Using wild-type rabies virus with attenuated neurovirulence",
      "Injecting rabies virus directly into cerebrospinal fluid",
      "Inhibiting all anterograde motor proteins with colchicine"
    ],
    "answer": 0,
    "explain": "The G-deleted rabies virus (EnvA-RVΔG-EGFP) cannot infect mammalian cells unless they express the avian receptor TVA. Once inside starter neurons, it uses the rabies glycoprotein (G) supplied in trans to assemble infectious particles that jump retrogradely across one synapse to presynaptic inputs. Because presynaptic neurons lack G, the virus cannot spread further.",
    "example": "Co-injecting Cre-dependent AAV-TVA and AAV-G into a Dopamine Transporter-Cre mouse allows mapping of all direct, monosynaptic inputs onto substantia nigra dopaminergic neurons."
  },
  {
    "id": "mol-014",
    "mode": "molecular",
    "level": 3,
    "type": "choice",
    "topic": "Chromatin Profiling: ATAC-seq",
    "prompt": "Assay for Transposase-Accessible Chromatin using sequencing (ATAC-seq) maps genome-wide chromatin accessibility by utilizing a hyperactive mutant of which enzyme?",
    "options": [
      "Micrococcal nuclease (MNase)",
      "Tn5 transposase loaded with sequencing adapters",
      "Cre recombinase",
      "DNase I"
    ],
    "answer": 1,
    "explain": "Hyperactive Tn5 transposase simultaneously cuts open, nucleosome-free regions of genomic DNA and ligates sequencing adapters ('tagmentation'). Subsequent PCR amplification and next-generation sequencing identify active promoters, enhancers, and transcription factor binding footprints genome-wide.",
    "example": "Single-cell ATAC-seq resolves cell-type-specific open chromatin landscapes across human cortical brain cells."
  },
  {
    "id": "mol-015",
    "mode": "molecular",
    "level": 4,
    "type": "choice",
    "topic": "Systemic AAV Capsid Engineering",
    "prompt": "The engineered capsid AAV-PHP.eB crosses the blood-brain barrier with extraordinary efficiency in C57BL/6 mice following intravenous injection because it binds which brain endothelial receptor?",
    "options": [
      "Low-density lipoprotein receptor-related protein 1 (LRP1)",
      "Transferrin receptor (TfR1)",
      "LY6A (Lymphocyte antigen 6 complex locus A)",
      "Insulin receptor"
    ],
    "answer": 2,
    "explain": "Deverman and colleagues engineered AAV-PHP.eB (derived from AAV9). Subsequent studies (Hordeaux et al., Batista et al. 2019) revealed that its dramatic CNS tropism is strictly dependent on binding the GPI-anchored endothelial protein LY6A. Because non-human primates and certain mouse strains (e.g. BALB/c) lack functional Ly6a expression on brain endothelia, AAV-PHP.eB fails to cross the BBB in primates.",
    "example": "A single tail-vein injection of AAV-PHP.eB transduces >70% of cortical and hippocampal neurons throughout the C57BL/6 mouse brain."
  },
  {
    "id": "mol-016",
    "mode": "molecular",
    "level": 4,
    "type": "choice",
    "topic": "Proximity Biotinylation (TurboID)",
    "prompt": "What major kinetic advantage does TurboID possess over first-generation BioID for mapping endogenous synaptic protein interactomes in neurons?",
    "options": [
      "TurboID targets proteins across an entire 50-micrometer radius",
      "TurboID operates only at temperatures above 60°C",
      "TurboID uses ATP-independent phosphorylation instead of biotin",
      "TurboID accomplishes robust biotinylation of neighboring proteins in 10 minutes, avoiding the 18 to 24-hour labeling periods required by BioID"
    ],
    "answer": 3,
    "explain": "Directed evolution of the bacterial BirA biotin ligase generated TurboID (Branon et al. 2018). TurboID generates reactive biotin-5'-AMP with dramatically higher catalytic efficiency, labeling neighboring proteins within a ~10-nm radius in just 10-30 minutes upon biotin addition, allowing temporal capture of dynamic synaptic signaling events.",
    "example": "TurboID fused to PSD-95 labels the postsynaptic proteome in cultured primary neurons within 15 minutes of exogenous biotin supplementation."
  },
  {
    "id": "mol-017",
    "mode": "molecular",
    "level": 4,
    "type": "choice",
    "topic": "Spatial Transcriptomics Methodologies",
    "prompt": "In spatial biology, image-based in situ hybridization methods (such as MERFISH) differ from array-based capture methods (such as standard 10x Visium) in that MERFISH offers:",
    "options": [
      "Subcellular, single-molecule optical resolution of a targeted gene panel, whereas standard Visium provides unbiased whole-transcriptome capture within 55-micrometer multi-cell spots",
      "Direct whole-genome sequencing of genomic DNA without RNA involvement",
      "Unbiased capture of all 20,000 genes at zero background",
      "Ability to record real-time action potentials"
    ],
    "answer": 0,
    "explain": "MERFISH (Multiplexed Error-Robust Fluorescence In Situ Hybridization) utilizes combinatorial binary barcoding and sequential imaging rounds to resolve individual mRNA molecules with ~100 nm optical precision for hundreds to thousands of pre-selected genes. Visium captures polyadenylated transcripts onto an array of barcoded 55-μm spots, providing broad unbiased profiling but pooling transcripts from 1-10 cells per spot.",
    "example": "MERFISH maps the subcellular dendritic localization of synaptic mRNAs (such as Camk2a and Arc) in intact brain tissue sections."
  },
  {
    "id": "mol-018",
    "mode": "molecular",
    "level": 4,
    "type": "choice",
    "topic": "Super-Resolution: Expansion Microscopy",
    "prompt": "Expansion Microscopy (ExM, Boyden lab) achieves super-resolution imaging of synaptic nanostructures on conventional diffraction-limited confocal microscopes by:",
    "options": [
      "Using two-photon lasers with ultra-short femtosecond pulses",
      "Physically expanding the biological tissue specimen isotropically using an embedded swellable polyacrylate hydrogel",
      "Deconvolving out-of-focus light with mathematical wave algorithms",
      "Freezing the specimen to absolute zero"
    ],
    "answer": 1,
    "explain": "ExM covalently anchors cellular proteins and fluorophores to an in situ synthesized swellable polyelectrolyte hydrogel (sodium polyacrylate). Following enzymatic proteolysis to homogenize mechanical properties, water addition expands the hydrogel isotropically 4- to 16-fold in each dimension, moving fluorophores apart and enabling ~20-70 nm spatial resolution on standard confocal microscopes.",
    "example": "ExM cleanly resolves the 20-30 nm synaptic cleft separating presynaptic Bassoon from postsynaptic PSD-95 without specialized STED/STORM hardware."
  },
  {
    "id": "mol-019",
    "mode": "molecular",
    "level": 5,
    "type": "choice",
    "topic": "Cryo-EM Structural Polymorphs of Amyloid Fibrils",
    "prompt": "Cryo-EM atomic resolution structures of tau filaments extracted from post-mortem human brains (Scheres and Goedert) established which paradigm-shifting principle in molecular neuropathology?",
    "options": [
      "Tau filaments are composed entirely of lipid micelles without protein backbone involvement",
      "All amyloid fibrils in the brain possess an identical, invariant tertiary fold regardless of clinical diagnosis",
      "Different tauopathies (e.g. Alzheimer's, Pick's disease, Corticobasal Degeneration) harbor distinct, disease-specific tau protofilament folds, proving they represent molecularly distinct conformers (strains)",
      "Synthetic recombinant tau fibrils grown in heparin adopt the exact same atomic structure as patient-derived Alzheimer's paired helical filaments"
    ],
    "answer": 2,
    "explain": "Cryo-EM structures solved by the Scheres and Goedert laboratories demonstrated that tau folds into distinct protofilament conformations in different diseases: Alzheimer's features a C-shaped cross-beta fold of both 3R and 4R tau; Pick's disease features an elongated 3R fold; CBD and PSP feature distinct 4R folds. Crucially, synthetic fibrils formed in vitro using heparin do NOT adopt the authentic patient brain-derived conformations.",
    "example": "Cryo-EM has revealed that diagnostic classification of neurodegenerative diseases can now be defined by the atomic cross-beta fold of patient-derived fibrils."
  },
  {
    "id": "mol-020",
    "mode": "molecular",
    "level": 5,
    "type": "choice",
    "topic": "Ex Vivo Dissociation Artifacts in Microglial Profiling",
    "prompt": "During enzymatic dissociation of mouse or human brain tissue at 37°C for single-cell transcriptomics, microglia undergo rapid artificial ex vivo activation characterized by induction of:",
    "options": [
      "Unregulated transcription of embryonic hemoglobin genes",
      "Complete degradation of ribosomal 18S and 28S RNA bands",
      "Spontaneous conversion into mature oligodendrocytes",
      "Immediate early genes (Fos, Jun, Egr1) and inflammatory heat shock proteins, which can be prevented by cold mechanical dissociation with transcriptional inhibitors"
    ],
    "answer": 3,
    "explain": "Marsh et al. (Nature Neuroscience 2022) and van den Brink et al. proved that standard warm enzymatic digestion (37°C for 30-45 min) triggers a massive ex vivo transcriptional artifact in microglia, rapidly inducing immediate early genes (c-Fos, Junb, Egr1) and inflammatory cytokines that masquerade as novel disease states. Performing mechanical dissociation on ice in the presence of actinomycin D and triptolide eliminates this artifact.",
    "example": "Including actinomycin D and anisomycin during cold brain tissue dissociation preserves true in vivo homeostatic microglial transcriptional states."
  },
  {
    "id": "mol-021",
    "mode": "molecular",
    "level": 2,
    "type": "choice",
    "topic": "Genetically Encoded Calcium Indicators",
    "prompt": "The GCaMP family of genetically encoded calcium indicators (e.g. GCaMP6s, jGCaMP8) detects neuronal calcium influx by fusing circular permutated EGFP to:",
    "options": [
      "Calmodulin (CaM) and the M13 peptide from myosin light-chain kinase",
      "Synaptotagmin-1 and SNAP-25",
      "Parvalbumin and Troponin C",
      "Rhodopsin and arrestin"
    ],
    "answer": 0,
    "explain": "GCaMP consists of circularly permuted green fluorescent protein (cpEGFP) fused to the Ca2+-binding protein calmodulin (CaM) and the CaM-target peptide M13. Ca2+ binding causes CaM to wrap around M13, altering the chromophore environment and dramatically increasing green fluorescence emission upon excitation.",
    "example": "In vivo two-photon calcium imaging of GCaMP6-expressing neurons resolves single action potentials and dendritic calcium transients in awake behaving mice."
  },
  {
    "id": "mol-022",
    "mode": "molecular",
    "level": 3,
    "type": "choice",
    "topic": "Translating Ribosome Affinity Purification (TRAP)",
    "prompt": "Translating Ribosome Affinity Purification (TRAP) and Ribo-seq profile cell-type-specific translation in complex brain tissue by genetically tagging:",
    "options": [
      "Transfer RNA (tRNA) with fluorescent quantum dots",
      "The ribosomal protein RPL10a with an epitope tag (e.g. EGFP) under a cell-type-specific promoter",
      "RNA Polymerase II with a nuclear retention signal",
      "Mitochondrial outer membrane proteins"
    ],
    "answer": 1,
    "explain": "Heintz and colleagues engineered the TRAP method: an EGFP tag is fused to ribosomal large subunit protein RPL10a under cell-type-specific promoters. Immunoprecipitating GFP from brain homogenates isolates translating polysomes specifically from target cell populations, yielding cell-type-specific mRNA profiles without requiring cell dissociation.",
    "example": "TRAP allows isolation of actively translated mRNAs from striatal D1 vs D2 medium spiny neurons directly from whole intact frozen striatal tissue."
  },
  {
    "id": "mol-023",
    "mode": "molecular",
    "level": 4,
    "type": "choice",
    "topic": "Fiber Photometry vs 2-Photon Imaging",
    "prompt": "In behavioral neuroscience, fiber photometry is widely used to record bulk fluorescent biosensor signals because it offers:",
    "options": [
      "Simultaneous recording of all 86 billion neurons in the human cortex",
      "Single-synapse diffraction-limited spatial resolution in the deep thalamus",
      "High temporal resolution bulk population calcium/dopamine dynamics from deep subcortical structures in freely moving animals via an implanted optical fiber",
      "Zero requirement for fluorescent proteins or light emission"
    ],
    "answer": 2,
    "explain": "Fiber photometry couples an implanted optical cannula (e.g. 200 or 400 μm core) to a spectrometer or photodetector. It records sum population fluorescence changes (such as GCaMP calcium transients or dLight dopamine fluctuations) from deep brain structures (e.g. VTA, striatum, amygdala) with millisecond precision in unconstrained, freely behaving mice.",
    "example": "Recording GRAB_DA or dLight with fiber photometry tracks rapid, sub-second dopamine transients during cue-reward associative learning."
  },
  {
    "id": "mol-024",
    "mode": "molecular",
    "level": 4,
    "type": "choice",
    "topic": "CUT&Tag vs ChIP-seq",
    "prompt": "Cleavage Under Targets and Tagmentation (CUT&Tag, Henikoff lab) provides a major advantage over traditional ChIP-seq for profiling histone marks in low-input brain samples because:",
    "options": [
      "It amplifies RNA instead of chromatin",
      "It sequences entire intact chromosomes without fragmenting DNA",
      "It works only on dead cells without requiring antibodies",
      "It uses a primary antibody-tethered Protein A-Tn5 transposase to cleave and ligate sequencing adapters strictly at chromatin target sites within intact nuclei, eliminating formaldehyde crosslinking and sonication"
    ],
    "answer": 3,
    "explain": "Traditional ChIP-seq requires harsh chemical crosslinking, sonication, and large cell inputs (>10^6 cells), yielding high background noise. CUT&Tag adds an antibody against a chromatin mark (e.g. H3K27ac), binds a Protein A-Tn5 transposase fusion, and activates tagmentation with Mg2+, generating sequencing libraries directly at target loci from as few as 100-1,000 isolated brain nuclei.",
    "example": "Single-cell CUT&Tag successfully maps histone modifications and active enhancer landscapes in rare neuronal subtypes."
  },
  {
    "id": "mol-025",
    "mode": "molecular",
    "level": 1,
    "type": "choice",
    "topic": "Western Blot Detection Methods",
    "prompt": "Compared to standard enzyme-based chemiluminescence (HRP/ECL), near-infrared fluorescence Western blotting (e.g. Li-Cor Odyssey) offers which significant quantitative advantage?",
    "options": [
      "A wide, linear dynamic range (>4 orders of magnitude) without film saturation, allowing simultaneous two-color multiplexed detection of phospho- and total protein on the same membrane",
      "Zero requirement for secondary antibodies",
      "Instantaneous visualization without requiring illumination or scanners",
      "Ability to measure protein translation in living humans"
    ],
    "answer": 0,
    "explain": "Chemiluminescence relies on an enzymatic reaction (HRP converting luminol) that rapidly saturates photographic film or CCDs, producing a narrow non-linear dynamic range. Near-infrared fluorescent dye-conjugated secondary antibodies (e.g. IRDye 680 and 800) emit photons proportional to antibody binding across >4 logs without saturation, enabling precise ratio quantification (e.g. phospho-protein / total protein).",
    "example": "Multiplexing with IRDye 680RD and 800CW allows simultaneous quantification of phospho-Akt and total Akt on the identical membrane band."
  },
  {
    "id": "mol-026",
    "mode": "molecular",
    "level": 2,
    "type": "choice",
    "topic": "In Vivo Microdialysis",
    "prompt": "In vivo intracerebral microdialysis is used in neuropharmacology to measure:",
    "options": [
      "Intracellular gene transcription rates inside individual mitochondria",
      "Extracellular interstitial fluid (ISF) concentrations of unbound neurotransmitters, metabolites, and soluble peptides in awake, behaving animals",
      "Resting membrane potentials in whole-cell configuration",
      "Cerebral blood flow velocity using Doppler ultrasound"
    ],
    "answer": 1,
    "explain": "A microdialysis probe containing a semipermeable membrane (e.g. 20-100 kDa molecular weight cutoff) is stereotaxically implanted into a target brain region and continuously perfused with artificial CSF. Molecules diffuse across the membrane down their concentration gradient, enabling sampling of extracellular dopamine, glutamate, or soluble Aβ in awake animals.",
    "example": "In vivo microdialysis in APP transgenic mice demonstrated that interstitial fluid Aβ levels rise during wakefulness and fall during sleep."
  },
  {
    "id": "mol-027",
    "mode": "molecular",
    "level": 3,
    "type": "choice",
    "topic": "FACS Isolation of Neuronal Nuclei",
    "prompt": "To purify neuronal nuclei away from glial nuclei from post-mortem human brain homogenates prior to single-nucleus sequencing or epigenomics, nuclei are stained and sorted by FACS using which marker?",
    "options": [
      "Iba1",
      "GFAP",
      "NeuN (RBFOX3), a neuron-specific nuclear splicing factor",
      "Myelin Basic Protein (MBP)"
    ],
    "answer": 2,
    "explain": "NeuN (encoded by RBFOX3) is an established, highly specific nuclear protein present in the vast majority of vertebrate post-mitotic neurons (with rare exceptions like Purkinje cells). Immunostaining isolated brain nuclei with fluorophore-conjugated anti-NeuN antibodies allows FACS gating to separate pure NeuN+ neuronal fractions from NeuN- glial fractions.",
    "example": "NeuN-based FACS gating yields 99% pure neuronal nuclear preparations for high-coverage ATAC-seq and DNA methylation profiling."
  },
  {
    "id": "mol-028",
    "mode": "molecular",
    "level": 5,
    "type": "choice",
    "topic": "Bimolecular Fluorescence Complementation (BiFC)",
    "prompt": "Bimolecular Fluorescence Complementation (BiFC) is used to directly visualize protein-protein interactions and oligomerization in living cells by:",
    "options": [
      "Expressing bacterial luciferase in the presence of luciferin",
      "Radiolabeling proteins with tritium and performing autoradiography",
      "Measuring fluorescence lifetime decay (FLIM) of monomeric rhodamine",
      "Splitting a fluorescent protein (e.g. Venus or GFP) into two non-fluorescent halves fused to two candidate proteins, which reconstitute functional fluorescence only upon direct physical interaction"
    ],
    "answer": 3,
    "explain": "BiFC splits a fluorescent protein (e.g. Venus) into N-terminal (VN) and C-terminal (VC) fragments. Neither fragment fluoresces on its own. When fused to proteins that interact (such as alpha-synuclein or tau monomers during early oligomerization), their close physical proximity allows the two halves to refold and reconstitute the fluorophore, emitting fluorescent signal.",
    "example": "BiFC allows spatial and temporal visualization of dimeric alpha-synuclein assembly in living primary hippocampal neurons."
  },
  {
    "level": 1,
    "topic": "SDS-PAGE Denaturing Mechanism",
    "prompt": "In SDS-PAGE, sodium dodecyl sulfate (SDS) prepares proteins for molecular weight separation primarily by:",
    "options": [
      "Denaturing tertiary structure and coating proteins with a uniform negative charge proportional to their polypeptide length (~1.4 g SDS per g protein)",
      "Selectively cleaving peptide bonds at lysine residues",
      "Forming covalent disulfide bonds between adjacent subunits",
      "Adding positive charges to drive proteins toward the cathode"
    ],
    "answer": 0,
    "explain": "SDS is an anionic detergent that disrupts non-covalent bonds, linearizing polypeptides and imparting a constant negative charge-to-mass ratio. Consequently, electrophoretic mobility through polyacrylamide gel pores depends strictly on molecular mass.",
    "example": "Western blot validation of synaptic scaffold PSD-95 resolves a characteristic immunoreactive band at approximately 95 kDa under SDS-PAGE conditions.",
    "id": "mol-029",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Reducing Agents in Protein Electrophoresis",
    "prompt": "Why are reducing agents such as beta-mercaptoethanol (BME) or dithiothreitol (DTT) routinely added to SDS-PAGE sample loading buffers?",
    "options": [
      "To prevent bacterial contamination of the polyacrylamide gel",
      "To reduce inter- and intra-molecular covalent disulfide bonds (S-S) to free sulfhydryl groups (-SH), ensuring complete protein unfolding",
      "To fluorescently stain the proteins for direct visualization",
      "To maintain alkaline pH in the running buffer"
    ],
    "answer": 1,
    "explain": "SDS denatures non-covalent interactions but cannot cleave covalent disulfide crosslinks between cysteine residues. Reducing agents like DTT or BME break disulfide bonds, allowing multimeric complexes to dissociate into monomeric polypeptide chains.",
    "example": "Boiling an antibody sample in SDS loading buffer with DTT separates it into 50 kDa heavy chains and 25 kDa light chains on the gel.",
    "id": "mol-030",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Bradford Protein Assay Chemistry",
    "prompt": "The Bradford protein quantification assay measures protein concentration based on an absorbance shift of Coomassie Brilliant Blue G-250 dye from:",
    "options": [
      "Green to yellow at 488 nm",
      "Colorless to deep purple at 562 nm via copper reduction",
      "Red/brown (465 nm) to blue (595 nm) upon electrostatic and hydrophobic binding to basic (especially arginine) and aromatic amino acids",
      "Infrared to ultraviolet"
    ],
    "answer": 2,
    "explain": "Under acidic conditions, Coomassie G-250 exists in a cationic red/brown form (absorbance peak 465 nm). Upon binding basic and aromatic amino acid residues in proteins, the dye converts to its unprotonated anionic blue form, shifting absorbance to 595 nm.",
    "example": "Standard curves generated with Bovine Serum Albumin (BSA) at 595 nm determine the exact microgram protein content of brain tissue homogenates.",
    "id": "mol-031",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "BCA Protein Assay Mechanism",
    "prompt": "The Bicinchoninic Acid (BCA) protein assay quantifies total protein by coupling the reduction of Cu2+ to Cu+ (the biuret reaction) with:",
    "options": [
      "Emission of bioluminescent light catalyzed by luciferase",
      "Fluorophore cleavage by endogenous proteases",
      "Precipitation of copper sulfate crystals",
      "Colorimetric chelation of two molecules of BCA with one Cu+ ion, forming a water-soluble purple complex with peak absorbance at 562 nm"
    ],
    "answer": 3,
    "explain": "Peptide bonds reduce cupric ions (Cu2+) to cuprous ions (Cu+) in an alkaline medium. Two molecules of bicinchoninic acid then chelate each Cu+ ion, generating an intense purple reaction product whose absorbance at 562 nm is linear over a wide protein concentration range.",
    "example": "Unlike the Bradford assay, the BCA assay is highly compatible with sample buffers containing non-ionic detergents like 1% Triton X-100 or NP-40.",
    "id": "mol-032",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Type II Restriction Endonucleases",
    "prompt": "Type II restriction endonucleases (such as EcoRI, BamHI, and HindIII) are molecular cloning workhorses because they:",
    "options": [
      "Recognize specific palindromic 4- to 8-base-pair DNA sequences and cleave predictable phosphodiester bonds at defined positions within or adjacent to the recognition site",
      "Randomly fragment DNA through oxidative cleavage",
      "Cleave exclusively RNA-DNA hybrid molecules",
      "Require ATP hydrolysis to translocate millions of base pairs before cutting"
    ],
    "answer": 0,
    "explain": "Type II restriction enzymes recognize symmetrical palindromic sequences (e.g. EcoRI recognizes 5'-GAATTC-3') and cleave within the motif without requiring ATP, generating either cohesive 'sticky' overhangs or flush 'blunt' ends that can be ligated.",
    "example": "Digesting a plasmid with EcoRI and HindIII produces non-compatible cohesive overhangs that enable directional cloning of a synaptic receptor cDNA insert.",
    "id": "mol-033",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Plasmid Vector Essential Elements",
    "prompt": "A standard plasmid cloning vector designed for propagation in Escherichia coli must contain which three minimal functional elements?",
    "options": [
      "A telomere, a centromere, and a histone octamer",
      "An origin of replication (ori), a selectable antibiotic resistance marker, and a multiple cloning site (MCS) containing unique restriction sites",
      "A viral capsid gene, a reverse transcriptase, and an envelope spike",
      "An 18S ribosomal RNA gene, a poly-A tail, and a 5' 7-methylguanosine cap"
    ],
    "answer": 1,
    "explain": "The origin of replication (e.g. ColE1/pUC ori) allows autonomous episomal replication in bacteria; the selectable marker (e.g. beta-lactamase for ampicillin resistance) ensures only transformed bacteria survive; and the MCS allows insertion of foreign DNA.",
    "example": "Transforming competent DH5-alpha E. coli with a pUC19 plasmid ligation mixture yields colonies exclusively on LB agar plates containing 100 μg/mL ampicillin.",
    "id": "mol-034",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Polyclonal vs Monoclonal Antibodies",
    "prompt": "In molecular neuroscience, what is the primary structural difference between polyclonal and monoclonal primary antibodies?",
    "options": [
      "Polyclonal antibodies only bind phosphorylated residues",
      "Monoclonal antibodies are composed of RNA, whereas polyclonals are proteins",
      "Polyclonal antibodies are an affinity-purified mixture of immunoglobulins secreted by multiple B-cell clones recognizing multiple distinct epitopes on the target protein, whereas monoclonal antibodies are produced by a single hybridoma clone and recognize a single specific epitope",
      "Monoclonal antibodies cannot be conjugated to fluorophores"
    ],
    "answer": 2,
    "explain": "Immunizing animals (rabbits, goats) yields polyclonal serum recognizing diverse surface epitopes, providing strong signal amplification but batch-to-batch variability. Monoclonals (from mouse hybridomas or recombinant cloning) recognize a single invariant epitope, ensuring supreme specificity and reproducibility.",
    "example": "A monoclonal antibody against the C-terminus of Gephyrin selectively labels inhibitory postsynaptic densities with zero cross-reactivity against related scaffolds.",
    "id": "mol-035",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Brain Tissue Paraformaldehyde Fixation",
    "prompt": "During histology and immunohistochemistry, 4% paraformaldehyde (PFA) preserves brain tissue morphology primarily by:",
    "options": [
      "Hydrolyzing all nucleic acids into free nucleotides",
      "Precipitating lipids through organic dehydration",
      "Freezing intracellular water into non-crystalline amorphous ice",
      "Forming covalent methylene bridge crosslinks (-CH2-) between free amino groups (especially lysine side chains) on adjacent proteins"
    ],
    "answer": 3,
    "explain": "PFA depolymerizes in solution to formaldehyde. Formaldehyde reacts rapidly with uncharged primary amines to form Schiff bases and hydroxymethyl intermediates, which react with adjacent peptides to create stable covalent methylene bridges that lock cellular architecture in place.",
    "example": "Transcardiac perfusion of an anesthetized mouse with ice-cold 4% PFA produces firm, well-fixed brain tissue suitable for vibratome sectioning.",
    "id": "mol-036",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Nissl Staining for Cytoarchitecture",
    "prompt": "The histological Nissl stain (using basic aniline dyes such as cresyl violet or thionin) visualizes neuronal somata and cortical lamination by binding electrostatically to:",
    "options": [
      "Negatively charged RNA within ribosomes and rough endoplasmic reticulum (Nissl substance / ergastoplasm)",
      "Phospholipids in the myelin sheath",
      "Microtubules in the axon initial segment",
      "Synaptic vesicles docked at the active zone"
    ],
    "answer": 0,
    "explain": "Because neurons sustain exceptionally high rates of protein synthesis, their somata are densely packed with rough endoplasmic reticulum and polyribosomes. Basic cationic dyes (cresyl violet) bind intensely to the phosphate backbone of ribosomal RNA, labeling somas while leaving unmyelinated neuropil pale.",
    "example": "Brodmann mapped the 52 classic human cytoarchitectonic cortical areas based on regional differences in laminar cell density and size revealed by Nissl staining.",
    "id": "mol-037",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Golgi-Cox Impregnation Technique",
    "prompt": "Camillo Golgi's classic 'reazione nera' (black reaction) and its modern Golgi-Cox modification visualizes complete individual neuronal dendritic trees with dendritic spines because:",
    "options": [
      "The stain selectively kills inhibitory interneurons",
      "Potassium dichromate and heavy metal salts (mercuric chloride / silver nitrate) randomly and completely impregnate only a tiny fraction (~1-5%) of neurons in their entirety while leaving neighbors unstained",
      "It labels every single neuron in the brain uniformly",
      "It requires fluorescent transgenic reporter mice"
    ],
    "answer": 1,
    "explain": "The unique power of Golgi staining lies in its extreme sparsity: by mechanisms involving localized crystal nucleation, silver/mercury chromate microcrystals fill only 1-5% of neurons completely from soma to distal dendritic spines, allowing individual arbor geometries to be traced without visual clutter.",
    "example": "Ramón y Cajal used Golgi impregnation to definitively establish the Neuron Doctrine, proving that neurons are contiguous independent individual cells rather than a continuous syncytium.",
    "id": "mol-038",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Reverse Transcription PCR cDNA Priming",
    "prompt": "In converting eukaryotic neuronal mRNA into complementary DNA (cDNA) via reverse transcriptase, which primer design specifically targets mature polyadenylated mRNAs?",
    "options": [
      "Gene-specific downstream antisense primers only",
      "Random hexamers",
      "Oligo(dT) primers",
      "Universal 16S primers"
    ],
    "answer": 2,
    "explain": "Mature eukaryotic mRNAs terminate in an enzymatic 3' polyadenylated tail (poly-A tail of 100-250 adenines). Oligo(dT) primers (chains of 12-18 thymidines) anneal specifically to this tail, initiating first-strand cDNA synthesis from the 3' end of mRNAs while excluding ribosomal and transfer RNAs.",
    "example": "First-strand cDNA synthesis using oligo(dT) primers followed by qPCR allows accurate quantification of brain-derived neurotrophic factor (Bdnf) transcript abundance.",
    "id": "mol-039",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "RT-qPCR Comparative Delta-Delta Ct Method",
    "prompt": "In quantitative real-time PCR (RT-qPCR), the Livak comparative 2^(-Delta Delta Ct) method calculates relative gene expression fold-change under the assumption that:",
    "options": [
      "Fluorescence is measured only after 50 cycles",
      "The reference gene is completely silent in control samples",
      "Genomic DNA contamination is 50% of the total sample",
      "Both the target gene and the reference housekeeping gene amplify with near 100% efficiency (doubling every PCR cycle, efficiency = 2.0)"
    ],
    "answer": 3,
    "explain": "The 2^(-ddCt) method normalizes target Ct to a stable reference gene (Gapdh or Actb) to yield dCt, and compares treated versus control dCt (ddCt). A 1-cycle decrease in ddCt represents a 2^1 = 2-fold upregulation, assuming doubling efficiency (E = 2.0).",
    "example": "RT-qPCR reveals a ddCt of -2.0 for c-Fos following electroconvulsive stimulation, indicating a 2^(-(-2)) = 4-fold induction of c-Fos mRNA.",
    "id": "mol-040",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Gibson Assembly Molecular Logic",
    "prompt": "Isothermal Gibson Assembly allows seamless, scarless joining of multiple overlapping DNA fragments in a single 50°C reaction using an enzymatic cocktail consisting of:",
    "options": [
      "A 5' to 3' exonuclease (T5 exonuclease), a DNA polymerase (Phusion), and a thermostable DNA ligase (Taq ligase)",
      "A restriction enzyme, an alkaline phosphatase, and reverse transcriptase",
      "CRISPR-Cas9, topoisomerase I, and RNA helicase",
      "DNAse I, proteinase K, and terminal transferase"
    ],
    "answer": 0,
    "explain": "T5 exonuclease chews back 5' ends of fragments sharing 20-40 bp sequence overlap, exposing single-stranded 3' overhangs that specifically anneal. Phusion polymerase fills in the remaining gaps, and Taq ligase covalently seals the nicks at 50°C in under an hour.",
    "example": "Constructing an optogenetic expression plasmid by assembling a CAG promoter, ChR2-mCherry cDNA, and a WPRE element into a digested viral backbone via Gibson assembly.",
    "id": "mol-041",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cell-Type-Specific Promoters in Neuroscience",
    "prompt": "To restrict expression of an optogenetic channel specifically to forebrain excitatory projection neurons in viral gene transfer, which promoter is most widely used?",
    "options": [
      "GFAP (glial fibrillary acidic protein) promoter",
      "CaMKIIa (calcium/calmodulin-dependent protein kinase II alpha) promoter",
      "hSyn (human synapsin-1) promoter",
      "mDLX (enhancer for Dlx5/6) promoter"
    ],
    "answer": 1,
    "explain": "The 1.3 kb or 0.4 kb mouse CaMKIIa promoter drives transgene expression selectively in forebrain glutamatergic pyramidal neurons (in neocortex and hippocampus) while sparing GABAergic interneurons. In contrast, GFAP targets astrocytes, mDLX targets GABAergic interneurons, and hSyn targets all neurons pan-neuronally.",
    "example": "Injecting AAV-CaMKIIa-ChR2-EYFP into hippocampal CA1 drives robust expression in CA1 pyramidal neurons with zero expression in parvalbumin-positive interneurons.",
    "id": "mol-042",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "WPRE Element in Viral Vectors",
    "prompt": "Why is the Woodchuck Hepatitis Virus Posttranscriptional Regulatory Element (WPRE) commonly placed in the 3' untranslated region of AAV and lentiviral transfer plasmids?",
    "options": [
      "It serves as a viral capsid protein",
      "It encodes an antibiotic resistance marker for mammalian selection",
      "It forms tertiary RNA stem-loop structures that promote nuclear mRNA export and prevent premature poly-A degradation, boosting transgene protein expression by 2- to 5-fold",
      "It drives reverse transcription of DNA into RNA"
    ],
    "answer": 2,
    "explain": "WPRE is a cis-acting RNA element that enhances processing, facilitates CRM1-independent nuclear export, and stabilizes the mRNA transcript against deadenylation, significantly elevating steady-state viral transgene protein levels in transduced brain tissue.",
    "example": "Comparing AAV vectors with and without WPRE demonstrates a 3-fold higher GCaMP6s fluorescence intensity when the WPRE cassette is included.",
    "id": "mol-043",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Co-Immunoprecipitation (Co-IP) Detergent Selection",
    "prompt": "When performing Co-Immunoprecipitation (Co-IP) to validate a physiological protein-protein interaction between two synaptic scaffolds, which lysis detergent is most appropriate?",
    "options": [
      "100% dimethyl sulfoxide (DMSO)",
      "A harsh ionic denaturing buffer containing 2% SDS and 8 M urea boiled at 95°C",
      "Pure acetone with 10% trichloroacetic acid",
      "A gentle non-ionic or zwitterionic detergent (e.g. 0.5-1% NP-40, Triton X-100, or digitonin)"
    ],
    "answer": 3,
    "explain": "Non-ionic detergents (NP-40, Triton X-100) solubilize plasma and vesicular membranes while preserving native non-covalent protein-protein interactions. Harsh ionic detergents (like SDS) or chaotropic agents (urea) denature quaternary and tertiary structures, dissociating physiological protein complexes.",
    "example": "Lysis of brain synaptosomes in 1% Triton X-100 enables efficient co-immunoprecipitation of NMDA receptor GluN1 subunits alongside postsynaptic scaffold PSD-95.",
    "id": "mol-044",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Chromatin Immunoprecipitation (ChIP) Formaldehyde Crosslinking",
    "prompt": "In classic Chromatin Immunoprecipitation (ChIP), treating neurons with 1% formaldehyde fixes protein-DNA interactions through:",
    "options": [
      "Reversible covalent crosslinks (~2 Å distance) between transcription factors or histones and nearby DNA bases, which can be reversed by heat incubation at 65°C",
      "Irreversible carbonization of the chromatin fiber",
      "Permanent cleavage of all linker DNA segments",
      "Phosphorylation of histone tail residues"
    ],
    "answer": 0,
    "explain": "Formaldehyde is a zero-length crosslinker that rapidly permeates cells, preserving in vivo protein-DNA and protein-protein complexes within 2 Å. Following chromatin sonication and antibody pull-down, overnight incubation at 65°C hydrolyzes the methylene crosslinks, yielding purified DNA fragments for qPCR or sequencing.",
    "example": "ChIP-qPCR using an anti-CREB antibody demonstrates activity-dependent recruitment of phosphorylated CREB to the Bdnf exon IV promoter following membrane depolarization.",
    "id": "mol-045",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "RNAscope Double Z-Probe Architecture",
    "prompt": "Advanced in situ hybridization using RNAscope achieves single-molecule RNA detection with virtually zero background signal primarily due to its:",
    "options": [
      "Use of radioactive 32P-labeled oligonucleotide ladders",
      "Paired double Z-probe design: signal amplification trees assemble only when two independent Z-probes hybridize contiguously side-by-side onto the target mRNA",
      "Complete enzymatic destruction of all ribosomal RNA prior to hybridization",
      "Application of 100°C boiling during the hybridization step"
    ],
    "answer": 1,
    "explain": "Each Z-probe has a target-binding site (14-25 nt), a spacer, and a tail sequence. A pre-amplifier can only bind across two adjacent hybridizing Z-probes (a 'ZZ pair'). Non-specific binding of a single isolated Z-probe cannot recruit the pre-amplifier, suppressing background noise and enabling single-molecule mRNA spot resolution.",
    "example": "Multiplex fluorescent RNAscope on mouse cortical slices cleanly distinguishes Vglut1 (Slc17a7) excitatory neurons from Vgat (Slc32a1) inhibitory interneurons with punctate resolution.",
    "id": "mol-046",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Whole-Cell Patch-Clamp Internal Solution Cs+ Substitution",
    "prompt": "When recording isolated excitatory postsynaptic currents (EPSCs) at depolarized potentials (e.g. holding at +40 mV to observe NMDA currents), why is potassium gluconate replaced with cesium methanesulfonate (Cs+) in the internal patch pipette solution?",
    "options": [
      "Cesium serves as an energy substrate for the Na+/K+ pump",
      "Cesium activates chloride channels to hyperpolarize the neuron",
      "Cesium ions block voltage-gated and inward-rectifying potassium channels from the intracellular side, preventing massive outward K+ currents that would compromise voltage-clamp control",
      "Cesium completely blocks all AMPA receptors"
    ],
    "answer": 2,
    "explain": "Depolarizing a patched neuron to +40 mV activates enormous outward delayed rectifier and leak potassium currents. Intracellular Cs+ (along with the quaternary blocker QX-314 to block voltage-gated Na+ channels) plugs K+ channels from the inside, eliminating outward K+ conductances and enabling clean voltage clamp of synaptic currents.",
    "example": "Measuring the NMDA/AMPA receptor ratio at -70 mV and +40 mV requires a Cs-based internal solution containing 5 mM QX-314.",
    "id": "mol-047",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Epitope Tagging Cleavage and Detection",
    "prompt": "The synthetic octapeptide FLAG tag (sequence DYKDDDDK) is particularly advantageous in biochemical neuroscience because:",
    "options": [
      "It binds directly to DNA promoter sequences",
      "It is completely hydrophobic and embeds within lipid droplets",
      "It emits intrinsic blue bioluminescence without cofactors",
      "It contains an enterokinase cleavage recognition sequence (DDDDK), allowing precise enzymatic removal of the tag after affinity purification"
    ],
    "answer": 3,
    "explain": "The hydrophilic FLAG octapeptide is highly immunogenic, allowing nanomolar-affinity isolation with anti-FLAG M2 monoclonal antibody resins. The five C-terminal residues (DDDDK) form the exact recognition site for bovine enterokinase, enabling cleavage directly after the lysine to release pristine recombinant protein.",
    "example": "Purifying recombinant AMPA receptor auxiliary subunits using an N-terminal 3xFLAG tag followed by elution with 3xFLAG competitive peptide or enterokinase digestion.",
    "id": "mol-048",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Dual-Luciferase Normalization Principle",
    "prompt": "In a Dual-Luciferase reporter assay used to study synaptic promoter regulation, why are two distinct luciferase enzymes (Firefly and Renilla) co-transfected into the same cells?",
    "options": [
      "Firefly luciferase reports on the experimental promoter activity, while constitutively driven Renilla luciferase serves as an internal control to normalize for differences in transfection efficiency and cell viability",
      "Both luciferases combine to form a heterodimeric fluorescent protein",
      "Renilla luciferase degrades the firefly luciferase substrate after 10 minutes",
      "Firefly luciferase requires ultraviolet light excitation"
    ],
    "answer": 0,
    "explain": "Transfection efficiency varies between culture wells. Firefly luciferase (from Photinus pyralis, utilizing beetle luciferin and ATP) measures the test promoter, while Renilla luciferase (from Renilla reniformis, utilizing coelenterazine) driven by a constitutive promoter (TK or SV40) normalizes well-to-well variability.",
    "example": "Measuring CRE-driven firefly luciferase luminescence divided by Renilla luminescence demonstrates true transcriptional activation downstream of Forskolin/PKA signaling.",
    "id": "mol-049",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Recombinant AAV Triple Transfection Packaging",
    "prompt": "Production of high-titer recombinant Adeno-Associated Virus (rAAV) vectors in HEK293T cells requires co-transfection of which three distinct plasmids?",
    "options": [
      "Three identical copies of the viral genome",
      "(1) The transgene expression plasmid flanked by AAV ITRs; (2) The Rep/Cap plasmid supplying replication and capsid proteins; (3) The Adenoviral helper plasmid supplying E2A, E4, and VA RNA genes",
      "A reverse transcriptase plasmid, an envelope glycoprotein plasmid, and a gag-pol plasmid",
      "A Cas9 plasmid, a guide RNA plasmid, and a donor template"
    ],
    "answer": 1,
    "explain": "AAV is a dependovirus requiring adenoviral helper genes. To ensure replication incompetence, the viral genome is split: the transgene carries only the ~145 bp Inverted Terminal Repeats (ITRs); Rep (replication) and Cap (capsid serotype) are provided on a second plasmid; and adenoviral helper genes (E2A, E4orf6, VA RNA) are on a third.",
    "example": "Harvesting HEK293T cells 72 hours post-triple-transfection followed by cell lysis and iodixanol gradient centrifugation yields >10^13 viral genomes (vg)/mL.",
    "id": "mol-050",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "AAV Capsid Serotype Tropism Differences",
    "prompt": "How does the in vivo neuroanatomical tropism of AAV-retro differ fundamentally from AAV1 and AAV9 in rodent brain circuit dissection?",
    "options": [
      "AAV-retro integrates into the host chromosome, while AAV1 and AAV9 do not",
      "AAV-retro infects only microglia, while AAV1 infects only astrocytes",
      "AAV-retro is efficiently taken up by axon terminals and transported retrogradely to label projection neuron somata, whereas AAV1 exhibits robust anterograde trans-synaptic spread and AAV9 exhibits broad local and systemic non-directional tropism",
      "AAV-retro requires pseudotyping with rabies glycoprotein to enter cells"
    ],
    "answer": 2,
    "explain": "Developed by Karpova, Schaffer, and colleagues (Neuron 2016), AAV-retro displays an engineered capsid peptide insert that dramatically boosts retrograde axonal transport, mapping inputs to injected target nuclei with 50-fold higher efficiency than wild-type serotypes.",
    "example": "Injecting AAV-retro-Cre into the dorsolateral striatum efficiently retrogradely transduces corticostriatal projection neurons across all layers of neocortex.",
    "id": "mol-051",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "FLEx / DIO Switch Recombination Mechanism",
    "prompt": "The Double-floxed Inverted Open reading frame (FLEx or DIO) switch ensures stable, zero-leakage Cre-dependent transgene expression by utilizing:",
    "options": [
      "A tetracycline-responsive transactivator domain",
      "A single pair of direct loxP repeats that excises a stop codon",
      "Bacterial flippase (Flp) recombinase acting on FRT sites",
      "Two pairs of orthogonal, heterotypic lox sites (e.g. loxP and lox2272) oriented in opposite directions; Cre inverts the coding sequence and excises one site from each pair, irreversibly locking the transgene in the sense orientation"
    ],
    "answer": 3,
    "explain": "Simple 'floxed-stop' cassettes can suffer from leaky transcription in neurons. The FLEx system clones the coding sequence in the reverse (antisense) orientation flanked by alternating antiparallel loxP and lox2272 sites. Cre first inverts the gene to the sense orientation, and then excises intervening sites, leaving two incompatible sites that prevent reverse inversion.",
    "example": "Injecting AAV-DIO-ChR2-EYFP into a DAT-Cre mouse guarantees that ChR2-EYFP is transcribed exclusively in Cre-expressing dopaminergic neurons with 0% leak in wild-type mice.",
    "id": "mol-052",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Monosynaptic Rabies Retrograde Circuit Tracing",
    "prompt": "In Edward Callaway's monosynaptic retrograde rabies tracing system, how is trans-synaptic viral transmission strictly restricted to exactly one synaptic step?",
    "options": [
      "The rabies genome lacks the glycoprotein gene (delta-G-RV) and is pseudotyped with EnvA; infection requires the TVA receptor on starter cells, and trans-synaptic spread requires supplying Rabies G in trans, which is absent in upstream presynaptic neurons",
      "Rabies virus naturally dies after traveling across one synapse",
      "A chemical inhibitor is injected into the brain 24 hours post-infection",
      "Presynaptic neurons degrade the rabies genome using CRISPR"
    ],
    "answer": 0,
    "explain": "EnvA-pseudotyped delta-G-RV can only infect cells expressing the avian TVA receptor. Once inside starter cells, supplying rabies glycoprotein G in trans allows new viral particles to assemble and bud across retrograde synapses. However, once in presynaptic afferents, no G is present, arresting further viral spread.",
    "example": "Using Cre-dependent AAV-FLEX-TVA-mCherry and AAV-FLEX-G in SST-Cre mice restricts rabies starter cells to somatostatin interneurons, labeling all direct monosynaptic inputs throughout the cortex.",
    "id": "mol-053",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "CRISPR-Cas9 NGG PAM and Cleavage Geometry",
    "prompt": "Wild-type Streptococcus pyogenes Cas9 (SpCas9) achieves target DNA cleavage through which precise biochemical mechanism?",
    "options": [
      "It cleaves DNA randomly 1,000 base pairs downstream of an ATG start codon",
      "It interrogates DNA for a 5'-NGG-3' Protospacer Adjacent Motif (PAM); after R-loop formation with the 20 nt guide RNA, the HNH domain cleaves the target strand and the RuvC domain cleaves the non-target strand, generating a blunt double-strand break 3 bp upstream of the PAM",
      "It deaminates cytosines without breaking the phosphodiester backbone",
      "It requires a 100-nucleotide single-stranded DNA donor template to initiate cutting"
    ],
    "answer": 1,
    "explain": "SpCas9 scanning locks onto 5'-NGG-3' PAMs in the target genome, melting adjacent DNA to test for guide RNA complementarity. The HNH catalytic domain cuts the RNA-paired target strand, while the RuvC-like domain cuts the displaced non-target strand, yielding a blunt DSB 3 nt upstream of PAM.",
    "example": "Repair of the blunt DSB by error-prone non-homologous end joining (NHEJ) introduces insertions or deletions (indels) that disrupt the open reading frame for functional gene knockout.",
    "id": "mol-054",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "CRISPRi vs CRISPRa Mechanism",
    "prompt": "How do CRISPR interference (CRISPRi) and CRISPR activation (CRISPRa) modulate gene expression without altering genomic DNA sequence?",
    "options": [
      "They methylate all histones across the entire chromosome",
      "They excise entire promoter regions using dual guide RNAs",
      "They employ catalytically dead Cas9 (dCas9, carrying D10A and H840A mutations) fused to transcriptional repressor domains (e.g. KRAB-MeCP2) or activator domains (e.g. VP64, VPR, or SunTag) targeted to promoters",
      "They reverse-transcribe target mRNAs into non-functional cDNAs"
    ],
    "answer": 2,
    "explain": "dCas9 retains high-affinity, sequence-specific guide-RNA-directed DNA binding but has zero endonuclease activity. Fused to KRAB or KRAB-MeCP2, it recruits chromatin-condensing corepressors (KAP1, NuRD) to silence transcription (CRISPRi). Fused to VPR (VP64-p65-Rta), it recruits basal transcription factors and RNA Polymerase II to boost transcription (CRISPRa).",
    "example": "Targeting dCas9-VPR with three sgRNAs to the quiet Scn1a promoter in human iPSC-derived neurons increases endogenous Nav1.1 mRNA and restores sodium current density.",
    "id": "mol-055",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "DREADD Chemogenetics Second Messenger Coupling",
    "prompt": "In modern behavioral neuroscience, what distinguishes the signaling cascades of the engineered muscarinic chemogenetic actuators hM3Dq and hM4Di?",
    "options": [
      "hM3Dq conducts chloride, while hM4Di conducts sodium",
      "hM3Dq is an ion channel, while hM4Di is an enzyme",
      "hM3Dq is activated by acetylcholine, while hM4Di is activated by dopamine",
      "hM3Dq couples to Gq/11, activating PLC to stimulate calcium release and neuronal excitation, whereas hM4Di couples to Gi/o, inhibiting adenylyl cyclase and opening GIRK channels to hyperpolarize and silence neurons"
    ],
    "answer": 3,
    "explain": "Engineered by Bryan Roth, hM3Dq and hM4Di carry two point mutations (Y149C/Y239G) abolishing acetylcholine sensitivity while conferring sub-nanomolar affinity for synthetic ligands (deschloroclozapine DCZ, CNO). hM3Dq drives Gq-dependent firing, while hM4Di drives Gi-dependent membrane hyperpolarization.",
    "example": "Systemic injection of 10 μg/kg deschloroclozapine (DCZ) in mice expressing hM4Di in lateral hypothalamus orexin neurons rapidly induces somnolence within 10 minutes.",
    "id": "mol-056",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "GCaMP Fluorophore Gating Physics",
    "prompt": "In genetically encoded calcium indicators of the GCaMP family (e.g. GCaMP6s, jGCaMP8f), what molecular mechanism drives the surge in green fluorescence upon calcium binding?",
    "options": [
      "Calcium binding to Calmodulin (CaM) triggers an intramolecular conformational wrap around the M13 peptide, shielding the circularly permuted EGFP (cpEGFP) chromophore from solvent and stabilizing its deprotonated fluorescent phenolate state",
      "Direct proteolytic cleavage of a quenching peptide",
      "Phosphorylation of the GFP fluorophore by protein kinase A",
      "FRET energy transfer between two distinct fluorescent proteins"
    ],
    "answer": 0,
    "explain": "cpEGFP has its N- and C-termini relocated next to the chromophore, creating an open solvent channel that quenches fluorescence in the apo (calcium-free) state. When Ca2+ binds the attached CaM-M13 clamp, it contracts, physically sealing the barrel hole and deprotonating the Tyr66 chromophore, increasing 488 nm fluorescence by >10- to 50-fold.",
    "example": "Two-photon in vivo imaging of GCaMP8f in visual cortex resolves single action potential calcium transients with sub-10 ms rise times.",
    "id": "mol-057",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "ATAC-seq Tn5 Transposase Tagmentation",
    "prompt": "Assay for Transposase-Accessible Chromatin using sequencing (ATAC-seq) maps genome-wide regulatory chromatin accessibility in as few as 500-50,000 neurons because:",
    "options": [
      "It requires radioactive micrococcal nuclease digestion followed by HPLC",
      "A hyperactive mutant Tn5 transposase loaded with sequencing adapters simultaneously cleaves open, nucleosome-depleted DNA and ligates sequencing adapters ('tagmentation') in a single step",
      "It uses whole-genome bisulfite conversion",
      "It sequences only unmethylated mitochondrial DNA"
    ],
    "answer": 1,
    "explain": "Tn5 transposase normally cuts and pastes bacterial transposons. In ATAC-seq, recombinant hyperactive Tn5 pre-loaded with Illumina sequencing adapters cannot access dense heterochromatin or nucleosome-bound DNA, selectively tagmenting accessible enhancers and promoters in open euchromatin.",
    "example": "ATAC-seq peak analysis in sorted striatal D1 vs D2 medium spiny neurons reveals cell-type-specific accessible enhancer landscapes that govern distinct behavioral states.",
    "id": "mol-058",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "TurboID vs BioID Kinetics in Living Brain Tissue",
    "prompt": "Why has engineered TurboID largely superseded classic BioID (BirA* R118G) for proximity labeling of the neuronal proteome in vivo?",
    "options": [
      "TurboID does not require exogenous biotin supplementation",
      "BioID is lethal to all mammalian cells, while TurboID is non-toxic",
      "TurboID achieves catalytic biotinylation of neighboring proteins in 10 minutes (compared to 18-24 hours for BioID), allowing tracking of rapid synaptic and activity-dependent proteomic changes",
      "TurboID labels only RNA molecules, leaving proteins untouched"
    ],
    "answer": 2,
    "explain": "Alice Ting and colleagues engineered TurboID by directed evolution in yeast, selecting for 15 mutations that dramatically increased biotin-AMP turnover. While BioID requires 18-24 hours of labeling (averaging long-term proteomic states), TurboID tags protein interactomes in 10 minutes at physiological temperatures.",
    "example": "Targeting TurboID to the postsynaptic density reveals dynamic recruitment of actin-remodeling scaffolds within 15 minutes of chemically induced LTP.",
    "id": "mol-059",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "APEX2 Subcellular Mapping Chemistry",
    "prompt": "Engineered ascorbate peroxidase (APEX2) maps localized proteomes (such as the synaptic cleft or mitochondrial matrix) with sub-minute resolution because:",
    "options": [
      "It degrades all proteins outside the target compartment",
      "It phosphorylates tyrosine residues using radioactive ATP",
      "It uses ultraviolet light to crosslink nucleic acids",
      "In the presence of biotin-phenol and hydrogen peroxide (H2O2), it generates short-lived biotin-phenoxyl radicals (<1 millisecond half-life) that covalently tag electron-rich amino acids within a tiny (<20 nm) labeling radius"
    ],
    "answer": 3,
    "explain": "Biotin-phenoxyl radicals generated by APEX2 have a half-life of <1 ms, meaning they cannot diffuse across biological membranes or far into the cytosol before being quenched by water. This restricts biotinylation to proteins within a tight 10-20 nm radius of the APEX2 fusion during a 1-minute pulse.",
    "example": "Targeting APEX2 to the synaptic cleft via LRRTM2 fusions mapped the endogenous synaptic cleft proteome in living neurons, identifying novel adhesion complexes.",
    "id": "mol-060",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "RiboTag vs Whole-Tissue RNA-seq in Brain Tissue",
    "prompt": "The RiboTag mouse model (expressing an HA-tagged RPL22 ribosomal subunit under Cre control) provides what decisive advantage over standard whole-tissue RNA-seq when studying rare cell types?",
    "options": [
      "It enables immunoprecipitation of actively translating, cell-type-specific polysomal mRNAs directly from intact homogenized brain tissue without requiring enzymatic tissue dissociation or FACS sorting",
      "It sequences only small non-coding microRNAs",
      "It eliminates all introns from the nuclear genome",
      "It doubles the sequencing read length on Illumina platforms"
    ],
    "answer": 0,
    "explain": "Enzymatic dissociation and FACS of adult brain cells takes hours, during which fragile neurons lyse and immediate-early genes (Fos, Jun, Egr1) are artificially transcribed. RiboTag bypasses dissociation: the whole brain is flash-frozen, lysed, and anti-HA magnetic beads isolate ribosome-bound mRNAs from only the Cre+ cell population in minutes.",
    "example": "Crossing RiboTag with Parvalbumin-Cre allows clean isolation of PV interneuron translatomes, avoiding transcriptional stress artifacts associated with single-cell enzymatic sorting.",
    "id": "mol-061",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "eCLIP Crosslinking-Induced Mutation Signatures",
    "prompt": "Enhanced Crosslinking and Immunoprecipitation (eCLIP) maps direct RNA-protein binding sites at single-nucleotide resolution by identifying:",
    "options": [
      "Double-strand DNA breaks repaired by NHEJ",
      "Reverse transcriptase stops or crosslink-induced mutations (e.g. deletions or misincorporations) that occur at the exact amino acid-RNA crosslink adduct following proteinase K digestion",
      "The position of 5-methylcytosine bases",
      "Regions where RNA polymerase stalls during in vitro transcription"
    ],
    "answer": 1,
    "explain": "UV crosslinking at 254 nm forms an irreversible covalent bond between an RNA base and an RNA-binding protein (such as TDP-43 or FMRP). After proteinase K digestion, a small peptide fragment remains permanently attached to the crosslinked nucleotide, causing reverse transcriptase to prematurely truncate or misread the base during cDNA synthesis, pinpointing the direct binding site.",
    "example": "TDP-43 eCLIP in human neurons reveals thousands of precise UG-repeat binding peaks located predominantly within long introns.",
    "id": "mol-062",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "CUT&Tag vs Standard ChIP-seq Resolution",
    "prompt": "Cleavage Under Targets and Tagmentation (CUT&Tag) represents a major breakthrough over conventional ChIP-seq for profiling histone modifications in the brain because:",
    "options": [
      "It cuts only unmethylated DNA molecules",
      "It requires millions of freshly dissected neurons to detect peaks",
      "A protein A-Tn5 transposase fusion binds the primary antibody in situ and tagments flanking chromatin directly, eliminating sonication, crosslink reversal, and end-repair/ligation library prep steps, enabling single-cell profiling with ultra-low background",
      "It utilizes radioactive isotopes to detect histone tails"
    ],
    "answer": 2,
    "explain": "Henikoff and colleagues developed CUT&Tag: antibodies recruit pA-Tn5 to target chromatin in intact permeabilized nuclei. Adding magnesium triggers tagmentation directly at target sites, avoiding global sonication background and yielding high signal-to-noise libraries from as few as 100 single cells.",
    "example": "Single-nucleus CUT&Tag profiling H3K27me3 in human motor cortex maps heterochromatic silencing across distinct neuronal and glial subtypes at single-cell resolution.",
    "id": "mol-063",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "STED Donut Beam Depletion Physics",
    "prompt": "Stimulated Emission Depletion (STED) super-resolution microscopy breaks the classical diffraction limit of light (~250 nm) by:",
    "options": [
      "Filtering out all photons with wavelengths below 700 nm",
      "Using electron beams instead of light in high vacuum",
      "Physically stretching the glass coverslip during imaging",
      "Superimposing a diffraction-limited excitation spot with a red-shifted, donut-shaped depletion laser beam that de-excites fluorophores at the periphery via stimulated emission, restricting spontaneous fluorescence to a sub-50 nm central focal point"
    ],
    "answer": 3,
    "explain": "Invented by Stefan Hell, STED uses a phase mask to generate a donut-shaped depletion beam with zero intensity at its center. Fluorophores in the donut ring are immediately forced to emit at the depletion wavelength by stimulated emission, silencing their spontaneous fluorescence. Only fluorophores at the exact central zero can emit, shrinking the effective point spread function to ~20-30 nm.",
    "example": "STED imaging of dendritic spines reveals the periodic ~190 nm actin-spectrin ring lattice along the axon initial segment.",
    "id": "mol-064",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Expansion Microscopy (ExM) Isotropic Swelling",
    "prompt": "Expansion Microscopy (ExM, Boyden et al., Science 2015) achieves nanoscale super-resolution on conventional diffraction-limited optical microscopes by:",
    "options": [
      "Covalently anchoring biomolecules to an expandable polyacrylate hydrogel mesh inside the tissue, enzymatically homogenizing proteins with proteinase K, and dialyzing in water to physically swell the sample isotropically by 4.5- to 10-fold",
      "Using deep ultraviolet lasers to excite fluorophores",
      "Compressing tissue into a thin monolayer under hydraulic pressure",
      "Cooling the microscope stage to liquid nitrogen temperatures"
    ],
    "answer": 0,
    "explain": "Rather than modifying the optics, ExM modifies the specimen. Synthesizing a swellable polyelectrolyte hydrogel (sodium acrylate/acrylamide) throughout the brain slice links fluorophores or antibodies to the polymer. Digestion with proteinase K relieves mechanical stress, and dialysis in pure water drives electrostatic repulsion, swelling the hydrogel 4.5x uniformly in 3D (a ~100-fold volume increase).",
    "example": "Imaging an ExM-treated brain slice with a standard 40x confocal objective resolves presynaptic Bassoon and postsynaptic Homer-1 separated across the ~20 nm synaptic cleft.",
    "id": "mol-065",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Patch-Seq Multimodal Triple Characterization",
    "prompt": "The Patch-seq methodology pioneered by the Allen Institute represents the zenith of single-neuron taxonomy because it gathers from the exact same individual neuron:",
    "options": [
      "Action potentials, blood pressure, and pupil diameter",
      "Triple modalities: (1) Whole-cell patch-clamp electrophysiology; (2) High-resolution morphological reconstruction via intracellular biocytin filling; and (3) Single-cell RNA-sequencing via cytoplasmic/nuclear RNA aspiration through the patch pipette",
      "Nuclear DNA sequence and mitochondrial respiration only",
      "Fluorescence in situ hybridization and whole-brain fMRI"
    ],
    "answer": 1,
    "explain": "Patch-seq harmonizes morphological, physiological, and transcriptomic classification schemes. Following whole-cell recording of firing dynamics, biocytin fills the dendritic arbor, and the cell contents are aspirated into the pipette tip for Smart-seq library preparation, mapping physiological properties directly onto transcriptomic cell types.",
    "example": "Patch-seq classification of thousands of mouse and human neocortical interneurons established that transcriptomically defined 't-types' exhibit distinctive intrinsic firing properties and dendritic geometries.",
    "id": "mol-066",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Genetically Encoded Voltage Indicators (GEVIs) Kinetics",
    "prompt": "State-of-the-art Genetically Encoded Voltage Indicators (such as ASAP3 or Voltron) offer what critical advantage over Genetically Encoded Calcium Indicators (GCaMP6/8) in optical circuit physiology?",
    "options": [
      "They remain active for months without bleaching",
      "They require zero photon excitation",
      "They report transmembrane voltage directly with sub-millisecond temporal kinetics, accurately capturing single action potential waveforms, afterhyperpolarizations, and subthreshold excitatory/inhibitory postsynaptic potentials that calcium buffers cannot detect",
      "They are expressed exclusively in myelin sheaths"
    ],
    "answer": 2,
    "explain": "Intracellular Ca2+ is an indirect, heavily buffered, and slow (decaying over tens to hundreds of milliseconds) surrogate of neural activity that completely misses hyperpolarizing IPSPs and subthreshold EPSPs. GEVIs track the movement of charged voltage-sensor domains within the lipid bilayer, reporting millisecond-fast voltage swings in real time.",
    "example": "Kilohertz-rate two-photon imaging of ASAP3 in cerebellar Purkinje neurons resolves the complex spike waveform, including individual fast spikelets riding on the calcium plateau.",
    "id": "mol-067",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "dLight1 and GRAB_DA Sensor Engineering",
    "prompt": "Genetically encoded neurotransmitter sensors such as dLight1 and GRAB_DA report real-time sub-second dopamine dynamics in behaving animals by using:",
    "options": [
      "A synthetic chemical dye injected into the ventricles",
      "An engineered bacterial tyrosine hydroxylase that emits light",
      "A dopamine-degrading enzyme coupled to horse-radish peroxidase",
      "A human dopamine receptor (D1R or D2R) backbone engineered with circularly permuted green fluorescent protein (cpGFP) inserted into its third intracellular loop; ligand binding induces a conformational shift that alters cpGFP fluorescence intensity"
    ],
    "answer": 3,
    "explain": "Developed by Lin Tian (dLight1) and Yulong Li (GRAB_DA), these sensors harness the high physiological nanomolar affinity and pharmacological selectivity of native dopamine GPCRs. Ligand binding switches receptor conformation, reorganizing the loop-inserted cpGFP and producing rapid, reversible fluorescence changes.",
    "example": "Fiber photometry recording of dLight1 in the nucleus accumbens detects sub-second dopamine release transients triggered by unexpected food reward delivery.",
    "id": "mol-068",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Tissue Clearing Refractive Index Matching Physics",
    "prompt": "Advanced whole-brain tissue clearing techniques (such as CLARITY, iDISCO, and CUBIC) render mammalian brains optically transparent by:",
    "options": [
      "Removing light-scattering lipid bilayers and equilibrating the remaining protein/hydrogel matrix in a high-refractive-index matching solution (RI ~1.45 to 1.56), eliminating internal light scattering at phase boundaries",
      "Dissolving all brain proteins while leaving only DNA intact",
      "Bleaching all pigments with boiling nitric acid",
      "Freezing the brain in optical-grade acrylic plastic"
    ],
    "answer": 0,
    "explain": "Brain tissue opacity is not caused by photon absorption, but by severe light scattering at the interface between low-refractive-index water (RI = 1.33) and high-refractive-index lipids/proteins (RI = 1.45-1.50). Clearing methods strip scatter-inducing lipids and infuse homogeneous clearing reagents that match the refractive index of the scaffold, allowing light to travel straight through centimeters of intact brain.",
    "example": "Light-sheet fluorescence microscopy of an intact cleared mouse hemisphere immunostained via iDISCO resolves long-range axon collateral projections from motor cortex to spinal cord.",
    "id": "mol-069",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM Helical Reconstruction of Amyloid Polymorphs",
    "prompt": "Sjors Scheres and Michel Goedert's pioneering single-particle Cryo-EM studies of tau filaments extracted from postmortem human brains established that:",
    "options": [
      "All tau fibrils possess identical crystal structures regardless of disease",
      "Tau filaments adopt distinct disease-specific protofilament folds in Alzheimer's disease (paired helical filaments of mixed 3R/4R), Pick's disease (narrow 3R folds), and Corticobasal Degeneration (four-layered 4R folds), proving that distinct tauopathies represent distinct structural conformers",
      "Tau fibrils are hollow tubes composed exclusively of tubulin dimers",
      "Tau fibrils contain no beta-sheet secondary structure"
    ],
    "answer": 1,
    "explain": "High-resolution (~3 Å) helical Cryo-EM reconstruction revealed that the tau cross-beta core adopts invariant, highly specific folds unique to each clinical diagnostic entity. For example, Alzheimer's filaments consist of two C-shaped protofilaments spanning residues 306-378, whereas CBD fibrils fold as a four-layered structure enclosing a non-proteinaceous cofactor.",
    "example": "Cryo-EM structures of brain-extracted filaments allow molecular design of PET tracers that selectively bind Alzheimer's tau folds over PSP or Pick folds.",
    "id": "mol-070",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Southern Blotting Nucleic Acid Target",
    "prompt": "Invented by Edwin Southern, the Southern blot technique is specifically designed to detect:",
    "options": [
      "Proteins using monoclonal antibodies",
      "Total cellular RNA using poly-T columns",
      "Specific DNA fragments by capillary transfer from an agarose gel to a membrane followed by hybridization with labeled DNA/RNA probes",
      "Lipids using thin-layer chromatography"
    ],
    "answer": 2,
    "explain": "Southern blotting fragments genomic DNA with restriction enzymes, separates them by agarose gel electrophoresis, depurinates/denatures them into single strands, transfers them to a nitrocellulose or nylon membrane, and hybridizes with radioactive or fluorescent labeled probes.",
    "example": "Southern blotting was the historical gold standard for measuring CAG repeat expansion sizes in Huntington's disease families.",
    "id": "mol-071",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Northern Blotting RNA Analysis",
    "prompt": "Unlike Southern blotting, Northern blotting analyzes RNA transcripts and requires running the agarose gel under denaturing conditions (e.g. with formaldehyde) to:",
    "options": [
      "Digest all ribosomal RNA",
      "Prevent bacteria from synthesizing DNA on the membrane",
      "Cleave the RNA into 20-nucleotide fragments",
      "Disrupt secondary RNA hairpin and stem-loop structures, ensuring migration depends strictly on linear nucleotide chain length"
    ],
    "answer": 3,
    "explain": "Single-stranded RNA molecules readily fold into extensive intra-molecular secondary structures (hairpins, stem-loops) that alter electrophoretic mobility. Formaldehyde or glyoxal denatures these secondary structures, ensuring linear size separation.",
    "example": "Northern blotting with a myelin basic protein (MBP) probe demonstrates developmental induction of MBP mRNA isoforms in developing mouse oligodendrocytes.",
    "id": "mol-072",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "DNA Melting Temperature (Tm) Determinants",
    "prompt": "In molecular cloning and PCR, the melting temperature (Tm) of a double-stranded DNA duplex increases with:",
    "options": [
      "Higher GC content (due to three hydrogen bonds per G-C pair versus two in A-T pairs) and higher monovalent cation (salt) concentration",
      "Higher AT content and lower salt concentration",
      "Shorter oligonucleotide length",
      "Addition of formamide or urea"
    ],
    "answer": 0,
    "explain": "G-C base pairs form three hydrogen bonds and favorable base-stacking interactions, requiring more thermal energy to separate than A-T pairs (two hydrogen bonds). Cations (Na+, K+) shield the negatively charged phosphate backbones, reducing electrostatic repulsion and stabilizing the duplex.",
    "example": "A 20-mer PCR primer with 60% GC content has a substantially higher Tm (~62°C) than a 20-mer with 30% GC content (~50°C).",
    "id": "mol-073",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "PCR Primer Design 3' GC Clamp",
    "prompt": "In designing PCR primers for neurogenetics, why is the inclusion of a 'GC clamp' (1 or 2 G or C bases at the extreme 3' terminus) highly recommended?",
    "options": [
      "It prevents DNA polymerase from cleaving the primer",
      "It promotes stable, high-affinity base-pairing at the 3' end where DNA polymerase initiates chain extension, minimizing non-specific annealing",
      "It acts as a fluorescent signal during real-time qPCR",
      "It causes the primer to form a circular loop"
    ],
    "answer": 1,
    "explain": "The 3' end of the primer is the initiation site for Taq polymerase. The stronger hydrogen bonding of 1-2 G or C residues at the 3' end ('GC clamp') prevents 'breathing' (transient unpairing) and enhances polymerization efficiency.",
    "example": "Standard primer design guidelines specify avoiding >3 consecutive G/C bases at the 3' end while ensuring at least 1 G or C to anchor the primer.",
    "id": "mol-074",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Proofreading Polymerase 3'-to-5' Exonuclease",
    "prompt": "High-fidelity PCR polymerases (such as Phusion or Q5) exhibit error rates >50-fold lower than wild-type Taq polymerase primarily because they possess:",
    "options": [
      "Reverse transcriptase activity",
      "5' to 3' exonuclease activity that destroys the template strand",
      "Intrinsic 3' to 5' exonuclease proofreading activity that excises misincorporated non-complementary nucleotides before continuing synthesis",
      "RNA-guided endonuclease domains"
    ],
    "answer": 2,
    "explain": "When high-fidelity polymerases incorporate an incorrect mismatched base, the stalled 3' terminus is shifted into the enzyme's 3'-to-5' exonuclease catalytic pocket, which hydrolyzes the mismatch and returns the strand to the polymerase active site.",
    "example": "Amplifying an ion channel cDNA for heterologous expression in Xenopus oocytes requires a proofreading polymerase to avoid introducing spurious functional mutations.",
    "id": "mol-075",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "TA Cloning Vector Chemistry",
    "prompt": "Standard Taq DNA polymerase naturally adds a single non-templated nucleotide to the 3' ends of PCR products, enabling TA cloning into specialized vectors featuring:",
    "options": [
      "Covalently attached topoisomerases",
      "Single-stranded 5' guanosine extensions",
      "Blunt ends treated with alkaline phosphatase",
      "A non-templated 3' adenosine (A) overhang on the PCR product that anneals to single 3' thymidine (T) overhangs on the linearized plasmid vector"
    ],
    "answer": 3,
    "explain": "Taq polymerase possesses terminal transferase activity that adds a non-templated adenine (A) to the 3' ends of amplicons. Linearized TA cloning vectors (e.g. pGEM-T) are manufactured with matching 3' thymidine (T) overhangs, facilitating fast sticky-end ligation without restriction digest.",
    "example": "TA cloning is routinely used to rapidly clone PCR amplicons of uncharacterized splice variants for Sanger sequencing confirmation.",
    "id": "mol-076",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Alkaline Phosphatase Dephosphorylation in Cloning",
    "prompt": "In restriction-enzyme-based molecular cloning, treating the linearized plasmid vector with Calf Intestinal Alkaline Phosphatase (CIP) prevents:",
    "options": [
      "Vector recircularization / self-ligation in the absence of an insert, by removing the essential 5'-phosphate groups from the vector ends",
      "Bacterial transformation by foreign plasmids",
      "Digestion of the insert DNA by exonucleases",
      "Transcription of the antibiotic resistance gene"
    ],
    "answer": 0,
    "explain": "T4 DNA ligase requires a 5'-monophosphate on one strand and a 3'-hydroxyl on the other to form a phosphodiester bond. Dephosphorylating the vector removes 5'-phosphates, making self-ligation chemically impossible while allowing ligation to a phosphorylated insert.",
    "example": "CIP-treating an EcoRI-linearized vector drops empty background colonies by >95% following transformation.",
    "id": "mol-077",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Enhanced Chemiluminescence (ECL) in Western Blotting",
    "prompt": "In Western blot detection, Enhanced Chemiluminescence (ECL) generates visible light at 425 nm through which enzyme-substrate reaction?",
    "options": [
      "Alkaline phosphatase cleaves bromochloroindolyl phosphate to form a blue precipitate",
      "Horseradish peroxidase (HRP) oxidizes cyclic diacylhydrazide (luminol) in the presence of hydrogen peroxide (H2O2) and chemical enhancers, emitting photons as luminol relaxes to the ground state",
      "Beta-galactosidase hydrolyzes X-gal in the presence of IPTG",
      "Luciferase consumes GTP to phosphorylate antibodies"
    ],
    "answer": 1,
    "explain": "Secondary antibodies conjugated to HRP catalyze the oxidation of luminol by H2O2 into 3-aminophthalate in an excited state. Phenolic enhancers (e.g. p-iodophenol) prolong and amplify photon emission at 425 nm, which is captured by autoradiography film or digital CCD/CMOS imagers.",
    "example": "Digital imaging of an ECL-developed membrane detects sub-picogram amounts of synaptic proteins in brain homogenates.",
    "id": "mol-078",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Brain Subcellular Differential Centrifugation",
    "prompt": "In standard biochemical fractionation of mammalian brain tissue, low-speed centrifugation at 1,000 x g for 10 minutes pellets which cellular component?",
    "options": [
      "Pure soluble cytosolic proteins (S3)",
      "Purified synaptic vesicles (P3)",
      "The nuclear fraction (P1) and unbroken whole cells, leaving the crude cytoplasmic/synaptosomal supernatant (S1)",
      "Isolated postsynaptic densities"
    ],
    "answer": 2,
    "explain": "Low centrifugal force (1,000 x g) sediments large, dense structures (intact nuclei, cell bodies, large debris) into pellet P1. Centrifuging supernatant S1 at 10,000-15,000 x g subsequently pellets mitochondria and synaptosomes (P2).",
    "example": "Isolating histone proteins or nuclear transcription factors (e.g. MeCP2) starts by harvesting the 1,000 x g P1 pellet from homogenized cerebral cortex.",
    "id": "mol-079",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Synaptosome Isolation Density Gradients",
    "prompt": "Functional, metabolically active synaptosomes (pinched-off presynaptic nerve terminals with attached postsynaptic densities) are isolated from crude brain homogenates (P2) using:",
    "options": [
      "Capillary zone electrophoresis at pH 2.0",
      "Boiling in 10% sodium hydroxide",
      "Affinity chromatography over nickel-NTA columns",
      "Discontinuous Percoll or Ficoll/sucrose density gradient ultracentrifugation, isolating synaptosomes at the interface between gradient layers"
    ],
    "answer": 3,
    "explain": "During mild homogenization in isotonic sucrose (0.32 M), nerve terminals shear off and their membranes instantly reseal into intact vesicles ('synaptosomes'). Layering over discontinuous Ficoll or Percoll gradients separates synaptosomes from free mitochondria and myelin fragments based on buoyant density.",
    "example": "Isolated synaptosomes retain functional membrane potentials, consume oxygen, and release glutamate in a calcium-dependent manner upon potassium depolarization.",
    "id": "mol-080",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Postsynaptic Density (PSD) Triton Insoluble Fraction",
    "prompt": "The postsynaptic density (PSD) of glutamatergic synapses is biochemically defined by its unique property of being:",
    "options": [
      "Insoluble in non-ionic detergents (e.g. 1% Triton X-100), forming an electron-dense proteinaceous disc that pellets upon high-speed centrifugation (PSD-I fraction)",
      "Instantly soluble in pure water",
      "Extracted only by chloroform and methanol",
      "Composed exclusively of non-coding RNA"
    ],
    "answer": 0,
    "explain": "The PSD is a massive multi-protein megacomplex crosslinked by PSD-95, Shank, GKAP, and actin. Non-ionic detergents solubilize lipid membranes and presynaptic vesicles but leave the dense postsynaptic scaffold intact as a detergent-insoluble pellet.",
    "example": "Biochemical Western blotting of the Triton X-100-insoluble PSD fraction shows intense enrichment of GluA1, GluN1, and CaMKII, with complete depletion of presynaptic synaptophysin.",
    "id": "mol-081",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cell-Surface Biotinylation of Neurotransmitter Receptors",
    "prompt": "To quantify the fraction of AMPA or NMDA receptors expressed on the plasma membrane versus intracellular endosomal pools, researchers perform surface biotinylation using:",
    "options": [
      "Lipophilic biotin that freely diffuses across all cellular membranes",
      "Sulfo-NHS-SS-biotin, a membrane-impermeant, water-soluble biotin ester that covalently labels extracellular lysine residues at 4°C, followed by NeutrAvidin pull-down",
      "Radioactive phosphorus (32P) labeling of ATP",
      "Triton X-100 permeabilization followed by antibody staining"
    ],
    "answer": 1,
    "explain": "Sulfo-NHS-SS-biotin contains a charged sulfonate group that prevents membrane crossing. Incubating intact neurons at 4°C (which blocks endocytosis) tags only surface-exposed extracellular domains. Lysis and pull-down with immobilized streptavidin separates surface from intracellular receptor fractions.",
    "example": "Surface biotinylation assays demonstrate a ~50% decrease in surface GluA1 levels following chemically induced NMDA-receptor-dependent LTD.",
    "id": "mol-082",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "FRET Distance-Dependence Physics",
    "prompt": "Förster Resonance Energy Transfer (FRET) measures nanoscale protein-protein interactions and conformational changes because the energy transfer efficiency scales inversely with:",
    "options": [
      "The square of the molecular weight of the complex",
      "The linear distance between fluorophores (1 / r)",
      "The sixth power of the inter-fluorophore distance (1 / r^6), operating over distances of 1 to 10 nanometers",
      "The pH of the extracellular solution"
    ],
    "answer": 2,
    "explain": "FRET is non-radiative dipole-dipole energy transfer from an excited donor to an acceptor fluorophore. The transfer efficiency E = R0^6 / (R0^6 + r^6), where R0 is the Förster radius (~5 nm). Because of the 1/r^6 dependence, FRET is exquisitely sensitive to sub-nanometer spatial rearrangements.",
    "example": "A FRET biosensor consisting of CFP and YFP flanking the CaMKII regulatory domain detects kinase activation as an immediate loss of FRET when the autoinhibitory domain unclamps.",
    "id": "mol-083",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "FRAP Mobile Fraction Measurement",
    "prompt": "Fluorescence Recovery After Photobleaching (FRAP) is used in living dendritic spines to calculate:",
    "options": [
      "The number of lipid bilayers surrounding an organelle",
      "The exact rate of protein synthesis in the cell nucleus",
      "The action potential firing threshold",
      "The mobile fraction and lateral diffusion coefficient (D) of tagged receptors moving between the synaptic density and extra-synaptic membranes"
    ],
    "answer": 3,
    "explain": "A high-intensity laser pulse irreversibly bleaches fluorescently tagged receptors (e.g. SEP-GluA1) in a single dendritic spine. Monitoring fluorescence recovery over time as unbleached receptors diffuse into the spine determines both the rate of diffusion and the proportion of mobile vs immobilized scaffold-anchored receptors.",
    "example": "FRAP curves demonstrate that TARP phosphorylation by CaMKII immobilizes AMPA receptors in the postsynaptic density, reducing their mobile fraction from 60% to 20%.",
    "id": "mol-084",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Fluorescence Lifetime Imaging Microscopy (FLIM)",
    "prompt": "Two-photon Fluorescence Lifetime Imaging Microscopy (2pFLIM) detects FRET between synaptic signaling proteins with superior quantitative accuracy over intensity-based ratiometric FRET because fluorescence lifetime:",
    "options": [
      "Is an intrinsic physical property of the donor fluorophore that is independent of donor/acceptor expression levels, fluorophore concentration, and optical path length",
      "Requires radioactive labeling of proteins",
      "Can only be performed on fixed, dehydrated tissue sections",
      "Does not require pulsed lasers"
    ],
    "answer": 0,
    "explain": "Fluorescence lifetime is the average time a fluorophore spends in the excited state before emitting a photon (typically ~2-4 ns for GFP). When FRET occurs, energy transfer introduces an additional de-excitation pathway, shortening the donor lifetime. Because lifetime is independent of fluorophore concentration, 2pFLIM eliminates artifacts caused by unequal expression in living neurons.",
    "example": "Yasuda and colleagues used 2pFLIM to monitor real-time monomeric Ras and RhoA activation within single dendritic spines during LTP induction.",
    "id": "mol-085",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Third-Generation Lentiviral Safety Features",
    "prompt": "Third-generation lentiviral packaging systems incorporate which critical biosafety feature to prevent the generation of replication-competent lentivirus?",
    "options": [
      "Complete removal of the envelope glycoprotein gene",
      "A Self-Inactivating (SIN) deletion in the 3' LTR (delta-U3), splitting the viral genome across four separate plasmids, and driving transcription from a Tat-independent chimeric 5' LTR",
      "Replacement of reverse transcriptase with Taq polymerase",
      "Inactivation of the packaging signal psi"
    ],
    "answer": 1,
    "explain": "The delta-U3 deletion in the 3' LTR is copied to the 5' LTR during reverse transcription in the target cell, abolishing viral promoter activity and preventing viral genome packaging in transduced neurons. Splitting Rev, Gag-Pol, Env, and the vector onto 4 separate plasmids makes recombining into a replication-competent virus virtually impossible.",
    "example": "Third-generation SIN lentiviral vectors pseudotyped with VSV-G stably integrate up to 8-10 kb expression cassettes into human neural stem cell chromosomes with minimal biosafety risk.",
    "id": "mol-086",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Lentivirus vs Retrovirus Cell-Cycle Tropism",
    "prompt": "Why can HIV-1-derived lentiviral vectors efficiently transduce post-mitotic differentiated adult neurons, whereas oncoretroviral vectors (such as MMLV) cannot?",
    "options": [
      "Lentiviruses do not integrate into DNA",
      "MMLV vectors only bind to mitotic spindle poles",
      "The lentiviral pre-integration complex (containing viral matrix, integrase, and Vpr) actively translocates through intact nuclear pores, whereas MMLV requires nuclear envelope breakdown during mitosis",
      "Adult neurons lack receptors for retroviral envelopes"
    ],
    "answer": 2,
    "explain": "Oncoretroviruses (MMLV) lack nuclear import machinery and cannot cross the intact nuclear lamina; they can only access host chromosomes when the nuclear envelope disassembles during cell division. Lentiviruses possess nuclear localization signals that engage importins, enabling efficient passage through intact nuclear pore complexes of quiescent, non-dividing neurons.",
    "example": "Stereotaxic injection of lentivirus into the adult rodent hippocampus yields robust lifelong transduction of mature, post-mitotic CA1 pyramidal neurons.",
    "id": "mol-087",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Tet-Off vs Tet-On Molecular Logic",
    "prompt": "In tetracycline-regulated gene expression in the brain, what is the operational difference between the Tet-Off and Tet-On systems?",
    "options": [
      "Tet-Off is irreversible, while Tet-On is permanent",
      "Tet-Off requires red light, while Tet-On requires blue light",
      "Tet-Off acts on RNA, while Tet-On acts on protein translation",
      "In Tet-Off, the tTA transactivator binds the TRE promoter in the absence of doxycycline to activate transcription, and dox shuts it off; in Tet-On, the mutated rtTA transactivator binds TRE only in the presence of doxycycline, turning transcription on"
    ],
    "answer": 3,
    "explain": "Tet-Off uses wild-type tetracycline transactivator (tTA). Administering doxycycline changes tTA conformation so it detaches from the tet operator (TRE), arresting transcription. Tet-On uses reverse tTA (rtTA), which requires doxycycline to bind TRE, enabling induction on demand.",
    "example": "Mayford and Kandel used Tet-Off transgenic mice to reversibly express mutant CaMKII in forebrain neurons, demonstrating that shutting off mutant CaMKII with doxycycline restored LTP and spatial memory.",
    "id": "mol-088",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Intersectional Genetic Targeting (INTRSECT)",
    "prompt": "The INTRSECT (intronic recombinase sites enabling combinatorial targeting) system allows transgene expression to be restricted strictly to cells expressing BOTH Cre AND Flp recombinases by using:",
    "options": [
      "A modular single-vector expression cassette where inverted coding exons are separated by alternating intronic loxP and FRT recognition sites arranged in a Boolean AND-gate logic",
      "Two separate viral vectors injected into different hemispheres",
      "A fusion protein of Cre and Flp recombinases",
      "A temperature-sensitive promoter requiring 42°C heat shock"
    ],
    "answer": 0,
    "explain": "Developed by Karl Deisseroth's group, INTRSECT places split or inverted exons of an opsin/indicator interrupted by orthogonal intronic recombination sites. Only cells expressing both Cre (excision/inversion 1) and Flp (excision/inversion 2) successfully assemble the complete uninterrupted coding transcript, implementing Boolean logic (A AND B, A AND NOT B).",
    "example": "Using an INTRSECT AAV in Vgat-Cre / CCK-Flp double transgenic mice selectively restricts optogenetic expression to the rare population of CCK-positive GABAergic interneurons.",
    "id": "mol-089",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Cre-ERT2 Tamoxifen Induction Mechanism",
    "prompt": "The inducible Cre-ERT2 recombinase system achieves temporal control over genomic excision in transgenic mice because in the absence of 4-hydroxytamoxifen (4-OHT):",
    "options": [
      "The protein is completely degraded by the proteasome every 5 minutes",
      "The fusion protein is sequestered in the cytoplasm by binding to Heat Shock Protein 90 (HSP90); 4-OHT displaces HSP90, allowing Cre-ERT2 to translocate into the nucleus",
      "The gene is not transcribed until tamoxifen binds to the promoter",
      "The recombinase acts as an RNA-dependent RNA polymerase"
    ],
    "answer": 1,
    "explain": "Cre is fused to a mutated ligand-binding domain of the human estrogen receptor (ERT2) that does not bind endogenous 17beta-estradiol, but binds synthetic 4-OHT with high affinity. Cytoplasmic HSP90 holds Cre-ERT2 inactive until 4-OHT administration triggers nuclear import for genomic loxP recombination.",
    "example": "Administering tamoxifen to adult Nestin-CreERT2 mice induces gene deletion specifically in adult hippocampal neural stem cells at a defined chronological time point.",
    "id": "mol-090",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Chrimson Red-Shifted Optogenetics",
    "prompt": "The red-shifted channelrhodopsin Chrimson (derived from Chlamydomonas noctigama) operates with an excitation maximum at 590 nm, enabling neuroscientists to:",
    "options": [
      "Stimulate neurons without needing retinal chromophores",
      "Inhibit neurons by pumping chloride into the cytoplasm",
      "Simultaneously perform optical excitation with red light (590-630 nm) while recording green calcium fluorescence (GCaMP, 488 nm) without optical cross-talk",
      "Cross the intact mouse skull using magnetic fields"
    ],
    "answer": 2,
    "explain": "Wild-type ChR2 is activated by blue light (~470 nm), which overlaps with the 488 nm excitation of GCaMP and causes massive artifactual optogenetic activation during imaging. Chrimson's ~100 nm red-shift separates excitation spectra, enabling all-optical circuit stimulation and imaging in the same cells.",
    "example": "Co-expressing Chrimson in presynaptic thalamic axons and GCaMP6s in postsynaptic cortical dendrites allows optogenetic synaptic stimulation while imaging postsynaptic calcium transients.",
    "id": "mol-091",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Chronos Ultrafast Kinetic Optogenetics",
    "prompt": "Compared to classic Channelrhodopsin-2, the opsin Chronos (isolated by Ed Boyden from Stigeoclonium helveticum) is distinguished by its:",
    "options": [
      "Inability to conduct sodium",
      "Selective permeability to potassium ions",
      "Slow open state that remains open for 30 minutes",
      "Ultra-fast channel deactivation kinetics (~3.6 ms tau) and exceptional light sensitivity, driving action potential trains up to 100 Hz with sub-millisecond spike precision"
    ],
    "answer": 3,
    "explain": "Chronos deactivates over five times faster than ChR2 (tau ~3.6 ms vs ~15-20 ms for ChR2). This rapid shut-off prevents charge accumulation and depolarization block during high-frequency stimulation, allowing high-fidelity spike entrainment up to 100 Hz in auditory and parvalbumin-positive interneurons.",
    "example": "Photostimulation of Chronos-expressing auditory brainstem neurons drives spike firing at 100 Hz without missed spikes or plateau potentials.",
    "id": "mol-092",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Step-Function Opsins (SSFOs) Bistable Mechanics",
    "prompt": "Stabilized Step-Function Opsins (SSFOs, e.g. ChR2-C128S/D156A) facilitate long-duration behavioral manipulations because:",
    "options": [
      "A single 2-second pulse of blue light locks the channel into a conducting open state with a ~30-minute deactivation half-life, which can be instantly terminated on demand with yellow light (590 nm)",
      "They require continuous high-power laser illumination throughout the behavior",
      "They permanently destroy the target neurons",
      "They conduct only divalent calcium ions"
    ],
    "answer": 0,
    "explain": "Mutations at C128 and D156 destabilize the retinal Schiff base ground state, extending the open conducting state from milliseconds to ~29 minutes. A brief blue flash lowers rheobase and increases network excitability across a 30-minute social behavioral assay without needing tethered fiber optic cables or tissue heating.",
    "example": "Delivering a 2-second blue light pulse to mice expressing SSFO in prefrontal interneurons elevates E/I balance for 20 minutes, impairing social interaction until terminated with yellow light.",
    "id": "mol-093",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "GtACR1 Light-Gated Chloride Channel Conductance",
    "prompt": "Guillardia theta Anion Channelrhodopsins (GtACR1 and GtACR2) represent ultra-potent optogenetic silencing tools because they function as:",
    "options": [
      "ATP-consuming proton pumps",
      "Direct light-gated anion channels with massive chloride conductance, requiring orders of magnitude less light intensity than chloride pumps (NpHR) to induce shunting inhibition",
      "Enzymatic RNA degraders",
      "Calcium-activated potassium channels"
    ],
    "answer": 1,
    "explain": "Unlike Halorhodopsin (NpHR) which pumps only one chloride ion per absorbed photon, GtACR channels open a large pore that conducts thousands of Cl- ions per single photon. This creates a massive membrane conductance surge that clamps the membrane potential to E_Cl, shunting action potentials with minimal light power.",
    "example": "Low-power blue light illumination (<0.1 mW/mm2) of GtACR1-expressing cortical pyramidal neurons completely silences sensory-evoked spiking.",
    "id": "mol-094",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "iGluSnFR3 Glutamate Optical Biosensor",
    "prompt": "The genetically encoded biosensor iGluSnFR3 reports synaptic glutamate release in vivo with high spatial resolution by coupling:",
    "options": [
      "Horseradish peroxidase to glutamate dehydrogenase",
      "A luciferase to an AMPA receptor channel pore",
      "Bacterial periplasmic glutamate-binding protein GltI to circularly permuted EGFP; glutamate binding triggers hinge closure that increases green fluorescence emission",
      "A synthetic chemical calcium dye to an axon terminal"
    ],
    "answer": 2,
    "explain": "iGluSnFR is an engineered chimera consisting of the E. coli periplasmic glutamate-binding protein GltI inserted into cpEGFP. Glutamate binding triggers a dramatic Venus-flytrap-like hinge motion that alters the electrostatic environment around the fluorophore, generating bright, millisecond-fast green flashes at active synapses.",
    "example": "Two-photon imaging of iGluSnFR3 in mouse cortex reveals single-synapse glutamate release events with sub-millisecond on-kinetics and single-dendritic-spine spatial localization.",
    "id": "mol-095",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Drop-seq Unique Molecular Identifier (UMI) Principle",
    "prompt": "In droplet-based single-cell and single-nucleus RNA sequencing (e.g. Drop-seq, 10x Genomics), Unique Molecular Identifiers (UMIs) are essential because they:",
    "options": [
      "Sequence the genomic promoter of every gene",
      "Identify which animal the tissue originated from",
      "Determine the speed of reverse transcriptase",
      "Allow computational deduplication of PCR duplicates, enabling absolute digital counting of original mRNA molecules captured per gene per cell"
    ],
    "answer": 3,
    "explain": "Each individual capture oligonucleotide on a gel bead carries a 10-12 nt random UMI alongside the cell barcode. When reverse transcription occurs, every captured mRNA molecule receives a unique UMI. After 14 cycles of PCR amplification, identical reads sharing the same UMI are collapsed into a single digital count, removing amplification bias.",
    "example": "If a single-nucleus library yields 100 sequencing reads for Camk2a all sharing the exact same 10-nt UMI sequence, the digital gene expression matrix counts this as exactly 1 transcript.",
    "id": "mol-096",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Smart-seq2 Full-Length Transcript Coverage",
    "prompt": "Unlike droplet-based single-cell RNA-seq platforms that capture only 3' or 5' ends, Smart-seq2 recovers full-length transcript coverage across entire gene bodies by utilizing:",
    "options": [
      "Moloney Murine Leukemia Virus (MMLV) reverse transcriptase's terminal transferase activity to add non-templated cytosines, enabling template switching with an oligo (TSO) for full-length cDNA PCR",
      "Random fragmentation of whole genomic chromosomes",
      "High-speed exon-specific microarrays",
      "Enzymatic ligation of RNA adapters to 5' caps"
    ],
    "answer": 0,
    "explain": "Upon reaching the 5' end of an mRNA, MMLV reverse transcriptase adds 2-5 non-templated cytosines (dCs). A Template-Switching Oligo (TSO) pairing with these dCs templates reverse transcription of a 5' PCR anchor, yielding full-length double-stranded cDNA suitable for analyzing alternative splicing and point mutations.",
    "example": "Smart-seq2 sequencing of single cortical pyramidal neurons detects full-length alternative splicing of Neurexin-1, identifying specific exon 20 inclusion isoforms.",
    "id": "mol-097",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Agarose Gel Concentration for DNA Sizing",
    "prompt": "When separating PCR products by agarose gel electrophoresis, resolving small DNA fragments (100-300 bp) with high resolution requires:",
    "options": [
      "A lower agarose concentration (e.g. 0.5%)",
      "A higher agarose concentration (e.g. 2.0% to 2.5%), creating smaller pore sizes in the polymer matrix",
      "Omitting the running buffer",
      "Running the gel at 400 volts"
    ],
    "answer": 1,
    "explain": "Higher agarose concentrations produce a denser polymer network with smaller sieve pores, slowing smaller fragments and resolving bands with minimal molecular weight differences (e.g. 100 bp vs 150 bp). Low concentrations (0.7-0.8%) are optimal for resolving large 5-10 kb plasmids.",
    "example": "Resolving a 25 bp insertion polymorphism in the serotonin transporter promoter (5-HTTLPR) requires a 2.5% high-resolution agarose gel.",
    "id": "mol-098",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Spectrophotometric DNA A260/A280 Purity Ratio",
    "prompt": "In NanoDrop spectrophotometric analysis of purified brain genomic DNA, an A260/A280 absorbance ratio of approximately 1.8 indicates:",
    "options": [
      "Extensive contamination with aromatic amino acids and phenol (ratio < 1.6)",
      "Severe RNA contamination (ratio > 2.2)",
      "Pure double-stranded DNA free from substantial protein contamination",
      "Complete degradation of all nucleic acids"
    ],
    "answer": 2,
    "explain": "Nucleic acids absorb maximally at 260 nm (due to ring resonance of purines and pyrimidines). Aromatic amino acids (tryptophan, tyrosine, phenylalanine) in proteins absorb at 280 nm. A pure dsDNA preparation has an A260/A280 ratio of ~1.8; pure RNA has a ratio of ~2.0.",
    "example": "An A260/A280 ratio of 1.4 in a hippocampal DNA extract indicates residual protein or phenol contamination, requiring re-precipitation.",
    "id": "mol-099",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Spectrophotometric A260/A230 Ratio and Organics",
    "prompt": "An A260/A230 spectrophotometric ratio substantially lower than 2.0 (e.g. < 1.5) in a TRIzol RNA extraction indicates contamination with:",
    "options": [
      "EDTA at neutral pH",
      "Ribosomal RNA fragments",
      "Plasmid vectors",
      "Guanidinium isothiocyanate, phenol, or carbohydrate carryover"
    ],
    "answer": 3,
    "explain": "Organic compounds such as chaotropic guanidinium salts, phenol, and polysaccharides absorb strongly at 230 nm. A pure RNA sample should exhibit an A260/A230 ratio between 2.0 and 2.2; lower values warn that residual salts may inhibit downstream reverse transcriptase enzymes.",
    "example": "Washing the RNA pellet with 75% ethanol removes residual guanidinium salts, restoring the A260/A230 ratio from 1.2 to 2.1.",
    "id": "mol-100",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "SDS-PAGE Stacking vs Resolving Gel Chemistry",
    "prompt": "In discontinuous SDS-PAGE (Laemmli system), how does the pH 6.8 stacking gel concentrate dilute protein samples into a razor-thin starting band?",
    "options": [
      "Via isotachophoresis: at pH 6.8, glycine is a zwitterion with near-zero net charge (slow trailing ion), while chloride is fully ionized (fast leading ion), sandwiching proteins between them into a tight stack before entering the pH 8.8 resolving gel",
      "By boiling the proteins inside the gel wells",
      "By filtering proteins through glass wool",
      "By precipitating proteins with ammonium sulfate"
    ],
    "answer": 0,
    "explain": "In the pH 6.8 stacking gel, glycine zwitterions move slowly behind the leading chloride ions, creating a steep local voltage gradient that compresses all proteins into a razor-thin starting line. Upon entering the pH 8.8 resolving gel, glycine deprotonates into a fast anion, passing the proteins and allowing sieving by molecular weight.",
    "example": "Discontinuous stacking ensures that a 30 μL dilute synaptic lysate enters the resolving gel as a sub-millimeter band, yielding sharp Western blot signals.",
    "id": "mol-101",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "PVDF vs Nitrocellulose Transfer Membranes",
    "prompt": "In Western blotting, Polyvinylidene Difluoride (PVDF) transfer membranes are preferred over nitrocellulose for stripping and reprobing because:",
    "options": [
      "PVDF is completely transparent to ultraviolet light",
      "PVDF possesses higher mechanical tensile strength and higher protein binding capacity (~150-200 μg/cm2), but requires mandatory pre-wetting in 100% methanol",
      "PVDF binds only phosphorylated proteins",
      "PVDF dissolves in water after 24 hours"
    ],
    "answer": 1,
    "explain": "PVDF is a hydrophobic fluoropolymer with exceptional tensile strength, withstanding multiple rounds of harsh chemical stripping and reprobing without tearing. Its high binding capacity ensures retention of low-abundance proteins, though its hydrophobicity necessitates brief methanol activation before equilibration in transfer buffer.",
    "example": "Reprobing a brain membrane blot five times with distinct synaptic antibodies requires PVDF membranes to avoid membrane disintegration.",
    "id": "mol-102",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Hybridoma Technology for Monoclonal Antibodies",
    "prompt": "In Kohler and Milstein's classic hybridoma technology, fused myeloma-splenocyte cells are selectively isolated using HAT medium because:",
    "options": [
      "HAT medium contains penicillin that degrades non-hybridoma membranes",
      "HAT medium selectively kills all cells except neurons",
      "Aminopterin blocks the de novo nucleotide synthesis pathway, forcing cells to use the salvage pathway (HGPRT and thymidine kinase); myeloma partner cells are HGPRT-deficient and die, whereas unfused splenocytes have a finite lifespan, leaving only immortal hybridomas alive",
      "Aminopterin specifically stimulates antibody transcription"
    ],
    "answer": 2,
    "explain": "The myeloma fusion partner lacks hypoxanthine-guanine phosphoribosyltransferase (HGPRT-). Aminopterin in HAT medium blocks de novo purine/pyrimidine synthesis. Unfused myeloma cells die because they cannot salvage hypoxanthine; unfused splenocytes die naturally after a few days; only hybridomas (inheriting immortality from myelomas and functional HGPRT from B cells) survive.",
    "example": "Screening HAT-resistant hybridoma clones identifies monoclonal lines producing invariant antibodies against PSD-95 or gephyrin.",
    "id": "mol-103",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Gateway Recombination Cloning Logic",
    "prompt": "The Gateway cloning system uses bacteriophage lambda site-specific recombination to shuttle cDNAs into diverse expression vectors without restriction enzymes via:",
    "options": [
      "Random insertion by retrotransposons",
      "Direct blunt-end ligation using T4 DNA ligase",
      "CRISPR-mediated homologous recombination in bacteria",
      "BP reactions (attB x attP using BP Clonase to generate Entry clones) and LR reactions (attL x attR using LR Clonase to transfer cDNA into Destination vectors)"
    ],
    "answer": 3,
    "explain": "Gateway cloning utilizes lambda integrase/excisionase machinery. A PCR product flanked by attB sites recombines with an attP donor vector (BP reaction) to create an Entry clone flanked by attL sites. Recombining the Entry clone with an attR Destination vector (LR reaction) directionally transfers the insert into any viral or mammalian expression vector in 1 hour.",
    "example": "Shuttling a GCaMP cDNA from a single Gateway Entry clone into multiple destination vectors containing hSyn, CaMKII, or GFAP promoters in parallel.",
    "id": "mol-104",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Golden Gate Assembly Type IIS Endonucleases",
    "prompt": "Golden Gate assembly enables one-pot, seamless, scarless assembly of multiple DNA fragments simultaneously because Type IIS restriction enzymes (e.g. BsaI, BsmBI):",
    "options": [
      "Cleave double-stranded DNA outside of their non-palindromic recognition sequence, generating custom 4-base-pair overhangs that eliminate the restriction site from the final assembled product",
      "Cleave at the exact center of palindromic sequences",
      "Degrade all circular plasmids",
      "Ligate DNA fragments without requiring ATP"
    ],
    "answer": 0,
    "explain": "Type IIS enzymes recognize asymmetric sequences (e.g. 5'-GGTCTC-3' for BsaI) and cut 1 and 5 bp downstream. By placing recognition sites at fragment ends facing inward, digestion exposes user-defined 4 bp cohesive overhangs and removes the enzyme site, preventing re-cleavage of the ligated product and driving complete assembly in one tube.",
    "example": "Assembling complex multi-part CRISPR guide RNA arrays or modular optogenetic constructs with 10 distinct fragments in a single 30-cycle Golden Gate reaction.",
    "id": "mol-105",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Proximity Ligation Assay (PLA) Resolution",
    "prompt": "The in situ Proximity Ligation Assay (PLA) visualizes endogenous protein-protein interactions in fixed brain slices with high spatial precision because:",
    "options": [
      "It requires genetic overexpression of fluorescent proteins",
      "Secondary antibodies conjugated to unique oligonucleotides form a circular DNA template that undergoes rolling circle amplification (RCA) and fluorescent probe binding only when the two target proteins are within <40 nanometers of each other",
      "It measures fluorescence lifetime in living tissue",
      "It uses heavy water (D2O) to precipitate protein complexes"
    ],
    "answer": 1,
    "explain": "Two primary antibodies from different species bind candidate interacting proteins. Secondary antibodies conjugated to PLA oligos bind. If the epitopes are within <40 nm, connector oligos hybridize to both probes, are ligated into a circle by T4 ligase, and phi29 DNA polymerase performs rolling circle amplification, generating hundreds of tandem repeats detected as bright, punctate fluorescent spots.",
    "example": "PLA in hippocampal slices reveals direct physical interaction between dopamine D1 and NMDA GluN1 receptors specifically within dendritic spines.",
    "id": "mol-106",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Yeast Two-Hybrid (Y2H) Gal4 Modular Transcription",
    "prompt": "The classic Yeast Two-Hybrid (Y2H) screen detects novel protein-protein interactions by exploiting the modular structure of the yeast Gal4 transcription factor, where:",
    "options": [
      "The bait protein cleaves the prey protein inside the endoplasmic reticulum",
      "Bait and prey proteins assemble an active potassium channel in yeast",
      "The DNA-Binding Domain (DBD) is fused to the 'bait' protein and the Activation Domain (AD) is fused to 'prey' proteins; interaction between bait and prey reconstitutes a functional transcription factor driving reporter gene expression (e.g. HIS3, LacZ)",
      "Interaction causes yeast cells to turn completely black"
    ],
    "answer": 2,
    "explain": "Gal4 consists of two physically separable domains: an N-terminal DBD that binds the UAS promoter and a C-terminal AD that recruits RNA Polymerase II. Neither domain activates transcription on its own. When bait and prey interact, they bring the DBD and AD into proximity, turning on nutritional reporters (HIS3, ADE2) that allow yeast growth on selective media.",
    "example": "Screening a brain cDNA prey library with the cytoplasmic tail of AMPA receptor GluA2 as bait in Y2H originally identified GRIP1 and PICK1 as interacting scaffolds.",
    "id": "mol-107",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "RNA Velocity Splicing Kinetics",
    "prompt": "In single-cell RNA sequencing data analysis, RNA velocity (La Manno et al., Nature 2018) predicts the future developmental trajectory and directional differentiation of individual neural cells by:",
    "options": [
      "Measuring the decay rate of 18S ribosomal RNA",
      "Measuring the physical speed of RNA polymerase II along chromosomes",
      "Calculating cell migration velocity across a Petri dish",
      "Distinguishing and modeling the quantitative ratio between unspliced nascent pre-mRNAs (containing introns) and mature spliced mRNAs for thousands of genes"
    ],
    "answer": 3,
    "explain": "Standard scRNA-seq captures both mature spliced mRNAs (exons only) and nascent unspliced pre-mRNAs (retaining introns). A high unspliced-to-spliced ratio indicates recent transcriptional induction, while a low ratio indicates active repression, defining a predictive velocity vector that forecasts the future state of each single cell.",
    "example": "Applying RNA velocity algorithms (scVelo) to developing mouse dentate gyrus resolves the continuous lineage progression from radial glia through intermediate progenitors to mature granule neurons.",
    "id": "mol-108",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Self-Complementary AAV (scAAV) Kinetics vs Packaging",
    "prompt": "Self-complementary AAV (scAAV) vectors achieve rapid transgene expression within 24 to 48 hours in the brain (compared to 2-3 weeks for single-stranded AAV), but suffer from what major constraint?",
    "options": [
      "The packaging capacity is halved to approximately 2.2 to 2.4 kilobases, because the vector carries an inverted repeat that folds into a dimeric double-stranded molecule upon uncoating",
      "They require radioactive iodine for purification",
      "They are toxic to all glial cells",
      "They can only be delivered through intracranial glass micropipettes"
    ],
    "answer": 0,
    "explain": "Single-stranded AAV must undergo rate-limiting host-cell second-strand DNA synthesis before transcription can initiate. Mutating one ITR creates a self-complementary inverted repeat that spontaneously anneals into transcription-competent dsDNA upon viral uncoating, speeding expression to days at the cost of halving cargo capacity to ~2.2 kb.",
    "example": "Onasemnogene abeparvovec (Zolgensma) for SMA utilizes an scAAV9 capsid to achieve rapid SMN1 expression in motor neurons before irreversible axonal atrophy occurs.",
    "id": "mol-109",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "CMV Promoter Silencing in Central Nervous System",
    "prompt": "Why has the strong viral Cytomegalovirus (CMV) immediate-early promoter largely fallen out of favor for chronic in vivo neuroscience experiments?",
    "options": [
      "It cleaves all endogenous mRNAs in the host cell",
      "It undergoes progressive DNA methylation and histone deacetylation in mammalian brain tissue, leading to complete transcriptional silencing within 2 to 4 weeks post-injection",
      "It requires continuous addition of tetracycline to remain active",
      "It drives expression exclusively in peripheral erythrocytes"
    ],
    "answer": 1,
    "explain": "The CMV promoter is recognized as foreign by mammalian host defenses, recruiting DNA methyltransferases and histone deacetylases that progressively heterochromatinize the viral promoter. Stable mammalian promoters (such as human Synapsin-1 hSyn, CaMKIIa, or CAG) resist silencing and sustain multi-year expression.",
    "example": "Cortical neurons injected with AAV-CMV-GFP show dimming fluorescence after 1 month, whereas AAV-hSyn-GFP maintains brilliant expression past 12 months.",
    "id": "mol-110",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Cas12a (Cpf1) T-Rich PAM and Cohesive Cleavage",
    "prompt": "How does the CRISPR endonuclease Cas12a (formerly Cpf1) differ from classic SpCas9 in its target recognition and cleavage architecture?",
    "options": [
      "Cas12a creates blunt double-strand breaks adjacent to G-rich PAMs",
      "Cas12a cuts only single-stranded RNA molecules",
      "Cas12a recognizes a T-rich 5'-TTTV-3' PAM, processes its own crRNA without requiring a tracrRNA, and introduces a staggered 5-nucleotide 5' overhang (cohesive sticky ends) distal to the PAM",
      "Cas12a is completely inactive at 37°C"
    ],
    "answer": 2,
    "explain": "SpCas9 targets G-rich regions (NGG) and leaves blunt cuts. Cas12a expands targeting to AT-rich promoters and introns via 5'-TTTV-3' PAMs. Its staggered 5 nt cohesive cut facilitates directional donor insertion during homology-directed repair and allows compact multiplexed guide arrays due to intrinsic RNase activity.",
    "example": "Cas12a is ideal for multiplexed gene knockout in neurons because a single promoter can transcribe an array of 5 distinct crRNAs that Cas12a autonomously cleaves into mature guides.",
    "id": "mol-111",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "dCas13-ADAR RNA Editing (REPAIR System)",
    "prompt": "The REPAIR (RNA Editing for Programmable A to I Replacement) system engineered by Feng Zhang and colleagues uses catalytically dead Cas13 (dCas13) fused to ADAR2 to:",
    "options": [
      "Block ribosomal translation of all cellular mRNAs",
      "Excise pathogenic CAG repeats from genomic DNA",
      "Methylate lysine residues on histone H3",
      "Directly deaminate specific adenosine bases into inosine (read as guanosine) in target mRNA transcripts without altering or cutting the genomic DNA sequence"
    ],
    "answer": 3,
    "explain": "dCas13 binds specific target mRNAs via guide RNA without cutting. Fusing dCas13 to the deaminase domain of ADAR2 directs hydrolytic deamination of targeted adenosines to inosines (A-to-I). Because inosine is read by ribosomes as guanosine, REPAIR enables programmable, reversible G-to-A disease mutation correction at the RNA level with zero risk of permanent genomic off-target mutations.",
    "example": "Applying REPAIR to correct a nonsense mutation in MECP2 mRNA restored functional full-length MeCP2 protein expression in cell models.",
    "id": "mol-112",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Prime Editing pegRNA Anatomy",
    "prompt": "In prime editing (Anzalone et al., Nature 2019), the prime editing guide RNA (pegRNA) directs Cas9 nickase fused to engineered reverse transcriptase by carrying:",
    "options": [
      "A standard 20 nt spacer directing Cas9 nickase to the target strand, plus a 3' extension containing a Primer Binding Site (PBS) and a Reverse Transcription Template (RTT) encoding the desired edit",
      "Two distinct palindromic restriction sites",
      "A poly-A tail of 500 adenines",
      "A radioactive phosphorus label"
    ],
    "answer": 0,
    "explain": "Cas9 nickase cuts only the non-target DNA strand. The liberated 3' single-stranded DNA flap hybridizes to the pegRNA's Primer Binding Site (PBS). The reverse transcriptase domain then copies the edit from the adjacent Reverse Transcription Template (RTT) directly into the DNA strand, facilitating all 12 base-to-base transitions, insertions, and deletions without double-strand breaks.",
    "example": "Prime editing successfully repaired the 4 bp pathogenic deletion in HEXA that causes Tay-Sachs disease in cortical neurons with minimal byproduct indels.",
    "id": "mol-113",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Mosaic Analysis with Double Markers (MADM)",
    "prompt": "Mosaic Analysis with Double Markers (MADM) allows single-cell genetic knockouts to be traced in the developing brain with absolute lineage fidelity by utilizing:",
    "options": [
      "Random injection of fluorescent beads into embryos",
      "Cre-mediated interchromosomal recombination during the G2 phase of dividing progenitors, generating daughter cells with homozygous mutations marked with GFP and sibling wild-type cells marked with tdTomato",
      "Viral infection with 10 different retroviruses",
      "Exposure of mice to sublethal X-ray irradiation"
    ],
    "answer": 1,
    "explain": "MADM splits chimeric GFP and RFP coding sequences across homologous chromosomes interrupted by loxP sites. G2-phase Cre-mediated recombination followed by X-segregation generates one green homozygous mutant daughter cell and one red homozygous wild-type sister cell, allowing direct cell-autonomous phenotypic comparison of mutant neurons alongside wild-type neighbors in the same brain slice.",
    "example": "MADM analysis of Lis1 mutant cortical projection neurons proved that Lis1 regulates cell migration in a strictly cell-autonomous manner.",
    "id": "mol-114",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Fiber Photometry Isosbestic 405 nm Normalization",
    "prompt": "In fiber photometry recording of GCaMP fluorescence in deep brain structures, why is a 405 nm excitation channel interleaved with the 470 nm calcium excitation channel?",
    "options": [
      "405 nm activates Channelrhodopsin-2 in presynaptic terminals",
      "405 nm excites a red fluorophore inside the same cell",
      "405 nm corresponds to the isosbestic point of GCaMP, where fluorescence emission is independent of calcium concentration, providing an internal reference to subtract motion artifacts, fiber bending, and autofluorescence",
      "405 nm measures extracellular pH changes"
    ],
    "answer": 2,
    "explain": "GCaMP has an isosbestic absorption point at ~405-410 nm where fluorescence does not change regardless of calcium levels. Any signal fluctuation at 405 nm is strictly an optical artifact (cable flexing, movement, photobleaching). Fitting the 405 nm trace to the 470 nm trace and calculating (F470 - F405_fit) / F405_fit yields artifact-free true neural delta-F/F.",
    "example": "During vigorous running behavior, raw 470 nm fiber photometry shows massive movement spikes that are completely eliminated after 405 nm isosbestic subtraction.",
    "id": "mol-115",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Fast-Scan Cyclic Voltammetry (FSCV) Dopamine Detection",
    "prompt": "Fast-Scan Cyclic Voltammetry (FSCV) at carbon-fiber microelectrodes measures sub-second in vivo dopamine transients based on:",
    "options": [
      "Recording membrane capacitance changes in postsynaptic spines",
      "Measuring light emission from a bioluminescent probe",
      "Collecting dialysate over 20-minute intervals for HPLC analysis",
      "Applying a high-speed triangular voltage ramp (-0.4 V to +1.3 V and back at 400 V/s) that rapidly oxidizes dopamine to dopamine-o-quinone, generating a diagnostic oxidation current peak at approximately +0.6 V"
    ],
    "answer": 3,
    "explain": "FSCV uses an 8-μm carbon-fiber electrode held at -0.4 V to adsorb catecholamines. A 400 V/s triangular ramp to +1.3 V oxidizes dopamine at ~+0.6 V and reduces dopamine-o-quinone at ~-0.2 V. The background-subtracted voltammogram provides a chemical fingerprint uniquely identifying dopamine with 100 ms temporal resolution.",
    "example": "FSCV recordings in the rat nucleus accumbens demonstrate phasic dopamine release bursts lasting 200 ms in response to conditioned sensory cues.",
    "id": "mol-116",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Patch-Clamp Series Resistance Compensation",
    "prompt": "In whole-cell voltage-clamp electrophysiology, uncompensated series resistance (Rs, pipette resistance plus access resistance) causes voltage-clamp errors because:",
    "options": [
      "A large synaptic current (I) flowing across the series resistance generates an unmeasured voltage drop (V_error = I * Rs), preventing the cell membrane from being held at the command potential",
      "It causes the patch pipette to melt",
      "It introduces persistent sodium channel inactivation",
      "It destroys all intracellular ATP"
    ],
    "answer": 0,
    "explain": "The actual membrane potential V_m = V_command - (I * Rs). If a neuron has an Rs of 20 M-Ohms and generates a 2 nA EPSC, the voltage error is 2 nA * 20 M-Ohms = 40 mV. Thus, a cell supposedly clamped at -70 mV actually depolarizes to -30 mV, causing severe distortion of synaptic kinetics and amplitudes.",
    "example": "Setting series resistance compensation to 70-80% on the patch amplifier minimizes voltage clamp errors during large evoked AMPA receptor currents.",
    "id": "mol-117",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Two-Photon Cranial Window Chronic Spine Dynamics",
    "prompt": "Chronic in vivo two-photon imaging of dendritic spine turnover across weeks in awake mice requires surgical implantation of a 'cranial window', where:",
    "options": [
      "The entire cerebral hemisphere is surgically removed",
      "A circular skull craniotomy is sealed with a glass coverslip bonded with cyanoacrylate and dental acrylic, maintaining physiological intracranial pressure and optical clarity for months",
      "A permanent hole is left open to atmospheric air",
      "The skull is thinned until it dissolves completely"
    ],
    "answer": 1,
    "explain": "The glass cranial window technique replaces a 3 mm circle of skull with an optical glass coverslip sealed hermetically with dental cement. This preserves normal brain physiology and intracranial pressure, enabling repeated two-photon imaging of the identical dendritic segments and spines over weeks to months.",
    "example": "Zuo, Gan, and colleagues used chronic two-photon cranial windows to show that motor skill learning promotes rapid formation and preferential stabilization of new dendritic spines in motor cortex.",
    "id": "mol-118",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Gradient Index (GRIN) Lens Deep Brain Endoscopy",
    "prompt": "Gradient Index (GRIN) micro-endoscopes enable optical calcium imaging of deep subcortical structures (such as the lateral hypothalamus or VTA) because:",
    "options": [
      "They are hollow needles that suck out cerebrospinal fluid",
      "They transmit light via total internal reflection like standard optical fibers",
      "They are slender cylindrical glass rods (0.5 to 1.0 mm diameter) with a radially parabolic refractive index profile that continually refracts light along a sinusoidal path, relaying deep focal planes to the skull surface",
      "They operate without any objective lens"
    ],
    "answer": 2,
    "explain": "Standard microscope objectives have working distances of <2 mm and cannot reach deep subcortical nuclei. A GRIN lens has a parabolic radial variation in refractive index (highest at the central axis, decreasing toward the edge), acting as a relay lens that transfers deep tissue images (up to 8 mm deep) to an external microscope objective.",
    "example": "Implanting a 0.6 mm GRIN lens above the substantia nigra pars compacta allows in vivo two-photon calcium imaging of dopaminergic neurons during locomotion.",
    "id": "mol-119",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Head-Mounted Miniature Microscopes (Miniscopes)",
    "prompt": "Open-source head-mounted miniature epifluorescence microscopes ('Miniscopes', pioneered by UCLA) advanced circuit neuroscience by allowing:",
    "options": [
      "Electrophysiological recording from thousands of neurons using light beams",
      "Whole-brain electron microscopy in live animals",
      "Direct sequencing of DNA in the skull",
      "Single-cell resolution calcium imaging of hundreds of fluorescent neurons in freely moving rodents performing unconstrained spatial, social, and anxiety behaviors, weighing under 3 grams"
    ],
    "answer": 3,
    "explain": "Traditional two-photon setups require head-fixed animals running on treadmills. Miniscopes integrate a miniature CMOS image sensor, LED illumination, and lightweight optics into a 2.5-gram 3D-printed housing mounted on a baseplate, enabling long-term recording of neuronal ensembles during naturalistic navigation in large mazes.",
    "example": "Miniscope imaging of hippocampal CA1 ensembles in freely exploring mice revealed representational drift of place cells across weeks.",
    "id": "mol-120",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "CLARITY Hydrogel-Tissue Chemistry",
    "prompt": "In Karl Deisseroth's CLARITY tissue clearing methodology, biological macromolecules are physically stabilized before lipid extraction by:",
    "options": [
      "Infusing acrylamide, bis-acrylamide, and formaldehyde to crosslink amine-bearing proteins and nucleic acids into a nanoporous hydrogel mesh, followed by SDS-mediated lipid extraction",
      "Freezing the brain in solid liquid nitrogen",
      "Dissolving the brain in 100% sulfuric acid",
      "Dehydrating the brain with acetone"
    ],
    "answer": 0,
    "explain": "CLARITY crosslinks cellular proteins and nucleic acids into a polyacrylamide hydrogel scaffold via formaldehyde crosslinking. Because phospholipids lack amine groups, they remain unbound and are stripped out using sodium dodecyl sulfate (SDS) micelles during passive or electrophoretic clearing, leaving an intact, optically transparent tissue-hydrogel hybrid.",
    "example": "Intact cleared mouse brains prepared with CLARITY can be repeatedly stained with antibodies and imaged in 3D without physical sectioning.",
    "id": "mol-121",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Light-Sheet Fluorescence Microscopy (LSFM) Planar Illumination",
    "prompt": "Light-Sheet Fluorescence Microscopy (LSFM / SPIM) is the optimal optical method for imaging large, cleared whole brains because:",
    "options": [
      "It uses scanning confocal pinholes to reject light",
      "A thin sheet of laser light illuminates only the single in-focus focal plane perpendicular to the widefield detection objective, virtually eliminating out-of-focus photobleaching and achieving rapid volumetric imaging",
      "It requires mechanical razor-blade slicing during imaging",
      "It records only infrared reflected light"
    ],
    "answer": 1,
    "explain": "Point-scanning confocal microscopes pass laser light through the entire specimen depth to image one pixel, causing massive photobleaching and taking days to scan a whole brain. LSFM illuminates only the plane being photographed by an sCMOS camera, collecting complete optical planes in milliseconds with minimal phototoxicity.",
    "example": "Imaging an entire iDISCO-cleared mouse brain on a light-sheet microscope takes under 2 hours and generates a comprehensive 3D map of c-Fos+ activated neuronal ensembles.",
    "id": "mol-122",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Tandem Mass Tagging (TMT) Isobaric Multiplexing",
    "prompt": "Tandem Mass Tagging (TMT) achieves multiplexed quantitative proteomics of up to 18 distinct brain tissue samples in a single LC-MS/MS run because TMT reagents:",
    "options": [
      "Emit different colored photons upon laser excitation",
      "Are radioactive isotopes that decay at different rates",
      "Are isobaric tags sharing identical total chemical mass and chromatographic retention, but fragment during high-energy collision-induced dissociation (HCD) to release unique, quantifiable reporter ions in the low-mass region (126-135 m/z)",
      "Carry different electrical charges that separate proteins by gel electrophoresis"
    ],
    "answer": 2,
    "explain": "Each TMT tag consists of an amine-reactive NHS ester, a mass normalizer, and a mass reporter. In MS1, peptides from all samples co-migrate as a single combined peak. In MS2, fragmentation cleaves the reporter arm, releasing distinct reporter ions whose relative peak heights directly quantify peptide abundance across the pooled conditions.",
    "example": "A 16-plex TMT experiment quantifies proteome-wide synaptic alterations across multiple brain regions in Alzheimer's disease versus control autopsy cases.",
    "id": "mol-123",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Data-Independent Acquisition (DIA) Mass Spectrometry",
    "prompt": "Data-Independent Acquisition (DIA, e.g. SWATH-MS) overcomes the stochastic missing-value problem of classic Data-Dependent Acquisition (DDA) proteomics by:",
    "options": [
      "Sequencing only phosphorylated peptides",
      "Selecting only the top 10 most abundant peptide peaks for fragmentation",
      "Discarding all low-molecular-weight peptides",
      "Sequentially stepping broad precursor isolation windows (e.g. 25 m/z) across the entire mass range to fragment all precursor ions within every window, creating a complete and reproducible digital proteome map"
    ],
    "answer": 3,
    "explain": "In DDA, the mass spectrometer dynamically chooses the most intense peaks in MS1, causing stochastic missing values between runs. In DIA, the instrument fragments all ions in broad contiguous m/z bins across the entire chromatographic gradient, generating dense composite MS2 spectra that are deconvoluted using spectral libraries.",
    "example": "DIA mass spectrometry of human postmortem cerebrospinal fluid reliably quantifies >1,500 proteins across hundreds of clinical cohorts with zero missing data points.",
    "id": "mol-124",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Ribo-seq Ribosome Footprinting Principle",
    "prompt": "Ribosome profiling (Ribo-seq, Ingolia & Weissman 2009) maps global translatomes at single-codon resolution by:",
    "options": [
      "Treating lysates with cycloheximide to freeze translating ribosomes, digesting unprotected mRNA with RNase I, and sequencing the 28-30 nucleotide 'ribosome footprints' protected inside the ribosomal exit channel",
      "Sequencing only total nuclear RNA",
      "Measuring antibody binding to ribosomal proteins",
      "Isolating polysomes on sucrose gradients without nuclease treatment"
    ],
    "answer": 0,
    "explain": "Translating ribosomes physically protect ~28-30 nucleotides of mRNA from RNase digestion. Deep sequencing of these ribosome-protected fragments (RPFs) precisely identifies which mRNAs are actively being translated and reveals non-canonical translation of upstream open reading frames (uORFs) and novel microproteins in neurons.",
    "example": "Ribo-seq in cortical neurons demonstrates that synaptic stimulation triggers instantaneous local translation of pre-existing dendritic mRNAs without de novo transcription.",
    "id": "mol-125",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Two-Photon Glutamate Uncaging Single Spines",
    "prompt": "Two-photon photolysis of 'caged' glutamate (e.g. MNI-caged L-glutamate) facilitates optical mapping of single-synapse function because:",
    "options": [
      "It irreversibly destroys the dendritic spine",
      "A biologically inactive, photolabile protective cage group is cleaved within microseconds by two-photon infrared laser absorption (720 nm) strictly within a tiny sub-femtoliter focal volume, mimicking single-vesicle quantal release at a single spine head",
      "It stimulates release of acetylcholine from presynaptic vesicles",
      "It opens only voltage-gated sodium channels"
    ],
    "answer": 1,
    "explain": "MNI-glutamate is biologically inert. Focused femtosecond laser pulses at 720 nm drive two-photon uncaging strictly at the diffraction-limited focal point (~0.1 femtoliters), delivering a focal pulse of free L-glutamate that activates AMPA receptors on a single chosen spine without spilling onto neighbors.",
    "example": "Matsuzaki et al. (Nature 2001) used two-photon glutamate uncaging to prove that individual dendritic spine head volume correlates linearly with functional AMPA receptor sensitivity (uEPSC amplitude).",
    "id": "mol-126",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Calcium Imaging Neuropil Contamination Subtraction",
    "prompt": "In somatic two-photon calcium imaging in dense cortical tissue, why must somatic GCaMP traces undergo neuropil signal subtraction (F_corrected = F_soma - r * F_neuropil)?",
    "options": [
      "To amplify the signal by 10-fold",
      "To remove background autofluorescence from the microscope objective glass",
      "Fluorescence from out-of-focus overlapping axons and dendritic branches in the surrounding neuropil contaminates somatic ROIs, causing false-positive correlations and distorted spike inference if uncorrected (typically r ~ 0.7)",
      "Because neuropil absorbs green light"
    ],
    "answer": 2,
    "explain": "In densely packed cortex, a somatic region-of-interest (ROI) inevitably captures light from thousands of fine, intertwined axonal fibers and dendritic branches passing above, below, and around the cell body. Measuring an annular halo around each soma (F_neuropil) and subtracting r * F_neuropil (r ~ 0.7) isolates true somatic calcium transients.",
    "example": "Failure to perform neuropil subtraction makes all neighboring neurons appear artificially synchronized during locomotion due to shared neuropil glow.",
    "id": "mol-127",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "MINFLUX Nanometer Single-Molecule Localization",
    "prompt": "Developed by Nobel laureate Stefan Hell, MINFLUX nanoscopy achieves 1 to 3 nanometer spatial resolution in living cells by:",
    "options": [
      "Infusing heavy mercury atoms into the cell membrane",
      "Using high-dose X-ray beams",
      "Freezing the specimen in liquid helium and cutting 5 nm slices",
      "Targeting individual fluorophores with an excitation beam containing a central intensity zero (donut beam); iteratively adjusting the donut position until photon emission drops to zero localizes the molecule with minimal photon emissions (~100 photons)"
    ],
    "answer": 3,
    "explain": "Standard PALM/STORM requires collecting thousands of photons to find the center of a diffraction-limited spot. MINFLUX turns this logic around: it sweeps an excitation beam with a dark center across the molecule. When the molecule is exactly at the central zero, zero photons are emitted. By minimizing emission, MINFLUX pinpoints coordinates with 1-2 nm precision using 20-fold fewer photons.",
    "example": "MINFLUX tracking in living axons resolved the individual 8-nanometer steps of single kinesin-1 motor proteins walking along microtubule protofilaments.",
    "id": "mol-128",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "DNA-PAINT Super-Resolution Kinetics",
    "prompt": "DNA-Point Accumulation in Nanoscale Topography (DNA-PAINT, Jungmann et al.) avoids photobleaching limitations in super-resolution imaging by utilizing:",
    "options": [
      "Transient, repetitive, low-affinity binding of short dye-labeled single-stranded oligonucleotides ('imager' strands) to complementary target-bound 'docking' strands, maintaining continuous blinking indefinitely from a constant solution reservoir",
      "Permanent covalent binding of antibodies",
      "High-power laser ablation of the specimen surface",
      "Direct labeling of DNA with heavy metal clusters"
    ],
    "answer": 0,
    "explain": "Traditional STORM fluorophores photobleach after a few thousand frames. In DNA-PAINT, target proteins carry a short docking oligo (~9-10 nt). Dye-labeled imager strands in the buffer transiently bind for ~100 ms and dissociate. Continuous exchange from the buffer reservoir provides infinite photon budgets, achieving sub-5 nm resolution across unlimited imaging cycles.",
    "example": "DNA-PAINT resolved the copy number and nanoscale clustering of individual Bassoon and Piccolo scaffold molecules within the presynaptic cytomatrix.",
    "id": "mol-129",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Optogenetically Tagged Single-Unit Recording (Opto-Tagging)",
    "prompt": "In extracellular in vivo neurophysiology, 'opto-tagging' definitively links an isolated single-unit spike waveform to a specific genetically defined cell type (e.g. PV interneurons) by:",
    "options": [
      "Sequencing the DNA of the electrode wire",
      "Delivering brief laser pulses (1-5 ms) to activate Channelrhodopsin-2 in Cre-expressing neurons, identifying units that fire action potentials with ultra-short latency (<3-5 ms), low jitter (<1 ms), and identical spike waveforms to spontaneous spikes",
      "Bleaching all neighboring cells with ultraviolet light",
      "Injecting fluorescent retro-beads through the recording electrode"
    ],
    "answer": 1,
    "explain": "Extracellular electrodes record spikes blindly from mixed cell populations. By expressing ChR2 in a specific Cre line (e.g. PV-Cre), delivering a brief light pulse selectively evokes direct spikes in ChR2+ cells. Units with sub-3 ms latency, low variance (jitter <0.5 ms), and matching waveform correlation (r > 0.95) are validated as the genetically tagged cell type.",
    "example": "Lima et al. used opto-tagging to prove that fast-spiking PV interneurons in primary auditory cortex provide divisive gain control of pyramidal neuron receptive fields.",
    "id": "mol-130",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Coomassie R-250 SDS-PAGE Gel Staining",
    "prompt": "Staining an SDS-PAGE polyacrylamide gel with 0.1% Coomassie Brilliant Blue R-250 in methanol/acetic acid detects total protein with a detection sensitivity of approximately:",
    "options": [
      "0.01 picograms of protein per band",
      "10 milligrams of protein per band",
      "30 to 50 nanograms of protein per band",
      "Only DNA molecules"
    ],
    "answer": 2,
    "explain": "Coomassie R-250 binds stoichiometrically to basic and aromatic amino acid residues via electrostatic and hydrophobic interactions. Following destaining in 10% acetic acid/methanol to clear background gel, distinct blue protein bands become visible with a sensitivity limit of ~30-50 ng.",
    "example": "Visualizing purified recombinant GFP on a Coomassie-stained gel confirms purity and confirms absence of contaminating bacterial proteins.",
    "id": "mol-131",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Silver Staining for Low-Abundance Proteins",
    "prompt": "Silver staining of SDS-PAGE gels provides sub-nanogram (~0.5-1 ng) detection sensitivity for low-abundance proteins by exploiting:",
    "options": [
      "Antibody-conjugated enzymatic luminescence",
      "Fluorescence emission under ultraviolet light",
      "Radioactive beta-decay of silver isotopes",
      "The reduction of silver ions (Ag+) to metallic black silver (Ag0) by formaldehyde in an alkaline sodium carbonate developing solution at the site of protein bands"
    ],
    "answer": 3,
    "explain": "Silver staining is ~50- to 100-fold more sensitive than Coomassie staining. Silver ions bind sulfhydryl and carboxyl groups on proteins; subsequent treatment with alkaline formaldehyde reduces bound silver into insoluble microscopic black metallic grains that visualize trace protein bands.",
    "example": "Silver staining of immunoprecipitated postsynaptic complexes reveals faint co-purifying interacting bands invisible by standard Coomassie staining.",
    "id": "mol-132",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Western Blot Blocking Agents Casein vs BSA",
    "prompt": "When probing Western blots with phospho-specific antibodies (e.g. anti-p-CaMKII or anti-p-tau), why must non-fat dry milk be avoided as a blocking agent?",
    "options": [
      "Non-fat milk contains abundant casein, a heavily phosphorylated milk protein that causes high non-specific background and quenches phospho-specific primary antibodies; 3-5% BSA should be used instead",
      "Milk digests the PVDF transfer membrane",
      "Milk inhibits horseradish peroxidase enzyme activity",
      "Milk cleaves peptide bonds at room temperature"
    ],
    "answer": 0,
    "explain": "Casein is a rich source of phosphoserine and phosphothreonine residues. Using milk blocking buffers causes phospho-specific antibodies to cross-react with casein on the membrane, creating intense background smearing and false-negative detection of target phosphorylated proteins.",
    "example": "Probing brain lysates for p-tau Ser202/Thr205 with antibody AT8 yields pristine signal-to-noise only when blocked in 5% Bovine Serum Albumin (BSA) in TBST.",
    "id": "mol-133",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Ponceau S Reversible Membrane Staining",
    "prompt": "In Western blotting protocols, staining transfer membranes with Ponceau S dye prior to antibody blocking is valuable because:",
    "options": [
      "It permanently fixes proteins to the membrane so they never detach",
      "It provides immediate, reversible visual confirmation of uniform protein transfer across all lanes without interfering with downstream antibody binding",
      "It acts as a secondary antibody detection reagent",
      "It selectively stains only nuclear transcription factors"
    ],
    "answer": 1,
    "explain": "Ponceau S is a rapid, non-destructive red dye that binds positively charged amino groups. It reveals transfer quality, air bubbles, and equal lane loading within 1 minute, and washes out completely with water or TBST before primary antibody incubation.",
    "example": "Ponceau S staining of a cortical membrane blot immediately reveals air-bubble artifacts that blocked transfer in lane 4, prompting re-transfer before wasting expensive antibodies.",
    "id": "mol-134",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Agarose Gel Loading Dye Density and Tracking",
    "prompt": "A standard 6x DNA gel loading dye contains glycerol or Ficoll along with tracking dyes (bromophenol blue and xylene cyanol) to:",
    "options": [
      "Stain the DNA with fluorescent light",
      "Amplify the DNA during electrophoresis",
      "Increase sample density so the DNA sinks to the bottom of the well, and provide visible color fronts to monitor electrophoretic migration distance in real time",
      "Prevent DNA from melting at room temperature"
    ],
    "answer": 2,
    "explain": "Glycerol or Ficoll increases the density of the sample relative to the TAE/TBE running buffer, ensuring the sample sinks evenly into the submerged well. Negatively charged tracking dyes migrate predictably (xylene cyanol ~4 kb, bromophenol blue ~300 bp in 1% agarose), indicating when to stop the electrical current.",
    "example": "Turning off the gel power supply when the dark blue bromophenol blue front reaches 2/3 of the gel length ensures small 200 bp PCR amplicons do not run off the bottom.",
    "id": "mol-135",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Hot-Start Taq Polymerase Mechanism",
    "prompt": "'Hot-Start' Taq DNA polymerases eliminate non-specific amplification and primer-dimer formation during PCR setup by:",
    "options": [
      "Carrying out PCR in a microwave oven",
      "Adding ice cubes to the PCR master mix",
      "Using radioactive dNTPs",
      "Inactivating the polymerase at room temperature with a bound monoclonal antibody or chemical moiety that dissociates only upon initial 95°C thermal denaturation"
    ],
    "answer": 3,
    "explain": "Standard Taq retains residual enzymatic activity at room temperature (20-25°C), extending misprimed primers and forming primer-dimers during reaction assembly. Hot-start formulations sequester the polymerase in an inactive complex until the initial 95°C heating step activates the enzyme, ensuring stringent high-temperature annealing.",
    "example": "Hot-start Taq is essential for low-copy-number genotyping assays, preventing spurious low-molecular-weight primer-dimer bands.",
    "id": "mol-136",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Touchdown PCR Annealing Strategy",
    "prompt": "Touchdown PCR improves reaction specificity for challenging neurogenetics templates by:",
    "options": [
      "Starting initial cycles at an annealing temperature several degrees above the calculated primer Tm, then decreasing by 0.5-1°C per cycle down to the final annealing temperature",
      "Freezing the tubes between every cycle",
      "Doubling the extension time every 5 minutes",
      "Decreasing the denaturation temperature to 50°C"
    ],
    "answer": 0,
    "explain": "High initial annealing temperatures favor only perfectly matched primer-template hybrids, exponentially amplifying the desired target in early cycles. By the time lower temperatures are reached in later cycles, the specific product outcompetes any non-specific mispriming.",
    "example": "Amplifying GC-rich promoters or repetitive trinucleotide repeat loci (such as FMR1 or HTT) with touchdown PCR yields sharp single amplicons devoid of non-specific smears.",
    "id": "mol-137",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Bimolecular Fluorescence Complementation (BiFC)",
    "prompt": "Bimolecular Fluorescence Complementation (BiFC, Split-YFP) directly visualizes protein-protein interactions in living cells because:",
    "options": [
      "It requires radioactive uranium isotopes",
      "Two non-fluorescent N-terminal and C-terminal fragments of a fluorescent protein (e.g. YFP1-154 and YFP155-238) refold into an active fluorophore when brought together by interacting fusion partners",
      "The fluorophore changes color from blue to red upon ATP hydrolysis",
      "It measures mass differences on mass spectrometers"
    ],
    "answer": 1,
    "explain": "Neither half of split-YFP can fluoresce on its own. When candidate interacting proteins (fused to NYFP and CYFP) bind in living cells, the two halves are brought into proximity, reconstituting the intact beta-barrel and generating permanent green/yellow fluorescence at the site of interaction.",
    "example": "BiFC in cultured cortical neurons reveals localized alpha-synuclein oligomerization specifically within presynaptic axonal varicosities.",
    "id": "mol-138",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Sucrose Cushion Centrifugation of Amyloid Fibrils",
    "prompt": "In biochemical studies of neurodegeneration, high-speed ultracentrifugation of brain lysates through a 20-50% sucrose cushion (e.g. at 100,000 x g for 1 hour) is used to:",
    "options": [
      "Precipitate soluble albumin",
      "Separate DNA from RNA",
      "Pellet high-molecular-weight insoluble amyloid fibrils and paired helical filaments while leaving soluble monomers and small oligomers in the supernatant",
      "Lyse intact cell nuclei"
    ],
    "answer": 2,
    "explain": "Dense protein fibrils (cross-beta amyloid or tau polymers) have high sedimentation coefficients that sediment through high-density sucrose cushions, whereas soluble monomeric and physiological dimeric species cannot penetrate the cushion, cleanly separating pathological inclusions for Western blot quantification.",
    "example": "Western blotting of sucrose-cushion pellets from Alzheimer's brain extracts reveals hyperphosphorylated, insoluble PHF-tau multimers.",
    "id": "mol-139",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Immunoisolation of Intact Synaptic Vesicles",
    "prompt": "Pure 40-nanometer synaptic vesicles are selectively immunoisolated from crude synaptosomal lysates using magnetic beads conjugated to antibodies against:",
    "options": [
      "Mitochondrial cytochrome c oxidase",
      "Postsynaptic PSD-95",
      "Nuclear histone H3",
      "Integral synaptic vesicle transmembrane proteins (e.g. Synaptophysin-1 or VGLUT1)"
    ],
    "answer": 3,
    "explain": "Synaptophysin-1 is the most abundant integral membrane protein of synaptic vesicles (~32 copies per 40 nm vesicle). Magnetic beads coated with anti-synaptophysin or anti-VGLUT1 antibodies capture intact vesicular spheres from hypotonically lysed synaptosomes without contamination from active zone plasma membranes.",
    "example": "Immunoisolated synaptic vesicles can be assayed for ATP-dependent vesicular glutamate uptake driven by V-ATPase acidification.",
    "id": "mol-140",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Quantitative Western Blot Linear Dynamic Range",
    "prompt": "Why has near-infrared (NIR) fluorescent Western blotting (e.g. LI-COR Odyssey with IRDye 680/800) largely replaced chemiluminescent film for quantitative protein measurements?",
    "options": [
      "NIR fluorescence displays a broad linear dynamic range spanning 3 to 4 orders of magnitude, avoiding the rapid enzymatic saturation and film over-exposure characteristic of ECL",
      "NIR signals can only be observed with the naked eye",
      "Chemiluminescence cannot detect phosphorylated proteins",
      "NIR blots require zero antibodies"
    ],
    "answer": 0,
    "explain": "ECL relies on enzymatic HRP turnover and photographic film, both of which saturate rapidly at high protein concentrations, compressing quantitative dynamic range to less than 1 order of magnitude. Direct near-infrared fluorophores emit photon counts directly proportional to antibody binding across a 4,000-fold dynamic range.",
    "example": "Multiplexing an IRDye 800-labeled anti-target antibody with an IRDye 680-labeled anti-beta-actin antibody allows simultaneous, non-saturated ratio normalization in the same blot lane.",
    "id": "mol-141",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "In Vitro Kinase Assay with Radio-Labeled ATP",
    "prompt": "An in vitro kinase phosphorylation assay definitively measures direct substrate phosphorylation by incubating purified kinase and recombinant substrate in the presence of:",
    "options": [
      "[alpha-32P]dCTP",
      "[gamma-32P]ATP, measuring covalent transfer of the radioactive gamma-phosphate onto serine, threonine, or tyrosine residues via autoradiography",
      "Unlabeled adenosine diphosphate",
      "Heavy water and urea"
    ],
    "answer": 1,
    "explain": "Protein kinases selectively transfer the terminal gamma-phosphate from ATP onto the hydroxyl group of target amino acid side chains. Using [gamma-32P]ATP produces a covalently radiolabeled substrate that resolves as a radioactive band on SDS-PAGE upon phosphorimaging, proving direct enzymatic catalysis.",
    "example": "Incubating purified CaMKII with recombinant synapsin-1 in the presence of calcium/calmodulin and [gamma-32P]ATP demonstrates rapid, direct phosphorylation of synapsin Site 1.",
    "id": "mol-142",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Electrophoretic Mobility Shift Assay (EMSA)",
    "prompt": "The Electrophoretic Mobility Shift Assay (EMSA or gel shift) evaluates transcription factor binding to specific brain promoter elements based on the principle that:",
    "options": [
      "Bound proteins become fluorescent under ultraviolet light",
      "DNA fragments are degraded when bound by proteins",
      "Protein-DNA complexes migrate significantly slower through a non-denaturing polyacrylamide gel than free, unbound radiolabeled DNA probes ('shifted band')",
      "Unbound DNA runs backwards toward the cathode"
    ],
    "answer": 2,
    "explain": "In non-denaturing gels, migration depends on mass, charge, and shape. When a nuclear transcription factor (e.g. CREB) binds a 32P-labeled oligonucleotide probe (e.g. a CRE element), the increased mass and altered hydrodynamic radius retards migration relative to free probe. Adding a specific antibody causes an even larger 'supershift'.",
    "example": "Incubating nuclear extracts from depolarized cortical neurons with a labeled CRE probe yields a prominent shifted band that is supershifted by an anti-CREB antibody.",
    "id": "mol-143",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Helper-Dependent Gutless Adenoviral Vectors (HDAd)",
    "prompt": "Helper-Dependent 'gutless' Adenoviral (HDAd) vectors are uniquely advantageous for neural gene delivery when:",
    "options": [
      "Only small 20-nucleotide microRNAs are delivered",
      "Retrograde axonal transport is the sole objective",
      "Transgenes must integrate permanently into host telomeres",
      "Massive transgenes up to 30-36 kilobases (such as full-length genomic loci with native introns and promoters) must be delivered without eliciting chronic host cytotoxic T-cell immunity"
    ],
    "answer": 3,
    "explain": "HDAd vectors have all viral coding sequences completely deleted, retaining only the inverted terminal repeats (ITRs) and packaging signal (psi). They carry up to 36 kb of foreign DNA, avoid expressing viral antigens that trigger immune destruction, and provide lifelong episomal transgene expression in non-dividing neurons.",
    "example": "HDAd vectors have successfully delivered the entire 30 kb human huntingtin genomic locus into mouse brain models to study full-length protein interactions.",
    "id": "mol-144",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "AAV-PHP.eB Systemic BBB Transduction Mechanism",
    "prompt": "Engineered AAV-PHP.eB (Deverman et al., Nature Biotech 2016) crosses the adult blood-brain barrier following simple intravenous injection in C57BL/6 mice because:",
    "options": [
      "A 7-amino-acid peptide insert in capsid variable region VIII binds with high affinity to the GPI-anchored Ly6a/Sca-1 receptor on mouse brain microvascular endothelial cells, mediating transcytosis",
      "It physically disrupts brain endothelial tight junctions like a detergent",
      "It is small enough to pass through aquaporin water channels",
      "It infects only circulating red blood cells"
    ],
    "answer": 0,
    "explain": "AAV-PHP.eB displays the engineered peptide TLAVPFKA in the AAV9 capsid loop. In C57BL/6 mice, this peptide recognizes the endothelial surface receptor Ly6a (lymphocyte antigen 6 complex locus A), triggering efficient receptor-mediated transcytosis across the intact blood-brain barrier to transduce up to 70% of cortical neurons.",
    "example": "Retro-orbital intravenous injection of 10^11 vg AAV-PHP.eB-CAG-GFP yields pan-cerebral green fluorescence across both hemispheres without requiring intracranial surgery.",
    "id": "mol-145",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "AAV Capsid Surface Tyrosine Mutations (Y-to-F)",
    "prompt": "Arun Srivastava and colleagues demonstrated that mutating surface-exposed tyrosine residues to phenylalanine (Y-to-F) in AAV capsids dramatically boosts in vivo viral transduction by:",
    "options": [
      "Allowing the virus to replicate autonomously without helper genes",
      "Preventing epidermal growth factor receptor protein tyrosine kinase (EGFR-PTK) phosphorylation of the capsid, which otherwise triggers ubiquitination and proteasomal degradation of the virion before nuclear uncoating",
      "Making the capsid resistant to boiling water",
      "Converting single-stranded AAV into double-stranded DNA"
    ],
    "answer": 1,
    "explain": "Upon host cell entry, cellular tyrosine kinases phosphorylate surface tyrosines on intact AAV capsids, targeting virions for K48-linked polyubiquitination and cytoplasmic proteasomal destruction. Mutating targeted tyrosines to phenylalanine (Y-F) evades ubiquitination, allowing up to 10-fold more intact genomes to reach the nucleus.",
    "example": "Subretinal injection of quadruple-mutant Y-F AAV2 achieves robust photoreceptor transduction at 10-fold lower vector doses than wild-type AAV2.",
    "id": "mol-146",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Germline Recombination in Cre Driver Lines",
    "prompt": "When breeding conditional knockout mice, researchers must carefully monitor for unexpected 'germline recombination' because:",
    "options": [
      "The Cre protein is secreted in maternal milk and enters newborn pups",
      "Cre recombinase permanently mutates all mitochondrial DNA",
      "Certain Cre driver lines (e.g. Nestin-Cre, EIIa-Cre, or DAT-Cre) exhibit transient or ectopic Cre expression in male or female germ cells, converting a supposed tissue-specific floxed allele into a systemic, whole-body germline knockout in subsequent generations",
      "LoxP sites spontaneously delete in the presence of oxygen"
    ],
    "answer": 2,
    "explain": "Many neural promoters (such as Nestin) are transiently active in the developing germline. If a male breeder carries both Cre and a floxed allele, Cre can excise the loxP cassette in sperm, yielding offspring that inherit a whole-body null deletion (converting a conditional experiment into an unintentional global knockout).",
    "example": "Genotyping tail DNA for both the conditional 'floxed' allele and the excised 'delta' allele confirms whether unwanted germline recombination occurred.",
    "id": "mol-147",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "In Vivo Microdialysis Zero-Net-Flux Method",
    "prompt": "The zero-net-flux method in microdialysis allows precise determination of true basal extracellular neurotransmitter concentrations in the brain by:",
    "options": [
      "Using radio-labeled neurotransmitters only",
      "Stopping the perfusion pump for 24 hours to let fluid equilibrate",
      "Measuring electrical current at the probe tip",
      "Perfusing known concentrations of neurotransmitter through the probe and plotting net gain or loss against perfusate concentration; the point where net flux equals zero represents true in vivo extracellular concentration"
    ],
    "answer": 3,
    "explain": "Standard microdialysis recovery rate varies with probe fouling and local tissue diffusion. In the zero-net-flux protocol, perfusing multiple concentrations (some higher, some lower than expected brain levels) creates a linear regression: the concentration where [perfusate_in] = [perfusate_out] (net flux = 0) exactly equals the true, unperturbed extracellular concentration.",
    "example": "Zero-net-flux microdialysis determined that true basal extracellular dopamine in the striatum is approximately 5 to 10 nM.",
    "id": "mol-148",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Perforated Patch Clamp Gramicidin vs Amphotericin B",
    "prompt": "When performing perforated whole-cell patch-clamp recordings to measure the native GABA-A reversal potential (E_GABA), gramicidin is preferred over amphotericin B because gramicidin pores:",
    "options": [
      "Are permeable exclusively to monovalent cations (Na+, K+) while completely excluding chloride anions, preserving the native intracellular chloride concentration ([Cl-]i)",
      "Conduct only divalent calcium ions",
      "Block all potassium leak channels",
      "Rupture the plasma membrane within 10 seconds"
    ],
    "answer": 0,
    "explain": "Standard whole-cell recordings dialyze the cytoplasm, replacing endogenous chloride with pipette chloride and artificially setting E_GABA. Amphotericin B forms pores permeable to both cations and chloride. Gramicidin forms pores strictly permeable to monovalent cations (Na+, K+, H+) that reject Cl-, leaving intracellular chloride and GABA reversal potential unperturbed.",
    "example": "Gramicidin perforated patch recordings demonstrated the developmental shift of GABA from depolarizing in neonatal neurons to hyperpolarizing in mature neurons.",
    "id": "mol-149",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Liquid Junction Potential (LJP) Physics",
    "prompt": "In whole-cell electrophysiology, the Liquid Junction Potential (LJP) that arises between the internal pipette solution and the external bath solution is caused by:",
    "options": [
      "Temperature differences between the room and the microscope stage",
      "Differences in the mobilities of anions and cations diffusing across the liquid boundary before seal formation, creating a steady-state offset voltage (typically 10-15 mV for gluconate-based internals) that must be subtracted from measured potentials",
      "Electrical noise generated by the computer monitor",
      "Evaporation of water from the recording chamber"
    ],
    "answer": 1,
    "explain": "Potassium gluconate solutions use large, bulky gluconate anions that diffuse much more slowly than small, fast chloride anions in the bath. As ions diffuse across the pipette tip into the bath prior to seal formation, a charge separation develops, establishing a 10-15 mV offset. Failing to correct for LJP misreports actual resting membrane potentials by 10-15 mV.",
    "example": "Using the Henderson equation to calculate and correct a -12 mV LJP shifts a measured resting potential of -60 mV to the true physiological value of -72 mV.",
    "id": "mol-150",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Two-Photon Imaging of Microglial Motility",
    "prompt": "Davalos et al. (Nature Neurosci 2005) and Nimmerjahn et al. (Science 2005) used in vivo two-photon imaging in CX3CR1-GFP mice to revolutionize glial biology by demonstrating that:",
    "options": [
      "Microglial cells lack nuclei",
      "Microglia are completely immotile cells frozen in place",
      "Microglia in the healthy intact brain are not 'resting', but actively survey their microenvironment with dynamic, continuously extending and retracting ramified processes that converge onto focal laser injuries within minutes",
      "Microglia fire sodium action potentials at 50 Hz"
    ],
    "answer": 2,
    "explain": "Long considered quiescent until brain injury, resting microglia were revealed by time-lapse two-photon microscopy to possess astonishingly dynamic filopodia-like processes that scan the entire brain parenchyma every few hours. Focal laser ablation releases local ATP, triggering rapid P2Y12-dependent directional migration of microglial processes toward the lesion within 15-30 minutes.",
    "example": "Two-photon time-lapse imaging captures microglial processes physically contacting synaptic elements in visual cortex during sensory-driven activity.",
    "id": "mol-151",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Expansion Microscopy AcX Anchor Chemistry",
    "prompt": "In Expansion Microscopy (ExM), the chemical linker 6-((acryloyl)amino)hexanoic acid succinimidyl ester (AcX) is essential because it:",
    "options": [
      "Precipitates lipids into crystals",
      "Degrades the extracellular matrix",
      "Acts as a green fluorescent dye",
      "Features an NHS-ester that covalently reacts with primary amines on proteins and an acrylamide moiety that copolymerizes directly into the swellable polyacrylate hydrogel mesh"
    ],
    "answer": 3,
    "explain": "To expand proteins isotropically, they must be covalently anchored to the hydrogel. AcX's N-hydroxysuccinimide (NHS) ester reacts with lysine epsilon-amines on antibodies and endogenous proteins, leaving an exposed polymerizable vinyl group. When the acrylate monomer gel is cast, AcX integrates the proteins into the expanding polymer grid.",
    "example": "Treating brain sections with AcX prior to gelation guarantees that primary and secondary antibodies expand uniformly with the hydrogel matrix.",
    "id": "mol-152",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Two-Photon FLIM-AKAR PKA Biosensor",
    "prompt": "Two-photon Fluorescence Lifetime Imaging Microscopy using the FLIM-AKAR biosensor measures localized Protein Kinase A (PKA) signaling in single dendritic spines by:",
    "options": [
      "Detecting a decrease in GFP donor fluorescence lifetime when active PKA phosphorylates the sensor's substrate motif, driving an intramolecular FRET interaction with a forkhead-associated (FHA) phospho-binding domain",
      "Measuring whole-cell electrical conductance",
      "Staining neurons with radioactive phosphate",
      "Recording action potentials with sharp microelectrodes"
    ],
    "answer": 0,
    "explain": "FLIM-AKAR consists of a donor fluorophore (GFP), a PKA consensus substrate sequence, an FHA1 domain, and an acceptor. When PKA phosphorylates the substrate, the FHA1 domain binds the phosphorylated residue, kinking the biosensor and bringing donor and acceptor into FRET range, which immediately shortens the donor fluorescence lifetime.",
    "example": "2pFLIM imaging of FLIM-AKAR reveals that beta-adrenergic stimulation triggers PKA activation that is compartmentalized strictly within individual stimulated dendritic spines.",
    "id": "mol-153",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Orbitrap Mass Analyzer Fourier Transform Physics",
    "prompt": "In neuroproteomics, the Orbitrap mass analyzer achieves ultra-high mass resolution (>240,000 at m/z 200) and sub-ppm mass accuracy by:",
    "options": [
      "Measuring the time it takes for ions to hit a photographic plate",
      "Trapping ions in electrostatic orbital oscillation around a central spindle-shaped electrode; the harmonic axial oscillation frequency is detected via image current on split outer electrodes and converted to mass-to-charge ratios via Fourier transform",
      "Deflecting ions using a permanent magnetic field",
      "Measuring the boiling point of ionized peptides"
    ],
    "answer": 1,
    "explain": "Developed by Alexander Makarov, the Orbitrap uses solely electrostatic fields. Ions orbit around the central electrode and oscillate back and forth along its horizontal axis. The axial frequency omega = sqrt(k / (m/z)) is completely independent of initial ion energy or angle, yielding exquisite mass resolution upon Fourier transformation of the induced differential image current.",
    "example": "Orbitrap mass spectrometers resolve isobaric peptide post-translational modifications (e.g. trimethylation vs acetylation differences of 0.036 Da) in postmortem brain synaptosomes.",
    "id": "mol-154",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Voltron Genetically Encoded Voltage Indicator Chemistry",
    "prompt": "The chemigenetic voltage indicator Voltron (Abdelfattah et al., Science 2019) achieves unprecedented brightness and photostability in vivo by pairing:",
    "options": [
      "A firefly enzyme with coelenterazine",
      "A green fluorescent protein with a luciferase",
      "A microbial rhodopsin voltage-sensing domain with a self-labeling HaloTag that binds ultra-bright, photostable synthetic Janelia Fluor (JF) dyes, using electrochromic FRET to report membrane voltage",
      "A synthetic chemical dye directly injected into blood"
    ],
    "answer": 2,
    "explain": "Fluorescent proteins bleach rapidly during kilohertz-rate voltage imaging. Voltron solves this by fusing the Ace2 rhodopsin voltage sensor to HaloTag. Administering synthetic Janelia Fluor dyes (e.g. JF525) forms a covalent, exceptionally bright fluorophore whose emission is modulated by resonance energy transfer into the rhodopsin retinal as voltage shifts.",
    "example": "In vivo Voltron imaging in behaving fruit flies and zebrafish records hundreds of single action potentials across continuous 15-minute behavioral sessions without photobleaching.",
    "id": "mol-155",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Expansion STED (Ex-STED) Sub-10 nm Resolution",
    "prompt": "Combining 4.5-fold isotropic Expansion Microscopy with Stimulated Emission Depletion (Ex-STED) super-resolution microscopy achieves effective optical resolution below 10 nanometers, enabling:",
    "options": [
      "Imaging of living human brains through the intact skull",
      "Direct whole-genome sequencing of chromosomes on glass slides",
      "Observation of individual electron orbitals",
      "Direct optical resolution of single protein subunits within presynaptic active zone cytomatrix complexes and determination of molecular stoichiometry in individual active zones"
    ],
    "answer": 3,
    "explain": "STED optics provide ~30 nm optical resolution. When applied to a specimen physically expanded 4.5-fold by ExM, the effective resolution scales down to 30 nm / 4.5 = ~6-8 nm. This sub-10 nm resolution is comparable to Cryo-ET, resolving individual protein epitopes within the dense postsynaptic density.",
    "example": "Ex-STED imaging resolved individual Piccolo and Bassoon molecules organized in ring-like nanoclusters at the presynaptic active zone of hippocampal mossy fiber terminals.",
    "id": "mol-156",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "MINFLUX Single-Motor Tracking Precision",
    "prompt": "Tracking kinesin and dynein molecular motors in living neurites using MINFLUX achieves 1 to 2 nanometer spatial resolution and microsecond temporal resolution because:",
    "options": [
      "The position of a single organic fluorophore is triangulated by steering a donut-shaped excitation laser beam with a central zero intensity in a targeted local coordinate pattern, extracting maximal positional information per collected photon",
      "It uses radioactive uranium tracers",
      "It requires freezing the motor proteins in liquid helium",
      "It monitors acoustic shockwaves generated by ATP hydrolysis"
    ],
    "answer": 0,
    "explain": "MINFLUX uses a targeted donut-shaped excitation beam. When the emitter is at the central intensity minimum (zero), zero photons are emitted. By positioning the donut at four points around the emitter, the ratio of detected photon counts precisely triangulates coordinates with 1 nm precision using minimal total photon emissions.",
    "example": "MINFLUX tracking of kinesin-1 walking on microtubules in living neurites resolved individual 8 nm center-of-mass steps and the 16 nm hand-over-hand stepping of individual motor heads.",
    "id": "mol-157",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Anterograde Trans-Synaptic Tracing HSV Strain H129",
    "prompt": "Unlike rabies virus which travels strictly in the retrograde direction, Herpes Simplex Virus type 1 (HSV-1) strain H129 is unique in neuroanatomy because it:",
    "options": [
      "Transmits only via gap junctions",
      "Transmits trans-synaptically exclusively in the anterograde direction from presynaptic axon terminals across synaptic clefts into postsynaptic cell bodies",
      "Infects only vascular endothelial cells",
      "Spreads symmetrically in both directions equally"
    ],
    "answer": 1,
    "explain": "HSV-1 strain H129 possesses natural neurotropism with strict anterograde trans-neuronal propagation. Recombinant H129 expressing Cre or fluorescent reporters allows mapping of multi-synaptic downstream projection networks originating from a defined starter nucleus.",
    "example": "Injecting H129-GFP into primary visual cortex specifically maps polysynaptic feed-forward pathways through higher visual areas into the superior colliculus and amygdala.",
    "id": "mol-158",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM Helical Reconstruction of Tau Filament Polymorphs",
    "prompt": "Helical reconstruction of single-particle Cryo-EM micrographs from human neurodegenerative brain autopsy tissue established that tau filaments in Alzheimer's disease:",
    "options": [
      "Are composed entirely of full-length 441-amino-acid tau including the N-terminus",
      "Are amorphous random tangles devoid of any regular helical symmetry",
      "Consist of Paired Helical Filaments (PHFs) and Straight Filaments (SFs) composed of two identical C-shaped protofilaments spanning residues 306-378, packing against each other via two distinct symmetrical interfaces",
      "Contain no beta-sheet secondary structure"
    ],
    "answer": 2,
    "explain": "Fitzpatrick et al. (Nature 2017) utilized helical single-particle Cryo-EM to solve the structure of tau filaments isolated from Alzheimer's brain at 3.4 Å resolution. They proved that PHFs and SFs share identical C-shaped protofilaments (residues 306-378 adopting an 8-stranded cross-beta fold) that differ solely in how the two protofilaments pack against each other at their interface.",
    "example": "High-resolution Cryo-EM protofilament maps revealed that the tau core in Pick's disease has a completely different fold from Alzheimer's tau, explaining why Alzheimer's tau PET tracers fail to bind Pick bodies.",
    "id": "mol-159",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Subtomogram Averaging of In Situ Synaptic GABAA Receptors",
    "prompt": "Cryo-electron tomography paired with subtomogram averaging of intact vitrified synaptosomes demonstrated that native GABAA receptors in cerebellar inhibitory synapses:",
    "options": [
      "Are located inside the cell nucleus",
      "Are freely floating lipids without protein scaffolds",
      "Form hollow tubes that span the entire cytoplasm",
      "Are anchored in semi-periodic arrays directly connected to a sub-membrane gephyrin hexagonal lattice that determines postsynaptic receptor density and channel open probability"
    ],
    "answer": 3,
    "explain": "Subtomogram averaging of vitrified inhibitory synapses resolves pentameric GABAA receptors in their unperturbed membrane environment. Receptors extend extracellular domains across the 20 nm cleft and connect their intracellular M3-M4 loops directly to a sub-membranous planar gephyrin lattice that clusters exactly 50-100 receptors per inhibitory postsynaptic density.",
    "example": "Cryo-ET reconstructions demonstrated that pharmacological gephyrin disruption leads to immediate spatial dispersion of native GABAA receptor clusters.",
    "id": "mol-160",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Ribosome Profiling in Neurons",
    "prompt": "Which high-throughput molecular technique isolates mRNA fragments protected from RNase digestion to quantify active, in vivo translation at codon-level resolution in neural tissues?",
    "options": [
      "Ribosome profiling (Ribo-seq)",
      "Total RNA-seq",
      "Chromatin immunoprecipitation sequencing (ChIP-seq)",
      "Single-cell Assay for Transposase-Accessible Chromatin (scATAC-seq)"
    ],
    "answer": 0,
    "explain": "Ribosome profiling (Ribo-seq) utilizes ribonuclease treatment to digest unprotected mRNA, followed by deep sequencing of ribosome-protected footprints (RPFs) to reveal active protein synthesis at single-codon resolution.",
    "example": "Neurobiologists utilize Ribo-seq to detect local dendritic translation and upstream open reading frame (uORF) translation during synaptic plasticity.",
    "id": "mol-161",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Direct RNA Nanopore Sequencing",
    "prompt": "Direct sequencing of full-length native RNA molecules using protein nanopores provides which critical advantage over short-read cDNA sequencing when analyzing neural transcriptomes?",
    "options": [
      "Enzymatic amplification of low-abundance transcripts via thermostable DNA polymerases",
      "Direct identification of native RNA chemical modifications (e.g., m6A) and complex alternative splicing isoforms without reverse transcription bias",
      "Zero sequencing error rate and higher per-base accuracy than standard Illumina sequencing",
      "Elimination of the requirement for poly(A) tail selection or ribosomal RNA depletion"
    ],
    "answer": 1,
    "explain": "Direct RNA Nanopore sequencing threads native RNA molecules through nanopores, enabling direct detection of epitranscriptomic marks like N6-methyladenosine (m6A) and resolving complex alternative splicing across entire transcripts.",
    "example": "Mapping complex Neurexin and Dscam isoform diversity in the nervous system relies on long-read direct RNA nanopore sequencing.",
    "id": "mol-162",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Postsynaptic Density Phase Separation",
    "prompt": "At excitatory postsynaptic densities, what thermodynamic phenomenon drives the condensation of PSD-95 and SynGAP into functional sub-membranous protein compartments without a surrounding membrane?",
    "options": [
      "Cholesterol-dependent detergent-resistant lipid raft solubilization",
      "Covalent transglutaminase-mediated protein crosslinking",
      "Liquid-liquid phase separation (LLPS) driven by multivalent protein-protein interactions",
      "Ubiquitin-dependent selective proteasomal aggregation"
    ],
    "answer": 2,
    "explain": "Multivalent interactions between the PDZ domains of PSD-95 and the intrinsically disordered/multivalent regions of SynGAP trigger liquid-liquid phase separation (LLPS), forming condensed, micron-scale liquid droplets that organize the postsynaptic signaling machinery.",
    "example": "Disruption of the SynGAP/PSD-95 phase separation threshold by phosphorylation alters AMPA receptor clustering and causes cognitive impairment phenotypes.",
    "id": "mol-163",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "FMRP Translational Regulation",
    "prompt": "How does Fragile X Mental Retardation Protein (FMRP) primarily modulate the local dendritic translation of synaptic mRNAs such as Arc and Map1b?",
    "options": [
      "By catalyzing N6-methyladenosine (m6A) methylation to direct synaptic mRNAs toward degradation",
      "By promoting the endonucleolytic degradation of target mRNAs via the cytoplasmic exosome complex",
      "By directly phosphorylating eIF2alpha to induce global translational arrest at the initiation complex",
      "By binding target mRNAs through its KH and RGG domains and reversibly stalling ribosomal translocation during elongation"
    ],
    "answer": 3,
    "explain": "FMRP binds specific RNA structural motifs through its KH domains and RGG box, interacting with the 80S ribosome complex to stall peptide chain elongation until synaptic signals (e.g., mGluR stimulation) trigger de-repression.",
    "example": "Loss of FMRP in Fragile X syndrome leads to unconstrained, exaggerated basal synthesis of synaptic proteins downstream of group I mGluRs.",
    "id": "mol-164",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "C9orf72 Dipeptide Repeat Nucleocytoplasmic Block",
    "prompt": "In models of C9orf72-associated neurodegeneration, arginine-rich dipeptide repeat proteins (poly-GR and poly-PR) directly disrupt nucleocytoplasmic transport by interacting with which cellular structure?",
    "options": [
      "Phenylalanine-glycine (FG) repeat domains within the central channel of nuclear pore complexes (NPCs)",
      "The cytoplasmic tail of the beta-amyloid precursor protein",
      "Microtubule-associated motor protein kinesin light chain subunit 1",
      "The lipid bilayer core of the inner mitochondrial membrane"
    ],
    "answer": 0,
    "explain": "Arginine-rich dipeptide repeats (poly-GR/poly-PR) phase-separate and bind to the unstructured FG-repeat domains of nucleoporins, clogging the central aqueous channel of the nuclear pore complex and halting karyopherin-mediated nucleocytoplasmic transport.",
    "example": "In C9orf72 ALS/FTD iPSC-derived motor neurons, poly-PR accumulation triggers nuclear retention of RanGTP and mislocalization of nuclear proteins to the cytoplasm.",
    "id": "mol-165",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Optogenetic Phase Separation Modeling",
    "prompt": "What optogenetic tool design allows spatiotemporal induction of intrinsically disordered protein condensation to model pathological protein phase transitions in living neurons?",
    "options": [
      "Fusing channelrhodopsin-2 directly to the catalytic core of presenilin-1",
      "Fusing the protein intrinsically disordered region (IDR) to the light-sensitive Cryptochrome 2 (Cry2) photolyase homology domain",
      "Coupling halorhodopsin to a nuclear localization signal peptide",
      "Conjugating bacterial archaerhodopsin to an antibody against alpha-synuclein"
    ],
    "answer": 1,
    "explain": "The optoDroplet system fuses intrinsically disordered protein domains (e.g., from TDP-43 or FUS) to the blue light-sensitive Cry2 domain, which oligomerizes upon blue light illumination (488 nm) to drive liquid-liquid phase separation.",
    "example": "Researchers use opto-TDP43 to demonstrate that light-induced reversible liquid droplets transition into irreversible cytotoxic fibrils upon prolonged photo-stimulation.",
    "id": "mol-166",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Retrograde Axonal Injury Signaling",
    "prompt": "Following axonal injury, which molecular complex mediates the retrograde transport of injury-activated transcription factor signals from the damaged axon terminal back to the soma?",
    "options": [
      "Anterograde mitochondrial transport complexes containing Miro and Milton",
      "Kinesin-1 heavy chain dimers interacting directly with clathrin coats",
      "Importin-alpha/beta heterodimers coupled to dynein via the adaptor protein snapin or dynactin",
      "Actin filament treadmilling driven by the Arp2/3 nucleation complex"
    ],
    "answer": 2,
    "explain": "Axonal lesions locally activate kinases that phosphorylate signaling proteins exposing nuclear localization signals (NLS); importin-alpha/beta dimers bind these NLS motifs and hitchhike onto the retrograde dynein-dynactin motor complex back to the cell nucleus.",
    "example": "Phosphorylated ERK and STAT3 are transported in retrograde importin complexes after sciatic nerve crush to initiate pro-regenerative gene transcription.",
    "id": "mol-167",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Aquaporin-4 Astrocytic Polarization Scaffold",
    "prompt": "Polarized localization of the water channel Aquaporin-4 (AQP4) to astrocytic endfeet facing brain microvessels requires anchorage by which macromolecular protein complex?",
    "options": [
      "The clathrin-adaptor protein AP-2 endocytic complex",
      "The cadherin-catenin adherens junction complex",
      "The postsynaptic density-95 / Shank scaffolding lattice",
      "The dystrophin-associated protein complex (including alpha-syntrophin and dystroglycan)"
    ],
    "answer": 3,
    "explain": "AQP4 is anchored to the astrocytic endfoot membrane through interaction with alpha-syntrophin, which links via dystroglycan and dystrophin to the perivascular extracellular matrix (agrin/laminin). Loss of alpha-syntrophin abolishes AQP4 polarity.",
    "example": "In alpha-syntrophin knockout mice, AQP4 is mislocalized away from perivascular endfeet into the parenchymal neuropil, impairing glymphatic clearance.",
    "id": "mol-168",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Subcellular Spatial Transcriptomics",
    "prompt": "Subcellular spatial transcriptomics methods such as MERFISH and SeqFISH achieve multiplexed detection of hundreds of distinct mRNA molecules within dendrites and axons primarily by using what approach?",
    "options": [
      "Sequential rounds of single-molecule fluorescence in situ hybridization (smFISH) with combinatorial pseudocolored barcoding and optical clearing",
      "Next-generation Illumina sequencing of flow-sorted intact individual synaptosomes",
      "Microfluidic cDNA library generation from laser-capture microdissected dendritic segments",
      "PCR-based single-cell whole-transcriptome rolling circle amplification on fixed tissue slides"
    ],
    "answer": 0,
    "explain": "Multiplexed error-robust fluorescence in situ hybridization (MERFISH) and SeqFISH apply iterative rounds of fluorescent probe hybridization and cleavage using error-detecting barcodes to resolve thousands of unique mRNAs at nanometer optical resolution in dendrites.",
    "example": "MERFISH studies in the hippocampal neuropil have identified localized translation hubs containing specific synaptic plasticity transcripts adjacent to active spines.",
    "id": "mol-169",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "NMDA Receptor Cryo-EM Architecture",
    "prompt": "Cryo-electron microscopy (cryo-EM) studies have revealed that the GluN2B-selective negative allosteric modulator ifenprodil stabilizes the NMDA receptor in an inhibited conformation by binding to which structural domain?",
    "options": [
      "The ligand-binding domain (LBD) glycine-binding cleft of the GluN1 subunit",
      "The heterodimeric interface between the GluN1 and GluN2B amino-terminal domains (ATDs)",
      "The transmembrane pore vestibule adjacent to the magnesium-binding M2 loop",
      "The intracellular C-terminal domain PDZ-binding motif of the GluN2B subunit"
    ],
    "answer": 1,
    "explain": "High-resolution cryo-EM structures demonstrated that ifenprodil binds exclusively at the allosteric dimer interface formed between the GluN1 and GluN2B amino-terminal domains (ATDs), locking the ATDs in a closed conformation that prevents gating movements.",
    "example": "Structural elucidation of the GluN1/GluN2B ATD interface enabled the rational design of subtype-selective NMDA receptor antagonists with minimal psychotomimetic side effects.",
    "id": "mol-170",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Synaptic Cleft Proximity Biotinylation",
    "prompt": "In proximity-dependent biotinylation assays (e.g., TurboID or APEX2) mapped to the synaptic cleft, what is the primary biochemical mechanism that ensures nanometer-scale spatial labeling accuracy?",
    "options": [
      "Enzymatic ubiquitination of lysine residues specifically within alpha-helical trans-synaptic bridges",
      "Direct covalent crosslinking of the enzyme active site to neighboring membrane phospholipids",
      "Generation of an ultra-short-lived reactive biotin intermediate (e.g., biotin-AMP or biotin-phenoxyl radical) with a labeling radius under 20 nm",
      "Cleavage of extracellular loops of transmembrane proteins followed by covalent peptide tagging"
    ],
    "answer": 2,
    "explain": "Enzymes like TurboID convert biotin and ATP into reactive biotinoyl-5-AMP (or APEX2 generates biotin-phenoxyl radicals) which diffuse only 10-20 nm before being quenched by water, covalently labeling only immediately adjacent proteins within milliseconds.",
    "example": "Synaptic cleft-targeted TurboID in vivo revealed the endogenous interactome of Neuroligin-1 and identified novel trans-synaptic adhesion molecules.",
    "id": "mol-171",
    "mode": "molecular",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Single-Nucleus Multimodal 3D Epigenomics",
    "prompt": "Single-nucleus methyl-cytosine and 3D chromatin conformation sequencing (snm3C-seq) dissects neuronal epigenomic diversity primarily by simultaneously measuring which two modalities in individual nuclei?",
    "options": [
      "Cellular ribosomal RNA abundance and telomere length repeats",
      "Single-cell open chromatin accessibility (ATAC) and nascent RNA transcription (GRO-seq)",
      "Histone H3K27me3 occupancy and single-stranded DNA break hotspots",
      "Single-cell bisulfite-converted DNA methylation (mCH and mCG) and chromosomal contact frequency (Hi-C)"
    ],
    "answer": 3,
    "explain": "snm3C-seq couples in situ chromatin conformation capture (Hi-C) with single-nucleus methylome sequencing (snmC-seq), concurrently measuring 3D chromatin contacts (loops/TADs) and whole-genome CG/CH DNA methylation in the same single neuron.",
    "example": "Applying snm3C-seq across human frontal cortex revealed how cell-type-specific enhancer-promoter chromatin loops orchestrate gene expression profiles distinct to parvalbumin-positive interneurons.",
    "id": "mol-172",
    "mode": "molecular",
    "type": "choice"
  }
];
