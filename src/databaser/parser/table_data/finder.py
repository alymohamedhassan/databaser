from typing import List

from src.databaser.parser.table_data.condition_parser import ConditionParser
from src.databaser.parser.table_data.join_parser import JoinParser


class Finder:

    def __init__(self, table_name: str, fields: List[str] = None, condition: dict = {}, joins: dict = {},
                 group_by: list = [], order_by: dict = {}, limit: int = 0, skip: int = 0, table_quote="", field_quote=""):
        self.table_name = table_name
        self.limit = limit
        self.conditions = condition
        self.joins = joins

        self.table_quote = table_quote
        self.field_quote = field_quote

        self.group_by = group_by
        if group_by is None or len(group_by) == 0:
            self.group_by = []

        self.order_by = order_by
        if order_by is None or len(order_by.keys()) == 0:
            self.order_by = {}

        if fields is None or len(fields) == 0:
            self.fields = "*"
        else:
            self.fields = self.field_quote + f'{self.field_quote},{self.field_quote}'.join(fields) + self.field_quote

    def order_by_parser(self, order_by: dict):
        orders = []
        for field in order_by.keys():
            order_type = order_by[field]
            if type(order_type) is not str:
                if type(order_type) is int:
                    order_type = "ASC" if order_type > 0 else "DESC"
                elif type(order_type) is bool:
                    order_type = "ASC" if order_type else "DESC"
                else:
                    order_type = "ASC"
            else:
                order_type = order_type.upper()

            orders.append(f'{field} {order_type}')

        return f"ORDER BY {','.join(orders)}"

    def get_sql(self) -> str:
        clauses = []

        joins = "" if len(self.joins.keys()) == 0 else JoinParser(self.table_name, self.joins, self.table_quote, self.field_quote).get_parsed()
        if joins != "":
            clauses.append(joins)

        where = "" if len(self.conditions.keys()) == 0 else "WHERE " + ConditionParser(self.conditions, self.field_quote).get_parsed()
        if where != "":
            clauses.append(where)

        group_by = "" if len(self.group_by) == 0 else f"GROUP BY {self.field_quote}{f'{self.field_quote}, {self.field_quote}'.join(self.group_by)}{self.field_quote}"
        if group_by != "":
            clauses.append(group_by)

        order_by = "" if len(self.order_by.keys()) == 0 else self.order_by_parser(self.order_by)
        if order_by != "":
            clauses.append(order_by)

        limit = f"LIMIT {self.limit}" if self.limit is not None and self.limit > 0 else ""
        if limit != "":
            clauses.append(limit)

        if len(clauses) > 0:
            clauses.insert(0, "")

        return f"""SELECT {self.fields} FROM {self.table_quote}{self.table_name}{self.table_quote}{' '.join(clauses)};"""
