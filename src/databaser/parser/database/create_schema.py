class CreateSchema:
    def __init__(self, schema_name: str):
        self.schema_name = schema_name

    def get_sql(self):
        sql = f"CREATE SCHEMA {self.schema_name};"
        return sql
