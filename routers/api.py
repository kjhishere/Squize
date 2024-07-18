from fastapi import APIRouter, Request

from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini, Lender


api = APIRouter(
	prefix="/api",
    tags=["API"]
)

gemini = Gemini()


async def get_answer(prompt: str) -> dict:
    response = gemini(prompt)
    lender = Lender(response)
    parsed = lender.parse_all()

    return parsed


@api.get("/physics")
async def physics(request: Request, unit: str, keyword: str):
    physics_prompt = Physics()
    return await get_answer(physics_prompt(unit, keyword))


@api.get("/chemistry")
async def chemistry(request: Request, unit: str, keyword: str):
    chemistry_prompt = Chemistry()
    return await get_answer(chemistry_prompt(unit, keyword))


@api.get("/biology")
async def biology(request: Request, unit: str, keyword: str):
    biology_prompt = Biology()
    return await get_answer(biology_prompt(unit, keyword))


@api.get("/earth")
async def earth(request: Request, unit: str, keyword: str):
    earth_prompt = Earth()
    return await get_answer(earth_prompt(unit, keyword))