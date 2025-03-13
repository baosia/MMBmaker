# MMBmaker
Mirror repository for the MMBmaker code included with malkovalab/MMBSearch
The full MMBSearch code can be found at https://github.com/malkovalab/MMBSearch

To cite, please use the following publication: 
https://doi.org/10.1093/nar/gkab685
Osia, B., Alsulaiman, T., Jackson, T., Kramara, J., Oliveira, S., & Malkova, A. (2021). Cancer cells are highly susceptible to accumulation of templated insertions linked to MMBIR. Nucleic acids research, 49(15), 8714-8731.

MMBMaker is a tool to generate MMBIR-like mutations in genomic DNA sequences (i.e., a chromosomal reference genome). 
There are two scripts - 1) to generate insertions only (no deletion of surrounding DNA sequence), and 2) to generate indels (insertions that replace the same amount of DNA sequence). 
Once a reference sequence has been generated with the user-specified number of mutations added, sequencing reads can be generated using artificial read generator software (e.g., ART - Weichun Huang, Leping Li, Jason R Myers, and Gabor T Marth. ART: a next-generation sequencing read simulator, Bioinformatics (2012) 28 (4): 593-594)

