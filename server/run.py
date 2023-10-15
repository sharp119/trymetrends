

from flask import Flask, render_template, request
from api.insertion import insertion
from api.selection import selection

app = Flask(__name__)

app.register_blueprint(insertion)
app.register_blueprint(selection)

@app.route('/')
def login():
    return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/products', methods=['GET'])
def get_products():
    # Fetch images and associated information from the database or other sources
    image1 = {
        'path': 'assests/product1/2.png.jpeg',
        'price': '$100',
        'seller': 'Seller Name 1'
    }
    image2 = {
        'path': 'assests/product1/in_origin.jpeg',
        'price': '$200',
        'seller': 'Seller Name 2'
    }
    return render_template('product.html', image1=image1, image2=image2)

@app.route('/tryon')
def tryon():
    image_type = request.args.get('image')

    image1 = {
        'path': 'assests/product1/2.png.jpeg',
        'price': '$100',
        'seller': 'Seller Name 1'
    }
    image2 = {
        'path': 'assests/product1/in_origin.jpeg',
        'price': '$200',
        'seller': 'Seller Name 2'
    }

    # Select which product to display based on image_type
    selected_image = image1 if image_type == 'image1' else image2

    return render_template('tryon.html', image=selected_image)

if __name__ == "__main__":
    app.run(debug=True)
