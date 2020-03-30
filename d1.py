import sys
import os

def parseCorpus(corpusFile):
    #Initialize an array for the data
    lines = []
    try:
        #Open the file specified by the user
        with open(corpusFile) as file:
            #Read in each sentence in a 2d array, each row being words and each column being a new sentence
            lines = [line.split() for line in file]
    finally:
        file.close()
    
    #Remove undesired characters
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].strip('\n')
            lines[i][j] = lines[i][j].strip(' ')
    
    #Return the 2d array which will be used as our corpus
    return lines
    

#Function that calculates Max Liklihood Estimation for a unigram
def unigramMLE(unigram, corpus):
    wordCount = 0
    totalCount = 0
    
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            #Increment totalCount for each word in corpus
            totalCount += 1
            if (unigram is corpus[i][j]):
                #Increment wordCount each time the word is found in corpus
                wordCount += 1
    
    unigramProb = wordCount/totalCount
    
    return unigramProb



#Function that returns Max Liklihood Estimation for a bigram
def bigramMLE(bigram):
    return bigram




if __name__ == "__main__":
    #Ask the user for the filename associated with the corpus
    print("Provide the filename, with extension, to the desired corpus.")
    corpusFile = raw_input()
    #Calls upon parseCorpus to extract the words from the corpus
    corpus = parseCorpus(corpusFile)

    print("Type 1 for unigram probability, or type 2 for bigram probability.")
    gramVal = input()
    
    #Directs the program to the unigramMLE calculation
    if (gramVal == 1):
        print("Enter the unigram of your choice.")
        #Take the unigram from the user
        unigram = raw_input()
        #Strip it of the newline character
        unigram = unigram.strip()
        
        #Call on unigramMLE function
        unigramProb = unigramMLE(unigram, corpus)
        print 'The unsmoothed unigram probability estimate is', unigramProb
    
    #Directs the program to the bigramMLE calculation
    elif (gramVal == 2):
        print("Enter the bigram of your choice.")
        #Take the bigram from the user
        bigram = raw_input('\n')
        #Strip it of the newline character
        bigram = bigram.strip('\n')
        
        #Call on bigramMLE function
        bigramProb = bigramMLE(bigram, corpus)
        print 'The unsmoothed bigram probability estimate is', bigramProb
     
    
    #Error handling for incorrect user input
    else:
        print("User input not recognized.")
