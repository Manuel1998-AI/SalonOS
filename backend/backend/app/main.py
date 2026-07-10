from fastapi import FastAPI

app = FastAPI(
    title="SalonOS API",
    description="Backend principale della piattaforma SalonOS",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "nome": "SalonOS",
        "stato": "Backend attivo",
        "versione": "0.1.0"
    }
