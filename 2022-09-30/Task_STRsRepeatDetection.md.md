# Task 1
## STR background reading
- Why is STR variation relevant to health and disease?
> Short tandem repeats (STRs) are some of the fastest mutating loci in the genome. Recent studies have leveraged these catalogs to show that STRs play a widespread role in regulating gene expression and other molecular phenotypes. These analyses suggest that STRs are an underappreciated but rich reservoir of variation that likely make significant contributions to Mendelian diseases, complex traits, and cancer. <br>
- What are some of the challenges in analysing STRs from NGS data?
> STRs are challenging to genotype from NGS. First, short reads often do not span entire repeats, effectively reducing the number of informative reads. Second, STR variations present as large insertions or deletions that may be difficult to align to a reference genome, and thus introduce significant mapping bias toward shorter alleles. Finally, PCR amplification during library preparation often introduces “stutter” noise in the number of repeats at STRs.

<br>

-------

<br>

# Task 2
## Introduction to TRAL
- Why should you use multiple tandem repeat detection algorithms to look for repeats in biological sequence?
> To know the location of STRs in the reference genome for further genotyping STRs e.g., in GangSTR.
- What different functionalities does TRAL provide?
> Annotate with sequence profile models <br>
Annotate with *de novo* tandem repeat detectors <br>
Identify and filter overlapping annotations <br>
Test and filter for statistical significance <br>
Retrieve tandem repeat characteristics <br>
Performance evaluation
