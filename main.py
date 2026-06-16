from fastapi import FastAPI

from scraper import buscar_mercari, KEYWORDS

app = FastAPI()


@app.get("/")
def status():
    return {"status": "ok"}


@app.get("/buscar")
def buscar():
    resultados = buscar_mercari(KEYWORDS)
    return resultados
