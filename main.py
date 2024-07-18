from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from routers.api import api
from routers.htmx import htmx


limiter = Limiter(key_func=get_remote_address, application_limits=["1/minute"])
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(api)
app.include_router(htmx)


app.mount("/", StaticFiles(directory="static", html=True), name="static")
