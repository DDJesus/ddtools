import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from curses.ascii import isdigit
from string import digits


def full_cleanse(data):
    """
    Creates list of list of cleaned word tokens out of text data

    :param data: string
    :return: list
    """
    tokenizer = RegexpTokenizer(r'\w+')
    stops = set(stopwords.words('english'))

    sent_toks = []
    for text in data:
        try:
            text = tokenizer.tokenize(text)
            pos_tagged = nltk.pos_tag(text)
            words = [w[0] for w in pos_tagged if w[1].capitalize() != 'NNP']
            words = [WordNetLemmatizer().lemmatize(w) for w in words]
            words = [w.lower() for w in words if not w.lower() in stops]
            words = [w for w in words if not w.isdigit()]
            sent_toks.append(words)
        except TypeError:
            pass
    return sent_toks


def remove_digits(text):
    """

    :param text: string
    :return: string
    """
    digits_removed = str.maketrans('', '', digits)
    return text.translate(digits_removed)


def word_tokens(text):
    """

    :param text: string
    :return: list
    """
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)


def sent_tokens(text):
    """

    :param text: string
    :return: list
    """
    return sent_tokenize(text)

