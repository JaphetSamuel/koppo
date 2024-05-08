from typing import Callable

from core.views.renderable import Renderable


def global_render(page: Renderable | Callable):
    result: str = ""
    if isinstance(page, Renderable):
        result = page.render()
    elif callable(page):
        result = page()
    return result