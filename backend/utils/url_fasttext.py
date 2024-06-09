import re
import numpy as np

from gensim.models import FastText

class FastTextURLService:

    def __init__(self, file_path):
        self.model = FastText.load(file_path)
    
    def vectorize_url(self, url):
        tokens = FastTextURLService.tokenizeURL(url)
        return self.aggregate_vectors(tokens, self.model)

    @staticmethod
    def tokenizeURL(url):
        tokens = re.split(r'\W+', url)
        tokens = [token.lower() for token in tokens if token]
        print(tokens)
        return tokens
    
    @staticmethod
    def aggregate_vectors(tokens, model):
        vectors = [model.wv[token] for token in tokens if token in model.wv]
        if vectors:
            return np.mean(vectors, axis=0)
        else:
            return np.zeros(model.vector_size)