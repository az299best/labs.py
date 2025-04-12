import sys
import functools
import json
import datetime
import sqlite3

# параметризованный декоратор
def trace(func=None, *, handle=sys.stdout):
    if func is None:
        return lambda func: trace(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        log_format = {'datetime': datetime.datetime.now().isoformat(),
                      'func_name': func.__name__,
                      'params': {'args': args, 'kwargs': kwargs},
                      'result': result}

        if isinstance(handle, str) and handle.endswith(".json"):
            with open(handle, "w") as json_file:
                json.dump(log_format, json_file)
        elif isinstance(handle, sqlite3.Connection):
            con = handle.cursor()
            con.execute("CREATE TABLE IF NOT EXISTS logtable ("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "datetime TEXT, "
                        "func_name TEXT, "
                        "params TEXT, "
                        "result TEXT)")
            cmd = (f"INSERT INTO logtable(datetime, func_name, params, result) VALUES ("
                   f"'{log_format['datetime']}', "
                   f"'{log_format['func_name']}', "
                   f"'{str(log_format['params']['args']) + " " + str(log_format['params']['kwargs'])}',"
                   f"'{log_format['result']}')")
            con.execute(cmd)
            handle.commit()
        else:
            handle.write(f"result={result}\n")
        return result
    return inner

def showlogs(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("SELECT * FROM logtable")
    rows = cur.fetchall()
    for row in rows:
        print(row)


@trace  # по умолчанию - sys.stdout
def increment(x):
    """Инкремент"""
    return x + 1

@trace(handle=sys.stderr) # вывод в sys.stderr
def decrement(x):
    """Инкремент"""
    return x - 1

@trace(handle="output.json")  # вывод в .json
def write_to_file(x):
    """Инкремент"""
    return x**3

db_handle = sqlite3.connect("sqlite3.db")
@trace(handle=db_handle) # вывод в sqlite3_database
def write_to_db(x):
    return x**4


res = increment(2)
print("Increment -> to default stdout:", res)
res = decrement(2)
print("Decrement -> to stderr:", res)
res = write_to_file(2)
print("Write_to_file -> to output.json:", res)

res = write_to_db(2)
print("Write_to_db -> tosqlite3.db:", res)

showlogs(db_handle)