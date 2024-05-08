import abc


class Renderable(abc.ABC):
    def render(self) -> str:
        ...