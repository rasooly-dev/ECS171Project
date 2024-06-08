import joblib
import numpy as np
from gensim.models import Word2Vec

model = joblib.load('xgboost_model.joblib')

def model_predict(Data):
    input_data = np.array([[Data.url, Data.domain, Data.specialCharacterCount,Data.isHTTPS, Data.numOfCodeLines, Data.domainTitleMatchScore, Data.hasDescription, Data.hasSocial, Data.hasCopyright,Data.countImage, Data.countJS, Data.countSelfRef,]]) # need to add url vector data
    
    prediction = model.predict(input_data)

    return prediction

def vectorize_url(url):
    tokenized_urls = (url)
    vec_model = Word2Vec(sentences=tokenized_urls, vector_size=100, window=5, min_count=1, workers=4)
    df['url_vector'] = df['tokenized_url'].apply(lambda x: aggregate_vectors(x, model))


def aggregate_vectors(tokens, model):
    vectors = [model.wv[token] for token in tokens if token in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)
