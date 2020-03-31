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

def vocabLength(corpus):
    model = []
    vocabCount = 0
    #Create list of all unigrams
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            tempWord = corpus[i][j]
            inModel = False
            #check that our model isn't empty so it doesn't go out of bounds
            if model:
                for k in range(len(model)):
                    if (tempWord == model[k][0]):
                        inModel = True
            #If our word isn't in our model yet, add one to the vocab count and append the new word
            if not inModel:
                vocabCount += 1
                model.append(tempWord)
    return vocabCount
    
    

#Function that calculates Max Liklihood Estimation for a unigram
def unigramMLE(unigram, corpus, smoothVal, vocabLength):
    wordCount = 0
    totalCount = 0
    
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            #Increment totalCount for each word in corpus
            totalCount += 1
            if (unigram == corpus[i][j]):
                #Increment wordCount each time the word is found in corpus
                wordCount += 1
    
    #Unsmoothed probability
    if (smoothVal == 1):
        unigramProb = wordCount/totalCount

    #Add-one smoothing is applied
    elif (smoothVal == 2):
        unigramProb = (wordCount + 1) / (totalCount + vocabLength)
        
    #Error handling for incorrect input
    else:
        print("Smoothing option not recognized. Returning a probability of zero.")
        unigramProb = 0
    
    #Return the probability
    return unigramProb

#Function to build our model with probabilities of each unigram
def unigramModel(corpus, smoothVal, vocabLength):
    model = []
    #First, go through and build a list of our possible unigrams
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            tempWord = corpus[i][j]
            inModel = False
            #check that our model isn't empty so it doesn't go out of bounds
            if model:
                for k in range(len(model)):
                    if (tempWord == model[k][0]):
                        inModel = True
            #If our word isn't in our model yet, we can first calculate it's MLE and then add it
            if not inModel:
                tempProb = unigramMLE(tempWord, corpus, smoothVal, vocabLength)
                model.append((tempWord, tempProb))
    return model
                
                    
            
#Function that calculate MLE for a bigram
def bigramMLE(bigram, corpus, smoothVal, vocabLength):
    phraseCount = 0
    totalCount = 0
    
    for i in range(len(corpus)):
        for j in (range(len(corpus[i])-1)):
            #Increment totalcount for each two word phrase in corpus
            totalCount += 1
            if(bigram == (' '.join([corpus[i][j], corpus[i][j+1]]))):
                #Increment phraseCount each time the phrase is found in corpus
                phraseCount += 1
                
    #Unsmoothed probability
    if (smoothVal == 1):
        bigramProb = phraseCount / totalCount

    #Add-one smoothing is applied
    elif (smoothVal == 2):
        bigramProb = (phraseCount + 1) / (totalCount + vocabLength)
        
    #Error handling for incorrect input
    else:
        print("Smoothing option not recognized. Returning a probability of zero.")
        bigramProb = 0
    
    #Return the probability
    return bigramProb

#Function to build our model with probabilities of each bigram
def bigramModel(corpus, smoothVal, vocabLength):
    model = []
    #First, go through and build a list of our possible bigrams
    for i in range(len(corpus)):
        for j in range(len(corpus[i])-1):
            tempPhrase = ' '.join([corpus[i][j], corpus[i][j+1]])
            inModel = False
            #check that our model isn't empty so it doesn't go out of bounds
            if model:
                for k in range(len(model)):
                    if (tempPhrase == model[k][0]):
                        inModel = True
            #If our word isn't in our model yet, we can first calculate it's MLE and then add it
            if not inModel:
                tempProb = bigramMLE(tempPhrase, corpus, smoothVal, vocabLength)
                model.append((tempPhrase, tempProb))
    return model





if __name__ == "__main__":
    #Ask the user for the filename associated with the corpus
    print('Provide the filename, with extension, to the desired corpus.')
    corpusFile = input()
    #Calls upon parseCorpus to extract the words from the corpus
    corpus = parseCorpus(corpusFile)
    #print(corpus)
    
    #Find vocabulary size
    vocabSize = vocabLength(corpus)
    
    #Ask user if they would like to use a unigram or a bigram
    print('Type 1 for unigram probability, or type 2 for bigram probability.')
    gramVal = input()
    
    #Ask the user if they would like to use unsmoothed or smoothed probability
    print('Type 1 for unsmoothed probability, or type 2 for add-1 smoothing.')
    smoothVal = int(input())
    
    #Create a model for unigrams and bigrams
    uniModel = unigramModel(corpus, smoothVal, vocabSize)
    biModel = bigramModel(corpus, smoothVal, vocabSize)
    
    #Directs the program to the unigramMLE calculation
    if (gramVal == '1'):
        print('Enter the unigram of your choice.')
        #Take the unigram from the user
        unigram = input()
        #Strip it of the newline character
        unigram = unigram.strip()

        #Call on unigramMLE function
        unigramProb = unigramMLE(unigram, corpus, smoothVal, vocabSize)
        print ('The unigram probability estimate is', unigramProb)

    #Directs the program to the bigramMLE calculation
    elif (gramVal == '2'):
        print('Enter the bigram of your choice.')
        #Take the bigram from the user
        bigram = input()
        #Strip it of the newline character
        bigram = bigram.strip('\n')

        #Call on bigramMLE function
        bigramProb = bigramMLE(bigram, corpus, smoothVal, vocabSize)
        print ('The bigram probability estimate is', bigramProb)


    #Error handling for incorrect user input
    else:
        print('User input not recognized.')
