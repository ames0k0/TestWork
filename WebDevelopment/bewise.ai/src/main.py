#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

/src
    /routers
        application.py
    /database
        app
        crud
        models
    /datastream
        app
tests
    /
"""


from typing import Union

from fastapi import FastAPI

from src.core import dependencies
from src.routers import application


app = FastAPI(
    title="bewise.ai",
    summary="Сервис для обработки заявок пользователей",
    lifespan=dependencies.lifespan,
)


app.include_router(
    router=application.router,
    prefix='/applications',
    tags=['Заявки'],
)
