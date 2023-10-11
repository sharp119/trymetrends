from database.db_connector import get_db_connection
# from server.queries.queries import INSERT_QUERIES


def execute_queries_from_file(filename):
    """
    executes sql queries from specified path sql file
    sql_file_path = "database/queries.sql"
    execute_queries_from_file(sql_file_path)
    """
    with open(filename, 'r') as file:
        sql_commands = file.read().split(';')
        conn = get_db_connection()
        cursor = conn.cursor()
        for command in sql_commands:
            if command.strip() != '':
                cursor.execute(command)
        conn.commit()
        cursor.close()
        conn.close()

# def insert(table_name, params):
#     """
#     table_name = "users"
#     params = ("some_wallet_address", "John Doe", 0)
#     insert(table_name, params)
#     """
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     # Get the insert query for the given table name
#     query = INSERT_QUERIES.get(table_name)
#     if not query:
#         raise ValueError(f"No insert query found for table: {table_name}")

#     cursor.execute(query, params)
#     connection.commit()

#     cursor.close()
#     connection.close()    

def insert(table_name, data):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    columns = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    # print(query)
    
    try:
        cursor.execute(query, values)
        connection.commit()
        result = {"status": "success", "message": f"Data inserted into {table_name}"}
    except Exception as e:
        result = {"status": "error", "message": str(e)}
    finally:
        cursor.close()
        connection.close()

    return result

def select(table_name, columns=None, where_column=None, where_value=None):
    """Usage examples: 

    user_data = select("users", where_column="wallet_address", where_value="some_wallet_address")
    print(user_data)
      
    users_data = select("users", columns=["name", "reward_points"])
    print(users_data)
      
    products_data = select("products")
    print(products_data)"""

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # dictionary=True will return results as dictionaries

    # If no columns provided, select all columns
    if not columns:
        select_columns = "*"
    else:
        select_columns = ", ".join(columns)

    query = f"SELECT {select_columns} FROM {table_name}"

    # If where conditions are provided, append them to the query
    if where_column and where_value:
        query += f" WHERE {where_column}=%s"
        cursor.execute(query, (where_value,))
    else:
        cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results   