from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Read items from the JSON file
    with open('items.json', 'r') as f:
        data = json.load(f)
    items = data.get('items', [])

    # Render the items.html template with the list of items
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        file_path = 'products.json'
        products = read_json_file(file_path)
    elif source == 'csv':
        file_path = 'products.csv'
        products = read_csv_file(file_path)
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
