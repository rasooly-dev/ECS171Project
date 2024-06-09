import numpy as np
import pickle
import joblib
import pandas as pd

class ModelService:

    def __init__(self, file_path, scaler_path = None):
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)
        with open(scaler_path, 'rb') as f:
            self.scaler = joblib.load(f)
    
    def normalize(self, df: pd.DataFrame):
        normalized_df = df.copy()
        normalized_df.columns = normalized_df.columns.astype(str)
        normalized_df[normalized_df.columns.difference(['IsHTTPS', 'IsResponsive', 'HasDescription', 'HasSocialNet', 'HasSubmitButton', 'HasCopyrightInfo'])] = self.scaler.transform(normalized_df[normalized_df.columns.difference(['label', 'IsHTTPS', 'IsResponsive', 'HasDescription', 'HasSocialNet', 'HasSubmitButton', 'HasCopyrightInfo'])])

        X = normalized_df.iloc[0:1]
        return X
        
    def predict(self, X):
        return self.model.predict(X)
    
    def get_data_frame(self, data, vectorized_url):
        
        del data['url']
        del data['domain']

        df = pd.DataFrame([np.array(
            [data['special'], data['https'], data['lines'], data['domain_title'], data['is_responsive'], data['description'], data['socials'], data['has_submit'], data['copyright'], data['images'], data['js'], data['self_ref']]
        )], columns=['SpacialCharRatioInURL', 'IsHTTPS', 'LineOfCode', 'DomainTitleMatchScore', 'IsResponsive', 'HasDescription', 'HasSocialNet', 'HasSubmitButton', 'HasCopyrightInfo', 'NoOfImage', 'NoOfJS', 'NoOfSelfRef'])

        url_vector = pd.DataFrame([vectorized_url], index=df.index)
        # only keep these columns from the vectorized URL: 7	10	25	40	41	51	54	65	73	88	89	97
        url_vector = url_vector.iloc[:, [7, 10, 25, 40, 41, 51, 54, 65, 73, 88, 89, 97]]

        combined = pd.concat([df, url_vector], axis=1)

        return combined
