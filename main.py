import abc
from typing import Callable, TypedDict, List

from fastapi import FastAPI, Response

from providers.pageProvider import pages

app = FastAPI()

for page in pages:
    app.include_router(page.get_route())
