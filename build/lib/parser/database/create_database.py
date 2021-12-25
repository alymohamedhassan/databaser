class CreateDatabase:
    def __init__(self, database_name: str):
        self.database_name = database_name

    def get_sql(self):
        return f"CREATE DATABASE {self.database_name}"