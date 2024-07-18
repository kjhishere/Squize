from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini, Lender


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

gemini = Gemini()


async def get_answer(prompt: str, to_html: bool) -> Union[dict, str]:
    response = gemini(prompt)
    lender = Lender(response)
    parsed = lender.parse_all()

    if to_html:
        parsed_list = [Lender.to_html(parse) for parse in parsed]
        return "<hr>".join(parsed_list)
    else:
        return parsed


@app.get("/api/physics")
@limiter.limit("1/minute")
async def physics(request: Request, unit: str, keyword: str, to_html: bool = False):
    physics_prompt = Physics()
    return await get_answer(physics_prompt(unit, keyword), to_html)


@app.get("/api/chemistry")
@limiter.limit("1/minute")
async def chemistry(request: Request, unit: str, keyword: str):
    chemistry_prompt = Chemistry()
    return await get_answer(chemistry_prompt(unit, keyword))


@app.get("/api/biology")
@limiter.limit("1/minute")
async def biology(request: Request, unit: str, keyword: str):
    biology_prompt = Biology()
    return await get_answer(biology_prompt(unit, keyword))


@app.get("/api/earth")
@limiter.limit("1/minute")
async def earth(request: Request, unit: str, keyword: str):
    earth_prompt = Earth()
    return await get_answer(earth_prompt(unit, keyword))


app.mount("/", StaticFiles(directory="static", html=True), name="static")
