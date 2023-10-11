# api/insertion.py

from flask import Blueprint, request, jsonify
from database.db_utils import insert

insertion = Blueprint('insertion', __name__)

@insertion.route('/insert/<table_name>', methods=['POST'])
def insert_data(table_name):
    data = request.json
    # print(data)
    # params = tuple(data.values())
    try:
        flag = insert(table_name, data)
        if flag["status"] != "error":
            return jsonify({"status": "success", "message": f"Data inserted successfully into {table_name}"})
        else:
            print(flag)
            raise
    except Exception as e:
        print({"status": "error", "message": str(e)})
        return jsonify({"status": "error", "message": "Internal error"})
