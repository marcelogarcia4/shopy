# Shopify Product Viewer

This is a simple web application that allows users to view product details from a Shopify store by providing the store's domain and the product's handle. The application consists of a Python Flask backend that fetches data from the [Shopify Product Scraper API on RapidAPI](https://rapidapi.com/restyler/api/shopify-product-scraper-fast-easy-reliable) and a basic HTML/JS/CSS frontend to display the information.

## Project Structure

```
/shopify-product-viewer/
├── backend/
│   ├── main.py           # Flask application and API endpoint
│   └── shopify_api.py    # Logic to call the RapidAPI
├── frontend/
│   ├── index.html        # Main HTML page for user interface
│   ├── app.js            # JavaScript for frontend logic (API calls, DOM manipulation)
│   └── styles.css        # CSS for styling the frontend
└── README.md             # This file
```

## Prerequisites

*   Python 3.x
*   pip (Python package installer)
*   A web browser

## Setup and Running the Application

1.  **Clone the repository (or create the files as described).**

2.  **Navigate to the project directory:**
    ```bash
    cd shopify-product-viewer
    ```

3.  **Install backend dependencies:**
    Open a terminal in the `shopify-product-viewer` directory and run:
    ```bash
    pip install flask requests flask-cors
    ```
    *(Note: `flask-cors` is used to allow cross-origin requests from the frontend to the backend during local development).*

4.  **Configure API Key (Optional but Recommended):**
    The RapidAPI key is currently hardcoded in `backend/shopify_api.py`. For better practice, you might want to set it as an environment variable and modify `shopify_api.py` to read `os.environ.get('RAPIDAPI_KEY')`. The key provided in the prompt is: `093b140645mshf84fbacd52761f8p10f316jsnb07679229d97`.

5.  **Run the backend server:**
    In the same terminal (from the `shopify-product-viewer` directory), run:
    ```bash
    python backend/main.py
    ```
    The backend server will start, typically on `http://localhost:5000`. You should see output indicating the server is running.

6.  **Open the frontend:**
    Open the `frontend/index.html` file directly in your web browser.
    *   You can usually do this by navigating to the `shopify-product-viewer/frontend/` directory in your file explorer and double-clicking `index.html`.
    *   Or, use your browser's "Open File" option (Ctrl+O or Cmd+O).

## How to Use

1.  Once `index.html` is open in your browser, you will see two input fields:
    *   **Store Domain:** Enter the Shopify store's domain (e.g., `loom.fr`).
    *   **Product Handle:** Enter the product's handle (e.g., `le-t-shirt-coton-bio-homme`).
2.  Click the "Get Product Info" button.
3.  The product's title, image, price, and a link to the original product page will be displayed below the form.
4.  If the product is not found or an error occurs, a message will be shown.

## Example Backend API Call

The backend exposes a `/product` endpoint. You can test it directly (once the backend server is running) by navigating to a URL like this in your browser or using a tool like `curl`:

`http://localhost:5000/product?store=loom.fr&handle=le-t-shirt-coton-bio-homme`

This should return a JSON response with the product details.
```
