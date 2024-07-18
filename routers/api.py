from typing import Union

from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini, Lender


router = APIRouter(
	prefix="/api"
)

gemini = Gemini()


async def get_answer(prompt: str, to_html: bool) -> Union[dict, str]:
    response = gemini(prompt)
    lender = Lender(response)
    parsed = lender.parse_all()

    if to_html:
        parsed_list = [Lender.to_html(parse) for parse in parsed]
        return PlainTextResponse("<hr>".join(parsed_list))
    else:
        return parsed


@router.get("/api/physics")
@limiter.limit("1/minute")
async def physics(request: Request, unit: str, keyword: str):
    physics_prompt = Physics()
    return await get_answer(physics_prompt(unit, keyword))


@router.get("/api/chemistry")
@limiter.limit("1/minute")
async def chemistry(request: Request, unit: str, keyword: str):
    chemistry_prompt = Chemistry()
    return await get_answer(chemistry_prompt(unit, keyword))


@router.get("/api/biology")
@limiter.limit("1/minute")
async def biology(request: Request, unit: str, keyword: str):
    biology_prompt = Biology()
    return await get_answer(biology_prompt(unit, keyword))


@router.get("/api/earth")
@limiter.limit("1/minute")
async def earth(request: Request, unit: str, keyword: str):
    earth_prompt = Earth()
    return await get_answer(earth_prompt(unit, keyword))