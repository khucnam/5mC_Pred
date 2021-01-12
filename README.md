This is the public site for the paper under submission named: "An extensive examination of discovering 5-Methylcytosine Sites in Genome-Wide DNA Promoters using machine learning based approaches" which has been accepted for presentation at the 19th Asia Pacific Bioinformatics Conference as a research article.

In this repo, we provide users with a standalone application for predicting 5mC sites in DNA Genome-wide promoters. 

In order to use our tool, first, please pay attention to the library requirements specified below:
	
	* LIBRARY REQUIREMENTS
	
		We will need to install some basic packages to run the programs as followed:
		
			+ git version 2.15.1.windows.2
			
			+ python 3.6.5
			
			+ numpy 1.14.3
			
			+ pandas 0.23.0
			
			+ sklearn 0.20.2
			
Then, in order to execute the prediction, please:

	1. Using git bash to clone the repository content from https://github.com/khucnam/5mC_Pred

	2. Execute the prediction command with the following syntax:
		
		python Predict.py <threshold> <path/to/seg/file>  

		+ <threshold>: threshold value to convert a predicted probability into a result (5mC site or non_5mC site) 
		+ <path/to/fasta/file>: path to fasta file contains the promoter segments of which the 5mc sites you want to identify. Please see the "sample.seg" as an example
		
	3. Open the "Result.txt" file in the same folder to see the prediction results.

We hope that our tool is helpful for you in predicting 5mC sites in DNA Genome-wide promoters! Thanks for interesting in our paper! 
All the questions can be send to nguyentrinhtrungduong@gmail.com.


