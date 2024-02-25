import redis.asyncio as redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from src.routes import auth
from src.conf.config import settings


app = FastAPI() 

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix='/api')



@app.on_event("startup")
async def startup():
    """
    Initializes the connection to a Redis database for rate limiting purposes.
    :params r: representing the connection with Redis database.
    :type r: Redis
    :return: None
    """

    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, encoding="utf-8",
                          decode_responses=True)
    await FastAPILimiter.init(r)

