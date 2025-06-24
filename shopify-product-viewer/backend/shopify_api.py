import requests
import os

# It's good practice to use environment variables for API keys,
# but for this exercise, we'll use the one provided in the prompt.
# For a real application, consider using os.environ.get('RAPIDAPI_KEY')
RAPIDAPI_KEY = "093b140645mshf84fbacd52761f8p10f316jsnb07679229d97" # Replace with your actual key if needed
RAPIDAPI_HOST = "shopify-product-scraper-fast-easy-reliable.p.rapidapi.com"
API_URL = f"https://{RAPIDAPI_HOST}/product"

def get_product_details(store: str, handle: str) -> dict | None:
    """
    Fetches product details from the Shopify product scraper API.

    Args:
        store: The store domain (e.g., "loom.fr").
        handle: The product handle (e.g., "le-t-shirt-coton-bio-homme").

    Returns:
        A dictionary containing product 'title', 'price', 'image', and 'link'
        if found, otherwise None.
    """
    if not store or not handle:
        return None

    querystring = {"store": store, "handle": handle}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }

    try:
        response = requests.get(API_URL, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)

        data = response.json()

        # According to the example, the API returns a list of products,
        # even if it's just one. We'll assume we need the first item if available.
        if isinstance(data, list) and len(data) > 0:
            product_data = data[0]
        elif isinstance(data, dict) and 'title' in data : # sometimes it returns a dict directly
             product_data = data
        else: # No product found or unexpected format
            print(f"No product data found or unexpected format for {store}/{handle}. Response: {data}")
            return None

        # Extract the required fields
        # The exact field names might vary, adjust based on actual API response structure
        # Based on typical Shopify structures and the prompt's requirements:
        title = product_data.get("title")

        # Price: Often nested, e.g., in variants or priceRange.
        # For simplicity, let's assume a top-level 'price' or check common structures.
        # This will need verification with an actual API response.
        price = None
        if "price" in product_data:
            price = product_data["price"]
        elif "variants" in product_data and len(product_data["variants"]) > 0:
            price = product_data["variants"][0].get("price")
        elif "priceRange" in product_data: # Example from a different Shopify API
             price = product_data["priceRange"]["minVariantPrice"]["amount"]


        # Image: Usually an object with a 'src' field.
        image_src = None
        if "image" in product_data and isinstance(product_data["image"], dict):
            image_src = product_data["image"].get("src")
        elif "images" in product_data and len(product_data["images"]) > 0:
             image_src = product_data["images"][0].get("src")


        # Link: Construct from store and handle if not directly provided.
        # A direct 'product_url' or 'onlineStoreUrl' might be available.
        link = product_data.get("product_url") or product_data.get("onlineStoreUrl")
        if not link:
            link = f"https://{store}/products/{handle}"


        if title and price and image_src:
            return {
                "title": title,
                "price": str(price), # Ensure price is a string
                "image": image_src,
                "link": link
            }
        else:
            print(f"Missing essential product details for {store}/{handle}. Data: {product_data}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"API request failed for {store}/{handle}: {e}")
        return None
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error parsing product data for {store}/{handle}: {e}. Data: {data if 'data' in locals() else 'N/A'}")
        return None

if __name__ == '__main__':
    # Example usage for testing
    test_store = "loom.fr"
    test_handle = "le-t-shirt-coton-bio-homme"
    product_info = get_product_details(test_store, test_handle)
    if product_info:
        print("Product Found:")
        print(f"  Title: {product_info['title']}")
        print(f"  Price: {product_info['price']}")
        print(f"  Image URL: {product_info['image']}")
        print(f"  Link: {product_info['link']}")
    else:
        print(f"Product not found or error fetching details for {test_store}/{test_handle}")

    test_store_goth = "gothiclamb" # Example that might not work or has different structure
    test_handle_goth = "dreamer-hoodie"
    product_info_goth = get_product_details(test_store_goth, test_handle_goth)
    if product_info_goth:
        print("\nProduct Found (Gothic Lamb):")
        print(f"  Title: {product_info_goth['title']}")
        print(f"  Price: {product_info_goth['price']}")
        print(f"  Image URL: {product_info_goth['image']}")
        print(f"  Link: {product_info_goth['link']}")
    else:
        print(f"\nProduct not found or error fetching details for {test_store_goth}/{test_handle_goth}")
