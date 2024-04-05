from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # SQLite database file path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for better performance

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Product model after initializing db
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    # Fetch all products from the database
    products = Product.query.all()
    product_list = [{
        'id': product.id,
        'productName': product.productName,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity
    } for product in products]
    return render_template('index.html', products=product_list)

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{
        'id': product.id,
        'productName': product.productName,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity
    } for product in products]
    return jsonify(product_list)

# Route to fetch a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        product_data = {
            'id': product.id,
            'productName': product.productName,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity
        }
        return jsonify(product_data), 200
    return jsonify({'message': 'Product not found'}), 404

# Route to add a product
@app.route('/products', methods=['POST'])
def add_product():
    product_name = request.json['productName']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']
    
    new_product = Product(productName=product_name, description=description, price=price, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()

    return 'Product added successfully', 200

# Route to update a product by ID
@app.route('/products/<int:product_id>/update', methods=['POST'])
def update_product(product_id):
    data = request.json
    product = Product.query.get(product_id)
    if product:
        product.productName = data.get('productName', product.productName)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.quantity = data.get('quantity', product.quantity)
        db.session.commit()
        return jsonify({
            'id': product.id,
            'productName': product.productName,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity
        }), 200
    return jsonify({'message': 'Product not found'}), 404

# Route to delete a product by ID
@app.route('/products/<int:product_id>/delete', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return 'Product deleted successfully', 200
    return 'Product not found', 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001, debug=True)

