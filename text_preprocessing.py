import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


ps = PorterStemmer()


def transform_text(text):
    # lower casing
    text = text.lower()

    # tokenization
    text = nltk.word_tokenize(text)

    # removing special characters
    tmp = []
    for i in text:
        if i.isalnum():
            tmp.append(i)

    text = tmp[:]
    tmp.clear()

    # removing stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            tmp.append(i)

    text = tmp[:]
    tmp.clear()

    # stemming
    for i in text:
        tmp.append(ps.stem(i))

    return " ".join(tmp)
