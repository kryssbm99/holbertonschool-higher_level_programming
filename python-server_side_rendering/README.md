
# Flask Dynamic Data Display

This project demonstrates a Flask application that reads and displays product data from JSON, CSV, and SQLite database sources. The application uses Jinja templates to render the data dynamically on web pages, allowing users to select the data source and filter products by ID.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Endpoints](#endpoints)
- [File Structure](#file-structure)
- [Testing](#testing)
- [Example URLs](#example-urls)
- [Resources](#resources)
- [License](#license)

## Features
- Read and display product data from JSON, CSV, and SQLite database files.
- Use query parameters to select the data source and filter products by ID.
- Dynamic data rendering using Jinja templates.
- Error handling for invalid inputs and missing data.

## Setup
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.

### Install Dependencies
Install Flask using pip:
```sh
pip install Flask
```

### Database Setup
Create and populate the SQLite database by running the following script:
```python
import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Notebook', 'Stationery', 5.49),
        (4, 'Headphones', 'Electronics', 199.99)
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
```

Run the script to create and populate the database:
```sh
python create_database.py
```

Open your web browser and navigate to `http://localhost:5000`.

## Endpoints
- `/products?source=json` - Display products from JSON file.
- `/products?source=csv` - Display products from CSV file.
- `/products?source=sql` - Display products from SQLite database.
- `/products?source=json&id=<id>` - Display a specific product by ID from JSON file.
- `/products?source=csv&id=<id>` - Display a specific product by ID from CSV file.
- `/products?source=sql&id=<id>` - Display a specific product by ID from SQLite database.

## File Structure
```
├── create_database.py        # Script to create and populate SQLite database
├── products.json             # JSON file containing product data
├── items.json                # JSON file containing items data
├── products.csv              # CSV file containing product data
├── products.db               # SQLite database file containing product data
├── task_01_jinja.py		  # Flask application for Task 1
├── task_02_logic.py          # Flask application for Task 2
├── task_03_files.py          # Flask application for Task 3
├── task_04_db.py             # Flask application for Task 4 (final)
├── templates                 # HTML templates
│   ├── header.html           # Reusable header template
│   ├── footer.html           # Reusable footer template
│   ├── index.html            # Home page template
│   ├── about.html            # About page template
│   ├── contact.html          # Contact page template
│   ├── items.html            # Template for displaying items
│   └── product_display.html  # Template for displaying products
└── README.md                 # Project documentation
```

## Testing
### Test the application with various scenarios:
1. Access URLs like `http://localhost:5000/products?source=json`, `http://localhost:5000/products?source=csv`, and `http://localhost:5000/products?source=sql`.
2. Test with and without the `id` parameter, and with both valid and invalid ID values.
3. Verify that the application correctly filters data, displays all products when no ID is provided, and shows appropriate error messages for edge cases.

## Example URLs
- `http://localhost:5000/products?source=json`
- `http://localhost:5000/products?source=csv`
- `http://localhost:5000/products?source=sql`
- `http://localhost:5000/products?source=json&id=1`
- `http://localhost:5000/products?source=csv&id=2`
- `http://localhost:5000/products?source=sql&id=3`
- `http://localhost:5000/products?source=xml` (invalid source)
- `http://localhost:5000/products?source=sql&id=999` (invalid ID)

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja Templating](https://jinja.palletsprojects.com/)
- [Python JSON Module](https://docs.python.org/3/library/json.html)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)
- [SQLite3 Module](https://docs.python.org/3/library/sqlite3.html)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

## License
This project is licensed under the MIT License. See the LICENSE file for details.
