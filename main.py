from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import api, htmx

app = FastAPI()
app.include_router(api)
app.include_router(htmx)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
