import pandas as pd
 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from collections import Counter

def unique_words(data):
    text = ' '.join(data)
    review_word = text.split(' ')
    all_reviews = ' '.join(review_word)
    words = all_reviews.split()

    # words wrong datatype
    counts = Counter(words)
    vocab = sorted(counts, key=counts.get, reverse=True)
    vocab_to_int = {word: ii for ii, word in enumerate(vocab, 1)}

    reviews_ints = []
    for review in review_word:
        reviews_ints.append([vocab_to_int[word] for word in review.split()])
    return vocab_to_int

# this is a very toy example, do not try this at home unless you want to understand the usage differences
docs=["the house had a tiny little mouse",
      "the cat saw the mouse",
      "the mouse ran away from the house",
      "the cat finally ate the mouse",
      "the end of the mouse story mouse"
     ]

uniques = unique_words(docs)
print('Unique words: ', len((uniques)))

print("============cv===============")

#instantiate CountVectorizer()
#Convert a collection of text documents to a matrix of token counts
cv=CountVectorizer(stop_words="english")
 
# this steps generates word counts for the words in your docs
word_count_vector=cv.fit_transform(docs)

#print(word_count_vector)
print(word_count_vector.shape)
print(cv.get_feature_names())
print(word_count_vector.toarray()) 


print("============ftidf===============")

# Initialize a TfidfVectorizer object: tfidf_vectorizer
tv = TfidfVectorizer(stop_words="english")

# Transform the training data: tfidf_train 
word_tfid_vector = tv.fit_transform(docs)

#print(word_tfid_vector)
print(word_tfid_vector.shape)
print(tv.get_feature_names())
print(word_tfid_vector.toarray()) 
 