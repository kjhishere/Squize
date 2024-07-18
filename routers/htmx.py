import asyncio

from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini, Lender


htmx = APIRouter(prefix="/htmx", tags=["htmx"])

gemini = Gemini()


async def get_answer(prompt: str) -> str:
    response = await asyncio.to_thread(gemini(prompt))
    lender = Lender(response)
    parsed = lender.parse_all()

    parsed_list = [Lender.to_html(parse) for parse in parsed]
    return PlainTextResponse("<hr>".join(parsed_list))


@htmx.get("/physics")
async def physics(request: Request, unit: str, keyword: str):
    physics_prompt = Physics()
    return await get_answer(physics_prompt(unit, keyword))


@htmx.get("/chemistry")
async def chemistry(request: Request, unit: str, keyword: str):
    chemistry_prompt = Chemistry()
    return await get_answer(chemistry_prompt(unit, keyword))


@htmx.get("/biology")
async def biology(request: Request, unit: str, keyword: str):
    biology_prompt = Biology()
    return await get_answer(biology_prompt(unit, keyword))


@htmx.get("/earth")
async def earth(request: Request, unit: str, keyword: str):
    earth_prompt = Earth()
    return await get_answer(earth_prompt(unit, keyword))
