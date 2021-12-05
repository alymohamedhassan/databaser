from core.parser.table_data.condition_parser import ConditionParser


class Delete:
    def __init__(self, table_name: str, conditions):
        self.table_name = table_name
        self.conditions = conditions

    def get_sql(self):
        where = "" if len(self.conditions.keys()) == 0 else ConditionParser(self.conditions).get_parsed()

        if where != "":
            where = "WHERE " + where

        return f"DELETE FROM {self.table_name} {where}"
