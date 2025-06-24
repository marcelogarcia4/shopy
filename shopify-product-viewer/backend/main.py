from flask import Flask, request, jsonify
from flask_cors import CORS
from shopify_api import get_product_details

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/product', methods=['GET'])
def product_route():
    store = request.args.get('store')
    handle = request.args.get('handle')

    if not store or not handle:
        return jsonify({"error": "Missing 'store' or 'handle' query parameters"}), 400

    product_info = get_product_details(store, handle)

    if product_info:
        return jsonify(product_info), 200
    else:
        return jsonify({"error": "Product not found or unable to retrieve details"}), 404

if __name__ == '__main__':
    # Note: For development, Flask's built-in server is fine.
    # For production, use a WSGI server like Gunicorn or uWSGI.
    app.run(debug=True, port=5000)
