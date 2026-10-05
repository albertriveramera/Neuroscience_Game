# scripts/bank_biochemistry.py
"""
Neurochemistry & Bioenergetics Question Bank (172 Curated Questions)
"""

QUESTIONS = [
  {
    "id": "bc-001",
    "mode": "biochemistry",
    "level": 1,
    "type": "choice",
    "topic": "Brain Energy Substrates",
    "prompt": "Under physiological postprandial conditions, what is the obligatory primary energetic fuel for the adult human brain?",
    "options": [
      "D-Glucose",
      "Free fatty acids",
      "Ketone bodies (acetoacetate and beta-hydroxybutyrate)",
      "Branched-chain amino acids"
    ],
    "answer": 0,
    "explain": "The adult brain accounts for ~20% of resting body energy consumption and relies almost exclusively on D-glucose under normal physiological conditions, consuming ~120 grams of glucose per day via aerobic glycolysis and oxidative phosphorylation.",
    "example": "During prolonged starvation or adherence to a strict ketogenic diet, the brain adapts to utilize ketone bodies for up to 60-70% of its energetic requirements."
  },
  {
    "id": "bc-002",
    "mode": "biochemistry",
    "level": 1,
    "type": "choice",
    "topic": "Catecholamine Biosynthesis",
    "prompt": "Which enzyme catalyzes the initial, rate-limiting step in the biosynthesis of dopamine, norepinephrine, and epinephrine?",
    "options": [
      "DOPA decarboxylase (Aromatic L-amino acid decarboxylase)",
      "Tyrosine hydroxylase (TH)",
      "Dopamine beta-hydroxylase (DBH)",
      "Phenylethanolamine N-methyltransferase (PNMT)"
    ],
    "answer": 1,
    "explain": "Tyrosine hydroxylase (TH) is the rate-limiting enzyme in catecholamine synthesis. It converts L-tyrosine to L-DOPA using molecular oxygen, iron (Fe2+), and the essential cofactor tetrahydrobiopterin (BH4).",
    "example": "Loss of tyrosine hydroxylase-positive neurons in the substantia nigra pars compacta is the defining neuropathological feature of Parkinson's disease."
  },
  {
    "id": "bc-003",
    "mode": "biochemistry",
    "level": 1,
    "type": "choice",
    "topic": "Glucose Transporters in Brain",
    "prompt": "High-affinity, insulin-independent uptake of glucose into mammalian neurons is mediated predominantly by which transporter?",
    "options": [
      "GLUT1 (45 kDa isoform)",
      "GLUT2",
      "GLUT3",
      "GLUT4"
    ],
    "answer": 2,
    "explain": "GLUT3 is the primary neuronal glucose transporter. It has a very low Km (~1.5 mM) and high Vmax, ensuring that neurons can extract glucose from interstitial fluid even when extracellular glucose concentrations fall.",
    "example": "GLUT1 is expressed on brain capillary endothelial cells (55 kDa) and astrocytes (45 kDa), whereas GLUT3 is enriched on neuronal processes and synapses."
  },
  {
    "id": "bc-004",
    "mode": "biochemistry",
    "level": 1,
    "type": "choice",
    "topic": "Cellular Antioxidant Defense",
    "prompt": "Superoxide radicals (O2•-) generated within the mitochondrial electron transport chain are dismutated to hydrogen peroxide by:",
    "options": [
      "Superoxide Dismutase (SOD1 in cytosol, SOD2 in mitochondrial matrix)",
      "Catalase",
      "Glutathione reductase",
      "Myeloperoxidase"
    ],
    "answer": 0,
    "explain": "Superoxide dismutases convert toxic superoxide anions into oxygen and hydrogen peroxide (H2O2). Manganese-dependent SOD2 (MnSOD) functions inside the mitochondrial matrix, while copper/zinc-dependent SOD1 (Cu/ZnSOD) resides in the cytosol and intermembrane space.",
    "example": "Dominant mutations in SOD1 were the first identified genetic cause of familial amyotrophic lateral sclerosis (ALS)."
  },
  {
    "id": "bc-005",
    "mode": "biochemistry",
    "level": 2,
    "type": "choice",
    "topic": "Astrocyte-Neuron Lactate Shuttle (ANLS)",
    "prompt": "According to the Astrocyte-Neuron Lactate Shuttle hypothesis (Pellerin & Magistretti), astrocytic glutamate uptake triggers:",
    "options": [
      "Astrocytic glycolysis and lactate export via MCT1/4, followed by neuronal lactate import via MCT2 to fuel oxidative phosphorylation",
      "Immediate conversion of glutamate to cholesterol for direct secretion",
      "Direct mitochondrial uncoupling in adjacent neurons",
      "Inhibition of all neuronal ATP synthesis"
    ],
    "answer": 0,
    "explain": "Glutamate uptake into astrocytes via Na+-coupled transporters (GLT-1) activates the Na+/K+-ATPase, stimulating astrocytic glycolysis. Lactate produced by astrocytes is exported via monocarboxylate transporters MCT1 and MCT4, imported into neurons via high-affinity MCT2, and oxidized by LDH-1 to pyruvate for the TCA cycle.",
    "example": "Knockdown of astrocytic MCT1 or neuronal MCT2 in the hippocampus impairs long-term memory formation in rats."
  },
  {
    "id": "bc-006",
    "mode": "biochemistry",
    "level": 2,
    "type": "choice",
    "topic": "Ubiquitin-Proteasome System (UPS)",
    "prompt": "Substrate proteins are marked for recognition and degradation by the 26S proteasome through polyubiquitin chains linked via which specific lysine residue?",
    "options": [
      "Lysine 6 (K6)",
      "Lysine 48 (K48)",
      "Lysine 63 (K63)",
      "Lysine 29 (K29)"
    ],
    "answer": 1,
    "explain": "Canonical targeting to the 26S proteasome requires polyubiquitin chains linked through Lys48 (K48) of ubiquitin. In contrast, Lys63 (K63)-linked polyubiquitination generally serves non-proteolytic regulatory roles, such as endocytic trafficking, DNA repair, and autophagic clearance.",
    "example": "Accumulation of K48-polyubiquitinated substrates is a hallmark of proteasome impairment in aging and neurodegenerative diseases."
  },
  {
    "id": "bc-007",
    "mode": "biochemistry",
    "level": 2,
    "type": "choice",
    "topic": "Autophagy Biomarkers",
    "prompt": "During macroautophagy, the conversion of cytosolic LC3-I to its autophagosome-membrane-bound form (LC3-II) occurs via covalent conjugation to:",
    "options": [
      "Phosphatidylcholine",
      "Phosphatidylethanolamine (PE)",
      "Phosphatidylserine",
      "Sphingomyelin"
    ],
    "answer": 1,
    "explain": "Following C-terminal cleavage by ATG4, cytosolic LC3-I is activated by ATG7 (E1-like), transferred to ATG3 (E2-like), and covalently conjugated to the lipid phosphatidylethanolamine (PE) on the nascent autophagosome isolation membrane, forming hydrophobic LC3-II.",
    "example": "Monitoring the ratio of LC3-II to LC3-I via Western blot is the gold standard assay for measuring autophagic vesicle formation."
  },
  {
    "id": "bc-008",
    "mode": "biochemistry",
    "level": 2,
    "type": "choice",
    "topic": "Mitochondrial Complex I Inhibitors",
    "prompt": "The neurotoxin 1-methyl-4-phenylpyridinium (MPP+), the active metabolite of MPTP, selectively damages dopaminergic neurons by inhibiting which component of the respiratory chain?",
    "options": [
      "Complex I (NADH:ubiquinone oxidoreductase)",
      "Complex II (Succinate dehydrogenase)",
      "Complex III (Cytochrome bc1 complex)",
      "Complex IV (Cytochrome c oxidase)"
    ],
    "answer": 0,
    "explain": "MPTP crosses the BBB and is oxidized by astrocytic MAO-B into toxic MPP+. MPP+ is concentrated into dopaminergic terminals via the dopamine transporter (DAT) and accumulates inside mitochondria, selectively inhibiting Complex I of the electron transport chain, causing ATP depletion and massive ROS generation.",
    "example": "Chronic administration of rotenone, another lipophilic Complex I inhibitor, similarly reproduces selective nigrostriatal degeneration and alpha-synuclein pathology in rodents."
  },
  {
    "id": "bc-009",
    "mode": "biochemistry",
    "level": 3,
    "type": "choice",
    "topic": "mTORC1 vs Autophagy Regulation",
    "prompt": "Under nutrient-rich conditions, mammalian target of rapamycin complex 1 (mTORC1) suppresses macroautophagy by directly phosphorylating:",
    "options": [
      "ULK1 (at Ser757) and ATG13",
      "Beclin-1 and VPS34",
      "LC3 and p62",
      "LAMP1 and Cathepsin D"
    ],
    "answer": 0,
    "explain": "Active mTORC1 phosphorylates the initiator kinase ULK1 at inhibitory Ser757 (in mice/humans), disrupting the interaction between ULK1 and AMPK and preventing autophagosome initiation. Nutrient deprivation or rapamycin inactivates mTORC1, allowing ULK1 dephosphorylation and activation of the autophagy cascade.",
    "example": "Pharmacological mTORC1 inhibition with rapamycin stimulates clearance of aggregate-prone proteins like mutant huntingtin and tau in animal models."
  },
  {
    "id": "bc-010",
    "mode": "biochemistry",
    "level": 3,
    "type": "choice",
    "topic": "PINK1-Parkin Mitophagy Pathway",
    "prompt": "Upon loss of mitochondrial membrane potential (Delta-Psi_m), the serine/threonine kinase PINK1 accumulates on the outer mitochondrial membrane (OMM) and initiates mitophagy by directly phosphorylating:",
    "options": [
      "Serine 65 of both Ubiquitin and Parkin's ubiquitin-like (Ubl) domain",
      "Threonine 286 on CaMKII",
      "Serine 473 on Akt",
      "Tyrosine 705 on STAT3"
    ],
    "answer": 0,
    "explain": "Loss of membrane potential arrests PINK1 import across the inner mitochondrial membrane, preventing its normal cleavage by PARL protease. Stabilized full-length PINK1 on the OMM phosphorylates Ser65 on ubiquitin. Phospho-Ser65-ubiquitin serves as the high-affinity receptor for Parkin, which is then phosphorylated by PINK1 at Ser65 of its Ubl domain, unlocking its full E3 ligase activity.",
    "example": "Parkin subsequently ubiquitinates outer membrane proteins (Mitofusins Mfn1/2, VDAC1), recruiting autophagy receptors (p62, optineurin) for lysosomal engulfment."
  },
  {
    "id": "bc-011",
    "mode": "biochemistry",
    "level": 3,
    "type": "choice",
    "topic": "Brain Cholesterol Homeostasis",
    "prompt": "Because circulating plasma lipoprotein complexes cannot cross the blood-brain barrier, brain cholesterol is synthesized de novo primarily by:",
    "options": [
      "Astrocytes, which package cholesterol into APOE-containing lipoprotein particles for secretion via ABCA1 transporters",
      "Microglia, which convert glucose directly into steroid hormones",
      "Ependymal cells, which pump cholesterol directly into CSF",
      "Oligodendrocytes, which synthesize cholesterol only during embryogenesis"
    ],
    "answer": 0,
    "explain": "The blood-brain barrier is impermeable to peripheral cholesterol. Astrocytes produce the majority of brain cholesterol via the de novo mevalonate/HMG-CoA reductase pathway. Cholesterol is loaded onto APOE particles via the ATP-binding cassette transporter ABCA1 and secreted into the interstitial fluid, where neurons take it up via LRP1 and LDLR to maintain synaptic membranes and myelin.",
    "example": "Genetic ablation of Abca1 in astrocytes reduces brain APOE lipidation, destabilizes APOE levels, and promotes amyloid plaque accumulation."
  },
  {
    "id": "bc-012",
    "mode": "biochemistry",
    "level": 3,
    "type": "choice",
    "topic": "Ferroptosis in Neurodegeneration",
    "prompt": "Ferroptotic non-apoptotic cell death in neurons is characterized by iron-dependent accumulation of lethal lipid reactive oxygen species and can be triggered by pharmacological inhibition of:",
    "options": [
      "Glutathione Peroxidase 4 (GPX4) or the cystine/glutamate antiporter System xc-",
      "Caspase-3 and Caspase-9",
      "PARP-1 and AIF",
      "Bcl-2 and Mcl-1"
    ],
    "answer": 0,
    "explain": "Ferroptosis is an iron-catalyzed form of regulated necrosis driven by the uncontrolled peroxidation of polyunsaturated fatty acid (PUFA)-containing membrane phospholipids. It is triggered when the glutathione-GPX4 axis is compromised (e.g. by RSL3 directly inhibiting GPX4, or erastin inhibiting System xc-). It is halted by lipophilic radical-trapping antioxidants like ferrostatin-1 or iron chelators like deferoxamine.",
    "example": "Conditional genetic deletion of Gpx4 in forebrain neurons triggers massive hippocampal neurodegeneration that is completely prevented by liproxstatin-1."
  },
  {
    "id": "bc-013",
    "mode": "biochemistry",
    "level": 4,
    "type": "choice",
    "topic": "TFEB & Lysosomal Biogenesis",
    "prompt": "Transcription Factor EB (TFEB) controls the CLEAR (Coordinated Lysosomal Expression and Regulation) gene network. Its nuclear translocation is triggered by:",
    "options": [
      "Dephosphorylation of Ser142 and Ser211 following mTORC1 inactivation and Calcineurin activation via lysosomal Ca2+ release",
      "Constitutive hyperphosphorylation by glycogen synthase kinase 3 beta (GSK3β)",
      "Direct covalent binding to monomeric beta-amyloid in the cytoplasm",
      "Irreversible cleavage by Caspase-1 inside the nucleus"
    ],
    "answer": 0,
    "explain": "Under nutrient-replete conditions, mTORC1 phosphorylates TFEB at Ser142 and Ser211, creating binding sites for 14-3-3 chaperones that sequester TFEB in the cytoplasm. During starvation or lysosomal stress, lysosomal Ca2+ is released via TRPML1, activating the phosphatase calcineurin. Calcineurin dephosphorylates TFEB, freeing it to translocate to the nucleus where it drives transcription of lysosomal hydrolases and autophagy genes.",
    "example": "Overexpression of TFEB in mouse models of Alzheimer's and tauopathy promotes lysosomal degradation of pathological protein aggregates."
  },
  {
    "id": "bc-014",
    "mode": "biochemistry",
    "level": 4,
    "type": "choice",
    "topic": "Microglial Metabolic Reprogramming",
    "prompt": "Upon acute pro-inflammatory stimulation (e.g. by LPS or Aβ oligomers), microglia undergo a metabolic switch reminiscent of the Warburg effect, shifting from:",
    "options": [
      "Mitochondrial oxidative phosphorylation to aerobic glycolysis driven by HIF-1alpha stabilization",
      "Aerobic glycolysis to beta-oxidation of long-chain fatty acids",
      "Ketone body oxidation to pure gluconeogenesis",
      "The pentose phosphate pathway to complete metabolic dormancy"
    ],
    "answer": 0,
    "explain": "Pro-inflammatory activation induces metabolic reprogramming in microglia: oxidative phosphorylation slows down and mitochondrial ROS increases, while aerobic glycolysis is robustly upregulated via stabilization of Hypoxia-Inducible Factor 1-alpha (HIF-1α) and PKM2 dimeric activation, rapidly generating ATP and biosynthetic intermediates required for cytokine secretion.",
    "example": "In chronically aged or AD brains, microglia become metabolically exhausted, exhibiting impaired glycolysis and defective mitochondrial respiration."
  },
  {
    "id": "bc-015",
    "mode": "biochemistry",
    "level": 4,
    "type": "choice",
    "topic": "Synaptic Mitochondrial Anchoring",
    "prompt": "In axons, stationary positioning of mitochondria at presynaptic boutons to supply local ATP and buffer calcium is mediated by docking to the axonal cytoskeleton via:",
    "options": [
      "Syntaphilin (SNPH)",
      "Miro1 (RHOT1)",
      "TRAK2",
      "Kinesin-1 heavy chain"
    ],
    "answer": 0,
    "explain": "Syntaphilin (SNPH) acts as an axon-specific molecular 'engine brake' for mitochondria. By binding both outer mitochondrial membrane receptors and axonal microtubules, SNPH immobilizes mitochondria at active presynaptic sites. High presynaptic Ca2+ can inactivate Miro motors and recruit SNPH, arresting mitochondrial transport at sites of elevated metabolic demand.",
    "example": "Syntaphilin knockout mice show 80% reduction in stationary axonal mitochondria, resulting in rapid synaptic depression during high-frequency firing."
  },
  {
    "id": "bc-016",
    "mode": "biochemistry",
    "level": 4,
    "type": "choice",
    "topic": "Lipid Rafts and Secretase Cleavage",
    "prompt": "BACE1-mediated cleavage of APP is strongly favored within cholesterol- and sphingolipid-rich lipid rafts because:",
    "options": [
      "BACE1 is post-translationally palmitoylated and partitions into ordered raft microdomains alongside clustered APP",
      "Lipid rafts lack all functional membrane proteins",
      "Alpha-secretase ADAM10 is exclusively active inside lipid rafts",
      "Lipid rafts completely repel presenilin-1"
    ],
    "answer": 0,
    "explain": "Lipid rafts are liquid-ordered membrane microdomains enriched in cholesterol, sphingomyelin, and GM1 ganglioside. BACE1 undergoes palmitoylation at four C-terminal cysteine residues, which targets BACE1 into lipid rafts where it co-localizes with and cleaves APP. In contrast, the non-amyloidogenic alpha-secretase ADAM10 resides predominantly in non-raft disordered membranes.",
    "example": "Depleting membrane cholesterol with statins or methyl-beta-cyclodextrin disrupts lipid rafts, shifting APP processing toward neuroprotective alpha-cleavage."
  },
  {
    "id": "bc-017",
    "mode": "biochemistry",
    "level": 5,
    "type": "choice",
    "topic": "Liquid-Liquid Phase Separation (LLPS)",
    "prompt": "Liquid-liquid phase separation (LLPS) of RNA-binding proteins like TDP-43 and FUS is driven by multivalent interactions within their intrinsically disordered regions (IDRs). In neurodegeneration, pathological fibrillization is accelerated when:",
    "options": [
      "Reversible liquid condensates undergo an aberrant liquid-to-solid phase transition into irreversible cross-beta amyloid fibrils promoted by disease mutations, aging, or persistent cellular stress",
      "Condensates dissolve completely into monomeric solutions at low pH",
      "Proteins are completely degraded by mitochondrial Lon protease",
      "The nuclear envelope dissolves during prophase"
    ],
    "answer": 0,
    "explain": "TDP-43 and FUS condense reversibly into dynamic liquid droplets (such as stress granules and nuclear paraspeckles) via weak multivalent hydrophobic, cation-pi, and dipole interactions in their IDRs. Pathogenic ALS mutations (e.g. TDP-43 A315T, FUS R521C), prolonged oxidative stress, or age-related chaperonopathy alter condensate viscosity, promoting an irreversible liquid-to-solid phase transition into pathological fibrillar aggregates.",
    "example": "Fluorescence Recovery After Photobleaching (FRAP) of TDP-43 granules reveals rapid recovery in young cells that converts to complete lack of mobile recovery (solidification) in ALS models."
  },
  {
    "id": "bc-018",
    "mode": "biochemistry",
    "level": 5,
    "type": "choice",
    "topic": "cGAS-STING Activation by Leaked mtDNA",
    "prompt": "In aged and neurodegenerative microglia, failed mitophagy leads to cytosolic escape of damaged mitochondrial DNA (mtDNA), which binds to and activates which innate immune sensor?",
    "options": [
      "cGAS (cyclic GMP-AMP synthase), driving 2'3'-cGAMP synthesis and STING activation on the ER to induce Type I interferons",
      "NLRP3 inflammasome directly without adaptor recruitment",
      "Toll-like receptor 4 (TLR4) on the outer plasma membrane",
      "Dicer enzyme in the cytoplasm"
    ],
    "answer": 0,
    "explain": "When damaged mitochondria rupture or cannot be cleared via mitophagy, double-stranded mtDNA leaks into the cytosol. Cytosolic mtDNA is recognized by cGAS, which catalyzes synthesis of the cyclic dinucleotide 2'3'-cGAMP. cGAMP binds STING on the endoplasmic reticulum, triggering TBK1 phosphorylation, IRF3 nuclear translocation, and robust transcription of Type I interferons (IFN-beta) and pro-inflammatory senescence genes.",
    "example": "Genetic ablation or pharmacological inhibition of STING in aged mice prevents chronic neuroinflammation and rescues cognitive decline."
  },
  {
    "id": "bc-019",
    "mode": "biochemistry",
    "level": 2,
    "type": "choice",
    "topic": "Monoamine Oxidase Subtypes",
    "prompt": "Monoamine Oxidase A (MAO-A) and Monoamine Oxidase B (MAO-B) degrade biogenic amines in the brain. Which statement accurately describes their primary substrate preferences and localization?",
    "options": [
      "MAO-A preferentially metabolizes serotonin (5-HT) and norepinephrine, whereas MAO-B preferentially metabolizes dopamine and phenylethylamine and is elevated in reactive astrocytes",
      "MAO-A metabolizes only histamine, while MAO-B metabolizes only GABA",
      "MAO-B is found exclusively inside the cell nucleus, while MAO-A is strictly extracellular",
      "Both enzymes are identical in substrate specificity and inhibited equally by selegiline"
    ],
    "answer": 0,
    "explain": "MAO-A has highest affinity for serotonin (5-HT) and norepinephrine, and is selectively inhibited by clorgyline. MAO-B metabolizes benzylamine, phenylethylamine, and dopamine, is selectively inhibited by selegiline/rasagiline, and increases substantially in reactive astrocytes in aging and Alzheimer's disease.",
    "example": "MAO-B inhibitors (e.g. rasagiline) are used clinically in Parkinson's disease to prolong the synaptic lifetime of levodopa-derived dopamine."
  },
  {
    "id": "bc-020",
    "mode": "biochemistry",
    "level": 3,
    "type": "choice",
    "topic": "Nitric Oxide - cGMP Cascade",
    "prompt": "In the central nervous system, retrograde synaptic signaling and vascular tone regulation by nitric oxide (NO) is mediated by NO binding to the heme moiety of which intracellular receptor?",
    "options": [
      "Soluble guanylyl cyclase (sGC), stimulating production of cyclic GMP (cGMP) and activation of Protein Kinase G (PKG)",
      "Adenylate cyclase, producing cAMP",
      "Phospholipase C-gamma",
      "Inositol trisphosphate receptor (IP3R)"
    ],
    "answer": 0,
    "explain": "Neuronal nitric oxide synthase (nNOS) is tethered to the postsynaptic density via PSD-95 and activated by NMDAR calcium influx. Diffusible NO gas binds the prosthetic heme group of soluble guanylyl cyclase (sGC) in presynaptic terminals and vascular smooth muscle, stimulating conversion of GTP to cGMP and activating Protein Kinase G (PKG).",
    "example": "NO-cGMP signaling mediates neurovascular coupling (functional hyperemia), dilating parenchymal arterioles during focal neural activity."
  },
  {
    "id": "bc-021",
    "mode": "biochemistry",
    "level": 4,
    "type": "choice",
    "topic": "Mitochondrial Dynamics: Fusion and Fission",
    "prompt": "Mitochondrial fission in neurons is executed when the cytosolic GTPase Dynamin-Related Protein 1 (Drp1) is recruited to the outer mitochondrial membrane and activated by phosphorylation at:",
    "options": [
      "Serine 616 (activating fission), whereas phosphorylation at Serine 637 by PKA inhibits fission",
      "Tyrosine 216 strictly by c-Src",
      "Threonine 286 by CaMKII",
      "Serine 129 by polo-like kinase 2"
    ],
    "answer": 0,
    "explain": "Drp1 is the master mediator of mitochondrial division. CDK1/cyclin B or CaMKII phosphorylates Drp1 at Ser616, recruiting Drp1 to constrict mitochondrial constriction sites defined by the endoplasmic reticulum. Conversely, PKA-mediated phosphorylation at Ser637 retains Drp1 in the cytosol, suppressing fission and promoting elongated, fused mitochondrial networks.",
    "example": "Excessive Drp1 Ser616 phosphorylation and mitochondrial fragmentation occur downstream of Aβ oligomer exposure and stroke in cortical neurons."
  },
  {
    "id": "bc-022",
    "mode": "biochemistry",
    "level": 4,
    "type": "choice",
    "topic": "Pentose Phosphate Pathway & Neuronal Redox",
    "prompt": "Astrocytes vigorously maintain the Pentose Phosphate Pathway (PPP) compared to neurons because the rate-limiting enzyme Glucose-6-Phosphate Dehydrogenase (G6PD) produces:",
    "options": [
      "NADPH, which is required to regenerate reduced glutathione (GSH) to defend against reactive oxygen species",
      "Large amounts of ATP without consuming oxygen",
      "Lactate directly for neuronal import",
      "Cholesterol esters for myelin formation"
    ],
    "answer": 0,
    "explain": "The PPP shunts glucose-6-phosphate to generate ribose-5-phosphate and NADPH. NADPH is the essential reducing currency utilized by glutathione reductase to regenerate reduced glutathione (GSH) from oxidized GSSG. Neurons degrade the rate-limiting glycolytic regulator PFKFB3, maintaining low PPP fluxes and relying on astrocytic glutathione precursors (cysteine/cys-gly) for antioxidant defense.",
    "example": "Astrocytes release glutathione into the extracellular space, where it is cleaved by gamma-glutamyl transpeptidase into precursors taken up by neurons."
  },
  {
    "id": "bc-023",
    "mode": "biochemistry",
    "level": 1,
    "type": "choice",
    "topic": "Glutamate-Glutamine Cycle",
    "prompt": "In the glutamate-glutamine cycle, synaptically released glutamate taken up by astrocytes is detoxified and converted into non-excitotoxic glutamine by which astrocyte-specific enzyme?",
    "options": [
      "Glutamine synthetase (GS)",
      "Phosphate-activated glutaminase (PAG)",
      "Glutamate dehydrogenase",
      "GABA transaminase"
    ],
    "answer": 0,
    "explain": "Astrocytes express high levels of glutamine synthetase (GS), an ATP-dependent enzyme that converts glutamate and ammonia into neutral glutamine. Glutamine is exported to the extracellular space, taken up by neurons, and converted back to glutamate by phosphate-activated glutaminase (PAG) inside synaptic mitochondria.",
    "example": "Inhibition of astrocytic glutamine synthetase with methionine sulfoximine (MSO) depletes neuronal glutamate reserves and causes epileptic seizures."
  },
  {
    "id": "bc-024",
    "mode": "biochemistry",
    "level": 2,
    "type": "choice",
    "topic": "Brain Glycogen Compartmentalization",
    "prompt": "In the adult mammalian central nervous system, glycogen granules are almost exclusively stored within which cell type?",
    "options": [
      "Astrocytes",
      "Cortical pyramidal neurons",
      "Microglia",
      "Choroid plexus epithelial cells"
    ],
    "answer": 0,
    "explain": "Under normal conditions, mature neurons repress glycogen synthase via constitutive degradation by malin-laforin complexes. Astrocytes represent the exclusive reservoir of brain glycogen, metabolizing glycogen into lactate via glycogenolysis to provide emergency fuel to neurons during intense activity or hypoglycemia.",
    "example": "Defective glycogen clearance in neurons causes Lafora disease, a fatal progressive myoclonic epilepsy marked by toxic polyglucosan bodies."
  },
  {
    "id": "bc-025",
    "mode": "biochemistry",
    "level": 3,
    "type": "choice",
    "topic": "Sphingosine-1-Phosphate (S1P) in Neuroimmunology",
    "prompt": "The FDA-approved multiple sclerosis therapeutic Fingolimod (FTY720) modulates neuroinflammation by binding to which receptor family?",
    "options": [
      "Sphingosine-1-phosphate (S1P) G-protein coupled receptors, causing receptor internalisation and sequestering auto-reactive lymphocytes in lymph nodes",
      "Dopamine D1 receptors in the basal ganglia",
      "Toll-like receptor 4 on microglia",
      "NMDA receptors in the hippocampus"
    ],
    "answer": 0,
    "explain": "Fingolimod is phosphorylated in vivo into Fingolimod-phosphate, an analog of sphingosine-1-phosphate (S1P). It acts as a functional antagonist of S1P1 receptors on T- and B-lymphocytes, inducing receptor internalization and preventing lymphocyte egress from secondary lymphoid organs into the systemic circulation and central nervous system.",
    "example": "Fingolimod reduces relapse rates and MRI lesion accumulation in relapsing-remitting multiple sclerosis."
  },
  {
    "id": "bc-026",
    "mode": "biochemistry",
    "level": 4,
    "type": "choice",
    "topic": "Calpain Activation in Excitotoxicity",
    "prompt": "During excitotoxic glutamate receptor stimulation, massive calcium influx hyperactivates the neutral cysteine protease calpain, producing a diagnostic 145/150 kDa breakdown product of which cytoskeletal protein?",
    "options": [
      "Alpha-II spectrin (fodrin)",
      "Histone H3",
      "Beta-catenin",
      "Glial fibrillary acidic protein (GFAP)"
    ],
    "answer": 0,
    "explain": "Calpain hyperactivation cleaves alpha-II spectrin into characteristic 150 kDa and 145 kDa spectrin breakdown products (SBDPs). In contrast, caspase-3 cleaves spectrin to generate a distinct 120 kDa fragment (SBDP120), allowing biochemical differentiation between calpain-mediated necrotic excitotoxicity and caspase-mediated apoptosis.",
    "example": "Western blotting for SBDP145/150 serves as a standard biomarker of calpain activation in ischemic stroke and traumatic brain injury."
  },
  {
    "level": 1,
    "topic": "Catecholamine Rate-Limiting Enzyme",
    "prompt": "What is the initial and rate-limiting enzyme in the biosynthesis of catecholamines (dopamine, norepinephrine, and epinephrine)?",
    "options": [
      "Tyrosine hydroxylase (TH)",
      "Aromatic L-amino acid decarboxylase (AADC)",
      "Dopamine beta-hydroxylase (DBH)",
      "Phenylethanolamine N-methyltransferase (PNMT)"
    ],
    "answer": 0,
    "explain": "Tyrosine hydroxylase (TH) catalyzes the conversion of L-tyrosine to L-DOPA. It is the rate-limiting step in catecholamine synthesis and requires tetrahydrobiopterin (BH4), molecular oxygen, and ferrous iron (Fe2+) as cofactors.",
    "example": "Phosphorylation of TH at Ser40 by protein kinase A relieves end-product feedback inhibition, increasing dopamine synthesis during high neural demand.",
    "id": "bc-027",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Cofactor for Tyrosine Hydroxylase",
    "prompt": "Which essential pterin cofactor is required by both tyrosine hydroxylase and tryptophan hydroxylase for aromatic amino acid hydroxylation?",
    "options": [
      "Tetrahydrobiopterin (BH4)",
      "Pyridoxal 5'-phosphate (PLP)",
      "Flavin adenine dinucleotide (FAD)",
      "Nicotinamide adenine dinucleotide (NADH)"
    ],
    "answer": 0,
    "explain": "Tetrahydrobiopterin (BH4) serves as the obligate electron donor for aromatic amino acid hydroxylases (TH, TPH1, TPH2, and PAH). Deficiencies in BH4 recycling enzymes (e.g., DHPR) cause severe neurotransmitter deficiency disorders.",
    "example": "Mutations in GTP cyclohydrolase 1 (GCH1), the rate-limiting enzyme for BH4 synthesis, cause DOPA-responsive dystonia (Segawa syndrome).",
    "id": "bc-028",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Serotonin Synthesis Rate-Limiting Step",
    "prompt": "Which enzyme catalyzes the primary rate-limiting step in the central synthesis of serotonin (5-hydroxytryptamine)?",
    "options": [
      "Tryptophan hydroxylase 2 (TPH2)",
      "Aromatic L-amino acid decarboxylase (AADC)",
      "Monoamine oxidase A (MAO-A)",
      "Serotonin N-acetyltransferase (AANAT)"
    ],
    "answer": 0,
    "explain": "Tryptophan hydroxylase 2 (TPH2) is the neuron-specific isoform of tryptophan hydroxylase expressed in raphe nuclei that converts L-tryptophan into 5-hydroxytryptophan (5-HTP), the committed rate-limiting step in brain serotonin synthesis.",
    "example": "TPH2 knockout mice exhibit profound depletion of brain serotonin (>95% reduction) with intact peripheral gut serotonin, which is produced by TPH1.",
    "id": "bc-029",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "GABA Biosynthesis and Cofactor",
    "prompt": "Gamma-aminobutyric acid (GABA) is synthesized from L-glutamate by glutamate decarboxylase (GAD). Which vitamin B6 derivative acts as its essential cofactor?",
    "options": [
      "Pyridoxal 5'-phosphate (PLP)",
      "Thiamine pyrophosphate (TPP)",
      "Tetrahydrofolate (THF)",
      "Biotin"
    ],
    "answer": 0,
    "explain": "Glutamate decarboxylase (GAD65 and GAD67) requires pyridoxal 5'-phosphate (PLP, the active form of vitamin B6) to catalyze the alpha-decarboxylation of L-glutamate into GABA. PLP deficiency or inhibition induces intractable epileptic seizures.",
    "example": "Infants with pyridoxine-dependent epilepsy develop status epilepticus that is rapidly terminated upon intravenous administration of pyridoxal 5'-phosphate.",
    "id": "bc-030",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Acetylcholine Synthesis by ChAT",
    "prompt": "Choline acetyltransferase (ChAT) synthesizes acetylcholine in cholinergic nerve terminals by transferring an acetyl group from which donor molecule to choline?",
    "options": [
      "Acetyl-CoA",
      "Acetoacetate",
      "Citrate",
      "Malonyl-CoA"
    ],
    "answer": 0,
    "explain": "ChAT transfers the acetyl moiety from mitochondrial-derived acetyl-CoA to choline imported from the extracellular fluid by the high-affinity choline transporter (CHT1).",
    "example": "ChAT expression is the primary biochemical diagnostic marker used to identify cholinergic projection neurons in the basal forebrain and striatal interneurons.",
    "id": "bc-031",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Acetylcholinesterase Catalytic Action",
    "prompt": "Acetylcholinesterase (AChE) terminates cholinergic transmission with extreme catalytic speed by hydrolyzing acetylcholine into:",
    "options": [
      "Choline and acetate",
      "Ethanolamine and acetyl-CoA",
      "Glycine and formic acid",
      "Betaine and carbon dioxide"
    ],
    "answer": 0,
    "explain": "AChE contains a catalytic triad (Ser-His-Glu) in a deep aromatic gorge that hydrolyzes ACh into acetate and free choline, achieving one of the highest turnover rates known in enzymology (~25,000 molecules of ACh per second per active site).",
    "example": "Organophosphate nerve agents covalently phosphonylate the active-site serine of AChE, causing toxic accumulation of acetylcholine at neuromuscular junctions.",
    "id": "bc-032",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Glutamate-Glutamine Cycle in Astrocytes",
    "prompt": "In the glutamate-glutamine cycle, astrocytes convert cleared synaptic glutamate into non-neurotoxic glutamine using which ATP-dependent enzyme?",
    "options": [
      "Glutamine synthetase (GS)",
      "Phosphate-activated glutaminase (PAG)",
      "Glutamate dehydrogenase (GDH)",
      "Aspartate aminotransferase (AST)"
    ],
    "answer": 0,
    "explain": "Glutamine synthetase (GS) is localized almost exclusively to astrocytes in the brain, where it uses ATP to amidate glutamate into neutral glutamine. Glutamine is then exported safely to neurons without activating postsynaptic receptors.",
    "example": "Inhibition of astrocytic glutamine synthetase with methionine sulfoximine (MSO) rapidly depletes neuronal glutamate pools and causes amnesia and seizures.",
    "id": "bc-033",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Neuronal Regeneration of Glutamate",
    "prompt": "Following export from astrocytes into neurons, glutamine is converted back into neurotransmitter glutamate primarily by which enzyme located in neuronal mitochondria?",
    "options": [
      "Phosphate-activated glutaminase (PAG / GLS1)",
      "Glutamine synthetase",
      "Alanine aminotransferase",
      "Carbamoyl phosphate synthetase"
    ],
    "answer": 0,
    "explain": "Phosphate-activated glutaminase (GLS1 / PAG), localized to the mitochondrial inner membrane of neurons, hydrolyzes glutamine into glutamate and ammonia, replenishing the vesicular glutamate pool.",
    "example": "Glutaminase-1 (Gls1) heterozygous mice show reduced synaptic glutamate release and altered cortical oscillations during sensory stimulation.",
    "id": "bc-034",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Norepinephrine Synthesis Location",
    "prompt": "Where in the adrenergic/noradrenergic neuron does the conversion of dopamine to norepinephrine occur?",
    "options": [
      "Inside synaptic vesicles (catalyzed by vesicular dopamine beta-hydroxylase)",
      "In the cytosol (catalyzed by soluble tyrosine hydroxylase)",
      "Inside the mitochondrial matrix",
      "At the outer plasma membrane surface"
    ],
    "answer": 0,
    "explain": "Dopamine beta-hydroxylase (DBH) is a copper-containing enzyme located inside the lumen of synaptic storage vesicles. Cytoplasmic dopamine must be transported into the vesicle via VMAT2 before DBH can hydroxylate it into norepinephrine.",
    "example": "In dopamine beta-hydroxylase deficiency, patients completely lack norepinephrine and epinephrine, exhibiting severe orthostatic hypotension and eyelid ptosis.",
    "id": "bc-035",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Epinephrine Synthesis Enzyme PNMT",
    "prompt": "The conversion of norepinephrine to epinephrine requires which enzyme that is localized in the cytoplasm and stimulated by glucocorticoids?",
    "options": [
      "Phenylethanolamine N-methyltransferase (PNMT)",
      "Catechol-O-methyltransferase (COMT)",
      "Dopamine beta-hydroxylase (DBH)",
      "Monoamine oxidase A (MAO-A)"
    ],
    "answer": 0,
    "explain": "PNMT transfers a methyl group from S-adenosylmethionine (SAM) to the amino group of norepinephrine, forming epinephrine. Because PNMT is cytoplasmic, norepinephrine must exit vesicles into the cytosol for methylation before repackaging.",
    "example": "High concentrations of cortisol delivered via intra-adrenal portal circulation strongly induce PNMT transcription in chromaffin cells of the adrenal medulla.",
    "id": "bc-036",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Monoamine Oxidase Isoform Specificity",
    "prompt": "Monoamine oxidase A (MAO-A) exhibits highest substrate selectivity and affinity for which pair of monoamines?",
    "options": [
      "Serotonin and norepinephrine",
      "Histamine and GABA",
      "Melatonin and acetylcholine",
      "Glutamate and aspartate"
    ],
    "answer": 0,
    "explain": "MAO-A preferentially deaminates serotonin (5-HT) and norepinephrine, and is selectively inhibited by moclobemide and clorgyline. In contrast, MAO-B preferentially deaminates benzylamine and phenylethylamine.",
    "example": "Selective reversible inhibitors of MAO-A (RIMAs) act as antidepressants without causing the severe tyramine hypertensive 'cheese effect' seen with irreversible non-selective MAOIs.",
    "id": "bc-037",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "COMT Metabolic Reaction",
    "prompt": "Catechol-O-methyltransferase (COMT) deactivates catecholamines by transferring a methyl group from S-adenosylmethionine (SAM) to which position?",
    "options": [
      "The 3-hydroxyl (meta-OH) group of the catechol benzene ring",
      "The primary amino group of the aliphatic side chain",
      "The beta-hydroxyl group of norepinephrine",
      "The carboxyl group of L-DOPA"
    ],
    "answer": 0,
    "explain": "COMT catalyzes the transfer of a methyl group from S-adenosyl-L-methionine (SAM) to the 3-hydroxyl (meta) position of catechol compounds, converting dopamine to 3-methoxytyramine and norepinephrine to normetanephrine.",
    "example": "In the prefrontal cortex, where DAT expression is sparse, COMT activity is the predominant mechanism clearing synaptic dopamine.",
    "id": "bc-038",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Brain Energy Budget Allocation",
    "prompt": "Approximately what percentage of the resting adult human body's glucose consumption is consumed by the brain, despite representing only ~2% of total body mass?",
    "options": [
      "20%",
      "5%",
      "50%",
      "85%"
    ],
    "answer": 0,
    "explain": "The human brain consumes ~20% of basal whole-body glucose and 20% of resting oxygen consumption. Over 50-70% of this energy expenditure is directly utilized by Na+/K+-ATPase pumps to restore ionic gradients disrupted by action potentials and postsynaptic currents.",
    "example": "FDG-PET imaging takes advantage of the brain's disproportionate glucose consumption to map regional metabolic activity in health and disease.",
    "id": "bc-039",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Hexokinase 1 Affinity in Neurons",
    "prompt": "Neuronal hexokinase 1 (HK1) has an exceptionally low Michaelis constant (Km < 0.1 mM) for glucose, ensuring that:",
    "options": [
      "Neuronal glucose phosphorylation proceeds at near-maximal velocity even under profound systemic hypoglycemia",
      "Neurons excrete free glucose into the cerebrospinal fluid",
      "Glycogen synthesis is prioritized over glycolysis in active axons",
      "Glucose is transported backwards into astrocytic endfeet"
    ],
    "answer": 0,
    "explain": "HK1 has a Km for glucose well below 0.1 mM, whereas physiological brain interstitial glucose concentrations range from 1 to 2.5 mM. Consequently, HK1 is essentially saturated and phosphorylates glucose at Vmax under all non-lethal physiological conditions.",
    "example": "HK1 binds directly to voltage-dependent anion channels (VDAC) on the mitochondrial outer membrane, granting it preferential access to newly synthesized mitochondrial ATP.",
    "id": "bc-040",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Glucose Transporter Isoforms in Brain",
    "prompt": "Which high-affinity glucose transporter is predominantly expressed on neuronal plasma membranes to ensure efficient glucose uptake into neurons?",
    "options": [
      "GLUT3 (SLC2A3)",
      "GLUT4 (SLC2A4)",
      "GLUT2 (SLC2A2)",
      "SGLT1 (SLC5A1)"
    ],
    "answer": 0,
    "explain": "GLUT3 (SLC2A3) is the primary neuronal glucose transporter. It has a high substrate affinity (Km ~ 1.5 mM) and higher maximum velocity than GLUT1, allowing neurons to effectively extract glucose from the neuropil even when extracellular levels fall.",
    "example": "In GLUT1 deficiency syndrome, GLUT1 is mutated in brain capillary endothelial cells, but neuronal GLUT3 remains normal; patients suffer severe neuroglycopenia due to defective transport across the blood-brain barrier.",
    "id": "bc-041",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "GABA Transaminase Catabolism",
    "prompt": "GABA transaminase (GABA-T) degrades GABA by converting it into which tricarboxylic acid (TCA) cycle intermediate precursor?",
    "options": [
      "Succinate semialdehyde (which is oxidized to succinate by SSADH)",
      "Oxaloacetate",
      "Citrate",
      "Fumarate"
    ],
    "answer": 0,
    "explain": "GABA-T transfers the amino group of GABA to alpha-ketoglutarate, producing succinate semialdehyde (SSA) and regenerating glutamate. SSA is subsequently oxidized to succinate by succinic semialdehyde dehydrogenase (SSADH), entering the TCA cycle.",
    "example": "Vigabatrin is an irreversible 'suicide' inhibitor of GABA transaminase that dramatically elevates brain GABA levels, used clinically for infantile spasms.",
    "id": "bc-042",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Histamine Synthesis in Tuberomammillary Nucleus",
    "prompt": "Histaminergic neurons that regulate wakefulness in the tuberomammillary nucleus synthesize histamine from L-histidine via which enzyme?",
    "options": [
      "Histidine decarboxylase (HDC)",
      "Histamine N-methyltransferase (HNMT)",
      "Diamine oxidase (DAO)",
      "Aromatic amino acid decarboxylase (AADC)"
    ],
    "answer": 0,
    "explain": "Histidine decarboxylase (HDC) is a pyridoxal 5'-phosphate-dependent enzyme that decarboxylates L-histidine into histamine. Central histaminergic neurons are located exclusively in the tuberomammillary nucleus of the posterior hypothalamus.",
    "example": "HDC knockout mice show profound deficits in maintaining wakefulness upon lights-off and during novel environmental exploration.",
    "id": "bc-043",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Histamine Degradation in the Mammalian Brain",
    "prompt": "Unlike peripheral tissues that utilize diamine oxidase, what is the predominant pathway for histamine degradation in the mammalian central nervous system?",
    "options": [
      "Ring methylation by Histamine N-methyltransferase (HNMT) to tele-methylhistamine",
      "Direct oxidation by diamine oxidase into imidazole acetic acid",
      "Conjugation to glucuronic acid in astrocytic lysosomes",
      "Cleavage into ammonia and glutamate by mitochondrial transaminases"
    ],
    "answer": 0,
    "explain": "In the brain, diamine oxidase (DAO) is virtually absent. Central histamine clearance relies almost exclusively on Histamine N-methyltransferase (HNMT), which transfers a methyl group from SAM to histamine, producing tele-methylhistamine.",
    "example": "Pharmacological inhibition of brain HNMT prolongs wakefulness and enhances vigilance in animal models of hypersomnia.",
    "id": "bc-044",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Glycine Synthesis from Serine",
    "prompt": "The primary pathway for glycine biosynthesis in the central nervous system is catalyzed by which enzyme that converts L-serine to glycine?",
    "options": [
      "Serine hydroxymethyltransferase (SHMT)",
      "Glycine cleavage system (GCS)",
      "Alanine-glyoxylate aminotransferase",
      "Phosphoserine phosphatase (PSP)"
    ],
    "answer": 0,
    "explain": "Serine hydroxymethyltransferase (SHMT1 cytosolic and SHMT2 mitochondrial) catalyzes the reversible conversion of L-serine and tetrahydrofolate (THF) into glycine and 5,10-methylene-THF, providing the major source of glycine in inhibitory spinal interneurons.",
    "example": "Defects in glycine degradation by the glycine cleavage system cause non-ketotic hyperglycinemia, manifesting as severe neonatal encephalopathy and intractable seizures.",
    "id": "bc-045",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Purinergic Signaling: Adenosine Generation",
    "prompt": "Extracellular ATP released during synaptic transmission is sequentially hydrolyzed to adenosine by which cell-surface ecto-enzymes?",
    "options": [
      "Ecto-nucleoside triphosphate diphosphohydrolase-1 (CD39) and ecto-5'-nucleotidase (CD73)",
      "Adenosine deaminase and purine nucleoside phosphorylase",
      "Protein kinase A and alkaline phosphatase",
      "Cyclic nucleotide phosphodiesterase and adenylate kinase"
    ],
    "answer": 0,
    "explain": "Ecto-enzymes CD39 (NTPDase1) hydrolyzes extracellular ATP/ADP to AMP, and CD73 (ecto-5'-nucleotidase) subsequently dephosphorylates AMP into adenosine, which binds inhibitory A1 receptors to suppress further neurotransmitter release.",
    "example": "Microglial CD39 and CD73 activity generates immunosuppressive and neuromodulatory adenosine clouds during neuroinflammatory flares.",
    "id": "bc-046",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Caffeine Mechanism of Action",
    "prompt": "Caffeine promotes psychomotor alertness and combats sleepiness primarily through which neurochemical mechanism at physiological concentrations?",
    "options": [
      "Non-selective competitive antagonism of A1 and A2A adenosine receptors",
      "Direct allosteric activation of dopamine D2 receptors",
      "Inhibition of acetylcholinesterase in the cerebral cortex",
      "Stimulation of GABA release from basal forebrain projections"
    ],
    "answer": 0,
    "explain": "At dietary doses (100-300 mg), caffeine acts as a competitive antagonist at adenosine A1 and A2A receptors, preventing sleep-promoting ambient adenosine from inhibiting cholinergic and monoaminergic wake-promoting centers.",
    "example": "In striatal medium spiny neurons, caffeine antagonism of A2A receptors relieves their tonic inhibition of D2 receptor signaling, enhancing psychomotor drive.",
    "id": "bc-047",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Endocannabinoid 2-AG Synthesis",
    "prompt": "The primary endocannabinoid 2-arachidonoylglycerol (2-AG) is synthesized on-demand in postsynaptic membranes through the hydrolysis of diacylglycerol by which enzyme?",
    "options": [
      "Diacylglycerol lipase alpha (DAGLalpha)",
      "Monoacylglycerol lipase (MAGL)",
      "N-acylphosphatidylethanolamine-specific phospholipase D (NAPE-PLD)",
      "Fatty acid amide hydrolase (FAAH)"
    ],
    "answer": 0,
    "explain": "DAGLalpha hydrolyzes diacylglycerol (generated from PIP2 by PLCbeta downstream of Gq or Ca2+ entry) into 2-AG. 2-AG then diffuses retrogradely across the synaptic cleft to activate presynaptic CB1 receptors.",
    "example": "Targeted deletion of DAGLalpha abolishes both depolarization-induced suppression of inhibition (DSI) and depolarization-induced suppression of excitation (DSE).",
    "id": "bc-048",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Anandamide Degradation by FAAH",
    "prompt": "The endocannabinoid anandamide (N-arachidonoylethanolamine, AEA) is primarily degraded inside postsynaptic neurons by which integral membrane enzyme?",
    "options": [
      "Fatty acid amide hydrolase (FAAH)",
      "Monoacylglycerol lipase (MAGL)",
      "Cyclooxygenase-2 (COX-2)",
      "Lipoxygenase-15 (15-LOX)"
    ],
    "answer": 0,
    "explain": "Fatty acid amide hydrolase (FAAH), localized to the endoplasmic reticulum, hydrolyzes anandamide into free arachidonic acid and ethanolamine, terminating its cannabinoid receptor-mediated signaling.",
    "example": "FAAH inhibitor drugs elevate brain anandamide concentrations, producing analgesic and anxiolytic effects in preclinical models without the motor ataxia caused by direct CB1 agonists.",
    "id": "bc-049",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "2-AG Degradation by MAGL",
    "prompt": "In contrast to anandamide, the predominant hydrolytic enzyme responsible for clearing ~85% of brain 2-arachidonoylglycerol (2-AG) is:",
    "options": [
      "Monoacylglycerol lipase (MAGL)",
      "Fatty acid amide hydrolase (FAAH)",
      "Diacylglycerol kinase (DGK)",
      "Secretory phospholipase A2 (sPLA2)"
    ],
    "answer": 0,
    "explain": "Monoacylglycerol lipase (MAGL), localized primarily to presynaptic axon terminals, hydrolyzes 2-AG into arachidonic acid and glycerol. MAGL serves as the principal enzymatic brake on retrograde 2-AG signaling.",
    "example": "Genetic or pharmacological disruption of MAGL massively elevates brain 2-AG levels and causes marked desensitization of CB1 receptors across the hippocampus and cerebellum.",
    "id": "bc-050",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Melatonin Biosynthesis in Pineal Gland",
    "prompt": "The rate-limiting step in pineal melatonin synthesis that undergoes dramatic circadian up-regulation at night is catalyzed by:",
    "options": [
      "Aralkylamine N-acetyltransferase (AANAT / serotonin N-acetyltransferase)",
      "Acetylserotonin O-methyltransferase (ASMT)",
      "Tryptophan hydroxylase 1 (TPH1)",
      "Aromatic L-amino acid decarboxylase (AADC)"
    ],
    "answer": 0,
    "explain": "Serotonin N-acetyltransferase (AANAT) converts serotonin to N-acetylserotonin. Sympathetic norepinephrine release via beta1-adrenergic receptors increases intracellular cAMP, activating PKA to phosphorylate and stabilize AANAT against proteasomal degradation at night.",
    "example": "Morning light exposure rapidly shuts off suprachiasmatic sympathetic stimulation to the pineal gland, triggering rapid dephosphorylation and ubiquitin-dependent destruction of AANAT.",
    "id": "bc-051",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Glutamate to Glutamine Stoichiometry",
    "prompt": "Astrocytic conversion of glutamate to glutamine by glutamine synthetase directly requires which energetic substrate?",
    "options": [
      "1 molecule of ATP and 1 molecule of ammonia (NH4+)",
      "1 molecule of GTP and 1 molecule of carbon dioxide",
      "1 molecule of NADH and 1 molecule of aspartate",
      "1 molecule of FADH2 and 1 molecule of hydrogen peroxide"
    ],
    "answer": 0,
    "explain": "Glutamine synthetase couples the amidation of glutamate with ammonia (NH4+) to the hydrolysis of ATP to ADP and inorganic phosphate: Glutamate + NH4+ + ATP -> Glutamine + ADP + Pi.",
    "example": "In hepatic encephalopathy, excessive blood ammonia enters the brain, driving astrocytic glutamine synthetase to consume glutamate and produce massive glutamine accumulation, causing cytotoxic astrocyte swelling.",
    "id": "bc-052",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Nitric Oxide Precursor and Cofactor",
    "prompt": "Neuronal nitric oxide synthase (nNOS) produces nitric oxide (NO) and L-citrulline from which amino acid substrate in a calcium/calmodulin-dependent reaction?",
    "options": [
      "L-Arginine",
      "L-Lysine",
      "L-Histidine",
      "L-Cysteine"
    ],
    "answer": 0,
    "explain": "nNOS oxidizes L-arginine to L-citrulline and nitric oxide (NO) in a 5-electron oxidation requiring NADPH, FAD, FMN, (6R)-tetrahydrobiopterin (BH4), heme, and Ca2+/calmodulin activation.",
    "example": "Endothelial and neuronal NOS inhibitors that mimic L-arginine (e.g., L-NAME) attenuate NMDA receptor-mediated neurotoxicity following transient ischemic stroke.",
    "id": "bc-053",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Aspartate as an Excitatory Neurotransmitter",
    "prompt": "L-Aspartate acts as an endogenous excitatory neurotransmitter in the central nervous system with selective agonist activity at which receptor type?",
    "options": [
      "NMDA receptors (binding the GluN2 glutamate/aspartate-recognition site)",
      "GABA-A receptors",
      "AMPA receptors exclusively",
      "Muscarinic M1 receptors"
    ],
    "answer": 0,
    "explain": "L-Aspartate activates NMDA receptors by binding to the GluN2 agonist binding domain with high affinity, but exhibits virtually no agonist activity at AMPA or kainate receptors, rendering it an endogenous NMDA-selective agonist.",
    "example": "Climbing fibers in the cerebellum release both L-aspartate and L-glutamate onto Purkinje cells to evoke complex spikes.",
    "id": "bc-054",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Choline Reuptake Transporter (CHT1)",
    "prompt": "What is the primary rate-limiting step in the overall synthesis of acetylcholine at cholinergic nerve terminals?",
    "options": [
      "High-affinity sodium-dependent choline uptake via CHT1 (SLC5A7)",
      "Choline acetyltransferase (ChAT) expression level",
      "Acetyl-CoA export from the mitochondrial matrix",
      "Hydrolysis of acetylcholine by butyrylcholinesterase"
    ],
    "answer": 0,
    "explain": "The high-affinity choline transporter CHT1 (SLC5A7) imports extracellular choline into the presynaptic terminal coupled to Na+ co-transport. CHT1 density and transport rate represent the primary rate-limiting bottleneck for sustained ACh synthesis.",
    "example": "Hemicholinium-3 competitively blocks CHT1 with nanomolar affinity, depleting presynaptic acetylcholine stores and causing neuromuscular transmission failure.",
    "id": "bc-055",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Taurine Neurochemical Function",
    "prompt": "Taurine (2-aminoethanesulfonic acid) is an abundant free amino acid in the brain that acts as an agonist at which inhibitory receptors?",
    "options": [
      "Glycine receptors and GABA-A receptors",
      "AMPA receptors and NMDA receptors",
      "Nicotinic acetylcholine receptors",
      "Purinergic P2X7 receptors"
    ],
    "answer": 0,
    "explain": "Taurine functions as an endogenous neuromodulator and osmoregulator; it directly activates strychnine-sensitive glycine receptors and GABAA receptors, dampening neuronal excitability and protecting against excitotoxic injury.",
    "example": "During hyposmotic cell swelling, neurons and astrocytes rapidly release taurine through volume-regulated anion channels (VRAC) to restore normal cell volume.",
    "id": "bc-056",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Vesicular Glutamate Transporters (VGLUTs)",
    "prompt": "Which primary biophysical driving force powers the vesicular uptake of L-glutamate through VGLUT1 and VGLUT2 into synaptic vesicles?",
    "options": [
      "The electrical potential gradient (delta-psi, inside positive) across the vesicular membrane generated by the vacuolar H+-ATPase",
      "The pH gradient (delta-pH, inside acidic) exclusively",
      "A direct sodium symport gradient powered by Na+/K+-ATPase",
      "Direct hydrolysis of ATP by the VGLUT transporter itself"
    ],
    "answer": 0,
    "explain": "VGLUT activity relies primarily on the electrical membrane potential component (delta-psi) of the proton electrochemical gradient established by the V-ATPase, with minimal dependence on delta-pH, ensuring optimal net negative glutamate anion loading.",
    "example": "Dissipation of delta-psi with the potassium ionophore valinomycin halts vesicular glutamate uptake without affecting delta-pH.",
    "id": "bc-057",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Vesicular GABA and Glycine Transporter (VGAT)",
    "prompt": "The vesicular inhibitory amino acid transporter (VGAT / VIAAT) is unique among classical vesicular transporters because it:",
    "options": [
      "Transports both GABA and glycine into synaptic vesicles utilizing both delta-pH and delta-psi equally",
      "Transports glutamate and aspartate in exchange for chloride",
      "Requires calcium binding to its cytoplasmic EF-hands to permit transport",
      "Is localized exclusively to the postsynaptic density"
    ],
    "answer": 0,
    "explain": "VGAT (SLC32A1) loads both GABA and glycine into synaptic vesicles. Unlike VGLUT (which depends mostly on delta-psi) or VMAT2 (which depends mostly on delta-pH), VGAT relies equally on both electrical (delta-psi) and chemical (delta-pH) components of the proton gradient.",
    "example": "In spinal cord interneurons, VGAT loads both GABA and glycine into the same vesicles, producing mixed inhibitory miniature postsynaptic currents.",
    "id": "bc-058",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "VMAT2 Stoichiometry and Pharmacology",
    "prompt": "Vesicular monoamine transporter 2 (VMAT2) packages dopamine, norepinephrine, and serotonin into vesicles via an antiport mechanism that exports:",
    "options": [
      "Two protons (H+) out of the vesicle lumen for every one neutral monoamine imported",
      "One sodium ion out for every one monoamine imported",
      "One chloride ion in alongside one monoamine",
      "One potassium ion out for every two monoamines imported"
    ],
    "answer": 0,
    "explain": "VMAT2 couples the uptake of one positively charged monoamine molecule to the extrusion of two luminal protons (2 H+), driven predominantly by the steep chemical pH gradient (delta-pH) maintained by the vacuolar H+-ATPase.",
    "example": "Tetrabenazine and reserpine selectively inhibit VMAT2, preventing monoamine storage and depleting central dopamine and serotonin reserves.",
    "id": "bc-059",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "EAAT2/GLT-1 Transport Stoichiometry",
    "prompt": "Astrocytic glutamate clearance through EAAT2 (GLT-1) achieves a 10^6-fold concentration gradient by coupling the import of one glutamate anion to the co-transport and counter-transport of:",
    "options": [
      "Co-transport of 3 Na+ and 1 H+, with counter-transport of 1 K+",
      "Co-transport of 1 Na+ and 1 Cl-, with counter-transport of 1 Ca2+",
      "Co-transport of 2 Na+, with counter-transport of 2 K+",
      "Co-transport of 3 K+, with counter-transport of 1 Na+"
    ],
    "answer": 0,
    "explain": "EAAT2 couples the inward transport of 1 L-glutamate anion to the inward movement of 3 Na+ ions and 1 H+, and the outward counter-transport of 1 K+ ion, utilizing the massive energy of the transmembrane sodium gradient.",
    "example": "During severe cerebral ischemia, the collapse of transmembrane Na+ and K+ gradients causes EAAT2 to run backwards, dumping toxic glutamate into the extracellular space.",
    "id": "bc-060",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Astrocyte-Neuron Lactate Shuttle Hypothesis",
    "prompt": "According to the Astrocyte-Neuron Lactate Shuttle (ANLS) model proposed by Pellerin and Magistretti, synaptic glutamate uptake into astrocytes triggers:",
    "options": [
      "Activation of the astrocytic Na+/K+-ATPase, stimulating aerobic glycolysis and lactate production for export to neurons",
      "Direct inhibition of astrocytic phosphofructokinase and cessation of glycolysis",
      "Immediate conversion of glutamate to beta-hydroxybutyrate for export via gap junctions",
      "Mitochondrial shutdown in astrocytes and exclusive reliance on neuronal ATP synthesis"
    ],
    "answer": 0,
    "explain": "Glutamate uptake via astrocytic EAATs brings 3 Na+ ions into the astrocyte, activating the alpha2-subunit Na+/K+-ATPase. The resulting ATP consumption stimulates astrocytic glucose uptake and glycolysis, generating lactate that is exported via MCT1/4 to fuel neuronal oxidative phosphorylation.",
    "example": "Disrupting astrocytic glycogenolysis or monocarboxylate transporter expression impairs long-term memory formation in rodents.",
    "id": "bc-061",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Monocarboxylate Transporters (MCTs) in Brain",
    "prompt": "Which monocarboxylate transporter isoform is selectively enriched on neuronal membranes, exhibiting high substrate affinity (Km ~ 0.7 mM) for lactate and pyruvate?",
    "options": [
      "MCT2 (SLC16A7)",
      "MCT1 (SLC16A1)",
      "MCT4 (SLC16A3)",
      "MCT8 (SLC16A2)"
    ],
    "answer": 0,
    "explain": "MCT2 is the primary neuronal lactate transporter. Its high affinity (Km ~0.7 mM) allows neurons to avidly take up lactate even when extracellular concentrations are low. Astrocytes predominantly express lower-affinity MCT1 and MCT4 (Km ~10-25 mM) optimized for lactate export.",
    "example": "Knockdown of hippocampal MCT2 blocks memory consolidation by starving active neurons of astrocyte-derived lactate.",
    "id": "bc-062",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Lactate Dehydrogenase Isozyme Distribution",
    "prompt": "Neurons preferentially express which lactate dehydrogenase (LDH) tetramer that favors the conversion of lactate to pyruvate for oxidative metabolism?",
    "options": [
      "LDH1 (composed of four LDHA-encoded H subunits)",
      "LDH5 (composed of four LDHB-encoded M subunits)",
      "LDH3 (a balanced H2M2 hybrid)",
      "Mitochondrial malate dehydrogenase"
    ],
    "answer": 0,
    "explain": "Neurons express predominantly LDH1 (H4 tetramer, encoded by LDHB), which exhibits a low Km for lactate and is allosterically inhibited by high pyruvate, favoring the oxidation of imported lactate into pyruvate for entry into the TCA cycle.",
    "example": "Astrocytes express LDH5 (M4 tetramer), which operates at high pyruvate concentrations to rapidly convert glycolytic pyruvate into exportable lactate.",
    "id": "bc-063",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Brain Glycogen Metabolism",
    "prompt": "In the adult mammalian central nervous system, glycogen granules are almost exclusively compartmentalized within which cell type?",
    "options": [
      "Astrocytes",
      "Pyramidal neurons",
      "Oligodendrocytes",
      "Microglia"
    ],
    "answer": 0,
    "explain": "Glycogen is stored almost entirely in astrocytes. Neurons express glycogen synthase but keep it constitutively silenced by glycogen synthase kinase-3 (GSK3) and the ubiquitin ligase malin-laforin complex to prevent catastrophic polyglucosan neurotoxicity.",
    "example": "Loss of malin or laforin leads to neuronal glycogen accumulation and toxic Lafora bodies, causing fatal progressive myoclonus epilepsy.",
    "id": "bc-064",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "nNOS Anchoring to Postsynaptic Density",
    "prompt": "Neuronal nitric oxide synthase (nNOS) is positioned directly adjacent to calcium influx through NMDA receptors via which molecular scaffolding mechanism?",
    "options": [
      "An N-terminal PDZ domain on nNOS that heterodimerizes with the second PDZ domain (PDZ2) of PSD-95",
      "Direct covalent palmitoylation to the GluN1 carboxyl tail",
      "Binding to ankyrin-G at the axon initial segment",
      "Transmembrane association with neuroligin-1"
    ],
    "answer": 0,
    "explain": "nNOS possesses an uncommon N-terminal PDZ domain that contains an internal beta-finger motif, which inserts into the peptide-binding pocket of PSD-95 PDZ2. This positions nNOS within nanometers of NMDA receptor calcium nanodomains.",
    "example": "Small-molecule disruptors of the nNOS/PSD-95 interaction prevent stroke-induced excitotoxic nitric oxide generation without blocking physiological NMDA channel gating.",
    "id": "bc-065",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Soluble Guanylyl Cyclase (sGC) Activation",
    "prompt": "Nitric oxide (NO) diffuses retrogradely into target cells and stimulates soluble guanylyl cyclase (sGC) to synthesize cyclic GMP by binding directly to:",
    "options": [
      "A prosthetic ferrous heme (Fe2+-protoporphyrin IX) group within the sGC beta1 subunit",
      "An ATP-binding Walker A motif on the alpha subunit",
      "A catalytic zinc finger in the regulatory domain",
      "A conserved tyrosine phosphorylation site"
    ],
    "answer": 0,
    "explain": "sGC is an obligate heterodimer (alpha1/beta1) containing a prosthetic Fe2+-heme. Binding of NO to the iron atom breaks the proximal histidine bond, causing a conformational change that stimulates catalytic conversion of GTP to cGMP by several hundred-fold.",
    "example": "sGC stimulators like riociguat bind to a non-heme allosteric site to sensitize sGC to endogenous low levels of nitric oxide.",
    "id": "bc-066",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Carbon Monoxide Gasotransmitter Synthesis",
    "prompt": "Carbon monoxide (CO) functions as a neural gasotransmitter and is produced constitutively in neurons through the breakdown of heme by which enzyme?",
    "options": [
      "Heme oxygenase-2 (HO-2)",
      "Biliverdin reductase",
      "Coproporphyrinogen oxidase",
      "Ferrochelatase"
    ],
    "answer": 0,
    "explain": "HO-2 is the constitutive neuronal isoform of heme oxygenase, richly expressed in hippocampus, cerebellum, and autonomic ganglia. It cleaves heme into carbon monoxide (CO), free iron (Fe2+), and biliverdin in an oxygen- and NADPH-dependent reaction.",
    "example": "Like NO, HO-2-derived CO stimulates soluble guanylyl cyclase to elevate cGMP in hippocampal neurons, modulating long-term potentiation.",
    "id": "bc-067",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Hydrogen Sulfide (H2S) in Neural Tissue",
    "prompt": "In the brain, hydrogen sulfide (H2S) functions as a neuromodulator produced primarily from L-cysteine by which enzyme that is enriched in astrocytes?",
    "options": [
      "Cystathionine beta-synthase (CBS)",
      "Rhodanese (thiosulfate sulfurtransferase)",
      "Methionine synthase",
      "Sulfite oxidase"
    ],
    "answer": 0,
    "explain": "Cystathionine beta-synthase (CBS) is the predominant enzyme generating H2S in the brain, utilizing L-cysteine and homocysteine. H2S enhances NMDA receptor currents by reducing critical disulfide bonds and activates astrocytic calcium waves.",
    "example": "Physiological nanomolar concentrations of H2S facilitate hippocampal long-term potentiation by potentiating NMDA receptor responses.",
    "id": "bc-068",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Neuropeptide Precursor Processing Enzymes",
    "prompt": "Proprotein convertases PC1/3 and PC2 cleave inactive neuropeptide precursors within the lumen of dense-core secretory granules specifically at which recognition motifs?",
    "options": [
      "Pairs of basic amino acid residues (such as Lys-Arg or Arg-Arg)",
      "Aromatic amino acid clusters (Phe-Trp-Tyr)",
      "Proline-rich motifs (PXXP)",
      "C-terminal acidic dipeptides (Asp-Glu)"
    ],
    "answer": 0,
    "explain": "Proprotein convertases 1/3 and 2 are calcium-dependent subtilisin-like endoproteases that cleave prohormones (e.g., pro-opiomelanocortin, pro-NPY) at the carboxyl side of paired basic residues (e.g., -Lys-Arg- and -Arg-Arg-).",
    "example": "Carboxypeptidase E (CPE) subsequently removes the basic residues exposed by PC1/3 and PC2 cleavage, completing neuropeptide maturation.",
    "id": "bc-069",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Neuropeptide C-Terminal Amidation (PAM)",
    "prompt": "Many biologically active neuropeptides (such as oxytocin, substance P, and NPY) require C-terminal amidation for receptor binding. Which enzyme catalyzes this modification using copper and ascorbic acid?",
    "options": [
      "Peptidylglycine alpha-amidating monooxygenase (PAM)",
      "Glutaminyl cyclase",
      "Protein L-isoaspartyl methyltransferase",
      "Transglutaminase 2"
    ],
    "answer": 0,
    "explain": "PAM is a bifunctional enzyme containing peptidylglycine alpha-hydroxylating monooxygenase (PHM) and peptidyl-alpha-hydroxyglycine alpha-amidating lyase (PAL) domains. It requires copper, ascorbate, and molecular oxygen to convert terminal glycine residues into amide (-NH2) groups.",
    "example": "Loss of PAM activity leaves neuropeptides with a negatively charged C-terminal carboxylate, abolishing their high-affinity receptor binding and bioactivity.",
    "id": "bc-070",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Calcium-Stimulated Adenylyl Cyclases",
    "prompt": "Which adenylyl cyclase isoforms are directly stimulated by submicromolar calcium/calmodulin, coupling postsynaptic Ca2+ influx to cyclic AMP production during synaptic plasticity?",
    "options": [
      "AC1 and AC8",
      "AC5 and AC6",
      "AC2 and AC4",
      "AC9 and soluble AC (sAC)"
    ],
    "answer": 0,
    "explain": "AC1 and AC8 are neuro-specific, calcium-calmodulin-stimulated adenylyl cyclases. During high-frequency synaptic stimulation, NMDA receptor Ca2+ influx activates AC1/AC8 via calmodulin, elevating cAMP to trigger PKA- and MAPK-mediated CREB phosphorylation.",
    "example": "AC1/AC8 double-knockout mice exhibit marked impairment in late-phase long-term potentiation (L-LTP) and spatial memory retention.",
    "id": "bc-071",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Phospholipase C-Beta Activation Mechanism",
    "prompt": "Phospholipase C-beta (PLCbeta) is stimulated downstream of Gq-protein coupled receptors (e.g., mGluR1/5, M1 muscarinic) to hydrolyze which membrane phospholipid?",
    "options": [
      "Phosphatidylinositol 4,5-bisphosphate (PIP2)",
      "Phosphatidylcholine",
      "Phosphatidylserine",
      "Sphingomyelin"
    ],
    "answer": 0,
    "explain": "Activated Galpha-q/11 stimulates PLCbeta, which hydrolyzes membrane phosphatidylinositol 4,5-bisphosphate (PIP2) into soluble inositol 1,4,5-trisphosphate (IP3) and membrane-bound 1,2-diacylglycerol (DAG).",
    "example": "PIP2 hydrolysis by PLCbeta not only generates IP3 and DAG but also depletes membrane PIP2, closing KCNQ/Kv7 M-channels and increasing neuronal firing frequency.",
    "id": "bc-072",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "IP3 Receptor Biphasic Calcium Sensitivity",
    "prompt": "Inositol 1,4,5-trisphosphate receptors (IP3Rs) on the endoplasmic reticulum exhibit which characteristic regulatory gating property in response to cytosolic calcium?",
    "options": [
      "A bell-shaped, biphasic open probability: stimulated by modest Ca2+ elevations (0.2-0.5 uM) and inhibited by high Ca2+ (>1 uM)",
      "Linear activation that increases monotonically up to 100 mM calcium",
      "Total insensitivity to calcium, opening strictly upon IP3 binding alone",
      "Irreversible channel inactivation whenever ATP is present"
    ],
    "answer": 0,
    "explain": "IP3Rs require both IP3 and Ca2+ as co-agonists. At resting Ca2+, binding of IP3 sensitizes the channel to Ca2+; rising cytosolic Ca2+ stimulates channel opening (positive feedback), but high Ca2+ (>1 uM) binds to a low-affinity inhibitory site, shutting the pore (negative feedback).",
    "example": "This biphasic Ca2+ dependence underpins regenerative, self-limiting intracellular calcium waves and oscillations in dendritic shafts and astrocytic syncytia.",
    "id": "bc-073",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Ryanodine Receptor Pharmacology and Dantrolene",
    "prompt": "Which therapeutic agent selectively binds and blocks ryanodine receptor channels (RyR1 and RyR3) on the endoplasmic reticulum, treating life-threatening hyperthermia and neuroleptic malignant syndrome?",
    "options": [
      "Dantrolene",
      "Thapsigargin",
      "Ruthenium red",
      "Tetrodotoxin"
    ],
    "answer": 0,
    "explain": "Dantrolene is a specific antagonist of ryanodine receptors (particularly RyR1), halting uncontrolled calcium-induced calcium release (CICR) from sarcoplasmic/endoplasmic reticulum stores to abort malignant hyperthermia crises.",
    "example": "Administering dantrolene in models of ischemic brain injury attenuates post-ischemic cytosolic calcium overload and reduces delayed neuronal death.",
    "id": "bc-074",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "SERCA Pump Inhibitor Thapsigargin",
    "prompt": "Thapsigargin is widely used in neurochemical research to deplete intracellular endoplasmic reticulum calcium stores because it selectively and irreversibly inhibits:",
    "options": [
      "Sarco/endoplasmic reticulum Ca2+-ATPase (SERCA) pumps",
      "Plasma membrane Ca2+-ATPase (PMCA)",
      "Mitochondrial calcium uniporters (MCU)",
      "Voltage-gated calcium channels (VGCC)"
    ],
    "answer": 0,
    "explain": "Thapsigargin locks the SERCA pump in an inactive conformation with sub-nanomolar affinity, preventing calcium re-uptake into the ER lumen. Unopposed basal passive ER leak rapidly depletes lumenal Ca2+ stores, activating store-operated Ca2+ entry (SOCE).",
    "example": "Application of thapsigargin to cultured cortical neurons triggers ER stress, unfolded protein response (UPR) activation, and CHOP-mediated apoptosis.",
    "id": "bc-075",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "PMCA vs NCX Kinetic Characteristics",
    "prompt": "Compared to the low-affinity, high-capacity Na+/Ca2+ exchanger (NCX), the Plasma Membrane Ca2+-ATPase (PMCA):",
    "options": [
      "Possesses a very high affinity for calcium (Km < 0.2 uM) but low maximal transport capacity, setting resting baseline calcium levels",
      "Transports calcium strictly into mitochondria rather than the extracellular space",
      "Requires extracellular sodium co-transport to extrude calcium",
      "Has a high capacity capable of clearing massive post-tetanic calcium loads in milliseconds"
    ],
    "answer": 0,
    "explain": "PMCA has high Ca2+ affinity (submicromolar Km) and is stimulated by Ca2+/calmodulin, making it ideal for maintaining baseline resting calcium (~50-100 nM). In contrast, NCX has lower affinity (Km ~1-5 uM) but high capacity, clearing large Ca2+ surges during intense action potential trains.",
    "example": "Targeted disruption of PMCA2 in auditory hair cells impairs resting calcium homeostasis, causing sensorineural deafness.",
    "id": "bc-076",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Parvalbumin Calcium Buffering Kinetics",
    "prompt": "Parvalbumin functions in fast-spiking basket cells as a 'slow-onset' calcium buffer primarily because:",
    "options": [
      "At resting intracellular conditions, its EF-hand binding sites are occupied by magnesium (Mg2+), requiring Mg2+ dissociation before Ca2+ can bind",
      "It is tethered exclusively to the outer mitochondrial membrane",
      "It requires cyclic AMP phosphorylation before it can interact with calcium",
      "It binds calcium with extremely low micromolar affinity (Kd > 50 uM)"
    ],
    "answer": 0,
    "explain": "Parvalbumin has high affinity for both Ca2+ and Mg2+. At resting Ca2+ (~50-100 nM) and physiological Mg2+ (~1 mM), parvalbumin is predominantly Mg2+-bound. Ca2+ cannot bind until Mg2+ slowly dissociates (k_off ~5-10 s^-1), allowing the initial Ca2+ spike to peak before parvalbumin accelerates the late decay phase.",
    "example": "This slow-buffering property allows parvalbumin-positive interneurons to fire at high frequencies (>100 Hz) without early Ca2+ attenuation.",
    "id": "bc-077",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Mitochondrial Complex I Function and Inhibitors",
    "prompt": "Complex I (NADH:ubiquinone oxidoreductase) transfers two electrons from NADH to ubiquinone while pumping how many protons across the inner mitochondrial membrane?",
    "options": [
      "4 protons (H+)",
      "2 protons (H+)",
      "6 protons (H+)",
      "0 protons (H+)"
    ],
    "answer": 0,
    "explain": "Complex I couples the exergonic transfer of 2 electrons from NADH to ubiquinone (via FMN and 8 iron-sulfur clusters) to the translocation of 4 protons across the inner mitochondrial membrane into the intermembrane space.",
    "example": "Rotenone and MPP+ bind to the ubiquinone reduction pocket of Complex I, halting proton pumping, depleting ATP, and stimulating superoxide production.",
    "id": "bc-078",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Mitochondrial Complex II (Succinate Dehydrogenase)",
    "prompt": "What distinguishes mitochondrial Complex II (succinate dehydrogenase) from Complexes I, III, and IV of the electron transport chain?",
    "options": [
      "It does not pump protons across the inner mitochondrial membrane and is encoded entirely by nuclear DNA",
      "It uses molecular oxygen as its direct electron acceptor",
      "It transfers electrons directly to cytochrome c without ubiquinone",
      "It is localized on the outer mitochondrial membrane"
    ],
    "answer": 0,
    "explain": "Complex II oxidizes succinate to fumarate in the TCA cycle and transfers electrons via FAD and Fe-S centers to ubiquinone. It does not pump protons (delta-psi is not generated) and is the only respiratory complex with zero subunits encoded by mitochondrial DNA (mtDNA).",
    "example": "3-Nitropropionic acid (3-NP) and malonate are suicide inhibitors of Complex II that produce selective striatal lesions mimicking Huntington's disease.",
    "id": "bc-079",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Complex IV (Cytochrome c Oxidase) Active Centers",
    "prompt": "Cytochrome c oxidase (Complex IV) catalyzes the final 4-electron reduction of O2 into 2 H2O using which active-site binuclear metal center?",
    "options": [
      "Heme a3 and copper B (CuB)",
      "Flavin adenine dinucleotide (FAD) and iron-sulfur cluster N2",
      "Molybdenum-pterin and tungsten",
      "Manganese cluster and zinc finger"
    ],
    "answer": 0,
    "explain": "Complex IV receives electrons from reduced cytochrome c at the binuclear CuA site, transfers them through heme a to the catalytic binuclear center composed of heme a3 and CuB, where molecular oxygen binds and is safely reduced to two water molecules without releasing toxic superoxide.",
    "example": "Cyanide and carbon monoxide bind with high affinity to the heme a3-CuB binuclear center, freezing cellular respiration and causing rapid anoxia.",
    "id": "bc-080",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Plasma Membrane Monoamine Transporter (PMAT)",
    "prompt": "The Plasma Membrane Monoamine Transporter (PMAT / SLC29A4) is distinguished from classical transporters (DAT, NET, SERT) because it:",
    "options": [
      "Is a sodium-independent, polyspecific, low-affinity, high-capacity 'uptake-2' transporter that transports dopamine, serotonin, and adenosine",
      "Couples monoamine uptake to the counter-transport of potassium and chloride",
      "Is selectively inhibited by citalopram and cocaine with sub-nanomolar affinity",
      "Transports monoamines exclusively in the outward direction into the synaptic cleft"
    ],
    "answer": 0,
    "explain": "PMAT (SLC29A4) operates independently of transmembrane Na+ and Cl- gradients. It mediates low-affinity, high-capacity (uptake-2) clearance of monoamines and purine nucleosides, playing a critical backup role in clearing monoamines when DAT/SERT are blocked.",
    "example": "In DAT knockout mice, residual dopamine clearance in the striatum is mediated in part by PMAT and organic cation transporters (OCTs).",
    "id": "bc-081",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "GlyT1 vs GlyT2 Functional Distinction",
    "prompt": "Which distinction accurately separates the two glycine transporters GlyT1 (SLC6A9) and GlyT2 (SLC6A5)?",
    "options": [
      "GlyT1 is localized on glia and postsynaptic elements to regulate NMDA receptor glycine co-agonist tone; GlyT2 is exclusively presynaptic and couples to 3 Na+ to refill vesicles",
      "GlyT1 is restricted to the spinal cord; GlyT2 is found exclusively in the retina",
      "GlyT1 is an ATP-dependent pump; GlyT2 is an ion channel",
      "GlyT1 transports glycine out of the brain; GlyT2 transports glycine into the brain across the BBB"
    ],
    "answer": 0,
    "explain": "GlyT1 operates with a 2 Na+ / 1 Cl- stoichiometry in astrocytes and neurons, keeping synaptic glycine levels near the threshold for NMDA receptor activation. GlyT2 is restricted to presynaptic glycinergic terminals and couples to 3 Na+ / 1 Cl-, generating the high gradient needed to reload synaptic vesicles.",
    "example": "Mutations in human GlyT2 (SLC6A5) impair presynaptic glycine refilling and cause hyperekplexia (hereditary startle disease).",
    "id": "bc-082",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Trace Amine-Associated Receptor 1 (TAAR1)",
    "prompt": "Trace Amine-Associated Receptor 1 (TAAR1) is an intracellular GPCR activated by trace amines and amphetamines that modulates dopamine neurotransmission by:",
    "options": [
      "Coupling to Gs and G13 to stimulate protein kinase cascades that trigger DAT internalization and reverse dopamine transport",
      "Directly opening postsynaptic chloride channels to hyperpolarize dopamine neurons",
      "Degrading cytosolic dopamine via non-oxidative deamination",
      "Blocking vesicular monoamine transporter 2 directly"
    ],
    "answer": 0,
    "explain": "TAAR1 is localized to intracellular compartments in monoaminergic neurons. Activation by trace amines (beta-PEA, tyramine) or amphetamines couples to Gs/cAMP and PKC signaling, phosphorylating DAT to promote transporter internalization and reverse transport (efflux).",
    "example": "TAAR1 agonists are being developed as novel non-D2-receptor-blocking antipsychotics that modulate dopaminergic hyperactivity without extrapyramidal side effects.",
    "id": "bc-083",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Phosphatidylserine Externalization in Synaptic Pruning",
    "prompt": "During developmental synaptic pruning, astrocytes and microglia recognize synapses tagged for engulfment via exposure of which phospholipid on the outer leaflet of the synaptic membrane?",
    "options": [
      "Phosphatidylserine (PtdSer)",
      "Phosphatidylcholine",
      "Sphingomyelin",
      "Cardiolipin"
    ],
    "answer": 0,
    "explain": "In healthy membranes, flippases keep phosphatidylserine (PtdSer) sequestered to the inner cytoplasmic leaflet. Local synaptic activity changes or complement activation stimulate scramblases, exposing PtdSer on the outer leaflet as an 'eat-me' signal recognized by microglial TREM2 and astrocytic MEGF10.",
    "example": "Blocking exposed phosphatidylserine with Annexin V protects inactive synapses from phagocytic elimination by reactive microglia.",
    "id": "bc-084",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "G-Protein Coupled Receptor Kinases (GRKs)",
    "prompt": "Following agonist binding to GPCRs (e.g., beta2-adrenergic or dopamine D1 receptors), homologous desensitization is initiated when GRKs phosphorylate:",
    "options": [
      "Serine and threonine residues in the intracellular C-terminal tail and third intracellular loop of the receptor",
      "The Galpha-s subunit at its GTP-binding cleft",
      "Extracellular loop 2 to displace the bound neurotransmitter",
      "The membrane phosphatidylinositol 4,5-bisphosphate headgroups"
    ],
    "answer": 0,
    "explain": "GRK2 and GRK3 selectively phosphorylate agonist-activated GPCRs on intracellular serine/threonine residues. This phosphorylation creates high-affinity binding sites for beta-arrestin-1 and beta-arrestin-2, sterically uncoupling the receptor from heterotrimeric G-proteins.",
    "example": "Beta-arrestin binding not only terminates G-protein signaling but also acts as an adaptor linking the receptor to clathrin-coated pits for endocytosis.",
    "id": "bc-085",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "RGS Proteins in G-Protein Signaling Termination",
    "prompt": "Regulators of G-protein Signaling (RGS proteins) accelerate the termination of GPCR signals by acting as:",
    "options": [
      "GTPase-Activating Proteins (GAPs) that accelerate the intrinsic GTP hydrolysis rate of Galpha subunits by up to 1,000-fold",
      "Guanine nucleotide exchange factors (GEFs) that load GTP onto Galpha",
      "Kinases that phosphorylate Gbeta-gamma dimers",
      "Proteases that cleave G-protein coupled receptors"
    ],
    "answer": 0,
    "explain": "RGS proteins bind directly to active Galpha-GTP, stabilizing the transition state for GTP hydrolysis. By functioning as GAPs, RGS proteins accelerate GTP hydrolysis by orders of magnitude, allowing rapid signal termination when the agonist unbinds.",
    "example": "RGS4 and RGS9-2 in the striatum terminate dopamine D2 and opioid receptor signaling; RGS9 knockout prolongs dopamine-induced locomotor responses.",
    "id": "bc-086",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Purinergic P2X vs P2Y Receptor Classes",
    "prompt": "Purinergic receptors for extracellular ATP and ADP are divided into two fundamentally different structural classes:",
    "options": [
      "P2X (trimeric ligand-gated cation channels) and P2Y (seven-transmembrane GPCRs)",
      "P2X (nuclear steroid receptors) and P2Y (tyrosine kinase receptors)",
      "P2X (chloride channels) and P2Y (voltage-gated sodium channels)",
      "P2X (heterotrimeric G-proteins) and P2Y (vesicular proton pumps)"
    ],
    "answer": 0,
    "explain": "P2X receptors (P2X1-7) are trimeric, ATP-gated non-selective cation channels (permeable to Na+, K+, and Ca2+). P2Y receptors (P2Y1, 2, 4, 6, 11, 12, 13, 14) are metabotropic GPCRs coupled to Gq, Gi, or Gs.",
    "example": "Microglial P2Y12 receptors couple to Gi to drive chemotaxis toward damaged neurons releasing ATP, whereas P2X7 channels trigger NLRP3 inflammasome assembly.",
    "id": "bc-087",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cardiolipin in Neuronal Mitochondria",
    "prompt": "Cardiolipin is a unique tetra-acyl phospholipid synthesized and localized almost exclusively to which cellular membrane, where it stabilizes respiratory chain supercomplexes?",
    "options": [
      "The mitochondrial inner membrane",
      "The neuronal plasma membrane lipid rafts",
      "The nuclear envelope outer membrane",
      "The synaptic vesicle membrane"
    ],
    "answer": 0,
    "explain": "Cardiolipin contains four acyl chains and two phosphate groups. It resides almost entirely in the inner mitochondrial membrane, where it physically bridges respiratory Complexes I, III, and IV into functional 'respirasomes' and anchors cytochrome c.",
    "example": "Peroxidation of cardiolipin by mitochondrial ROS triggers cytochrome c detachment and permeabilization of the outer membrane, initiating intrinsic apoptosis.",
    "id": "bc-088",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Superoxide Dismutase Isoforms and Localization",
    "prompt": "Which superoxide dismutase is compartmentalized within the mitochondrial matrix, utilizing manganese as a cofactor to convert superoxide radicals (O2•-) into hydrogen peroxide?",
    "options": [
      "SOD2 (MnSOD)",
      "SOD1 (Cu/ZnSOD)",
      "SOD3 (EcSOD)",
      "Catalase"
    ],
    "answer": 0,
    "explain": "SOD2 (manganese superoxide dismutase) is encoded in the nucleus, imported into the mitochondrial matrix, and scavenges superoxide anions generated by electron leakage from Complexes I and III of the electron transport chain.",
    "example": "Mice lacking Sod2 die within the first days of life from dilated cardiomyopathy and severe neurodegeneration with massive mitochondrial lipid peroxidation.",
    "id": "bc-089",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Glutathione Biosynthesis Rate-Limiting Enzyme",
    "prompt": "What is the committed rate-limiting step in the de novo biosynthesis of the primary neuronal antioxidant glutathione (GSH)?",
    "options": [
      "L-glutamate-L-cysteine ligase (GCL, catalyzed by GCLC/GCLM subunits)",
      "Glutathione synthetase (GS)",
      "Glutathione reductase (GR)",
      "Gamma-glutamyl transpeptidase (GGT)"
    ],
    "answer": 0,
    "explain": "Glutamate-cysteine ligase (GCL) couples L-glutamate and L-cysteine via an atypical gamma-glutamyl bond, consuming ATP. It is the rate-limiting enzyme for GSH synthesis and is allosterically feedback-inhibited by physiologic concentrations of GSH.",
    "example": "Overexpression of the catalytic subunit GCLC in dopaminergic neurons protects against MPTP toxicity by maintaining intracellular glutathione pools.",
    "id": "bc-090",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Glutathione Peroxidase 4 and Selenocysteine",
    "prompt": "Glutathione peroxidase 4 (GPX4) uniquely prevents ferroptotic cell death in neurons by reducing toxic lipid hydroperoxides directly within membrane bilayers, using which catalytic residue?",
    "options": [
      "Selenocysteine",
      "Cysteine",
      "Dehydroalanine",
      "Methionine sulfoxide"
    ],
    "answer": 0,
    "explain": "GPX4 contains an active-site selenocysteine encoded by a recoded UGA stop codon. Selenocysteine confers resistance to irreversible oxidative over-oxidation, allowing GPX4 to efficiently detoxify phospholipid hydroperoxides (PLOOH) to lipid alcohols (PLOH).",
    "example": "Conditional genetic deletion of Gpx4 in forebrain neurons triggers massive hippocampal neurodegeneration that is halted by lipophilic radical-trapping antioxidants.",
    "id": "bc-091",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Peroxynitrite Formation Kinetics",
    "prompt": "Peroxynitrite (ONOO-) is a potent cytotoxic reactive nitrogen species formed in neurons through a diffusion-limited, non-enzymatic reaction between which two radicals?",
    "options": [
      "Nitric oxide (NO•) and superoxide (O2•-)",
      "Hydroxyl radical (OH•) and nitrogen dioxide (NO2•)",
      "Hydrogen peroxide (H2O2) and ammonia (NH4+)",
      "Singlet oxygen (1O2) and nitrite (NO2-)"
    ],
    "answer": 0,
    "explain": "Nitric oxide reacts with superoxide anion at a near-diffusion-limited rate constant (~10^10 M^-1 s^-1), outcompeting endogenous SOD. The resulting peroxynitrite protonates to peroxynitrous acid, which rapidly cleaves into hydroxyl and nitrogen dioxide radicals.",
    "example": "Nitrotyrosine immunoreactivity serves as a stable pathological footprint of peroxynitrite-mediated protein damage in Parkinsonian substantia nigra.",
    "id": "bc-092",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Parthanatos Cell Death Mechanism",
    "prompt": "During excitotoxicity and severe oxidative stress, overactivation of Poly(ADP-ribose) Polymerase-1 (PARP-1) triggers parthanatos cell death primarily by:",
    "options": [
      "Depleting cellular NAD+ and ATP pools, while poly(ADP-ribose) polymers trigger mitochondrial release of Apoptosis-Inducing Factor (AIF)",
      "Directly phosphorylating and opening the pore of GABAA receptors",
      "Degrading histones to disrupt chromosomal architecture",
      "Cleaving pro-caspase-3 into active executioner caspase fragments"
    ],
    "answer": 0,
    "explain": "Excessive DNA single-strand breaks overactivate nuclear PARP-1, which hydrolyzes massive quantities of NAD+ to build poly(ADP-ribose) (PAR) polymers. Cytoplasmic PAR polymers bind mitochondrial AIF, causing AIF-MIF nuclear translocation and large-scale DNA fragmentation.",
    "example": "PARP-1 knockout mice and animals treated with PARP inhibitors (e.g., olaparib) are dramatically resistant to stroke and glutamate excitotoxicity.",
    "id": "bc-093",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Polyunsaturated Fatty Acids in Neural Membranes",
    "prompt": "Which omega-3 polyunsaturated fatty acid represents over 40% of all PUFAs in mammalian brain grey matter and is critical for synaptic membrane fluidity and rhodopsin activation?",
    "options": [
      "Docosahexaenoic acid (DHA, 22:6 n-3)",
      "Eicosapentaenoic acid (EPA, 20:5 n-3)",
      "Alpha-linolenic acid (ALA, 18:3 n-3)",
      "Arachidonic acid (ARA, 20:4 n-6)"
    ],
    "answer": 0,
    "explain": "Docosahexaenoic acid (DHA, 22:6 n-3) possesses six unconjugated cis-double bonds, conferring extreme conformational flexibility and low membrane viscosity, which accelerates rhodopsin conformational transitions and synaptic vesicle fusion kinetics.",
    "example": "Dietary omega-3 deficiency depletes hippocampal DHA, impairs synaptic plasticity, and compromises learning performance in behavioural assays.",
    "id": "bc-094",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Plasmalogens in Myelin and Synapses",
    "prompt": "Plasmalogens are specialized ether glycerophospholipids enriched in myelin and synaptic membranes that act as sacrificial antioxidants due to which unique chemical feature?",
    "options": [
      "A vinyl-ether (cis-alpha,beta-unsaturated) double bond at the sn-1 position of the glycerol backbone",
      "A high-energy thioester bond linked to coenzyme A",
      "A cyclic phosphate group that traps free radicals",
      "A sphingoid base attached to a long-chain saturated fatty acid"
    ],
    "answer": 0,
    "explain": "Plasmalogens contain a vinyl-ether linkage (-O-CH=CH-) at the sn-1 position that is uniquely sensitive to homolytic attack by singlet oxygen and hydroxyl radicals, terminating lipid peroxidation cascades by decomposing into benign aldehydes without generating propagating radicals.",
    "example": "Peroxisomal biogenesis disorders (such as Zellweger syndrome) fail to synthesize plasmalogens, leading to devastating demyelination and early death.",
    "id": "bc-095",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Gangliosides and Lipid Raft Organization",
    "prompt": "Which sialic acid-containing glycosphingolipid is the predominant ganglioside in adult mammalian cerebral cortex, acting as a crucial regulator of lipid rafts and neurotrophin Trk receptor signaling?",
    "options": [
      "GM1 (monosialoganglioside 1)",
      "GD1b",
      "GT1b",
      "Galactosylceramide"
    ],
    "answer": 0,
    "explain": "GM1 consists of a ceramide lipid anchor attached to an oligosaccharide core bearing a single sialic acid residue. It partitions into cholesterol-rich membrane microdomains (lipid rafts), where it physically stabilizes TrkA/TrkB receptors and neurotrophic factor signaling complexes.",
    "example": "Exogenous administration of GM1 ganglioside enhances neurotrophin responsiveness and exerts neuroprotective effects in Parkinson's disease models.",
    "id": "bc-096",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Ketone Body Utilization in Fasting Brain",
    "prompt": "During prolonged starvation or adherence to a ketogenic diet, which enzyme converts acetoacetate to acetoacetyl-CoA in neuronal mitochondria, initiating ketone body utilization for ATP generation?",
    "options": [
      "Succinyl-CoA:3-ketoacid CoA transferase (SCOT / OXCT1)",
      "Beta-hydroxybutyrate dehydrogenase 1 (BDH1)",
      "HMG-CoA synthase",
      "Acetoacetyl-CoA thiolase (ACAT1)"
    ],
    "answer": 0,
    "explain": "SCOT (OXCT1) transfers CoA from succinyl-CoA to acetoacetate, generating acetoacetyl-CoA and succinate. SCOT is abundantly expressed in neurons and glia, but completely absent in liver (preventing futile hepatic consumption of newly synthesized ketone bodies).",
    "example": "In severe diabetic ketoacidosis or starvation, ketone bodies can supply over 60% of the brain's total energy expenditure.",
    "id": "bc-097",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "O-GlcNAcylation and Phosphorylation Crosstalk",
    "prompt": "O-GlcNAc transferase (OGT) utilizes UDP-GlcNAc from the hexosamine biosynthetic pathway to attach O-linked N-acetylglucosamine to serine/threonine residues of synaptic proteins, functionally acting to:",
    "options": [
      "Compete directly with protein kinases for identical or adjacent Ser/Thr residues, modulating synaptic strength and preventing tau hyperphosphorylation",
      "Target synaptic proteins to the 20S proteasome for degradation",
      "Anchor cytoplasmic enzymes to the inner leaflet of the plasma membrane",
      "Induce irreversible crosslinking of cytoskeletal neurofilaments"
    ],
    "answer": 0,
    "explain": "O-GlcNAcylation is a dynamic, nutrient-sensitive post-translational modification. Because O-GlcNAc and phosphate groups target serine and threonine hydroxyls, O-GlcNAcylation often reciprocally blocks pathological hyperphosphorylation on proteins such as tau and synapsin.",
    "example": "Inhibitors of O-GlcNAcase (OGA), such as Thiamet-G, elevate brain O-GlcNAc levels and significantly slow tau aggregation in transgenic tauopathy models.",
    "id": "bc-098",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "System xc- Cystine/Glutamate Antiporter",
    "prompt": "System xc- (composed of catalytic subunit SLC7A11 and chaperone SLC3A2) maintains intracellular glutathione synthesis by operating as a sodium-independent antiporter that:",
    "options": [
      "Imports one molecule of cystine in exchange for exporting one molecule of intracellular glutamate",
      "Imports one molecule of cysteine along with three sodium ions",
      "Exports oxidized glutathione (GSSG) in exchange for imported ATP",
      "Transports glutamine and glycine symmetrically across the BBB"
    ],
    "answer": 0,
    "explain": "System xc- exports intracellular glutamate down its steep concentration gradient to drive the uphill import of extracellular cystine (the oxidized dimer of cysteine). Inside the cell, cystine is rapidly reduced to cysteine, the rate-limiting building block for GSH.",
    "example": "High concentrations of extracellular glutamate competitively inhibit System xc-, causing intracellular cysteine and GSH depletion, driving oxidative ferroptosis.",
    "id": "bc-099",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Ferroptosis Driver: PE-PUFA Peroxidation",
    "prompt": "In the biochemical execution of neuronal ferroptosis, which specific lipid species undergoes lethal iron-dependent peroxidative cleavage?",
    "options": [
      "Phosphatidylethanolamines containing arachidonic and adrenic acids (PE-PUFAs)",
      "Saturated dipalmitoylphosphatidylcholine",
      "Myelin cerebrosides and sulfatides",
      "Mitochondrial cardiolipin exclusively"
    ],
    "answer": 0,
    "explain": "Acyl-CoA synthetase long-chain family member 4 (ACSL4) and lysophosphatidylcholine acyltransferase 3 (LPCAT3) esterify polyunsaturated fatty acids (arachidonic and adrenic acid) into phosphatidylethanolamines (PE). Non-heme iron and 15-lipoxygenase then catalyze the peroxidation of these PE-PUFAs, disrupting membrane integrity.",
    "example": "Knockout of ACSL4 prevents ferroptosis by depleting oxidizable PE-arachidonoyl species from the membrane.",
    "id": "bc-100",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Fenton Reaction in Labile Iron Pool",
    "prompt": "The labile iron pool (LIP) in dopaminergic and cortical neurons promotes catastrophic oxidative damage primarily by catalyzing the Fenton reaction, in which:",
    "options": [
      "Ferrous iron (Fe2+) reacts with hydrogen peroxide (H2O2) to generate the highly reactive hydroxyl radical (OH•) and ferric iron (Fe3+)",
      "Ferric iron (Fe3+) is reduced to iron metal by molecular oxygen",
      "Iron atoms insert into the active site of tyrosine hydroxylase",
      "Hydrogen peroxide is converted to molecular nitrogen"
    ],
    "answer": 0,
    "explain": "The Fenton reaction (Fe2+ + H2O2 -> Fe3+ + OH• + OH-) produces the hydroxyl radical (OH•), the most electrophilic and reactive ROS known, which reacts instantly with nearby lipids, proteins, and DNA at diffusion-controlled rates.",
    "example": "Iron chelators like deferoxamine sequester free Fe2+, halting Fenton chemistry and reducing dopaminergic cell loss in neurotoxin models.",
    "id": "bc-101",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Mitochondrial Outer Membrane Fusion by Mitofusins",
    "prompt": "Mitochondrial outer membrane fusion in neurons requires which membrane-anchored dynamin-related GTPases that form homo- and heterotypic trans-tethers between adjacent mitochondria?",
    "options": [
      "Mitofusin 1 (MFN1) and Mitofusin 2 (MFN2)",
      "Optic atrophy 1 (OPA1)",
      "Dynamin-related protein 1 (DRP1)",
      "Mitochondrial fission factor (Mff)"
    ],
    "answer": 0,
    "explain": "MFN1 and MFN2 are GTPases embedded in the outer mitochondrial membrane. GTP binding and hydrolysis drive conformational changes that bring the outer membranes of adjacent mitochondria into close apposition, triggering lipid bilayer mixing and fusion.",
    "example": "Dominant mutations in MFN2 cause Charcot-Marie-Tooth disease type 2A (CMT2A), a peripheral sensorimotor neuropathy characterized by axonal mitochondrial fragmentation.",
    "id": "bc-102",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Inner Mitochondrial Membrane Fusion by OPA1",
    "prompt": "Fusion of the inner mitochondrial membrane and stabilization of narrow cristae junctions to trap cytochrome c is coordinated by:",
    "options": [
      "Optic atrophy 1 (OPA1)",
      "Mitofusin 1 (MFN1)",
      "Fis1",
      "Parkin"
    ],
    "answer": 0,
    "explain": "OPA1 is an inner membrane GTPase that exists in long (membrane-bound) and short (proteolytically cleaved) forms. Together, they mediate inner membrane fusion and oligomerize to cinch cristae junctions, preventing the premature release of cytochrome c.",
    "example": "Loss-of-function mutations in OPA1 cause Autosomal Dominant Optic Atrophy (ADOA) through retinal ganglion cell degeneration caused by cristae disorganization.",
    "id": "bc-103",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Mitochondrial Fission by DRP1",
    "prompt": "Mitochondrial fission is executed when cytosolic Dynamin-Related Protein 1 (DRP1) is recruited to the outer mitochondrial membrane and:",
    "options": [
      "Assembles into helical rings around the constriction site, hydrolyzing GTP to constrict and sever both inner and outer membranes",
      "Inserts into cristae to pump protons into the matrix",
      "Directly ubiquitinates voltage-dependent anion channels",
      "Translocates to the nucleus to induce apoptosis"
    ],
    "answer": 0,
    "explain": "DRP1 is recruited from the cytosol to outer membrane receptors (Mff, Fis1, MiD49/51). DRP1 oligomerizes into spiral collars around ER-mitochondria contact sites, utilizing GTP hydrolysis to generate mechanical force that constricts and divides the organelle.",
    "example": "Inhibition of DRP1 with the small molecule Mdivi-1 prevents excessive mitochondrial fragmentation and protects neurons during ischemic reperfusion.",
    "id": "bc-104",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "PINK1 Stabilization Mechanism",
    "prompt": "Under normal physiological conditions with polarized mitochondria, newly synthesized PTEN-induced kinase 1 (PINK1) is rapidly degraded because it is:",
    "options": [
      "Imported across both membranes and cleaved by the inner membrane rhomboid protease PARL, triggering N-end rule proteasomal degradation",
      "Phosphorylated by PKA in the cytosol and retained in ribosomes",
      "Directly excreted from the cell via multivesicular bodies",
      "Sequestered inside the mitochondrial matrix by chaperones"
    ],
    "answer": 0,
    "explain": "In healthy mitochondria with intact delta-psi, PINK1 is imported via the TIM23 complex. Its transmembrane domain is cleaved by presenilin-associated rhomboid-like protease (PARL). The cleaved 52 kDa fragment retrotranslocates to the cytosol and is degraded by the ubiquitin-proteasome system.",
    "example": "Loss of membrane potential halts import, causing full-length 64 kDa PINK1 to accumulate on the outer membrane, initiating mitophagy.",
    "id": "bc-105",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Phosphorylated Ubiquitin as Mitophagy Signal",
    "prompt": "Stabilized on depolarized mitochondrial outer membranes, PINK1 initiates mitophagy by phosphorylating which critical substrate at Serine 65?",
    "options": [
      "Both Ubiquitin and the ubiquitin-like (Ubl) domain of Parkin",
      "Cytochrome c and Complex I subunit NDUFS1",
      "Voltage-dependent anion channel 1 (VDAC1) exclusively",
      "Mitochondrial transcription factor A (TFAM)"
    ],
    "answer": 0,
    "explain": "PINK1 phosphorylates both free/conjugated Ubiquitin at Ser65 and the N-terminal Ubl domain of Parkin at Ser65. Phospho-Ser65-Ubiquitin acts as a high-affinity allosteric activator that recruits auto-inhibited Parkin and triggers its E3 ligase activity.",
    "example": "Mutations preventing Ser65 phosphorylation of Parkin or Ubiquitin impair autophagic engulfment of damaged mitochondria in early-onset Parkinson's disease.",
    "id": "bc-106",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "PFKFB3 Degradation and Neuronal Bioenergetics",
    "prompt": "Why do neurons exhibit a markedly lower glycolytic rate than astrocytes, diverting glucose preferentially into the pentose phosphate pathway (PPP)?",
    "options": [
      "Neurons constitutively degrade the potent glycolytic activator enzyme PFKFB3 via the APC/C-Cdh1 ubiquitin ligase",
      "Neurons lack hexokinase and cannot phosphorylate glucose",
      "Neuronal glucose transporters are completely inactive under basal conditions",
      "The neuronal cytoplasm contains no NAD+ to support glycolysis"
    ],
    "answer": 0,
    "explain": "6-Phosphofructo-2-kinase/fructose-2,6-bisphosphatase 3 (PFKFB3) synthesizes fructose-2,6-bisphosphate, the most potent allosteric activator of phosphofructokinase-1. In neurons, the E3 ligase APC/C-Cdh1 constitutively degrades PFKFB3, shunting glucose-6-phosphate into the PPP to regenerate NADPH for glutathione reduction.",
    "example": "Forced expression of PFKFB3 in neurons elevates glycolysis but causes oxidative stress and apoptotic cell death due to NADPH depletion.",
    "id": "bc-107",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Adenosine Kinase (ADK) and Seizure Susceptibility",
    "prompt": "In the central nervous system, ambient extracellular adenosine tone is primarily dictated by astrocytic adenosine kinase (ADK), which:",
    "options": [
      "Phosphorylates adenosine into AMP, driving passive adenosine influx into astrocytes through equilibrative nucleoside transporters (ENTs)",
      "Degrades adenosine into inosine and hypoxanthine",
      "Synthesizes adenosine from AMP on the outer surface of astrocytes",
      "Pumps adenosine across the blood-brain barrier into cerebral capillaries"
    ],
    "answer": 0,
    "explain": "Astrocytic ADK has a low Km for adenosine (~1 uM), keeping intracellular astrocytic adenosine levels extremely low. This draws extracellular adenosine into astrocytes via ENTs, setting the ambient inhibitory adenosine tone at neuronal A1 receptors.",
    "example": "In chronic epilepsy, astrogliosis causes marked ADK overexpression, depleting ambient adenosine and removing A1-mediated inhibition, promoting recurrent seizures.",
    "id": "bc-108",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Allopregnanolone Biosynthesis and GABAA Receptors",
    "prompt": "The endogenous neurosteroid allopregnanolone (3alpha,5alpha-tetrahydroprogesterone) is a potent positive allosteric modulator of GABAA receptors synthesized from progesterone by:",
    "options": [
      "Sequential reduction by 5alpha-reductase and 3alpha-hydroxysteroid dehydrogenase (3alpha-HSD)",
      "Oxidation by aromatase and 17beta-HSD",
      "Hydroxylation by cytochrome P450c17",
      "Sulfation by steroid sulfotransferase (SULT2A1)"
    ],
    "answer": 0,
    "explain": "Progesterone is reduced by 5alpha-reductase to 5alpha-dihydroprogesterone, which is then converted by 3alpha-HSD into allopregnanolone. Allopregnanolone binds to transmembrane cavities on extrasynaptic delta-subunit-containing GABAA receptors, massively potentiating tonic inhibition.",
    "example": "Brexanolone (synthetic allopregnanolone) and zuranolone are approved rapid-acting therapeutics for postpartum depression.",
    "id": "bc-109",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Sulfated Neurosteroids as Negative Modulators",
    "prompt": "Unlike allopregnanolone, sulfated neurosteroids such as pregnenolone sulfate (PS) and dehydroepiandrosterone sulfate (DHEAS) modulate neuronal excitability by:",
    "options": [
      "Acting as non-competitive antagonists at GABAA receptors and positive allosteric modulators at NMDA receptors",
      "Inhibiting voltage-gated sodium channels directly",
      "Binding to cannabinoid CB1 receptors to block retrograde inhibition",
      "Stimulating astrocytic glutamate reuptake through EAAT2"
    ],
    "answer": 0,
    "explain": "Pregnenolone sulfate acts as a negative allosteric modulator of GABAA receptors (accelerating desensitization) and a positive allosteric modulator of NMDA receptors (increasing channel open probability), thereby enhancing neuronal excitability.",
    "example": "Age-related declines in central pregnenolone sulfate levels correlate with deficits in NMDA receptor-dependent synaptic plasticity and cognitive decline.",
    "id": "bc-110",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "PIP2 Regulation of KCNQ/Kv7 Channels",
    "prompt": "Neuronal KCNQ2/3 (Kv7.2/7.3) channels that generate the non-inactivating 'M-current' require direct membrane binding of which lipid to remain open at subthreshold potentials?",
    "options": [
      "Phosphatidylinositol 4,5-bisphosphate (PIP2)",
      "Lysophosphatidic acid (LPA)",
      "Ceramide 1-phosphate",
      "Diacylglycerol (DAG)"
    ],
    "answer": 0,
    "explain": "Kv7 channels require PIP2 electrostatic interaction with basic residues in the S4-S5 linker and C-terminal tail to couple voltage-sensor movement to pore opening. Hydrolysis of PIP2 by Gq-coupled receptors (e.g., M1, bradykinin) shuts the channel, depolarizing the neuron.",
    "example": "Retigabine (ezogabine) is an allosteric opener that stabilizes the open conformation of Kv7 channels, acting as a potent anticonvulsant.",
    "id": "bc-111",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Synaptojanin-1 in Endocytic Vesicle Uncoating",
    "prompt": "Synaptojanin-1 (SYNJ1) is a dual-domain inositol polyphosphate phosphatase that facilitates clathrin coat shedding during synaptic vesicle recycling by hydrolyzing:",
    "options": [
      "PI(4,5)P2 into phosphatidylinositol (PI), releasing clathrin adaptor proteins like AP-2 and AP180",
      "ATP into cAMP inside the vesicle lumen",
      "GTP to drive dynamin constriction",
      "Phosphatidylserine to trigger membrane fusion"
    ],
    "answer": 0,
    "explain": "Synaptojanin-1 contains a 5-phosphatase domain that converts PI(4,5)P2 to PI(4)P, and a SAC1 domain that converts PI(4)P to PI. Depletion of PI(4,5)P2 on newly endocytosed vesicle membranes destabilizes clathrin adaptors (AP-2, AP180), triggering rapid uncoating.",
    "example": "Synaptojanin-1 knockout mice display an accumulation of clathrin-coated vesicles at synapses and severe neurological impairment with early postnatal lethality.",
    "id": "bc-112",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "S-Nitrosylation of Synaptic Proteins",
    "prompt": "S-Nitrosylation is a redox-based post-translational modification wherein nitric oxide is covalently attached to which specific functional group on target proteins?",
    "options": [
      "A reactive cysteine thiol group (-SH) to form an S-nitrosothiol (-SNO)",
      "A lysine epsilon-amino group to form a Schiff base",
      "A tyrosine phenolic ring to form 3-nitrotyrosine",
      "A serine hydroxyl group to form an O-nitro ester"
    ],
    "answer": 0,
    "explain": "S-Nitrosylation involves the non-enzymatic coupling of an NO moiety to a nucleophilic cysteine sulfhydryl group (-SH) to form an S-nitrosothiol (-SNO). It modulates the activity of hundreds of proteins, including NMDA receptors, Parkin, and Drp1.",
    "example": "S-Nitrosylation of the E3 ubiquitin ligase Parkin (S-NO-Parkin) inhibits its neuroprotective ligase activity in sporadic Parkinson's disease.",
    "id": "bc-113",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Mitochondrial Permeability Transition Pore Trigger",
    "prompt": "During acute glutamate excitotoxicity, massive calcium entry into the mitochondrial matrix triggers opening of the mitochondrial permeability transition pore (mPTP), leading to:",
    "options": [
      "Immediate collapse of the mitochondrial membrane potential (delta-psi-m), matrix swelling, and release of pro-apoptotic factors like Cytochrome c",
      "A rapid surge in ATP synthesis through Complex V",
      "Hyperpolarization of the inner membrane to -220 mV",
      "Selective export of calcium while maintaining proton impermeability"
    ],
    "answer": 0,
    "explain": "Matrix Ca2+ overload, exacerbated by ROS and adenine nucleotide depletion, opens the high-conductance mPTP (>1.5 kDa cutoff). This collapses delta-psi-m, uncouples oxidative phosphorylation, causes osmotic matrix swelling that ruptures the outer membrane, and releases cytochrome c.",
    "example": "Cyclosporin A inhibits cyclophilin D (CypD), preventing mPTP opening and reducing brain infarct volume following stroke.",
    "id": "bc-114",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "MPTP Conversion and Dopaminergic Vulnerability",
    "prompt": "The pro-neurotoxin MPTP produces Parkinsonian neurodegeneration following which specific sequence of metabolic transformations and transport events?",
    "options": [
      "Astrocytic MAO-B converts MPTP to MPP+, which is selectively concentrated into dopaminergic neurons via DAT and inhibits mitochondrial Complex I",
      "Neuronal MAO-A converts MPTP to 6-OHDA, which destroys dopamine receptors",
      "Endothelial cells convert MPTP into cyanide, which blocks Complex IV in the striatum",
      "Microglial iNOS converts MPTP into peroxynitrite, triggering parthanatos"
    ],
    "answer": 0,
    "explain": "Lipophilic MPTP crosses the BBB and is converted by astrocytic MAO-B into toxic MPP+ (1-methyl-4-phenylpyridinium). MPP+ is exported from glia and selectively imported by dopamine neurons via DAT, where it accumulates inside mitochondria and blocks Complex I.",
    "example": "DAT knockout mice and animals pretreated with the MAO-B inhibitor selegiline are completely protected against MPTP neurotoxicity.",
    "id": "bc-115",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Trk Receptor Tyrosine Kinase Downstream Cascades",
    "prompt": "Activation of TrkB by Brain-Derived Neurotrophic Factor (BDNF) leads to receptor dimerization, trans-autophosphorylation, and recruitment of PLCgamma1 via which conserved protein domain?",
    "options": [
      "An SH2 (Src Homology 2) domain that recognizes phosphorylated Tyr816 on the TrkB carboxyl tail",
      "A PDZ domain binding to the C-terminal valine residue",
      "A Pleckstrin homology (PH) domain binding to membrane PIP3",
      "A WW domain binding to proline-rich sequences"
    ],
    "answer": 0,
    "explain": "Phosphorylated Tyr816 on TrkB creates a high-affinity docking site for the SH2 domain of PLCgamma1. Once bound, PLCgamma1 is phosphorylated and activated, hydrolyzing PIP2 into IP3 and DAG, stimulating CaMKII and promoting synaptic plasticity.",
    "example": "Mice bearing a targeted mutation at the TrkB Tyr816 docking site (TrkB-PLCgamma mutant) fail to express long-term potentiation in CA1 hippocampus.",
    "id": "bc-116",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "A-Kinase Anchoring Proteins (AKAPs) in Synaptic Targeting",
    "prompt": "AKAP150 (AKAP79/150) organizes postsynaptic signaling complexes at dendritic spines by directly scaffolding which group of enzymes to NMDA and AMPA receptors?",
    "options": [
      "Protein Kinase A (PKA), Protein Kinase C (PKC), and Protein Phosphatase 2B (Calcineurin)",
      "Tyrosine hydroxylase, dopamine beta-hydroxylase, and MAO-A",
      "Hexokinase 1, phosphofructokinase, and pyruvate kinase",
      "RNA polymerase II, histone deacetylase 1, and DNA topoisomerase"
    ],
    "answer": 0,
    "explain": "AKAP79/150 is a master postsynaptic scaffold that tethers the regulatory subunits of PKA, along with PKC and calcineurin (PP2B), directly to PSD-95 and SAP97, ensuring rapid, bidirectional phosphorylation/dephosphorylation of GluA1 AMPA subunits during LTP and LTD.",
    "example": "Disrupting the PKA-binding domain of AKAP150 prevents PKA phosphorylation of GluA1 at Ser845 and impairs long-term potentiation maintenance.",
    "id": "bc-117",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "BK vs SK Calcium-Activated Potassium Channels",
    "prompt": "Small-conductance calcium-activated potassium channels (SK channels, SK1-3) generate the slow afterhyperpolarization (sAHP) to regulate action potential firing frequency because they:",
    "options": [
      "Are strictly voltage-independent and gated exclusively by submicromolar calcium via constitutively bound calmodulin",
      "Require extreme membrane depolarizations (+40 mV) to open",
      "Are activated by ATP binding to their cytoplasmic nucleotide-binding domain",
      "Are impermeable to potassium and conduct chloride anions"
    ],
    "answer": 0,
    "explain": "Unlike BK channels (which require both depolarization and micromolar Ca2+), SK channels are voltage-independent and gated exclusively by submicromolar Ca2+ (EC50 ~0.3 uM) via constitutively tethered calmodulin, generating prolonged afterhyperpolarizations that limit burst firing.",
    "example": "Apamin, a peptide neurotoxin from honeybee venom, selectively blocks SK2/SK3 channels, increasing neuronal excitability and facilitating learning.",
    "id": "bc-118",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Brain Cholesterol Synthesis Exclusively In Situ",
    "prompt": "Because circulating plasma lipoproteins cannot cross the intact blood-brain barrier, essentially 100% of brain cholesterol is synthesized in situ primarily by:",
    "options": [
      "Astrocytes (via the de novo mevalonate pathway) and transported to neurons on ApoE-containing lipoprotein particles",
      "Endothelial cells and transported into neurons via GLUT1",
      "Microglia and secreted into the cerebrospinal fluid as free crystals",
      "Oligodendrocytes exclusively during embryogenesis with zero adult turnover"
    ],
    "answer": 0,
    "explain": "Brain cholesterol is synthesized de novo from acetyl-CoA via HMG-CoA reductase, predominantly in astrocytes. Astrocytes load cholesterol and phospholipids onto Apolipoprotein E (ApoE) discs via the ABCA1 transporter for receptor-mediated uptake by neuronal LRP1/LDLR.",
    "example": "ApoE4 exhibits impaired lipid efflux compared to ApoE3, leading to altered neuronal membrane lipid raft composition and increased A-beta aggregation.",
    "id": "bc-119",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Dopamine Quinone Toxicity and Neuromelanin",
    "prompt": "Unsequestered cytosolic dopamine undergoes non-enzymatic auto-oxidation in the presence of trace transition metals to produce:",
    "options": [
      "Reactive dopamine ortho-quinones and aminochromes, which polymerize into insoluble neuromelanin granules",
      "Serotonin and 5-HIAA",
      "Glutamate and GABA through transamination",
      "Insoluble beta-sheet amyloid plaques"
    ],
    "answer": 0,
    "explain": "Free cytosolic dopamine auto-oxidizes into dopamine quinones, semiquinone radicals, and superoxide. Quinones covalently adduct nucleophilic cysteines on Parkin, TH, and Complex I, before eventually polymerizing into protective neuromelanin pigments in substantia nigra neurons.",
    "example": "Age-dependent saturation of neuromelanin's metal-binding capacity promotes iron release into the cytosol, accelerating Parkinsonian neurodegeneration.",
    "id": "bc-120",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "D-Serine Biosynthesis by Serine Racemase",
    "prompt": "D-Serine functions as the predominant endogenous co-agonist at NMDA receptors in the forebrain, synthesized from L-serine by which PLP-dependent enzyme?",
    "options": [
      "Serine racemase (SR)",
      "D-amino acid oxidase (DAAO)",
      "Phosphoserine phosphatase (PSP)",
      "3-Phosphoglycerate dehydrogenase (PHGDH)"
    ],
    "answer": 0,
    "explain": "Serine racemase is a pyridoxal 5'-phosphate (PLP)-dependent enzyme expressed in neurons and astrocytes that catalyzes the reversible conversion of L-serine to D-serine. It is allosterically stimulated by ATP and Mg2+.",
    "example": "Serine racemase knockout mice show an 85-90% reduction in brain D-serine levels, leading to severe deficits in NMDA-dependent hippocampal LTP.",
    "id": "bc-121",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Kynurenine Pathway Neuroactive Metabolites",
    "prompt": "In the microglial kynurenine pathway of tryptophan degradation, which downstream metabolite acts as an endogenous NMDA receptor agonist capable of producing excitotoxic lesions?",
    "options": [
      "Quinolinic acid (QUIN)",
      "Kynurenic acid (KYNA)",
      "Anthranilic acid",
      "Picolinic acid"
    ],
    "answer": 0,
    "explain": "Pro-inflammatory cytokines (e.g., IFN-gamma) induce microglial IDO1, shunting tryptophan into the kynurenine pathway to produce quinolinic acid (QUIN). QUIN is a potent agonist at NMDA receptors and generates lipid peroxidation, while astrocytic KYNA is an NMDA antagonist.",
    "example": "Elevated quinolinic acid / kynurenic acid ratios in the cerebrospinal fluid correlate with neurocognitive impairment in HIV-associated neurocognitive disorders and depression.",
    "id": "bc-122",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Amphetamine Mechanism of Action at DAT and VMAT2",
    "prompt": "Amphetamine elevates extracellular dopamine through a coordinated 'reverse transport' process involving which sequential molecular steps?",
    "options": [
      "Entering the terminal as a DAT substrate, disrupting the vesicular pH gradient to displace dopamine into the cytoplasm, and stimulating CaMKII/PKC phosphorylation of DAT to reverse its transport direction",
      "Directly inhibiting acetylcholinesterase to increase acetylcholine release onto dopamine terminals",
      "Opening presynaptic voltage-gated calcium channels to stimulate exocytosis",
      "Covalently alkylating postsynaptic dopamine D2 autoreceptors"
    ],
    "answer": 0,
    "explain": "Amphetamine is transported into the axon terminal via DAT. Being a weak base, it dissipates the vesicular proton gradient (delta-pH) via VMAT2, causing vesicular dopamine to leak into the cytoplasm. Elevated cytoplasmic dopamine, combined with PKC/CaMKII-mediated DAT N-terminal phosphorylation, reverses the transporter, driving non-exocytotic dopamine efflux.",
    "example": "Mutating the N-terminal phosphorylation sites on DAT prevents amphetamine-induced reverse dopamine transport without affecting normal dopamine uptake.",
    "id": "bc-123",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Structural Mechanism of VMAT2 Alternating Access",
    "prompt": "Cryo-EM structures of human VMAT2 have demonstrated that proton counter-transport and substrate translocation rely on two conserved aspartate residues located in:",
    "options": [
      "Transmembrane helices 1 and 10 (Asp33 and Asp399), which alternate between protonated and substrate-bound states",
      "The luminal loop between TM7 and TM8",
      "The intracellular amino-terminal cytoplasmic tail",
      "The membrane-associated amphipathic helix 12"
    ],
    "answer": 0,
    "explain": "Asp33 (TM1) and Asp399 (TM10) form a conserved acidic pair inside the central binding cavity. Protonation of these aspartates stabilizes the lumen-facing conformation; subsequent deprotonation upon monoamine binding triggers rocker-switch rocking of the N- and C-terminal bundles to face the cytoplasm.",
    "example": "Tetrabenazine traps VMAT2 in the cytoplasm-facing occluded conformation, whereas reserpine locks it in the lumen-facing state.",
    "id": "bc-124",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "EAAT2 Trimeric Elevator Transport Mechanism",
    "prompt": "Cryo-EM and biophysical studies of EAAT2 (GLT-1) have demonstrated that glutamate uptake occurs via an 'elevator mechanism' wherein:",
    "options": [
      "Each protomer in the trimer operates independently, with a mobile substrate-binding transport domain moving ~18 Å vertically through a rigid lipid-anchored scaffold domain",
      "All three protomers must open simultaneously in a coordinated rotary motion powered by ATP hydrolysis",
      "The entire trimeric complex rotates 180 degrees in the membrane plane to flip glutamate across the bilayer",
      "Glutamate passes through a static, water-filled central pore formed at the trimer symmetry axis"
    ],
    "answer": 0,
    "explain": "EAAT2 exists as a homotrimer where each subunit contains a rigid scaffold domain that oligomerizes, and a dynamic transport domain carrying hairpins HP1 and HP2. The transport domain binds 1 glutamate, 3 Na+, and 1 H+, plunging 18 Å across the membrane like an elevator car.",
    "example": "Crosslinking the transport domain to the scaffold domain with engineered disulfide bridges completely paralyzes glutamate transport.",
    "id": "bc-125",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Mitochondrial Calcium Uniporter (MCU) Gating",
    "prompt": "At resting cytosolic calcium concentrations (<100 nM), calcium influx through the mitochondrial calcium uniporter (MCU) pore is kept completely shut by which EF-hand gatekeepers?",
    "options": [
      "MICU1 and MICU2 heterodimers located in the mitochondrial intermembrane space",
      "Calbindin-D28k and parvalbumin in the cytosol",
      "Bcl-2 and Bax on the outer membrane",
      "Cyclophilin D in the mitochondrial matrix"
    ],
    "answer": 0,
    "explain": "MICU1 and MICU2 form an intermembrane space heterodimer that caps the MCU pore at resting [Ca2+] (<500 nM), preventing catastrophic mitochondrial calcium overload and loss of delta-psi-m. Only when local Ca2+ exceeds ~1-2 uM do MICU1/2 bind Ca2+ and swing open the pore.",
    "example": "Loss-of-function mutations in human MICU1 abolish this threshold gate, causing chronic mitochondrial calcium overload, myopathy, and severe learning disabilities.",
    "id": "bc-126",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Palmitoylation Cycles in PSD-95 Dynamics",
    "prompt": "Synaptic targeting and clustering of PSD-95 at postsynaptic densities is reversibly regulated by palmitoylation of Cys3 and Cys5, catalyzed by which enzyme family?",
    "options": [
      "DHHC-family zinc finger palmitoyl acyltransferases (e.g., zDHHC8 and zDHHC17)",
      "Protein kinase A (PKA)",
      "Phospholipase C (PLC)",
      "Fatty acid synthase (FAS)"
    ],
    "answer": 0,
    "explain": "zDHHC enzymes catalyze the addition of 16-carbon palmitate groups to N-terminal Cys3 and Cys5 of PSD-95 via thioester bonds. Palmitoylation anchors PSD-95 to synaptic membranes; depalmitoylation by acyl-protein thioesterases (APT1/2) triggers PSD-95 dispersal away from the synapse during LTD.",
    "example": "Activity-dependent depalmitoylation of PSD-95 is required for the endocytosis of AMPA receptors during cerebellar long-term depression.",
    "id": "bc-127",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Astrocytic Kir4.1 Spatial Potassium Buffering",
    "prompt": "During high-frequency repetitive action potential firing, the clearance of extracellular potassium (K+) from the synaptic cleft into astrocytic networks is primarily driven by:",
    "options": [
      "Inwardly rectifying potassium channels Kir4.1 (KCNJ10), coupled to water co-entry through Aquaporin-4 (AQP4)",
      "Voltage-gated potassium channels Kv1.1 on axon initial segments",
      "Simple passive aqueous diffusion across the dura mater",
      "Direct symport with glucose through GLUT1 transporters"
    ],
    "answer": 0,
    "explain": "Astrocytes have a very negative resting potential (~-85 mV) governed by Kir4.1 channels. Local rises in synaptic K+ shift the local K+ equilibrium potential, driving massive K+ influx into astrocytes through Kir4.1, which is spatially redistributed through astrocytic gap junctions (Cx43).",
    "example": "Conditional knockout of Kir4.1 in astrocytes leads to elevated baseline extracellular K+, severe hyperexcitability, spontaneous epileptic seizures, and early death.",
    "id": "bc-128",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "GAPDH Moonlighting and Siah1 Apoptotic Cascade",
    "prompt": "Under severe oxidative stress, the glycolytic enzyme glyceraldehyde-3-phosphate dehydrogenase (GAPDH) undergoes which non-metabolic 'moonlighting' transformation that triggers apoptosis?",
    "options": [
      "S-nitrosylation at Cys150, enabling GAPDH to bind the E3 ligase Siah1 and translocate to the nucleus to stabilize p300/CBP and activate p53",
      "Cleavage by caspase-3 into toxic peptides that perforate the plasma membrane",
      "Conversion into an active kinase that phosphorylates tau at Ser202",
      "Irreversible aggregation into Lewy body filaments"
    ],
    "answer": 0,
    "explain": "Nitric oxide reacts with the active-site Cys150 of GAPDH to form S-nitrosylated GAPDH (S-NO-GAPDH). This abolishes glycolytic activity and reveals a binding site for the E3 ubiquitin ligase Siah1. The complex translocates into the nucleus, activating apoptotic cascades.",
    "example": "Deprenyl (selegiline) and its derivative CGP 3466B prevent S-NO-GAPDH/Siah1 binding at picomolar concentrations, blocking apoptotic neuronal death.",
    "id": "bc-129",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Neurovascular Coupling Biochemical Cascade",
    "prompt": "Functional hyperemia (neurovascular coupling) during intense local synaptic activity is mediated by astrocytic calcium rises that stimulate:",
    "options": [
      "Cytosolic phospholipase A2 (cPLA2), releasing arachidonic acid which is converted by cytochrome P450 epoxygenases into vasodilatory epoxyeicosatrienoic acids (EETs)",
      "Urea cycle enzymes to produce toxic ammonia that paralyzes vascular smooth muscle",
      "Lactate export that lowers blood pH to induce reflex vasoconstriction",
      "Myelin sheath contraction around capillary pericytes"
    ],
    "answer": 0,
    "explain": "Synaptic glutamate activates astrocytic mGluR and purinergic receptors, triggering IP3-mediated Ca2+ elevations. This activates cPLA2, liberating arachidonic acid (AA). Astrocytic CYP2C epoxygenases convert AA to 14,15-EET and 11,12-EET, which dilate parenchymal arterioles.",
    "example": "Pharmacological blockade of CYP epoxygenases significantly blunts the BOLD fMRI hemodynamic response in sensory cortex upon whisker stimulation.",
    "id": "bc-130",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Purinergic P2X7 Receptor Pore Dilation",
    "prompt": "Upon sustained, high-concentration stimulation by extracellular ATP (>1 mM), the trimeric P2X7 receptor undergoes a unique transition known as 'pore dilation', resulting in:",
    "options": [
      "Opening of a large, non-selective macropore permeable to hydrophilic molecules and dyes up to 900 Da (e.g., YO-PRO-1), followed by NLRP3 inflammasome activation",
      "Complete and permanent desensitization to ATP within 5 milliseconds",
      "Transformation into an exclusive chloride-selective channel",
      "Disassembly of the trimer into inactive monomeric subunits"
    ],
    "answer": 0,
    "explain": "Prolonged ATP activation converts P2X7 from a small cation channel (Na+/Ca2+) into a large-conductance pore permeable to molecules up to ~900 Da. This causes massive intracellular K+ depletion, triggering assembly of the NLRP3 inflammasome and caspase-1-dependent release of IL-1beta.",
    "example": "P2X7 receptor antagonists suppress neuroinflammation and microglial activation in models of traumatic brain injury and amyotrophic lateral sclerosis.",
    "id": "bc-131",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Carnitine Palmitoyltransferase 1c (CPT1c) in Neurons",
    "prompt": "The brain-specific carnitine palmitoyltransferase isoform CPT1c is localized to the endoplasmic reticulum rather than mitochondria, functioning not in beta-oxidation but in:",
    "options": [
      "Sensing energy status by binding malonyl-CoA to regulate GluA1 AMPA receptor trafficking and spine morphology",
      "Synthesizing ketone bodies from short-chain fatty acids",
      "Importing fatty acids into synaptic vesicles for transmitter loading",
      "Phosphorylating glycogen synthase in cortical astrocytes"
    ],
    "answer": 0,
    "explain": "CPT1c possesses malonyl-CoA binding activity but negligible carnitine acyltransferase activity. Localized to the neuronal ER, it acts as a metabolic sensor: when malonyl-CoA levels fall, CPT1c promotes the forward trafficking and surface expression of GluA1-containing AMPA receptors.",
    "example": "Cpt1c knockout mice exhibit abnormal cerebellar Purkinje cell dendritic arborization and severe motor coordination deficits.",
    "id": "bc-132",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "TET Enzymes and 5-Hydroxymethylcytosine in Brain",
    "prompt": "Ten-eleven translocation (TET) enzymes (TET1-3) are exceptionally abundant in mammalian neurons, catalyzing the oxidation of 5-methylcytosine (5mC) into 5-hydroxymethylcytosine (5hmC) using which obligate co-substrates?",
    "options": [
      "Alpha-ketoglutarate (2-oxoglutarate), molecular oxygen (O2), and ferrous iron (Fe2+)",
      "S-adenosylmethionine (SAM) and ATP",
      "NADPH and flavin adenine dinucleotide (FAD)",
      "Tetrahydrofolate and vitamin B12"
    ],
    "answer": 0,
    "explain": "TET proteins belong to the Fe2+/alpha-ketoglutarate-dependent dioxygenase superfamily. They convert 5mC to 5hmC (and further to 5fC and 5caC) in an alpha-ketoglutarate- and ascorbate-dependent manner, opening chromatin and promoting active DNA demethylation during memory consolidation.",
    "example": "5hmC constitutes up to 1% of total cytosines in the mammalian hippocampus—more than tenfold higher than in non-neuronal somatic tissues.",
    "id": "bc-133",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Histone Serotonylation by Transglutaminase 2",
    "prompt": "In an epigenetic neurochemical mechanism, transglutaminase 2 (TGM2) establishes permissive chromatin states for neuroplasticity genes by covalently conjugating:",
    "options": [
      "Serotonin to glutamine 5 of histone H3 (H3Q5ser), creating a combinatorial mark with trimethylated lysine 4 (H3K4me3)",
      "Dopamine to lysine 9 of histone H3",
      "GABA to the C-terminal tail of histone H2A",
      "Acetylcholine to the globular core of histone H4"
    ],
    "answer": 0,
    "explain": "TGM2 uses serotonin as an alternative amine substrate, forming an isopeptide bond with glutamine 5 on histone H3. This 'serotonylation' mark (H3Q5ser) stabilizes TFIID at the promoter, facilitating transcription of neurodevelopmental and synaptic plasticity genes.",
    "example": "Pharmacological or genetic inhibition of histone serotonylation impairs the differentiation of serotonergic raphe neurons.",
    "id": "bc-134",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Striatal Phosphodiesterase 10A (PDE10A)",
    "prompt": "Phosphodiesterase 10A (PDE10A) is exceptionally enriched in striatal medium spiny neurons (MSNs), where it coordinates motor output by hydrolyzing:",
    "options": [
      "Both cyclic AMP (cAMP) and cyclic GMP (cGMP) in both striatonigral (direct) and striatopallidal (indirect) pathway projection neurons",
      "Phosphatidylinositol 4,5-bisphosphate exclusively",
      "S-adenosylmethionine into homocysteine",
      "Adenosine triphosphate into inorganic pyrophosphate"
    ],
    "answer": 0,
    "explain": "PDE10A is a dual-substrate phosphodiesterase with high affinity for cAMP and cGMP. Enriched in striatal MSNs, it acts as a master enzymatic regulator of dopamine D1 (cAMP-elevating) and D2 (cAMP-lowering) signaling cascades.",
    "example": "PDE10A inhibitors elevate striatal cyclic nucleotides and are under clinical investigation for Huntington's disease and schizophrenia.",
    "id": "bc-135",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Synaptic Vesicle V-ATPase Rotary Mechanism",
    "prompt": "The vacuolar H+-ATPase (V-ATPase) that generates the electrochemical proton gradient across synaptic vesicles operates as a rotary nanomotor composed of:",
    "options": [
      "A peripheral cytoplasmic V1 complex that hydrolyzes ATP to rotate a central stalk, driving proton translocation through the membrane-embedded V0 proteolipid ring",
      "A single polypeptide chain that oscillates back and forth across the lipid bilayer",
      "A voltage-gated ion channel that consumes NADH to pump protons",
      "An ABC-transporter cassette that flips protonated phospholipids"
    ],
    "answer": 0,
    "explain": "The V-ATPase has two domains: the soluble V1 domain (A3B3 hexamer) that hydrolyzes ATP, and the integral membrane V0 domain (c-ring). ATP hydrolysis generates mechanical torque that spins the central rotor, driving protons through the V0 channel against a steep electrochemical gradient.",
    "example": "Bafilomycin A1 specifically binds the c-subunit ring of the V0 sector, instantly arresting vesicular acidification and halting neurotransmitter uptake.",
    "id": "bc-136",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Lysosomal Glucocerebrosidase (GBA1) in Dopamine Neurons",
    "prompt": "Loss-of-function mutations in the lysosomal enzyme glucocerebrosidase (GBA1) represent the strongest common genetic risk factor for Parkinson's disease because glucosylceramide accumulation:",
    "options": [
      "Directly stabilizes and accelerates toxic alpha-synuclein oligomerization while alpha-synuclein reciprocally inhibits lysosomal GBA1 trafficking",
      "Inhibits dopamine beta-hydroxylase to block norepinephrine synthesis",
      "Blocks glucose uptake across the blood-brain barrier",
      "Triggers immediate calcification of the basal ganglia"
    ],
    "answer": 0,
    "explain": "GBA1 hydrolyzes glucosylceramide into ceramide and glucose in lysosomes. GBA1 deficiency leads to accumulation of lipid substrates that physically interact with alpha-synuclein, stabilizing toxic protofibrils. In turn, alpha-synuclein aggregates disrupt ER-to-Golgi trafficking of nascent GBA1, creating a pathogenic feed-forward loop.",
    "example": "Heterozygous carriers of GBA1 N370S or L444P mutations have an ~5-fold increased lifetime risk of developing Parkinson's disease with earlier cognitive decline.",
    "id": "bc-137",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Reverse Electron Transport (RET) at Complex I",
    "prompt": "During the reperfusion phase following cerebral ischemia, massive and explosive bursts of reactive oxygen species (ROS) are produced by mitochondrial Complex I via:",
    "options": [
      "Reverse electron transport (RET), driven by succinate oxidation at Complex II pushing electrons backwards into an over-reduced ubiquinone pool and onto Complex I",
      "Forward electron leakage from Cytochrome c oxidase",
      "Direct reduction of oxygen by myoglobin",
      "De-lipidation of the inner mitochondrial membrane by phospholipase D"
    ],
    "answer": 0,
    "explain": "During ischemia, succinate accumulates to high levels. Upon reperfusion, succinate dehydrogenase (Complex II) rapidly oxidizes succinate, generating a massive protonmotive force and hyper-reducing the coenzyme Q pool. This forces electrons to flow backwards through Complex I, generating catastrophic amounts of superoxide at the FMN site.",
    "example": "Administering malonate (a competitive Complex II inhibitor) at the start of reperfusion blocks succinate oxidation and eliminates RET-driven ROS generation, dramatically reducing stroke infarct size.",
    "id": "bc-138",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "S-Adenosylmethionine (SAM) Methylation Potential",
    "prompt": "The cellular 'methylation potential' that regulates DNA and histone methyltransferases in the brain is quantified biochemically by the ratio of:",
    "options": [
      "S-adenosylmethionine (SAM) to S-adenosylhomocysteine (SAH)",
      "Glutathione (GSH) to oxidized glutathione (GSSG)",
      "ATP to ADP",
      "NADH to NAD+"
    ],
    "answer": 0,
    "explain": "SAM serves as the methyl donor for DNA (DNMTs), RNA, and protein (HMTs) methyltransferases, yielding S-adenosylhomocysteine (SAH) as a product. Because SAH is a potent competitive product inhibitor of nearly all methyltransferases, the SAM/SAH ratio dictates global methylation capacity.",
    "example": "Accumulation of SAH due to S-adenosylhomocysteine hydrolase (AHCY) inhibition causes global DNA hypomethylation and severe neurological developmental arrest.",
    "id": "bc-139",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Astrocytic Pyruvate Carboxylase Anaplerosis",
    "prompt": "Net replenishment of TCA cycle intermediates (anaplerosis) lost during glutamate synthesis in the brain is performed exclusively by astrocytes through which enzyme?",
    "options": [
      "Pyruvate carboxylase (PC)",
      "Malic enzyme",
      "Phosphoenolpyruvate carboxykinase (PEPCK)",
      "Pyruvate dehydrogenase (PDH)"
    ],
    "answer": 0,
    "explain": "Pyruvate carboxylase (PC) carboxylates pyruvate into oxaloacetate consuming ATP and CO2. PC is expressed in astrocytes but is completely absent in neurons. Therefore, neurons cannot synthesize new 4-carbon dicarboxylic acids and depend entirely on astrocytic glutamine for anaplerosis.",
    "example": "Infants with pyruvate carboxylase deficiency develop severe lactic acidosis, brain malformations, and lethal neonatal encephalopathy.",
    "id": "bc-140",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Single-Spine ATP Measurements with PercevalHR",
    "prompt": "Genetically encoded fluorescent biosensors (such as PercevalHR and ATeam) have revealed that during high-frequency synaptic transmission, single dendritic spines:",
    "options": [
      "Experience transient localized ATP depletion that recovers within seconds primarily via local astrocytic glycolysis and phosphocreatine shuttling",
      "Remain at completely stable, infinite ATP levels without fluctuation",
      "Completely shut off all ATP consumption",
      "Rely exclusively on beta-oxidation of fatty acids"
    ],
    "answer": 0,
    "explain": "Two-photon imaging of PercevalHR in individual spines demonstrates that synaptic glutamate stimulation drives intense local ATP hydrolysis by actin-remodeling ATPases and ion pumps. Immediate ATP buffering depends on the creatine kinase/phosphocreatine circuit and rapid glycolytic influx.",
    "example": "Inhibition of the creatine kinase shuttle severely reduces the frequency of AMPA receptor insertion into postsynaptic densities during LTP.",
    "id": "bc-141",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Liquid-Liquid Phase Separation of Synapsin-1",
    "prompt": "At presynaptic nerve terminals, the tight spatial clustering of the reserve synaptic vesicle pool into condensed clusters is mediated by:",
    "options": [
      "Liquid-liquid phase separation (LLPS) of synapsin-1 and its interaction with lipid membranes and actin filaments",
      "Covalent transglutaminase crosslinking of synaptobrevin-2",
      "Rigid clathrin cage lattices encapsulating hundreds of vesicles",
      "Direct attachment to mitochondrial cristae junctions"
    ],
    "answer": 0,
    "explain": "Synapsin-1 possesses an intrinsically disordered C-terminal region that undergoes liquid-liquid phase separation (LLPS), forming condensed liquid droplets that capture synaptic vesicles through multivalent lipid and protein interactions, organizing the reserve vesicle pool.",
    "example": "Action potential-evoked Ca2+ influx activates CaMKII, which phosphorylates synapsin-1, dissolving the liquid condensate and releasing vesicles to the active zone.",
    "id": "bc-142",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Bioenergetic Vulnerability of Substantia Nigra Axons",
    "prompt": "Midbrain dopaminergic neurons in the substantia nigra pars compacta exhibit extreme selective vulnerability to bioenergetic failure compared to VTA neurons because:",
    "options": [
      "They possess massive, unmyelinated, highly complex axonal arborizations with up to 1-2 million synaptic release sites, placing massive basal demands on mitochondrial ATP and Ca2+ buffering",
      "They have no mitochondria in their axons",
      "They consume zero glucose and rely exclusively on extracellular lactate",
      "They express no superoxide dismutase enzymes"
    ],
    "answer": 0,
    "explain": "Single human substantia nigra dopamine neurons project over 4 meters of total axonal length with ~1-2.4 million synapses. Maintaining action potential propagation across this massive unmyelinated axonal arbor, coupled with continuous autonomous pacemaking and Ca2+ influx via Cav1.3 channels, pushes their mitochondria to the brink of metabolic exhaustion.",
    "example": "VTA dopaminergic neurons have significantly smaller axonal arbors and lower Cav1.3-mediated Ca2+ loads, explaining their relative sparing in Parkinson's disease.",
    "id": "bc-143",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "GABAA Receptor Beta-Arrestin Independent Desensitization",
    "prompt": "Rapid desensitization of alpha1-beta2-gamma2 GABAA receptors during sustained millimolar GABA application is biophysically dictated by:",
    "options": [
      "Conformational transitions in the transmembrane channel pore that close the channel while agonists remain bound to the extracellular binding pocket",
      "Endocytosis mediated by clathrin and AP-2",
      "Hydrolysis of GABA into glutamate inside the synaptic cleft",
      "Phosphorylation of the channel by protein kinase C"
    ],
    "answer": 0,
    "explain": "Desensitization of pentameric ligand-gated ion channels is an intrinsic biophysical gating transition: following channel opening, the pore transitions into a long-lived closed, non-conducting state with high agonist affinity, preventing continuous depolarization or hyperpolarization.",
    "example": "Mutations at the intracellular vestibule of GABAA receptor beta subunits alter desensitization kinetics, causing familial idiopathic epilepsy.",
    "id": "bc-144",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Lipid Droplets in Reactive Astrocytes and Glia",
    "prompt": "Under conditions of severe neuronal oxidative stress and mitochondrial dysfunction, neurons transfer toxic peroxidated fatty acids to nearby astrocytes via:",
    "options": [
      "Apolipoprotein E (ApoE) and ApoD particles, where astrocytes store the lipids in protective lipid droplets for subsequent beta-oxidation",
      "Direct diffusion through gap junctions",
      "Exocytosis of naked lipid crystals into the cerebrospinal fluid",
      "Retrograde transport along the corticospinal tract"
    ],
    "answer": 0,
    "explain": "Hyperactive neurons produce excessive toxic peroxidated lipids that they cannot safely store or oxidize. Neurons export these lipids on ApoE/ApoD particles; neighboring astrocytes internalize them via LRP1 and store them as triacylglycerol inside cytoplasmic lipid droplets, shielding neurons from lipotoxicity.",
    "example": "Astrocytes carrying the ApoE4 allele fail to properly form lipid droplets, exacerbating neuronal death in neurodegenerative models.",
    "id": "bc-145",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Microglial Hexokinase 2 and Neuroinflammation",
    "prompt": "Upon microglial inflammatory activation by lipopolysaccharide (LPS) or aggregated A-beta, microglia undergo a metabolic shift from oxidative phosphorylation to aerobic glycolysis driven by:",
    "options": [
      "Induction of Hexokinase 2 (HK2) and its translocation to the outer mitochondrial membrane via VDAC binding",
      "Total degradation of all cellular mitochondria",
      "Direct inhibition of phosphofructokinase-1",
      "Switching from glucose consumption to exclusive reliance on glutamine"
    ],
    "answer": 0,
    "explain": "Pro-inflammatory polarization (M1-like) triggers up-regulation of HK2, which binds to outer mitochondrial VDAC. This couples glycolysis directly to mitochondrial ATP export, driving rapid ATP synthesis and generating glycolytic intermediates needed for cytokine synthesis and ROS production via NADPH oxidase.",
    "example": "Dissociating HK2 from VDAC using peptide inhibitors attenuates microglial pro-inflammatory cytokine release and prevents neuroinflammation.",
    "id": "bc-146",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Endogenous Opioid Peptide Processing and Dynorphin",
    "prompt": "Prodynorphin is processed by proprotein convertases to yield Dynorphin A and Dynorphin B, which exhibit selective agonist activity at which opioid receptor subtype?",
    "options": [
      "Kappa-opioid receptor (KOR)",
      "Mu-opioid receptor (MOR)",
      "Delta-opioid receptor (DOR)",
      "Nociceptin/Orphanin FQ receptor (NOP)"
    ],
    "answer": 0,
    "explain": "Dynorphins are endogenous opioid peptides derived from prodynorphin that display nanomolar selectivity and high efficacy at the Gi/o-coupled kappa-opioid receptor (KOR). KOR activation suppresses dopamine release in the nucleus accumbens, mediating dysphoria and anhedonia.",
    "example": "KOR antagonists are under clinical investigation as novel rapid-acting antidepressants that block stress-induced anhedonia.",
    "id": "bc-147",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Cerebellar Purkinje Cell Inositol Monophosphatase",
    "prompt": "Inositol monophosphatase (IMPase) is a key enzyme in the phosphoinositide recycling pathway that is therapeutically inhibited at uncompetitive therapeutic concentrations by:",
    "options": [
      "Lithium ions (Li+)",
      "Sodium valproate",
      "Carbamazepine",
      "Lamotrigine"
    ],
    "answer": 0,
    "explain": "Lithium inhibits IMPase uncompetitively by displacing magnesium (Mg2+) from the enzyme active site. This traps inositol monophosphate, depleting free myo-inositol pools and dampening overactive Gq/PLC/PIP2 signaling in manic-depressive disorder (the 'inositol depletion hypothesis').",
    "example": "Myo-inositol supplementation reverses lithium's therapeutic dampening of synaptic phosphoinositide signaling.",
    "id": "bc-148",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Optogenetic Control of cAMP with bPAC",
    "prompt": "In molecular neurobiology, photoactivated adenylyl cyclase (bPAC from Beggiatoa) allows spatiotemporal manipulation of neuronal signaling by:",
    "options": [
      "Directly synthesizing cyclic AMP upon exposure to blue light (450-480 nm) with high quantum yield and minimal dark background activity",
      "Opening a light-gated sodium channel to trigger action potentials",
      "Degrading cGMP into 5'-GMP in response to red light",
      "Phosphorylating CREB in the nucleus without second messengers"
    ],
    "answer": 0,
    "explain": "bPAC is a tiny, flavin-containing photoprotein that combines a BLUF (blue-light sensor using FAD) domain with a class III adenylyl cyclase domain. Illumination with blue light triggers rapid catalytic synthesis of cAMP from ATP, allowing precise optical control of PKA signaling in axons and spines.",
    "example": "Expressing bPAC in hippocampal presynaptic terminals demonstrated that localized cAMP pulses acutely enhance synaptic vesicle priming and transmitter release probability.",
    "id": "bc-149",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Sialylation and PSA-NCAM in Synaptic Plasticity",
    "prompt": "Polysialic acid (PSA) attached to the neural cell adhesion molecule (NCAM) promotes structural plasticity and cell migration in the adult hippocampus because:",
    "options": [
      "Its massive, negatively charged alpha-2,8-linked sialic acid chains generate steric hindrance and electrostatic repulsion between adjacent cell membranes",
      "It forms covalent crosslinks between pre- and post-synaptic densities",
      "It binds directly to the glutamate recognition site of AMPA receptors",
      "It is degraded by calpain to lock synapses in a rigid permanent conformation"
    ],
    "answer": 0,
    "explain": "Polysialyltransferases (ST8SiaII and ST8SiaIV) add long polymers of negatively charged sialic acid (PSA) to NCAM. The huge hydration volume and negative charge physically prevent close membrane apposition, keeping synapses flexible for remodeling during LTP and adult neurogenesis.",
    "example": "Enzymatic cleavage of PSA with endoneuraminidase-N (Endo-N) impairs hippocampal LTP and disrupts spatial learning in Morris water maze trials.",
    "id": "bc-150",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Nicotinamide Phosphoribosyltransferase (NAMPT) in Brain NAD+ Salvage",
    "prompt": "Neuronal NAD+ levels are maintained primarily by the NAD+ salvage pathway, wherein which rate-limiting enzyme converts nicotinamide and PRPP into nicotinamide mononucleotide (NMN)?",
    "options": [
      "Nicotinamide phosphoribosyltransferase (NAMPT)",
      "NMN adenylyltransferase 1 (NMNAT1)",
      "Nicotinic acid phosphoribosyltransferase (NAPRT)",
      "Poly(ADP-ribose) glycohydrolase (PARG)"
    ],
    "answer": 0,
    "explain": "NAMPT is the rate-limiting enzyme of the NAD+ salvage pathway. It synthesizes NMN from nicotinamide and phosphoribosyl pyrophosphate (PRPP). NMN is subsequently adenylated to NAD+ by NMNAT enzymes, replenishing NAD+ consumed by PARPs, sirtuins (SIRT1-3), and SARM1.",
    "example": "FK866 is a potent, selective inhibitor of NAMPT that depletes neuronal NAD+ and triggers axonal degeneration mimicking Wallerian degeneration.",
    "id": "bc-151",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "SARM1 as an Executioner of Axon Degeneration",
    "prompt": "Following axonal injury or NMNAT2 depletion, the sterile alpha and TIR motif-containing 1 (SARM1) protein executes Wallerian axon self-destruction by:",
    "options": [
      "Activating its intrinsic NADase domain to hydrolyze massive quantities of NAD+ into nicotinamide and cADPR, causing rapid bioenergetic collapse",
      "Phosphorylating neurofilaments to dissolve the axon skeleton",
      "Directly cleaving microtubule-associated motor protein kinesin",
      "Opening the mitochondrial permeability transition pore directly"
    ],
    "answer": 0,
    "explain": "In healthy axons, NMNAT2 keeps the NMN/NAD+ ratio low. Axonal injury or transport failure causes rapid loss of labile NMNAT2, leading to NMN accumulation. NMN binds the auto-inhibitory ARM domain of SARM1, activating its TIR domain to catabolize NAD+ with extreme catalytic speed.",
    "example": "Genetic knockout of Sarm1 allows transected distal axons to survive intact and functionally viable for weeks post-axotomy.",
    "id": "bc-152",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Ketone Body Epigenetics: beta-Hydroxybutyrate as HDAC Inhibitor",
    "prompt": "Beyond serving as an alternative mitochondrial fuel, beta-hydroxybutyrate (beta-HB) directly modulates neural gene expression by acting at physiological millimolar concentrations as:",
    "options": [
      "An endogenous competitive inhibitor of Class I and IIa histone deacetylases (HDACs)",
      "A DNA methyltransferase co-activator",
      "A ligand for nuclear estrogen receptors",
      "An inhibitor of RNA polymerase II elongation"
    ],
    "answer": 0,
    "explain": "beta-HB acts as an endogenous HDAC inhibitor (IC50 ~2-5 mM) targeting HDAC1, HDAC2, and HDAC3. Treatment with beta-HB increases global histone acetylation at histone H3 Lys9 and Lys14, driving transcription of FoxO3a, catalase, and BDNF.",
    "example": "Fasting and ketogenic diets elevate cortical beta-HB to millimolar levels, conferring resistance to oxidative stress and promoting neuroprotection.",
    "id": "bc-153",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM Structure of Active 5-HT2A-Gq Complex",
    "prompt": "High-resolution cryo-electron microscopy of the human 5-HT2A receptor bound to psychedelic agonists (such as psilocin or 25-CN-NBOH) and heterotrimeric Gq revealed that canonical activation is characterized by:",
    "options": [
      "An outward displacement of the intracellular end of transmembrane helix 6 (TM6) by ~14 Å to accommodate the C-terminal alpha5 helix of Galpha-q",
      "Total collapse of transmembrane helix 3 into an unfolded loop",
      "Dimerization of two 5-HT2A receptors via their extracellular N-termini",
      "Inward pinching of TM6 that traps GDP in the active site"
    ],
    "answer": 0,
    "explain": "Agonist binding in the orthosteric pocket triggers rotamer shifts in conserved microswitches (CWxP in TM6, DRY in TM3, and NPxxY in TM7), driving a large 14 Å outward swing of TM6. This opens a hydrophobic intracellular cavity into which the C-terminal alpha5 helix of Galpha-q docks.",
    "example": "Biased 5-HT2A ligands that stabilize distinct conformations of TM6 and intracellular loop 3 can activate Gq without recruiting beta-arrestin2, isolating therapeutic anti-depressive plasticity from adverse halluncinatory effects.",
    "id": "bc-154",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "13C-MRS Flux Quantification of Glutamate-Glutamine Cycling",
    "prompt": "In vivo 13C magnetic resonance spectroscopy (13C-MRS) using intravenous infusions of [1-13C]glucose and [2-13C]acetate allows non-invasive quantification of the neuronal-astrocytic glutamate-glutamine cycling rate (V_cyc) because:",
    "options": [
      "[2-13C]acetate is selectively taken up and metabolized exclusively by astrocytes via acetyl-CoA synthetase 1, labeling glutamine before glutamate",
      "Neurons cannot metabolize glucose under magnetic fields",
      "Acetate is converted exclusively to GABA in inhibitory interneurons",
      "[1-13C]glucose is transported exclusively across pericyte membranes"
    ],
    "answer": 0,
    "explain": "Astrocytes possess monocarboxylate transporter 1 (MCT1) and acetyl-CoA synthetase 1 (ACSS1), allowing them to selectively utilize acetate, whereas neurons cannot. Infusing [2-13C]acetate labels astrocytic glutamine C4, which is then transferred to neurons and converted to glutamate C4 at rate V_cyc.",
    "example": "Human 13C-MRS studies revealed that the rate of glutamate-glutamine cycling (V_cyc) is directly coupled to neuronal oxidative glucose consumption (V_tca_n) across varying cognitive and anaesthetic states.",
    "id": "bc-155",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Single-Molecule FRET of GPCR Conformational Landscapes",
    "prompt": "Single-molecule fluorescence resonance energy transfer (smFRET) experiments on detergent-solubilized and nanodisc-reconstituted beta2-adrenergic and opioid receptors have established that:",
    "options": [
      "GPCRs sample multiple pre-existing, dynamically interconverting conformational states, and agonists act through conformational selection by shifting the equilibrium toward the active state",
      "Receptors are entirely rigid static structures until an agonist acts as an enzymatic hammer to bend the helices",
      "Receptor activation involves irreversible proteolytic cleavage of the extracellular loop 2",
      "G-proteins are covalently tethered to the receptor at all times"
    ],
    "answer": 0,
    "explain": "smFRET tracks real-time distances between fluorophores attached to TM6 and TM3/TM4. Receptors exist in dynamic equilibrium between at least four conformational substates. Agonists do not induce a single rigid state but bias the conformational landscape toward active substates that can bind G-proteins.",
    "example": "Partial agonists fail to fully stabilize the active substate, spending more time in intermediate conformations, explaining their lower intrinsic efficacy in electrophysiological assays.",
    "id": "bc-156",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Molecular Architecture of Synaptic Vesicle Proteome",
    "prompt": "In the landmark quantitative molecular model of the average synaptic vesicle by Takamori et al. (2006), approximately what number of Vesicular Glutamate Transporters (VGLUTs) and V-ATPase complexes are present per individual vesicle?",
    "options": [
      "Approximately 8-10 VGLUT transporters and only 1-2 V-ATPase complexes",
      "Over 500 VGLUT transporters and 50 V-ATPases",
      "Exactly 1 VGLUT transporter and zero V-ATPases",
      "V-ATPases are only present in mitochondria, not on synaptic vesicles"
    ],
    "answer": 0,
    "explain": "Quantitative mass spectrometry and immunoblotting demonstrated that each 42 nm synaptic vesicle carries ~1-2 copies of the huge multi-subunit V-ATPase (sufficient to acidify the tiny vesicle lumen within milliseconds) and an average of 9-10 VGLUT molecules, along with ~70 synaptobrevin-2 molecules.",
    "example": "Because each vesicle has only 1-2 V-ATPases, pharmacological inhibition of a single V-ATPase molecule with bafilomycin completely inactivates that vesicle's refilling capability.",
    "id": "bc-157",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of Mammalian Respirasome (Supercomplex I1-III2-IV1)",
    "prompt": "Cryo-EM reconstructions of the intact mammalian brain mitochondrial respirasome (Complex I1-III2-IV1 supercomplex) revealed that physical assembly of respiratory complexes functions primarily to:",
    "options": [
      "Enable substrate channeling of ubiquinol and cytochrome c, minimizing diffusion distances and limiting electron leakage to prevent superoxide generation",
      "Prevent protons from entering the intermembrane space",
      "Trap molecular oxygen inside the inner membrane lipid core",
      "Facilitate the direct phosphorylation of Complex II by PKA"
    ],
    "answer": 0,
    "explain": "In the respirasome, Complex I, a Complex III dimer, and Complex IV form a tightly packed supramolecular entity bridged by cardiolipin. This architecture optimizes ubiquinol and cytochrome c channeling, enhances electron transport kinetics, and suppresses ROS generation.",
    "example": "Disassembly of brain respirasomes is an early biochemical hallmark in models of Alzheimer's disease and complex-I-linked mitochondrial encephalomyopathies.",
    "id": "bc-158",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Allosteric Regulation of Serine Racemase by PIP2",
    "prompt": "Biophysical and crystallographic analysis of brain Serine Racemase (SR) demonstrated that its catalytic activity is suppressed in basal states by which membrane-associated mechanism?",
    "options": [
      "Direct electrostatic binding to membrane phosphatidylinositol 4,5-bisphosphate (PIP2), which holds the enzyme in an inactive open conformation until receptor-mediated PIP2 hydrolysis releases it",
      "Covalent phosphorylation by PKA that targets it for lysosomal destruction",
      "Binding to mitochondrial cardiolipin",
      "Irreversible S-nitrosylation at Cys28"
    ],
    "answer": 0,
    "explain": "Serine racemase binds directly to PIP2 in the plasma membrane via basic residues, holding it in an inactive conformation. When Gq-coupled receptors activate PLCbeta to hydrolyze PIP2, SR is released into the cytosol, where ATP and Ca2+ bind to allosterically stimulate D-serine production.",
    "example": "Mutating the PIP2-binding basic motif of serine racemase constitutively disinhibits the enzyme, dramatically elevating baseline synaptic D-serine concentrations.",
    "id": "bc-159",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Structural Basis of GluN2B Selectivity by Ifenprodil",
    "prompt": "High-resolution crystal and cryo-EM structures of NMDA receptors demonstrated that the negative allosteric modulator ifenprodil achieves absolute subunit selectivity for GluN2B over GluN2A by binding to:",
    "options": [
      "A non-symmetric heterodimeric cleft formed between the amino-terminal domains (ATD) of GluN1 and GluN2B, stabilizing an inactive clamshell-closed ATD conformation",
      "The glutamate-binding pocket within the S1-S2 ligand binding core of GluN2B",
      "The intracellular carboxyl-terminal domain",
      "The channel pore vestibule directly adjacent to the Asn616 magnesium-coordinating residue"
    ],
    "answer": 0,
    "explain": "Ifenprodil binds specifically at the heterodimeric interface between the amino-terminal domains (ATDs) of GluN1 and GluN2B. GluN2A has distinct ATD surface residues that sterically clash with ifenprodil, conferring >400-fold pharmacological selectivity for GluN2B.",
    "example": "Structure-guided medicinal chemistry utilized this ATD dimer interface to develop orally bioavailable GluN2B-selective antagonists like traxoprodil (CP-101,606).",
    "id": "bc-160",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of Human CHT1 Choline Transporter",
    "prompt": "Cryo-electron microscopy structures of human high-affinity choline transporter CHT1 (SLC5A7) in complex with the clinical inhibitor hemicholinium-3 revealed that transport involves:",
    "options": [
      "A conserved LeuT-fold with 10 core transmembrane helices, where hemicholinium-3 occupies the central substrate binding site and locks the transporter in an outward-open conformation",
      "A 14-helix elevator mechanism similar to EAAT transporters",
      "A single continuous pore that spans the membrane without gating",
      "A tetrameric ring arrangement that conducts free choline alongside water"
    ],
    "answer": 0,
    "explain": "CHT1 belongs to the solute carrier 5 (SLC5) family sharing an inverted-repeat LeuT-like fold. Hemicholinium-3 binds at the central sodium- and choline-coordinating pocket, acting as a competitive inhibitor that blocks inward rocking of transmembrane helices 1 and 6.",
    "example": "Human congenital myasthenic syndrome mutations mapped onto the CHT1 structure disrupt the sodium-binding Na2 site, crippling acetylcholine synthesis at motor endplates.",
    "id": "bc-161",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Mass Spectrometry Imaging (MALDI-MSI) of Brain Sulfatides",
    "prompt": "Matrix-assisted laser desorption/ionization mass spectrometry imaging (MALDI-MSI) at 5-micron spatial resolution can resolve lipid microdomains in brain tissue, demonstrating that sulfatides (sulfated galactosylceramides):",
    "options": [
      "Are localized almost exclusively to myelin sheaths and white matter tracts, displaying a dramatic and selective depletion in very early preclinical stages of Alzheimer's disease",
      "Are concentrated exclusively in the nucleolus of pyramidal neurons",
      "Are restricted entirely to the choroid plexus epithelium",
      "Are present only during fetal development and disappear completely in adults"
    ],
    "answer": 0,
    "explain": "High-spatial-resolution MALDI-MSI maps sulfatides directly on brain cryosections without extraction, demonstrating their dense concentration in myelin tracts. In early preclinical Alzheimer's, sulfatides are specifically depleted (>90% loss in grey matter) due to ApoE-mediated trafficking disruptions.",
    "example": "MALDI-MSI enables simultaneous spatial tracking of lipid peroxidation products, gangliosides, and drug distribution in stroke penumbra tissue.",
    "id": "bc-162",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Thermodynamic Non-Equilibrium in Glutamate Clearance",
    "prompt": "Biophysical calculations demonstrate that the 3 Na+ / 1 H+ / 1 K+ stoichiometry of EAAT2 allows astrocytes to maintain an extracellular-to-intracellular glutamate concentration gradient of:",
    "options": [
      "Greater than 10^5 to 10^6 fold, keeping ambient extracellular glutamate below 20-50 nanomolar to prevent excitotoxic tonic receptor desensitization",
      "Exactly 1:1, allowing passive equilibrium across the astrocytic membrane",
      "Approximately 10-fold, keeping extracellular glutamate at 100 micromolar",
      "Transporters do not maintain concentration gradients and operate by simple facilitation"
    ],
    "answer": 0,
    "explain": "Coupling the uptake of 1 glutamate anion to the co-transport of 3 Na+ and 1 H+, and the counter-transport of 1 K+, harnesses three distinct transmembrane chemical and electrical gradients, generating a theoretical concentration gradient exceeding 10^6. This keeps resting extracellular glutamate at ~20 nM, far below the activation threshold of AMPA and NMDA receptors.",
    "example": "If extracellular K+ rises to 30 mM during spreading depression, the reversal potential of EAAT2 shifts dramatically, halting clearance and causing transporter reversal.",
    "id": "bc-163",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of System xc- (SLC7A11/SLC3A2) and Erastin Binding",
    "prompt": "High-resolution cryo-EM structures of the human System xc- heterodimer in complex with the ferroptosis inducer erastin have demonstrated that erastin binds to:",
    "options": [
      "An extracellular-facing vestibule of SLC7A11, locking the transporter in an outward-open state that physically occludes the cystine binding site",
      "The cytoplasmic carboxyl terminus of SLC3A2",
      "The membrane-spanning alpha-helix of glutathione peroxidase 4",
      "The active-site heme of lipoxygenase-15"
    ],
    "answer": 0,
    "explain": "SLC7A11 possesses a classic 12-transmembrane LeuT fold linked to the SLC3A2 chaperone via a conserved inter-subunit disulfide bond. Erastin binds within the outer vestibule of SLC7A11, blocking the conformational switch needed to translocate cystine and triggering rapid intracellular cysteine depletion.",
    "example": "Mutational substitution of Phe254 within the SLC7A11 erastin-binding pocket confers resistance to erastin-induced ferroptosis without disrupting physiological cystine transport.",
    "id": "bc-164",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of GABAA Receptor Neurosteroid Binding Cavities",
    "prompt": "Cryo-EM structures of alpha1-beta3-gamma2 and alpha1-beta2-gamma2 GABAA receptors in complex with neurosteroids (e.g., pregnanolone and alphaxalone) have resolved positive allosteric binding pockets located in:",
    "options": [
      "Transmembrane inter-subunit crevices between adjacent alpha and beta subunits, and intra-subunit pockets within each alpha subunit transmembrane bundle",
      "The extracellular agonist binding pocket overlapping with the GABA binding site",
      "The intracellular M3-M4 amphipathic loop",
      "The central chloride pore vestibule directly obstructing anion flow"
    ],
    "answer": 0,
    "explain": "Cryo-EM resolves two distinct neurosteroid binding sites within the transmembrane domain: a potentiating site nestled in the lipid-facing inter-subunit crevice between alpha(+) and beta(-) subunits (where neurosteroids wedge to stabilize pore opening), and a distinct intra-subunit alpha-bundle site responsible for direct channel gating at high concentrations.",
    "example": "Mutating Gln241 within the alpha1 transmembrane domain selectively abolishes neurosteroid potentiation without altering benzodiazepine or barbiturate modulation.",
    "id": "bc-165",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Mitochondrial Permeability Transition Pore (mPTP) Molecular Core",
    "prompt": "Recent high-resolution structural and patch-clamp studies indicate that the high-conductance megachannel of the mitochondrial permeability transition pore (mPTP) forms primarily from:",
    "options": [
      "Conformational remodeling and dimerization interfaces of the F-ATP synthase (Complex V) complex, specifically involving the c-subunit ring and peripheral stalk",
      "A hexameric assembly of voltage-dependent anion channels (VDAC1-3) alone",
      "Pure lipid bicelles without any protein involvement",
      "Mitochondrial transcription factor A (TFAM) multimers"
    ],
    "answer": 0,
    "explain": "While the exact composition has sparked intense debate, cryo-EM and genetic evidence demonstrate that matrix Ca2+ and cyclophilin D bind to the peripheral stalk (OSCP subunit) of F-ATP synthase, inducing a conformational shift that converts ATP synthase dimers into a massive, non-selective channel pore.",
    "example": "Reconstitution of purified F-ATP synthase dimers into lipid bilayers yields high-conductance, Ca2+-activated channels that are blocked by cyclosporin A.",
    "id": "bc-166",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Mass Spectrometry Analysis of Brain Polysialic Acid",
    "prompt": "Direct mass spectrometric profiling and fluorometric HPLC of brain-derived polysialic acid (PSA) caps have established that functional neurodevelopmental PSA polymers consist of:",
    "options": [
      "Linear homopolymers of alpha-2,8-linked N-acetylneuraminic acid (Neu5Ac) with chain lengths exceeding 50 to 100 sialic acid residues",
      "Branched beta-1,4-linked glucose oligomers",
      "Alternating dimers of glucuronic acid and N-acetylglucosamine",
      "Sulfated chondroitin disaccharide repeats"
    ],
    "answer": 0,
    "explain": "PSA synthesized by polysialyltransferases ST8SiaII/IV consists of linear, unbranched homopolymers of alpha-2,8-linked Neu5Ac extending up to 100-200 monomers in length. The helical conformation and intense negative charge envelope of these giant polymers dictate synaptic plasticity.",
    "example": "Endo-N enzyme specifically hydrolyzes alpha-2,8-sialic acid linkages with chain lengths >5, rapidly clearing PSA from brain sections without cleaving other glycoproteins.",
    "id": "bc-167",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of Human Dopamine Transporter (DAT) in Inward-Facing State",
    "prompt": "Cryo-EM structures of the human dopamine transporter (DAT) have uncovered that transition from the outward-facing to the inward-facing state to release dopamine into the cytosol involves:",
    "options": [
      "A ~45-degree rotation and inward collapse of transmembrane helix 1a (TM1a), which breaks the cytoplasmic ionic salt bridge network and unseals the intracellular gate",
      "Unfolding of the extracellular loop 2 (EL2) into an amphipathic alpha helix",
      "Phosphorylation of every serine residue in the C-terminal tail",
      "Disassembly of the DAT homodimer into free monomers"
    ],
    "answer": 0,
    "explain": "Substrate translocation in DAT involves coordinated rocking of the bundle domain (TM1, 2, 6, 7) relative to the scaffold domain. As dopamine and sodium unbind, TM1a tilts outward away from TM6b, breaking the conserved cytoplasmic salt bridge (Arg60-Asp436 in human DAT) and opening the cytoplasmic permeation pathway.",
    "example": "Parkinson's disease-associated mutations in DAT (e.g., Arg445Trp) disrupt this intracellular network, locking the transporter in a dysfunctional inward-facing conformation that leaks cations.",
    "id": "bc-168",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Brain-Specific N-Glycosylation and Lectin Arrays",
    "prompt": "High-throughput glycomic profiling of the human brain has revealed that neuronal glycoproteins differ fundamentally from peripheral somatic glycoproteins by carrying an exceptionally high abundance of:",
    "options": [
      "Bisecting GlcNAc, core-fucosylated complex N-glycans, and high-mannose structures that regulate neurotransmitter receptor clustering at synaptic membranes",
      "Extensive poly-N-acetyllactosamine repeats with terminal sialyl-Lewis-X antigens",
      "Unbranched glucose-only oligosaccharides",
      "No N-glycosylation whatsoever due to absent oligosaccharyltransferases"
    ],
    "answer": 0,
    "explain": "Brain N-glycans feature unique structural signatures, including abundant bisecting N-acetylglucosamine (GlcNAc) added by Mgat3, core alpha-1,6-fucosylation by Fut8, and terminal sialylation. These carbohydrate trees dictate the spatial organization, stability, and mobility of AMPA, NMDA, and GABAA receptors within synaptic densities.",
    "example": "Mice lacking core fucosylation (Fut8 knockout) exhibit marked downregulation of LTP and develop severe behavioral abnormalities with schizophrenia-like endophenotypes.",
    "id": "bc-169",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Spatial Metabolomics of Cortical Layers via DESI-MS",
    "prompt": "Desorption electrospray ionization mass spectrometry (DESI-MS) imaging of mammalian neocortex at ambient atmospheric pressure has demonstrated that cortical layer IV (granular layer):",
    "options": [
      "Exhibits a distinct metabolic signature characterized by dense enrichment of creatine, ATP/ADP metabolites, and specific polyunsaturated phosphatidylethanolamines reflecting dense thalamocortical synaptic terminals",
      "Is totally devoid of all amino acids and neurotransmitters",
      "Contains solely triglycerides with no membrane phospholipids",
      "Shows identical metabolic spectra to the corpus callosum"
    ],
    "answer": 0,
    "explain": "DESI-MS imaging enables direct label-free chemical visualization of endogenous metabolites across cortical lamina. Layer IV, receiving dense thalamic projections, is intensely enriched in energy metabolites (phosphocreatine, ATP) and neurotransmitters, distinguishing it metabolically from supra- and infragranular layers.",
    "example": "DESI-MS spatial metabolomics identifies focal biochemical micro-heterogeneities and neurotransmitter depletion in seizure onset zones in resected human epilepsy tissue.",
    "id": "bc-170",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Cryo-EM of Cannabinoid CB1-Gi Signaling Complex",
    "prompt": "Cryo-EM structures of the full-length human cannabinoid receptor 1 (CB1) coupled to heterotrimeric Gi1 protein have revealed that the high potency and efficacy of synthetic cannabinoids (e.g., MDMB-Fubinaca) stem from:",
    "options": [
      "Deep insertion into a hydrophobic orthosteric pocket that stabilizes a continuous hydrophobic core (Phe200 and Trp356 'twin toggle switch'), inducing maximal outward movement of TM6",
      "Direct covalent disulfide crosslinking to the Galpha-i protein",
      "Simultaneous binding to both the orthosteric site and the extracellular N-terminus",
      "Binding exclusively to the cytoplasmic face of the receptor"
    ],
    "answer": 0,
    "explain": "High-potency synthetic cannabinoids penetrate deeply into the CB1 orthosteric binding pocket, engaging the Phe200/Trp356 'twin toggle switch'. This locks TM6 in a fully open position, explaining their 50- to 100-fold higher efficacy and life-threatening toxicity compared to partial agonist phytocannabinoid THC.",
    "example": "Structural insights into the twin toggle switch permit the rational design of peripherally restricted, pathway-biased CB1 modulators that reduce pain without causing psychoactive side effects.",
    "id": "bc-171",
    "mode": "biochemistry",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "S-Acylation (Palmitoylation) Dynamics on Synaptic Scaffold Gephyrin",
    "prompt": "At inhibitory synapses, the hexagonal lattice clustering of the master scaffold gephyrin beneath postsynaptic membranes is dynamically driven by which post-translational modification?",
    "options": [
      "Palmitoylation at Cys212 and Cys284 by the palmitoyl acyltransferase DHHC12, which recruits gephyrin to the plasma membrane and increases GABAA receptor cluster size",
      "Ubiquitination by Parkin that drives gephyrin into autophagosomes",
      "Phosphorylation by CaMKII that dissolves the gephyrin lattice into monomeric subunits",
      "Myristoylation at Gly2 by N-myristoyltransferase"
    ],
    "answer": 0,
    "explain": "Palmitoylation of gephyrin at Cys212 and Cys284 by zDHHC12 anchors gephyrin trimers to the inner leaflet of the inhibitory postsynaptic membrane, promoting gephyrin oligomerization into a sub-membranous hexagonal lattice that stabilizes synaptic GABAA and glycine receptor clusters.",
    "example": "Inhibition of gephyrin palmitoylation causes gephyrin dispersal into the cytoplasm and decreases the amplitude and frequency of miniature inhibitory postsynaptic currents (mIPSCs).",
    "id": "bc-172",
    "mode": "biochemistry",
    "type": "choice"
  }
]
