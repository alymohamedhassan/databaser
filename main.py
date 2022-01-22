from databaser.tests import test_queries, test_insertions, test_update, test_delete, test_DB, table_structure, \
    test_engine


def test_app():
    print("Databaser Starting ...")
    test_queries()
    test_insertions()
    test_update()
    test_delete()

    test_DB()

    table_structure()


if __name__ == '__main__':
    test_app()
