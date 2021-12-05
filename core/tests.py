from core.parser.database.create_database import CreateDatabase
from core.parser.database.drop_database import DropDatabase
from core.parser.table_data.delete import Delete
from core.parser.table_data.insert import Insert
from core.parser.table_data.finder import Finder
from core.parser.table_data.update import Update
from core.parser.table_structure.add_column import AddColumn
from core.parser.table_structure.create_table import CreateTable


def test_queries():
    print("Testing queries")
    # SELECT * FROM tablename
    sql = Finder("table_name").get_sql()
    print(sql)
    assert sql == "SELECT * FROM table_name"

    # SELECT a, b, c FROM table_name
    sql = Finder("table_name", ["a", "b", "c"]).get_sql()
    print(sql)
    assert sql == "SELECT a,b,c FROM table_name"

    # SELECT a, b, c FROM table_name LIMIT 10
    sql = Finder("table_name", ["a", "b", "c"], limit=10).get_sql()
    print(sql)
    assert sql == "SELECT a,b,c FROM table_name LIMIT 10"

    # SELECT * FROM table_name WHERE name = 'abc'
    condition = {
        "name": {
            "$value": "abc"
        },
    }
    sql = Finder("table_name", ["a", "b", "c"], condition=condition, limit=10).get_sql()
    print(sql)
    assert sql == "SELECT a,b,c FROM table_name WHERE name = 'abc' LIMIT 10"

    # SELECT * FROM table_name WHERE name = 'abc' AND names = 'abc'
    condition = {
        "name": {
            "$value": "abc"
        },
        "names": {
            "$value": "abc"
        },
    }
    sql = Finder("table_name", ["a", "b", "c"], condition=condition, limit=10).get_sql()
    print(sql)
    assert sql == "SELECT a,b,c FROM table_name WHERE name = 'abc' AND names = 'abc' LIMIT 10"

    # SELECT * FROM table_name WHERE name = 'abc'
    condition = {
        "name": {
            "$value": "abc"
        },
        "$group": {
            "$type": "OR",
            "name": {
                "$value": "abc"
            },
            "names": {
                "$value": "abc"
            },
            "named": {
                "$value": "abc"
            },
        }
    }
    sql = Finder("table_name", ["a", "b", "c"], condition=condition, limit=10).get_sql()
    print(sql)
    assert sql == "SELECT a,b,c FROM table_name WHERE name = 'abc' AND (name = 'abc' OR names = 'abc' OR named = 'abc') LIMIT 10"

    # SELECT * FROM table_name GROUP BY name, lol
    sql = Finder("table_name", group_by=["name", "lol"]).get_sql()
    print(sql)
    assert sql == "SELECT * FROM table_name GROUP BY name, lol"

    # SELECT * FROM table_name ORDER BY name ASC
    sql = Finder("table_name", order_by={"name": True}).get_sql()
    print(sql)
    assert sql == "SELECT * FROM table_name ORDER BY name ASC"


def test_insertions():
    print("Testing Insertions")
    # SELECT * FROM tablename
    data = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    sql = Insert("table_name", data=data).get_sql()
    print(sql)
    assert sql == "INSERT INTO table_name (a, b, c) VALUES (1, 2, 3)"


def test_update():
    print("Testing update")
    # UPDATE table_name SET name = 'lol' WHERE name = 'mido'
    conditions = {
        "name": {
            "$value": "mido"
        }
    }
    data = {
        "name": "lol"
    }
    sql = Update("table_name", data=data, conditions=conditions).get_sql()
    print(sql)
    assert sql == "UPDATE table_name SET name = 'lol' WHERE name = 'mido'"

    # UPDATE table_name SET name = 'lol' WHERE name = 'mido'
    conditions = {
        "name": {
            "$value": "mido"
        }
    }
    data = {
        "name": "lol",
        "date": "lol",
    }
    sql = Update("table_name", data=data, conditions=conditions).get_sql()
    print(sql)
    assert sql == "UPDATE table_name SET name = 'lol', date = 'lol' WHERE name = 'mido'"


def test_delete():
    print("Testing Delete")
    # UPDATE table_name SET name = 'lol' WHERE name = 'mido'
    conditions = {
        "name": {
            "$value": "mido"
        }
    }
    sql = Delete("table_name", conditions=conditions).get_sql()
    print(sql)
    assert sql == "DELETE FROM table_name WHERE name = 'mido'"


def table_structure():
    print("Test Table Structure")
    sql = CreateTable().get_sql()
    assert sql == ""

    sql = AddColumn("tablename", "column_name", "string", True).get_sql()
    print("SQL:", sql)
    # assert sql == "ALTER TABLE tablename ADD COLUMN column_name string NOT NULL"


def test_DB():
    print("Testing test_create_DB")
    # CREATE DATABASE database_name
    sql = CreateDatabase("database_name").get_sql()
    print(sql)
    assert sql == "CREATE DATABASE database_name"

    # CREATE DATABASE database_name
    sql = DropDatabase("database_name").get_sql()
    print(sql)
    assert sql == "DROP DATABASE database_name"

