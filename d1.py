import sys
import os
import math
import random
import operator

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
            lines[i][j] = lines[i][j].lower()
            lines[i][j] = lines[i][j].strip('\n')
            lines[i][j] = lines[i][j].strip(')')
            lines[i][j] = lines[i][j].strip('(')
            lines[i][j] = lines[i][j].strip(':')
            lines[i][j] = lines[i][j].strip(';')
            lines[i][j] = lines[i][j].strip(' ')
            lines[i][j] = lines[i][j].strip('\"')
            lines[i][j] = lines[i][j].strip('\'')
    
    #Return the 2d array which will be used as our corpus
    return lines

def uniVocab(corpus):
    vocab = []
    
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            if corpus[i][j] not in vocab:
                vocab.append(corpus[i][j])
    
    #Return the list of unique words
    return vocab
    
def biVocab(corpus):
    #Initialize the list
    vocab = []
    
    #Parse through the corpus, adding any unique phrases to the vocab
    for i in range(len(corpus)):
        for j in range(len(corpus[i]) - 1):
            if (' '.join([corpus[i][j], corpus[i][j+1]]) not in vocab):
                vocab.append(' '.join([corpus[i][j], corpus[i][j+1]]))
    
    #Return the list of unique phrases
    return vocab
    
    

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

#Calculate perplexity of given testset using unigram model
def uniPerplexity(uniModel, testset, corpus, vocabSize):
    probabilities = []
    parsedTest = parseCorpus(testset)
    for row in range(len(parsedTest)):
        for word in range(len(parsedTest[row])):
            #Use smoothed probability to ensure no divide by zero
            probabilities.append(unigramMLE(parsedTest[row][word], corpus, 2, vocabSize))
    pp = 1
    
    for probability in probabilities:
        pp += math.log(probability, 2)
    
    pp = (1 / len(probabilities)) * pp
    pp = math.pow(1/2, pp)
    
    return pp
        
        

def biPerplexity(biModel, testset, corpus, vocabSize):
    probabilities = []
    parsedTest = parseCorpus(testset)
    #print(parsedTest)
    for row in range(len(parsedTest)):
        for word in range(len(parsedTest[row])-1):
            #print(word)
            #print(row)
            #Use smoothed probability to ensure no divide by zero
            probabilities.append(bigramMLE(' '.join([parsedTest[row][word], parsedTest[row][word+1]]), corpus, 2, vocabSize))
    pp = 1
    
    for probability in probabilities:
        pp += math.log(probability, 2)
    
    pp = (1 / (len(probabilities) + 1)) * pp
    pp = math.pow(1/2, pp)
    
    return pp
    
    
def topUnigrams(corpus, unigramVocab):
    probabilities = []
    mostLikely = []
    list = []
    topTen = []
    
    #Create a list of tuples containing unique unigrams and their probabilities
    for i in range(len(unigramVocab)):
        tup = (unigramMLE(unigramVocab[i], corpus, 1, 0), unigramVocab[i])
        list.append(tup)

    #Sort this list in descending order by their probabilities
    list.sort(key = operator.itemgetter(0), reverse = True)
    
    #Place the words in order of probability into mostLikely[]
    mostLikely = [j[1] for j in list]
    
    for i in range(10):
        topTen.append(mostLikely[i])
    
    #Return the top 10 words
    return topTen
    
    
def topBigrams(corpus, bigramVocab):
    probabilities = []
    mostLikely = []
    list = []
    topTen = []
    
    #Create a list of tuples containing unique bigrams and their probabilities
    for i in range(len(bigramVocab)):
        tup = (bigramMLE(bigramVocab[i], corpus, 1, 0), bigramVocab[i])
        list.append(tup)

    #Sort this list in descending order by their probabilities
    list.sort(key = operator.itemgetter(0), reverse = True)
    
    #Place the phrases in order of probability into mostLikely[]
    mostLikely = [j[1] for j in list]
    
    for i in range(10):
        topTen.append(mostLikely[i])
    
    #Return the top 10 phrases
    return topTen
    
    
def generateSentences(corpus, topUnigrams, unigramVocab):
    probabilities
    #For each new sentence:
        #Select a likely first word as "word"
        #Print the word
        #While the sentence has not finished:
            #For each unique unigram:
                #Create tuples of next words and their probabilities, probabilities found with bigramMLE(' '.join([word, unigramVocab[i]]), corpus, 1, 0)
            #Find the highest probability word and print it
            #Change variable "word" to this highest prob word
            #Check if sentence ahs ended
    
    return


if __name__ == "__main__":
    #Ask the user for the filename associated with the corpus
    print('Provide the filename, with extension, to the desired corpus.')
    corpusFile = input()
    #Calls upon parseCorpus to extract the words from the corpus
    corpus = parseCorpus(corpusFile)
    print("parsed corpus")
    
    #Find vocabulary size
    unigramVocab = uniVocab(corpus)
    print("unigram model created")
    bigramVocab = biVocab(corpus)
    print("bigram model created")
    #Use these vocabularies to generate values for V
    uniVocabSize = len(unigramVocab)
    biVocabSize = len(bigramVocab)
    print("Perplexity of testset using unigram model is:", uniPerplexity(unigramVocab, "corpustest.txt", corpus, uniVocabSize))
    print("Perplexity of testset using bigram model is:", biPerplexity(bigramVocab, "corpustest.txt", corpus, biVocabSize))
    
    #Calculate highest probability unigrams and bigrams, then print the top 10 for each
    topUnigrams = topUnigrams(corpus, unigramVocab)
    topBigrams = topBigrams(corpus, bigramVocab)
    print("The ten most likely words in this corpus are: ", topUnigrams)
    print("The ten most likely phrases in this corpus are: ", topBigrams)

    
    answer = "Y"
    while(answer != "N"):
        #Ask user if they would like to use a unigram or a bigram
        print('Type 1 for unigram probability, or type 2 for bigram probability.')
        gramVal = input()
        
        #Ask the user if they would like to use unsmoothed or smoothed probability
        print('Type 1 for unsmoothed probability, or type 2 for add-1 smoothing.')
        smoothVal = int(input())

        #Directs the program to the unigramMLE calculation
        if (gramVal == '1'):
            print('Enter the unigram of your choice.')
            #Take the unigram from the user
            unigram = input()
            #Strip it of the newline character
            unigram = unigram.strip()

            #Call on unigramMLE function
            unigramProb = unigramMLE(unigram, corpus, smoothVal, uniVocabSize)
            print ('The unigram probability estimate is', unigramProb)

        #Directs the program to the bigramMLE calculation
        elif (gramVal == '2'):
            print('Enter the bigram of your choice.')
            #Take the bigram from the user
            bigram = input()
            #Strip it of the newline character
            bigram = bigram.strip('\n')

            #Call on bigramMLE function
            bigramProb = bigramMLE(bigram, corpus, smoothVal, biVocabSize)
            print ('The bigram probability estimate is', bigramProb)


        #Error handling for incorrect user input
        else:
            print('User input not recognized.')
            
        #Ask the user if they would like to generate sentences
        print('Would you like to generate sentences using these probability estimates? Type "Y" for yes, or "N" for no.')
        sentenceChoice = input()
           
        if (sentenceChoice == 'Y'):
            #Randomly generate high probability sentences from the models we created
            generateSentences(corpus, topUnigrams, unigramVocab)
        
           
            
        answer = input("Do you want to keep going with the current corpus? Write \"N\" if no, or simply press enter to continue.")
        
        
