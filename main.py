from typing import Union

from fastapi import FastAPI

from modules import Physics, Chemistry, Biology, Earth


app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/physics")
async def physics(unit: str, keyword: str):
    return {"Unit": unit, "Keyword": keyword}


@app.get("/chemistry")
async def chemistry(unit: str, keyword: str):
    return {"Unit": unit, "Keyword": keyword}


@app.get("/biology")
async def biology(unit: str, keyword: str):
    return {"Unit": unit, "Keyword": keyword}


@app.get("/earth")
async def earth(unit: str, keyword: str):
    return {"Unit": unit, "Keyword": keyword}
