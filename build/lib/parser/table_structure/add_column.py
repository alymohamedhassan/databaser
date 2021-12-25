class AddColumn:
    def __init__(self, table_name: str, column_name: str, data_type: str, not_null: bool):
        self.table_name = table_name
        self.column_name = column_name
        self.data_type = data_type
        self.not_null = not_null

    def get_sql(self):
        nullable = 'NOT NUll' if self.not_null else 'NULL'
        return f"ALTER TABLE {self.table_name} ADD COLUMN {self.column_name} {self.data_type} {nullable}"
