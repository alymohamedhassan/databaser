class Insert:

    def __init__(self, table_name: str, data: dict):
        self.table_name = table_name
        self.fields = []
        self.values = []

        if len(data.keys()) == 0:
            raise Exception("There is no data to insert")

        for field in data.keys():
            self.values.append(str(data[field]))
            self.fields.append(field)

    def get_sql(self):
        fields = self.fields
        values = self.values

        return f"INSERT INTO {self.table_name} ({', '.join(fields)}) VALUES ({', '.join(values)})"
