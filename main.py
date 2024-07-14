from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/api/physics")
@limiter.limit("1/minute")
async def physics(request: Request, unit: str, keyword: str):
    physics_prompt = Physics()
    prompt = physics_prompt(unit, keyword)
    return {"prompt": prompt}


@app.get("/api/chemistry")
@limiter.limit("1/minute")
async def chemistry(request: Request, unit: str, keyword: str):
    chemistry_prompt = Chemistry()
    prompt = chemistry_prompt(unit, keyword)
    return {"prompt": prompt}


@app.get("/api/biology")
@limiter.limit("1/minute")
async def biology(request: Request, unit: str, keyword: str):
    biology_prompt = Biology()
    prompt = biology_prompt(unit, keyword)
    return {"prompt": prompt}


@app.get("/api/earth")
@limiter.limit("1/minute")
async def earth(request: Request, unit: str, keyword: str):
    earth_prompt = Earth()
    prompt = earth_prompt(unit, keyword)
    return {"prompt": prompt}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
