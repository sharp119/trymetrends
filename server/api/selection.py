from flask import Blueprint, request, jsonify
from database.db_utils import select

selection = Blueprint('selection', __name__)

@selection.route('/select/<table_name>', methods=['GET'])
def select_data(table_name):
    params = request.json
    columns = params.get('columns', None)  # Default to None if 'columns' key is not provided
    where_column = params.get('where_column', None)
    where_value = params.get('where_value', None)

    try:
        data = select(table_name, columns=columns, where_column=where_column, where_value=where_value)
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        print({"status": "error", "message": str(e)})
        return jsonify({"status": "error", "message": "Internal error"})