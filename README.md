# Nanopore micro genome assembly

![nanopore](./Nanopore.png)

## Raw Data

The most original/raw data are .fast5 files (earlier versions are multi-FAST5, where each read is stored in a separate HDF5 file), which contain:

<ol>
<li>fast5（HDF5 格式）传统的数据保存方式（一直用到 2023 年左右）:</li>

    fast5/
     ├─ FAK12345_pass_0001.fast5
     ├─ FAK12345_pass_0002.fast5
     └─ ...
     分为：single-read FAST5 与 multi-read FAST5
     

<li>pod5（新版）</li>

    Pod5 是为减少数据冗余和适应高速数据处理而设计的新数据结构，按 read 划分。
    一样包括 raw signals，但是文件大小更紧凑，适合高速 I/O

</ol>

## FAST52pod5

微生物基因组拼接的起点一般是fastq或者未比对的BAM

FAST5:

*single-read FAST5--->multi-read FAST5*

ont_fast5_api:https://github.com/nanoporetech/ont_fast5_api<br>

<pre>
pip3 install ont-fast5-api
single_to_multi_fast5 --input_path /data/reads --save_path /data/multi_reads --filename_base batch_output --batch_size 100 --recursive
</pre>
        
*multi-read FAST5--->pod5*

POD5 File Format:https://pod5-file-format.readthedocs.io/<br>
<pre>
pip3 install pod5
pod5 convert fast5 ./input/*.fast5 --output converted.pod5
</pre>

## Docker

<pre>docker pull fanyucai1/nanopore_micro</pre>

*software list:*

**/opt/conda/envs/python3/bin:**

    NanoPlot filtlong flye pod5 ont-fast5-api

**/opt/conda/envs/biosoftware/bin:**

    medaka prokka resfinder seqsero2 fastcat mlst mosdepth pomoxis

## models

<pre>docker run fanyucai1/nanopore_micro /software/dorado-1.0.2-linux-x64/bin/dorado download --list</pre>

<pre>
dna_r9.4.1_e8.1_sup@v4.0.0
│   │    │     │     │
│   │    │     │     └── 模型版本号
│   │    │     └──────── 模型类型（fast速度快, hac平衡速度与准确度，满足大部分情况, sup准确度高）
│   │    └────────────── flow cell 化学版本（E8.1）
│   └─────────────────── 测序芯片（如 R9.4.1, R10.4.1）
└────────────────────── 模型用途（dna, rna）
</pre>

## details

**step1:base calling**(dorado:https://github.com/nanoporetech/dorado)

    dorado basecaller hac pod5s/ > calls.bam    

**step2:Sequencing Output Statistics**NanoPlot:https://github.com/wdecoster/NanoPlot

**step3:quality control**(Filtlong:https://github.com/rrwick/Filtlong)

    filtlong --min_length 1000 --keep_percent 90 --target_bases 500000000 input.fastq.gz | gzip > output.fastq.gz

**step4:genome assembly**(Flye:https://github.com/mikolmogorov/Flye)

**step5:correct draft sequences,variant calling and stats.**(Medaka:https://github.com/nanoporetech/medaka and bcftools:https://github.com/samtools/bcftools)

https://github.com/epi2me-labs/wf-bacterial-genomes/blob/master/modules/local/medaka.nf

**step6:annotation (Prokka:https://github.com/tseemann/prokka)**

**step7:Multi-locus sequence typing (MLST:https://github.com/tseemann/mlst)**

**step8:Antimicrobial resistance (AMR) calling(ResFinder:https://bitbucket.org/genomicepidemiology/resfinder/src/master/)**

**step9:Salmonella serotyping(SeqSero2:https://github.com/denglab/SeqSero2)**

## Reference

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

5.  **Trycycler：https://github.com/rrwick/Trycycler** is a tool for generating consensus long-read assemblies for bacterial genomes. I.e. if you have multiple long-read assemblies for the same isolate, Trycycler can combine them into a single assembly that is better than any of your inputs.

    [Wick R R, Judd L M, Cerdeira L T, et al. Trycycler: consensus long-read assemblies for bacterial genomes[J]. Genome biology, 2021, 22: 1-17.](https://github.com/rrwick/Trycycler)

## Links:

Assembling the perfect bacterial genome:https://github.com/rrwick/Perfect-bacterial-genome-tutorial/wiki

Bacterial assembly and annotation workflow:https://github.com/epi2me-labs/wf-bacterial-genomes/

[Wick R R, Judd L M, Holt K E. Assembling the perfect bacterial genome using Oxford Nanopore and Illumina sequencing[J]. PLOS Computational Biology, 2023, 19(3): e1010905.](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010905)