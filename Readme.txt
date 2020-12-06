Computing the bigram model (counts and probabilities) on the given corpus


1. Open CommandPrompt and run the python file - "NLP_Homework_2.py" along with the below arguments. (Place the corpus file in the same folder)
2. Arguments are : 
	Corpus training data : NLP6320_POSTaggedTrainingSet-Windows.txt
	Any input sentence : "My company turnover is 7 million $"
	Smoothing Type : No Smoothing - 1
			 Add-one Smoothing - 2
		         Good-Turing Discounting based Smoothing - 3

For Example: 

For "No Smoothing" type:

python NLP_Homework_2.py NLP6320_POSTaggedTrainingSet-Windows.txt "My company turnover is 7 million $" 1

For "Add-one Smoothing" type:

python NLP_Homework_2.py NLP6320_POSTaggedTrainingSet-Windows.txt "My company turnover is 7 million $" 2

For "Good-Turing Discounting based Smoothing" type:

python NLP_Homework_2.py NLP6320_POSTaggedTrainingSet-Windows.txt "My company turnover is 7 million $" 3
