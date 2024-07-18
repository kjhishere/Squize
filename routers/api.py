from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini, Lender


limiter = Limiter(key_func=get_remote_address)
router = APIRouter(
	prefix="/api"
)
router.state.limiter = limiter
router.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

gemini = Gemini()


async def get_answer(prompt: str) -> dict:
    response = gemini(prompt)
    lender = Lender(response)
    parsed = lender.parse_all()

    return parsed


@router.get("/physics")
@limiter.limit("1/minute")
async def physics(request: Request, unit: str, keyword: str):
    physics_prompt = Physics()
    return await get_answer(physics_prompt(unit, keyword))


@router.get("/chemistry")
@limiter.limit("1/minute")
async def chemistry(request: Request, unit: str, keyword: str):
    chemistry_prompt = Chemistry()
    return await get_answer(chemistry_prompt(unit, keyword))


@router.get("/biology")
@limiter.limit("1/minute")
async def biology(request: Request, unit: str, keyword: str):
    biology_prompt = Biology()
    return await get_answer(biology_prompt(unit, keyword))


@router.get("/earth")
@limiter.limit("1/minute")
async def earth(request: Request, unit: str, keyword: str):
    earth_prompt = Earth()
    return await get_answer(earth_prompt(unit, keyword))