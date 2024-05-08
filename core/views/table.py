from typing import TypedDict, List

from core.views.renderable import Renderable


class Header(TypedDict, total=False):
    name: str
    istype: str
    is_visible: bool

class Table(Renderable):
    headers: list[Header]
    data: dict

    def __init__(self):
        self.headers = []
        self.data = []

    def setHeader(self, name: str, istype: str, is_visible: bool = True):
        self.headers.append({"name": name, "istype": istype, "is_visible": is_visible})
        return self

    def setData(self, data:List[dict]):
        self.data = data
        return self

    def render(self):
        return f"""
        <table>
            <thead>
                <tr>
                    {"\n".join([f"<th>{header["name"]}</th>" for header in self.headers if header["is_visible"]])}
                </tr>
            </thead>
            <tbody>
                {"\n".join([f"<tr>{'\n'.join([f'<td>{data}</td>' for data in row.values()])}</tr>" for row in self.data])}
            </tbody>
        """
