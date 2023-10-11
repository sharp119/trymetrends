from db_utils import execute_queries_from_file
# from .db_utils import execute_queries_from_file

# from db_connector import get_db_connection


# def execute_queries_from_file(filename):
#     """
#     executes sql queries from specified path sql file
#     sql_file_path = "database/queries.sql"
#     execute_queries_from_file(sql_file_path)
#     """
#     with open(filename, 'r') as file:
#         sql_commands = file.read().split(';')
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         for command in sql_commands:
#             if command.strip() != '':
#                 cursor.execute(command)
#         conn.commit()
#         cursor.close()
#         conn.close()

filename = "queries/db_setup.sql"

execute_queries_from_file(filename)        