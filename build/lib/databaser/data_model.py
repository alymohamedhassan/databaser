from typing import List

from databaser.engine.engine import DatabaseEngine
from databaser.parser.table_structure.create_table import TableField
from databaser.pgsql import Query

from config import conn_string


class DataModel:
    table_name = None
    schema_name = 'public'
    fields: List[TableField] = []

    def __init__(self):
        self.__sql = []

    def __get_fields(self):
        fields = []
        for field in self.fields:
            fields.append(field.name)

        return fields

    def get(self, fields: List = None, condition: dict = {}, joins: dict = {},
                 group_by: list = [], order_by: dict = {}, limit: int = 0, skip: int = 0):

        if fields is None:
            fields = self.__get_fields()

        sql = Query(
            'pgsql'
        ).find(self.table_name, fields, condition, joins, group_by, order_by, limit, skip, schema_name=self.schema_name).get_sql()
        self.__sql.append(sql)
        return self

    def get_one(self, fields: List[str] = None, condition: dict = {}, joins: dict = {}):
        sql = Query(
            'pgsql'
        ).find(self.table_name, fields, condition, joins, limit=1, schema_name=self.schema_name).get_sql()
        # print("This instance:", id(self))
        # print("This instance:", self.__sql)

        self.__sql.append(sql)

        return self

    def insert(self, data: dict, value_quote: bool = True):
        sql = Query(
            'pgsql'
        ).insert(self.table_name, data=data, value_quote=value_quote, schema_name=self.schema_name).get_sql()
        self.__sql.append(sql)
        return self

    def update(self, data: dict, conditions: dict, value_quote: bool = True):
        sql = Query(
            'pgsql'
        ).update(self.table_name, data=data, conditions=conditions, value_quote=value_quote, schema_name=self.schema_name).get_sql()
        self.__sql.append(sql)
        return self

    def get_transactions(self):
        return self.__sql

    def show(self, fetch_one: bool = False):
        return DatabaseEngine(**conn_string).execute(self.__sql, has_return=True, return_many=(not fetch_one))

    def commit(self):
        return DatabaseEngine(**conn_string).execute(self.__sql, transaction=True)

    def set_schema_name(self, schema_name: str):
        self.schema_name = schema_name
        return self.schema_name

    def get_schema_name(self) -> str:
        return self.schema_name
