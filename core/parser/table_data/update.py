from core.parser.table_data.condition_parser import ConditionParser


class Update:
    def __init__(self, table_name: str, data: dict, conditions: dict):
        self.table_name = table_name
        self.conditions = conditions
        self.data = data

    def get_sql(self):
        data = []
        where = "" if len(self.conditions.keys()) == 0 else ConditionParser(self.conditions).get_parsed()

        for field in self.data.keys():
            value = f"{field} = '{self.data[field]}'"
            data.append(value)

        if len(data) == 0:
            return ""

        if where != "":
            where = "WHERE " + where

        return f"UPDATE {self.table_name} SET {', '.join(data)} {where}"
