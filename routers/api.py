import asyncio

from fastapi import APIRouter

from modules import QuizD
from modules import Gemini, Lender


api = APIRouter(prefix="/api", tags=["API"])

gemini = Gemini()


async def get_answer(prompt: str) -> dict:
    def wrapper():
        return gemini(prompt)

    response = await asyncio.to_thread(wrapper)
    lender = Lender(response)
    parsed = lender.parse_all()

    return parsed


@api.get("/physics")
async def physics(unit: str, keyword: str):
    physics_prompt = QuizD.Physics()
    return await get_answer(physics_prompt(unit, keyword))


@api.get("/chemistry")
async def chemistry(unit: str, keyword: str):
    chemistry_prompt = QuizD.Chemistry()
    return await get_answer(chemistry_prompt(unit, keyword))


@api.get("/biology")
async def biology(unit: str, keyword: str):
    biology_prompt = QuizD.Biology()
    return await get_answer(biology_prompt(unit, keyword))


@api.get("/earth")
async def earth(unit: str, keyword: str):
    earth_prompt = QuizD.Earth()
    return await get_answer(earth_prompt(unit, keyword))


@api.get("/history")
async def history(unit: str, keyword: str):
    history_prompt = QuizD.History()
    return await get_answer(history_prompt(unit, keyword))


@api.get("/accounting")
async def accounting(unit: str, keyword: str):
    accounting_prompt = QuizD.Accounting()
    return await get_answer(accounting_prompt(unit, keyword))
