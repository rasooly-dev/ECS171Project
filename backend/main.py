from fastapi import FastAPI
from utils.model import ModelService
from utils.url_fasttext import FastTextURLService
from utils.scrape_url import ScrapeService

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Or specify precise methods ['GET', 'POST', etc.]
    allow_headers=["*"],  # Or specify precise headers
)

model = ModelService(file_path='models/Random Forest_fold_4.pkl', scaler_path='models/scaler.pkl')
fasttext_url_service = FastTextURLService(file_path='models/url_fasttext.model')

@app.get("/")
def read_root():
    return {"message": "Testing 123!"}

class PredictPayload(BaseModel):
    url: str

@app.post("/predict")
async def scrape_url(payload: PredictPayload):
    # print(payload)
    url  = payload.url

    scraper = ScrapeService(url)
    data = await scraper.get_data()

    if not data:
        return {
            "url": url,
            "error": "Invalid URL"
        }

    data = data.to_dict()

    vectorized_url = fasttext_url_service.vectorize_url(url)

    combined = model.get_data_frame(data, vectorized_url)

    X = model.normalize(combined)
    print(X)

    prediction = model.predict(X)[0]
    
    return {
        "url": url,
        'data': data,
        "prediction": False if prediction == 1 else True
    }
