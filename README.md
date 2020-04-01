Notes so far:

CORPUS:
Two corpus used are
1. Reuter's http://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html
2. State of the Union C-Span State of the Union Address Corpus
Both were found on nltk.com, compiled with cat * > {corpus.txt}, and contain not tags.


Currently, we cannot test perplexity using the corpora found online (or their associated filetest.txt files). See below for details.

PRE-PROCESSING:
1. We are converting all uppercase characters to lowercase, in an effort to remove unnecessary vocabulary. While this is not ideal, it is a simple way to preserve basic meanings without compromising too much loss of accuracy.
2. We are removing all punctuation (except periods). Similar to 1, by removing punctuation we simplify the problem tremondously while still retaining meaning.
3. Our corpora do not contain <s> or <\s> characters, as they are not really necessary for our computations. Sentences are bounded by periods.
4. Periods are handled in a very basic way - they are found at the end of words that are at the end of sentences (i.e. the sentence "I love dogs." is tokenized as "I", "love", and "dogs.", including the period). While it is debatable whether this is a good way to handle them, it allows us to a. Not have to do a double parse on each word throughout the vocab And b. Still recognize the weight of periods, as they are now combined with another word in a sort of pseudo-bigram.


TO DO:
1. Sentence Generation.
-  The easiest way (I think) is to build a list of all probabilities associated with the vocab list. Then generate a random number(0-1), and then take steps through the lists of probabilities until that random number is reached (for example, if you have a list of probabilities like ([dog, .3], [man, .2], [cat, .5]), and you generate the number .4, you add .3 to the our steps, see that it is less than our number generated, and then add .2 to the steps, see that it is bigger than our generated number, and thus output it next. There might be a function to do this in a package but I'm guessing not in any that come with python.
2. Perplexity / add-one smoothing support
- Should be easy to implement just didn't have a chance to do it.
3. Model Analysis.
- Perplexity issues; when analyzed without add-1 smoothing, the test set MUST contain only vocabulary of the corpus (otherwise, a divide by zero error will occur). This is trivial for unigrams, but for bigrams, it becomes a little bit trickier. Either we have to find a way around this (i.e. when probability equals zero, set it equal to delta? (the smallest possible number)) or we have to just create a test set that contains only vocabulary our model knows. This is obvioulsy not a problem when the probabilities used in perplexity are calculated using add one smoothing.
- We need to find the top 10 most probable words for each corpus, which shouldn't be too hard; we just need a sorting algorithm on a list of associated probabilites with our vocab(which we need anyway for sentence generation)
