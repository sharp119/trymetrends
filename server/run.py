# from flask import Flask, render_template, request, jsonify
# import mysql.connector

# app = Flask(__name__)

# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="solana_auth"
#     )

# @app.route('/')
# def login():
#     return render_template('login.html')


# @app.route('/verify-address', methods=['POST'])
# def verify_address():
#     address = request.json['address']
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users WHERE address=%s", (address,))
#     user = cursor.fetchone()
#     cursor.close()
#     conn.close()

#     if user:
#         return jsonify(status="Logged In")
#     else:
#         return jsonify(status="Not Registered")

# @app.route('/register', methods=['POST'])
# def register():
#     username = request.json['username']
#     shop_name = request.json['shop_name']
#     address = request.json['address']

#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users(username, shop_name, address) VALUES(%s, %s, %s)", (username, shop_name, address))
#     conn.commit()
#     cursor.close()
#     conn.close()

#     return jsonify(status="Registered Successfully")

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
from api.insertion import insertion
from api.selection import selection

app = Flask(__name__)

app.register_blueprint(insertion)
app.register_blueprint(selection)

@app.route('/')
def login():
    return render_template('login.html')




if __name__ == "__main__":
    app.run(debug=True)
