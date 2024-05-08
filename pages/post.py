from core.views.page import Page
from core.views.table import Table


class PostPage(Page):

    def table(self):
        return Table().setHeader("Name", "string").setHeader("Age", "number").setData([
            {"Name": "John", "Age": 20},
            {"Name": "Doe", "Age": 30},
            {"Name": "Jane", "Age": 40},
        ])

    def path_str(self):
        return "posts"