# scripts/bank_neurogenetics.py
"""
Neurogenetics Question Bank (172 Curated Questions)
"""

QUESTIONS = [
  {
    "id": "ng-001",
    "mode": "neurogenetics",
    "level": 1,
    "type": "choice",
    "topic": "Trinucleotide Repeat Expansion",
    "prompt": "Huntington's disease is caused by an unstable trinucleotide repeat expansion in the HTT gene. Which repeat sequence is expanded?",
    "options": [
      "CGG",
      "CAG",
      "GAA",
      "CTG"
    ],
    "answer": 1,
    "explain": "Huntington's disease is an autosomal dominant neurodegenerative disorder caused by expansion of a CAG trinucleotide repeat (encoding a polyglutamine tract) in exon 1 of the HTT gene, with repeats >36-40 conferring full penetrance.",
    "example": "Huntington's chorea and striatal medium spiny neuron degeneration correlate inversely with age of onset as CAG repeat length increases beyond 40."
  },
  {
    "id": "ng-002",
    "mode": "neurogenetics",
    "level": 1,
    "type": "choice",
    "topic": "Down Syndrome Neuropathology",
    "prompt": "Individuals with Down syndrome (Trisomy 21) virtually all develop Alzheimer's disease neuropathology by age 40 because which gene is located on chromosome 21?",
    "options": [
      "MAPT (Microtubule-associated protein tau)",
      "PSEN1 (Presenilin-1)",
      "APP (Amyloid Precursor Protein)",
      "APOE (Apolipoprotein E)"
    ],
    "answer": 2,
    "explain": "The APP gene resides on chromosome 21. Trisomy 21 confers a 1.5-fold gene dosage increase in APP expression from birth, leading to lifelong overproduction of amyloid-beta and universal plaque deposition by the fourth decade of life.",
    "example": "Duplication of the APP locus alone on chromosome 21 is sufficient to cause early-onset familial Alzheimer's disease with cerebral amyloid angiopathy."
  },
  {
    "id": "ng-003",
    "mode": "neurogenetics",
    "level": 1,
    "type": "choice",
    "topic": "Fragile X Syndrome",
    "prompt": "Fragile X syndrome, the most common inherited cause of intellectual disability and autism, is caused by transcriptional silencing of FMR1 due to:",
    "options": [
      "A missense point mutation in the kinase domain",
      "An expansion of >200 CGG repeats in the 5' UTR leading to hypermethylation",
      "Complete deletion of the mitochondrial genome",
      "Premature termination in the polyadenylation signal"
    ],
    "answer": 1,
    "explain": "When the CGG repeat expansion in the 5' untranslated region of FMR1 exceeds 200 copies (full mutation), extensive DNA hypermethylation of the promoter occurs, silencing FMR1 transcription and eliminating FMRP, an essential mRNA-binding translational repressor.",
    "example": "Absence of FMRP in Fragile X mice results in exaggerated mGluR5-dependent LTD and abnormal long, immature dendritic spines."
  },
  {
    "id": "ng-004",
    "mode": "neurogenetics",
    "level": 1,
    "type": "choice",
    "topic": "Familial AD Inheritance",
    "prompt": "Autosomal dominant early-onset familial Alzheimer's disease (FAD) is caused by fully penetrant mutations in which three genes?",
    "options": [
      "APP, PSEN1, and PSEN2",
      "APOE, TREM2, and BIN1",
      "SNCA, LRRK2, and PRKN",
      "SOD1, TARDBP, and C9orf72"
    ],
    "answer": 0,
    "explain": "Monogenic FAD is caused by mutations in APP (chromosome 21), Presenilin-1 (PSEN1, chromosome 14), or Presenilin-2 (PSEN2, chromosome 1). All three gene products converge directly on the processing of APP to alter Aβ production or elevate the Aβ42/Aβ40 ratio.",
    "example": "PSEN1 mutations account for the largest proportion of familial early-onset AD, often manifesting clinically before age 50."
  },
  {
    "id": "ng-005",
    "mode": "neurogenetics",
    "level": 1,
    "type": "choice",
    "topic": "Central Dogma & Splicing",
    "prompt": "The process by which non-coding intervening sequences are excised from pre-mRNA and coding exons are joined together is known as:",
    "options": [
      "Transcription elongation",
      "RNA splicing",
      "Polyadenylation",
      "Translational initiation"
    ],
    "answer": 1,
    "explain": "Nuclear pre-mRNA splicing is catalyzed by the spliceosome (composed of snRNPs U1, U2, U4, U5, and U6), which identifies conserved 5' donor, branch point, and 3' acceptor splice sites to remove introns.",
    "example": "Aberrant alternative splicing of MAPT exon 10 alters the 3R:4R tau ratio, precipitating frontotemporal dementia."
  },
  {
    "id": "ng-006",
    "mode": "neurogenetics",
    "level": 1,
    "type": "choice",
    "topic": "Rett Syndrome Genetics",
    "prompt": "Rett syndrome is an X-linked dominant neurodevelopmental disorder typically caused by mutations in which methyl-CpG-binding transcriptional regulator?",
    "options": [
      "MECP2",
      "FOXG1",
      "CDKL5",
      "UBE3A"
    ],
    "answer": 0,
    "explain": "Loss-of-function mutations in MECP2 (Methyl-CpG-Binding Protein 2) on the X chromosome cause Rett syndrome. MECP2 binds methylated DNA and recruits chromatin remodeling complexes to regulate neuronal gene transcription during synaptic maturation.",
    "example": "Re-expression of Mecp2 in adult symptomatic knockout mice remarkably reverses neurological deficits, demonstrating structural plasticity is preserved."
  },
  {
    "id": "ng-007",
    "mode": "neurogenetics",
    "level": 2,
    "type": "choice",
    "topic": "APOE Allelic Polymorphisms",
    "prompt": "The three major human APOE alleles (epsilon 2, epsilon 3, epsilon 4) differ by single amino acid substitutions at which two residue positions?",
    "options": [
      "Residues 112 and 158 (Cysteine vs Arginine)",
      "Residues 24 and 86 (Serine vs Threonine)",
      "Residues 202 and 205 (Proline vs Lysine)",
      "Residues 40 and 42 (Alanine vs Isoleucine)"
    ],
    "answer": 0,
    "explain": "APOE ε2 has Cys112/Cys158; APOE ε3 has Cys112/Arg158; APOE ε4 has Arg112/Arg158. The presence of Arg at position 112 in ε4 alters domain interaction with Glu255, modifying receptor binding, lipid trafficking, and accelerating Aβ aggregation.",
    "example": "Carrying a single APOE ε4 allele increases late-onset AD risk ~3-fold, whereas two copies (ε4/ε4) increase risk >12-fold."
  },
  {
    "id": "ng-008",
    "mode": "neurogenetics",
    "level": 2,
    "type": "choice",
    "topic": "CRISPR-Cas9 Mechanism",
    "prompt": "Wild-type Streptococcus pyogenes Cas9 requires what specific Protospacer Adjacent Motif (PAM) immediately downstream of the target DNA sequence to execute cleavage?",
    "options": [
      "5'-TTN-3'",
      "5'-NGG-3'",
      "5'-AAT-3'",
      "5'-CCG-3'"
    ],
    "answer": 1,
    "explain": "SpCas9 recognizes a 5'-NGG-3' PAM motif immediately 3' to the 20-nucleotide target protospacer specified by the single guide RNA (sgRNA). Recognition triggers local DNA melting, RNA-DNA heteroduplex formation, and double-strand break cleavage by the RuvC and HNH nuclease domains.",
    "example": "Target sites lacking a 5'-NGG-3' PAM are not bound or cleaved by canonical SpCas9, preventing off-target genomic cleavage."
  },
  {
    "id": "ng-009",
    "mode": "neurogenetics",
    "level": 2,
    "type": "choice",
    "topic": "Spinal Muscular Atrophy Splicing",
    "prompt": "In Spinal Muscular Atrophy (SMA), homozygous deletion of SMN1 is partially compensated by the paralogous gene SMN2, which differs primarily by a silent C-to-T transition that causes:",
    "options": [
      "Complete transcriptional shutdown of the promoter",
      "Alternative skipping of exon 7, producing a truncated unstable protein",
      "Frameshift mutation in the tudor domain",
      "Constitutive activation of ubiquitin ligation"
    ],
    "answer": 1,
    "explain": "SMN2 harbors a C-to-T transition in exon 7 that disrupts an exonic splicing enhancer (SF2/ASF) and creates an exonic splicing silencer (hnRNP A1). Consequently, ~85-90% of SMN2 transcripts skip exon 7 (SMNΔ7), producing a rapidly degraded truncated protein.",
    "example": "Nusinersen (Spinraza) is an antisense oligonucleotide that binds the SMN2 intron 6/7 splicing silencer, forcing exon 7 inclusion to restore functional full-length SMN protein."
  },
  {
    "id": "ng-010",
    "mode": "neurogenetics",
    "level": 2,
    "type": "choice",
    "topic": "Parkinson's Disease Monogenic Causes",
    "prompt": "Which mutation represents the most common autosomal dominant genetic cause of Parkinson's disease worldwide?",
    "options": [
      "SNCA A53T",
      "LRRK2 G2019S",
      "PRKN Exon 3 deletion",
      "DJ-1 L166P"
    ],
    "answer": 1,
    "explain": "The G2019S mutation in LRRK2 (Leucine-Rich Repeat Kinase 2) is the most frequent monogenic cause of Parkinson's disease, accounting for 1-2% of sporadic and up to 5% of familial PD cases globally (higher in Ashkenazi Jewish and North African Berber populations).",
    "example": "The G2019S mutation resides in the kinase domain activation loop, causing hyperphosphorylation of downstream Rab GTPases."
  },
  {
    "id": "ng-011",
    "mode": "neurogenetics",
    "level": 2,
    "type": "choice",
    "topic": "Cre-LoxP Recombination Rules",
    "prompt": "When two loxP sites are positioned in the same directional orientation flanking a target DNA exon ('floxed'), Cre recombinase activity results in:",
    "options": [
      "Inversion of the flanked sequence",
      "Excision and deletion of the flanked sequence",
      "Duplication of the flanked exon",
      "Translocation to another chromosome"
    ],
    "answer": 1,
    "explain": "Cre recombinase catalyzes DNA exchange at 34-bp loxP recognition sites. If the loxP sites are aligned in the SAME orientation, Cre excises the intervening DNA as a circular molecule, producing a permanent conditional knockout.",
    "example": "Crossing a floxed gene mouse with a CaMKIIa-Cre driver deletes the gene specifically in forebrain excitatory neurons."
  },
  {
    "id": "ng-012",
    "mode": "neurogenetics",
    "level": 2,
    "type": "choice",
    "topic": "Parkin-Mediated Juvenile Parkinsonism",
    "prompt": "Autosomal recessive juvenile parkinsonism (AR-JP) with onset before age 40 is most frequently caused by loss-of-function mutations in:",
    "options": [
      "PRKN (Parkin, an E3 ubiquitin ligase)",
      "SNCA (alpha-synuclein)",
      "HTRA2",
      "ATP13A2"
    ],
    "answer": 0,
    "explain": "Loss-of-function mutations in PRKN (encoding Parkin, a cytosolic RING-between-RING E3 ubiquitin ligase) are the most common cause of early-onset recessive parkinsonism, characterized by selective loss of nigrostriatal dopaminergic neurons without classical Lewy bodies.",
    "example": "Parkin works in concert with the kinase PINK1 to coordinate mitophagy of depolarized mitochondria."
  },
  {
    "id": "ng-013",
    "mode": "neurogenetics",
    "level": 3,
    "type": "choice",
    "topic": "C9orf72 Repeat Expansion in ALS/FTD",
    "prompt": "The most common genetic etiology of both familial ALS and Frontotemporal Dementia (FTD) is a hexanucleotide repeat expansion of:",
    "options": [
      "GGGGCC in the first intron/promoter of C9orf72",
      "CAG in exon 1 of ATXN2",
      "CCUG in intron 1 of CNBP",
      "CCTG in the 3' UTR of DMPK"
    ],
    "answer": 0,
    "explain": "A massive GGGGCC (G4C2) repeat expansion (hundreds to thousands of repeats) in non-coding intron 1/promoter of C9orf72 accounts for ~40% of familial ALS and ~25% of familial FTD. Pathogenesis involves loss of C9orf72 protein function, toxic RNA foci that sequester RNA-binding proteins, and repeat-associated non-AUG (RAN) translation.",
    "example": "Antisense oligonucleotides targeting C9orf72 sense and antisense transcripts degrade repeat RNA foci in patient-derived motor neurons."
  },
  {
    "id": "ng-014",
    "mode": "neurogenetics",
    "level": 3,
    "type": "choice",
    "topic": "TREM2 Genetics in Alzheimer's",
    "prompt": "In Alzheimer's disease GWAS and sequencing studies, the rare missense variant R47H in TREM2 confers:",
    "options": [
      "Complete protection against amyloid accumulation",
      "A 3- to 4-fold increased risk of developing Alzheimer's disease, comparable in effect size to APOE epsilon 4",
      "Early-onset parkinsonism with extensive Lewy bodies",
      "Severe childhood-onset leukoencephalopathy"
    ],
    "answer": 1,
    "explain": "Guerreiro et al. and Jonsson et al. (2013) identified the TREM2 R47H variant as a major risk factor for late-onset AD (odds ratio ~3-4). The R47H mutation resides in the immunoglobulin-like ligand-binding domain, impairing microglial recognition of anionic lipids, APOE, and Aβ oligomers.",
    "example": "TREM2 R47H knock-in mice exhibit defective microglial clustering around amyloid plaques, leaving naked fibrillar edges that exacerbate synaptic dystrophy."
  },
  {
    "id": "ng-015",
    "mode": "neurogenetics",
    "level": 3,
    "type": "choice",
    "topic": "Cell-Type Specific Promoters",
    "prompt": "Which promoter sequence is widely used in adeno-associated viral (AAV) vectors to restrict transgene expression specifically to forebrain excitatory neurons in mice?",
    "options": [
      "Camk2a promoter (0.4 or 1.3 kb)",
      "Gfap promoter",
      "Cx3cr1 promoter",
      "Gad67 promoter"
    ],
    "answer": 0,
    "explain": "The CaMKIIa (Camk2a) promoter drives robust expression selectively in glutamatergic excitatory projection neurons (pyramidal cells in cortex and hippocampus), sparing GABAergic interneurons and glial cells.",
    "example": "AAV-Camk2a-ChR2-mCherry drives optogenetic excitation of cortical pyramidal neurons without recruiting local parvalbumin interneurons directly."
  },
  {
    "id": "ng-016",
    "mode": "neurogenetics",
    "level": 3,
    "type": "choice",
    "topic": "FLEx / DIO Switch Recombination",
    "prompt": "In viral transgenics, a 'DIO' (Double-floxed Inverted Open reading frame) or 'FLEx' switch enforces Cre-dependent expression because the transgene is cloned:",
    "options": [
      "In the sense orientation flanked by identical loxP sites",
      "In the inverted (antisense) orientation flanked by two mutually incompatible pairs of antiparallel lox sites (loxP and lox2722)",
      "Downstream of a tandem stop cassette containing three polyadenylation signals",
      "Inside the viral inverted terminal repeat (ITR)"
    ],
    "answer": 1,
    "explain": "FLEx switches utilize two heterotypic, incompatible lox sites (e.g. loxP and lox2722). In the presence of Cre, one pair recombines to invert the coding sequence into the sense orientation, followed by excision of one site from each pair, locking the transgene irreversibly in the functional sense orientation.",
    "example": "Injecting AAV-DIO-ChR2 into a PV-Cre mouse guarantees that ChR2 is transcribed only inside Cre-expressing PV interneurons."
  },
  {
    "id": "ng-017",
    "mode": "neurogenetics",
    "level": 3,
    "type": "choice",
    "topic": "Parkinson's Disease GWAS Loci",
    "prompt": "Heterozygous loss-of-function variants in GBA1 (encoding the lysosomal enzyme glucocerebrosidase) represent the most potent known genetic risk factor for:",
    "options": [
      "Amyotrophic lateral sclerosis",
      "Parkinson's disease and Dementia with Lewy Bodies",
      "Frontotemporal dementia",
      "Spinocerebellar ataxia"
    ],
    "answer": 1,
    "explain": "Homozygous GBA1 mutations cause Gaucher's disease. Remarkably, heterozygous carriers of GBA1 mutations (e.g. N370S, L444P) have a ~5- to 10-fold increased risk of developing Parkinson's disease. Glucocerebrosidase deficiency causes glucosylceramide accumulation, stabilizing toxic alpha-synuclein oligomeric intermediates.",
    "example": "GBA1-associated PD presents with earlier age of onset and higher prevalence of cognitive decline than idiopathic PD."
  },
  {
    "id": "ng-018",
    "mode": "neurogenetics",
    "level": 3,
    "type": "choice",
    "topic": "MicroRNA-Mediated Neuronal Reprogramming",
    "prompt": "Knockdown of which single RNA-binding polypyrimidine tract protein has been demonstrated to convert astrocytes or fibroblasts into functional neurons by relieving global repression of neuronal alternative splicing?",
    "options": [
      "PTBP1 (PTB)",
      "Nova-1",
      "RBFOX1",
      "hnRNP A1"
    ],
    "answer": 0,
    "explain": "PTBP1 is an essential master repressor of neuronal alternative splicing programs in non-neuronal cells. Depletion or antisense oligonucleotide knockdown of PTBP1 unlocks a neuronal transcription and splicing cascade (inducing miR-124 and PTBP2), directly reprogramming glia into induced neurons.",
    "example": "Qian et al. (2020) demonstrated that shRNA-mediated depletion of Ptbp1 converted midbrain astrocytes into dopamine neurons, alleviating motor deficits in 6-OHDA parkinsonian mice."
  },
  {
    "id": "ng-019",
    "mode": "neurogenetics",
    "level": 4,
    "type": "choice",
    "topic": "C9orf72 RAN Translation Products",
    "prompt": "Repeat-Associated Non-AUG (RAN) translation of sense and antisense transcripts from the C9orf72 G4C2 expansion generates which five distinct dipeptide repeat (DPR) proteins?",
    "options": [
      "Poly-GA, Poly-GP, Poly-GR, Poly-PR, and Poly-PA",
      "Poly-alanine, Poly-glutamine, Poly-leucine, Poly-serine, and Poly-valine",
      "Poly-tyrosine, Poly-tryptophan, Poly-cysteine, Poly-methionine, and Poly-proline",
      "Poly-lysine, Poly-arginine, Poly-histidine, Poly-aspartate, and Poly-glutamate"
    ],
    "answer": 0,
    "explain": "Unconventional non-AUG translation across all reading frames of sense (G4C2: poly-GA, poly-GP, poly-GR) and antisense (C4G2: poly-PR, poly-PG, poly-PA) transcripts produces 5 DPRs. The arginine-rich basic dipeptides (poly-PR and poly-GR) are potent neurotoxins that bind nucleoli, disrupt nuclear pore complexes, and impair nucleocytoplasmic transport.",
    "example": "Expression of poly-PR or poly-GR alone in flies or cortical neurons precipitates cell death and cytosolic mislocalization of TDP-43."
  },
  {
    "id": "ng-020",
    "mode": "neurogenetics",
    "level": 4,
    "type": "choice",
    "topic": "APOE Christchurch Protective Variant",
    "prompt": "A famous Colombian carrier of the deterministic PSEN1 E280A (Paisa) mutation resisted cognitive impairment until her seventies due to homozygous inheritance of which rare APOE variant?",
    "options": [
      "APOE Christchurch (R136S)",
      "APOE Jacksonville (V236E)",
      "APOE ε2/ε2 genotype",
      "APOE knockout null allele"
    ],
    "answer": 0,
    "explain": "Arboleda-Velasquez et al. (2019) reported a woman carrying the devastating PSEN1 E280A mutation who remained cognitively unimpaired for nearly three decades past expected onset. She was homozygous for the APOE3 Christchurch (R136S) mutation, which dramatically abrogated APOE binding to low-density lipoprotein receptors and heparan sulfate proteoglycans (HSPGs), preventing the trans-synaptic propagation of tau tangles despite massive brain amyloid.",
    "example": "APOE Christchurch alters the heparin-binding domain of APOE, blunting tau pathology seeding in preclinical models."
  },
  {
    "id": "ng-021",
    "mode": "neurogenetics",
    "level": 4,
    "type": "choice",
    "topic": "Transgenic AD Models: 5xFAD",
    "prompt": "The widely used 5xFAD transgenic mouse model recapitulates rapid, aggressive amyloid deposition by 2 months of age by expressing human APP and PSEN1 containing which mutations under the Thy1 promoter?",
    "options": [
      "Swedish (K670N/M671L), Florida (I716V), London (V717I) in APP + M146L and L286V in PSEN1",
      "Arctic (E693G) and Indiana (V717F) in APP + Delta-E9 in PSEN1",
      "Dutch (E693Q) and Flemish (A692G) in APP + P264L in PSEN2",
      "P301L and R406W in MAPT + G2019S in LRRK2"
    ],
    "answer": 0,
    "explain": "5xFAD mice co-express human APP695 harboring three FAD mutations (Swedish, Florida, and London) and human Presenilin-1 harboring two FAD mutations (M146L and L286V) driven by the neuron-specific Thy1 promoter. This combination drives massive production of Aβ42, inducing intraneuronal Aβ accumulation at 1.5 months and robust extracellular plaques by 2 months.",
    "example": "5xFAD mice show early microgliosis, astrocytosis, and cognitive deficits in Y-maze testing, but do not develop tau neurofibrillary tangles."
  },
  {
    "id": "ng-022",
    "mode": "neurogenetics",
    "level": 4,
    "type": "choice",
    "topic": "Epigenetic Repression of Memory Genes",
    "prompt": "In the aging and Alzheimer's hippocampus, epigenetic blockade of synaptic plasticity genes (such as Bdnf and Fos) is mediated by recruitment of which class of chromatin-modifying enzymes?",
    "options": [
      "Histone deacetylases (particularly HDAC2 and HDAC3)",
      "Histone acetyltransferases (such as p300/CBP)",
      "DNA topoisomerases",
      "Histone demethylase KDM6A"
    ],
    "answer": 0,
    "explain": "HDAC2 is upregulated in the hippocampus of aged mice and human AD brains, where it binds promoter regions of memory and synaptic plasticity genes (Bdnf, Egr1, Fos), removing acetyl groups from histone tails. This compacts chromatin into transcriptionally silent heterochromatin.",
    "example": "Pharmacological inhibition of HDAC2 with SAHA or targeted HDAC2 knockdown restores histone acetylation, rescues dendritic spine density, and reinstates memory formation in AD mouse models."
  },
  {
    "id": "ng-023",
    "mode": "neurogenetics",
    "level": 4,
    "type": "choice",
    "topic": "Tau Haplotype Genetics",
    "prompt": "The human MAPT gene on chromosome 17q21.31 resides within a 900-kb inversion polymorphism defining two distinct haplotypes, H1 and H2. The H1/H1 genotype is strongly associated with:",
    "options": [
      "Progressive Supranuclear Palsy (PSP) and Corticobasal Degeneration (CBD)",
      "Spinocerebellar Ataxia type 3",
      "Amyotrophic Lateral Sclerosis with SOD1 mutation",
      "Pure autosomal dominant frontotemporal lobar degeneration with TDP-43 inclusions"
    ],
    "answer": 0,
    "explain": "The non-inverted H1 haplotype promotes higher baseline transcription of MAPT and drives alternative splicing favoring 4-repeat (4R) tau isoforms. The homozygous H1/H1 genotype is a significant genetic risk factor for the primary 4R tauopathies Progressive Supranuclear Palsy (PSP) and Corticobasal Degeneration (CBD).",
    "example": "Genome-wide association studies consistently identify the MAPT H1 haplotype as the primary locus associated with susceptibility to PSP."
  },
  {
    "id": "ng-024",
    "mode": "neurogenetics",
    "level": 4,
    "type": "choice",
    "topic": "Polygenic Risk Scores in Late-Onset AD",
    "prompt": "Beyond the major APOE locus, polygenic risk scores (PRS) in late-onset Alzheimer's disease demonstrate that genetic susceptibility is heavily concentrated in pathways regulating:",
    "options": [
      "Innate immune response / microglial phagocytosis and endocytic trafficking",
      "Glycolytic enzyme transcription in cerebellar Purkinje cells",
      "Voltage-gated potassium channel pore structures",
      "Serotonergic synthesis and vesicular storage in the raphe nuclei"
    ],
    "answer": 0,
    "explain": "Pathway analyses of the >70 late-onset AD loci identified by large-scale GWAS (including BIN1, PICALM, CD33, CLU, CR1, INPP5D, and TREM2) demonstrate overwhelming enrichment in two functional modules: microglial immune surveillance/lipid clearance and endolysosomal trafficking/autophagy.",
    "example": "High polygenic risk scores predict earlier conversion from mild cognitive impairment (MCI) to Alzheimer's dementia even among APOE ε3/ε3 individuals."
  },
  {
    "id": "ng-025",
    "mode": "neurogenetics",
    "level": 5,
    "type": "choice",
    "topic": "Somatic Mosaicism in the Aging Brain",
    "prompt": "Single-cell whole-genome sequencing of post-mortem human cortical neurons (Walsh and Lodato) revealed that each healthy adult neuron accumulates approximately how many somatic single-nucleotide variants (sSNVs) per year of life?",
    "options": [
      "15 to 20 sSNVs per year, accumulating predominantly via oxidative DNA damage (signature A)",
      "500 to 1,000 sSNVs per year driven by retrotransposon jumping",
      "Zero sSNVs because post-mitotic neurons completely arrest all mutational processes",
      "100,000 sSNVs per year due to telomere shortening"
    ],
    "answer": 0,
    "explain": "Lodato et al. (Science 2018) discovered that human post-mitotic neurons accrue ~15-20 somatic single-nucleotide variants annually across a lifetime (accumulating ~1,500-2,500 mutations in an 80-year-old brain). This 'genomic clock' is driven predominantly by oxidative DNA damage (signature A) and increases significantly in repair-deficient neurodegenerative conditions.",
    "example": "Single-neuron DNA sequencing demonstrates that adult brain somatic mutations can disrupt critical synaptic and ion channel genes in a mosaic subset of neurons."
  },
  {
    "id": "ng-026",
    "mode": "neurogenetics",
    "level": 5,
    "type": "choice",
    "topic": "Prime Editing vs Base Editing in Post-Mitotic Neurons",
    "prompt": "When targeting point mutations in non-dividing adult neurons in vivo, Prime Editing (PE) offers which distinct mechanistic advantage over classical Cas9 HDR?",
    "options": [
      "It requires no double-strand DNA breaks and does not require an exogenous donor DNA template, relying instead on a reverse-transcriptase-fused Cas9 nickase and a pegRNA",
      "It generates large chromosomal deletions that eliminate entire toxic gene loci",
      "It operates exclusively on ribosomal RNA in the nucleolus",
      "It relies entirely on high endogenous levels of homologous recombination (HDR) enzymes"
    ],
    "answer": 0,
    "explain": "Post-mitotic neurons lack Homology-Directed Repair (HDR) because HDR is restricted to S/G2 phase. Classical Cas9 double-strand breaks in neurons yield unpredictable indels via NHEJ. Prime Editing fuses an engineered M-MLV reverse transcriptase to an H840A Cas9 nickase, using a prime editing guide RNA (pegRNA) to directly reverse-transcribe desired edits without double-strand breaks.",
    "example": "In vivo delivery of prime editors via split-AAV systems has corrected pathogenic mutations (e.g. in PRNP or Huntington's) directly in adult mouse brain."
  },
  {
    "id": "ng-027",
    "mode": "neurogenetics",
    "level": 5,
    "type": "choice",
    "topic": "Single-Cell eQTL Brain Cell Dissection",
    "prompt": "Single-nucleus expression quantitative trait locus (sn-eQTL) mapping in post-mortem human brain tissue (Bryois et al. 2022) revealed that the vast majority of disease-associated causal genetic variants in Alzheimer's disease act specifically through:",
    "options": [
      "Microglia-specific regulatory elements, rather than neuronal or astrocytic enhancers",
      "Cerebellar granule neuron axon guidance enhancers",
      "Choroid plexus ciliary transport genes",
      "Ependymal cell fluid pump promoters"
    ],
    "answer": 0,
    "explain": "While bulk brain tissue homogenates are dominated by neuronal and astrocytic transcripts (diluting microglial signals), single-nucleus eQTL mapping revealed that late-onset AD GWAS variants and epigenetic open chromatin regions overlap almost exclusively with microglia-specific promoters and enhancers.",
    "example": "Fine-mapping of the BIN1 risk locus demonstrated that the risk allele acts via a microglia-specific enhancer that alters BIN1 expression during microglial activation."
  },
  {
    "id": "ng-028",
    "mode": "neurogenetics",
    "level": 5,
    "type": "choice",
    "topic": "SNCA Triplication Gene Dosage Mechanism",
    "prompt": "Families harboring a genomic triplication of the wild-type SNCA locus on chromosome 4q22.1 present with which unique clinical and pathological phenotype compared to those with an SNCA duplication?",
    "options": [
      "Severe early-onset Parkinson's disease with rapid progression to dementia and extensive cortical Lewy bodies, demonstrating strict dosage dependency",
      "A benign, late-onset resting tremor without any cognitive decline or nigral cell loss",
      "Pure cerebellar ataxia with complete absence of parkinsonian features",
      "Early-onset frontotemporal lobar degeneration with pure TDP-43 pathology"
    ],
    "answer": 0,
    "explain": "Singleton et al. (Science 2003) demonstrated that SNCA gene dosage directly dictates disease severity. Duplication of SNCA (3 copies total) produces late-onset classic Parkinson's disease, whereas triplication (4 copies total, doubling α-synuclein protein levels) produces early-onset aggressive parkinsonism (onset in 30s) with early dementia, dysautonomia, and widespread cortical Lewy bodies.",
    "example": "Quantifying α-synuclein mRNA and protein in SNCA triplication patients revealed a 2-fold elevation in brain tissue, proving that wild-type protein overproduction alone is sufficient to drive neurodegeneration."
  },
  {
    "id": "ng-029",
    "mode": "neurogenetics",
    "level": 1,
    "type": "choice",
    "topic": "Friedreich's Ataxia Genetics",
    "prompt": "Friedreich's Ataxia, the most common inherited ataxia, is an autosomal recessive disorder caused by a GAA triplet repeat expansion in intron 1 of which gene?",
    "options": [
      "FXN (Frataxin)",
      "ATXN1",
      "HTT",
      "DMPK"
    ],
    "answer": 0,
    "explain": "Friedreich's ataxia is caused by an intronic GAA repeat expansion in the FXN gene, which forms non-B DNA structures and heterochromatin, silencing frataxin expression. Frataxin is an essential mitochondrial protein required for iron-sulfur (Fe-S) cluster assembly.",
    "example": "Loss of frataxin causes mitochondrial iron overload, deficient OXPHOS, and progressive sensory ataxia and cardiomyopathy."
  },
  {
    "id": "ng-030",
    "mode": "neurogenetics",
    "level": 2,
    "type": "choice",
    "topic": "Icelandic Protective APP Variant",
    "prompt": "The rare Icelandic mutation (A673T) in the APP gene is celebrated in neurogenetics because it:",
    "options": [
      "Protects against Alzheimer's disease and cognitive decline by reducing BACE1 cleavage of APP by ~40%",
      "Causes aggressive, early-onset dementia before age 30",
      "Completely eliminates all synaptic transmission in the hippocampus",
      "Prevents microglial proliferation in the cerebellum"
    ],
    "answer": 0,
    "explain": "Jonsson et al. (Nature 2012) discovered the APP A673T substitution adjacent to the beta-secretase cleavage site. The mutation reduces BACE1 cleavage efficiency by ~40% in vitro and in vivo, resulting in lifelong lower Aβ levels, protection against Alzheimer's disease, and preserved cognitive performance in elderly carriers.",
    "example": "The Icelandic mutation provided powerful genetic proof-of-concept that lifetime suppression of BACE1 cleavage protects human brains against dementia."
  },
  {
    "id": "ng-031",
    "mode": "neurogenetics",
    "level": 3,
    "type": "choice",
    "topic": "Tuberous Sclerosis Complex",
    "prompt": "Tuberous Sclerosis Complex (TSC), characterized by benign brain cortical tubers, intractable epilepsy, and autism, is caused by loss-of-function mutations in TSC1 or TSC2 leading to hyperactivation of:",
    "options": [
      "mTORC1 (mammalian target of rapamycin complex 1)",
      "PTEN phosphatase",
      "Glycogen synthase kinase 3 beta",
      "Calcineurin phosphatase"
    ],
    "answer": 0,
    "explain": "Hamartin (TSC1) and Tuberin (TSC2) form a GTPase-activating protein (GAP) complex that inactivates the small GTPase Rheb. Inactivating mutations in either TSC1 or TSC2 leave Rheb constitutively GTP-bound, hyperactivating mTORC1 and driving abnormal cell growth, enlarged dysplastic neurons, and cortical tubers.",
    "example": "Treatment of TSC patients with the mTORC1 inhibitor everolimus shrinks subependymal giant cell astrocytomas (SEGAs) and reduces seizure frequency."
  },
  {
    "id": "ng-032",
    "mode": "neurogenetics",
    "level": 4,
    "type": "choice",
    "topic": "Charcot-Marie-Tooth Type 1A",
    "prompt": "Charcot-Marie-Tooth disease type 1A (CMT1A), the most common inherited peripheral neuropathy, is caused by which genomic structural variation on chromosome 17p11.2?",
    "options": [
      "A 1.4-Mb duplication encompassing the PMP22 (Peripheral Myelin Protein 22) gene",
      "A heterozygous deletion of the entire myelin basic protein gene",
      "A CAG repeat expansion in the P0 glycoprotein gene",
      "A point mutation in the mitochondrial genome"
    ],
    "answer": 0,
    "explain": "CMT1A is caused by non-allelic homologous recombination resulting in a 1.4-Mb tandem duplication of chromosome 17p11.2 containing PMP22. Overexpression of PMP22 disrupts Schwann cell differentiation and myelin compaction, causing demyelinating neuropathy with slowed nerve conduction velocities and distal muscle wasting.",
    "example": "Conversely, reciprocal deletion of the exact same 1.4-Mb PMP22 region causes Hereditary Neuropathy with Liability to Pressure Palsies (HNPP)."
  },
  {
    "level": 1,
    "topic": "Autosomal Dominant Inheritance Probability",
    "prompt": "If a person heterozygous for an autosomal dominant neurological disorder marries a genetically unaffected individual, what is the probability that their first child will inherit the disorder?",
    "options": [
      "50%",
      "25%",
      "75%",
      "100%"
    ],
    "answer": 0,
    "explain": "An individual heterozygous for an autosomal dominant condition has one mutant allele (A) and one normal allele (a). An unaffected mate has genotype (aa). Each offspring has a 1-in-2 (50%) chance of inheriting allele A.",
    "example": "In Huntington's disease, every child of an affected heterozygous parent has an independent 50% probability of carrying the expanded HTT allele."
  },
  {
    "level": 1,
    "topic": "Autosomal Recessive Carrier Risk",
    "prompt": "Two phenotypically healthy carriers of an autosomal recessive neurodegenerative disease (such as Tay-Sachs) have a child. What is the chance that the child is an unaffected carrier?",
    "options": [
      "50% (2/4)",
      "25% (1/4)",
      "75% (3/4)",
      "0%"
    ],
    "answer": 0,
    "explain": "Cross: Aa x Aa yields 1 AA (healthy non-carrier, 25%), 2 Aa (healthy carriers, 50%), and 1 aa (affected, 25%). Thus, 50% of all offspring are unaffected carriers.",
    "example": "Tay-Sachs carrier screening identifies heterozygotes who carry one defective HEXA allele without displaying any neurological signs."
  },
  {
    "level": 1,
    "topic": "X-Linked Recessive Transmission",
    "prompt": "A female carrier of an X-linked recessive neurological disorder (such as Duchenne muscular dystrophy) has children with an unaffected male. What proportion of their sons will be affected?",
    "options": [
      "50%",
      "100%",
      "25%",
      "0%"
    ],
    "answer": 0,
    "explain": "The mother passes either her normal X or her mutant X chromosome to her sons with equal probability (50%). Since sons receive their Y chromosome from the father, sons inheriting the mutant X are hemizygous and affected.",
    "example": "Duchenne muscular dystrophy almost exclusively affects males, who inherit the mutated dystrophin gene on the maternal X chromosome."
  },
  {
    "level": 1,
    "topic": "X-Chromosome Inactivation Lyonization",
    "prompt": "Random X-chromosome inactivation (lyonization) in mammalian female somatic cells occurs during early embryogenesis and is orchestrated by the long non-coding RNA:",
    "options": [
      "Xist (X-inactive specific transcript)",
      "HOTAIR",
      "MALAT1",
      "H19"
    ],
    "answer": 0,
    "explain": "Xist lncRNA is transcribed from the X-inactivation center (XIC) on the future inactive X chromosome, coating it in cis and recruiting silencing complexes (polycomb repressive complexes) to induce heterochromatinization into a Barr body.",
    "example": "Female carriers of X-linked conditions like Rett syndrome or Fragile X exhibit mosaic phenotypes depending on the ratio of skewed X-inactivation in the brain."
  },
  {
    "level": 1,
    "topic": "Maternal Mitochondrial Inheritance",
    "prompt": "Disorders of the mitochondrial genome, such as Leber's Hereditary Optic Neuropathy (LHON) and MELAS, are transmitted exclusively by:",
    "options": [
      "The mother to all of her children (both sons and daughters)",
      "The father to all of his sons",
      "The mother to her sons only",
      "Autosomal recessive non-disjunction"
    ],
    "answer": 0,
    "explain": "Sperm mitochondria are ubiquitinated and degraded upon fertilization in mammalian zygotes; therefore, all mitochondrial DNA (mtDNA) is inherited strictly through the maternal oocyte cytoplasm.",
    "example": "An affected mother with homoplasmic mtDNA mutations transmits the mutation to 100% of her progeny, whereas an affected father transmits it to 0%."
  },
  {
    "level": 1,
    "topic": "Mitochondrial Heteroplasmy",
    "prompt": "In mitochondrial genetics, 'heteroplasmy' refers to:",
    "options": [
      "The coexistence of both mutant and wild-type mitochondrial genomes within a single cell or tissue",
      "The presence of extra chromosomes in the cell nucleus",
      "The fusion of mitochondria with lysosomes",
      "Equal distribution of mitochondria between daughter cells"
    ],
    "answer": 0,
    "explain": "Because each eukaryotic cell harbors hundreds to thousands of mtDNA molecules, a mutation can affect a fraction of these genomes. Clinical disease manifestation occurs only when the proportion of mutant mtDNA crosses a tissue-specific critical threshold (usually 60-80%).",
    "example": "A patient with 85% mutant mtDNA in cerebral cortex develops severe seizures (MERRF), while a sibling with 30% heteroplasmy remains asymptomatic."
  },
  {
    "level": 1,
    "topic": "Karyotype of Klinefelter Syndrome",
    "prompt": "Which chromosomal constitution is characteristic of Klinefelter syndrome, associated with mild executive deficits and hypogonadism?",
    "options": [
      "47,XXY",
      "45,X",
      "47,XYY",
      "47,XXX"
    ],
    "answer": 0,
    "explain": "Klinefelter syndrome is characterized by an extra X chromosome in males (47,XXY), caused by meiotic nondisjunction in either paternal or maternal gametogenesis.",
    "example": "Patients often present in adolescence with tall stature, gynecomastia, and subtle language-based learning disabilities."
  },
  {
    "level": 1,
    "topic": "Turner Syndrome Genetics",
    "prompt": "Turner syndrome, characterized by short stature, webbed neck, and specific non-verbal visuospatial cognitive impairments, results from:",
    "options": [
      "Complete or partial monosomy X (45,X)",
      "Trisomy 18",
      "Trisomy 13",
      "47,XXY"
    ],
    "answer": 0,
    "explain": "Turner syndrome (45,X) occurs in approximately 1 in 2,500 live female births due to complete or partial absence of the second sex chromosome.",
    "example": "Neurocognitive evaluations of individuals with 45,X frequently reveal normal verbal IQ but selective deficits in arithmetic and visuospatial processing."
  },
  {
    "level": 1,
    "topic": "RNA Splicing Consensus Sequences",
    "prompt": "In eukaryotic pre-mRNA splicing, the highly conserved invariant dinucleotides found at the 5' splice donor and 3' splice acceptor junctions are:",
    "options": [
      "GU at the 5' donor site and AG at the 3' acceptor site",
      "AG at the 5' donor site and GU at the 3' acceptor site",
      "AU at the 5' donor site and GC at the 3' acceptor site",
      "CC at the 5' donor site and GG at the 3' acceptor site"
    ],
    "answer": 0,
    "explain": "The canonical U2-type spliceosome recognizes the invariant GU (GT in DNA) at the 5' boundary of the intron and AG at the 3' boundary, flanked by the branch point sequence and polypyrimidine tract.",
    "example": "A single G-to-A point mutation in the 5' donor site (IVS1+1G>A) completely abolishes splicing, causing intron retention or exon skipping."
  },
  {
    "level": 1,
    "topic": "Nonsense-Mediated mRNA Decay 50-nt Rule",
    "prompt": "Nonsense-mediated mRNA decay (NMD) targets an aberrant mRNA for rapid degradation when a premature termination codon (PTC) is located:",
    "options": [
      "More than 50-55 nucleotides upstream of the final exon-junction complex (EJC)",
      "Within the final exon of the transcript",
      "Directly at the 5' cap site",
      "Within the poly-A tail"
    ],
    "answer": 0,
    "explain": "During the pioneer round of translation, the ribosome displaces exon junction complexes (EJCs). If a PTC causes the ribosome to stall >50-55 nt upstream of an intact EJC, the EJC recruits UPF1/2/3 to initiate rapid mRNA decapping and deadenylation.",
    "example": "Nonsense mutations in the last exon of the neurofibromatosis gene NF1 escape NMD, producing truncated stable proteins rather than complete mRNA degradation."
  },
  {
    "level": 1,
    "topic": "Genomic Imprinting Concept",
    "prompt": "Genomic imprinting in mammalian neurobiology refers to an epigenetic phenomenon where:",
    "options": [
      "A gene is expressed exclusively from either the maternal or paternal allele depending on parent of origin",
      "Both parental alleles are deleted during gametogenesis",
      "DNA sequences are altered by retroviral integration",
      "Chromosomes undergo permanent fragmentation in embryonic neurons"
    ],
    "answer": 0,
    "explain": "Imprinted genes carry differential DNA methylation established during gametogenesis, resulting in monoallelic expression based on whether the chromosome was inherited from the mother or father.",
    "example": "UBE3A is imprinted exclusively in mature brain neurons, where only the maternal allele is transcriptionally active."
  },
  {
    "level": 2,
    "topic": "Myotonic Dystrophy Type 1 RNA Toxicity",
    "prompt": "Myotonic Dystrophy Type 1 (DM1) is caused by a CTG trinucleotide repeat expansion in the 3' UTR of the DMPK gene that exerts pathogenic effects via:",
    "options": [
      "RNA toxic gain-of-function: nuclear CUG repeat RNA foci sequester the splicing factor MBNL1, causing transcriptome-wide mis-splicing",
      "Direct toxicity of polyglutamine aggregates in the cytoplasm",
      "Complete loss of DMPK protein kinase catalytic activity",
      "Degradation of the nuclear envelope by mutant DNA helicases"
    ],
    "answer": 0,
    "explain": "Transcribed mutant DMPK mRNA containing expanded CUG repeats forms stable hairpin structures that aggregate into nuclear RNA foci. These foci sequester muscleblind-like proteins (MBNL1/2) and upregulate CELF1, disrupting alternative splicing of CLCN1 (causing myotonia) and INSR (insulin resistance).",
    "example": "Fluorescence in situ hybridization (FISH) using CAG probes reveals dense ribonuclear foci in cortical and skeletal muscle nuclei of DM1 patients."
  },
  {
    "level": 2,
    "topic": "Huntington's Disease CAG Repeat Thresholds",
    "prompt": "In the HTT gene on chromosome 4p16.3, what CAG repeat length defines the threshold for 100% full penetrance of Huntington's disease within a normal human lifespan?",
    "options": [
      "40 or more CAG repeats",
      "27 to 35 repeats",
      "10 to 26 repeats",
      "60 or more repeats only"
    ],
    "answer": 0,
    "explain": "Normal alleles have <27 CAG repeats; intermediate alleles (27-35) do not cause disease but may expand in paternal transmission; reduced penetrance occurs at 36-39 repeats; full penetrance occurs at 40 or more repeats.",
    "example": "A predictive genetic test demonstrating 44 CAG repeats in HTT confirms that the individual will develop Huntington's chorea if they live a normal lifespan."
  },
  {
    "level": 2,
    "topic": "Fragile X Tremor/Ataxia Syndrome (FXTAS)",
    "prompt": "Carriers of an FMR1 premutation (55 to 200 CGG repeats) do not develop Fragile X syndrome, but older adult males are at high risk of developing:",
    "options": [
      "FXTAS: late-onset progressive intention tremor, cerebellar ataxia, and intranuclear ubiquitin-positive inclusions caused by toxic RNA gain-of-function",
      "Early-infantile epileptic encephalopathy with profound intellectual disability",
      "Spastic diplegia and optic nerve hypoplasia",
      "Juvenile-onset Huntington-like chorea"
    ],
    "answer": 0,
    "explain": "Premutation carriers have elevated FMR1 mRNA levels (2-8x normal) despite normal or slightly reduced FMRP protein. The excess CGG-expanded mRNA forms toxic nuclear inclusions that recruit RNA-binding proteins, causing neurodegeneration in older men.",
    "example": "MRI of an elderly male presenting with progressive gait ataxia reveals bilateral T2/FLAIR hyperintensities in the middle cerebellar peduncles (the classic 'MCP sign' of FXTAS)."
  },
  {
    "level": 2,
    "topic": "Friedreich's Ataxia Molecular Pathogenesis",
    "prompt": "Friedreich's Ataxia (FRDA) is an autosomal recessive condition caused by an intronic GAA repeat expansion in FXN that leads to:",
    "options": [
      "Severe transcriptional silencing of frataxin, impairing mitochondrial iron-sulfur (Fe-S) cluster biogenesis and causing mitochondrial iron overload",
      "Overproduction of toxic polyalanine aggregates in the cytoplasm",
      "Constitutive hyperactivation of electron transport chain Complex I",
      "Premature degradation of mitochondrial DNA helicase"
    ],
    "answer": 0,
    "explain": "The GAA expansion in intron 1 of FXN forms sticky DNA triplex structures and R-loops that promote heterochromatin spreading (H3K9me3), silencing frataxin expression. Frataxin is essential for Fe-S cluster biogenesis; its absence causes mitochondrial iron accumulation and oxidative stress.",
    "example": "Patients present in adolescence with progressive sensory and cerebellar ataxia, loss of deep tendon reflexes, hypertrophic cardiomyopathy, and scoliosis."
  },
  {
    "level": 2,
    "topic": "Spinocerebellar Ataxia Type 3 (Machado-Joseph)",
    "prompt": "The most common autosomal dominant hereditary ataxia worldwide, Spinocerebellar Ataxia Type 3 (SCA3 or Machado-Joseph disease), is caused by a CAG polyglutamine expansion in:",
    "options": [
      "ATXN3 (encoding ataxin-3, a deubiquitinating enzyme)",
      "ATXN1",
      "CACNA1A",
      "TBP"
    ],
    "answer": 0,
    "explain": "SCA3 is caused by CAG expansion (>60 repeats) in ATXN3. Mutant ataxin-3 accumulates in nuclear inclusions, impairing ubiquitin-proteasome system function and inducing progressive degeneration of cerebellar dentate nuclei, substantia nigra, and motor tracts.",
    "example": "Clinical presentation includes progressive ataxia, bulging eyes, facial fasciculations, spasticity, and parkinsonian features."
  },
  {
    "level": 2,
    "topic": "Wilson's Disease Copper Transport Defect",
    "prompt": "Wilson's disease is an autosomal recessive disorder of copper metabolism caused by mutations in the P-type ATPase gene:",
    "options": [
      "ATP7B",
      "ATP7A",
      "SLC30A1",
      "CP (ceruloplasmin)"
    ],
    "answer": 0,
    "explain": "ATP7B mediates copper excretion into bile and copper incorporation into apoceruloplasmin in hepatocytes. Inactive ATP7B leads to copper accumulation in liver, basal ganglia (causing parkinsonism and dystonia), and Descemet's membrane of the cornea (Kayser-Fleischer rings).",
    "example": "Serum testing demonstrates low ceruloplasmin, elevated 24-hour urinary copper excretion, and response to copper chelators like D-penicillamine or trientine."
  },
  {
    "level": 2,
    "topic": "Menkes Disease X-Linked Copper Deficiency",
    "prompt": "Menkes disease, characterized by kinky brittle hair, severe neurodevelopmental failure, and arterial tortuosity, is caused by loss-of-function mutations in:",
    "options": [
      "ATP7A (impaired intestinal copper absorption and copper delivery to the brain)",
      "ATP7B",
      "SOD1",
      "SLC11A2"
    ],
    "answer": 0,
    "explain": "ATP7A exports copper across the basolateral membrane of enterocytes and across the blood-brain barrier. Mutations prevent copper absorption, resulting in systemic and cerebral copper deficiency, crippling copper-dependent enzymes (cytochrome c oxidase, dopamine beta-hydroxylase, lysyl oxidase).",
    "example": "Subcutaneous copper histidinate therapy initiated in the first weeks of life can bypass intestinal block and prevent severe neurodegeneration in some Menkes infants."
  },
  {
    "level": 2,
    "topic": "Phenylketonuria PAH Enzyme Defect",
    "prompt": "Classic Phenylketonuria (PKU) leads to severe intellectual disability and hypopigmentation if untreated, caused by deficiency of:",
    "options": [
      "Phenylalanine hydroxylase (PAH), which converts phenylalanine to tyrosine in the presence of tetrahydrobiopterin (BH4)",
      "Tyrosine hydroxylase (TH)",
      "Dopamine beta-hydroxylase (DBH)",
      "Homogentisate 1,2-dioxygenase"
    ],
    "answer": 0,
    "explain": "PAH deficiency causes toxic plasma and brain accumulation of phenylalanine, which saturates the LAT1 (SLC7A5) large neutral amino acid transporter at the blood-brain barrier, starving the brain of tyrosine and tryptophan and inhibiting myelin synthesis.",
    "example": "Newborn blood-spot screening (Guthrie card) detects elevated Phe/Tyr ratios, allowing immediate dietary phenylalanine restriction to prevent cognitive impairment."
  },
  {
    "level": 2,
    "topic": "Gaucher Disease GBA1 Mutations and Parkinson's",
    "prompt": "Heterozygous carrier status for loss-of-function mutations in GBA1 (encoding lysosomal glucocerebrosidase) represents the most common known genetic risk factor for:",
    "options": [
      "Parkinson's disease and Lewy body dementia (increasing risk 5- to 8-fold)",
      "Amyotrophic lateral sclerosis",
      "Huntington's disease",
      "Spinal muscular atrophy"
    ],
    "answer": 0,
    "explain": "Glucocerebrosidase hydrolyzes glucosylceramide in lysosomes. Mutant GBA1 impairs lysosomal autophagy, stabilizing alpha-synuclein oligomers and promoting Lewy body pathology in dopaminergic neurons.",
    "example": "Approximately 5-10% of idiopathic Parkinson's disease patients carry a heterozygous GBA1 mutation (such as N370S or L444P)."
  },
  {
    "level": 2,
    "topic": "Niemann-Pick Type C Lysosomal Trafficking",
    "prompt": "Niemann-Pick Disease Type C (NPC) is a neurovisceral lysosomal lipid storage disease characterized by vertical supranuclear gaze palsy and cerebellar ataxia, caused by mutations in:",
    "options": [
      "NPC1 or NPC2, which mediate unesterified cholesterol export from the lysosomal compartment",
      "SMPD1 (acid sphingomyelinase)",
      "HEXA",
      "GLB1"
    ],
    "answer": 0,
    "explain": "NPC1 (transmembrane lysosomal protein) and NPC2 (soluble luminal cholesterol-binding protein) cooperatively export unesterified cholesterol out of late endosomes/lysosomes. Mutations trap cholesterol and glycosphingolipids, causing selective Purkinje cell loss.",
    "example": "Filipin staining of patient fibroblasts reveals intense fluorescent accumulation of unesterified cholesterol within perinuclear lysosomes."
  },
  {
    "level": 2,
    "topic": "Prion Protein Codon 129 Polymorphism",
    "prompt": "In human prion diseases (such as sporadic and variant Creutzfeldt-Jakob disease), which common coding polymorphism in PRNP heavily influences susceptibility and incubation time?",
    "options": [
      "Methionine vs Valine at codon 129 (Met129Val)",
      "Alanine vs Glycine at codon 53",
      "Lysine vs Arginine at codon 670",
      "Proline vs Leucine at codon 102"
    ],
    "answer": 0,
    "explain": "Homozygosity at codon 129 (129Met/Met or 129Val/Val) dramatically accelerates prion conversion kinetics compared to heterozygosity (129Met/Val). Nearly 100% of confirmed cases of variant CJD (vCJD) from bovine prions occurred in 129Met/Met homozygotes.",
    "example": "Codon 129 profiling in human prion cohorts demonstrates that Met/Val heterozygotes exhibit significantly longer disease incubation times and prolonged clinical courses."
  },
  {
    "level": 2,
    "topic": "Duchenne vs Becker Reading Frame Rule",
    "prompt": "The 'reading frame hypothesis' (Monaco rule) explains why deletions in the massive DMD gene cause either severe Duchenne muscular dystrophy (DMD) or milder Becker muscular dystrophy (BMD) based on:",
    "options": [
      "DMD deletions disrupt the translational open reading frame (out-of-frame), causing premature stop codons and complete absence of dystrophin, whereas BMD deletions maintain the reading frame (in-frame), producing a shorter but partially functional protein",
      "BMD mutations occur in the promoter, while DMD mutations occur in introns",
      "DMD is caused by duplication of the entire chromosome, while BMD is a point mutation",
      "BMD is autosomal dominant, while DMD is X-linked recessive"
    ],
    "answer": 0,
    "explain": "The reading-frame rule holds true in >90% of dystrophinopathy cases. In-frame deletions (e.g. exons 45-47) preserve the C-terminal dystroglycan-binding domain, whereas out-of-frame deletions trigger nonsense-mediated decay or unstable truncated dystrophin.",
    "example": "Exon-skipping therapeutics (such as eteplirsen for exon 51) are designed to restore an out-of-frame transcript into an in-frame Becker-like transcript."
  },
  {
    "level": 3,
    "topic": "Dravet Syndrome SCN1A Interneuron Disinhibition",
    "prompt": "In Dravet syndrome (severe myoclonic epilepsy of infancy), why do heterozygous loss-of-function mutations in SCN1A (Nav1.1) cause profound epileptic hyperexcitability rather than hypoexcitability?",
    "options": [
      "Nav1.1 is preferentially expressed in parvalbumin-positive GABAergic interneurons; loss of Nav1.1 impairs interneuron action potential generation, causing network disinhibition",
      "Nav1.1 mutations generate a 10-fold gain-of-function current in pyramidal neurons",
      "Nav1.1 selectively pumps potassium into astrocytes",
      "Mutant Nav1.1 channels cleave GABA receptors on postsynaptic membranes"
    ],
    "answer": 0,
    "explain": "William Catterall and colleagues proved that Nav1.1 channels carry the vast majority of sodium current in fast-spiking PV+ cortical and hippocampal interneurons. Nav1.1 haploinsufficiency cripples interneuron firing, abolishing inhibitory brake control and causing runaway network seizures.",
    "example": "Sodium channel-blocking antiepileptic drugs (e.g. carbamazepine, phenytoin) exacerbate seizures in Dravet syndrome patients by further suppressing residual interneuron Nav1.1 activity."
  },
  {
    "level": 3,
    "topic": "SCN2A Phenotypic Dichotomy",
    "prompt": "Mutations in SCN2A (encoding Nav1.2) exhibit a striking genotype-phenotype correlation where:",
    "options": [
      "Gain-of-function missense mutations cause early-onset epileptic encephalopathy (<3 months of age), whereas loss-of-function (protein-truncating) mutations cause autism spectrum disorder and intellectual disability without early infantile seizures",
      "Loss-of-function mutations cause neonatal seizures, while gain-of-function causes late-onset dementia",
      "All mutations produce identical forms of adult-onset myoclonus",
      "Mutations only affect cardiac conduction, leaving the brain unaffected"
    ],
    "answer": 0,
    "explain": "Nav1.2 is expressed along unmyelinated axons and the axon initial segment during early development before being replaced by Nav1.6 at nodes. Gain-of-function mutations hyperpolarize activation or slow inactivation, driving infantile seizures. Truncating loss-of-function mutations decrease neuronal excitability and synaptic transmission, leading to ASD/ID.",
    "example": "Electrophysiological whole-cell voltage clamp of patient-derived SCN2A variants classifies variants into GOF (responsive to sodium blockers) vs LOF (worsened by sodium blockers)."
  },
  {
    "level": 3,
    "topic": "SCN8A Encephalopathy Gain of Function",
    "prompt": "Early infantile epileptic encephalopathy type 13 (EIEE13) caused by de novo mutations in SCN8A (Nav1.6) is typically driven by:",
    "options": [
      "Gain-of-function mutations that impair channel inactivation, generating persistent non-inactivating sodium currents and spontaneous repetitive firing in pyramidal neurons",
      "Complete deletion of the SCN8A gene locus",
      "Selective blockade of potassium permeation through Nav1.6",
      "Premature termination codons triggering nonsense-mediated decay"
    ],
    "answer": 0,
    "explain": "Nav1.6 is the dominant channel at mature axon initial segments and nodes of Ranvier. De novo missense SCN8A mutations (such as N1768D) shift activation to hyperpolarized voltages and elevate persistent inward Na+ currents, causing severe treatment-resistant epilepsy and high SUDEP risk.",
    "example": "High-dose sodium channel blockers (such as oxcarbazepine or phenytoin) often provide selective seizure control in SCN8A gain-of-function patients."
  },
  {
    "level": 3,
    "topic": "CACNA1A Allelic Disorders",
    "prompt": "The P/Q-type voltage-gated calcium channel alpha1A subunit gene, CACNA1A, is an example of an allelic series where different mutation classes produce:",
    "options": [
      "Episodic Ataxia type 2 (loss of function / truncating), Familial Hemiplegic Migraine type 1 (gain of function missense), and SCA6 (small polyglutamine expansion in the C-terminus)",
      "Dravet syndrome, Rett syndrome, and Fragile X syndrome",
      "Parkinson's disease, Huntington's disease, and ALS",
      "Only pure hereditary spastic paraplegia across all alleles"
    ],
    "answer": 0,
    "explain": "CACNA1A encodes Cav2.1. Truncating mutations cause haploinsufficiency, manifesting as Episodic Ataxia 2 (acetazolamide-responsive). Missense mutations enhancing Ca2+ influx cause FHM1. Small CAG expansions (20-33 repeats) in the cytoplasmic tail cause pure cerebellar ataxia (SCA6).",
    "example": "A family presenting with hemiplegic aura lasting hours following mild head trauma is found to carry a missense CACNA1A mutation (e.g. T666M) that increases Cav2.1 channel open probability."
  },
  {
    "level": 3,
    "topic": "KCNQ2/KCNQ3 Channelopathies",
    "prompt": "Benign Familial Neonatal Seizures (BFNS) are caused by heterozygous loss-of-function mutations in KCNQ2 or KCNQ3, which encode subunits of:",
    "options": [
      "The Kv7 potassium channel responsible for the subthreshold, non-inactivating M-current (I_M)",
      "The ATP-sensitive inward rectifier K+ channel (K_ATP)",
      "The high-conductance calcium-activated potassium channel (BK)",
      "The cardiac hERG delayed rectifier channel"
    ],
    "answer": 0,
    "explain": "Kv7.2 and Kv7.3 form heterotetrameric potassium channels at the axon initial segment. The M-current activates at subthreshold voltages (-60 mV) and does not inactivate, acting as a critical brake on repetitive firing. Even a modest 25% reduction in M-current causes neonatal hyperexcitability.",
    "example": "The pharmacological Kv7 opener retigabine (ezogabine) hyperpolarizes the membrane and suppresses seizure firing in KCNQ2 encephalopathy models."
  },
  {
    "level": 3,
    "topic": "GLUT1 Deficiency Syndrome Genetics",
    "prompt": "De novo or inherited heterozygous mutations in SLC2A1 cause GLUT1 Deficiency Syndrome (De Vivo disease), clinically characterized by infantile seizures, developmental delay, and microcephaly, diagnosable by:",
    "options": [
      "Hypoglycorrhachia: a profoundly reduced cerebrospinal fluid (CSF) glucose concentration with a CSF-to-blood glucose ratio <0.4 in the absence of meningitis",
      "Hyperglycemia with elevated CSF lactate >5.0 mM",
      "Excessive urinary excretion of copper",
      "Elevated phenylalanine levels on newborn screening"
    ],
    "answer": 0,
    "explain": "GLUT1 is the primary transporter facilitating D-glucose passage across the blood-brain barrier endothelial cells. When defective, brain glucose delivery fails, starving neurons of their primary metabolic substrate despite normal peripheral blood glucose.",
    "example": "Patients show dramatic therapeutic response to a high-fat, low-carbohydrate ketogenic diet, which provides ketone bodies (acetoacetate and beta-hydroxybutyrate) as an alternate fuel via MCT1."
  },
  {
    "level": 3,
    "topic": "Rett Syndrome MECP2 Epigenetics",
    "prompt": "Mutations in the X-linked gene MECP2 cause Rett syndrome in females. At the molecular level, MeCP2 protein functions primarily as:",
    "options": [
      "An epigenetic reader that binds 5-methylcytosine (5mC) and 5-hydroxymethylcytosine (5hmC) in DNA, recruiting the NCoR/SMRT corepressor complex to modulate chromatin architecture and repress transcription",
      "A cytosolic kinase that phosphorylates tau at Ser202",
      "A vesicular neurotransmitter transporter for glycine",
      "A core component of the spliceosomal U1 snRNP"
    ],
    "answer": 0,
    "explain": "MeCP2 contains a methyl-CpG-binding domain (MBD) and a transcriptional repression domain (TRD). It binds methylated DNA across the neuronal genome and recruits histone deacetylases (HDAC3 via NCoR/SMRT), fine-tuning the expression of thousands of genes (including BDNF) essential for synaptic maturation.",
    "example": "Adrian Bird's laboratory demonstrated that genetic reactivation of Mecp2 in adult symptomatic Rett mouse models reverses neurological deficits and normalizes synaptic density."
  },
  {
    "level": 3,
    "topic": "Angelman Syndrome UBE3A Imprinting",
    "prompt": "Angelman syndrome ('happy puppet' syndrome, severe speech impairment, ataxia, paroxysms of laughter) is caused by loss of function of UBE3A, which is uniquely imprinted in neurons such that:",
    "options": [
      "Only the maternally inherited UBE3A allele is active in neurons, while the paternal allele is silenced in cis by a long non-coding antisense transcript (UBE3A-ATS)",
      "Only the paternal UBE3A allele is active in neurons",
      "Both alleles are expressed equally in neurons but silenced in glia",
      "The gene is translocated to the mitochondrial genome"
    ],
    "answer": 0,
    "explain": "In mature mammalian neurons, the paternal UBE3A allele is repressed by the long non-coding antisense RNA transcript UBE3A-ATS. Consequently, any maternal mutation, maternal 15q11-q13 microdeletion, or paternal uniparental disomy leaves neurons completely devoid of functional UBE3A ubiquitin ligase.",
    "example": "Antisense oligonucleotides (ASOs) targeting UBE3A-ATS degrade the repressor transcript, successfully un-silencing the intact paternal UBE3A allele in preclinical models."
  },
  {
    "level": 3,
    "topic": "Prader-Willi Syndrome SNORD116 Cluster",
    "prompt": "Unlike Angelman syndrome, Prader-Willi syndrome (neonatal hypotonia followed by insatiable hyperphagia, morbid obesity, and hypogonadism) results from loss of expression of paternally inherited genes on 15q11-q13, critical among which is:",
    "options": [
      "The SNORD116 small nucleolar RNA (snoRNA) cluster",
      "The UBE3A catalytic domain",
      "The MECP2 methyl-binding domain",
      "The FMR1 CGG repeat tract"
    ],
    "answer": 0,
    "explain": "Microdeletions specifically restricted to the paternally expressed SNORD116 C/D box snoRNA cluster recapitulate the core hypothalamic phenotype of Prader-Willi syndrome, demonstrating that loss of these non-coding snoRNAs impairs prohormone processing in POMC neurons.",
    "example": "High-resolution chromosomal microarray in atypical PWS patients identifies minimal critical deletions pinpointed strictly to the SNORD116 locus."
  },
  {
    "level": 3,
    "topic": "Tuberous Sclerosis Complex mTORC1 Hyperactivation",
    "prompt": "In Tuberous Sclerosis Complex (TSC), loss-of-function mutations in either TSC1 (hamartin) or TSC2 (tuberin) lead to subependymal giant cell astrocytomas (SEGAs) and cortical tubers because:",
    "options": [
      "The TSC1-TSC2 complex acts as a GTPase-activating protein (GAP) for the small GTPase Rheb; loss of the complex locks Rheb in an active GTP-bound state that constitutively hyperactivates mTORC1",
      "The complex directly degrades insulin receptors on the cell surface",
      "The complex blocks ribosomal RNA transcription in the nucleolus",
      "Loss of the complex causes constitutive opening of mitochondrial permeability transition pores"
    ],
    "answer": 0,
    "explain": "TSC1 and TSC2 form a functional heterodimer. TSC2 harbors the GAP catalytic domain that accelerates GTP hydrolysis on Rheb (Rheb-GTP to Rheb-GDP). Loss of either protein leaves Rheb-GTP unrestrained, driving permanent mTORC1 hyperactivation, p70S6K phosphorylation, dysplastic cell growth, and intractable epilepsy.",
    "example": "Treatment with mTORC1 allosteric inhibitors such as rapamycin (sirolimus) or everolimus regresses SEGA tumor volume and reduces seizure frequency in TSC patients."
  },
  {
    "level": 3,
    "topic": "Neurofibromatosis Type 1 Ras-GAP Defect",
    "prompt": "Neurofibromatosis type 1 (NF1, von Recklinghausen disease) is caused by mutations in NF1 on chromosome 17q11.2, whose protein product neurofibromin normally functions as:",
    "options": [
      "A negative regulator of p21-Ras that accelerates hydrolysis of active Ras-GTP to inactive Ras-GDP",
      "A tyrosine kinase that phosphorylates epidermal growth factor receptors",
      "A nuclear receptor for thyroid hormone",
      "A structural microtubule-associated protein stabilizing axons"
    ],
    "answer": 0,
    "explain": "Neurofibromin contains a GAP-related domain (GRD) that inactivates Ras. Loss-of-function mutations lead to hyperactive downstream Ras-Raf-MEK-ERK signaling, driving benign and malignant nerve sheath tumors (neurofibromas, optic pathway gliomas).",
    "example": "The MEK inhibitor selumetinib received FDA approval for pediatric patients with inoperable plexiform neurofibromas based on tumor shrinkage."
  },
  {
    "level": 3,
    "topic": "Lissencephaly LIS1 vs Doublecortin DCX",
    "prompt": "Classical lissencephaly ('smooth brain') results from defective neuronal migration. What distinguishes mutations in LIS1 (PAFAH1B1) from Doublecortin (DCX)?",
    "options": [
      "LIS1 is autosomal dominant causing a posterior-predominant lissencephaly gradient, whereas DCX is X-linked, causing anterior-predominant lissencephaly in hemizygous males and subcortical band heterotopia ('double cortex') in heterozygous females",
      "DCX causes cerebellar hypoplasia, while LIS1 affects only the spinal cord",
      "LIS1 mutations affect only astrocytes, whereas DCX affects only microglia",
      "DCX is an mitochondrial enzyme, while LIS1 is an ion channel"
    ],
    "answer": 0,
    "explain": "Both proteins regulate microtubule dynamics during radial neuroblast migration (LIS1 interacts with cytoplasmic dynein; DCX binds microtubules directly). DCX on Xq22.3 causes severe smooth brain in males, but random X-inactivation in females creates two populations of migrating neurons, resulting in an arrest of half the neurons in the subcortical white matter (double cortex).",
    "example": "Brain MRI of a female with drug-resistant epilepsy revealing a uniform band of heterotopic gray matter beneath the cortex confirms subcortical band heterotopia due to a DCX mutation."
  },
  {
    "level": 3,
    "topic": "FOXP2 Forkhead Domain Speech Apraxia",
    "prompt": "The discovery of the KE family by Fisher, Vargha-Khadem, and colleagues identified a point mutation (R553H) in FOXP2 on chromosome 7q31, defining its role in:",
    "options": [
      "Severe developmental verbal dyspraxia and orofacial motor sequencing deficits through impairment of its forkhead DNA-binding transcription factor domain",
      "Complete congenital bilateral deafness",
      "Childhood-onset blindness due to photoreceptor degeneration",
      "Primary motor neuron degeneration identical to ALS"
    ],
    "answer": 0,
    "explain": "FOXP2 is a winged-helix/forkhead transcription factor expressed in corticostriatal and olivocerebellar circuits. The R553H mutation resides in the DNA-binding domain, disrupting transcription of downstream target genes (such as CNTNAP2) necessary for motor learning of speech articulation.",
    "example": "Humanized mice carrying two human-specific amino acid substitutions in Foxp2 display accelerated ultrasonic vocalization maturation and altered striatal synaptic plasticity."
  },
  {
    "level": 3,
    "topic": "SHANK3 Haploinsufficiency Phelan-McDermid",
    "prompt": "Haploinsufficiency or microdeletions of SHANK3 on chromosome 22q13.3 cause Phelan-McDermid syndrome, characterized by severe expressive language delay, hypotonia, and autism, because Shank3:",
    "options": [
      "Is a master postsynaptic scaffold protein that crosslinks Homer-mGluR complexes to GKAP-PSD-95-NMDA receptor complexes in dendritic spines",
      "Transports dopamine across the blood-brain barrier",
      "Forms the voltage sensor of Nav1.1 channels",
      "Degrades beta-amyloid plaques in the extracellular matrix"
    ],
    "answer": 0,
    "explain": "Shank3 forms a sheet-like platform at the base of the postsynaptic density via SAM domain oligomerization, bridging NMDA/AMPA receptors to actin filaments. Shank3 loss causes spine thinning, reduced mEPSC amplitude, and impaired corticostriatal transmission.",
    "example": "Shank3 complete knockout mice show compulsive self-grooming leading to skin lesions and marked deficits in social interaction."
  },
  {
    "level": 3,
    "topic": "SYNGAP1 Synaptic Plasticity Mutations",
    "prompt": "De novo loss-of-function mutations in SYNGAP1 cause intellectual disability, autism, and generalized epilepsy because SynGAP protein:",
    "options": [
      "Is a postsynaptic density Ras/Rap-GAP that negatively regulates Ras-ERK signaling to limit AMPA receptor synaptic insertion during basal transmission",
      "Directly pumps chloride out of developing neurons",
      "Synthesizes acetylcholine from choline and acetyl-CoA",
      "Packs synaptic vesicles with glutamate at the presynaptic active zone"
    ],
    "answer": 0,
    "explain": "SynGAP is a major component of the PSD (~3% of total protein) phosphorylated by CaMKII. It hydrolyzes Ras-GTP to Ras-GDP, suppressing premature AMPA receptor exocytosis. Syngap1 haploinsufficiency leads to premature unsilencing of synapses and precocious critical period maturation.",
    "example": "Syngap1+/- heterozygous mice show abnormally elevated basal AMPA receptor levels in dendritic spines and collapsed synaptic plasticity."
  },
  {
    "level": 4,
    "topic": "22q11.2 Microdeletion DGCR8 Microprocessor",
    "prompt": "Individuals with 22q11.2 deletion syndrome (DiGeorge / Velocardiofacial syndrome) have a ~30-fold increased risk of developing schizophrenia. Molecularly, hemizygosity of DGCR8 contributes to this risk because:",
    "options": [
      "DGCR8 is an essential subunit of the nuclear microprocessor complex that associates with Drosha to cleave primary microRNAs (pri-miRNAs) into pre-miRNAs",
      "DGCR8 encodes the catalytic subunit of DNA polymerase epsilon",
      "DGCR8 is the sole transporter of serotonin across the synaptic cleft",
      "DGCR8 directly blocks dopamine D2 receptor internalization"
    ],
    "answer": 0,
    "explain": "The 3 Mb 22q11.2 microdeletion removes DGCR8, leading to haploinsufficiency in microRNA biogenesis throughout the brain. This dysregulates hundreds of microRNAs (such as miR-185), perturbing neuronal morphogenesis, dendritic spine stability, and cortical connectivity.",
    "example": "Dgcr8+/- mouse models exhibit widespread ~20-30% reductions in mature microRNA levels and abnormal hippocampal-prefrontal functional synchrony."
  },
  {
    "level": 4,
    "topic": "16p11.2 Reciprocal CNV Mirror Phenotypes",
    "prompt": "The reciprocal copy number variation at chromosome 16p11.2 (~600 kb, 29 genes) produces striking mirror brain phenotypes where:",
    "options": [
      "Microdeletion causes macrocephaly, obesity, and increased risk of autism, whereas microduplication causes microcephaly, low BMI, and high risk of schizophrenia",
      "Microdeletion causes congenital blindness, whereas duplication causes deafness",
      "Microdeletion causes ALS, whereas duplication causes Parkinson's",
      "Microdeletion is universally lethal at conception, while duplication is asymptomatic"
    ],
    "answer": 0,
    "explain": "16p11.2 is one of the clearest examples of gene dosage-dependent brain morphogenesis. Genes in the region (including MAPK3, KCTD13, TAOK2) regulate progenitor proliferation: deletion causes hyper-proliferation (macrocephaly/ASD), whereas duplication promotes premature differentiation/apoptosis (microcephaly/schizophrenia).",
    "example": "Volumetric MRI studies in 16p11.2 CNV carriers demonstrate dose-dependent linear scaling of total brain volume across 1, 2, and 3 genomic copy states."
  },
  {
    "level": 4,
    "topic": "GWAS Genome-Wide Significance Threshold",
    "prompt": "Why is the statistical significance threshold in human Genome-Wide Association Studies (GWAS) traditionally set at p < 5 x 10^-8 rather than p < 0.05?",
    "options": [
      "It represents a Bonferroni correction for approximately 1,000,000 independent linkage disequilibrium (LD) test blocks across the human genome (0.05 / 10^6)",
      "It accounts for experimental pipetting errors in DNA microarrays",
      "It represents the exact number of base pairs on the X chromosome",
      "It is chosen arbitrarily to guarantee that no false positives ever occur"
    ],
    "answer": 0,
    "explain": "Although dense arrays genotype millions of SNPs, linkage disequilibrium means SNPs are not independent. In European populations, the genome resolves into ~1 million independent LD blocks. Applying Bonferroni correction for 1 million tests yields alpha = 0.05 / 1,000,000 = 5 x 10^-8.",
    "example": "A locus reaching p = 2 x 10^-7 is considered 'suggestive' but fails genome-wide significance, requiring replication in larger meta-analytic cohorts."
  },
  {
    "level": 4,
    "topic": "LD Score Regression (LDSC) Polygenicity vs Stratification",
    "prompt": "In psychiatric and statistical genetics, Linkage Disequilibrium Score Regression (LDSC) evaluates summary statistics to distinguish true polygenicity from confounding population stratification by:",
    "options": [
      "Regressing GWAS test statistics (chi-square) against LD scores; true polygenic signals scale linearly with the amount of genetic variation tagged, while the regression intercept quantifies confounding inflation",
      "Sequencing all family members to track Mendelian segregation",
      "Counting the total number of chromosomes in blood lymphocytes",
      "Measuring the fluorescence intensity of homozygous probes on DNA microarrays"
    ],
    "answer": 0,
    "explain": "Under a polygenic model, a SNP in a region of high LD tags more causal variants by chance, so its expected chi-square test statistic is higher. Confounding bias (population stratification or cryptic relatedness) inflates chi-square uniformly regardless of LD score, appearing as an intercept > 1.0.",
    "example": "Schizophrenia GWAS summary statistics show an LDSC intercept of ~1.02 despite massive genomic inflation (lambda_GC > 1.4), proving that the signal is driven by polygenic architecture rather than ancestral stratification."
  },
  {
    "level": 4,
    "topic": "Polygenic Risk Score (PRS) Methodology",
    "prompt": "A Polygenic Risk Score (PRS) for a complex neuropsychiatric disorder (e.g. major depression or bipolar disorder) is calculated for an individual by:",
    "options": [
      "Summing the count of risk alleles (0, 1, or 2) across thousands of genome-wide SNPs, each weighted by its effect size (log odds ratio beta) derived from an independent discovery GWAS",
      "Measuring the telomere length of peripheral leukocytes",
      "Sequencing the single most pathogenic mutation in mitochondrial DNA",
      "Averaging the methylation percentage across all CpG islands"
    ],
    "answer": 0,
    "explain": "PRS = sum(beta_i * dosage_i). The PRS captures an individual's cumulative burden of common risk alleles. While inadequate for individual clinical diagnosis due to low predictive power, PRS effectively stratifies populations into high- vs low-risk deciles.",
    "example": "Individuals in the top 10% of schizophrenia PRS show approximately a 3- to 4-fold higher odds of developing psychosis compared to those in the lowest decile."
  },
  {
    "level": 4,
    "topic": "PsychENCODE Brain eQTL and sQTL Colocalization",
    "prompt": "How does Bayesian colocalization analysis (e.g. coloc) integrate psychiatric GWAS risk loci with brain postmortem eQTL/sQTL data?",
    "options": [
      "It calculates the posterior probability that the causal variant driving disease risk and the variant altering gene expression or splicing in brain tissue are one and the same single nucleotide variant",
      "It merges clinical hospital records with genomic sequencing files",
      "It tests whether two different patients carry identical rare deletions",
      "It determines if viral RNA is present in postmortem brain slices"
    ],
    "answer": 0,
    "explain": "Colocalization evaluates five hypotheses (H0-H4). Posterior probability of H4 (PPH4 > 0.8) indicates that the GWAS trait and the molecular QTL share a single causal variant, prioritizing candidate effector genes over mere physical proximity.",
    "example": "Colocalization of schizophrenia GWAS locus 3p21.1 with human frontal cortex sQTLs pinpointed aberrant splicing of the actin-binding gene CLCN3 as the functional driver."
  },
  {
    "level": 4,
    "topic": "Chromatin Looping Hi-C at Non-Coding GWAS Loci",
    "prompt": "Because over 90% of neuropsychiatric GWAS risk variants reside in non-coding intergenic or intronic regions, Chromosome Conformation Capture (Hi-C) in human neural progenitor cells reveals that:",
    "options": [
      "Risk SNPs frequently reside within cell-type-specific distal enhancers that loop across hundreds of kilobases to physically contact target gene promoters, often bypassing the nearest linear gene",
      "All non-coding SNPs are sequencing artifacts that do not exist in vivo",
      "Non-coding SNPs are translated into novel toxic micropeptides in the nucleus",
      "Enhancers can only contact promoters situated within 500 base pairs"
    ],
    "answer": 0,
    "explain": "Linear proximity is a poor predictor of target genes. Hi-C and Micro-C maps demonstrate that 3D chromatin loops bring distal non-coding regulatory elements into physical proximity with promoters within topologically associating domains (TADs).",
    "example": "In human fetal brain Hi-C maps, schizophrenia risk variants in an intron of FOXG1 loop across 700 kb to regulate the promoter of distant PRMT7."
  },
  {
    "level": 4,
    "topic": "Twin Concordance and Schizophrenia Heritability",
    "prompt": "Classical twin studies establish the high genetic heritability (~80%) of schizophrenia based on the finding that:",
    "options": [
      "Monozygotic (identical) twins show a concordance rate of approximately 40-50%, compared to approximately 10-15% in dizygotic (fraternal) twins",
      "Monozygotic twins show 100% concordance, proving strictly Mendelian inheritance",
      "Dizygotic twins show higher concordance than monozygotic twins",
      "Concordance rates are identical between biological twins and adoptive siblings"
    ],
    "answer": 0,
    "explain": "The substantial gap between monozygotic (~48%) and dizygotic (~15%) concordance demonstrates strong additive genetic liability, while discordance among identical twins proves the contribution of environmental triggers and somatic/epigenetic factors.",
    "example": "Falconer's formula for heritability (h^2 = 2 * (r_MZ - r_DZ)) yields an estimated liability heritability of ~60-80% for schizophrenia and bipolar disorder."
  },
  {
    "level": 4,
    "topic": "SCHEMA Consortium Ultra-Rare Coding Variants",
    "prompt": "The Schizophrenia Exome Sequencing Meta-Analysis (SCHEMA) consortium identified 10 genes harboring ultra-rare, damaging coding mutations with large effect sizes (OR > 10-50), prominently featuring:",
    "options": [
      "SETD1A (histone methyltransferase), GRIN2A (NMDA receptor subunit GluN2A), and CUL1 (ubiquitin ligase component)",
      "APP, PSEN1, and PSEN2",
      "HTRA1, NOTCH3, and COL4A1",
      "DMD, SMN1, and FXN"
    ],
    "answer": 0,
    "explain": "SCHEMA sequenced >24,000 schizophrenia cases and identified high-impact protein-truncating variants (PTVs). Loss of SETD1A (epigenetic chromatin modifier) and GRIN2A (glutamatergic NMDA neurotransmission) confers massive individual odds ratios for psychosis.",
    "example": "Carriers of loss-of-function SETD1A mutations exhibit a >30-fold increased risk of developing schizophrenia accompanied by neurodevelopmental delay."
  },
  {
    "level": 4,
    "topic": "SPARK and ASC De Novo Autism Risk Architecture",
    "prompt": "Large-scale exome sequencing studies of autism simplex trios (Autism Sequencing Consortium and SPARK) demonstrated that de novo loss-of-function variants are heavily enriched in two distinct functional modules:",
    "options": [
      "Chromatin remodelers / transcriptional regulators (e.g. CHD8, ARID1B, KMT2C) and synaptic transmission / scaffolding proteins (e.g. SHANK3, SYNGAP1, SCN2A)",
      "Mitochondrial respiratory chain complexes and fatty acid oxidation enzymes",
      "Myelin sheath structural proteins and oligodendrocyte differentiation factors",
      "Extracellular collagen structural fibrils and integrin receptors"
    ],
    "answer": 0,
    "explain": "De novo mutations in ASD cluster into early embryonic nuclear regulators of gene expression (such as CHD8, which regulates thousands of downstream neurodevelopmental genes) and late-stage synaptic regulators that establish synaptic balance.",
    "example": "Patients with de novo CHD8 mutations share a recognizable syndromic subtype of autism characterized by macrocephaly, sleep disturbances, and gastrointestinal symptoms."
  },
  {
    "level": 4,
    "topic": "MAPT H1 vs H2 Inversion Haplotype",
    "prompt": "On chromosome 17q21.31, the MAPT locus exists as two major divergent haplotypes (H1 and H2) defined by a ~900 kb genomic inversion. Homozygosity for the H1 haplotype is strongly associated with increased risk of:",
    "options": [
      "Progressive Supranuclear Palsy (PSP) and Corticobasal Degeneration (CBD)",
      "Huntington's disease chorea",
      "Spinal muscular atrophy type 1",
      "Multiple sclerosis relapses"
    ],
    "answer": 0,
    "explain": "The H1/H2 inversion suppresses meiotic recombination across the 900 kb region. The H1 clade (and specifically the H1c sub-haplotype) drives higher overall MAPT transcription and higher 4R tau expression, conferring substantial risk for 4R tauopathies (PSP, CBD) and Parkinson's disease.",
    "example": "Over 90% of pathologically confirmed Progressive Supranuclear Palsy cases carry the homozygous H1/H1 genotype."
  },
  {
    "level": 5,
    "topic": "Single-Nucleus vs Single-Cell RNA-seq in Postmortem Brain",
    "prompt": "Why has single-nucleus RNA-sequencing (snRNA-seq) largely replaced single-cell RNA-sequencing (scRNA-seq) as the gold standard for profiling frozen human postmortem brain tissue?",
    "options": [
      "Intact single-cell enzymatic dissociation from frozen tissue causes severe cell lysis of fragile arborized neurons and induces massive artificial immediate-early gene stress responses, whereas mechanical isolation of nuclei is cold, rapid, and captures both neurons and glia without dissociation bias",
      "Nuclei contain 100 times more mRNA molecules than the surrounding cytoplasm",
      "snRNA-seq sequences only mitochondrial DNA, avoiding nuclear contamination",
      "Single-cell methods cannot separate cells by FACS"
    ],
    "answer": 0,
    "explain": "Enzymatic tissue digestion at 37°C destroys complex projection neurons and artificially activates microglial and astrocytic immediate early genes (c-Fos, EGR1). Flash-frozen postmortem tissue cannot yield viable intact single cells; isolated nuclei retain nascent nuclear transcripts that correlate >90% with whole-cell expression.",
    "example": "Droplet-based snRNA-seq of postmortem human prefrontal cortex readily resolves tens of thousands of nuclei into 40+ discrete neuronal and non-neuronal transcriptomic subclusters."
  },
  {
    "level": 5,
    "topic": "Single-Cell eQTLs in Microglial Alzheimer's Risk",
    "prompt": "Single-cell eQTL mapping in human Alzheimer's disease cohorts revealed that non-coding GWAS risk variants at loci such as BIN1, SPI1, and MS4A act as cis-eQTLs specifically in which cell type?",
    "options": [
      "Microglia, where they modulate transcription of genes governing phagocytosis and endolysosomal trafficking",
      "Layer 5 pyramidal projection neurons exclusively",
      "Myelinating oligodendrocytes in white matter tracts",
      "Cerebral capillary endothelial pericytes"
    ],
    "answer": 0,
    "explain": "Bulk brain tissue eQTLs dilute cell-type-specific signals. Single-cell eQTLs demonstrated that over 60% of late-onset Alzheimer's disease GWAS loci are enriched in microglial cis-regulatory elements, demonstrating that inherited AD risk is primarily driven by innate immune and myeloid clearance dysfunction.",
    "example": "The common AD risk variant rs1057233 acts as a potent eQTL downregulating SPI1 (PU.1) expression specifically in human microglia, altering cell survival and amyloid uptake."
  },
  {
    "level": 5,
    "topic": "Somatic MTOR Mosaicism in Focal Cortical Dysplasia",
    "prompt": "Focal Cortical Dysplasia type II (FCDII), the most common cause of intractable focal epilepsy in pediatric neurosurgery, is caused by low-level brain somatic mosaicism involving:",
    "options": [
      "Somatic activating missense mutations (1-5% variant allele frequency) in MTOR, PIK3CA, or AKT3 restricted specifically to dysplastic neuroglial cells in the epileptic lesion",
      "Germline homozygous deletions of the huntingtin gene",
      "Viral integration of Epstein-Barr virus into astrocytic DNA",
      "Complete loss of all mitochondrial genomes in white matter"
    ],
    "answer": 0,
    "explain": "Lee and colleagues (Nature Medicine 2015) performed deep amplicon sequencing (>1,000x coverage) on surgically resected FCDII brain tissue, discovering post-zygotic somatic mutations in MTOR (e.g. C1483Y, S2215Y). These mutations arise during early embryonic corticogenesis, hyperactivating mTORC1 and creating cytomegalic 'balloon cells' that trigger intractable focal seizures.",
    "example": "Surgical resection of the localized dysplastic lesion eliminates the mosaic mutated cells, curing the child of refractory seizures."
  },
  {
    "level": 5,
    "topic": "LINE-1 Retrotransposition in Neural Progenitors",
    "prompt": "Long Interspersed Nuclear Element-1 (LINE-1 or L1) retrotransposons contribute to somatic genomic diversity in the mammalian brain through which mechanism?",
    "options": [
      "Target-primed reverse transcription (TPRT): bicistronic L1 RNA encoding ORF1p (RNA chaperone) and ORF2p (endonuclease and reverse transcriptase) inserts de novo L1 cDNA copies into the nuclear genome of dividing neural progenitor cells",
      "Excision of DNA transposons via a cut-and-paste transposase",
      "Homologous recombination between telomeres and centromeres",
      "Direct translation of reverse transcriptase into the mitochondrial matrix"
    ],
    "answer": 0,
    "explain": "Human L1 is ~6 kb long and constitutes ~17% of the human genome. Most elements are retrotransposition-incompetent due to 5' truncations, but ~80-100 'hot' L1s escape epigenetic silencing in neurogenesis, generating novel somatic insertions that can alter neuronal gene expression.",
    "example": "Single-cell whole-genome sequencing of individual human hippocampal neurons estimates an average of 0.1 to 1 novel somatic L1 insertion per neuron."
  },
  {
    "level": 5,
    "topic": "Neuronal Non-CpG DNA Methylation (mCH)",
    "prompt": "Unlike most somatic tissues where DNA methylation occurs almost exclusively at CpG dinucleotides (mCG), mature mammalian neurons uniquely accumulate massive levels of non-CpG methylation (mCH, where H = A, C, or T) that:",
    "options": [
      "Accumulates postnatally during the period of maximal synaptogenesis, is deposited by de novo DNA methyltransferase DNMT3A, and is recognized and bound by MeCP2 to repress neuronal enhancers",
      "Is deposited exclusively in embryonic stem cells and erased at birth",
      "Causes immediate apoptosis of all cortical neurons if present",
      "Occurs only on the mitochondrial chromosome"
    ],
    "answer": 0,
    "explain": "Lister et al. (Science 2013) demonstrated that during postnatal brain development (ages 0-5 in humans), mCH (primarily mCA) surges to become as abundant as mCG in human frontal cortex neurons. DNMT3A deposits mCH, which provides high-density binding substrates for MeCP2 to modulate synaptic gene expression.",
    "example": "Conditional postnatal deletion of Dnmt3a in mouse forebrain neurons prevents mCH accumulation, causing behavioral abnormalities and defective synaptic maturation."
  },
  {
    "level": 5,
    "topic": "Ten-Eleven Translocation (TET) 5hmC Dynamics",
    "prompt": "Mammalian brain tissue harbors the highest levels of 5-hydroxymethylcytosine (5hmC, ~1% of all cytosines in cerebellar Purkinje neurons) of any organ, generated by:",
    "options": [
      "TET family dioxygenases (TET1, TET2, TET3) utilizing Fe(II) and alpha-ketoglutarate to iteratively oxidize 5-methylcytosine, facilitating active and passive DNA demethylation",
      "DNA methyltransferases operating in reverse without cofactors",
      "Polymerase chain reaction amplification artifacts",
      "Lysosomal degradation of methylated RNA primers"
    ],
    "answer": 0,
    "explain": "TET enzymes convert 5mC to 5hmC, and further to 5-formylcytosine (5fC) and 5-carboxylcytosine (5caC), which are recognized and excised by Thymine DNA Glycosylase (TDG) for base-excision repair, restoring unmethylated cytosine. In neurons, 5hmC also acts as a stable, long-lived epigenetic mark enriched at active enhancers and transcribed gene bodies.",
    "example": "Single-base resolution oxidative bisulfite sequencing (OxBS-seq) distinguishes 5hmC from 5mC across postmortem human brain genomes."
  },
  {
    "level": 5,
    "topic": "ADAR2 GluA2 Q/R RNA Editing Efficiency",
    "prompt": "In the mammalian brain, ADAR2 (ADARB1) catalyzes adenosine-to-inosine (A-to-I) hydrolytic deamination of the GluA2 pre-mRNA at the Q/R site with >99.9% efficiency, which ensures that:",
    "options": [
      "Codon 607 (CAG, glutamine) is edited to CIG (read as CGG, arginine), inserting a positively charged arginine into the channel pore to render heterotetrameric AMPA receptors calcium-impermeable",
      "AMPA receptors become hyper-permeable to calcium and magnesium",
      "GluA2 subunits are targeted for immediate proteasomal destruction",
      "The channel pore conducts only chloride ions"
    ],
    "answer": 0,
    "explain": "The Q/R site in GluA2 is the most critical A-to-I editing site in the mammalian transcriptome. Unedited GluA2(Q) channels are calcium-permeable and blocked by polyamines. ADAR2 editing to GluA2(R) introduces a positive charge into the pore selectivity filter, rendering mature AMPARs Ca2+-impermeable and protecting neurons from excitotoxicity.",
    "example": "Heterozygous Adar2-null mice fail to edit the Q/R site, developing massive seizures and dying within 3 weeks of birth from unconstrained AMPA calcium influx."
  },
  {
    "level": 5,
    "topic": "Somatic CAG Repeat Expansion Instability in Huntington's",
    "prompt": "Genome-Wide Association Studies of age of onset and progression in Huntington's disease (GeM-HD consortium) revealed that the single most powerful modifiers of clinical onset are genes involved in:",
    "options": [
      "DNA mismatch repair (MMR) pathways, including MSH2, MSH3 (MutSbeta), PMS1, and FAN1, which drive tissue-specific somatic expansion of the CAG repeat in striatal neurons",
      "Dopamine receptor D2 transcriptional promoters",
      "Mitochondrial Complex IV assembly chaperones",
      "Astroglial water channel aquaporin-4 polarization"
    ],
    "answer": 0,
    "explain": "The inherited CAG repeat length (e.g. 42 repeats) is not static: over decades, striatal medium spiny neurons undergo continuous somatic expansion, with repeats lengthening beyond 100 to 500 repeats due to toxic hairpin repair by MutSbeta (MSH2-MSH3). Inactivating MSH3 or overexpressing FAN1 arrests somatic expansion and delays neurodegeneration in mouse models.",
    "example": "Therapeutic development of ASOs and small molecules targeting MSH3 aims to halt somatic CAG expansion to prevent onset in HD mutation carriers."
  },
  {
    "level": 1,
    "topic": "Penetrance vs Expressivity",
    "prompt": "In clinical neurogenetics, if some individuals with a pathogenic dominant mutation show severe symptoms while others with the exact same mutation show mild signs, the condition exhibits:",
    "options": [
      "Variable expressivity",
      "Incomplete penetrance",
      "Genetic anticipation",
      "Heteroplasmy"
    ],
    "answer": 0,
    "explain": "Variable expressivity describes the range of different phenotypic severity or signs among individuals sharing the identical pathogenic genotype. Incomplete penetrance, by contrast, is an all-or-none phenomenon where some gene carriers exhibit no symptoms at all.",
    "example": "Neurofibromatosis type 1 exhibits extreme variable expressivity: within the same family, one member may have only café-au-lait macules while another has disfiguring plexiform neurofibromas."
  },
  {
    "level": 1,
    "topic": "Pleiotropy in Neurodevelopmental Syndromes",
    "prompt": "When a single mutated gene produces multiple distinct, apparently unrelated phenotypic effects across different organ systems, the genetic phenomenon is termed:",
    "options": [
      "Pleiotropy",
      "Epistasis",
      "Codominance",
      "Genetic heterogeneity"
    ],
    "answer": 0,
    "explain": "Pleiotropy occurs when a gene product is utilized in multiple tissues or biochemical cascades, causing a single mutation to produce multi-organ manifestations.",
    "example": "Tuberous sclerosis demonstrates pleiotropy: mutations in TSC1 or TSC2 cause cortical tubers, cardiac rhabdomyomas, renal angiomyolipomas, and facial angiofibromas."
  },
  {
    "level": 1,
    "topic": "Consanguinity and Rare Recessive Disorders",
    "prompt": "Consanguinity (mating between biological relatives) significantly elevates the risk of offspring inheriting:",
    "options": [
      "Rare autosomal recessive disorders, due to increased identity-by-descent (IBD) of shared ancestral alleles",
      "Autosomal dominant disorders",
      "Mitochondrial heteroplasmic mutations",
      "X-linked dominant conditions in males"
    ],
    "answer": 0,
    "explain": "Related parents share a higher proportion of their genome inherited identical-by-descent from common ancestors. This drastically increases the probability that both parents carry the identical rare deleterious recessive allele.",
    "example": "In first-cousin marriages, the coefficient of inbreeding (F = 1/16) results in a substantially increased incidence of rare metabolic neurodegenerative disorders."
  },
  {
    "level": 1,
    "topic": "Uniparental Disomy (UPD)",
    "prompt": "Uniparental disomy (UPD) describes a chromosomal condition where:",
    "options": [
      "An individual inherits two copies of a chromosome from one parent and zero copies from the other parent",
      "Both parental chromosomes are lost during early mitosis",
      "One chromosome is fragmented and reassembled in reverse",
      "A chromosome carries two centromeres"
    ],
    "answer": 0,
    "explain": "UPD occurs typically via 'trisomy rescue' during early embryogenesis. If the involved chromosome contains imprinted genes (such as chromosome 15), UPD results in severe disorders like Angelman or Prader-Willi syndrome.",
    "example": "Maternal uniparental disomy of chromosome 15 (mUPD15) accounts for ~25% of all cases of Prader-Willi syndrome."
  },
  {
    "level": 1,
    "topic": "Centimorgan Definition",
    "prompt": "In genetic linkage analysis, one centimorgan (cM) is defined as the genetic map distance between two loci corresponding to a recombination frequency of:",
    "options": [
      "1% (0.01)",
      "10% (0.10)",
      "0.1% (0.001)",
      "50% (0.50)"
    ],
    "answer": 0,
    "explain": "Named in honor of Thomas Hunt Morgan, one centimorgan represents a 1% chance that two markers on the same chromosome will be separated by a meiotic crossover event. In the human genome, 1 cM corresponds on average to approximately 1 megabase (Mb) of physical DNA.",
    "example": "Markers separated by 5 cM show recombinant genotypes in approximately 5 out of 100 meiotic offspring."
  },
  {
    "level": 1,
    "topic": "Robertsonian Translocation",
    "prompt": "Robertsonian translocations occur exclusively between which class of human chromosomes?",
    "options": [
      "Acrocentric chromosomes (chromosomes 13, 14, 15, 21, and 22)",
      "Metacentric chromosomes 1 and 2",
      "The X and Y sex chromosomes only",
      "Submetacentric chromosomes 4 and 5"
    ],
    "answer": 0,
    "explain": "Robertsonian translocations involve centric fusion of the long arms (q-arms) of two acrocentric chromosomes, with loss of the tiny short arms (p-arms) containing redundant ribosomal RNA genes.",
    "example": "A balanced maternal Robertsonian translocation rob(14;21) confers a high recurrence risk (~10-15%) of Down syndrome in subsequent pregnancies."
  },
  {
    "level": 1,
    "topic": "Hardy-Weinberg Equilibrium Law",
    "prompt": "In population genetics, the Hardy-Weinberg equilibrium equation (p^2 + 2pq + q^2 = 1) allows calculation of carrier frequency (2pq) based on which fundamental assumptions?",
    "options": [
      "Random mating, infinite population size, and absence of mutation, migration, and natural selection",
      "Continuous non-random assortative mating and high selective pressure",
      "Strict maternal inheritance across all generations",
      "Presence of frequent de novo genomic rearrangements"
    ],
    "answer": 0,
    "explain": "Hardy-Weinberg equilibrium describes a stable state where allele and genotype frequencies remain constant across generations in an ideal panmictic, infinitely large diploid population free from evolutionary forces.",
    "example": "If the incidence of spinal muscular atrophy (q^2) is 1 in 10,000, then q = 0.01, and the carrier frequency (2pq) is approximately 2 * 1 * 0.01 = 1 in 50."
  },
  {
    "level": 1,
    "topic": "MicroRNA Seed Sequence Architecture",
    "prompt": "Mature microRNAs (miRNAs) achieve target mRNA recognition and translational repression primarily through base-pairing of their 'seed region', which encompasses nucleotides:",
    "options": [
      "2 through 7 or 8 from the 5' end of the miRNA",
      "15 through 22 at the 3' end of the miRNA",
      "The exact middle 5 nucleotides",
      "The poly-A tail of the passenger strand"
    ],
    "answer": 0,
    "explain": "The seed sequence (nucleotides 2-8 at the 5' end) enters the binding pocket of the Argonaute (AGO) protein in the RISC complex, presenting a pre-helical conformation that binds complementary sites in target mRNA 3' UTRs.",
    "example": "A single point mutation in the seed region of brain-specific miR-96 causes non-syndromic progressive sensorineural hearing loss in humans."
  },
  {
    "level": 2,
    "topic": "Spinocerebellar Ataxia Type 1 Capicua Interaction",
    "prompt": "In Spinocerebellar Ataxia Type 1 (SCA1), the expanded polyglutamine tract in Ataxin-1 causes Purkinje cell neurodegeneration primarily by stabilizing Ataxin-1's interaction with which native transcription factor?",
    "options": [
      "Capicua (CIC), forming an aberrant repressor complex that silences essential cerebellar survival genes",
      "CREB, hyperactivating BDNF transcription",
      "p53, triggering instantaneous somatic necrosis",
      "NF-kappaB, inducing peripheral demyelination"
    ],
    "answer": 0,
    "explain": "Ataxin-1 naturally binds the transcriptional repressor Capicua (CIC). The polyglutamine expansion prevents normal phosphorylation-dependent clearance of Ataxin-1, locking CIC in hyper-stable repressive complexes on cerebellar promoters.",
    "example": "Huda Zoghbi's laboratory showed that knocking down Cic in SCA1 transgenic mice rescues cerebellar pathology and motor coordination."
  },
  {
    "level": 2,
    "topic": "ATXN2 Intermediate PolyQ Repeats and ALS Risk",
    "prompt": "While large CAG repeat expansions (>34 repeats) in ATXN2 cause Spinocerebellar Ataxia Type 2 (SCA2), intermediate-length CAG expansions (27 to 33 repeats) represent a significant genetic risk factor for:",
    "options": [
      "Amyotrophic Lateral Sclerosis (ALS)",
      "Alzheimer's disease",
      "Dravet syndrome",
      "Wilson's disease"
    ],
    "answer": 0,
    "explain": "Aaron Gitler and colleagues discovered that intermediate Ataxin-2 polyQ repeats act as a potent genetic modifier of TDP-43 toxicity, promoting cytoplasmic TDP-43 mislocalization and stress granule persistence in motor neurons.",
    "example": "Antisense oligonucleotides targeting Ataxin-2 reduce TDP-43 aggregation, extend lifespan in ALS mouse models, and have advanced into clinical trials."
  },
  {
    "level": 2,
    "topic": "Spinocerebellar Ataxia Type 7 Retinal Degeneration",
    "prompt": "Spinocerebellar Ataxia Type 7 (SCA7) is clinically unique among the polyglutamine ataxias because progressive cerebellar ataxia is accompanied by:",
    "options": [
      "Severe progressive retinal cone-rod dystrophy leading to bilateral visual loss",
      "Profound sensorineural deafness with intact vision",
      "Peripheral polyneuropathy sparing cranial nerves",
      "Severe cardiac conduction block without motor signs"
    ],
    "answer": 0,
    "explain": "Ataxin-7 is an integral subunit of the STAGA/TFTC histone acetyltransferase coactivator complex. In SCA7, polyQ-expanded Ataxin-7 interferes with CRX (cone-rod homeobox) transcription factor function in photoreceptors, driving cone-rod degeneration alongside Purkinje cell loss.",
    "example": "Visual symptoms (blue-yellow color blindness and central scotomas) often precede cerebellar ataxia in early-onset SCA7 pedigrees."
  },
  {
    "level": 2,
    "topic": "Kennedy's Disease Androgen Receptor PolyQ",
    "prompt": "Spinal and Bulbar Muscular Atrophy (SBMA, Kennedy's disease) is an X-linked motor neuronopathy caused by a CAG repeat expansion in the androgen receptor (AR). Why does the disease manifest only in adult males?",
    "options": [
      "Toxicity requires ligand binding: testosterone causes the mutant androgen receptor to translocate into the nucleus and aggregate, whereas low circulating androgen levels in females prevent nuclear toxicity",
      "The AR gene is completely silenced in females",
      "Females lack spinal motor neurons",
      "Estrogen directly degrades the expanded CAG repeat DNA"
    ],
    "answer": 0,
    "explain": "SBMA pathogenesis is strictly androgen-dependent. In the presence of testosterone, mutant AR dissociates from heat shock proteins, dimerizes, and translocates into the nucleus where it forms toxic aggregates. Symptomatic males develop proximal limb weakness, bulbar dysphagia, muscle fasciculations, and gynecomastia.",
    "example": "Surgical or pharmacological castration (androgen deprivation therapy with leuprorelin) completely rescues motor function and extends survival in male SBMA mice."
  },
  {
    "level": 2,
    "topic": "Canavan Disease ASPA Deficiency and NAA",
    "prompt": "Canavan disease is an autosomal recessive leukodystrophy characterized by macrocephaly, severe hypotonia, and extensive spongy white matter degeneration, caused by deficiency of:",
    "options": [
      "Aspartoacylase (ASPA), leading to massive accumulation of N-acetylaspartate (NAA) in brain and urine",
      "Galactosylceramidase (GALC)",
      "Arylsulfatase A (ARSA)",
      "Hexosaminidase A (HEXA)"
    ],
    "answer": 0,
    "explain": "ASPA hydrolyzes NAA (synthesized in neurons) into acetate and L-aspartate in oligodendrocytes, supplying acetate for myelin lipid synthesis. ASPA deficiency causes NAA buildup, creating osmotic swelling, vacuolization, and dysmyelination.",
    "example": "Proton Magnetic Resonance Spectroscopy (1H-MRS) in an infant with Canavan disease reveals a diagnostic, massively elevated NAA resonance peak at 2.02 ppm."
  },
  {
    "level": 2,
    "topic": "Krabbe Disease Psychosine Toxicity",
    "prompt": "Krabbe disease (globoid cell leukodystrophy) is caused by deficiency of galactosylceramidase (GALC), which results in the toxic accumulation of which neurotoxic metabolite that selectively destroys oligodendrocytes?",
    "options": [
      "Psychosine (galactosylsphingosine)",
      "Glucosylceramide",
      "Sulfatide",
      "Sphingomyelin"
    ],
    "answer": 0,
    "explain": "GALC degrades both galactosylceramide and psychosine. When GALC is defective, galactosylceramide is alternatively metabolized into psychosine, an amphiphilic lysosphingolipid that disrupts lipid rafts, collapses mitochondrial potential, and induces rapid oligodendrocyte apoptosis.",
    "example": "Postmortem histopathology in Krabbe disease reveals severe demyelination with characteristic multinucleated globoid macrophages containing stored galactolipids."
  },
  {
    "level": 2,
    "topic": "Alexander Disease GFAP Mutation Rosenthal Fibers",
    "prompt": "Alexander disease is a rare leukodystrophy caused by dominant de novo gain-of-function mutations in GFAP, which leads pathologically to:",
    "options": [
      "Astrocytic accumulation of eosinophilic, ubiquitinated cytoplasmic inclusions known as Rosenthal fibers containing GFAP and small heat shock proteins",
      "Intranuclear polyglutamine inclusions in cortical pyramidal cells",
      "Extracellular amyloid plaques in the white matter",
      "Selective death of microglial cells throughout the spinal cord"
    ],
    "answer": 0,
    "explain": "GFAP mutations (most commonly R79H or R239H/C) impair normal intermediate filament assembly, causing GFAP to aggregate alongside alphaB-crystallin and HSP27 into dense Rosenthal fibers within astrocyte cytoplasm, inducing non-cell-autonomous myelin loss.",
    "example": "ASO-mediated suppression of GFAP mRNA reverses Rosenthal fiber accumulation and rescues motor phenotypes in Alexander disease animal models."
  },
  {
    "level": 2,
    "topic": "X-Linked Adrenoleukodystrophy ABCD1",
    "prompt": "X-linked Adrenoleukodystrophy (X-ALD), which can present as rapid inflammatory cerebral demyelination in boys (Lorenzo's Oil disease), is caused by mutations in ABCD1 encoding:",
    "options": [
      "A peroxisomal membrane ATP-binding cassette transporter required for importing very-long-chain fatty acids (VLCFAs) into peroxisomes for beta-oxidation",
      "A mitochondrial carnitine palmitoyltransferase",
      "A nuclear steroid hormone receptor",
      "A lysosomal sphingomyelinase"
    ],
    "answer": 0,
    "explain": "Inactivating mutations in ABCD1 prevent peroxisomal import and subsequent beta-oxidation of VLCFAs (particularly hexacosanoic acid, C26:0). Unmetabolized VLCFAs incorporate into myelin lipids and adrenal cortex membranes, causing severe membrane instability and neuroinflammation.",
    "example": "Diagnosis is established by gas chromatography demonstrating elevated plasma hexacosanoic acid (C26:0) and elevated C26:0/C22:0 ratios."
  },
  {
    "level": 2,
    "topic": "Pelizaeus-Merzbacher Disease PLP1 Dosage",
    "prompt": "Pelizaeus-Merzbacher disease (PMD) is an X-linked hypomyelinating leukodystrophy illustrating gene dosage sensitivity, where the most frequent genetic etiology (~60-70% of cases) is:",
    "options": [
      "Genomic duplication of the entire PLP1 (proteolipid protein 1) locus on chromosome Xq22.2",
      "Heterozygous missense mutations in myelin basic protein (MBP)",
      "Complete deletion of the myelin-associated glycoprotein (MAG) gene",
      "Trisomy of chromosome 18"
    ],
    "answer": 0,
    "explain": "PMD is classic dosage-sensitive: PLP1 overexpression caused by tandem genomic duplication triggers oligodendrocyte endoplasmic reticulum stress and unfolded protein response (UPR) apoptosis. Point mutations that misfold PLP1 also cause severe PMD, whereas PLP1 null deletions paradoxically cause a milder paraplegic phenotype (SPG2).",
    "example": "Interphase FISH or chromosomal microarray confirms a tandem interstitial duplication encompassing the PLP1 locus in an infant presenting with pendular nystagmus, stridor, and spastic quadriplegia."
  },
  {
    "level": 2,
    "topic": "PMP22 Duplication vs Deletion (CMT1A vs HNPP)",
    "prompt": "Charcot-Marie-Tooth disease type 1A (CMT1A) and Hereditary Neuropathy with Liability to Pressure Palsies (HNPP) represent classic reciprocal genomic disorders at chromosome 17p12 where:",
    "options": [
      "CMT1A results from a 1.4 Mb tandem duplication containing PMP22 (3 copies), whereas HNPP results from the reciprocal 1.4 Mb deletion (1 copy)",
      "CMT1A is a trinucleotide repeat expansion, while HNPP is an intronic point mutation",
      "CMT1A is mitochondrial, while HNPP is autosomal recessive",
      "CMT1A affects only the central nervous system, while HNPP affects only the autonomic system"
    ],
    "answer": 0,
    "explain": "Flanking low-copy repeats (CMT1A-REPs) mediate non-allelic homologous recombination (NAHR). Unequal crossing-over generates a duplication of PMP22 (causing demyelinating sensorimotor polyneuropathy CMT1A) and a deletion of PMP22 (causing recurrent painless nerve palsies following minor mechanical pressure, HNPP).",
    "example": "Nerve conduction studies in CMT1A show uniformly slowed motor velocities (<38 m/s), whereas HNPP demonstrates focal conduction blocks and 'tomacula' (myelin outfoldings) on nerve biopsy."
  },
  {
    "level": 3,
    "topic": "GABRG2 Mutations in Childhood Absence Epilepsy",
    "prompt": "Familial febrile seizures and childhood absence epilepsy can be caused by heterozygous missense mutations in GABRG2 (such as R43Q) that impair:",
    "options": [
      "The gamma2 subunit of the GABA-A receptor, reducing surface receptor trafficking and disrupting benzodiazepine sensitivity",
      "The glycine receptor pore architecture",
      "The astrocytic GABA transporter GAT-1",
      "The voltage sensor of Nav1.2 channels"
    ],
    "answer": 0,
    "explain": "The gamma2 subunit is essential for targeting GABA-A receptors to the postsynaptic membrane and mediates high-affinity benzodiazepine binding. The R43Q mutation in GABRG2 impairs subunit folding and endoplasmic reticulum exit, reducing synaptic GABAergic inhibition in thalamocortical loops.",
    "example": "Knock-in mice carrying the Gabrg2(R43Q) mutation exhibit spontaneous, ethosuximide-sensitive 3 Hz spike-and-wave discharges on electroencephalography."
  },
  {
    "level": 3,
    "topic": "ADNFLE Nicotinic Receptor Gain of Function",
    "prompt": "Autosomal Dominant Nocturnal Frontal Lobe Epilepsy (ADNFLE) is caused by heterozygous mutations in CHRNA4 or CHRNB2, encoding subunits of the alpha4beta2 nicotinic receptor, which produce:",
    "options": [
      "Gain-of-function hypersensitivity to acetylcholine, causing excessive burst firing of frontal cortical circuits during non-REM sleep",
      "Complete loss of all cholinergic neurotransmission throughout the brainstem",
      "Inhibition of voltage-gated potassium channels",
      "Permanent degradation of choline acetyltransferase"
    ],
    "answer": 0,
    "explain": "Mutations in the M2 pore-lining domain of alpha4 or beta2 nicotinic subunits increase receptor sensitivity to ACh by up to 10-fold and slow desensitization. Normal endogenous nocturnal acetylcholine release during NREM sleep triggers paroxysmal hyperactivation of frontal cortical networks.",
    "example": "Patients experience dramatic hypermotor nocturnal seizures from sleep, which show selective pharmacological response to carbamazepine."
  },
  {
    "level": 3,
    "topic": "DEPDC5 and GATOR1 Complex Focal Epilepsy",
    "prompt": "Familial Focal Epilepsy with Variable Foci (FFEVF) is caused by loss-of-function mutations in DEPDC5, NPRL2, or NPRL3, which form the GATOR1 complex that functions as:",
    "options": [
      "A GTPase-activating protein (GAP) for RagA/B GTPases that negatively regulates amino acid-dependent mTORC1 activation at the lysosomal surface",
      "A core spliceosomal component for small nuclear RNAs",
      "A potassium channel auxiliary subunit",
      "A nuclear transcription factor for dopamine receptors"
    ],
    "answer": 0,
    "explain": "GATOR1 senses amino acid starvation and represses mTORC1. Inactivating DEPDC5 mutations prevent GATOR1 from switching RagA-GTP to RagA-GDP, causing unrestrained mTORC1 signaling that produces focal cortical dysplasias, abnormal neuronal morphology, and focal seizures.",
    "example": "Surgical brain tissue from patients with refractory focal epilepsy due to DEPDC5 mutations demonstrates hypertrophic cytomegalic neurons with hyperphosphorylated S6 (p-S6)."
  },
  {
    "level": 3,
    "topic": "PCDH19 Clustering Epilepsy Paradigm",
    "prompt": "PCDH19-related epilepsy (Early Infantile Epileptic Encephalopathy 9) exhibits a paradoxical inheritance pattern where:",
    "options": [
      "Heterozygous females are severely affected with cluster seizures and intellectual disability, whereas hemizygous transmitting males are completely unaffected, due to cellular interference between mosaic cell populations",
      "Males are lethal at conception, while females are normal",
      "It affects only homozygous males",
      "It is transmitted exclusively through the Y chromosome"
    ],
    "answer": 0,
    "explain": "Protocadherin-19 is an X-linked cell-adhesion molecule. Due to random X-inactivation, heterozygous females possess a mosaic mixture of PCDH19-positive and PCDH19-negative neurons; abnormal communication between these two divergent populations ('cellular interference') disrupts neural circuitry. Hemizygous males have a uniform PCDH19-negative population, avoiding cellular interference and remaining asymptomatic.",
    "example": "Mosaic males with somatic post-zygotic PCDH19 mutations do develop the severe clustering epilepsy syndrome, confirming the cellular interference mechanism."
  },
  {
    "level": 3,
    "topic": "CDKL5 Deficiency Disorder",
    "prompt": "CDKL5 Deficiency Disorder (CDD), formerly considered an atypical early-seizure variant of Rett syndrome, is caused by mutations in the X-linked serine/threonine kinase CDKL5, which phosphorylates:",
    "options": [
      "Shootin-1, Amphiphysin-1, and HDAC4, regulating neuronal morphogenesis, vesicle endocytosis, and dendritic arborization",
      "Beta-amyloid precursor protein at the gamma-secretase cleavage site",
      "Voltage-gated sodium channels in cardiac tissue only",
      "Glucocerebrosidase in the lysosomal lumen"
    ],
    "answer": 0,
    "explain": "CDKL5 is a nuclear and dendritic spine kinase. It phosphorylates shootin-1 (guiding axon outgrowth) and endocytic proteins. Loss of CDKL5 kinase activity disrupts synaptic architecture and spine stability, causing drug-resistant infantile spasms starting in the first months of life.",
    "example": "In 2022, ganaxolone (a neuroactive steroid positive allosteric modulator of GABA-A receptors) received FDA approval specifically for seizures associated with CDKL5 deficiency disorder."
  },
  {
    "level": 3,
    "topic": "PTEN Macrocephaly and Autism",
    "prompt": "Germline loss-of-function mutations in the tumor suppressor PTEN cause PTEN Hamartoma Tumor Syndrome and a syndromic subtype of autism characterized by:",
    "options": [
      "Extreme macrocephaly (>98th percentile, head circumference > +2.5 to +4 SD) driven by hyperactivation of the PI3K-Akt-mTOR pathway",
      "Severe microcephaly with sloping forehead",
      "Congenital insensitivity to pain with anhidrosis",
      "Juvenile-onset parkinsonism without cognitive impairment"
    ],
    "answer": 0,
    "explain": "PTEN is a lipid phosphatase that dephosphorylates PIP3 back into PIP2, antagonizing PI3K. Inactivating PTEN mutations cause constitutive Akt and mTORC1 hyperactivation, stimulating excessive somatic cell growth, neuronal hypertrophy, and megalencephaly with autistic features.",
    "example": "Clinical genetics guidelines recommend PTEN mutation screening in any child presenting with autism spectrum disorder accompanied by prominent macrocephaly."
  },
  {
    "level": 3,
    "topic": "BAF Complex ARID1B Intellectual Disability",
    "prompt": "De novo mutations in ARID1B, encoding a subunit of the SWI/SNF (BAF) chromatin-remodeling complex, represent one of the most common monogenic causes of:",
    "options": [
      "Non-syndromic and syndromic intellectual disability (Coffin-Siris syndrome), through failure of nucleosome repositioning at neurodevelopmental enhancers",
      "Adult-onset frontotemporal dementia",
      "Hereditary spastic paraplegia",
      "Familial hemiplegic migraine"
    ],
    "answer": 0,
    "explain": "The mammalian BAF complex utilizes ATP hydrolysis to slide and evict nucleosomes, rendering regulatory chromatin accessible to transcription factors. ARID1B is an essential DNA-binding subunit; haploinsufficiency disrupts transcriptional programs required for cortical dendritic branching and corpus callosum development.",
    "example": "Patients with ARID1B haploinsufficiency exhibit intellectual disability, expressive speech delay, hypertrichosis, and hypoplastic fifth fingernails (Coffin-Siris syndrome)."
  },
  {
    "level": 3,
    "topic": "Rubinstein-Taybi CREBBP Histone Acetylation",
    "prompt": "Rubinstein-Taybi syndrome (intellectual disability, broad thumbs and great toes, grimacing smile) is caused by heterozygous mutations in CREBBP or EP300, which encode:",
    "options": [
      "Histone acetyltransferases (HATs) that acetylate lysine residues on core histones (e.g. H3K27ac) to relax chromatin and activate gene transcription",
      "Histone deacetylases (HDACs) that compact chromatin",
      "DNA methyltransferases that deposit 5-methylcytosine",
      "ATP-dependent chromatin loop extrusion motors"
    ],
    "answer": 0,
    "explain": "CBP and p300 are homologous transcriptional coactivators with intrinsic HAT activity that catalyze histone acetylation at promoters and enhancers, facilitating CREB-dependent memory consolidation and developmental gene programs. Loss of one allele cripples histone acetylation.",
    "example": "Pharmacological treatment with HDAC inhibitors (such as trichostatin A or suberoylanilide hydroxamic acid) restores histone acetylation and rescues LTP deficits in Crebbp+/- mice."
  },
  {
    "level": 3,
    "topic": "Kabuki Syndrome Epigenetic Machinery",
    "prompt": "Kabuki syndrome (arched eyebrows, long palpebral fissures with eversion of lateral lower eyelids, intellectual disability) is caused by mutations in KMT2D or KDM6A, which coordinately control:",
    "options": [
      "Opening of chromatin: KMT2D is a histone H3K4 methyltransferase (activating mark), while KDM6A is a histone H3K27 demethylase (removing repressive marks)",
      "DNA methylation at telomeres exclusively",
      "Degradation of unfolded proteins in the proteasome",
      "Splicing of the dystrophin pre-mRNA"
    ],
    "answer": 0,
    "explain": "KMT2D (MLL4) deposits monomethyl and dimethyl marks on histone H3 lysine 4 (H3K4me1/2) at enhancers, while X-linked KDM6A (UTX) removes repressive trimethylation from histone H3 lysine 27 (H3K27me3). Both activities promote an open, transcriptionally permissive chromatin state.",
    "example": "Hans Bjornsson's group demonstrated that administering a ketogenic diet or HDAC inhibitors normalizes hippocampal neurogenesis and rescues memory deficits in Kabuki mouse models."
  },
  {
    "level": 3,
    "topic": "Cohesinopathies Cornelia de Lange Syndrome",
    "prompt": "Cornelia de Lange syndrome (CdLS, severe developmental delay, synophrys, hirsutism, upper-limb reduction defects) is caused by mutations in NIPBL, SMC1A, or SMC3, which compose:",
    "options": [
      "The multi-subunit Cohesin ring complex that mediates sister chromatid cohesion and orchestrates 3D chromatin loop extrusion with CTCF",
      "The mitochondrial ribosome large subunit",
      "The nuclear pore complex central channel",
      "The clathrin adaptor complex AP-2"
    ],
    "answer": 0,
    "explain": "NIPBL loads the ring-shaped Cohesin complex onto DNA. Cohesin extrudes chromatin loops until blocked by convergent CTCF boundaries, organizing the genome into topologically associating domains (TADs). In CdLS, defective loop extrusion disrupts enhancer-promoter long-range communication.",
    "example": "Hi-C analysis in NIPBL-deficient neural cells demonstrates widespread attenuation of intra-TAD chromatin loops and dysregulation of developmental gene clusters."
  },
  {
    "level": 3,
    "topic": "Pitt-Hopkins Syndrome TCF4 Transcription Factor",
    "prompt": "Pitt-Hopkins syndrome (severe intellectual disability, episodic hyperventilation followed by apnea, wide mouth with prominent cup-shaped ears) is caused by haploinsufficiency of:",
    "options": [
      "TCF4, encoding a basic helix-loop-helix (bHLH) transcription factor essential for pontine and autonomic respiratory nucleus development",
      "MECP2",
      "FOXP2",
      "UBE3A"
    ],
    "answer": 0,
    "explain": "TCF4 (transcription factor 4, on 18q21.2) heterodimerizes with other bHLH proteins to bind E-box DNA motifs, driving differentiation of neurons in the brainstem, hippocampus, and cortex. Loss of TCF4 causes characteristic paroxysmal hyperventilation-apnea episodes and cognitive arrest.",
    "example": "Tcf4 heterozygous knockout mice display pronounced respiratory irregularity during plethysmography, mimicking the respiratory rhythm defects seen in clinical Pitt-Hopkins patients."
  },
  {
    "level": 4,
    "topic": "7q11.23 Williams vs Duplication Cognitive Dissociation",
    "prompt": "The 7q11.23 copy number variation presents a dramatic double dissociation in cognitive architecture where:",
    "options": [
      "Hemizygous microdeletion (Williams-Beuren syndrome) produces hypersociability, strong verbal fluency, and severe visuospatial impairment, whereas microduplication produces severe expressive speech impairment, social anxiety, and autism",
      "Deletion causes blindness, while duplication causes deafness",
      "Deletion causes pure motor ALS, while duplication causes spinal muscular atrophy",
      "Deletion is completely silent, while duplication causes holoprosencephaly"
    ],
    "answer": 0,
    "explain": "Williams-Beuren deletion (~1.5 Mb, 26-28 genes including GTF2I, LIMK1, ELN) confers a hypersocial 'cocktail party' personality with relatively preserved language syntax but profound dorsal stream visuospatial deficits. Reciprocal 7q11.23 duplication causes the exact inverse: severe expressive language delay and social withdrawal.",
    "example": "Structural MRI shows reduction of the intraparietal sulcus in Williams syndrome, correlating with visuospatial constructive dyspraxia."
  },
  {
    "level": 4,
    "topic": "3q29 Microdeletion Schizophrenia Risk",
    "prompt": "The recurrent 1.6 Mb microdeletion at chromosome 3q29 confers an extraordinary ~40-fold increased risk of developing schizophrenia. Which genes within the interval are implicated in synaptic regulation?",
    "options": [
      "DLG1 (encoding the postsynaptic density scaffolding protein SAP97) and PAK2 (p21-activated kinase)",
      "APP and BACE1",
      "DRD2 and COMT",
      "HTR2A and SLC6A4"
    ],
    "answer": 0,
    "explain": "The 3q29 deletion spans ~22 genes. DLG1/SAP97 binds AMPA and NMDA receptor complexes, while PAK2 regulates actin polymerization in dendritic spines. Loss of these genes impairs cortical glutamatergic synaptic transmission and dendritic spine maintenance.",
    "example": "Human iPSC-derived cortical neurons carrying the 3q29 deletion display reduced spontaneous excitatory postsynaptic currents and defective neurite outgrowth."
  },
  {
    "level": 4,
    "topic": "Smith-Magenis vs Potocki-Lupski RAI1 Dosage",
    "prompt": "Chromosome 17p11.2 reciprocal rearrangements involving RAI1 (Retinoic Acid Induced 1) cause Smith-Magenis syndrome (deletion) and Potocki-Lupski syndrome (duplication), where Smith-Magenis is hallmark characterized by:",
    "options": [
      "Inverted circadian melatonin rhythm (elevated daytime melatonin), sleep disturbances, self-hugging, and polyembolokoilamania (insertion of foreign objects into orifices)",
      "Childhood absence epilepsy responding to ethosuximide",
      "Pure cerebellar ataxia without intellectual disability",
      "Precocious puberty with gigantism"
    ],
    "answer": 0,
    "explain": "RAI1 is a dosage-sensitive transcriptional regulator of circadian rhythm genes (including CLOCK and PER2). Deletion causes daytime melatonin secretion with nighttime drops, driving extreme sleep disruption, daytime behavioral outbursts, and unique stereotypic behaviors.",
    "example": "Treatment of Smith-Magenis patients with daytime beta1-adrenergic antagonists (to block daytime melatonin) and nighttime exogenous melatonin partially realigns the circadian cycle."
  },
  {
    "level": 4,
    "topic": "Splicing QTLs (sQTLs) in Brain Disease",
    "prompt": "Recent large-scale postmortem human brain functional genomic analyses (e.g. PsychENCODE) revealed that disease-associated non-coding GWAS variants are more frequently:",
    "options": [
      "Splicing quantitative trait loci (sQTLs) that alter alternative exon inclusion or splice junction usage, often without changing total overall gene expression levels",
      "Mutations that introduce premature stop codons in every cell",
      "Translocations between telomeric repeats",
      "Variants that alter the genetic code for isoleucine"
    ],
    "answer": 0,
    "explain": "Alternative splicing is extraordinarily complex in human brain neurons. Many GWAS variants create or disrupt splicing regulatory elements (exonic/intronic splicing enhancers or silencers, ESE/ISE), shifting the ratio of protein isoforms without altering total steady-state mRNA abundance.",
    "example": "A common schizophrenia-associated SNP in CLCN3 modulates alternative splicing of exon 2, creating an aberrant chloride channel isoform without altering total CLCN3 transcript levels."
  },
  {
    "level": 4,
    "topic": "Cross-Disorder Psychiatric Genetics PGC Analysis",
    "prompt": "The Psychiatric Genomics Consortium (PGC) cross-disorder meta-analyses evaluated common variant sharing across major psychiatric disorders, demonstrating the highest genetic correlation (r_g ~ 0.70) between:",
    "options": [
      "Schizophrenia and Bipolar Disorder",
      "Schizophrenia and Amyotrophic Lateral Sclerosis",
      "Bipolar Disorder and Parkinson's Disease",
      "Autism Spectrum Disorder and Alzheimer's Disease"
    ],
    "answer": 0,
    "explain": "Cross-disorder LD score regression reveals profound pleiotropy across clinical diagnostic categories. Schizophrenia and bipolar disorder share >70% of their common genetic variant liability, questioning traditional Kraepelinian dichotomies.",
    "example": "Shared risk loci between SCZ and BIP include CACNA1C (L-type calcium channel alpha1C) and ANK3 (ankyrin-G, scaffolding the axon initial segment)."
  },
  {
    "level": 4,
    "topic": "Transcriptome-Wide Association Studies (TWAS)",
    "prompt": "Transcriptome-Wide Association Studies (TWAS, such as PrediXcan or FUSION) identify candidate risk genes from GWAS summary statistics by:",
    "options": [
      "Using reference brain expression panels (e.g. GTEx) to train machine-learning models that predict genetically regulated gene expression (GReX), and testing for correlation between predicted expression and the GWAS phenotype",
      "Sequencing all circular RNAs in patient serum",
      "Performing in situ hybridization on live human subjects",
      "Measuring ribosomal translation speeds in yeast"
    ],
    "answer": 0,
    "explain": "TWAS imputes tissue-specific transcript expression directly into large GWAS cohorts where only genotype data exist, bridging the gap from non-coding SNPs to specific gene targets and direction of effect (upregulated vs downregulated).",
    "example": "TWAS of Alzheimer's disease identified predicted lower expression of CD33 and higher expression of CR1 in myeloid cells as causal drivers of disease susceptibility."
  },
  {
    "level": 5,
    "topic": "Multimodal Single-Cell Profiling (Multiome)",
    "prompt": "Single-nucleus multiome sequencing (such as 10x Multiome or SHARE-seq) advances neurogenetics by simultaneously measuring from the exact same individual nucleus:",
    "options": [
      "Gene expression (snRNA-seq) and chromatin accessibility (snATAC-seq), enabling direct correlation of cis-regulatory element accessibility with target promoter transcription",
      "Nuclear DNA sequence and cytoplasmic protein phosphorylation",
      "Lipid bilayer viscosity and mitochondrial membrane potential",
      "Action potential firing rate and axon diameter"
    ],
    "answer": 0,
    "explain": "Measuring both modalities from identical nuclei resolves ambiguity in computational integration. It enables direct inference of gene-regulatory networks, linking dynamic transcription factor binding motifs at open enhancers to changes in target gene transcript levels.",
    "example": "Applying single-cell multiomics to human corticogenesis identified human-specific accessible enhancers driving outer radial glia proliferation."
  },
  {
    "level": 5,
    "topic": "Human Neocortex Expansion NOTCH2NL Paralog Genes",
    "prompt": "Human-specific evolution of an expanded neocortex is driven in part by the emergence of the human-specific NOTCH2NL paralog genes (on 1q21.1), which function to:",
    "options": [
      "Downregulate differentiation and prolong the self-renewal and expansion phase of radial glial neural stem cells by enhancing Notch signaling",
      "Promote rapid apoptosis of subventricular zone progenitors",
      "Inhibit myelination of all cortical white matter tracts",
      "Block axonal branching in Layer 5 projection neurons"
    ],
    "answer": 0,
    "explain": "NOTCH2NL arose via segmental duplication and gene conversion in the hominin lineage ~3-4 million years ago. NOTCH2NL proteins delay neurogenesis, allowing radial glia to undergo more rounds of proliferative symmetric division, dramatically expanding the cortical progenitor pool.",
    "example": "Ectopic expression of human NOTCH2NL in mouse embryonic cortex expands radial glial cell populations and leads to increased neocortical neuron production."
  },
  {
    "level": 5,
    "topic": "Long-Read Sequencing Brain Transcriptome Complexity",
    "prompt": "Pacific Biosciences Iso-Seq and Oxford Nanopore long-read sequencing technologies have revolutionized neurogenomics by demonstrating that:",
    "options": [
      "Short-read sequencing missed thousands of unannotated, full-length, combinatorial alternative splicing and polyadenylation isoforms in critical brain genes (such as DSCAM, Neurexins, and CACNA1A)",
      "Human brain neurons do not utilize RNA splicing at all",
      "All neuronal mRNAs possess identical 5' and 3' ends",
      "DNA methylation does not exist in mammalian cortical tissue"
    ],
    "answer": 0,
    "explain": "Short reads (~150 bp) cannot resolve which distant alternative exons are spliced together on the same transcript molecule. Full-length long reads (>10 kb) sequence unbroken cDNAs from 5' cap to poly-A tail, uncovering massive combinatoric isoform diversity in synaptic receptors and cell-adhesion molecules.",
    "example": "Long-read sequencing of human cerebral cortex revealed over 30,000 novel transcript isoforms, many containing unannotated microexons enriched in autism risk genes."
  },
  {
    "level": 5,
    "topic": "TANGO ASO-Mediated Synthetic Rescue of SCN1A",
    "prompt": "The targeted augmentation of nuclear gene output (TANGO) antisense oligonucleotide technology rescues haploinsufficiency in Dravet syndrome (STK-001) by:",
    "options": [
      "Binding specifically to a non-productive alternative spliced exon containing a premature stop codon in SCN1A pre-mRNA, forcing exon skipping to redirect splicing toward productive full-length Nav1.1 mRNA",
      "Integrating a new functional SCN1A gene into the host genome via retroviral delivery",
      "Directly binding and opening mutant sodium channel pores",
      "Cleaving all microRNAs that target potassium channels"
    ],
    "answer": 0,
    "explain": "Approximately 10-20% of wild-type SCN1A transcripts undergo alternative splicing to include a 'poison exon' (exon 20N) bearing an in-frame stop codon that triggers nonsense-mediated decay. TANGO ASOs sterically block inclusion of this poison exon, channeling 100% of pre-mRNA from the remaining intact allele into functional, therapeutic Nav1.1 protein.",
    "example": "STK-001 administration in Dravet mouse models doubles functional Nav1.1 protein levels in brain tissue, suppresses electrographic seizures, and prevents SUDEP."
  },
  {
    "level": 5,
    "topic": "Targeted Epigenetic Editing with dCas9-Tet1",
    "prompt": "Unlike classic CRISPR-Cas9 which creates permanent double-strand DNA breaks, catalytically dead Cas9 fused to the catalytic domain of TET1 (dCas9-Tet1) rescues hypermethylated disease genes (such as FMR1 in Fragile X) by:",
    "options": [
      "Directly demethylating 5mC at the expanded CGG repeat and promoter without cutting the DNA backbone, stably reactivating FMRP transcription and restoring synaptic function",
      "Excision of the entire chromosome 21",
      "Inducing widespread random insertions throughout the genome",
      "Transcribing artificial RNA primers into the cytoplasm"
    ],
    "answer": 0,
    "explain": "Jaenisch and colleagues (Cell 2018) directed dCas9-Tet1 with sgRNAs to the methylated FMR1 promoter in Fragile X iPSCs and postmitotic neurons. Targeted demethylation restored normal chromatin architecture (H3K4me3 gain, H3K9me3 loss), sustained persistent FMRP protein re-expression, and rescued electrophysiological hyperactivity.",
    "example": "Fragile X neurons treated with dCas9-Tet1 maintain persistent unmethylated FMR1 status and normal firing rates even after transplantation into mouse brains."
  },
  {
    "level": 1,
    "topic": "Epistasis Definition",
    "prompt": "In neurogenetics, when the phenotypic expression of an allele at one genetic locus is masked or modified by an allele at a completely different locus, the phenomenon is termed:",
    "options": [
      "Epistasis",
      "Incomplete penetrance",
      "Pleiotropy",
      "Heteroplasmy"
    ],
    "answer": 0,
    "explain": "Epistasis refers to inter-genic interactions where the action of one gene (epistatic locus) overrides or alters the phenotype dictated by another gene (hypostatic locus).",
    "example": "Modifier loci in cystic fibrosis and spinal muscular atrophy alter clinical severity through epistatic transcriptional or splicing interactions."
  },
  {
    "level": 1,
    "topic": "Hemizygosity in Human Genetics",
    "prompt": "An individual is described as 'hemizygous' for a genetic locus when:",
    "options": [
      "Only one copy of the gene is present in an otherwise diploid organism, such as genes on the X chromosome in XY males",
      "Both parental alleles carry identical missense mutations",
      "The gene is duplicated tandemly on the same chromosome",
      "The gene is expressed only in mitochondrial DNA"
    ],
    "answer": 0,
    "explain": "Males have one X and one Y chromosome; thus, all genes on the non-pseudoautosomal region of the X chromosome are hemizygous, meaning any recessive mutation will directly manifest phenotypically.",
    "example": "Males carrying a single mutant copy of the X-linked dystrophin gene develop Duchenne muscular dystrophy because they lack a second homologous allele."
  },
  {
    "level": 1,
    "topic": "STRs and Microsatellites in Forensic Neurogenetics",
    "prompt": "Short Tandem Repeats (STRs or microsatellites) are highly polymorphic 2- to 6-base pair repeated DNA sequences widely used in linkage mapping and forensics because:",
    "options": [
      "High replication slippage during DNA synthesis generates high heterozygosity and multiallelic variation across human populations",
      "They code for all known neurotransmitter receptors",
      "They never undergo meiotic recombination",
      "They are found exclusively within ribosomal RNA operons"
    ],
    "answer": 0,
    "explain": "Slippage of DNA polymerase during replication of short tandem repeat motifs leads to frequent insertion or deletion of repeat units, generating extensive polymorphism across individuals.",
    "example": "Capillary electrophoresis sizing of 20 core CODIS STR loci provides unique genetic identity fingerprints in human linkage studies."
  },
  {
    "level": 1,
    "topic": "Synonymous vs Non-Synonymous Mutations",
    "prompt": "A single nucleotide substitution within an exon that alters the codon but does not change the encoded amino acid (due to the degeneracy of the genetic code) is termed a:",
    "options": [
      "Synonymous (silent) mutation",
      "Missense mutation",
      "Nonsense mutation",
      "Frameshift mutation"
    ],
    "answer": 0,
    "explain": "Because multiple codons can encode the same amino acid (wobble hypothesis), synonymous mutations preserve primary peptide sequence, although they can occasionally impact mRNA stability or splicing.",
    "example": "A mutation changing GAG to GAA both code for glutamate, representing a synonymous single nucleotide variant."
  },
  {
    "level": 1,
    "topic": "SNP Minor Allele Frequency Threshold",
    "prompt": "In medical and population genomics, a Single Nucleotide Polymorphism (SNP) is formally distinguished from a rare single nucleotide variant when the minor allele frequency (MAF) in the general population exceeds:",
    "options": [
      "1% (0.01)",
      "10% (0.10)",
      "0.001% (0.00001)",
      "5% (0.05)"
    ],
    "answer": 0,
    "explain": "By convention, common variants present at a frequency greater than or equal to 1% in a population are designated as polymorphisms (SNPs), whereas variants with MAF < 1% are classified as rare variants.",
    "example": "The 1000 Genomes Project cataloged millions of SNPs with MAF > 1% to construct standard imputation reference panels."
  },
  {
    "level": 1,
    "topic": "Triploidy vs Trisomy",
    "prompt": "What is the cytogenetic difference between triploidy and trisomy in humans?",
    "options": [
      "Triploidy involves three complete sets of all 23 chromosomes (69 chromosomes in total), whereas trisomy involves an extra copy of one single chromosome (47 chromosomes)",
      "Trisomy affects all chromosomes, while triploidy affects sex chromosomes only",
      "Triploidy is compatible with normal adult life, while trisomy is always embryonic lethal",
      "There is no cytogenetic difference; the terms are synonymous"
    ],
    "answer": 0,
    "explain": "Triploidy (69,XXX, 69,XXY, or 69,XYY) is a complete extra haploid set resulting from polyspermy or meiotic failure. Trisomy (e.g. trisomy 21) is an aneuploidy involving an extra single chromosome (47 total).",
    "example": "Triploidy is a common finding in early spontaneous miscarriages (~15% of chromosomally abnormal abortuses) and is almost universally lethal in utero."
  },
  {
    "level": 1,
    "topic": "Balanced Reciprocal Translocation",
    "prompt": "A balanced reciprocal chromosomal translocation is characterized by:",
    "options": [
      "An exchange of chromosomal segments between two non-homologous chromosomes without any net gain or loss of genetic material",
      "A fusion of two acrocentric chromosomes with loss of p-arms",
      "The duplication of an entire chromosome arm",
      "The loss of all telomeres on a chromosome"
    ],
    "answer": 0,
    "explain": "In a balanced reciprocal translocation, breaks occur in two different chromosomes and the fragments swap positions. Because total genetic content is preserved, the carrier is typically phenotypically normal, but faces high risks of recurrent miscarriages or offspring with unbalanced rearrangements.",
    "example": "Karyotyping of a parent with multiple recurrent miscarriages frequently identifies a balanced translocation such as t(4;8)(p16;p23)."
  },
  {
    "level": 1,
    "topic": "Sanger Dideoxy Chain-Termination Principle",
    "prompt": "Classic Sanger DNA sequencing halts nascent DNA strand extension specifically because 2',3'-dideoxynucleoside triphosphates (ddNTPs):",
    "options": [
      "Lack the 3'-hydroxyl (-OH) group required for forming the next phosphodiester bond with incoming nucleotides",
      "Degrade the DNA polymerase enzyme",
      "Cleave the template strand at adenine residues",
      "Inhibit helicase unwinding of double-stranded DNA"
    ],
    "answer": 0,
    "explain": "DNA polymerase requires a free 3'-OH group on the growing primer strand to attack the alpha-phosphate of incoming dNTPs. Incorporation of a synthetic ddNTP (lacking the 3'-OH) causes immediate, irreversible chain termination.",
    "example": "Fluorescent dye-terminator Sanger sequencing remains the clinical gold standard for validating diagnostic single nucleotide variants detected by NGS."
  },
  {
    "level": 2,
    "topic": "Dentatorubral-Pallidoluysian Atrophy (DRPLA)",
    "prompt": "Dentatorubral-pallidoluysian atrophy (DRPLA, Haw River syndrome) is a polyglutamine neurodegenerative disorder caused by a CAG repeat expansion in:",
    "options": [
      "ATN1 (encoding atrophin-1)",
      "HTT (huntingtin)",
      "ATXN1 (ataxin-1)",
      "AR (androgen receptor)"
    ],
    "answer": 0,
    "explain": "DRPLA is caused by CAG expansion (>48 repeats) in ATN1 on chromosome 12p13.31. Expanded atrophin-1 forms neuronal intranuclear inclusions, leading to combined degeneration of the dentatorubral and pallidoluysian systems with myoclonus, epilepsy, ataxia, and dementia.",
    "example": "DRPLA exhibits dramatic genetic anticipation, with juvenile-onset cases often expanding by tens of repeats during paternal transmission."
  },
  {
    "level": 2,
    "topic": "Oculopharyngeal Muscular Dystrophy Polyalanine",
    "prompt": "Oculopharyngeal muscular dystrophy (OPMD, progressive ptosis and dysphagia) is molecularly distinct from polyglutamine ataxias because it is caused by:",
    "options": [
      "A small (GCG)6 to (GCG)8-13 triplet repeat expansion in PABPN1 that expands a polyalanine tract from 10 to 11-18 alanines",
      "A large intronic pentanucleotide repeat expansion",
      "A promoter hypermethylation event silencing PABPN1",
      "A frameshift insertion in dystrophin"
    ],
    "answer": 0,
    "explain": "Poly(A) binding protein nuclear 1 (PABPN1) contains an N-terminal polyalanine tract. Expansion beyond 10 alanines causes mutant PABPN1 to misfold into insoluble tubular intranuclear filamentous aggregates in skeletal muscle and pharyngeal fibers.",
    "example": "Muscle biopsy in an elderly adult presenting with bilateral ptosis and swallowing difficulty demonstrates pathognomonic 8.5 nm intranuclear tubulofilamentous inclusions."
  },
  {
    "level": 2,
    "topic": "NGLY1 Congenital Disorder of Deglycosylation",
    "prompt": "NGLY1 deficiency is a rare autosomal recessive congenital disorder of deglycosylation characterized by global developmental delay, movement disorders, and:",
    "options": [
      "Alacrima (absence of tears) and transient transaminase elevations, caused by loss of N-glycanase 1 in cytosolic protein quality control",
      "Extreme tall stature and aortic aneurysms",
      "Profound hypoglycemia responding to galactose",
      "Congenital cataracts without neurological signs"
    ],
    "answer": 0,
    "explain": "NGLY1 cleaves N-glycans from misfolded glycoproteins retro-translocated from the ER during endoplasmic-reticulum-associated degradation (ERAD). NGLY1 loss causes accumulation of misfolded glycoproteins and cripples activation of the transcription factor Nrf1/NFE2L1.",
    "example": "The triad of developmental delay, choreoathetoid movement disorder, and alacrima (crying without tears) is clinically diagnostic for NGLY1 deficiency."
  },
  {
    "level": 2,
    "topic": "Allan-Herndon-Dudley Syndrome MCT8 Transporter",
    "prompt": "Allan-Herndon-Dudley syndrome is an X-linked intellectual disability disorder characterized by severe hypotonia and progressive spastic paraplegia caused by mutations in:",
    "options": [
      "SLC16A2 (MCT8), which encodes the primary thyroid hormone monocarboxylate transporter facilitating T3 entry across the blood-brain barrier",
      "SLC6A1 (GAT1 GABA transporter)",
      "SLC1A2 (GLT-1 glutamate transporter)",
      "SLC2A1 (GLUT1 glucose transporter)"
    ],
    "answer": 0,
    "explain": "MCT8 is essential for transporting active triiodothyronine (T3) across the blood-brain barrier and into developing neurons. Defective MCT8 starves the developing central nervous system of thyroid hormone despite elevated peripheral circulating T3 levels.",
    "example": "Thyroid function tests showing high free T3, low free T4, and normal-to-mildly elevated TSH in a hypotonic male infant establish the diagnosis of MCT8 deficiency."
  },
  {
    "level": 2,
    "topic": "Metachromatic Leukodystrophy Arylsulfatase A",
    "prompt": "Metachromatic Leukodystrophy (MLD) is an autosomal recessive lysosomal storage leukodystrophy caused by deficiency of:",
    "options": [
      "Arylsulfatase A (ARSA), resulting in toxic accumulation of sulfatides (cerebroside 3-sulfate) in oligodendrocytes and Schwann cells",
      "Acid sphingomyelinase",
      "Alpha-galactosidase A",
      "Beta-galactosidase"
    ],
    "answer": 0,
    "explain": "ARSA desulfates sulfatides into galactosylceramide. When inactive, sulfatides accumulate inside lysosomes, forming metachromatic granules that stain brown-gold with cresyl violet, causing central and peripheral demyelination.",
    "example": "Ex-vivo lentiviral hematopoietic stem cell gene therapy (atidarsagene autotemcel, Libmeldy) restores ARSA expression and halts disease progression in pre-symptomatic MLD infants."
  },
  {
    "level": 2,
    "topic": "Tay-Sachs vs Sandhoff HEXA vs HEXB Genetics",
    "prompt": "Both Tay-Sachs and Sandhoff diseases present with identical infantile neurodegeneration and cherry-red macular spots, but they are genetically distinguished because:",
    "options": [
      "Tay-Sachs is caused by mutations in HEXA (alpha subunit, affecting beta-hexosaminidase A only), whereas Sandhoff is caused by mutations in HEXB (beta subunit, affecting both hexosaminidases A and B)",
      "Tay-Sachs is X-linked, while Sandhoff is autosomal dominant",
      "Tay-Sachs affects glycogen storage, while Sandhoff affects cholesterol",
      "Sandhoff affects only adult females, while Tay-Sachs affects male infants"
    ],
    "answer": 0,
    "explain": "Beta-hexosaminidase A is a heterodimer (alpha-beta), while hexosaminidase B is a homodimer (beta-beta). Mutations in HEXA cripple Hex A (accumulating GM2 ganglioside in brain). Mutations in HEXB eliminate both Hex A and Hex B, causing visceral organomegaly alongside brain GM2 accumulation.",
    "example": "Enzyme assays showing absent Hex A with normal Hex B confirm Tay-Sachs, while absent Hex A and Hex B confirm Sandhoff disease."
  },
  {
    "level": 2,
    "topic": "Fabry Disease GLA Deficiency Acroparesthesias",
    "prompt": "Fabry disease is an X-linked lysosomal storage disorder caused by deficient alpha-galactosidase A (GLA), which leads to episodic burning neuropathic pain in the extremities (acroparesthesias) due to accumulation of:",
    "options": [
      "Globotriaosylceramide (Gb3 / GL-3) in dorsal root ganglion neurons and vascular endothelial cells",
      "Glucosylceramide in macrophages",
      "Sphingomyelin in liver and spleen",
      "Phytanic acid in peroxisomes"
    ],
    "answer": 0,
    "explain": "Loss of GLA prevents degradation of neutral glycosphingolipids, trapping Gb3 in vascular endothelial cells and small unmyelinated C-fibers, triggering painful small-fiber neuropathy, hypohidrosis, and premature ischemic strokes.",
    "example": "Enzyme replacement therapy (agalsidase beta) or the pharmacological chaperone migalastat stabilizes mutant GLA and reduces renal and vascular Gb3 deposits."
  },
  {
    "level": 2,
    "topic": "Zellweger Spectrum Peroxisome PEX Mutations",
    "prompt": "Zellweger syndrome, the most severe peroxisome biogenesis disorder, is caused by autosomal recessive mutations in PEX genes (e.g. PEX1, PEX6) that impair:",
    "options": [
      "The import of peroxisomal matrix enzymes carrying PTS1 or PTS2 targeting signals, leading to empty peroxisomal 'ghosts' and severe VLCFA accumulation",
      "Mitochondrial cytochrome c release",
      "Nuclear mRNA export through the nuclear pore",
      "Endosomal sorting of neurotransmitter receptors"
    ],
    "answer": 0,
    "explain": "Peroxisomal biogenesis factor (PEX) proteins assemble the peroxisomal docking and translocation machinery. Inactivating mutations prevent matrix enzymes from entering, causing total failure of peroxisomal beta-oxidation, plasmalogen synthesis, and bile acid conjugation.",
    "example": "Infants present with high forehead, large fontanelles, profound hypotonia, neonatal seizures, and elevated plasma C26:0 very long chain fatty acids."
  },
  {
    "level": 2,
    "topic": "Leber Congenital Amaurosis RPE65 Gene Therapy",
    "prompt": "Leber Congenital Amaurosis type 2 (LCA2), causing severe visual loss in infancy, is caused by biallelic mutations in RPE65, whose normal biochemical role is:",
    "options": [
      "Acting as the all-trans-retinyl ester isomerohydrolase in retinal pigment epithelial cells to regenerate 11-cis-retinal for rhodopsin",
      "Forming the light-sensing photopigment in rod photoreceptors",
      "Transporting vitamin A into the lens",
      "Synthesizing visual cortex myelin"
    ],
    "answer": 0,
    "explain": "RPE65 isomerizes all-trans-retinyl esters into 11-cis-retinol in the visual cycle. Mutations abolish 11-cis-retinal regeneration, depriving photoreceptors of chromophore. In 2017, Voretigene neparvovec (Luxturna, subretinal AAV2-RPE65) became the first FDA-approved in vivo gene therapy.",
    "example": "Subretinal injection of Luxturna in LCA2 patients restores functional vision, enabling navigation through low-light obstacle courses."
  },
  {
    "level": 2,
    "topic": "Stargardt Disease ABCA4 Retinoid Transporter",
    "prompt": "Stargardt disease (juvenile macular degeneration) is caused by autosomal recessive mutations in ABCA4, which functions as:",
    "options": [
      "An ATP-binding cassette flippase in photoreceptor outer segments that translocates N-retinylidene-phosphatidylethanolamine out of the disc lumen, preventing toxic bisretinoid A2E accumulation",
      "A potassium channel in bipolar cells",
      "A structural protein of the optic nerve sheath",
      "An enzyme synthesizing rhodopsin"
    ],
    "answer": 0,
    "explain": "ABCA4 flips retinoid-phospholipid complexes across disc membranes. In its absence, all-trans-retinal reacts with phosphatidylethanolamine to form toxic lipofuscin fluorophores (such as A2E) that poison retinal pigment epithelial cells, causing central macular atrophy.",
    "example": "Fundus autofluorescence in a teenager with progressive central visual loss demonstrates characteristic fleck-like hyperautofluorescent deposits across the posterior pole."
  },
  {
    "level": 2,
    "topic": "Usher Syndrome Ciliopathy Genetics",
    "prompt": "Usher syndrome, the leading cause of combined deaf-blindness, is caused by mutations in genes (such as MYO7A, USH2A, and CDH23) that encode:",
    "options": [
      "Components of the hair cell stereocilia tip-link complex and photoreceptor connecting cilium, essential for sensory mechanotransduction and trafficking",
      "Voltage-gated calcium channels in auditory cortex",
      "Transcription factors regulating cochlear bone density",
      "Neurotransmitters synthesized in the vestibular nucleus"
    ],
    "answer": 0,
    "explain": "Usher proteins form an interconnected network at stereociliary ankle links and tip links in cochlear hair cells and at the periciliary membrane complex of retinal photoreceptors, coordinating actin-based transport and mechanotransduction.",
    "example": "A child presenting with congenital severe sensorineural hearing loss and progressive tunnel vision from retinitis pigmentosa is diagnosed with Usher syndrome type 1 due to MYO7A mutations."
  },
  {
    "level": 3,
    "topic": "SCN1B Auxiliary Beta1 Subunit in GEFS+",
    "prompt": "Generalized Epilepsy with Febrile Seizures plus (GEFS+) can be caused by mutations in SCN1B (such as C121W), which encodes the beta1 auxiliary subunit of voltage-gated sodium channels that:",
    "options": [
      "Modulates Nav channel gating kinetics and functions as an immunoglobulin-superfamily cell adhesion molecule stabilizing channel clustering at nodes and axon initial segments",
      "Pumps sodium out of the mitochondria",
      "Phosphorylates the inactivation gate of potassium channels",
      "Forms the calcium selectivity filter of Cav2.1"
    ],
    "answer": 0,
    "explain": "SCN1B encodes a single-pass transmembrane beta1 subunit containing an extracellular Ig-like fold. The C121W mutation disrupts a conserved disulfide bond, impairing Nav gating modulation and disrupting homophilic cell adhesion at the axon initial segment.",
    "example": "Scn1b-null mice display severe spontaneous seizures, delayed myelination, and ataxia, mimicking severe pediatric Dravet-like channelopathies."
  },
  {
    "level": 3,
    "topic": "GABRA1 Mutation in Juvenile Myoclonic Epilepsy",
    "prompt": "Familial Juvenile Myoclonic Epilepsy (JME) can be caused by missense mutations in GABRA1 (such as A322D in the third transmembrane domain), which causes:",
    "options": [
      "Misfolding, endoplasmic reticulum retention, and severe reduction in surface GABA-A receptor alpha1 expression and inhibitory peak current density",
      "Constitutive ligand-independent opening of chloride channels",
      "Conversion of GABA-A into an excitatory cation channel",
      "Direct proteolytic destruction of presynaptic terminals"
    ],
    "answer": 0,
    "explain": "The A322D mutation introduces a charged aspartate into the hydrophobic M3 transmembrane helix, causing severe misfolding and proteasomal degradation (ER-associated degradation). The resulting loss of surface alpha1beta2gamma2 receptors lowers the seizure threshold in cortical networks.",
    "example": "Heterozygous expression of GABRA1(A322D) in HEK cells causes an >80% reduction in GABA-evoked chloride current compared to wild-type."
  },
  {
    "level": 3,
    "topic": "FOXG1 Syndrome Forebrain Transcription",
    "prompt": "FOXG1 syndrome, a severe neurodevelopmental disorder characterized by severe microcephaly, corpus callosum hypogenesis, and hyperkinetic choreoathetoid movements, is caused by haploinsufficiency of FOXG1, which encodes:",
    "options": [
      "A winged-helix/forkhead transcription factor that establishes telencephalic anterior-posterior patterning and promotes neural progenitor proliferation",
      "A transmembrane potassium leak channel",
      "A lysosomal hydrolase degrading gangliosides",
      "A mitochondrial carrier for pyruvate"
    ],
    "answer": 0,
    "explain": "FOXG1 (Brain Factor 1) is expressed selectively in the embryonic telencephalic neuroepithelium. It represses premature neurogenesis by antagonizing Smad/TGF-beta signaling, ensuring sufficient expansion of cortical progenitors before neuronal differentiation.",
    "example": "Foxg1 knockout mice exhibit catastrophic failure of ventral and dorsal telencephalon development, with near-total absence of cerebral hemispheres."
  },
  {
    "level": 3,
    "topic": "ARX Polyalanine Expansions in Interneuron Migration",
    "prompt": "Mutations in the X-linked aristaless-related homeobox gene (ARX) cause a wide spectrum of disorders where polyalanine tract expansions cause Partington syndrome and nonsyndromic intellectual disability, whereas truncating homeodomain mutations cause:",
    "options": [
      "X-linked lissencephaly with abnormal genitalia (XLAG), characterized by severe failure of tangential GABAergic interneuron migration from the ganglionic eminences",
      "Pure peripheral polyneuropathy without CNS involvement",
      "Spinal muscular atrophy type 3",
      "Congenital insensitivity to pain"
    ],
    "answer": 0,
    "explain": "ARX is essential for the specification and tangential migration of GABAergic interneurons from the medial ganglionic eminence (MGE) to the neocortex. Complete loss-of-function (XLAG) results in almost total depletion of neocortical GABAergic interneurons, causing catastrophic neonatal encephalopathy.",
    "example": "Brain autopsy of XLAG infants reveals a three-layered disorganized lissencephalic cortex devoid of parvalbumin- and somatostatin-positive interneurons."
  },
  {
    "level": 3,
    "topic": "Primary Microcephaly Centrosomal Spindle Genes",
    "prompt": "Autosomal recessive primary microcephaly (MCPH) genes (such as ASPM, WDR62, and MCPH1/microcephalin) encode proteins that localize primarily to which cellular structure?",
    "options": [
      "The centrosome and mitotic spindle poles, regulating spindle orientation and symmetric vs asymmetric division of neural progenitors",
      "The postsynaptic density of dendritic spines",
      "The inner mitochondrial membrane respiratory complexes",
      "The Golgi apparatus trans-face cisternae"
    ],
    "answer": 0,
    "explain": "Radial glial progenitors must maintain exact mitotic spindle alignment perpendicular to the ventricular surface to undergo proliferative symmetric divisions. Mutations in MCPH centrosomal proteins cause spindle misorientation, triggering premature asymmetric division or apoptosis, depleting the progenitor pool and causing microcephaly with a small, normally architectured brain.",
    "example": "ASPM (abnormal spindle-like microcephaly-associated) mutations are the most frequent cause of primary microcephaly, reducing cerebral cortex volume by >60% while sparing cerebellar proportions."
  },
  {
    "level": 3,
    "topic": "Nicolaides-Baraitser SMARCA2 Core ATPase",
    "prompt": "Nicolaides-Baraitser syndrome (intellectual disability, sparse scalp hair, microcephaly, prominent interphalangeal joints) is caused by heterozygous de novo missense mutations in SMARCA2, which acts as:",
    "options": [
      "The catalytic ATPase subunit of the SWI/SNF (BAF) chromatin-remodeling complex, with mutations exerting a dominant-negative effect on ATP hydrolysis",
      "A histone deacetylase that represses synaptic genes",
      "A DNA methyltransferase in the maternal germline",
      "A microRNA export factor"
    ],
    "answer": 0,
    "explain": "SMARCA2 (BRM) hydrolyzes ATP to reposition nucleosomes. Missense mutations specifically cluster in the helicase/ATPase domain, producing an intact BAF complex that binds chromatin but cannot translocate DNA, acting as a potent dominant-negative poison.",
    "example": "Whole-exome sequencing in children with Nicolaides-Baraitser syndrome consistently identifies de novo non-synonymous mutations within the conserved SNF2 helicase domain of SMARCA2."
  },
  {
    "level": 3,
    "topic": "Kleefstra Syndrome EHMT1 Histone Methylation",
    "prompt": "Kleefstra syndrome (intellectual disability, childhood hypotonia, distinctive facial features, autistic behavior) is caused by haploinsufficiency of EHMT1 on 9q34.3, which encodes:",
    "options": [
      "Euchromatic Histone Methyltransferase 1 (GLP), which catalyzes mono- and dimethylation of histone H3 lysine 9 (H3K9me1 and H3K9me2) to repress non-neuronal genes in postmitotic neurons",
      "A histone acetyltransferase activating c-Fos",
      "A deubiquitinating enzyme in dendritic spines",
      "A kinase phosphorylating the tau repeat domain"
    ],
    "answer": 0,
    "explain": "EHMT1 and EHMT2 (G9a) form a heteromeric complex responsible for the majority of euchromatic H3K9 dimethylation, an epigenetic repressive mark that silences pluripotency and inappropriate non-neuronal genes during neuronal maturation. Loss of EHMT1 disrupts homeostatic synaptic plasticity.",
    "example": "Ehmt1 heterozygous mice show deficient novel object recognition and impaired maintenance of hippocampal long-term potentiation."
  },
  {
    "level": 3,
    "topic": "Sotos Syndrome NSD1 H3K36 Methyltransferase",
    "prompt": "Sotos syndrome (cerebral gigantism, advanced bone age, macrodolichocephaly, learning disability) is caused by heterozygous mutations or microdeletions of NSD1 on 5q35, which encodes:",
    "options": [
      "A histone methyltransferase that specifically methylates histone H3 lysine 36 (H3K36me2), coordinating developmental gene expression and cell growth",
      "A ribosomal release factor",
      "An insulin receptor tyrosine kinase",
      "A cyclin-dependent kinase inhibitor"
    ],
    "answer": 0,
    "explain": "NSD1 catalyzes H3K36 dimethylation, an epigenetic modification that prevents spurious intragenic transcription initiation and demarcates active chromatin domains. Haploinsufficiency of NSD1 causes widespread genome hypomethylation, driving excessive prenatal and postnatal somatic growth and macrocephaly.",
    "example": "DNA methylation profiling (epigenetic signature / EpiSign) of blood from individuals with Sotos syndrome identifies a diagnostic genome-wide episignature specific to NSD1 mutations."
  },
  {
    "level": 3,
    "topic": "Weaver Syndrome EZH2 Overgrowth Epigenetics",
    "prompt": "Weaver syndrome, an overgrowth disorder with intellectual disability, macrocephaly, and distinctive facial features, is caused by de novo mutations in EZH2, which functions as:",
    "options": [
      "The catalytic methyltransferase subunit of Polycomb Repressive Complex 2 (PRC2) that trimethylates histone H3 lysine 27 (H3K27me3)",
      "A histone deacetylase associated with MeCP2",
      "A DNA topoisomerase unwinding replication forks",
      "A mitochondrial elongation factor"
    ],
    "answer": 0,
    "explain": "EZH2 uses its SET domain to deposit H3K27me3, an essential repressive chromatin mark orchestrating developmental gene silencing. Mutations in EZH2 in Weaver syndrome perturb PRC2 repressive activity, causing loss of epigenetic restraint over growth and neurodevelopmental pathways.",
    "example": "Distinct blood DNA methylation patterns differentiate Weaver syndrome (EZH2) from the clinically overlapping Sotos syndrome (NSD1)."
  },
  {
    "level": 3,
    "topic": "Coffin-Lowry Syndrome RPS6KA3 / RSK2",
    "prompt": "Coffin-Lowry syndrome, an X-linked disorder characterized by severe intellectual disability, tapering fingers, and stimulus-induced drop episodes (cataplexy-like falls without loss of consciousness), is caused by mutations in:",
    "options": [
      "RPS6KA3 (RSK2), encoding a growth-factor-regulated serine/threonine kinase that phosphorylates CREB, histone H3, and c-Fos",
      "MECP2",
      "CDKL5",
      "DMD"
    ],
    "answer": 0,
    "explain": "RSK2 acts downstream of the Ras-MAPK pathway in response to neurotrophins and synaptic activity. In neurons, RSK2 phosphorylates CREB at Ser133 and histone H3 at Ser10, coupling activity to immediate-early gene transcription. Inactivating mutations severely impair memory and spinal reflex inhibition.",
    "example": "Stimulus-induced drop episodes in Coffin-Lowry patients are triggered by sudden auditory or visual stimuli, responding pharmacologically to clonazepam or SSRIs."
  },
  {
    "level": 3,
    "topic": "Christianson Syndrome SLC9A6 / NHE6",
    "prompt": "Christianson syndrome (an Angelman-like X-linked syndrome with microcephaly, absent speech, ataxia, and seizures) is caused by mutations in SLC9A6, encoding:",
    "options": [
      "NHE6, an endosomal Na+/H+ exchanger that regulates the luminal pH and trafficking of early/recycling endosomes in neurons",
      "A lysosomal cystine transporter",
      "A mitochondrial calcium uniporter",
      "A synaptic vesicle zinc transporter"
    ],
    "answer": 0,
    "explain": "NHE6 extrudes protons from the endosomal lumen in exchange for sodium/potassium, preventing excessive endosomal hyper-acidification. NHE6 loss causes endosomal over-acidification, impairing TrkB neurotrophin receptor recycling and AMPA receptor trafficking, leading to progressive cerebellar atrophy and cognitive deficits.",
    "example": "Slc9a6-null mice show progressive loss of cerebellar Purkinje cells and accumulation of GM2 gangliosides in lysosomal compartments."
  },
  {
    "level": 4,
    "topic": "15q11.2 BP1-BP2 Burnside-Butler Microdeletion",
    "prompt": "The recurrent 15q11.2 microdeletion between breakpoints BP1 and BP2 (~500 kb, spanning TUBGCP5, CYFIP1, NIPA1, NIPA2) acts as a low-penetrance susceptibility locus for:",
    "options": [
      "Dyslexia, autism spectrum disorder, schizophrenia, and ADHD, with CYFIP1 modulating both WAVE-dependent actin remodeling and FMRP translational repression",
      "Severe infantile Tay-Sachs neurodegeneration",
      "Early-onset Alzheimer's disease before age 40",
      "Congenital insensitivity to pain"
    ],
    "answer": 0,
    "explain": "CYFIP1 bridges the FMRP repressor complex and the WAVE regulatory complex (which drives actin polymerization). CYFIP1 haploinsufficiency alters dendritic spine morphology and impairs synaptic protein synthesis, conferring an ~2-fold increase in risk for multiple neurodevelopmental traits.",
    "example": "Mice with heterozygous Cyfip1 deletion exhibit increased immature filopodial spines and altered mGluR-dependent long-term depression."
  },
  {
    "level": 4,
    "topic": "Bivariate LD Score Regression Genetic Covariance",
    "prompt": "Bivariate cross-trait Linkage Disequilibrium Score Regression (bivariate LDSC) estimates the genetic correlation (r_g) between two neurological traits using solely:",
    "options": [
      "GWAS summary statistics (Z-scores) and reference linkage disequilibrium patterns, without requiring individual-level genotype data or shared subjects across cohorts",
      "Whole-genome sequencing of monozygotic twin pairs",
      "Postmortem brain Western blot band intensities",
      "Automated MRI volumetric segmentation measurements"
    ],
    "answer": 0,
    "explain": "By regressing the product of Z-scores from two GWAS against LD scores across SNPs, bivariate LDSC calculates genome-wide genetic covariance free from sample overlap bias, yielding the genetic correlation r_g ranging from -1.0 to +1.0.",
    "example": "Applying cross-trait LDSC demonstrated significant negative genetic correlation (r_g ~ -0.22) between educational attainment and Alzheimer's disease risk."
  },
  {
    "level": 4,
    "topic": "Mendelian Randomization in Neurogenetics",
    "prompt": "Two-sample Mendelian Randomization (MR) evaluates whether an exposure (e.g. circulating inflammatory cytokine levels) causally influences a neurological disease (e.g. Alzheimer's) by:",
    "options": [
      "Using genetic variants strongly associated with the exposure as instrumental variables (IVs) to estimate unconfounded causal effects, leveraging Mendel's law of independent assortment",
      "Treating patients with recombinant cytokines in a clinical trial",
      "Sequencing only the HLA region in affected individuals",
      "Artificially mutating cytokine genes in cell culture"
    ],
    "answer": 0,
    "explain": "Because alleles are randomly assigned at conception, they are free from reverse causation and confounding lifestyle factors, serving as natural randomized trials. Key assumptions: the genetic instrument associates with exposure (relevance), is unconfounded (independence), and affects outcome only via exposure (exclusion restriction).",
    "example": "Mendelian randomization studies showed that genetically predicted higher circulating IL-6 receptor signaling (mimicked by tocilizumab) is causally protective against coronary disease but not Alzheimer's."
  },
  {
    "level": 4,
    "topic": "Sequence Kernel Association Test (SKAT) for Rare Variants",
    "prompt": "In sequencing studies of complex neurological traits, the Sequence Kernel Association Test (SKAT) is superior to simple burden 'collapsing' tests when:",
    "options": [
      "A gene harbors both protective (gain-of-function) and damaging (loss-of-function) rare variants, or many non-causal variants, which cancel each other out in simple burden tests",
      "All variants in the gene have identical effect sizes and same direction of effect",
      "Only common SNPs with MAF > 10% are analyzed",
      "Sample size is smaller than 10 individuals"
    ],
    "answer": 0,
    "explain": "Burden tests sum allele counts, losing power if variants have opposite effect directions. SKAT is a variance-component score test that aggregates variant-level score statistics with flexible weights, retaining robust power regardless of whether rare variants increase or decrease disease risk.",
    "example": "SKAT-O (an optimal combination of burden and SKAT tests) was used in large ALS exome studies to identify NEK1 and KIF5A as bona fide risk genes."
  },
  {
    "level": 4,
    "topic": "Somatic Megabase-Scale Aneuploidies in Cortical Neurons",
    "prompt": "Single-cell whole-genome sequencing of postmortem human cerebral cortex (e.g. McConnell et al., Science 2013) revealed that approximately 10-20% of healthy human cortical neurons harbor:",
    "options": [
      "Large somatic copy number variations (sCNVs) and chromosome-scale aneuploidies (gains or losses >1 Mb) that arose during early embryonic neurogenesis",
      "Total loss of all ribosomal RNA genes",
      "Complete mitochondrial genome duplications",
      "Identical somatic mutations shared across all cells in the brain"
    ],
    "answer": 0,
    "explain": "Neural progenitor cells undergo mitotic chromosome segregation errors during the peak of cortical neurogenesis. As a result, the healthy human brain is a somatic mosaic of cells with distinct large-scale genomic copy number variations that alter individual neuronal transcriptomes.",
    "example": "Single-cell low-pass sequencing demonstrates non-random enrichment of somatic chromosome 1q duplications and 22q deletions in healthy adult prefrontal neurons."
  },
  {
    "level": 5,
    "topic": "Spatial Transcriptomics Sub-Cellular Optical Resolution",
    "prompt": "Next-generation in situ spatial transcriptomics platforms (e.g. 10x Xenium, Vizgen MERSCOPE) achieve superior cellular resolution over first-generation spatial arrays (e.g. 10x Visium) because they:",
    "options": [
      "Use high-magnification optical imaging and multiplexed cyclic fluorescent probing directly on tissue sections to localize individual RNA molecules with sub-micron (~200 nm) resolution inside single cell boundaries",
      "Grind tissue into single-cell suspensions for flow cytometry",
      "Rely on 55-micrometer capture spots that average 5 to 10 neighboring cells together",
      "Capture only mitochondrial ribosomal RNA"
    ],
    "answer": 0,
    "explain": "First-generation spatial arrays (Visium) place tissue over 55 μm capture spots, mixing transcripts from multiple cell types. Optical in situ platforms (Xenium, MERFISH, CosMx) use padlock probes or cyclic single-molecule FISH to optically decode hundreds of RNA targets with 200 nm accuracy, resolving subcellular transcript localization in dendrites and axons.",
    "example": "Applying 10x Xenium to mouse brain slices precisely maps the distinct dendritic localization of Camk2a and Arc transcripts in hippocampal pyramidal layers."
  },
  {
    "level": 5,
    "topic": "ARHGAP11B Human Neocortex Expansion Mechanism",
    "prompt": "The human-specific evolutionary gene ARHGAP11B arose ~5 million years ago and drives neocortical expansion in humans because a single C-to-G splice site mutation created:",
    "options": [
      "A novel 47-amino-acid C-terminal sequence that targets ARHGAP11B protein to the outer mitochondrial membrane, where it closes permeability transition pores to expand basal radial glial progenitors",
      "A GTPase that degrades myelin sheaths in primates",
      "A nuclear transcription factor that represses all potassium channels",
      "A microRNA that silences dystrophin expression"
    ],
    "answer": 0,
    "explain": "Wieland Huttner and colleagues discovered that human-specific ARHGAP11B arose by partial duplication of ARHGAP11A. A single base substitution alters pre-mRNA splicing, creating a unique C-terminus that translocates to mitochondria, elevates glutaminolysis, and triggers massive proliferation of basal radial glia, folding otherwise lissencephalic mouse and marmoset brains.",
    "example": "Transgenic expression of human ARHGAP11B in fetal marmoset brains increases cortical plate thickness and induces neocortical gyrification (folding)."
  },
  {
    "level": 5,
    "topic": "Zika Virus Microcephaly Radial Glia Apoptosis",
    "prompt": "Human cerebral organoid models revealed that congenital Zika virus (ZIKV) infection causes catastrophic microcephaly because the flavivirus selectively infects and destroys:",
    "options": [
      "SOX2-positive ventricular radial glial neural progenitor cells, triggering TLR3 activation, mitotic spindle defects, and p53-dependent apoptosis while arresting neurogenesis",
      "Mature myelinating oligodendrocytes in white matter tracts",
      "Postsynaptic dendritic spines on mature pyramidal neurons",
      "Dura mater fibroblasts exclusively"
    ],
    "answer": 0,
    "explain": "ZIKV binds cell surface receptors (e.g. AXL) on radial glia. Viral replication activates toll-like receptor 3 (TLR3) and p53-dependent cell death pathways, halts progenitor proliferation, and prevents intermediate progenitor generation, collapsing cortical plate expansion.",
    "example": "Inoculation of human brain organoids with ZIKV leads to rapid organoid shrinkage, detachment of apical junctions, and massive apoptosis of SOX2+ progenitors."
  },
  {
    "level": 5,
    "topic": "Engineered Zinc Finger Epigenetic Repressors",
    "prompt": "Engineered Zinc Finger Protein transcriptional repressors (ZFP-KRAB) targeted to the mutant expanded HTT allele in Huntington's disease achieve therapeutic allele-selective silencing by:",
    "options": [
      "Binding specifically to the long expanded CAG repeat tract with high avidity to deposit repressive H3K9me3 marks and recruit KAP1/HP1, silencing transcription of mutant huntingtin while sparing normal alleles with short CAG tracts",
      "Inducing double-strand DNA breaks that trigger translocations",
      "Degrading mature huntingtin protein in the lysosome",
      "Inhibiting all RNA polymerase II transcription across the genome"
    ],
    "answer": 0,
    "explain": "Unlike Cas9 which requires a PAM site, multivalent zinc fingers can be engineered to recognize tandem CAG repeats. Long pathogenic repeats provide multiple contiguous binding sites, enabling high-avidity binding of ZFP-KRAB that selectively heterochromatinizes the expanded HTT allele without cutting genomic DNA.",
    "example": "Striatal AAV delivery of allele-selective ZFP repressors in HD mouse models sustainably reduces mutant huntingtin protein by >75% for over a year without neuroinflammation."
  },
  {
    "level": 5,
    "topic": "Base Editors vs Prime Editors in Post-Mitotic Neurons",
    "prompt": "In therapeutic neurogenetics, Cytidine and Adenine Base Editors (CBE and ABE) are advantageous over traditional CRISPR-Cas9 in post-mitotic adult brain neurons because they:",
    "options": [
      "Mediate precise single base transitions (C-to-T or A-to-G) without creating double-strand breaks (DSBs) or requiring homology-directed repair (HDR), which is inactive in post-mitotic neurons",
      "Can insert entire cDNA transgenes up to 20 kilobases without viral vectors",
      "Cut both DNA strands to generate large deletions in all target genes",
      "Require ultraviolet light irradiation to activate catalysis"
    ],
    "answer": 0,
    "explain": "Homology-directed repair (HDR) operates only during S/G2 phase of dividing cells, rendering classic donor-template CRISPR-Cas9 ineffective in mature neurons. Base editors (Cas9 nickase fused to cytidine deaminase or engineered TadA adenine deaminase) enzymatically alter bases on single-stranded R-loops, enabling high-efficiency correction in quiescent neurons with minimal indel formation.",
    "example": "In vivo AAV delivery of an adenine base editor corrected a pathogenic point mutation in a mouse model of Hutchinson-Gilford progeria, doubling lifespan and rescuing vascular smooth muscle architecture."
  },
  {
    "level": 1,
    "topic": "Alpha-Fetoprotein in Neural Tube Defects",
    "prompt": "During second-trimester prenatal screening, markedly elevated levels of alpha-fetoprotein (MSAFP) in maternal serum and amniotic fluid strongly indicate:",
    "options": [
      "Open neural tube defects (such as myelomeningocele / spina bifida aperta or anencephaly)",
      "Down syndrome (trisomy 21)",
      "Fragile X syndrome",
      "Huntington's chorea"
    ],
    "answer": 0,
    "explain": "Alpha-fetoprotein is a fetal plasma glycoprotein. When the neural tube fails to close completely during embryogenesis (weeks 3-4), fetal serum proteins leak directly into amniotic fluid and cross into the maternal circulation, causing elevated maternal serum AFP.",
    "example": "Periconceptional supplementation with folic acid (400 to 4,000 μg daily) reduces the incidence of open neural tube defects by up to 70%."
  },
  {
    "level": 2,
    "topic": "Charcot-Marie-Tooth Type 1B Myelin Protein Zero",
    "prompt": "Charcot-Marie-Tooth disease type 1B (CMT1B) is an autosomal dominant demyelinating neuropathy caused by mutations in MPZ encoding:",
    "options": [
      "Myelin Protein Zero (P0), the major structural transmembrane adhesion glycoprotein holding compact peripheral myelin lamellae together",
      "Peripheral myelin protein 22 (PMP22)",
      "Connexin-32 (GJB1)",
      "Early growth response 2 (EGR2)"
    ],
    "answer": 0,
    "explain": "Myelin Protein Zero constitutes >50% of total protein in peripheral myelin. Its extracellular immunoglobulin-like domain mediates homophilic adhesion across intraperiod lines. Point mutations in MPZ disrupt compact myelin formation, causing slowed motor conduction and distal muscle atrophy.",
    "example": "Nerve biopsy in CMT1B shows marked hypomyelination and 'onion-bulb' formations resulting from recurrent cycles of Schwann cell demyelination and remyelination."
  },
  {
    "level": 3,
    "topic": "KCNT1 Gain of Function Sleep-Related Epilepsy",
    "prompt": "Severe sleep-related hypermotor epilepsy and epilepsy of infancy with migrating focal seizures (EIMFS) can be caused by de novo gain-of-function mutations in KCNT1 encoding:",
    "options": [
      "The Slack sodium-activated potassium channel, generating massive outward K+ currents that accelerate action potential repolarization and promote burst firing",
      "The Kv1.2 voltage-gated potassium channel",
      "The calcium-permeable AMPA receptor GluA1",
      "The GABA transporter GAT-3"
    ],
    "answer": 0,
    "explain": "KCNT1 encodes the Slack (sequence like a calcium-activated K+ channel) channel gated by intracellular Na+. Gain-of-function mutations increase channel open probability by up to 5- to 10-fold, accelerating spike repolarization and deinactivating Nav channels, which ironically triggers high-frequency burst firing.",
    "example": "The antiarrhythmic drug quinidine acts as an open-channel blocker of KCNT1 and has demonstrated targeted therapeutic efficacy in subsets of KCNT1-mutated patients."
  }
]
