





## 参考文献

1.  In this small evaluation of 13 isolates we found that nanopore long-read-only R10.4.1/kit 14 assemblies with updated basecallers trained using bacterial methylated DNA produce accurate assemblies with **≥40×depth**, sufficient to be cost-effective compared with hybrid ONT/Illumina sequencing in our setting.

[Sanderson N D, Hopkins K M V, Colpus M, et al. Evaluation of the accuracy of bacterial genome reconstruction with Oxford Nanopore R10. 4.1 long-read-only sequencing[J]. Microbial Genomics, 2024, 10(5): 001246.](https://www.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.001246)

2.  It was shown that the **Flye** program demonstrates plausible assembly results relative to others (Shasta, Canu, and Necat). 
The required coverage depth for successful assembly strongly depends on the size of reads. 
When using high-quality samples with an average read length of **8 Kbp or more**, the coverage depth of **30×** is sufficient to assemble the complete genome de novo and reliably determine single-nucleotide variations in it. 
For samples with shorter reads with **mean lengths of 2 Kbp**, a higher coverage depth of **50×** is required. Avoiding of mechanical mixing is obligatory for samples preparation.
Nanopore sequencing can be used alone to determine antibiotics-resistant genetic features of bacterial strains.

[Khrenova M G, Panova T V, Rodin V A, et al. Nanopore sequencing for de novo bacterial genome assembly and search for single-nucleotide polymorphism[J]. International Journal of Molecular Sciences, 2022, 23(15): 8569.](https://www.mdpi.com/1422-0067/23/15/8569)

3.  Polishing of the **Flye** assembly with Illumina paired-end reads restored the genome completeness to a level that is comparable to the hybrid and Illumina-only assemblies. The high percentage of
fragmented genes in long-read-only assembly is usually a result of erroneous frameshifts from indel sequencing errors in the long
reads. Although higher coverage of long read may lead to an increase the consensus accuracy; its accuracy will unlikely match
that of an Illumina-polished assembly due to Nanopore-specific systematic errors. As a result, polishing of long-read assembly
using Illumina short reads can be considered as a cost-effective but less convenient approach for producing highly accurate and contiguous microbial genome assembly.

[Gan HM and Austin CM. Nanopore long reads enable the first complete genome assembly of a Malaysian Vibrio parahaemolyticus isolate bearing the pVa plasmid associated with acute hepatopancreatic necrosis disease [version 1; peer review: 1 approved with reservations, 1 not approved]. F1000Research 2019, 8:2108](https://f1000research.com/articles/8-2108)

4.  Of the filtering, basecalling, and polishing tested, we recommend avoiding using Canu or Raven alone when assembling LR to determine the presence of ARG. Overall, **Flye** is the best assembler we tested for LR assemblies. Guppy basecalling has clearly and consistently improved since its release. As re-basecalling old FAST5 data benefits from these improvements, we wholeheartedly recommend that **FAST5 data from ongoing experiments be saved for re-basecalling**.

[Boostrom I, Portal E A R, Spiller O B, et al. Comparing long-read assemblers to explore the potential of a sustainable low-cost, low-infrastructure approach to sequence antimicrobial resistant bacteria with oxford nanopore sequencing[J]. Frontiers in Microbiology, 2022, 13: 796465.](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.796465/full)
