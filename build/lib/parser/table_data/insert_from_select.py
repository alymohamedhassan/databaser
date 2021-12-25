from typing import List

from src import Finder


class InsertFromSelect:
    def __init__(self, table_name: str, fields: List[str], select: Finder):
        self.table_name = table_name
        self.fields = fields
        self.select: str = select.get_sql()

    def get_sql(self):
        return f"INSERT INTO {self.table_name} ({','.join(self.fields)}) {self.select}"