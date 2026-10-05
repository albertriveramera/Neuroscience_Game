// Neuroscience PhD Arena - NEUROBIOLOGY Question Bank (172 Curated Items)
window.C2_DATA = window.C2_DATA || {};
window.NEURO_DATA = window.C2_DATA;

window.C2_DATA.neurobiology = [
  {
    "id": "nb-001",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Resting Membrane Potential",
    "prompt": "Which ion's equilibrium potential is the predominant determinant of the resting membrane potential in typical mammalian neurons?",
    "options": [
      "Potassium (K+)",
      "Sodium (Na+)",
      "Chloride (Cl-)",
      "Calcium (Ca2+)"
    ],
    "answer": 0,
    "explain": "At rest, the neuronal membrane has far higher permeability to K+ than to other ions due to constitutively open inwardly rectifying and two-pore domain potassium channels (K2P). Consequently, the resting potential rests near the K+ equilibrium potential (-70 to -85 mV) as described by the Goldman-Hodgkin-Katz equation.",
    "example": "Pharmacological blockade of resting K+ channels causes rapid membrane depolarization toward threshold."
  },
  {
    "id": "nb-002",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Action Potential Phases",
    "prompt": "The rapid upstroke of a neuronal action potential is primarily driven by:",
    "options": [
      "Opening of voltage-gated Ca2+ channels",
      "Regenerative influx of Na+ through voltage-gated Na+ channels",
      "Inactivation of voltage-gated K+ channels",
      "Active pumping by the Na+/K+-ATPase"
    ],
    "answer": 1,
    "explain": "Depolarization beyond threshold opens voltage-gated Na+ channels (Nav), creating a positive feedback loop: Na+ enters down its electrochemical gradient, further depolarizing the membrane and recruiting additional Nav channels until inactivation occurs.",
    "example": "Application of tetrodotoxin (TTX) selectively abolishes the action potential upstroke without affecting delayed rectifying K+ currents."
  },
  {
    "id": "nb-003",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Neurotransmitter Systems",
    "prompt": "Which neurotransmitter serves as the primary fast excitatory neurotransmitter in the mammalian central nervous system?",
    "options": [
      "Acetylcholine",
      "GABA",
      "L-Glutamate",
      "Glycine"
    ],
    "answer": 2,
    "explain": "L-Glutamate mediates the vast majority of fast excitatory synaptic transmission in the brain by binding to ionotropic receptors (AMPA, NMDA, and kainate), allowing rapid cation influx.",
    "example": "Glutamate receptor antagonism with CNQX and APV blocks nearly all spontaneous excitatory postsynaptic currents in cortical slices."
  },
  {
    "id": "nb-004",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Glial Biology",
    "prompt": "Which glial cell type is responsible for forming the insulating myelin sheath around axons within the central nervous system (CNS)?",
    "options": [
      "Astrocytes",
      "Microglia",
      "Schwann cells",
      "Oligodendrocytes"
    ],
    "answer": 3,
    "explain": "Oligodendrocytes myelinate multiple axonal segments in the CNS, whereas Schwann cells myelinate single axon segments in the peripheral nervous system (PNS).",
    "example": "Demyelination of central axons by autoimmune attack on oligodendrocytes is the hallmark of multiple sclerosis."
  },
  {
    "id": "nb-005",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Refractory Period",
    "prompt": "The absolute refractory period of an axon is primarily caused by:",
    "options": [
      "Complete inactivation of voltage-gated Na+ channels",
      "Deactivation of delayed rectifier K+ channels",
      "Exhaustion of intracellular ATP supplies",
      "Hyperpolarization driven by Cl- influx"
    ],
    "answer": 0,
    "explain": "During the absolute refractory period, voltage-gated Na+ channels reside in a non-conducting inactivated state (the 'ball-and-chain' or IFM motif blocked pore) and cannot reopen until the membrane repolarizes to negative potentials.",
    "example": "Regardless of stimulus intensity, a second action potential cannot be elicited during the absolute refractory period."
  },
  {
    "id": "nb-006",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Electrical Synapses",
    "prompt": "Unlike chemical synapses, electrical synapses transmit signals across specialized intercellular channels composed of:",
    "options": [
      "Cadherin complexes",
      "Connexin hemichannels (gap junctions)",
      "Integrin heterodimers",
      "Claudin tight junctions"
    ],
    "answer": 1,
    "explain": "Electrical synapses consist of gap junctions formed by hexameric connexin hemichannels that dock across the intercellular space, allowing bidirectional passive diffusion of ions and small second messengers with virtually zero synaptic delay.",
    "example": "Connexin-36 (Cx36) knockout mice show impaired electrical coupling and synchronized gamma firing across cortical interneuron networks."
  },
  {
    "id": "nb-007",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Inhibitory Neurotransmission",
    "prompt": "GABA-A receptors operate as ligand-gated ion channels selective for:",
    "options": [
      "Sodium (Na+)",
      "Potassium (K+)",
      "Chloride (Cl-)",
      "Calcium (Ca2+)"
    ],
    "answer": 2,
    "explain": "GABA-A receptors are pentameric ligand-gated anion channels permeable to Cl- (and to a lesser extent HCO3-). In mature neurons where intracellular Cl- is kept low by KCC2, GABA-A opening hyperpolarizes or shunts the membrane.",
    "example": "Bicuculline blocks GABA-A receptors, eliminating inhibitory postsynaptic currents and precipitating epileptiform burst firing."
  },
  {
    "id": "nb-008",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Neurotransmitter Clearance",
    "prompt": "What is the primary mechanism by which acetylcholine is eliminated from the synaptic cleft?",
    "options": [
      "Retrograde endocytosis into synaptic vesicles",
      "Reuptake via presynaptic sodium-dependent transporters",
      "Astroglial pinocytosis",
      "Enzymatic hydrolysis by acetylcholinesterase"
    ],
    "answer": 3,
    "explain": "Unlike monoamines and glutamate, which rely on secondary active reuptake transporters, acetylcholine is rapidly broken down in the synaptic cleft into choline and acetate by acetylcholinesterase (AChE).",
    "example": "Organophosphate pesticides irreversibly inhibit acetylcholinesterase, leading to toxic cholinergic hyperstimulation."
  },
  {
    "id": "nb-009",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "NMDA Receptor Biophysics",
    "prompt": "At hyperpolarized resting potentials (-70 mV), the NMDA receptor channel is blocked by extracellular:",
    "options": [
      "Magnesium (Mg2+)",
      "Zinc (Zn2+)",
      "Cadmium (Cd2+)",
      "Barium (Ba2+)"
    ],
    "answer": 0,
    "explain": "At resting membrane potentials, hydrated Mg2+ ions enter the outer vestibule of the NMDA receptor pore and become lodged, physically blocking current. Membrane depolarization relieves this block by electrostatically repelling Mg2+ from the pore.",
    "example": "Recording NMDAR currents in a Mg2+-free bath solution unmasks large inward currents even at -70 mV upon glutamate application."
  },
  {
    "id": "nb-010",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "AMPA Receptor Subunit Composition",
    "prompt": "Calcium permeability of AMPA receptors is determined by post-transcriptional RNA editing of which subunit?",
    "options": [
      "GluA1",
      "GluA2",
      "GluA3",
      "GluA4"
    ],
    "answer": 1,
    "explain": "ADAR2-mediated Q/R site editing of the GluA2 subunit converts a glutamine (Q) codon to an arginine (R) codon in the channel pore. The positive charge of arginine repels Ca2+, rendering GluA2(R)-containing AMPA receptors virtually Ca2+-impermeable.",
    "example": "GluA2 knockout mice or mice expressing unedited GluA2(Q) show markedly enhanced Ca2+ influx and increased vulnerability to excitotoxicity."
  },
  {
    "id": "nb-011",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "SNARE-Mediated Exocytosis",
    "prompt": "Which protein acts as the primary low-affinity calcium sensor triggering synchronous synaptic vesicle exocytosis?",
    "options": [
      "Synaptobrevin-2 (VAMP2)",
      "Syntaxin-1",
      "Synaptotagmin-1",
      "Complexin"
    ],
    "answer": 2,
    "explain": "Synaptotagmin-1 contains two C2 domains (C2A and C2B) that bind multiple Ca2+ ions cooperatively. Ca2+ binding induces partial insertion into the plasma membrane, cooperating with SNARE complexes to drive bilayer fusion.",
    "example": "Synaptotagmin-1 knockout neurons lose fast synchronous release while maintaining slow asynchronous exocytosis."
  },
  {
    "id": "nb-012",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "Passive Cable Properties",
    "prompt": "The length constant (lambda) of a dendrite increases if:",
    "options": [
      "Dendritic diameter becomes infinitely narrow",
      "Internal axial resistance increases and membrane resistance decreases",
      "Membrane capacitance increases",
      "Membrane resistance increases and internal axial resistance decreases"
    ],
    "answer": 3,
    "explain": "The length constant is defined as lambda = sqrt(rm / ri). Increasing membrane resistance (rm) prevents current leak, while decreasing axial resistance (ri, e.g. wider diameter) allows electrotonic signals to propagate farther along the cable.",
    "example": "Thick apical dendrites possess larger length constants than thin basal dendrites, allowing EPSPs to propagate with less attenuation."
  },
  {
    "id": "nb-013",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "Toxin Mechanisms",
    "prompt": "Tetanus toxin (TeNT) causes spastic paralysis by selectively cleaving which SNARE protein in spinal inhibitory interneurons?",
    "options": [
      "Synaptobrevin (VAMP)",
      "Syntaxin-1",
      "SNAP-25",
      "Munc18-1"
    ],
    "answer": 0,
    "explain": "Tetanus neurotoxin is retrogradely transported to spinal interneurons where its zinc-endopeptidase light chain cleaves Synaptobrevin (VAMP), blocking GABA and glycine release and causing disinhibitory spastic convulsions.",
    "example": "In contrast, Botulinum toxin serotype A (BoNT/A) cleaves SNAP-25 at peripheral neuromuscular junctions, producing flaccid paralysis."
  },
  {
    "id": "nb-014",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "Electrophysiology Configurations",
    "prompt": "In the whole-cell patch clamp configuration, what is the topological relationship between the recording pipette and the cell interior?",
    "options": [
      "The pipette tip rests against the cell surface without membrane rupture",
      "The membrane patch beneath the pipette is ruptured, creating low-resistance electrical continuity with the cytoplasm",
      "The cell membrane is pulled completely away leaving an excised inside-out patch",
      "The pipette records extracellular field potentials from the synaptic cleft"
    ],
    "answer": 1,
    "explain": "After forming a high-resistance gigaohm seal (cell-attached), brief suction ruptures the patch of membrane under the pipette tip, establishing electrical and chemical continuity between the pipette solution and the intracellular dialysate.",
    "example": "Whole-cell recordings allow measurement of total macroscopic transmembrane currents and dialyze intracellular solutes within minutes."
  },
  {
    "id": "nb-015",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "Quantal Analysis",
    "prompt": "In classic quantal analysis of synaptic transmission (Del Castillo & Katz), what does the parameter 'q' represent?",
    "options": [
      "The number of functional release sites",
      "The probability of vesicle release per action potential",
      "The postsynaptic electrical response elicited by a single vesicle of neurotransmitter",
      "The coefficient of variation of the evoked EPSC amplitude"
    ],
    "answer": 2,
    "explain": "Mean synaptic response amplitude E = n * p * q, where 'n' is the number of release sites, 'p' is release probability, and 'q' is quantal size (the postsynaptic voltage or current generated by release of a single vesicle's contents).",
    "example": "An increase in mEPSC amplitude without changes in frequency indicates an increase in quantal size (q), typically reflecting postsynaptic receptor upregulation."
  },
  {
    "id": "nb-016",
    "mode": "neurobiology",
    "level": 2,
    "type": "choice",
    "topic": "Glutamate Transporters",
    "prompt": "The primary glial glutamate transporter responsible for clearing over 90% of extracellular glutamate in the forebrain is:",
    "options": [
      "EAAT1 (GLAST)",
      "vGLUT1",
      "EAAT3 (EAAC1)",
      "EAAT2 (GLT-1)"
    ],
    "answer": 3,
    "explain": "GLT-1 (EAAT2), expressed abundantly on perisynaptic astrocytic processes, clears the overwhelming majority of synaptically released glutamate via secondary active transport coupled to 3 Na+ and 1 H+ inward / 1 K+ outward.",
    "example": "Pharmacological inhibition of GLT-1 with DHK leads to glutamate spillover, prolonged EPSCs, and excitotoxic neuronal death."
  },
  {
    "id": "nb-017",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Long-Term Potentiation (LTP) Signaling",
    "prompt": "During hippocampal CA1 LTP induction, which phosphorylation event locks CaMKII into an autonomous, Ca2+/calmodulin-independent active state?",
    "options": [
      "Thr286 autophosphorylation",
      "Ser831 phosphorylation",
      "Tyr1472 phosphorylation",
      "Ser845 phosphorylation"
    ],
    "answer": 0,
    "explain": "When Ca2+/calmodulin activates adjacent subunits within the dodecameric CaMKII holoenzyme, intersubunit autophosphorylation occurs at Thr286. This creates a steric block that prevents the autoinhibitory domain from rebinding, sustaining kinase activity even after Ca2+ levels decline.",
    "example": "Knock-in mice carrying a CaMKII T286A mutation fail to develop hippocampal LTP and display severe spatial learning deficits in the Morris water maze."
  },
  {
    "id": "nb-018",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Long-Term Depression (LTD)",
    "prompt": "Hippocampal NMDAR-dependent LTD is initiated by low, prolonged rises in intracellular Ca2+, leading preferentially to activation of:",
    "options": [
      "Protein kinase C (PKC)",
      "Protein phosphatase 2B (Calcineurin) and PP1",
      "PKA and MAP kinase",
      "PI3 kinase and Akt"
    ],
    "answer": 1,
    "explain": "Calcineurin (PP2B) has a higher affinity for Ca2+/calmodulin than CaMKII. Modest Ca2+ elevations selectively activate calcineurin, which dephosphorylates inhibitor-1, activating protein phosphatase 1 (PP1). This drives dephosphorylation and clathrin-mediated endocytosis of GluA1-containing AMPA receptors.",
    "example": "Application of the calcineurin inhibitors FK506 or cyclosporin A prevents the induction of low-frequency stimulation (LFS)-induced LTD."
  },
  {
    "id": "nb-019",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Retrograde Synaptic Plasticity",
    "prompt": "Depolarization-Induced Suppression of Inhibition (DSI) is mediated by retrograde diffusion of which lipid signaling molecule?",
    "options": [
      "Anandamide (AEA)",
      "Arachidonic acid",
      "2-Arachidonoylglycerol (2-AG)",
      "Prostaglandin E2"
    ],
    "answer": 2,
    "explain": "Postsynaptic Ca2+ influx activates phospholipase C-beta (PLCβ) and diacylglycerol lipase (DAGL), synthesizing 2-AG. 2-AG diffuses retrogradely across the synaptic cleft to bind presynaptic CB1 cannabinoid receptors, inhibiting presynaptic Ca2+ channels and suppressing GABA release.",
    "example": "Targeted genetic deletion of DAGLα in pyramidal neurons abolishes retrograde DSI while leaving baseline synaptic transmission intact."
  },
  {
    "id": "nb-020",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Cortical Interneuron Diversity",
    "prompt": "Which class of cortical GABAergic interneurons targets the perisomatic region of pyramidal cells, exhibits fast-spiking non-adapting firing, and is enclosed by perineuronal nets?",
    "options": [
      "Somatostatin-positive (SST+) Martinotti cells",
      "Vasoactive intestinal peptide-positive (VIP+) interneurons",
      "Neuropeptide Y-positive (NPY+) neurogliaform cells",
      "Parvalbumin-positive (PV+) basket cells"
    ],
    "answer": 3,
    "explain": "PV+ basket cells are fast-spiking interneurons capable of firing action potentials at >200 Hz with minimal adaptation due to Kv3 channels. They synapse on pyramidal somas and proximal dendrites, entraining local network gamma oscillations (30-80 Hz).",
    "example": "Optogenetic silencing of PV+ interneurons desynchronizes cortical pyramidal firing and disrupts behavioral sensory discrimination."
  },
  {
    "id": "nb-021",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Axon Initial Segment Architecture",
    "prompt": "Action potential generation occurs at the axon initial segment (AIS), a domain organized by which master scaffolding cytoskeletal protein?",
    "options": [
      "Ankyrin-G (AnkG)",
      "Postsynaptic density-95 (PSD-95)",
      "Gephyrin",
      "Homer-1"
    ],
    "answer": 0,
    "explain": "Ankyrin-G (encoded by ANK3) is the master organizer of the AIS. It directly tethers Nav1.6, Nav1.2, and Kcnq2/3 channels to the submembranous beta-IV spectrin/actin cytoskeleton, establishing the lowest threshold zone for action potential initiation.",
    "example": "Knockdown of Ankyrin-G abolishes AIS molecular assembly, disperses sodium channels, and causes loss of neuronal polarity."
  },
  {
    "id": "nb-022",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Astroglial Potassium Buffering",
    "prompt": "Spatial potassium buffering by astrocytes during intense neuronal firing is primarily executed by which inwardly rectifying potassium channel?",
    "options": [
      "Kir2.1",
      "Kir4.1",
      "Kir3.1 (GIRK1)",
      "KCNQ1"
    ],
    "answer": 1,
    "explain": "Kir4.1 is enriched on perisynaptic astrocytic endfeet. It takes up excess extracellular K+ released during neuronal repolarization, redistributing it through the astrocytic syncytium via gap junctions to maintain low extracellular [K+].",
    "example": "Astrocytic Kir4.1 conditional knockout mice exhibit elevated resting [K+]o, unprovoked epileptic seizures, and ataxia."
  },
  {
    "id": "nb-023",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Short-Term Plasticity",
    "prompt": "Paired-Pulse Facilitation (PPF) at a synapse is fundamentally driven by:",
    "options": [
      "Depletion of the readily releasable vesicular pool",
      "Upregulation of postsynaptic AMPA receptor single-channel conductance",
      "Residual presynaptic calcium persisting in the terminal after the first action potential",
      "Retrograde nitric oxide synthesis"
    ],
    "answer": 2,
    "explain": "When two action potentials invade a nerve terminal in rapid succession (intervals <100 ms), residual Ca2+ from the first spike sums with Ca2+ entered during the second, increasing release probability (p) for the second pulse.",
    "example": "Synapses with a low initial release probability exhibit pronounced paired-pulse facilitation, whereas high-p synapses typically show paired-pulse depression."
  },
  {
    "id": "nb-024",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Microglial Surveillance",
    "prompt": "Under physiological baseline conditions, ramified microglia continuously extend and retract motile processes to survey synaptic structures via which purinergic receptor?",
    "options": [
      "P2X7 receptor",
      "P2X4 receptor",
      "P2Y1 receptor",
      "P2Y12 receptor"
    ],
    "answer": 3,
    "explain": "The Gi-coupled P2Y12 purinergic receptor detects minute gradients of extracellular ATP/ADP leaked from active or injured synapses, directing microglial process chemotaxis toward sites of localized neuronal activity.",
    "example": "P2Y12-deficient mice show normal baseline microglial density but complete absence of directed process chemotaxis toward focal laser injury."
  },
  {
    "id": "nb-025",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Spike-Timing-Dependent Plasticity (STDP)",
    "prompt": "According to the canonical asymmetric Hebbian STDP rule in pyramidal neurons, long-term potentiation (LTP) is induced when:",
    "options": [
      "A presynaptic spike precedes a postsynaptic action potential by 10 to 20 ms",
      "A postsynaptic action potential precedes a presynaptic spike by 10 to 20 ms",
      "Presynaptic and postsynaptic action potentials fire completely out of phase by 150 ms",
      "Postsynaptic hyperpolarization precedes presynaptic bursting"
    ],
    "answer": 0,
    "explain": "When the presynaptic spike arrives 5-20 ms BEFORE the postsynaptic action potential (pre-before-post), the EPSP coincides with the backpropagating action potential (bAP). This drives maximal unblocking of NMDARs and a sharp, suprathreshold Ca2+ spike, triggering LTP.",
    "example": "Inverting the pairing sequence to post-before-pre causes submaximal Ca2+ influx that preferentially activates phosphatases, yielding LTD."
  },
  {
    "id": "nb-026",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Voltage Clamp Series Resistance",
    "prompt": "In whole-cell voltage clamp recordings, failing to compensate for high series resistance (Rs) results in:",
    "options": [
      "Artificial acceleration of current activation kinetics",
      "Significant voltage clamp errors and underestimation of rapid peak conductances",
      "Spontaneous oscillation and runaway cell depolarization",
      "False elevation of the calculated reversal potential for chloride"
    ],
    "answer": 1,
    "explain": "Series resistance introduces an uncompensated voltage drop (V_error = I * Rs) between the pipette electrode and the cell interior. For large currents (e.g. Nav currents of several nA), the actual membrane potential deviates substantially from the command voltage, distorting kinetics and underestimating peak conductance.",
    "example": "To minimize voltage clamp errors in biophysical channel studies, Rs is typically compensated by 70-85% electronically."
  },
  {
    "id": "nb-027",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Dopamine Receptor Signaling",
    "prompt": "In striatal medium spiny neurons (MSNs), stimulation of D1 vs D2 dopamine receptors activates which divergent G-protein cascades?",
    "options": [
      "D1 couples to G12/13 to activate RhoA; D2 couples to Gt to stimulate phosphodiesterase",
      "D1 couples to Gq to activate PLC; D2 couples to Gs to stimulate protein kinase A",
      "D1 couples to Gs/olf to activate adenylate cyclase; D2 couples to Gi/o to inhibit adenylate cyclase and open GIRK channels",
      "D1 couples to Gi to inhibit cAMP; D2 couples to Gs to elevate cAMP"
    ],
    "answer": 2,
    "explain": "D1-MSNs (direct pathway) express D1 receptors coupled to Golf/Gs, elevating cAMP, activating PKA, and phosphorylating DARPP-32 at Thr34. D2-MSNs (indirect pathway) express D2 receptors coupled to Gi/o, repressing cAMP synthesis and opening inward rectifier K+ channels (GIRK).",
    "example": "Selective optogenetic stimulation of striatal D1-MSNs initiates locomotion, whereas D2-MSN activation suppresses movement."
  },
  {
    "id": "nb-028",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Cortical Disinhibition Circuits",
    "prompt": "In cortical microcircuits, disinhibition of pyramidal neurons during behavioral arousal is predominantly achieved when:",
    "options": [
      "Microglia phagocytose GABAergic terminals on axon initial segments",
      "SST+ interneurons directly synapse onto PV+ basket cells",
      "Pyramidal cells make direct electrical connections to neurogliaform cells",
      "VIP+ interneurons selectively inhibit SST+ and PV+ interneurons"
    ],
    "answer": 3,
    "explain": "Vasoactive intestinal peptide (VIP)-expressing interneurons receive top-down cholinergic and cortical inputs. They preferentially innervate Somatostatin (SST+) Martinotti cells and PV+ interneurons, releasing pyramidal dendrites from inhibition and opening a gain window for sensory processing.",
    "example": "Two-photon calcium imaging in behaving mice shows VIP interneuron activation upon locomotion directly disinhibits visual cortex pyramidal cells."
  },
  {
    "id": "nb-029",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Developmental GABAergic Polarity Switch",
    "prompt": "During early postnatal brain development, GABA depolarizes immature neurons because intracellular chloride is maintained at high levels by:",
    "options": [
      "NKCC1 (Na+/K+/2Cl- cotransporter)",
      "KCC2 (K+/Cl- cotransporter)",
      "CLC-3 chloride channel",
      "Anion exchanger 3 (AE3)"
    ],
    "answer": 0,
    "explain": "In immature neurons, NKCC1 expression dominates over KCC2, actively pumping Cl- into the cell. Consequently, the chloride reversal potential (E_Cl) sits positive to resting membrane potential, causing Cl- efflux and depolarization upon GABA-A opening. Around P7-P14 in rodents, KCC2 is upregulated, extruding Cl- and shifting GABA to hyperpolarizing.",
    "example": "Impaired developmental upregulation of KCC2 delays the excitatory-to-inhibitory switch and is linked to neonatal epilepsy."
  },
  {
    "id": "nb-030",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Structural Plasticity Dynamics",
    "prompt": "During structural LTP (sLTP), rapid spine head enlargement requires actin filament turnover regulated by phosphorylation and inactivation of which actin-severing protein?",
    "options": [
      "Profilin",
      "Cofilin",
      "Gelsolin",
      "CapZ"
    ],
    "answer": 1,
    "explain": "NMDAR Ca2+ influx activates the RhoA/ROCK and Rac1/PAK pathways, which phosphorylate and activate LIM kinase (LIMK). LIMK phosphorylates cofilin at Ser3, inactivating its actin-severing activity and allowing Arp2/3-mediated branched F-actin stabilization in the spine head.",
    "example": "Uncaging glutamate on single dendritic spines triggers rapid spine head enlargement that fails if cofilin phosphorylation is pharmacologically blocked."
  },
  {
    "id": "nb-031",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Complement-Mediated Synaptic Pruning",
    "prompt": "During developmental remodeling of the retinogeniculate circuit, vulnerable or inactive synapses are targeted for microglial phagocytosis by which complement proteins?",
    "options": [
      "Factor B and Factor D",
      "C5a and C5b",
      "C1q and C3",
      "Mannose-binding lectin (MBL)"
    ],
    "answer": 2,
    "explain": "Classic work from Stevens and colleagues demonstrated that C1q opsonizes weaker presynaptic inputs in the dorsal lateral geniculate nucleus (dLGN), activating C3 convertase to deposit C3b. Microglia express complement receptor 3 (CR3/Mac-1) which binds C3b, triggering phagocytic engulfment of the synapse.",
    "example": "C1q or C3 knockout mice display deficient synaptic pruning, characterized by failure of retinal ganglion cell inputs to segregate into eye-specific territories."
  },
  {
    "id": "nb-032",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "Sodium Channel Subtype Segregation",
    "prompt": "At the mature myelinated axon initial segment (AIS), what is the spatial distribution of Nav1.2 versus Nav1.6 channels?",
    "options": [
      "Nav1.6 is present only in glia, while Nav1.2 occupies the entire axonal arbor",
      "Nav1.6 is strictly restricted to the soma, while Nav1.2 is clustered exclusively at nodes of Ranvier",
      "Nav1.2 and Nav1.6 are randomly and homogenously intermixed along the entire AIS",
      "Nav1.2 is enriched at the proximal AIS (near the soma), while Nav1.6 is concentrated at the distal AIS (near the first myelin sheath)"
    ],
    "answer": 3,
    "explain": "Nav1.6 has a lower activation threshold than Nav1.2. Clustered at the distal AIS, Nav1.6 initiates forward-propagating action potentials. Nav1.2, localized to the proximal AIS, facilitates backpropagation of the action potential into the soma and dendrites.",
    "example": "In Nav1.6 knockout neurons, action potential initiation shifts to more depolarized potentials and threshold current requirements increase."
  },
  {
    "id": "nb-033",
    "mode": "neurobiology",
    "level": 5,
    "type": "choice",
    "topic": "Optogenetic Channel Kinetics",
    "prompt": "Compared to wild-type Channelrhodopsin-2 (ChR2), the ultrafast engineered opsin 'Chronos' exhibits which key biophysical property enabling high-frequency spike entrainment up to 100 Hz?",
    "options": [
      "Substantially faster deactivation off-kinetics (tau_off ~3.6 ms) and higher light sensitivity",
      "Shifted red excitation spectrum into the infrared window (750 nm)",
      "Strict selectivity for chloride over monovalent cations",
      "Irreversible lock-in state upon single-photon excitation"
    ],
    "answer": 0,
    "explain": "Chronos possesses an unusually fast channel closing rate (tau_off ~3.6 ms at room temp, even faster at physiological temp) combined with high single-channel conductance. This rapid deactivation prevents plateau depolarizations and sodium channel inactivation, allowing neurons to follow light pulses at 100 Hz with high fidelity.",
    "example": "Auditory brainstem neurons expressing Chronos can be driven to fire one action potential per light pulse up to 100 Hz in vitro."
  },
  {
    "id": "nb-034",
    "mode": "neurobiology",
    "level": 5,
    "type": "choice",
    "topic": "Perineuronal Nets & Critical Periods",
    "prompt": "Perineuronal nets (PNNs) wrap parvalbumin interneurons to terminate juvenile critical periods of neuroplasticity. Enzymatic reopening of adult cortical plasticity can be achieved by injecting:",
    "options": [
      "Hyaluronidase IV",
      "Chondroitinase ABC (ChABC)",
      "Collagenase type II",
      "Neuraminidase"
    ],
    "answer": 1,
    "explain": "PNNs are specialized extracellular matrix assemblies rich in chondroitin sulfate proteoglycans (CSPGs, e.g. aggrecan) anchored by hyaluronic acid. Chondroitinase ABC enzymatically degrades the glycosaminoglycan (GAG) side chains of CSPGs, disassembling PNNs and restoring ocular dominance plasticity in adult visual cortex.",
    "example": "Pizzorusso et al. (2002) demonstrated that microinjection of ChABC into adult rat visual cortex fully reactivated ocular dominance plasticity following monocular deprivation."
  },
  {
    "id": "nb-035",
    "mode": "neurobiology",
    "level": 5,
    "type": "choice",
    "topic": "Glymphatic Clearance Dynamics",
    "prompt": "Glymphatic clearance of interstitial solutes (such as amyloid-beta) relies on polarized localization of which water channel to astrocytic vascular endfeet?",
    "options": [
      "Aquaporin-1 (AQP1)",
      "Aquaporin-9 (AQP9)",
      "Aquaporin-4 (AQP4)",
      "TRPV4"
    ],
    "answer": 2,
    "explain": "Nedergaard and colleagues showed that Aquaporin-4 (AQP4) water channels are densely clustered at astrocytic endfeet facing cerebral microvessels. This polarized expression facilitates bulk convective flow of CSF from periarterial spaces through the interstitial parenchyma into perivenous drainage routes, clearing metabolic waste during slow-wave sleep.",
    "example": "Aqp4 gene deletion or loss of AQP4 perivascular polarization in aged mice slows parenchymal clearance of radiolabeled Aβ by over 50%."
  },
  {
    "id": "nb-036",
    "mode": "neurobiology",
    "level": 5,
    "type": "choice",
    "topic": "Dendritic Spikes & Active Conductances",
    "prompt": "In Layer 5 pyramidal neurons, associative coincidence detection between feedforward sensory inputs at the basal dendrites and top-down feedback inputs at the apical tuft is mediated by:",
    "options": [
      "Backpropagating sodium action potentials that fail completely to enter apical shafts",
      "Purely passive electrotonic sum at the axon hillock without dendritic channel recruitment",
      "Inhibition of all outward K+ conductances via astrocytic glutamate release",
      "Dendritic calcium action potentials generated in the apical nexus via Cav1/Cav2 channels"
    ],
    "answer": 3,
    "explain": "Matthew Larkum discovered that when a backpropagating action potential (bAP) from the soma coincides with distal synaptic input at the apical tuft within 10-30 ms, it triggers a long-lasting, high-amplitude dendritic Ca2+ action potential at the apical nexus. This drives burst firing at the soma, serving as a cellular coincidence detector.",
    "example": "Two-photon calcium uncaging at the apical nexus directly recruits L-type Cav1 channels, converting single somatic spikes into high-frequency output bursts."
  },
  {
    "id": "nb-037",
    "mode": "neurobiology",
    "level": 5,
    "type": "choice",
    "topic": "Neuromodulatory Microcircuit Dynamics",
    "prompt": "In the prefrontal cortex, stimulation of alpha-2A noradrenergic receptors enhances working memory delay-period firing by which downstream biophysical mechanism?",
    "options": [
      "Inhibiting adenylate cyclase and cAMP, which closes nearby HCN and KCNQ channels to prevent shunting of dendritic spines",
      "Activating Gq to stimulate PLC, which uncouples PSD-95 from AMPA receptors",
      "Opening BK channels to cause rapid repolarization of somatic action potentials",
      "Directly gating Cav2.1 P/Q-type calcium channels in the soma"
    ],
    "answer": 0,
    "explain": "Amy Arnsten's laboratory demonstrated that alpha-2A adrenoceptors couple to Gi, inhibiting cAMP production. Lower cAMP reduces PKA activity, keeping hyperpolarization-activated cyclic nucleotide-gated (HCN) and KCNQ potassium channels closed. Closing these leaky channels increases input resistance and strengthens synaptic signal transmission on dendritic spines during working memory.",
    "example": "Guanfacine, an alpha-2A agonist, rescues age-related working memory deficits in aged monkeys by closing HCN channels in dorsolateral prefrontal cortex."
  },
  {
    "id": "nb-038",
    "mode": "neurobiology",
    "level": 5,
    "type": "choice",
    "topic": "Synaptic Vesicle Replenishment & Endocytosis",
    "prompt": "During sustained high-frequency synaptic transmission, clathrin-independent 'ultrafast endocytosis' retrieves vesicular membrane at physiological temperatures on what timescale?",
    "options": [
      "10 to 20 seconds through canonical clathrin-coated pits",
      "50 to 100 milliseconds at sites adjacent to the active zone",
      "3 to 5 minutes via macropinocytosis at the distal axon shaft",
      "Instantaneous kiss-and-run within 1 millisecond"
    ],
    "answer": 1,
    "explain": "Watanabe and Jorgensen discovered via flash-and-freeze electron microscopy that at physiological temperature (37°C), synaptic vesicle exocytosis is followed within 50-100 ms by ultrafast endocytosis. Large vesicles form directly at active zone lateral edges independent of clathrin, subsequently resolving into functional synaptic vesicles via endosomes.",
    "example": "Flash-and-freeze experiments reveal large invaginations forming at active zone edges 50 ms after a single optogenetic light pulse."
  },
  {
    "id": "nb-039",
    "mode": "neurobiology",
    "level": 1,
    "type": "choice",
    "topic": "Synaptic Delay",
    "prompt": "What is the typical time delay across a chemical synapse from presynaptic action potential invasion to the onset of the postsynaptic potential?",
    "options": [
      "Less than 0.01 milliseconds",
      "50 to 100 milliseconds",
      "0.5 to 2.0 milliseconds",
      "500 to 1000 milliseconds"
    ],
    "answer": 2,
    "explain": "The synaptic delay at chemical synapses is typically 0.5 to 2.0 ms, reflecting the time required for voltage-gated Ca2+ channel opening, Ca2+ microdomain influx, synaptotagmin activation, SNARE complex fusion, neurotransmitter diffusion across the ~20 nm cleft, and postsynaptic receptor gating.",
    "example": "In contrast, electrical synapses transmit current instantaneously (<0.1 ms) via direct connexin gap junctions."
  },
  {
    "id": "nb-040",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "Perisomatic vs Dendritic Inhibition",
    "prompt": "Martinotti cells in the cerebral cortex are somatostatin-positive (SST+) interneurons whose axons specifically ascend to Layer 1 to innervate:",
    "options": [
      "Myelinated nodes of Ranvier",
      "The pyramidal cell soma and axon initial segment",
      "Blood vessel pericytes directly",
      "The distal apical dendrites and tufts of pyramidal neurons"
    ],
    "answer": 3,
    "explain": "Martinotti cells provide feedback dendritic inhibition by projecting vertically to Layer 1, where their axons arborize extensively to contact the distal apical tufts of Layer 2/3 and Layer 5 pyramidal neurons, gating top-down dendritic calcium spikes.",
    "example": "Silencing Martinotti cells selectively enhances dendritic calcium spikes without altering somatic baseline threshold."
  },
  {
    "id": "nb-041",
    "mode": "neurobiology",
    "level": 3,
    "type": "choice",
    "topic": "HCN Channels and Ih Current",
    "prompt": "Hyperpolarization-activated cyclic nucleotide-gated (HCN) channels generate the inward 'Ih' pacemaker current. In cortical pyramidal dendrites, the spatial gradient of Ih density:",
    "options": [
      "Increases dramatically from soma to distal apical dendrites, acting to dampen distal EPSPs and normalize temporal summation",
      "Is concentrated exclusively at the synaptic cleft of spine heads",
      "Decreases to zero in the apical tuft",
      "Is present only in unmyelinated axons"
    ],
    "answer": 0,
    "explain": "HCN1/HCN2 channels exhibit an increasing somato-dendritic density gradient (up to 60-fold higher in distal apical dendrites of Layer 5 pyramidal neurons). The constitutively open Ih at rest lowers dendritic input resistance, accelerating EPSP decay kinetics and standardizing temporal summation across distal and proximal inputs.",
    "example": "Pharmacological blockade of Ih with ZD7288 increases dendritic input resistance and markedly broadens EPSP duration."
  },
  {
    "id": "nb-042",
    "mode": "neurobiology",
    "level": 4,
    "type": "choice",
    "topic": "GABA-B Receptor Heterodimerization",
    "prompt": "Functional metabotropic GABA-B receptors require obligate heterodimerization between which two subunits?",
    "options": [
      "GABA-A alpha-1 and GABA-A beta-2",
      "GABA-B1 (which binds GABA) and GABA-B2 (which couples to Gi/o proteins)",
      "GABA-B1a and GABA-B1b directly",
      "GABA-C and Glycine receptor alpha-1"
    ],
    "answer": 1,
    "explain": "GABA-B operates as an obligate heterodimer: GABA-B1 contains the extracellular Venus flytrap domain that binds GABA, but possesses an ER-retention motif (RXR). GABA-B2 masks this retention motif, transports the complex to the cell surface, and contains the intracellular loops that couple to Gi/o to inhibit Cav channels and open GIRK K+ channels.",
    "example": "GABA-B1 knockout mice show complete loss of all pre- and postsynaptic GABA-B-mediated responses."
  },
  {
    "level": 1,
    "topic": "Sodium-Potassium ATPase Stoichiometry",
    "prompt": "For each molecule of ATP hydrolyzed, the neuronal Na+/K+-ATPase pump translocates:",
    "options": [
      "3 Na+ ions into the cell and 3 K+ ions out of the cell",
      "2 Na+ ions out of the cell and 3 K+ ions into the cell",
      "3 Na+ ions out of the cell and 2 K+ ions into the cell",
      "1 Na+ ion out and 1 K+ ion in"
    ],
    "answer": 2,
    "explain": "The Na+/K+-ATPase is electrogenic: it pumps 3 Na+ out of the cytoplasm for every 2 K+ imported per ATP consumed, generating a net outward positive current and sustaining the physiological ion gradients.",
    "example": "Cardiac glycosides like ouabain inhibit the Na+/K+-ATPase, causing progressive intracellular Na+ accumulation and cell swelling.",
    "id": "nb-043",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Henneman's Size Principle",
    "prompt": "According to Henneman's Size Principle, during graded voluntary muscle contraction, motor units are recruited in what order?",
    "options": [
      "Simultaneously regardless of force demand",
      "From largest to smallest motor neurons",
      "In a completely random sequence",
      "From smallest motor neurons (low threshold, slow-twitch) to largest motor neurons (high threshold, fast-fatigable)"
    ],
    "answer": 3,
    "explain": "Smaller motor neurons have higher input resistance (R_in) due to their smaller surface area. According to Ohm's law (V = I * R), a given synaptic current generates a larger EPSP in small motor neurons, reaching action potential threshold first.",
    "example": "Electromyography during gentle finger movement demonstrates early recruitment of small fatigue-resistant Type I motor units.",
    "id": "nb-044",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Spatial Summation",
    "prompt": "Spatial summation of synaptic inputs occurs when:",
    "options": [
      "Multiple distinct synaptic inputs arriving simultaneously at different dendritic locations summate at the axon hillock",
      "A single presynaptic terminal fires repeatedly in rapid succession",
      "All synaptic receptors are degraded by extracellular proteases",
      "Action potentials backpropagate into dendritic spines"
    ],
    "answer": 0,
    "explain": "Spatial summation integrates electrical currents generated concurrently across disparate spatial sites on the dendritic tree as they conduct electrotonically to the spike trigger zone.",
    "example": "Simultaneous EPSPs from three separate dendritic branches combine to cross threshold at the axon initial segment.",
    "id": "nb-045",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Temporal Summation",
    "prompt": "Temporal summation occurs when successive synaptic potentials elicited at the same synapse summate because:",
    "options": [
      "The space constant is reduced to zero",
      "The inter-stimulus interval is shorter than the membrane time constant (tau)",
      "Chloride channels open irreversibly",
      "Action potentials fire at 0.1 Hz"
    ],
    "answer": 1,
    "explain": "If presynaptic action potentials arrive before the postsynaptic potential from the preceding spike has fully decayed, the new EPSP adds on top of the residual depolarization.",
    "example": "High-frequency stimulation (100 Hz) yields robust temporal summation of EPSPs, driving the membrane to firing threshold.",
    "id": "nb-046",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Tetrodotoxin Mechanism",
    "prompt": "The potent marine neurotoxin Tetrodotoxin (TTX), found in pufferfish, selectively blocks which ion channels?",
    "options": [
      "GABA-A receptors",
      "Voltage-gated potassium channels (Kv)",
      "Voltage-gated sodium channels (Nav)",
      "Nicotinic acetylcholine receptors"
    ],
    "answer": 2,
    "explain": "TTX binds with nanomolar affinity to the outer pore vestibule of TTX-sensitive voltage-gated Na+ channels (Nav1.1-1.4, Nav1.6, Nav1.7), physically occluding the ion pathway and arresting action potentials.",
    "example": "Bath application of 1 μM TTX in brain slice electrophysiology abolishes all evoked action potentials while sparing miniature EPSCs (mEPSCs).",
    "id": "nb-047",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Tetraethylammonium (TEA) Blockade",
    "prompt": "The classical pharmacological tool tetraethylammonium (TEA) blocks voltage-gated potassium channels, resulting in which effect on the action potential?",
    "options": [
      "Permanent hyperpolarization below -100 mV",
      "Immediate abolition of the initial upstroke",
      "Complete elimination of the resting membrane potential",
      "Significant broadening of the action potential duration due to slowed repolarization"
    ],
    "answer": 3,
    "explain": "TEA selectively blocks delayed rectifier potassium channels. Without outward K+ currents to repolarize the membrane, action potential repolarization is prolonged, resulting in broad action potentials.",
    "example": "Intracellular or extracellular TEA application broadens the squid giant axon action potential from 1 ms to over 10 ms.",
    "id": "nb-048",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Renshaw Cell Feedback Inhibition",
    "prompt": "In the spinal cord, Renshaw cells are inhibitory interneurons that receive excitatory collateral inputs from motor neurons and send inhibitory feedback to:",
    "options": [
      "The same alpha-motor neuron and neighboring motor neurons to prevent runaway excitation",
      "Sensory muscle spindle afferents strictly",
      "The primary sensory cortex",
      "Cerebellar Purkinje neurons"
    ],
    "answer": 0,
    "explain": "Renshaw cells provide recurrent negative feedback inhibition in the spinal cord, releasing glycine and GABA onto the alpha-motor neurons to dampen motor firing and stabilize muscle contraction.",
    "example": "Strychnine blocks glycine receptors on motor neurons, eliminating Renshaw cell inhibition and causing severe tetanic muscle spasms.",
    "id": "nb-049",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Photoreceptor Dark Current",
    "prompt": "In vertebrate rod photoreceptors, in the dark, the resting membrane potential sits around -40 mV due to a continuous inward 'dark current' carried by:",
    "options": [
      "K+ exiting through delayed rectifiers",
      "Na+ and Ca2+ entering through cGMP-gated cation channels",
      "Chloride entering via GABA-A receptors",
      "Protons entering via v-ATPase"
    ],
    "answer": 1,
    "explain": "In darkness, high constitutive levels of cyclic GMP (cGMP) keep cyclic nucleotide-gated (CNG) cation channels open, allowing an inward Na+/Ca2+ current that keeps rods depolarized (-40 mV) and tonically releasing glutamate.",
    "example": "Photon absorption by rhodopsin activates transducin and phosphodiesterase-6 (PDE6), hydrolyzing cGMP, closing CNG channels, and hyperpolarizing the photoreceptor.",
    "id": "nb-050",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Chemical Synapse Unidirectionality",
    "prompt": "Unlike gap junctions, chemical synapses enforce strictly unidirectional information transfer because:",
    "options": [
      "Phospholipid bilayers are polar",
      "Action potentials can only travel backward",
      "Neurotransmitter release machinery is localized exclusively presynaptically while receptors reside postsynaptically",
      "Synaptic clefts contain negative voltages"
    ],
    "answer": 2,
    "explain": "The structural asymmetry of the chemical synapse—vesicles and exocytic active zones on the presynaptic side, receptors on the postsynaptic density—enforces strictly polarized forward transmission.",
    "example": "Applying glutamate to a presynaptic terminal does not trigger transmitter release from the postsynaptic spine.",
    "id": "nb-051",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Equilibrium Potential for Sodium",
    "prompt": "With typical mammalian concentrations of [Na+]out ≈ 145 mM and [Na+]in ≈ 12 mM, the equilibrium potential for Na+ (E_Na) calculated via the Nernst equation at 37°C is approximately:",
    "options": [
      "-90 mV",
      "-70 mV",
      "0 mV",
      "+60 to +65 mV"
    ],
    "answer": 3,
    "explain": "E_Na = 61.5 * log10(145 / 12) ≈ +66 mV. Because resting potential is negative, the electrochemical driving force (V_m - E_Na) on sodium is massive (~-140 mV), driving rapid influx when channels open.",
    "example": "At the peak of the action potential (+30 mV), the membrane approaches but does not exceed E_Na before sodium channels inactivate.",
    "id": "nb-052",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "BK Channel Gating",
    "prompt": "Large-conductance calcium-activated potassium channels (BK channels, Maxi-K, KCa1.1) are synergistically gated by:",
    "options": [
      "Simultaneous membrane depolarization and micromolar elevations of intracellular calcium",
      "Protons and extracellular chloride",
      "Pure hyperpolarization below -90 mV",
      "ATP depletion alone"
    ],
    "answer": 0,
    "explain": "BK channels contain both voltage sensors (S4 segments) and high-affinity cytosolic Ca2+-sensing RCK domains. Binding of intracellular Ca2+ shifts the voltage-activation curve by >100 mV toward negative potentials, allowing rapid opening during action potentials to hasten repolarization.",
    "example": "Iberiotoxin selectively blocks BK channels, slowing action potential repolarization and enhancing neurotransmitter release.",
    "id": "nb-053",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "SK Channel Afterhyperpolarization",
    "prompt": "Small-conductance calcium-activated potassium channels (SK channels, KCa2.1-2.3) lack voltage sensitivity and are gated strictly by Ca2+ through constitutive association with:",
    "options": [
      "Troponin C",
      "Calmodulin (CaM)",
      "Parvalbumin",
      "Synaptotagmin-1"
    ],
    "answer": 1,
    "explain": "SK channels are voltage-independent. Calmodulin is constitutively bound to the SK C-terminal CaM-binding domain (CaMBD). Submicromolar Ca2+ binding to calmodulin triggers channel opening, generating the medium afterhyperpolarization (mAHP) that sets spike frequency adaptation.",
    "example": "Apamin, a bee venom peptide, selectively blocks SK channels, eliminating the mAHP and causing bursting activity.",
    "id": "nb-054",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Synapsin Function",
    "prompt": "Synapsin-1 tethers synaptic vesicles to the actin cytoskeleton in the reserve pool. Release of vesicles from this pool during high-frequency stimulation is triggered by:",
    "options": [
      "Direct proteolytic cleavage by caspase-3",
      "Dephosphorylation by calcineurin",
      "Phosphorylation of Synapsin-1 by PKA and CaMKII, causing its detachment from actin",
      "Ubiquitination by Parkin"
    ],
    "answer": 2,
    "explain": "Synapsin-1 crosslinks synaptic vesicles to actin filaments. Phosphorylation of Synapsin-1 at site 1 (by PKA/CaMKI) and sites 2/3 (by CaMKII) lowers its affinity for both vesicles and actin, allowing vesicles to mobilize from the reserve pool to the active zone.",
    "example": "Synapsin triple-knockout mice show severe depletion of reserve pool vesicles and rapid synaptic fatigue during prolonged stimulus trains.",
    "id": "nb-055",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Munc18-1 and Syntaxin-1 Conformation",
    "prompt": "Munc18-1 (SM protein) regulates SNARE complex assembly by binding to which conformation of syntaxin-1?",
    "options": [
      "Directly to the vesicle lumen",
      "Only to denatured syntaxin fragments",
      "Strictly to synaptobrevin",
      "The 'closed' autoinhibited conformation of syntaxin-1 to chaperone it, then stabilizing the assembled four-helix core complex"
    ],
    "answer": 3,
    "explain": "Munc18-1 binds monomeric syntaxin-1 in its closed, autoinhibited state, protecting it from non-productive aggregation. It then assists in transitioning syntaxin-1 into the open conformation during four-helix bundle assembly with SNAP-25 and synaptobrevin.",
    "example": "Munc18-1 knockout in mice results in completely paralyzed neurotransmission with total loss of all spontaneous and evoked synaptic exocytosis.",
    "id": "nb-056",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Complexin Clamp Function",
    "prompt": "The small cytosolic protein Complexin stabilizes assembled trans-SNARE complexes and regulates exocytosis by:",
    "options": [
      "Acting as a dual fusion clamp (preventing premature spontaneous fusion) and an exocytic activator upon calcium binding to synaptotagmin",
      "Degrading SNAP-25 after fusion",
      "Pumping calcium into synaptic vesicles",
      "Phosphorylating voltage-gated calcium channels"
    ],
    "answer": 0,
    "explain": "Complexin inserts an accessory alpha-helix into the grooved trans-SNARE bundle, arresting fusion immediately prior to pore opening. When Ca2+ binds synaptotagmin-1, synaptotagmin displaces complexin, allowing complete SNARE zippering and membrane fusion.",
    "example": "Knockdown of complexin elevates spontaneous miniature vesicle fusion while dramatically reducing evoked synchronous release.",
    "id": "nb-057",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Kainate Receptor Desensitization and GluK2",
    "prompt": "GluK2-containing kainate receptors differ from AMPA receptors in that their postsynaptic currents exhibit:",
    "options": [
      "Complete inability to conduct sodium",
      "Significantly slower decay kinetics and profound desensitization in the presence of continuous glutamate",
      "Strict permeability to calcium only",
      "Resistance to CNQX blockade"
    ],
    "answer": 1,
    "explain": "Kainate receptor-mediated EPSCs (e.g. at mossy fiber-CA3 synapses) exhibit characteristically slow rise and decay kinetics (decay tau ~50-100 ms vs ~5-10 ms for AMPARs), providing tonic depolarization during repetitive firing.",
    "example": "Concanavalin A (ConA) prevents kainate receptor desensitization, markedly amplifying steady-state kainate currents in patch clamp recordings.",
    "id": "nb-058",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Glycine Receptor Subunits and Gephyrin",
    "prompt": "Postsynaptic clustering of pentameric glycine receptors (composed of alpha and beta subunits) at inhibitory spinal synapses is organized by the submembranous scaffold protein:",
    "options": [
      "Homer",
      "PSD-95",
      "Gephyrin",
      "CASK"
    ],
    "answer": 2,
    "explain": "The intracellular loop of GlyR beta subunits binds with high nanomolar affinity to gephyrin. Gephyrin self-assembles into a submembranous hexagonal lattice that anchors GlyRs and GABA-A receptors directly opposite presynaptic inhibitory release sites.",
    "example": "Knockout or genetic silencing of gephyrin prevents glycine receptor clustering in the spinal cord, leading to fatal hyperekplexia.",
    "id": "nb-059",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cav2 Channel Subtypes at Presynaptic Terminals",
    "prompt": "Fast neurotransmitter exocytosis at central mammalian synapses is triggered predominantly by calcium influx through which high-voltage-activated calcium channel subtypes?",
    "options": [
      "RyR1 ryanodine channels",
      "Cav1.2 (L-type) exclusively",
      "Cav3.1 (T-type) low-voltage channels",
      "Cav2.1 (P/Q-type) and Cav2.2 (N-type)"
    ],
    "answer": 3,
    "explain": "Cav2.1 (P/Q-type, blocked by omega-agatoxin IVA) and Cav2.2 (N-type, blocked by omega-conotoxin GVIA) interact directly with active zone RIM and SNARE proteins via their synprint sites, positioning them nanometers from docked vesicles.",
    "example": "Co-application of omega-agatoxin IVA and omega-conotoxin GVIA eliminates >95% of evoked synaptic transmission at hippocampal Schaffer collateral synapses.",
    "id": "nb-060",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cav3 T-Type Calcium Channels and Burst Firing",
    "prompt": "Low-voltage-activated T-type calcium channels (Cav3.1-3.3) in thalamocortical relay neurons activate at subthreshold potentials (-65 mV) and generate:",
    "options": [
      "Low-threshold calcium spikes (LTCS) that trigger burst firing during non-REM sleep and absence seizures",
      "Fast sodium action potentials at the axon initial segment",
      "Permanent hyperpolarization",
      "Sustained outward potassium current"
    ],
    "answer": 0,
    "explain": "Cav3 channels de-inactivate upon membrane hyperpolarization (-70 mV). Subsequent mild depolarization opens them, generating a transient inward Ca2+ current that produces a low-threshold spike, riding atop which are high-frequency bursts of classic action potentials.",
    "example": "Ethosuximide, an anti-absence epilepsy drug, therapeutic efficacy stems from selective blockade of thalamic T-type Ca2+ channels.",
    "id": "nb-061",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Optogenetic Voltage Sensors (GEVIs)",
    "prompt": "Genetically encoded voltage indicators like Voltron or ASAP3 detect membrane potential changes by coupling a voltage-sensing domain (e.g. from Ciona intestinalis phosphatase) to:",
    "options": [
      "A luciferase enzyme requiring ATP",
      "A circularly permuted fluorescent protein or synthetic dye whose fluorescence changes via FRET or electrochromism",
      "An inward chloride pump",
      "A sodium-dependent channel"
    ],
    "answer": 1,
    "explain": "GEVIs convert sub-millisecond transmembrane electrical fluctuations into optical signals: S4 voltage-sensor movement alters the chromophore environment or modulates FRET/quenching to a synthetic fluorophore (e.g. Voltron with Janelia Fluor dyes).",
    "example": "In vivo imaging with Voltron allows optical recording of individual action potentials and subthreshold EPSPs from cortical neurons in behaving animals.",
    "id": "nb-062",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "CaMKII Dodecameric Structure and Autoinhibition",
    "prompt": "In basal conditions, CaMKII activity is suppressed because its regulatory domain autoinhibitory segment:",
    "options": [
      "Pumps calcium into the ER",
      "Degrades the catalytic subunit",
      "Sterically blocks the catalytic substrate-binding pocket (S-site and T-site)",
      "Binds covalently to actin"
    ],
    "answer": 2,
    "explain": "In the basal resting state, the pseudosubstrate region of CaMKII's regulatory domain binds its own catalytic core, obstructing ATP and substrate access. Binding of Ca2+/calmodulin pulls the regulatory domain away, unmasking the catalytic pocket and exposing Thr286 for autophosphorylation.",
    "example": "Mutating Thr286 to aspartate (T286D) mimics phosphorylation, creating a constitutively active kinase that occludes further LTP induction.",
    "id": "nb-063",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Silent Synapse Maturation",
    "prompt": "'Silent synapses' in the developing neonatal brain are functionally silent at resting membrane potentials (-70 mV) because they contain:",
    "options": [
      "No postsynaptic density proteins whatsoever",
      "AMPA receptors but lack NMDA receptors",
      "Only GABA-A receptors",
      "Postsynaptic NMDA receptors but lack functional AMPA receptors"
    ],
    "answer": 3,
    "explain": "At resting membrane potentials (-70 mV), NMDA receptors are blocked by Mg2+. Because silent synapses lack AMPA receptors, presynaptic glutamate release generates zero postsynaptic current. Depolarization during LTP unblocks NMDARs, recruiting AMPA receptors into the synapse ('unsilencing').",
    "example": "Liao, Malenka, and Malinow demonstrated that pairing presynaptic stimulation with postsynaptic depolarization (-70 to 0 mV) unsilences transmission by driving AMPAR exocytosis.",
    "id": "nb-064",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "mGluR-Dependent LTD Signaling",
    "prompt": "Group I metabotropic glutamate receptor-dependent LTD (mGluR-LTD) in the hippocampus requires rapid, local dendritic translation of:",
    "options": [
      "Arc/Arg3.1 and MAP1B, which promote dynamin-dependent endocytosis of AMPA receptors",
      "CaMKII alpha exclusively",
      "Sodium channels Nav1.2",
      "Histone H3"
    ],
    "answer": 0,
    "explain": "Stimulation of mGluR1/5 triggers Gq-mediated ERK1/2 and mTOR signaling that stimulates local dendritic translation of pre-existing mRNAs, including Arc (Activity-Regulated Cytoskeleton-Associated Protein). Arc binds dynamin and endophilin, accelerating endocytosis of GluA1/GluA2 AMPARs.",
    "example": "Application of protein synthesis inhibitors (cycloheximide or anisomycin) to dendritic layers blocks mGluR-LTD without affecting NMDAR-dependent LTD.",
    "id": "nb-065",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Homeostatic Synaptic Scaling",
    "prompt": "Chronic pharmacological silencing of neuronal activity with TTX for 48 hours induces homeostatic synaptic scaling up, characterized by:",
    "options": [
      "Linear reduction in mEPSC frequency only",
      "Multiplicative upregulation of all miniature EPSC (mEPSC) amplitudes across all synapses via postsynaptic AMPAR accumulation",
      "Complete elimination of all dendritic spines",
      "Conversion of excitatory synapses into inhibitory GABAergic junctions"
    ],
    "answer": 1,
    "explain": "Turrigiano et al. discovered that prolonged inactivity causes neurons to multiplicatively scale up the strength of all excitatory synapses by recruiting GluA1- and GluA2-containing AMPARs (mediated by TNF-alpha and beta3 integrins), preserving relative synaptic weights while restoring target firing rates.",
    "example": "Plotting rank-ordered mEPSC amplitudes before and after TTX demonstrates true multiplicative scaling: post-TTX amplitudes equal pre-TTX amplitudes multiplied by a constant scaling factor.",
    "id": "nb-066",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Cerebellar Mossy Fiber vs Climbing Fiber Architecture",
    "prompt": "In the cerebellar cortex, Purkinje cells receive two profoundly distinct excitatory inputs: climbing fibers (which produce all-or-none complex spikes) originate exclusively from:",
    "options": [
      "The pontine nuclei via mossy fibers",
      "The vestibular nuclei",
      "The contralateral inferior olivary nucleus",
      "The cerebral motor cortex directly"
    ],
    "answer": 2,
    "explain": "Each adult Purkinje cell receives synaptic input from exactly ONE climbing fiber originating in the contralateral inferior olive. A single climbing fiber action potential evokes a massive, multi-peaked 'complex spike' featuring large Ca2+ influx. In contrast, Purkinje cells receive inputs from >100,000 granule cell parallel fibers (driven by mossy fibers), generating simple spikes.",
    "example": "Climbing fiber complex spikes serve as the instructive error signal that drives cerebellar LTD at co-active parallel fiber synapses.",
    "id": "nb-067",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Perforated Patch Clamp Configuration",
    "prompt": "The perforated patch clamp technique preserves endogenous intracellular second messenger signaling and prevents 'washout' of LTP by rupturing the membrane with pore-forming antibiotics such as:",
    "options": [
      "Streptomycin",
      "Penicillin or ampicillin",
      "Tetracycline",
      "Amphotericin B, nystatin, or gramicidin"
    ],
    "answer": 3,
    "explain": "Amphotericin B and nystatin form small pores in the membrane patch permeable strictly to monovalent ions (Na+, K+, Cl-), establishing electrical access while preventing the diffusion and 'washout' of large proteins, kinases, ATP, and second messengers into the recording pipette.",
    "example": "Gramicidin perforated patch is uniquely permeable to monovalent cations but impermeable to chloride, allowing measurement of the true unperturbed intracellular chloride concentration and E_Cl.",
    "id": "nb-068",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Astrocytic Calcium Waves and IP3R2",
    "prompt": "Intercellular calcium waves propagating across astrocytic syncytia via gap junctions require release of calcium from endoplasmic reticulum stores mediated by which receptor?",
    "options": [
      "Inositol 1,4,5-trisphosphate receptor type 2 (IP3R2)",
      "Ryanodine receptor type 1",
      "NMDA receptors",
      "P2X7 receptors exclusively"
    ],
    "answer": 0,
    "explain": "Astrocytes selectively express the IP3R2 isoform. Gq-coupled GPCR activation (e.g. by ATP or glutamate) stimulates PLCbeta, generating IP3 that gates IP3R2 on the ER, releasing stored Ca2+ to generate cytosolic transients and propagate intercellular waves via connexin hemichannels.",
    "example": "IP3R2 knockout mice exhibit total loss of spontaneous and GPCR-mediated somatic Ca2+ elevations in cortical astrocytes.",
    "id": "nb-069",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Neuropixels Silicon Probe Technology",
    "prompt": "Neuropixels CMOS silicon probes revolutionized systems electrophysiology (Jun et al. Nature 2017) by allowing simultaneous recording of hundreds of single neurons across multiple brain structures using:",
    "options": [
      "A single gold-coated glass pipette",
      "Nearly 1,000 recording sites along a single thin 10-mm shank with integrated on-chip amplification and digitization",
      "Intracellular optical fibers measuring pH",
      "Magnetic resonance coils"
    ],
    "answer": 1,
    "explain": "Neuropixels probes integrate 960 recording sites on a 10-mm long, 70-μm wide silicon shank, with 384 user-selectable channels digitized directly on the probe base, enabling simultaneous recording of spiking activity across cortex, hippocampus, and thalamus in behaving mice.",
    "example": "Using automated spike sorting (Kilosort), a single Neuropixels probe typically yields 200 to 500 well-isolated single units per recording session.",
    "id": "nb-070",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Metaplasticity and the BCM Rule",
    "prompt": "According to the Bienenstock-Cooper-Munro (BCM) theoretical model of synaptic plasticity, the modification threshold (theta_M) separating LTP from LTD is dynamic, shifting to the right when:",
    "options": [
      "All NMDA receptors are irreversibly blocked",
      "Postsynaptic activity has been zero for days",
      "Historical postsynaptic activity has been high, making further LTP harder to induce and favoring LTD",
      "Calcium levels drop to absolute zero"
    ],
    "answer": 2,
    "explain": "The BCM rule introduces a sliding modification threshold (theta_M). High prior cortical activity shifts theta_M to the right (requiring stronger stimulation to achieve LTP, preventing runaway saturation), whereas prolonged inactivity shifts theta_M to the left, facilitating LTP induction.",
    "example": "Dark rearing shifts the visual cortical plasticity threshold to the left, allowing low-frequency stimulation to induce LTP that would normally produce LTD in light-reared animals.",
    "id": "nb-071",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Action Potential Phase Plot Analysis",
    "prompt": "In electrophysiological analysis, plotting the time derivative of membrane potential (dV/dt) against membrane potential (V) produces a phase plot whose initial sharp inflection point reveals:",
    "options": [
      "The single-channel conductance of potassium channels",
      "The intracellular chloride reversal potential",
      "The rate of protein synthesis",
      "The precise voltage threshold for action potential initiation at the axon initial segment"
    ],
    "answer": 3,
    "explain": "The phase plot (dV/dt vs V) shows a characteristic two-component upstroke: the initial sharp take-off reflects Nav channel activation at the distant axon initial segment (AIS), followed by the second peak representing the invasion of the action potential into the larger somatic capacitance.",
    "example": "Axotomy or AIS disruption eliminates the initial sharp inflection on phase plots, merging somatic and axonal activation.",
    "id": "nb-072",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Sodium Channel Inactivation IFM Motif",
    "prompt": "Fast voltage-dependent inactivation of Nav channels occurs within 1-2 ms of opening when the hydrophobic 'hinged lid' motif in the III-IV intracellular linker binds the channel inner vestibule. This motif consists of:",
    "options": [
      "Isoleucine-Phenylalanine-Methionine (IFM)",
      "Lysine-Arginine-Histidine (KRH)",
      "Aspartate-Glutamate-Aspartate (DED)",
      "Proline-Glycine-Proline (PGP)"
    ],
    "answer": 0,
    "explain": "William Catterall demonstrated that the IFM motif in the cytoplasmic loop between domains III and IV serves as the hydrophobic latch that swings into the inner pore vestibule upon depolarization, blocking ion permeation and establishing the absolute refractory period.",
    "example": "Mutating the phenylalanine in the IFM motif to glutamine (IFM -> IQM) completely eliminates fast sodium channel inactivation.",
    "id": "nb-073",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Corticospinal Tract Decussation",
    "prompt": "In human neuroanatomy, approximately 85-90% of descending corticospinal motor fibers cross the midline at the decussation of the pyramids in the caudal medulla to form the:",
    "options": [
      "Anterior corticospinal tract",
      "Lateral corticospinal tract in the lateral funiculus of the spinal cord",
      "Rubrospinal tract",
      "Vestibulospinal tract"
    ],
    "answer": 1,
    "explain": "The majority of fibers decussate at the spinomedullary junction, descending in the contralateral lateral funiculus to innervate distal limb motor neurons (fine manipulative movements). The uncrossed 10-15% descend as the anterior corticospinal tract, which decussates at segmental levels to control axial/trunk musculature.",
    "example": "A unilateral stroke damaging the internal capsule above the decussation produces spastic hemiparesis on the contralateral side of the body.",
    "id": "nb-074",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Homer-Shank Scaffolding Complex",
    "prompt": "At the postsynaptic density, Homer-1 proteins crosslink group I metabotropic glutamate receptors (mGluR1/5) and IP3 receptors to the master PSD scaffold Shank, which directly links to:",
    "options": [
      "Voltage-gated sodium channels at nodes of Ranvier",
      "Tubulin dimers inside the axon hillock",
      "GKAP (SAPAP), which binds PSD-95 to physically bridge NMDARs with intracellular calcium stores",
      "Extracellular laminin"
    ],
    "answer": 2,
    "explain": "The Homer-Shank-GKAP-PSD-95 protein network forms a high-order protein lattice beneath the postsynaptic membrane. Homer tetramers bind the EVH1 domains of Shank and the C-termini of mGluR5 and IP3R, aligning surface receptors with endoplasmic reticulum Ca2+ stores.",
    "example": "The immediate early gene Homer-1a is a monomeric, dominant-negative truncated isoform that uncouples Homer scaffolds, scaling down synaptic strength during sleep.",
    "id": "nb-075",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Optogenetic Voltage Sensors vs Calcium Indicators",
    "prompt": "While genetically encoded calcium indicators (GECIs like GCaMP6s) are widely used, their primary biophysical limitation compared to voltage indicators (GEVIs) is:",
    "options": [
      "Direct blockade of NMDA receptors",
      "Complete lack of fluorescent emission",
      "Inability to cross the nuclear membrane",
      "Slow temporal kinetics (decay tau ~200-1000 ms), inability to resolve subthreshold hyperpolarizing IPSPs, and saturation during high-frequency spike trains"
    ],
    "answer": 3,
    "explain": "Cytosolic Ca2+ transients are downstream, buffered, low-pass filtered proxies of neural activity with rise times of 10-50 ms and decay times of hundreds of milliseconds. They cannot detect subthreshold hyperpolarizations, IPSPs, or accurately count individual spikes in bursts >50 Hz, whereas GEVIs report true membrane potential in real time.",
    "example": "Simultaneous two-photon imaging of GCaMP and patch-clamp electrophysiology demonstrates that single action potentials evoke broad, overlapping calcium transients that conceal high-frequency interneuron firing.",
    "id": "nb-076",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Chandelier Cells and the Axon Initial Segment",
    "prompt": "Cortical chandelier (axo-axonic) cells are specialized parvalbumin-positive interneurons whose distinctive terminal 'cartridges' synapse exclusively onto:",
    "options": [
      "The axon initial segments (AIS) of pyramidal neurons",
      "Dendritic spine heads of other interneurons",
      "Cerebral capillary pericytes",
      "Astrocytic cell bodies"
    ],
    "answer": 0,
    "explain": "Chandelier cells display unique vertical strings of boutons ('cartridges') that contact the axon initial segment (AIS) of pyramidal cells. Because the AIS is the site of action potential initiation, chandelier cells exert profound control over the final output of pyramidal networks.",
    "example": "Because the AIS has a relatively depolarized chloride reversal potential (E_Cl), axo-axonic GABA release can under certain conditions exert depolarizing, though still shunting, effects.",
    "id": "nb-077",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Microglial Elimination of Perineuronal Nets",
    "prompt": "In the adult cortex, experience-dependent remodeling of perineuronal nets (PNNs) surrounding parvalbumin interneurons is executed by microglia via secretion of:",
    "options": [
      "Myelin basic protein",
      "Matrix metalloproteinases (MMP-9) and Cathepsins",
      "Choline acetyltransferase",
      "Dopamine beta-hydroxylase"
    ],
    "answer": 1,
    "explain": "Microglia continuously remodel the extracellular matrix. During sensory enrichment or learning, microglial processes contact PNNs, secreting matrix metalloproteinase-9 (MMP-9) and tissue plasminogen activator (tPA) to locally cleave chondroitin sulfate proteoglycans, reopening synaptic plasticity windows.",
    "example": "Pharmacological depletion of microglia with PLX3397 causes aberrant accumulation of hyperdense PNNs and impairs fear memory extinction.",
    "id": "nb-078",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Synaptic Scaling Multiplicative Equation",
    "prompt": "Mathematically, homeostatic synaptic scaling transforms the distribution of postsynaptic miniature EPSC amplitudes according to the linear equation:",
    "options": [
      "y = x^2, representing exponential divergence",
      "y = x + c, representing additive shift",
      "y = a * x, where 'a' is a uniform scaling factor and 'x' is the basal mEPSC amplitude",
      "y = 1 / x, representing reciprocal inhibition"
    ],
    "answer": 2,
    "explain": "Scaling is strictly multiplicative (y = ax). Because every synapse on the neuron scales up or down by the same proportional factor (e.g. multiplied by 1.8 after prolonged inactivity), the relative differences in synaptic weights established by prior Hebbian LTP/LTD are perfectly conserved.",
    "example": "Cumulative frequency plots of mEPSC amplitudes demonstrate that scaling shifts the curve along the x-axis by a pure multiplicative scalar factor.",
    "id": "nb-079",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Single-Channel Patch-Clamp Subconductance States",
    "prompt": "In single-channel cell-attached patch clamp recordings of AMPA receptors (e.g. GluA1/2 heteromers), binding of multiple glutamate molecules reveals four distinct subconductance states corresponding to:",
    "options": [
      "Four distinct phosphorylation states of the lipid bilayer",
      "Complete denaturation of the channel pore",
      "Entry of 4 distinct divalent cations simultaneously",
      "Sequential opening of 1, 2, 3, or all 4 pore-lining subunits in the tetramer, with single-channel conductance increasing with occupancy from ~9 pS to ~28 pS"
    ],
    "answer": 3,
    "explain": "Rosenmund, Stern-Bach, and Stevens (Science 1998) proved that individual AMPA receptor tetramers open in four discrete subconductance levels corresponding to binding of 1, 2, 3, or 4 glutamate molecules. High-affinity CaMKII phosphorylation at GluA1 Ser831 increases single-channel conductance by shifting channel gating toward higher subconductance open states.",
    "example": "CaMKII phosphorylation increases the mean single-channel conductance of GluA1 homomers from ~9 pS to ~28 pS during LTP.",
    "id": "nb-080",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Spine Neck Resistance Measurement",
    "prompt": "Using combined two-photon glutamate uncaging and whole-cell dendritic recording (Bloodgood & Sabatini, Harnett et al.), the electrical resistance of typical mature CA1 dendritic spine necks was measured to be:",
    "options": [
      "Approximately 100 to 500 Megaohms (M-ohms), sufficient to generate large local spine head depolarizations (~20-40 mV) relative to the parent shaft",
      "Near zero (<1 ohm)",
      "Exceeding 50 Gigaohms, completely isolating the spine electrically",
      "Negative resistance"
    ],
    "answer": 0,
    "explain": "Spine neck resistance (R_neck ~100-500 MΩ) is sufficiently high that small synaptic currents (e.g. 50-100 pA) produce large local EPSPs inside the spine head (20-40 mV), relieving local NMDA receptor Mg2+ block even when somatic recordings register only a 1 mV EPSP.",
    "example": "FRAP measurements of fluorescent dye diffusion across the spine neck confirm that diffusional resistance correlates directly with measured electrical neck resistance.",
    "id": "nb-081",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Kv1 Channels at Juxtaparanodes",
    "prompt": "At mature myelinated peripheral and central axons, Kv1.1 and Kv1.2 channels are precisely sequestered beneath the myelin sheath at the juxtaparanode through interaction with:",
    "options": [
      "Ankyrin-G and beta-IV spectrin",
      "Caspr2 (Contactin-associated protein-like 2) and TAG-1",
      "Connexin-32 hemichannels",
      "Integrin alpha-6-beta-1"
    ],
    "answer": 1,
    "explain": "The axo-glial junction at the paranode (Caspr/contactin) acts as a physical diffusion barrier that segregates nodal Nav1.6 channels from juxtaparanodal Kv1.1/1.2 channels. Kv1 channels are anchored to the axonal cytoskeleton by Caspr2 and the cell adhesion molecule TAG-1.",
    "example": "In Caspr2 knockout mice or in autoimmune encephalitis targeting Caspr2/LGI1, Kv1 channels disperse into internodes, causing axonal hyperexcitability and neuromyotonia.",
    "id": "nb-082",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "GABA-B Receptor G-Protein Coupling Kinetics",
    "prompt": "Single-cell FRET studies of GABA-B receptor activation (Lohse lab) demonstrated that the rate-limiting step in slow metabotropic inhibitory postsynaptic potentials (slow IPSPs, peak ~150-200 ms) is:",
    "options": [
      "Internalization of the receptor into endosomes",
      "The slow diffusion of GABA across the synaptic cleft",
      "The slow diffusion and collision of G-protein beta-gamma subunits across the plasma membrane to gate GIRK channels, rather than slow ligand binding",
      "Slow transcription of new GIRK channel genes"
    ],
    "answer": 2,
    "explain": "GABA binds the GABA-B1 Venus flytrap domain within milliseconds. However, GDP-GTP exchange, dissociation of the G-protein heterotrimer, and lateral membrane diffusion of G_beta-gamma subunits to physically bind and open inward rectifier potassium (GIRK) channels requires 100-200 ms, dictating the slow kinetics of GABA-B IPSPs.",
    "example": "Direct optical uncaging of GABA at postsynaptic dendrites confirms a ~30-50 ms latency before GIRK outward currents begin.",
    "id": "nb-083",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Equilibrium Potential Calculation",
    "prompt": "Which equation is used to calculate the equilibrium potential for a single permeant ion across a semipermeable membrane based on its intra- and extracellular concentrations?",
    "options": [
      "Hill equation",
      "Goldman-Hodgkin-Katz equation",
      "Michaelis-Menten equation",
      "Nernst equation"
    ],
    "answer": 3,
    "explain": "The Nernst equation (E_ion = (RT/zF) * ln([ion]_out / [ion]_in)) calculates the electrical membrane potential that exactly balances the chemical concentration gradient for a single ion species.",
    "example": "Calculating E_K with [K+]out = 4 mM and [K+]in = 140 mM yields approximately -89 mV at mammalian body temperature (37°C).",
    "id": "nb-084",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Voltage Sensor Motif",
    "prompt": "In voltage-gated ion channels, the positively charged S4 transmembrane segment that serves as the primary voltage sensor is enriched in which amino acid?",
    "options": [
      "Arginine (and Lysine)",
      "Proline",
      "Glutamate",
      "Aspartate"
    ],
    "answer": 0,
    "explain": "The S4 segment features positively charged basic residues (arginine or lysine) positioned at every third or fourth position. Depolarization exerts an outward electrostatic force on these charges, shifting S4 outward and opening the channel gate.",
    "example": "Neutralizing basic arginine residues in S4 shifts the voltage-dependence of activation to more depolarized potentials.",
    "id": "nb-085",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Potassium Channel Selectivity Filter",
    "prompt": "The potassium channel selectivity filter coordinates dehydrated K+ ions with sub-angstrom precision using backbone carbonyl oxygens bearing the conserved signature sequence:",
    "options": [
      "Arg-Gly-Asp (RGD)",
      "Thr-Val-Gly-Tyr-Gly (TVGYG)",
      "Lys-Asp-Glu-Leu (KDEL)",
      "Asn-Pro-Val-Tyr (NPVY)"
    ],
    "answer": 1,
    "explain": "Roderick MacKinnon's crystal structures of KcsA proved that the TVGYG sequence presents backbone carbonyl oxygens that precisely mimic the hydration shell of K+ (1.33 Å radius), coordinating K+ while rejecting smaller Na+ (0.95 Å) due to energetic dehydration penalties.",
    "example": "Mutation of any single residue within the TVGYG filter collapses potassium selectivity and allows sodium permeation.",
    "id": "nb-086",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Myelinated Axon Propagation",
    "prompt": "Action potential propagation in myelinated axons jumps from one unmyelinated gap to the next in a process termed:",
    "options": [
      "Ephaptic coupling",
      "Continuous electrotonic propagation",
      "Saltatory conduction",
      "Retrograde decremental conduction"
    ],
    "answer": 2,
    "explain": "Myelin sheaths increase effective membrane resistance and decrease membrane capacitance, allowing local currents to propagate electrotonically with minimal loss to the next node of Ranvier, where action potentials are regeneratively regenerated.",
    "example": "Saltatory conduction increases action potential conduction velocity up to 100-fold compared to unmyelinated fibers of the same diameter.",
    "id": "nb-087",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Nodes of Ranvier Sodium Channels",
    "prompt": "At mature central nervous system nodes of Ranvier, which voltage-gated sodium channel isoform is densely clustered to regenerate action potentials?",
    "options": [
      "Nav1.9",
      "Nav1.5",
      "Nav1.4",
      "Nav1.6 (SCN8A)"
    ],
    "answer": 3,
    "explain": "Nav1.6 is the predominant sodium channel isoform clustered at mature nodes of Ranvier and the distal axon initial segment, recruited by interactions with Ankyrin-G and beta-IV spectrin.",
    "example": "During early postnatal development, nodes initially cluster Nav1.2, which is subsequently replaced by Nav1.6 as myelination matures.",
    "id": "nb-088",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Chloride Equilibrium and GABA Action",
    "prompt": "In mature neurons, the intracellular chloride concentration is kept exceptionally low (~5-10 mM) by the continuous outward extrusion activity of which cotransporter?",
    "options": [
      "KCC2 (K+/Cl- cotransporter 2)",
      "NKCC1",
      "NCX1",
      "NHE1"
    ],
    "answer": 0,
    "explain": "KCC2 utilizes the outward potassium gradient to extrude chloride ions against their electrochemical gradient, maintaining a hyperpolarized chloride reversal potential (E_Cl ≈ -75 to -85 mV) in mature neurons.",
    "example": "Downregulation of KCC2 after traumatic spinal cord injury causes intracellular chloride accumulation, rendering GABA depolarizing and causing neuropathic allodynia.",
    "id": "nb-089",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Small-Molecule Neurotransmitter Vesicular Loading",
    "prompt": "The loading of glutamate, GABA, and monoamines into synaptic vesicles is driven by a transmembrane proton electrochemical gradient generated by:",
    "options": [
      "Na+/K+-ATPase",
      "Vacuolar-type H+-ATPase (v-ATPase)",
      "Mitochondrial ATP synthase",
      "Calcium ATPase (PMCA)"
    ],
    "answer": 1,
    "explain": "The vesicular v-ATPase pumps protons into the vesicle lumen, creating an interior-acidic (pH ~5.5) and interior-positive electrical potential (ΔΨ). Vesicular transporters (vGLUT, vGAT, VMAT) exploit this proton-motive force via secondary active antiport.",
    "example": "Bafilomycin A1 selectively inhibits v-ATPase, dissipating the proton gradient and depleting synaptic vesicles of neurotransmitters within minutes.",
    "id": "nb-090",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Electrical Resistance of Cell Membranes",
    "prompt": "Biological phospholipid bilayers in the absence of open protein channels exhibit an electrical resistance that is:",
    "options": [
      "Zero, behaving as superconductors",
      "Extremely low, allowing free passive current flow",
      "Extremely high (>10^8 ohms), acting as near-perfect electrical insulators",
      "Fluctuating between zero and infinity at 1 kHz"
    ],
    "answer": 2,
    "explain": "Pure lipid bilayers are virtually impermeable to hydrophilic ions, presenting an electrical resistance of 10^8 to 10^9 ohms per square centimeter, functioning as dielectric capacitors until ion channels are gated.",
    "example": "Patch clamp recordings from seal patches devoid of ion channels register picoampere-level currents even under 100 mV voltage steps.",
    "id": "nb-091",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Calcium Equilibrium Potential",
    "prompt": "Because the resting intracellular free Ca2+ concentration (~50-100 nM) is four orders of magnitude lower than extracellular Ca2+ (~1-2 mM), the equilibrium potential for Ca2+ (E_Ca) is:",
    "options": [
      "-55 mV",
      "Highly negative (-90 mV)",
      "Zero mV",
      "Highly positive (+120 to +140 mV)"
    ],
    "answer": 3,
    "explain": "Applying the Nernst equation for a divalent cation (z = +2) with a 20,000-fold concentration gradient yields an equilibrium potential exceeding +120 mV. Consequently, opening of Ca2+ channels creates an immense inward driving force.",
    "example": "Even at depolarized action potential peaks (+30 mV), the driving force on Ca2+ remains strongly inward (approx. 90 mV).",
    "id": "nb-092",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Ionotropic vs Metabotropic Receptors",
    "prompt": "In contrast to ionotropic receptors that contain an integral ion-conducting pore, metabotropic receptors signal across the membrane by:",
    "options": [
      "Activating intracellular heterotrimeric G-proteins and second messenger cascades",
      "Forming nuclear transcription factor dimers directly",
      "Directly phosphorylating lipid bilayers without proteins",
      "Pumping protons across the plasma membrane"
    ],
    "answer": 0,
    "explain": "Metabotropic receptors are seven-transmembrane domain GPCRs that couple to heterotrimeric G-proteins (Gs, Gi/o, Gq/11), modulating intracellular second messengers (cAMP, IP3, DAG, Ca2+) and indirectly gating ion channels over slower timescales (hundreds of ms to seconds).",
    "example": "Muscarinic acetylcholine receptors, metabotropic glutamate receptors (mGluRs), and GABA-B receptors are all metabotropic.",
    "id": "nb-093",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Gap Junction Structure",
    "prompt": "Each functional intercellular gap junction channel at an electrical synapse is formed by the end-to-end docking of two hemichannels called:",
    "options": [
      "Septins",
      "Connexons (each composed of six connexin subunits)",
      "Integrin heterodimers",
      "Cadherin homopentamers"
    ],
    "answer": 1,
    "explain": "A connexon is a hexameric ring of connexin proteins spanning the plasma membrane of one cell. When it docks with a matching connexon in an adjacent cell, it forms a continuous 1.5 to 2 nm pore allowing diffusion of ions, cAMP, and IP3.",
    "example": "In the retina, connexin-36 (Cx36) mediates electrical coupling between AII amacrine cells and ON cone bipolar terminals.",
    "id": "nb-094",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Glutamate Excitotoxicity Concept",
    "prompt": "Excessive, sustained accumulation of extracellular glutamate leads to neuronal death ('excitotoxicity') primarily through massive, unregulated influx of:",
    "options": [
      "Chloride (Cl-) through gap junctions",
      "Sodium (Na+) via potassium channels",
      "Calcium (Ca2+) via NMDA receptors and voltage-gated Ca2+ channels",
      "Glucose through GLUT3"
    ],
    "answer": 2,
    "explain": "Prolonged glutamate stimulation overactivates NMDA receptors, driving lethal calcium overload. Excess cytosolic Ca2+ hyperactivates calpains, calcineurin, and nNOS, triggering mitochondrial depolarization, mPTP opening, ROS burst, and necrotic/apoptotic cell lysis.",
    "example": "In ischemic stroke, failure of astrocytic glutamate uptake causes massive excitotoxic infarction in the ischemic penumbra.",
    "id": "nb-095",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Astrocyte Morphology and GFAP",
    "prompt": "The primary intermediate filament protein utilized as an immunohistochemical marker for reactive astrocytes in the mammalian brain is:",
    "options": [
      "Peripherin",
      "Vimentin exclusively",
      "Neurofilament heavy chain (NF-H)",
      "Glial Fibrillary Acidic Protein (GFAP)"
    ],
    "answer": 3,
    "explain": "GFAP is a type III intermediate filament protein that forms the cytoskeletal architecture of mature astrocytes. In response to brain injury, stroke, or neurodegeneration, astrocytes undergo astrogliosis marked by dramatic upregulation of GFAP expression and hypertrophy of processes.",
    "example": "Immunostaining for GFAP reveals intense astrocytic scar formation bordering cortical ischemic stroke lesions.",
    "id": "nb-096",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Microglia Origin",
    "prompt": "Unlike neuroectoderm-derived neurons, astrocytes, and oligodendrocytes, brain microglia originate embryonically from:",
    "options": [
      "Primitive myeloid progenitors in the embryonic yolk sac",
      "The neural crest during gastrulation",
      "The floor plate of the neural tube",
      "Bone marrow monocytes entering strictly after birth"
    ],
    "answer": 0,
    "explain": "Microglia derive from primitive erythro-myeloid progenitors in the yolk sac at embryonic day 7.5 to 8.5 in mice. These cells migrate into the developing neural tube and self-renew locally throughout adult life without replacement by circulating bone marrow monocytes under physiological conditions.",
    "example": "Lineage-tracing experiments by Ginhoux et al. proved that yolk sac macrophages are the exclusive developmental source of resident microglia.",
    "id": "nb-097",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Katz Quantal Hypothesis Poisson Model",
    "prompt": "In Katz's statistical model of neurotransmitter release, when the release probability (p) is very low and the number of available vesicles (n) is large, synaptic failure rates follow a Poisson distribution where the mean quantal content (m) equals:",
    "options": [
      "N_failures / N_total",
      "ln(N_total / N_failures)",
      "n * p^2",
      "sqrt(quantal size)"
    ],
    "answer": 1,
    "explain": "In a Poisson process where failures correspond to zero vesicle releases (k=0), P(0) = e^(-m). Rearranging gives m = ln(N / N_0), where N is the total number of trials and N_0 is the number of complete release failures, allowing direct quantal content determination.",
    "example": "Lowering extracellular calcium to 0.5 mM reduces release probability (p), allowing accurate measurement of m using the method of failures.",
    "id": "nb-098",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "TARP Regulation of AMPA Receptors",
    "prompt": "Transmembrane AMPA Receptor Regulatory Proteins (TARPs, such as Stargazin/gamma-2) control AMPA receptor function by:",
    "options": [
      "Phosphorylating sodium channels at the axon initial segment",
      "Completely blocking all channel gating",
      "Promoting trafficking to the cell surface, stabilizing PSD-95 binding, and slowing deactivation/desensitization kinetics",
      "Degrading GluA1 subunits in the lysosome"
    ],
    "answer": 2,
    "explain": "TARPs are auxiliary four-transmembrane subunits that assemble with AMPAR tetramers. Their intracellular C-terminal PDZ-binding motifs anchor AMPARs to PSD-95 at the postsynaptic density, while extracellular loops modulate gating by increasing glutamate affinity and slowing desensitization.",
    "example": "Stargazer mutant mice lack Stargazin (gamma-2), causing loss of functional AMPA receptors at cerebellar granule cell synapses and producing absence epilepsy.",
    "id": "nb-099",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Polyamine Block of AMPARs",
    "prompt": "GluA2-lacking AMPA receptors exhibit inward rectification because at depolarized potentials (+40 mV), the channel pore is plugged by intracellular:",
    "options": [
      "ATP molecules",
      "Magnesium ions",
      "Zinc ions",
      "Endogenous polyamines (spermine and spermidine)"
    ],
    "answer": 3,
    "explain": "GluA2-lacking AMPA receptors (e.g. GluA1 homomers or GluA1/GluA3 heteromers) possess unedited glutamine (Q) residues at the pore loop filter. At depolarized potentials, positively charged intracellular polyamines (spermine) enter the pore from the cytoplasm and block outward current, producing strong inward rectification.",
    "example": "Measuring the rectification index (current at +40 mV divided by current at -60 mV) in the presence of intracellular spermine determines whether synaptic AMPARs contain GluA2.",
    "id": "nb-100",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "NMDA Receptor GluN2B vs GluN2A Kinetics",
    "prompt": "During postnatal brain development, cortical synapses undergo a programmatic switch from GluN2B-containing to GluN2A-containing NMDA receptors, which alters synaptic currents by:",
    "options": [
      "Substantially accelerating deactivation decay kinetics (producing much faster, shorter EPSCs)",
      "Slowing deactivation kinetics to over 2 seconds",
      "Eliminating all sensitivity to magnesium block",
      "Converting the channel into a selective chloride pore"
    ],
    "answer": 0,
    "explain": "GluN2B-containing NMDARs exhibit slow deactivation kinetics (decay tau ~300-400 ms), allowing long integration windows in immature circuits. As GluN2A subunits replace GluN2B during synaptic maturation, deactivation accelerates ~4-fold (decay tau ~50-80 ms), narrowing the temporal coincidence detection window.",
    "example": "Ro 25-6981 and ifenprodil selectively inhibit GluN2B-containing NMDARs, allowing pharmacological dissection of subunit contribution.",
    "id": "nb-101",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "SNARE Disassembly by NSF and alpha-SNAP",
    "prompt": "Following membrane fusion, the extraordinarily stable four-helix cis-SNARE bundle is disassembled and recycled through ATP hydrolysis by which chaperone complex?",
    "options": [
      "Dynamin and Amphiphysin",
      "N-ethylmaleimide-sensitive factor (NSF) and alpha-SNAP",
      "Hsc70 and Auxilin",
      "Clathrin and AP-2"
    ],
    "answer": 1,
    "explain": "The core SNARE complex is so energetically stable that it resists SDS denaturation at room temperature. The hexameric AAA+ ATPase NSF, recruited by soluble alpha-SNAP adaptors, uses the energy of ATP hydrolysis to unwind the four parallel alpha-helices, freeing synaptobrevin, syntaxin, and SNAP-25 for subsequent rounds of fusion.",
    "example": "Treating nerve terminals with N-ethylmaleimide (NEM) alkylates and inactivates NSF, causing rapid accumulation of post-fusion cis-SNARE complexes and synaptic failure.",
    "id": "nb-102",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Synaptotagmin-7 and Asynchronous Release",
    "prompt": "While Synaptotagmin-1 mediates fast synchronous exocytosis, which high-affinity calcium sensor mediates slow, asynchronous neurotransmitter release and short-term synaptic facilitation?",
    "options": [
      "Otoferlin",
      "Synaptotagmin-4",
      "Synaptotagmin-7 (Syt7)",
      "Complexin-2"
    ],
    "answer": 2,
    "explain": "Syt7 has a higher Ca2+ affinity and slower Ca2+ dissociation kinetics than Syt1. It binds residual Ca2+ that persists after action potential trains, mediating sustained asynchronous release and presynaptic paired-pulse facilitation.",
    "example": "Syt7 knockout mice retain normal single-spike synchronous transmission but exhibit complete loss of paired-pulse facilitation and asynchronous release.",
    "id": "nb-103",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "A-Type Potassium Channels and Dendritic Filtering",
    "prompt": "Rapidly activating and inactivating A-type potassium channels (encoded by Kv4.2/Kv4.3) are densely localized in the apical dendrites of CA1 pyramidal neurons where they:",
    "options": [
      "Permeate calcium during high-frequency firing",
      "Accelerate action potential upstrokes at the axon hillock",
      "Open exclusively during profound hyperpolarization below -100 mV",
      "Dampen the amplitude of backpropagating action potentials (bAPs) and limit subthreshold dendritic summation"
    ],
    "answer": 3,
    "explain": "Kv4.2 channels display a 5- to 6-fold increasing density gradient from the soma to distal apical dendrites in CA1. They activate rapidly upon subthreshold depolarization, providing outward K+ current that attenuates backpropagating action potential amplitudes and limits local dendritic Ca2+ entry.",
    "example": "Pharmacological block of A-type K+ channels with 4-aminopyridine (4-AP) allows backpropagating action potentials to invade distal dendrites without attenuation.",
    "id": "nb-104",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Cerebellar Purkinje Cell Output",
    "prompt": "Cerebellar Purkinje neurons, the sole projection neurons of the cerebellar cortex, inhibit deep cerebellar nuclei neurons using which neurotransmitter?",
    "options": [
      "GABA",
      "L-Glutamate",
      "Acetylcholine",
      "Dopamine"
    ],
    "answer": 0,
    "explain": "Despite their massive dendritic trees and reception of >100,000 excitatory parallel fiber and climbing fiber inputs, Purkinje cells are GABAergic inhibitory neurons. Their high-frequency baseline firing (50-100 Hz) tonic-inhibits targets in the deep cerebellar and vestibular nuclei.",
    "example": "Optogenetic stimulation of Purkinje cell axon terminals in the interpositus nucleus immediately halts ongoing motor execution.",
    "id": "nb-105",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Shunting Inhibition Biophysics",
    "prompt": "Shunting inhibition occurs when GABA-A receptor opening occurs at a membrane potential that is equal to the chloride reversal potential (V_m = E_Cl) because:",
    "options": [
      "The cell immediately depolarizes by 40 mV",
      "Membrane conductance dramatically increases, which shunts depolarizing excitatory currents without changing baseline membrane potential",
      "Chloride ions cease moving entirely",
      "Potassium channels close irreversibly"
    ],
    "answer": 1,
    "explain": "When V_m = E_Cl, opening GABA-A channels produces zero net current (I = g * (V_m - E_Cl) = 0), so no hyperpolarization is observed. However, the large increase in membrane conductance (g_Cl) lowers input resistance (R_in), meaning co-occurring excitatory currents produce much smaller EPSPs according to Ohm's law (ΔV = I_exc * R_in).",
    "example": "Shunting inhibition strategically located at the soma or proximal axon hillock can veto massive distal dendritic excitatory inputs.",
    "id": "nb-106",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Astrocyte Glutamine Synthetase",
    "prompt": "In the brain, the high-affinity conversion of neurotoxic free ammonia and glutamate into neutral glutamine is executed exclusively by which enzyme?",
    "options": [
      "Glutamate decarboxylase (GAD)",
      "Glutaminase",
      "Glutamine synthetase (GS)",
      "Aspartate aminotransferase"
    ],
    "answer": 2,
    "explain": "Glutamine synthetase is an ATP-dependent enzyme localized exclusively to astrocytes in the central nervous system. It detoxifies ammonia and recycles glutamate into glutamine, which is safe to export to the extracellular space for neuronal reuptake.",
    "example": "In hepatic encephalopathy, excessive systemic ammonia saturates astrocytic glutamine synthetase, causing osmotic swelling of astrocytes and cerebral edema.",
    "id": "nb-107",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Cerebellar LTD Induction Mechanism",
    "prompt": "Long-Term Depression (LTD) at parallel fiber-Purkinje cell synapses requires the precise temporal coincidence of parallel fiber and climbing fiber activation, which drives:",
    "options": [
      "Complete degradation of the postsynaptic density by calpain",
      "Pure NMDA receptor calcium influx through NR1/NR2A subunits",
      "Calcineurin-dependent dephosphorylation of CaMKII Thr286",
      "Gq-mediated PLCbeta/IP3/DAG activation coinciding with climbing fiber Ca2+ influx, activating PKCalpha to phosphorylate GluA2 at Ser880"
    ],
    "answer": 3,
    "explain": "Purkinje cells lack functional postsynaptic NMDA receptors. Parallel fibers stimulate mGluR1 (Gq -> PLCbeta -> DAG + IP3), while climbing fiber complex spikes drive massive voltage-gated Ca2+ influx through Cav2.1. The synergistic Ca2+ and DAG elevation hyperactivates PKCalpha, which phosphorylates GluA2 at Ser880, disrupting GRIP/ABP binding and driving clathrin-dependent AMPAR endocytosis.",
    "example": "Purkinje-cell-specific knockout of PKCalpha or mGluR1 abolishes cerebellar LTD and severely impairs eyeblink classical conditioning.",
    "id": "nb-108",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Retrograde Nitric Oxide Plasticity",
    "prompt": "Postsynaptic generation of nitric oxide (NO) during certain forms of LTP requires that neuronal nitric oxide synthase (nNOS) be physically tethered to the postsynaptic density through binding to:",
    "options": [
      "The PDZ2 domain of PSD-95",
      "The C-terminus of beta-actin",
      "Gephyrin",
      "Stargazin"
    ],
    "answer": 0,
    "explain": "nNOS contains an N-terminal PDZ domain that forms a unique heterodimer with the PDZ2 domain of PSD-95. Because PSD-95 also binds the NMDA receptor GluN2B subunit, this scaffolds nNOS within nanometers of the NMDAR pore, allowing immediate activation by incoming Ca2+/calmodulin.",
    "example": "Disrupting the nNOS-PSD-95 interaction with targeted uncoupling peptides blocks NO generation and protects against excitotoxicity without blocking NMDAR channel current.",
    "id": "nb-109",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Optogenetic Control of Gi Signaling",
    "prompt": "The chimeric engineered rhodopsin-GPCR 'opto-XR' known as 'opto-beta2-AR' or 'opto-MOR' allows light-driven control of specific G-protein cascades by replacing the intracellular loops of rhodopsin with those of:",
    "options": [
      "Voltage-gated potassium channels",
      "Specific adrenergic or opioid GPCRs that couple to Gs, Gi/o, or Gq",
      "Bacterial bacteriorhodopsin pumps",
      "Receptor tyrosine kinases (TrkB)"
    ],
    "answer": 1,
    "explain": "Karl Deisseroth's lab engineered opto-XRs by fusing the light-absorbing extracellular and transmembrane domains of bovine rhodopsin with the intracellular cytoplasmic loops of specific GPCRs (e.g. beta2-adrenergic for Gs, or mu-opioid for Gi/o), permitting green light stimulation of cAMP or IP3 signaling in defined neural circuits.",
    "example": "In vivo opto-alpha1-AR stimulation in nucleus accumbens mimicked Gq activation, modulating conditioned place preference in mice.",
    "id": "nb-110",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Clathrin-Mediated Endocytosis Mechanics",
    "prompt": "During clathrin-mediated endocytosis of synaptic vesicles, the pinch-off (scission) of the vesicle neck from the plasma membrane requires GTP hydrolysis by which large mechanochemical GTPase?",
    "options": [
      "Cdc42",
      "Rab3a",
      "Dynamin-1 and Dynamin-3",
      "Ras"
    ],
    "answer": 2,
    "explain": "Dynamin forms a helical collar around the invaginated neck of clathrin-coated pits. Upon GTP hydrolysis, a concerted conformational constriction and twisting motion severs the membrane stalk, releasing the free coated vesicle into the cytoplasm.",
    "example": "The non-hydrolyzable GTP analog GTP-gamma-S or the chemical inhibitor dynasore arrests endocytosis, producing nerve terminals littered with long, unpinched membrane stalks.",
    "id": "nb-111",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Interneuron Gamma Oscillations",
    "prompt": "Cortical and hippocampal gamma oscillations (30-80 Hz) underlying cognitive feature binding and working memory are generated by mutual synaptic feedback between:",
    "options": [
      "Sensory afferents and Schwann cells",
      "Astrocytes and ependymal cilia",
      "Climbing fibers and cerebellar granule cells",
      "Pyramidal excitatory neurons and fast-spiking PV+ basket interneurons (the PING mechanism)"
    ],
    "answer": 3,
    "explain": "The Pyramidal-Interneuron Network Gamma (PING) model demonstrates that synchronous pyramidal cell firing excites PV+ interneurons via AMPA receptors; PV+ interneurons fire back rapid, synchronous GABA-A inhibitory postsynaptic currents that silence pyramidal cells for ~15-25 ms (one gamma period) until inhibition decays.",
    "example": "Optogenetic drive of PV+ interneurons at 40 Hz enhances cognitive cognitive flexibility and information routing through the medial prefrontal cortex.",
    "id": "nb-112",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Dendritic Spine Ca2+ Compartmentalization",
    "prompt": "The high electrical and biochemical isolation of an individual dendritic spine head from its parent dendritic shaft is primarily dictated by the physical dimensions of the:",
    "options": [
      "Spine neck (length and narrow diameter providing high diffusional and electrical resistance)",
      "Postsynaptic density diameter",
      "Spine apparatus ribosomes",
      "Astrocyte endfoot wrapper"
    ],
    "answer": 0,
    "explain": "The spine neck acts as a biological bottleneck. A long, thin spine neck creates high diffusional resistance, restricting incoming Ca2+ and active kinases (such as activated CaMKII) within the spine head for several seconds, ensuring that synaptic plasticity modifications remain strictly input-specific.",
    "example": "Two-photon fluorescence recovery after photobleaching (FRAP) demonstrates that calcium dye clearance from spine heads is dictated directly by neck resistance.",
    "id": "nb-113",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Presynaptic Autoreceptor Feedback",
    "prompt": "At noradrenergic, serotonergic, and dopaminergic nerve terminals, local release of transmitter provides negative feedback inhibition of further exocytosis by binding presynaptic autoreceptors coupled to:",
    "options": [
      "Gs proteins stimulating cAMP",
      "Gi/o proteins (alpha-2, 5-HT1B/D, and D2 autoreceptors inhibiting presynaptic Cav channels)",
      "Gq proteins activating protein kinase C",
      "Ionotropic chloride channels directly"
    ],
    "answer": 1,
    "explain": "Terminal autoreceptors (alpha-2A for noradrenaline, D2 for dopamine, 5-HT1B for serotonin) couple to Gi/o. G-protein beta-gamma subunits directly bind presynaptic P/Q- and N-type voltage-gated Ca2+ channels, shifting their activation to depolarized voltages and reducing exocytotic release probability.",
    "example": "Clonidine stimulates presynaptic alpha-2 receptors, suppressing noradrenaline release and dampening sympathetic outflow.",
    "id": "nb-114",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Microglial Elimination of Redundant Synapses",
    "prompt": "During postnatal critical periods, microglia recognize synapses destined for phagocytic elimination when presynaptic terminals express:",
    "options": [
      "Chondroitinase ABC",
      "High levels of myelin basic protein",
      "Exposed phosphatidylserine ('eat-me' signal) and bound complement proteins C1q and C3b",
      "Voltage-gated potassium channels"
    ],
    "answer": 2,
    "explain": "Vulnerable or inactive synapses transiently flip phosphatidylserine to the outer membrane leaflet and recruit C1q and C3b opsonins. Microglial complement receptor 3 (CR3 / CD11b-CD18) and phagocytic receptors (GPR56, TREM2, MERTK) recognize these signals to engulf the presynaptic bouton.",
    "example": "Blocking exposed phosphatidylserine with Annexin V protects inactive synapses from microglial phagocytosis in vivo.",
    "id": "nb-115",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Calcium-Induced Calcium Release (CICR)",
    "prompt": "In central neurons, amplification of cytosolic calcium transients via Calcium-Induced Calcium Release (CICR) from endoplasmic reticulum stores is mediated by:",
    "options": [
      "Mitochondrial uncoupling protein 1",
      "IP3 receptors exclusively",
      "SERCA pumps",
      "Ryanodine receptors (RyR1-3)"
    ],
    "answer": 3,
    "explain": "Ryanodine receptors on the smooth endoplasmic reticulum are gated by micromolar cytosolic Ca2+. Influx of extracellular Ca2+ through voltage-gated Ca2+ channels or NMDARs binds RyR, triggering rapid release of stored ER calcium into dendritic shafts and spines.",
    "example": "Dantrolene antagonizes ryanodine receptors, blunting excessive CICR and protecting neurons from malignant hyperthermia and excitotoxic injury.",
    "id": "nb-116",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Nav1.1 Channelopathy in Dravet Syndrome",
    "prompt": "Dravet syndrome (Severe Myoclonic Epilepsy of Infancy) is caused by heterozygous loss-of-function mutations in SCN1A (Nav1.1), which causes intractable seizures because Nav1.1 is selectively expressed in:",
    "options": [
      "GABAergic interneurons (particularly PV+ and SST+ cells), leading to failure of inhibitory firing and massive network disinhibition",
      "Cortical glutamatergic pyramidal neurons exclusively",
      "Microglia",
      "Choroid plexus epithelial cells"
    ],
    "answer": 0,
    "explain": "Nav1.1 channels are preferentially concentrated at the axon initial segment of parvalbumin-positive fast-spiking and somatostatin-positive interneurons. Loss-of-function SCN1A mutations impair the ability of interneurons to sustain high-frequency action potential firing, leaving excitatory networks unrestrained.",
    "example": "Selective genetic deletion of Scn1a in forebrain interneurons fully recapitulates epileptic seizures and temperature-induced seizures in mice.",
    "id": "nb-117",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Synaptic Tagging and Capture",
    "prompt": "The 'Synaptic Tagging and Capture' hypothesis (Frey & Morris) explains input-specific late-LTP (L-LTP) by demonstrating that:",
    "options": [
      "Every synapse synthesizes its own nuclear envelope",
      "Weak stimulation sets an input-specific local 'tag' that captures freshly translated Plasticity-Related Proteins (PRPs) synthesized in the soma by a strong stimulus at another input",
      "Plasticity requires retrograde viral transgenesis across all synapses",
      "Tagged synapses immediately undergo apoptosis"
    ],
    "answer": 1,
    "explain": "Frey and Morris showed that a weak stimulus induces early LTP and creates a transient synaptic tag (composed of actin remodeling and kinase complexes). When a strong stimulus at a separate pathway induces transcription and translation of PRPs (e.g. PKMzeta, Arc, homer-1a), these proteins travel throughout the dendritic arbor but are captured strictly by tagged synapses to sustain L-LTP.",
    "example": "A weak stimulation that normally produces decremental E-LTP (decaying in 2 hours) is converted to permanent L-LTP if preceded or followed by strong tetanization of an independent pathway.",
    "id": "nb-118",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Endocannabinoid Clearance Degradation",
    "prompt": "Following retrograde signaling across the synaptic cleft, 2-Arachidonoylglycerol (2-AG) is terminated primarily in presynaptic axon terminals through enzymatic hydrolysis by:",
    "options": [
      "Diacylglycerol lipase (DAGL)",
      "Fatty acid amide hydrolase (FAAH)",
      "Monoacylglycerol lipase (MAGL)",
      "Cyclooxygenase-2"
    ],
    "answer": 2,
    "explain": "While anandamide (AEA) is degraded postsynaptically by FAAH, 2-AG (the primary mediator of retrograde DSI and DSE) is taken up and hydrolyzed into arachidonic acid and glycerol by presynaptic Monoacylglycerol Lipase (MAGL).",
    "example": "Pharmacological inhibition of MAGL with JZL184 dramatically prolongs the duration of depolarization-induced suppression of inhibition (DSI).",
    "id": "nb-119",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Two-Pore Domain Potassium Channels (K2P)",
    "prompt": "The background leak potassium conductance that sets resting membrane potential and is modulated by volatile anesthetics, pH, and membrane stretch is mediated by which channel family?",
    "options": [
      "KCNQ / Kv7 channels",
      "Kv1.1 delayed rectifiers",
      "GIRK channels",
      "K2P channels (e.g. TREK-1, TRAAK, TASK-1)"
    ],
    "answer": 3,
    "explain": "Two-pore domain potassium (K2P) channels operate as homodimers where each subunit contains four transmembrane segments and two pore-forming loops (2P). They are constitutively open at resting potentials, lack voltage-dependent inactivation, and generate the Goldman-Hodgkin-Katz leak current.",
    "example": "Volatile general anesthetics like isoflurane and sevoflurane activate TREK-1 channels, hyperpolarizing central neurons and inducing surgical anesthesia.",
    "id": "nb-120",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Neuroligin-Neurexin Trans-Synaptic Adhesion",
    "prompt": "The trans-synaptic molecular bridge aligning presynaptic vesicle release machinery with postsynaptic receptor densities is formed by interaction between:",
    "options": [
      "Presynaptic Neurexins and postsynaptic Neuroligins",
      "Presynaptic Integrins and postsynaptic Claudins",
      "Presynaptic Synapsins and postsynaptic Actin",
      "Presynaptic Connexins and postsynaptic Claudins"
    ],
    "answer": 0,
    "explain": "Presynaptic neurexins bind across the 20-nm synaptic cleft to postsynaptic neuroligins. Alternative splicing of neurexins (SS#4) and neuroligins dictates synaptic matching: Neuroligin-1 organizes excitatory glutamatergic PSDs, whereas Neuroligin-2 organizes inhibitory gephyrin-containing GABAergic synapses.",
    "example": "Mutations and copy-number variations in NRXN1 and NLGN3/4 are strongly associated with autism spectrum disorders and schizophrenia.",
    "id": "nb-121",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Tripartite Synapse D-Serine vs Glycine",
    "prompt": "In the mature hippocampus, the endogenous co-agonist required alongside glutamate to gate synaptic NMDA receptors at CA3-CA1 synapses is predominantly:",
    "options": [
      "Glycine",
      "D-Serine (synthesized by serine racemase in neurons and astrocytes)",
      "GABA",
      "L-Alanine"
    ],
    "answer": 1,
    "explain": "While glycine serves as the primary co-agonist in the spinal cord, brainstem, and extrasynaptic NMDARs, D-serine (synthesized from L-serine by serine racemase) is the obligate co-agonist for synaptic NMDARs in the adult forebrain and hippocampus.",
    "example": "Depleting endogenous D-serine using D-amino acid oxidase (DAAO) eliminates NMDAR-mediated synaptic transmission and blocks LTP induction in CA1.",
    "id": "nb-122",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Channelrhodopsin Inward Photocurrent Desensitization",
    "prompt": "During sustained continuous illumination of ChR2, the transition from an initial large peak photocurrent (I_peak) to a smaller steady-state plateau current (I_ss) reflects:",
    "options": [
      "Intracellular sodium depletion in the cell soma",
      "Rapid irreversible bleaching of 100% of retinal molecules",
      "A four-state photocycle featuring photo-isomerization of all-trans retinal and thermal relaxation into a lower-conductance conducting state (O2)",
      "Phosphorylation of the opsin by rhodopsin kinase within 5 milliseconds"
    ],
    "answer": 2,
    "explain": "ChR2 gating follows a four-state photocycle (two dark states C1/C2 and two open states O1/O2). Initial photon absorption transitions C1 to high-conductance open state O1 (generating I_peak). Over tens of milliseconds, thermal branch reactions equilibrate O1 with lower-conductance state O2, establishing the plateau steady-state current I_ss.",
    "example": "Engineered opsins like CatCh introduce mutations (e.g. L132C) that elevate calcium permeability and increase stationary photocurrents by altering photocycle kinetics.",
    "id": "nb-123",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Active Zone Nanocolumn Alignment",
    "prompt": "Super-resolution STED and STORM imaging revealed that synaptic transmission occurs within nanoscale trans-synaptic 'nanocolumns' where:",
    "options": [
      "Calcium channels are physically separated from SNARE proteins by >1 micrometer",
      "Receptors are distributed in a completely uniform, random liquid continuum across the entire spine head",
      "Vesicles fuse exclusively at the periphery of the dendritic shaft",
      "Presynaptic RIM clusters and voltage-gated Ca2+ channels are directly aligned across the synaptic cleft with postsynaptic AMPA receptor and PSD-95 nanoclusters"
    ],
    "answer": 3,
    "explain": "Tang et al. (Nature 2016) discovered that synapses are organized into trans-synaptic nanocolumns ~80-100 nm wide. Presynaptic RIM1/2 concentrates docking vesicles directly opposite postsynaptic AMPA receptor clusters anchored by PSD-95. Because glutamate drops off sharply outside the nanodomain, alignment guarantees maximal receptor activation.",
    "example": "Disrupting trans-synaptic adhesion molecules (such as LRRTM2 or neuroligin-1) misaligns the nanocolumn, reducing EPSC amplitude without altering vesicle release probability.",
    "id": "nb-124",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Calyx of Held Nanodomain vs Microdomain Coupling",
    "prompt": "In the auditory brainstem Calyx of Held giant synapse, the developmental transition from microdomain (~100 nm) to nanodomain (~20 nm) coupling between Ca2+ channels and synaptic vesicles is demonstrated experimentally by:",
    "options": [
      "The emergence of resistance to the slow calcium chelator EGTA, while remaining fully sensitive to the fast calcium chelator BAPTA",
      "Total insensitivity to both BAPTA and EGTA",
      "Sensitivity to EGTA but complete resistance to BAPTA",
      "Complete loss of all Cav2.1 P/Q channels"
    ],
    "answer": 0,
    "explain": "EGTA binds Ca2+ with a slow association rate (k_on ~10^6 M^-1 s^-1), allowing Ca2+ to diffuse ~100 nm before being captured, whereas BAPTA binds Ca2+ ~100 times faster. In mature calyces, Ca2+ channels are clustered within 10-20 nm of the vesicle sensor (nanodomain coupling); thus, incoming Ca2+ triggers exocytosis before EGTA can bind, conferring EGTA-insensitivity while fast BAPTA still intercepts Ca2+.",
    "example": "Dialyzing 10 mM EGTA into immature (P7) presynaptic calyces severely inhibits EPSCs, whereas mature (P14) calyces show minimal EPSC depression.",
    "id": "nb-125",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Dendritic Branch Specific Plasticity",
    "prompt": "Non-linear synaptic integration in thin basal and apical oblique dendrites relies on localized 'NMDA spikes' that are initiated when:",
    "options": [
      "A single isolated synapse fires at 1 Hz",
      "Clustered synaptic inputs (20-50 inputs) activate cooperatively within a 1-2 ms window on a single 10-20 micrometer dendritic branch, relieving local Mg2+ block",
      "The soma is hyperpolarized to -120 mV",
      "Astrocytic glutamate transporters are overexpressed by 10-fold"
    ],
    "answer": 1,
    "explain": "Polsky et al. and Losonczy & Magee demonstrated that thin dendritic branches function as independent computational processing subunits. When synchronous clustered inputs arrive on the same branch, local input impedance creates a large local depolarization that unblocks NMDARs, generating a regenerative, plateau-like 'NMDA spike' lasting 20-50 ms.",
    "example": "Two-photon glutamate uncaging on 20 neighboring spines of a single basal dendrite produces a supralinear local NMDA spike that propagates forward to drive somatic action potentials.",
    "id": "nb-126",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Axon Hillock Action Potential Initiation",
    "prompt": "Why is the action potential threshold lowest at the axon initial segment (AIS) compared to the soma or dendrites?",
    "options": [
      "It has the thickest myelin sheath on the entire neuron",
      "It lacks all potassium channels, preventing repolarization",
      "It has an exceptionally high density of voltage-gated sodium channels (Nav1.6 and Nav1.2) anchored by ankyrin-G",
      "It has a resting membrane potential that sits permanently at 0 mV"
    ],
    "answer": 2,
    "explain": "The axon initial segment concentrates Nav channels at densities 40- to 50-fold higher than the soma through direct binding to the scaffolding protein ankyrin-G, creating the lowest voltage threshold for action potential trigger.",
    "example": "Immunostaining for ankyrin-G and Nav1.6 reveals dense clustering across the proximal 20-40 μm of the axon.",
    "id": "nb-127",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Gap Junction Structure",
    "prompt": "Electrical synapses mediate direct, bidirectional, low-resistance ionic current flow between neurons through intercellular channels composed of:",
    "options": [
      "Clathrin triskelions assembling a physical bridge across the cleft",
      "SNARE protein four-helix bundles spanning the intercellular space",
      "Tetrameric NMDA receptor complexes contacting presynaptic vesicular proteins",
      "Two docked hemichannels (connexons), each formed by a hexamer of connexin subunits"
    ],
    "answer": 3,
    "explain": "An electrical synapse consists of a gap junction where two connexons (hemichannels)—each composed of six connexin proteins (predominantly Cx36 in mature mammalian neurons)—dock across the extracellular space.",
    "example": "Connexin-36 knockout mice exhibit loss of high-frequency gamma oscillations and desynchronized firing among inhibitory interneurons.",
    "id": "nb-128",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Chemical Synapse Synaptic Delay",
    "prompt": "The characteristic physiological delay (0.5 to 1.0 ms) observed between presynaptic action potential invasion and postsynaptic potential onset at a chemical synapse is primarily caused by:",
    "options": [
      "The time required for voltage-gated Ca2+ channels to open and trigger calcium-dependent vesicle fusion",
      "The time required for action potentials to travel down the dendritic spine neck",
      "The slow diffusion of small-molecule transmitters across the 20 nm synaptic cleft",
      "The time required to synthesize glutamate de novo from glutamine"
    ],
    "answer": 0,
    "explain": "While transmitter diffusion across the ~20 nm synaptic cleft takes only microseconds (~10-20 μs), the kinetic delay of Cav channel opening and the biochemical assembly of calcium-triggered SNARE fusion requires 0.5-1.0 ms.",
    "example": "Dual somatic patch recordings at 22°C show a ~1 ms synaptic delay that narrows to ~0.3 ms at physiological mammalian temperature (37°C).",
    "id": "nb-129",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Length Constant Definition",
    "prompt": "In passive cable theory, the length constant (lambda) of a dendrite or axon is defined as the distance over which a steady-state subthreshold voltage change decays to what percentage of its initial value?",
    "options": [
      "50% of its maximum amplitude",
      "1/e (~37%) of its maximum amplitude",
      "1/e^2 (~13.5%) of its maximum amplitude",
      "0% (complete dissipation)"
    ],
    "answer": 1,
    "explain": "The length constant lambda = sqrt(r_m / r_i), where r_m is membrane resistance and r_i is internal axial resistance. Over distance x = lambda, voltage drops exponentially to V_0 / e (~36.8%).",
    "example": "A thick apical dendrite with low axial resistance has a larger lambda (e.g., 500-1000 μm), allowing distal inputs to propagate electrotonically with less attenuation.",
    "id": "nb-130",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Time Constant Definition",
    "prompt": "The membrane time constant (tau = r_m * c_m) characterizes:",
    "options": [
      "The time it takes for a neurotransmitter molecule to be hydrolyzed by esterases",
      "The total duration of an action potential from threshold to baseline",
      "The time required for a membrane potential change to reach 1 - 1/e (~63%) of its final steady-state value in response to a current step",
      "The refractory period duration during maximum high-frequency firing"
    ],
    "answer": 2,
    "explain": "Tau characterizes the passive charging rate of the lipid bilayer capacitance through the membrane resistance. A longer tau allows wider temporal summation windows for incoming synaptic potentials.",
    "example": "Neurons with a long membrane time constant (e.g. 30 ms) summate asynchronous EPSPs arriving over several tens of milliseconds.",
    "id": "nb-131",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "SNARE Cleavage by Botulinum Neurotoxins",
    "prompt": "Botulinum neurotoxin serotype A (BoNT/A) permanently arrests acetylcholine release at the neuromuscular junction by specifically cleaving which core SNARE protein?",
    "options": [
      "Synaptotagmin-1",
      "Synaptobrevin-2 / VAMP2",
      "Syntaxin-1A",
      "SNAP-25 (cleaving nine amino acids from the C-terminus)"
    ],
    "answer": 3,
    "explain": "BoNT/A is a zinc endopeptidase whose light chain selectively cleaves the C-terminal peptide of SNAP-25, preventing the complete four-helix bundle zippering required for membrane fusion.",
    "example": "Intramuscular injection of BoNT/A produces flaccid paralysis that persists for months until new nerve terminals sprout and SNAP-25 is resynthesized.",
    "id": "nb-132",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Tetanus Toxin Retrograde Transport",
    "prompt": "Unlike Botulinum toxin, Tetanus neurotoxin (TeNT) causes spastic spasticity because it:",
    "options": [
      "Undergoes retrograde axonal transport to spinal motor neuron cell bodies and trans-synaptically enters inhibitory Renshaw cells to cleave VAMP2",
      "Directly activates acetylcholine receptors at the neuromuscular junction",
      "Blocks voltage-gated potassium channels throughout peripheral motor axons",
      "Destroys myelin sheaths in the dorsal columns of the spinal cord"
    ],
    "answer": 0,
    "explain": "TeNT is endocytosed at motor terminals, avoids acidification, undergoes dynein-dependent retrograde axonal transport to the spinal cord, and crosses synapses to cleave synaptobrevin-2 in inhibitory interneurons (Renshaw cells), abolishing glycine release and causing violent disinhibition.",
    "example": "Tetanus poisoning manifests as lockjaw (trismus) and generalized extensor spasms (opisthotonos) due to loss of spinal reciprocal inhibition.",
    "id": "nb-133",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Synaptotagmin C2 Domain Metal Coordination",
    "prompt": "The primary fast calcium sensor for synchronous exocytosis, Synaptotagmin-1, coordinates five Ca2+ ions across its tandem C2 domains (C2A and C2B) primarily through loops enriched in which amino acid residue?",
    "options": [
      "Arginine",
      "Aspartate (negatively charged carboxylate side chains)",
      "Leucine",
      "Cysteine"
    ],
    "answer": 1,
    "explain": "The C2A and C2B domains fold as eight-stranded beta-sandwiches. Conserved aspartate residues coordinate divalent Ca2+ ions without neutralizing charges until Ca2+ binds, whereupon hydrophobic loops insert into the anionic PIP2-rich plasma membrane.",
    "example": "Point mutations neutralizing aspartate residues (e.g. D232N in C2A) reduce calcium-binding affinity and severely depress evoked synchronous EPSCs.",
    "id": "nb-134",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Complexin Clamping Mechanism",
    "prompt": "What is the dual physiological function of the small presynaptic protein Complexin in neurotransmitter release?",
    "options": [
      "It degrades excess glutamate in the presynaptic cytosol",
      "It phosphorylates synapsin to release vesicles from the actin cytoskeleton",
      "It stabilizes partially assembled SNAREpins to clamp premature spontaneous fusion while priming vesicles for rapid calcium-triggered release",
      "It pumps protons into synaptic vesicles against their concentration gradient"
    ],
    "answer": 2,
    "explain": "Complexin binds the groove of the assembling trans-SNARE complex with its central alpha-helix, inserting an accessory helix that arrests full zippering (clamping spontaneous fusion) while aligning SNAREs for explosive fusion upon Ca2+ binding to synaptotagmin.",
    "example": "Complexin knockout in hippocampal neurons increases spontaneous mini EPSC frequency (unclamped mini release) while reducing evoked release amplitude.",
    "id": "nb-135",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Vesicle Acidification V-ATPase",
    "prompt": "The electrochemical driving force for loading neurotransmitters into synaptic vesicles is generated by which molecular pump?",
    "options": [
      "Calcium-activated potassium pump",
      "Na+/K+-ATPase on the vesicular membrane",
      "Mitochondrial F1F0 ATP synthase operating in reverse",
      "Vacuolar-type H+-ATPase (V-ATPase) hydrolyzing ATP to pump protons into the vesicle lumen"
    ],
    "answer": 3,
    "explain": "The vacuolar H+-ATPase pumps H+ into the lumen, generating both an electrical potential difference (inside positive) and a chemical pH gradient (inside acidic, pH ~5.6), which drive vesicular monoamine, glutamate, and GABA transporters.",
    "example": "Application of the specific V-ATPase inhibitor bafilomycin A1 rapidly dissipates the proton gradient, halting synaptic vesicle transmitter reloading.",
    "id": "nb-136",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Parvalbumin Fast-Spiking Interneuron Biophysics",
    "prompt": "Cortical parvalbumin-expressing (PV+) fast-spiking basket cells sustain high-frequency non-adapting firing (>150 Hz) primarily due to high expression of which potassium channel family?",
    "options": [
      "Kv3 family (Kv3.1 and Kv3.2) exhibiting depolarized activation thresholds and extremely fast deactivation kinetics",
      "Kv1.1 channels with ultra-slow inactivation",
      "KCNQ/Kv7 channels mediating slow M-currents",
      "Inward-rectifying Kir2.1 channels"
    ],
    "answer": 0,
    "explain": "Kv3 channels activate only at depolarized potentials (> -10 mV) and deactivate ultra-rapidly. This ensures rapid spike repolarization without creating a prolonged afterhyperpolarization, enabling instantaneous recovery of Nav channels for high-frequency firing.",
    "example": "Pharmacological blockade of Kv3 channels with low-dose TEA (0.1-1 mM) broadens PV cell action potentials and impairs high-frequency firing capabilities.",
    "id": "nb-137",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Somatostatin Martinotti Interneuron Circuit",
    "prompt": "In the neocortex, Martinotti cells are somatostatin-positive (SST+) GABAergic interneurons whose axons target which specific compartment of pyramidal neurons?",
    "options": [
      "The axon initial segment exclusively, blocking action potential generation",
      "Distal apical dendrites and tufts in Layer 1, providing feedback dendritic inhibition",
      "The cell soma perisomatically to control spike timing",
      "Postsynaptic dendritic spines on basal dendrites"
    ],
    "answer": 1,
    "explain": "Martinotti cells project their ascending axons up to Layer 1, arborizing across distal apical dendritic tufts of pyramidal neurons to regulate dendritic integration, NMDA plateau potentials, and calcium spikes.",
    "example": "In vivo two-photon imaging shows that SST interneuron activation controls dendritic calcium bursts during sensory perception.",
    "id": "nb-138",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "VIP Disinhibitory Microcircuit",
    "prompt": "Vasoactive intestinal peptide-expressing (VIP+) interneurons in the neocortex modulate local circuit activity primarily by:",
    "options": [
      "Directly terminating the primary thalamocortical sensory afferents",
      "Releasing glutamate directly onto layer 4 spiny stellate neurons",
      "Selectively inhibiting SST+ and PV+ GABAergic interneurons, thereby disinhibiting pyramidal projection neurons",
      "Forming electrical gap junctions exclusively with vascular smooth muscle cells"
    ],
    "answer": 2,
    "explain": "VIP+ interneurons receive top-down neuromodulatory and cortical inputs and synapse predominantly onto SST+ Martinotti and PV+ interneurons. By silencing these inhibitory cells, VIP interneurons disinhibit pyramidal dendrites, gating sensory transmission.",
    "example": "Optogenetic activation of auditory cortex VIP interneurons enhances auditory detection thresholds in behaving mice through dendritic disinhibition.",
    "id": "nb-139",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Endocannabinoid DSI / DSE Mechanism",
    "prompt": "Depolarization-Induced Suppression of Inhibition (DSI) and Depolarization-Induced Suppression of Excitation (DSE) are mediated by:",
    "options": [
      "Glutamate spillover to presynaptic kainate autoreceptors",
      "Vesicular release of anandamide from postsynaptic dendritic spines activating postsynaptic CB2 receptors",
      "Nitric oxide diffusion across gap junctions stimulating adenylyl cyclase",
      "Postsynaptic Ca2+ influx stimulating on-demand synthesis of 2-Arachidonoylglycerol (2-AG), which retrogradely activates presynaptic CB1 receptors to inhibit Cav channels"
    ],
    "answer": 3,
    "explain": "Strong postsynaptic depolarization triggers calcium influx that activates diacylglycerol lipase (DAGL-alpha) to synthesize 2-AG. Lipophilic 2-AG diffuses retrogradely across the cleft to bind presynaptic CB1 GPCRs, activating Gi/o to close presynaptic Cav channels and halt transmitter release.",
    "example": "Pre-incubation with the CB1 inverse agonist rimonabant (SR141716) completely blocks DSI in hippocampal CA1 pyramidal neurons.",
    "id": "nb-140",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Silent Synapses and LTP Unsilencing",
    "prompt": "What defines an electrophysiologically 'silent synapse' in the neonatal and developing mammalian hippocampus?",
    "options": [
      "A synapse containing postsynaptic NMDA receptors but lacking functional surface AMPA receptors at resting membrane potentials (-70 mV)",
      "A presynaptic terminal that contains synaptic vesicles but lacks synaptobrevin-2",
      "A synapse that transmits electrical current via gap junctions without chemical transmitters",
      "A dendritic spine where all receptors have undergone endosomal degradation"
    ],
    "answer": 0,
    "explain": "At resting membrane potentials (-70 mV), silent synapses pass no EPSC when stimulated because extracellular Mg2+ blocks NMDA receptors, and there are no surface AMPA receptors. LTP induction depolarizes the spine, relieves Mg2+ block, and triggers rapid insertion of GluA1-containing AMPARs, unsilencing the synapse.",
    "example": "In neonatal CA1 slices held at -70 mV, minimal stimulation yields all-or-none failures, whereas depolarizing the cell to +40 mV reveals robust NMDA receptor-mediated EPSCs.",
    "id": "nb-141",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Synaptic Tagging and Capture Hypothesis",
    "prompt": "According to the Synaptic Tagging and Capture hypothesis proposed by Uwe Frey and Richard Morris, how does a synapse maintain late-phase LTP (L-LTP) specifically?",
    "options": [
      "Each stimulated spine synthesizes its own nuclear envelope and transcribes mRNA locally without somatic input",
      "Weak stimulation sets a local synaptic 'tag' that captures cell-wide, newly synthesized plasticity-related proteins (PRPs) generated by strong stimulation at another input",
      "Retrograde neurotrophins destroy all untagged synapses in the same arbor",
      "Astrocytes physically seal the stimulated spine with an impermeable glial sheath"
    ],
    "answer": 1,
    "explain": "A weak tetanus induces a local, transient molecular tag (involving CaMKII, actin restructuring, and PKA) that lasts 1-2 hours. If a strong tetanus occurs at another pathway in the same neuron, triggering nuclear transcription of PRPs (e.g. PKMzeta, Homer1a), the tagged synapse captures these PRPs to establish permanent L-LTP.",
    "example": "Stimulating Pathway S1 weakly produces decaying E-LTP, but delivering strong L-LTP tetanus to Pathway S2 within 60 minutes converts S1 into persistent L-LTP (behavioral tagging).",
    "id": "nb-142",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Spreading Depolarization Electrophysiology",
    "prompt": "Cortical spreading depolarization (CSD), the pathophysiological substrate of migraine aura and stroke penumbral damage, is characterized by:",
    "options": [
      "Sudden synchronous hyperpolarization of all neocortical neurons below -120 mV",
      "A rapid traveling wave of high-frequency epileptic discharges propagating at 100 meters per second",
      "A slow-moving (~2-5 mm/min) wave of near-complete cellular depolarization, loss of ion homeostasis, massive extracellular K+ elevation (>50 mM), and electrocorticographic depression",
      "Instantaneous demyelination of white matter tracts across both hemispheres"
    ],
    "answer": 2,
    "explain": "CSD occurs when local metabolic exhaustion or excessive K+ release overwhelms astrocytic clearance, triggering positive-feedback opening of Nav and NMDA channels. The membrane potential collapses to near 0 mV, extracellular K+ surges to 50-80 mM, and spontaneous EEG activity is silenced (spreading depression).",
    "example": "Subdural strip electrodes in traumatic brain injury patients detect slow negative DC potential shifts corresponding to spreading depolarizations that exacerbate secondary ischemic lesions.",
    "id": "nb-143",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Thalamocortical Burst vs Tonic Firing",
    "prompt": "Thalamocortical relay neurons switch between single-spike tonic firing and rhythmic burst firing depending on the state of which low-threshold calcium channel?",
    "options": [
      "Ryanodine receptors on the mitochondrial inner membrane",
      "L-type calcium channels (Cav1.2), which require severe hyperpolarization to open",
      "P/Q-type channels (Cav2.1), which require zinc co-binding",
      "T-type calcium channels (Cav3.1), which inactivate at depolarized resting potentials and deinactivate only upon prolonged membrane hyperpolarization"
    ],
    "answer": 3,
    "explain": "At depolarized resting potentials (-60 mV during awake states), Cav3.1 channels are inactivated, so inputs elicit single spikes (tonic mode). During slow-wave sleep or anesthesia, sustained hyperpolarization below -70 mV relieves inactivation (deinactivation), allowing subsequent depolarizations to trigger low-threshold Ca2+ spikes topped by high-frequency sodium bursts.",
    "example": "Application of nickel or the selective T-type blocker TTA-P2 abolishes low-threshold burst firing in thalamic slices without altering baseline resting potential.",
    "id": "nb-144",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Optogenetic Inactivation Biophysics",
    "prompt": "Unlike the hyperpolarizing light-driven chloride pump Halorhodopsin (NpHR), the outward proton pump Archaerhodopsin (ArchT) silences neurons without:",
    "options": [
      "Causing a collapse of the intracellular chloride gradient that can induce paradoxical rebound excitation upon light termination",
      "Requiring all-trans retinal as a chromophore",
      "Consuming photons in the visible spectrum",
      "Altering intracellular pH"
    ],
    "answer": 0,
    "explain": "Sustained activation of NpHR pumps large quantities of Cl- into the cytoplasm, shifting the GABA-A reversal potential (E_Cl) in a depolarizing direction, which can trigger paradoxical rebound firing when the light turns off. Arch silences cells by extruding protons (H+), avoiding intracellular chloride loading.",
    "example": "Whole-cell recordings during sustained 10-second yellow light pulses demonstrate stable, rebound-free hyperpolarization in Arch-expressing cortical pyramidal neurons.",
    "id": "nb-145",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Substantia Nigra Autonomous Pacemaking",
    "prompt": "Dopaminergic neurons of the substantia nigra pars compacta generate continuous autonomous pacemaking (1-4 Hz) in the absence of synaptic input driven in part by:",
    "options": [
      "High-frequency gap junctional drive from neighboring astrocytes",
      "Subthreshold activation of low-voltage-activated L-type Ca2+ channels (Cav1.3) interacting with SK channels and HCN channels",
      "Continuous spontaneous exocytosis of GABA from local axon collaterals",
      "Rhythmic influx of chloride ions through resting glycine receptors"
    ],
    "answer": 1,
    "explain": "Cav1.3 channels activate at unusually hyperpolarized potentials (~ -50 mV). In SNc dopaminergic neurons, sustained Cav1.3 Ca2+ influx drives rhythmic depolarizations that trigger sodium spikes, followed by SK channel activation to hyperpolarize the membrane and restart the cycle, causing high basal mitochondrial oxidative stress.",
    "example": "Dihydropyridines such as isradipine selectively antagonize Cav1.3 channels, converting pacemaking from Ca2+-driven to less metabolically stressful Na+-driven firing.",
    "id": "nb-146",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Trans-Synaptic Splice Code Neurexin-Neuroligin",
    "prompt": "How does alternative splicing at site 4 (SS#4) of presynaptic neurexins dictate postsynaptic receptor recruitment across the synaptic cleft?",
    "options": [
      "Alternative splicing at SS#4 alters voltage-dependent gating of Cav2.1 channels",
      "Insertion of SS#4 causes immediate proteolytic cleavage of neurexin by secretases",
      "Neurexin isoforms lacking insert SS#4 selectively bind neuroligin-1 to recruit NMDA/AMPA receptors, whereas insertion of SS#4 switches affinity toward cerebellin-GluD complexes and LRRTM2",
      "SS#4 inclusion changes neurexin from a transmembrane protein into a soluble extracellular hormone"
    ],
    "answer": 2,
    "explain": "Neurexin alternative splicing functions as a molecular master switch. Neurexin-1 lacking SS#4 binds neuroligin-1 with high affinity to organize postsynaptic PSD-95 and AMPA/NMDA complexes, whereas inclusion of SS#4 sterically impairs neuroligin-1 binding and enables selective binding to Cerebellins (Cbln1/2) that bridge to postsynaptic GluD receptors.",
    "example": "Knock-in mice engineered to constitutively express Neurexin-1 with SS#4 display selective impairment of Schaffer collateral LTP and altered AMPA receptor synaptic recruitment.",
    "id": "nb-147",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Munc13 MUN Domain Catalytic Opening",
    "prompt": "During synaptic vesicle priming, the essential priming factor Munc13-1 converts syntaxin-1 from its closed default conformation to an open SNARE-competent state through its conserved:",
    "options": [
      "Pleckstrin homology domain that hydrolyzes PIP2",
      "Zinc-finger domain that phosphorylates SNAP-25",
      "C2A domain that cleaves synaptobrevin-2",
      "MUN domain, which physically accelerates the transition of closed syntaxin-1-Munc18-1 complexes into productive core SNARE bundles"
    ],
    "answer": 3,
    "explain": "Munc18-1 initially holds syntaxin-1 in a closed auto-inhibitory conformation. The ~500-amino acid elongated MUN domain of Munc13 acts as a molecular chaperone, dislodging the inhibitory syntaxin Habc domain to allow syntaxin's SNARE motif to assemble into a four-helix bundle with SNAP-25 and synaptobrevin-2.",
    "example": "Munc13-1/2 double-knockout neurons exhibit total paralysis of both evoked and spontaneous neurotransmitter release, despite containing morphologically docked vesicles.",
    "id": "nb-148",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Glymphatic Sleep-Wake Interstitial Dynamics",
    "prompt": "Maiken Nedergaard's landmark studies established that the glymphatic clearance of interstitial waste products (such as A-beta and tau) increases by >60% during natural sleep primarily because:",
    "options": [
      "Locus coeruleus noradrenergic tone drops dramatically, expanding the cortical interstitial space volume fraction from ~14% to ~23%",
      "Astrocytes undergo rapid apoptosis and regenerate every morning",
      "The blood-brain barrier becomes porous to large proteins during non-REM sleep",
      "Arterial pulsatility ceases entirely during slow-wave sleep"
    ],
    "answer": 0,
    "explain": "High noradrenergic output during wakefulness maintains cell swelling and compresses the interstitial space. During NREM slow-wave sleep or ketamine/xylazine anesthesia, noradrenaline levels plummet, causing interstitial space expansion and facilitating convective bulk CSF-ISF flow driven by arterial pulsations and astrocytic AQP4 water channels.",
    "example": "In vivo two-photon imaging of fluorescent CSF tracers in mouse neocortex reveals 2-fold faster tracer influx and clearance during sleep compared to wakefulness.",
    "id": "nb-149",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Ultrafast Endocytosis Kinetics",
    "prompt": "Using flash-and-freeze electron microscopy, Erik Jorgensen and colleagues revealed that at physiological temperatures (37°C), synaptic vesicle endocytosis occurs via:",
    "options": [
      "Direct clathrin coat assembly on single fusing vesicles within 1 millisecond",
      "Ultrafast endocytosis within 50 to 100 milliseconds at the lateral active zone edges, forming large endocytic vacuoles that resolve via clathrin-dependent budding at synaptic endosomes",
      "Total retrograde axonal transport of the entire fused plasma membrane back to the soma",
      "Direct mechanical retraction of the fused vesicle without membrane fission"
    ],
    "answer": 1,
    "explain": "Unlike classic clathrin-mediated endocytosis which takes 10-30 seconds, ultrafast endocytosis invaginates large 80-nm vesicles at active zone borders within 50-100 ms in an actin- and dynamin-dependent manner. These large vacuoles subsequently travel to synaptic endosomes, where classic clathrin machinery buds mature 40-nm synaptic vesicles over ~5 seconds.",
    "example": "High-pressure freezing of optogenetically stimulated hippocampal slices at 100 ms reveals prominent invaginations lacking clathrin coats flanking the active zone.",
    "id": "nb-150",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Dendritic Calcium Spike Generation",
    "prompt": "In Layer 5 thick-tufted neocortical pyramidal neurons, back-propagating action potentials (bAPs) coincide with distal apical inputs to trigger a regenerative dendritic calcium spike (BAC firing) mediated by:",
    "options": [
      "Complete opening of all somatic potassium leak channels",
      "Direct activation of astrocytic Ryanodine receptors across the glia limitans",
      "L-type and P/Q-type calcium channels clustered in the apical trunk bifurcation hot spot, generating a prolonged plateau potential and somatic burst firing",
      "Immediate retrograde action potential generation from the axon terminal"
    ],
    "answer": 2,
    "explain": "Larkum and colleagues demonstrated BAC (bAP-activated Ca2+ spike) firing: a somatic action potential back-propagating up the apical trunk meets subthreshold synaptic input at the apical tuft, crossing threshold for low-voltage Cav channels in an apical 'hot zone' to trigger a ~30 ms calcium plateau that drives somatic spike bursts.",
    "example": "Dual patch-clamp recordings from the soma and apical dendritic bifurcation 600 μm away demonstrate BAC firing, functioning as a cellular coincidence detector between bottom-up sensory and top-down feedback inputs.",
    "id": "nb-151",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 5,
    "topic": "Astrocytic Spatial Potassium Buffering Biophysics",
    "prompt": "During intense neuronal activity, astrocytes clear extracellular K+ via Kir4.1 channels and distribute it through the astrocytic syncytium in a process driven by:",
    "options": [
      "Direct phosphorylation of myelin sheath proteins by extracellular kinases",
      "Active endocytosis of K+ ions into lysosomes for vesicular secretion into the bloodstream",
      "Reverse transport of K+ through sodium-calcium exchangers",
      "Connexin-43/30 gap junctional coupling and electrodiffusive current loops where K+ enters at sites of high [K+]o and exits at distant lower concentration sites"
    ],
    "answer": 3,
    "explain": "Astrocytes have a hyperpolarized resting potential (-85 mV) governed by Kir4.1. Local K+ surges shift the local K+ equilibrium potential depolarizing the local astrocyte membrane, generating a syncytial current loop through Cx43/Cx30 gap junctions that drives K+ efflux at distant resting astrocytic endfeet.",
    "example": "Conditional knockout of astrocytic Kir4.1 impairs extracellular K+ clearance, slows EPSC decay times, and leads to spontaneous epileptic seizures in mice.",
    "id": "nb-152",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Pyramidal Decussation Neuroanatomy",
    "prompt": "Approximately 85-90% of descending corticospinal motor fibers cross the anatomical midline to form the lateral corticospinal tract at the:",
    "options": [
      "Pyramidal decussation in the caudal medulla oblongata",
      "Optic chiasm in the diencephalon",
      "Corpus callosum in the telencephalon",
      "Pons at the level of the middle cerebellar peduncles"
    ],
    "answer": 0,
    "explain": "The corticospinal tract descends through the internal capsule, cerebral peduncles, and ventral pons into the medullary pyramids, where ~85-90% of axons decussate in the caudal medulla to descend in the contralateral lateral funiculus of the spinal cord.",
    "example": "A lesion in the left precentral gyrus above the decussation produces spastic hemiparesis on the contralateral (right) side of the body.",
    "id": "nb-153",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 1,
    "topic": "Dorsal Column-Medial Lemniscal Pathway",
    "prompt": "Conscious discriminative touch, proprioception, and vibration from the lower extremities travel via which spinal cord fasciculus before synapsing in the medulla?",
    "options": [
      "Fasciculus cuneatus (lateral dorsal column)",
      "Fasciculus gracilis (medial dorsal column)",
      "Lateral spinothalamic tract",
      "Ventral spinocerebellar tract"
    ],
    "answer": 1,
    "explain": "Sensory afferents from lower limb dermatomes (below T6) travel ascendingly in the medial fasciculus gracilis to synapse on the nucleus gracilis. Afferents from upper extremities (T6 and above) ascend in the lateral fasciculus cuneatus to the nucleus cuneatus.",
    "example": "Tabes dorsalis in neurosyphilis selectively degenerates the dorsal columns, causing sensory ataxia and loss of proprioception (positive Romberg test).",
    "id": "nb-154",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Magnocellular vs Parvocellular Visual Pathways",
    "prompt": "In the primate lateral geniculate nucleus (LGN), magnocellular neurons (layers 1 and 2) are functionally distinguished from parvocellular neurons (layers 3 through 6) by having:",
    "options": [
      "High spatial acuity and sustained firing responses to stationary fine details",
      "Exquisite color selectivity for red-green spectral differences",
      "Larger receptive fields, high transient sensitivity to motion and luminance contrast, and faster axonal conduction velocities",
      "Insensitivity to all moving visual stimuli"
    ],
    "answer": 2,
    "explain": "Magnocellular cells receive parasol retinal ganglion cell inputs, processing low spatial frequency, high temporal frequency (motion, flicker), and low-contrast stimuli. Parvocellular cells receive midget ganglion inputs, processing high spatial resolution and color.",
    "example": "Focal ibotenic acid lesions of the magnocellular LGN layers in monkeys selectively impair motion detection while sparing visual color discrimination.",
    "id": "nb-155",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Olfactory Receptor One-Neuron-One-Receptor Rule",
    "prompt": "Linda Buck and Richard Axel demonstrated that mammalian olfactory sensory neurons (OSNs) achieve odorant discrimination by:",
    "options": [
      "Translating odorant receptors only after physical binding to odorant molecules",
      "Expressing all 1,000 receptor genes uniformly in every sensory neuron",
      "Using alternative splicing of a single universal olfactory mRNA",
      "Expressing exclusively one functional odorant receptor gene chosen from ~1,000 genes via singular monoallelic expression"
    ],
    "answer": 3,
    "explain": "Each mammalian olfactory receptor neuron chooses and stably transcribes only one allele of a single olfactory receptor (OR) gene out of ~1,000 genes, and all neurons expressing the same OR converge their axons onto two stereotypic glomeruli in the olfactory bulb.",
    "example": "Targeted gene deletion of a specific OR gene in mice abolishes axonal convergence onto its designated olfactory bulb glomeruli.",
    "id": "nb-156",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Alpha7 Nicotinic Receptor Ca2+ Permeability",
    "prompt": "The homopentameric alpha7 nicotinic acetylcholine receptor (alpha7 nAChR) is distinguished from heteropentameric alpha4beta2 receptors by its:",
    "options": [
      "Exceptionally high Ca2+ permeability, fast desensitization kinetics, and selective blockade by alpha-bungarotoxin",
      "Impermeability to all divalent cations",
      "Total resistance to alpha-bungarotoxin and picomolar affinity for nicotine",
      "Coupling to heterotrimeric Gq proteins rather than forming an ion channel"
    ],
    "answer": 0,
    "explain": "Alpha7 receptors form homopentamers characterized by high relative Ca2+ permeability (P_Ca/P_Na ~10-20, comparable to NMDA receptors), rapid activation and desensitization, and high-affinity irreversible blockade by snake toxin alpha-bungarotoxin.",
    "example": "Presynaptic alpha7 nAChRs on hippocampal mossy fibers facilitate glutamate release through direct Ca2+ influx during cholinergic septal activation.",
    "id": "nb-157",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Adenosine A1 Receptor Presynaptic Inhibition",
    "prompt": "Caffeine promotes wakefulness and alertness primarily by acting as an antagonist at which receptor class in the central nervous system?",
    "options": [
      "GABA-A receptors at the benzodiazepine modulatory site",
      "Adenosine A1 and A2A receptors, preventing endogenous adenosine from suppressing excitatory neurotransmission",
      "Dopamine D2 autoreceptors, stimulating dopamine synthesis",
      "Postsynaptic AMPA glutamate receptors"
    ],
    "answer": 1,
    "explain": "Endogenous adenosine accumulates during prolonged wakefulness, binding presynaptic Gi-coupled A1 receptors to suppress excitatory transmitter release. Caffeine competitively blocks A1 and A2A receptors, preventing adenosine-mediated sleep pressure.",
    "example": "Transgenic mice lacking adenosine A1 receptors show markedly reduced somnogenic responses to prolonged sleep deprivation.",
    "id": "nb-158",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 2,
    "topic": "Radial Glia and Cortical Neurogenesis",
    "prompt": "During mammalian neocortical development, ventricular radial glial cells (vRGs) serve as primary neural stem cells by undergoing:",
    "options": [
      "Apoptosis to create the ventricular fluid cavity",
      "Permanent symmetric division producing only mature astrocytes",
      "Asymmetric division to self-renew while generating either an intermediate progenitor cell (IPC) or a nascent neuron that migrates along the radial glial fiber",
      "Direct transdifferentiation into microglial cells"
    ],
    "answer": 2,
    "explain": "Radial glia span the ventricular zone to the pial surface. They divide asymmetrically at the apical ventricular surface: one daughter cell maintains radial glia identity while the other becomes a postmitotic neuroblast or an intermediate progenitor cell.",
    "example": "Time-lapse imaging in embryonic slice cultures demonstrates migrating neuroblasts using the basal process of radial glia as a scaffold to reach the cortical plate.",
    "id": "nb-159",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Perineuronal Nets and Critical Period Closure",
    "prompt": "In the postnatal visual cortex, the end of the critical period for ocular dominance plasticity is physically stabilized by the consolidation of perineuronal nets (PNNs) around which cell type?",
    "options": [
      "Myelin-producing mature oligodendrocytes",
      "Layer 1 Cajal-Retzius pioneer neurons",
      "Microglial cells surveying cortical capillaries",
      "Parvalbumin-expressing (PV+) fast-spiking basket interneurons"
    ],
    "answer": 3,
    "explain": "PNNs are dense extracellular matrix specialized coats composed of chondroitin sulfate proteoglycans (CSPGs like aggrecan) and tenascins that wrap PV+ soma and proximal dendrites. They restrict structural synaptic remodeling and seal critical period plasticity.",
    "example": "Enzymatic digestion of PNNs in adult visual cortex with chondroitinase ABC restores juvenile-like ocular dominance plasticity in response to monocular deprivation.",
    "id": "nb-160",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Cajal-Retzius Cells and Reelin Signaling",
    "prompt": "During embryonic corticogenesis, transient Cajal-Retzius cells residing in the marginal zone secrete the large extracellular glycoprotein Reelin to:",
    "options": [
      "Bind VLDLR and ApoER2 receptors on migrating neuroblasts, driving Dab1 phosphorylation to instruct inside-out cortical layering",
      "Trigger programmed cell death of all layer 5 projection neurons",
      "Promote angiogenesis by binding VEGF receptors on endothelial cells",
      "Induce immediate premature myelination of subplate axons"
    ],
    "answer": 0,
    "explain": "Reelin binds ApoER2 and VLDLR receptors on migrating projection neurons, recruiting and phosphorylating Disabled-1 (Dab1) via Src family kinases. This signals migrating neurons to detach from radial glial fibers and arrest, generating an 'inside-out' laminar architecture.",
    "example": "The 'reeler' mutant mouse lacks functional Reelin, resulting in an inverted cortical lamination where older neurons occupy superficial layers.",
    "id": "nb-161",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Axon Guidance Midline Crossing",
    "prompt": "Spinal commissural axons are attracted toward the ventral floor plate by Netrin-1 binding to DCC receptors, but cross the midline without turning back because:",
    "options": [
      "Netrin-1 is irreversibly degraded by proteases at the exact moment of crossing",
      "Upon crossing, surface expression of Robo1/2 receptors is upregulated, enabling floor-plate Slit proteins to repel the axon away from the midline",
      "Axon growth cones permanently lose all actin filaments at the midline",
      "DCC receptors switch from binding Netrin to binding myelin-associated glycoprotein"
    ],
    "answer": 1,
    "explain": "Pre-crossing axons express DCC (attracted to Netrin-1) while Robo repulsion is silenced by Rig-1/Robo3. Once axons cross the midline, Robo1 and Robo2 are displayed on the growth cone surface, binding floor-plate Slit ligands to mediate strong repulsion that prevents re-crossing.",
    "example": "In Robo mutant flies, commissural axons circle the midline repeatedly without exiting, giving rise to the characteristic 'roundabout' phenotype.",
    "id": "nb-162",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Semaphorin-Plexin Growth Cone Collapse",
    "prompt": "Secreted class 3 semaphorins (such as Sema3A) induce growth cone collapse and axon repulsion by binding to a receptor complex consisting of:",
    "options": [
      "EphA4 and Ephrin-B2 ligands",
      "TrkB and p75 neurotrophin receptors",
      "Neuropilin-1 (ligand-binding obligate coreceptor) and Plexin-A1 (intracellular signaling subunit)",
      "L1-CAM and NCAM neural adhesion molecules"
    ],
    "answer": 2,
    "explain": "Sema3A cannot bind plexins directly; it requires Neuropilin-1 as a high-affinity binding partner, which then complexes with Plexin-A1. Plexin-A1 activates intracellular GTPase-activating proteins (GAPs) for R-Ras, leading to F-actin depolymerization and growth cone collapse.",
    "example": "Adding 10 nM recombinant Sema3A to cultured sensory DRG growth cones causes rapid retraction of filopodia and lamellipodial collapse within 5 minutes.",
    "id": "nb-163",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Hyperekplexia Glycine Receptor Alpha1 Mutation",
    "prompt": "Hereditary hyperekplexia (startle disease), characterized by severe neonatal muscle rigidity and exaggerated startle responses to tactile stimuli, is caused by loss-of-function mutations in:",
    "options": [
      "GABRA1, encoding the GABA-A receptor alpha1 subunit",
      "SCN1A, encoding the Nav1.1 sodium channel",
      "GRIN2B, encoding the GluN2B NMDA receptor subunit",
      "GLRA1, encoding the ligand-binding alpha1 subunit of the strychnine-sensitive inhibitory glycine receptor"
    ],
    "answer": 3,
    "explain": "GLRA1 point mutations (such as R271Q/L) disrupt glycine binding or chloride pore opening in pentameric GlyRs in the brainstem and spinal cord. Without glycinergic reciprocal inhibition, motor neurons hyper-respond to sensory triggers.",
    "example": "Patients with hyperekplexia show dramatic symptomatic reduction in stiffness and life-threatening apneic spells when treated with the GABA-A PAM clonazepam.",
    "id": "nb-164",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Classical Psychedelics and 5-HT2A Signaling",
    "prompt": "Classical serotonergic psychedelics (such as psilocybin, LSD, and DMT) produce their profound perceptual and subjective effects primarily by acting as agonists at:",
    "options": [
      "5-HT2A receptors expressed abundantly on the apical dendrites of Layer 5 neocortical pyramidal neurons",
      "5-HT1A somatodendritic autoreceptors in the dorsal raphe nucleus exclusively",
      "5-HT3 ionotropic ligand-gated cation channels",
      "Dopamine D1 receptors in the nucleus accumbens core"
    ],
    "answer": 0,
    "explain": "5-HT2A is a Gq-coupled GPCR concentrated on deep layer 5 pyramidal neurons. Agonist binding stimulates PLC and triggers calcium-dependent asynchronous glutamate release, desynchronizing spontaneous cortical oscillatory patterns.",
    "example": "Pretreatment with the selective 5-HT2A antagonist ketanserin completely abolishes both the visual hallucinations in humans and the head-twitch response in rodents.",
    "id": "nb-165",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 3,
    "topic": "Auditory Coincidence Detection in MSO",
    "prompt": "In the auditory brainstem, the medial superior olive (MSO) computes sound source azimuth for low-frequency tones (<1.5 kHz) based on:",
    "options": [
      "Interaural level differences (ILD) calculated by lateral superior olive (LSO) neurons",
      "Interaural time differences (ITD) calculated by binaural coincidence-detector neurons receiving delay-line inputs from spherical bushy cells",
      "Phase cancellation of bone-conducted acoustic waves in the cochlear apex",
      "Doppler shift analysis in the inferior colliculus"
    ],
    "answer": 1,
    "explain": "Lloyd Jeffress' model describes axonal delay lines projecting from bilateral cochlear nuclei onto MSO coincidence detectors. An MSO neuron fires maximally only when action potentials from both ears arrive simultaneously at its soma, encoding microsecond-level ITDs.",
    "example": "Whole-cell recordings from gerbil MSO neurons demonstrate sub-millisecond precision in spike timing tuned to specific microsecond interaural delays.",
    "id": "nb-166",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Protocadherin Combinatorial Diversity",
    "prompt": "Mammalian clustered protocadherins (Pcdh-alpha, beta, and gamma clusters) provide an indispensable molecular code for:",
    "options": [
      "Voltage-gated potassium channel inactivation gating",
      "Direct vesicular packaging of biogenic amines",
      "Single-neuron dendritic self-avoidance and synaptic specificity through combinatorial homophilic binding",
      "GABAergic interneuron tangential migration from the ganglionic eminences"
    ],
    "answer": 2,
    "explain": "Each neuron stochastically expresses a unique combination of ~58 clustered protocadherins, assembling multi-protein homophilic recognition units. When sister dendrites from the same neuron contact each other, identical Pcdh complexes bind homophilically to trigger contact repulsion (self-avoidance).",
    "example": "Genetic deletion of the entire Pcdh-gamma cluster in mice causes severe loss of spinal interneurons and extensive dendritic self-clumping in retinal starburst amacrine cells.",
    "id": "nb-167",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Climbing Fiber Synapse Elimination",
    "prompt": "During early postnatal development of the mouse cerebellum, Purkinje cells transition from being innervated by multiple climbing fibers to a single climbing fiber through:",
    "options": [
      "Total genetic silencing of the inferior olivary complex",
      "Apoptosis of all inferior olive neurons except one per hemisphere",
      "Conversion of excess climbing fibers into parallel fibers",
      "Activity-dependent competition where the strongest climbing fiber translocates to the dendritic arbor while weaker somatic inputs are pruned"
    ],
    "answer": 3,
    "explain": "At birth, each Purkinje cell is contacted by 3-5 climbing fibers on its soma. Postnatal functional competition driven by Cav2.1 Ca2+ influx and GluD2/Cbln1 signaling allows the dominant input to translocate to the dendrite and eliminate the others by P21.",
    "example": "Purkinje-cell-specific Cav2.1 knockout mice retain persistent multi-innervation of Purkinje cells by multiple climbing fibers throughout adulthood.",
    "id": "nb-168",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Synaptic Scaling Multiplicative Homeostasis",
    "prompt": "Gina Turrigiano's classical demonstration of homeostatic synaptic scaling showed that chronic activity deprivation (e.g. 48 hours of TTX) leads to:",
    "options": [
      "A multiplicative, proportional increase in the amplitudes of all miniature EPSCs across the entire neuron, preserving relative synaptic weight relationships",
      "An all-or-none silencing of 90% of dendritic spines",
      "A collapse of resting membrane potential to 0 mV",
      "Complete downregulation of postsynaptic GluA1 and GluA2 AMPA receptors"
    ],
    "answer": 0,
    "explain": "Unlike Hebbian plasticity which is input-specific and positive-feedback, synaptic scaling is cell-wide and negative-feedback. Chronic TTX upregulates postsynaptic AMPARs multiplicatively (scaled by a constant factor), stabilizing somatic firing rates while preserving stored memory weights.",
    "example": "Plotting rank-ordered mEPSC amplitudes before and after TTX treatment reveals a linear scaling function with a slope > 1.0 (multiplicative up-scaling).",
    "id": "nb-169",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Synaptic Homeostasis Hypothesis of Sleep",
    "prompt": "According to Giulio Tononi and Chiara Cirelli's Synaptic Homeostasis Hypothesis (SHY), the primary physiological function of slow-wave sleep is to:",
    "options": [
      "Synthesize massive new dendritic spines to double total synaptic connections",
      "Renormalize overall synaptic strength through widespread, energy-conserving net down-selection (downscaling) of synaptic weights potentiated during wakefulness",
      "Permanently erase all memories acquired during the prior 24 hours",
      "Suppress all protein synthesis throughout the neocortex"
    ],
    "answer": 1,
    "explain": "Wakefulness is associated with net synaptic potentiation across cortical networks, which consumes substantial energy and cellular space. Slow-wave sleep oscillations promote coordinated, baseline-restoring synaptic downscaling, consolidating strong memories while pruning weak connections.",
    "example": "Serial section electron microscopy of mouse motor cortex reveals an ~18% decrease in axon-spine interface contact area after a sleep period compared to prolonged wakefulness.",
    "id": "nb-170",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Basal Ganglia Hyperdirect Pathway",
    "prompt": "In the basal ganglia, the 'hyperdirect pathway' enables rapid, emergency motor cancellation ('stopping') by projecting directly from:",
    "options": [
      "The globus pallidus internus directly to the primary somatosensory cortex",
      "The substantia nigra pars compacta directly to spinal alpha motor neurons",
      "The cortex (pre-SMA and inferior frontal gyrus) directly to the subthalamic nucleus (STN), bypassing the striatum",
      "The cerebellar dentate nucleus directly to the striatal patch compartment"
    ],
    "answer": 2,
    "explain": "While the striatal indirect pathway involves a multi-synaptic delay (Cortex -> Striatum -> GPe -> STN -> GPi), the hyperdirect pathway sends fast, monosynaptic glutamatergic projections from cortical motor areas straight to the STN, exciting the GPi to rapidly abort initiated actions.",
    "example": "Stop-signal reaction time tasks in humans during fMRI reveal transient activation of the right inferior frontal cortex and STN preceding successful motor inhibition.",
    "id": "nb-171",
    "mode": "neurobiology",
    "type": "choice"
  },
  {
    "level": 4,
    "topic": "Lateral Habenula Aversive Circuit",
    "prompt": "Neurons in the lateral habenula (LHb) increase their firing rate in response to:",
    "options": [
      "High-frequency auditory tones in the ultrasonic range",
      "Unexpectedly large, pleasurable dopamine surges",
      "Warm ambient environmental temperatures",
      "Negative reward prediction errors (omission of an expected reward or delivery of an aversive punishment)"
    ],
    "answer": 3,
    "explain": "LHb neurons signal disappointment and aversion. When an expected reward is omitted, LHb neurons fire bursts that project to the GABAergic rostromedial tegmental nucleus (RMTg / tail of the VTA), which strongly inhibits midbrain dopaminergic neurons.",
    "example": "Electrophysiological recordings in primates performing reward tasks demonstrate rapid suppression of VTA dopamine neuron firing following burst activation in LHb.",
    "id": "nb-172",
    "mode": "neurobiology",
    "type": "choice"
  }
];
