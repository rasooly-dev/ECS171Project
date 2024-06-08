from fastapi import FastAPI
from scrape_url import fetchURL
from model import model_predict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Testing 123!"}

@app.post("/url")
async def scrape_url(request):
    url  = request.url
    data = fetchURL(url=url)
    prediction = model_predict(data)
    
    return {"prediction": prediction}
