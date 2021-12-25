from typing import List

from src import Finder
from src import Insert
from src import Update
from src import Delete


class Query:
    TABLE_QUOTE = ""
    FIELD_QUOTE = ""

    def __init__(self, server_name: str):
        if server_name == "pgsql":
            self.FIELD_QUOTE = '"'
            self.TABLE_QUOTE = '"'

    def find(self, table_name: str, fields: List[str] = None, condition: dict = {}, joins: dict = {},
                 group_by: list = [], order_by: dict = {}, limit: int = 0, skip: int = 0):
        return Finder(table_name, fields, condition, joins, group_by, order_by, limit, skip, self.FIELD_QUOTE,
                      self.FIELD_QUOTE)

    def insert(self, table_name: str, data: dict, value_quote: bool = False):
        return Insert(table_name, data, self.FIELD_QUOTE, self.FIELD_QUOTE, value_quote)

    def update(self, table_name: str, data: dict, conditions: dict, value_quote: bool = False):
        return Update(table_name, data, conditions, self.FIELD_QUOTE, self.FIELD_QUOTE, value_quote)

    def delete(self, table_name: str, conditions: dict, value_quote: bool = False):
        return Delete(table_name, conditions, self.FIELD_QUOTE, self.FIELD_QUOTE, value_quote)
