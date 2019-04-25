import pandas as pd
from sklearn.model_selection import cross_val_score
import numpy as np
from nltk.stem.porter import PorterStemmer
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(question):
    classifications = pd.read_csv('perguntas.csv', encoding = 'utf-8')
    count_vectorizer = CountVectorizer(stop_words='english')
    
    questionsCsv = classifications['Pergunta 1'].str.lower()

    answersCsv = classifications['Resposta'].str.lower()
    
    count_vectorizer.fit_transform(tuple(questionsCsv))
    freq_term_matrix = count_vectorizer.transform(tuple([question]))
    tfidf = TfidfTransformer()
    tfidf.fit(freq_term_matrix)
    tf_idf_matrix = tfidf.transform(freq_term_matrix)

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(tuple(questionsCsv))
    tfidf_matrix_question = tfidf_vectorizer.transform(tuple([question]))
    cosine_values = cosine_similarity(tfidf_matrix_question, tfidf_matrix).tolist()
    index = cosine_values[0].index(max(cosine_values[0]))
    print(index)
    return answersCsv[index]

if __name__ == '__main__':
    calculate_similarity(sys.argv[1])