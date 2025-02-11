from contextlib import asynccontextmanager


from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """`startup` and `shutdown` logic"""
    # TODO: postgresql
    yield
