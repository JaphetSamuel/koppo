from core.utils import global_render
from core.views.renderable import Renderable
from core.views.table import Table
from fastapi import Response


class Page(Renderable):

    def __init__(self):
        self._path_str= self.path_str() or self.__class__.__name__
        self._table = self.table() or None

    def table(self)->Table:
        ...

    def path_str(self)->str:
        ...

    def get_route(self):
        from fastapi import APIRouter
        router = APIRouter(tags=[self._path_str])

        @router.get(f"/{self._path_str}")
        def get():
            return Response(content=global_render(self))

        return router

    def render(self):
        return f"""
        <html>
            <head>
                <title>Tree</title>
            </head>
            <body>
                <section>
                {self._table.render() if self._table else ""}
                </section>
                <p>Tree structure</p>
            </body>
        </html>
    """
