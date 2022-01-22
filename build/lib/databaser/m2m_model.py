from .data_model import DataModel

class Many2ManyModel(DataModel):

    joining_table_name = None

    def get(self, fields: List = None, condition: dict = {}, joins: dict = {},
                 group_by: list = [], order_by: dict = {}, limit: int = 0, skip: int = 0):
        if self.joining_table_name is not None:
            raise Exception("Joining Table Missing")

        if fields is None:
            fields = self.__get_fields()

        sql = Query(
            'pgsql'
        ).find(self.table_name, fields, condition, joins, group_by, order_by, limit, skip, schema_name=self.schema_name).get_sql()

        # TODO: add a joining table

        self.__sql.append(sql)
        return self
