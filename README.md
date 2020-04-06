Notes so far:

CORPUS:
Two corpus used are
1. Reuter's http://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html
2. State of the Union C-Span State of the Union Address Corpus
Both were found on nltk.com, compiled with cat * > {corpus.txt}, and contain not tags.

PRE-PROCESSING:
1. We are converting all uppercase characters to lowercase, in an effort to remove unnecessary vocabulary. While this is not ideal, it is a simple way to preserve basic meanings without compromising too much loss of accuracy.
2. We are removing all punctuation (except periods). Similar to 1, by removing punctuation we simplify the problem tremondously while still retaining meaning.
3. Our corpora do not contain <s> or <\s> characters, as they are not really necessary for our computations. Sentences are bounded by periods.
4. Periods are handled in a very basic way - they are found at the end of words that are at the end of sentences (i.e. the sentence "I love dogs." is tokenized as "I", "love", and "dogs.", including the period). While it is debatable whether this is a good way to handle them, it allows us to a. Not have to do a double parse on each word throughout the vocab And b. Still recognize the weight of periods, as they are now combined with another word in a sort of pseudo-bigram.

PERPLEXITY:
Perplexity is calculated with the standard formula, and always with add-one smoothing.
