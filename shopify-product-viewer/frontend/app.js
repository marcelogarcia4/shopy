document.addEventListener('DOMContentLoaded', () => {
    const productForm = document.getElementById('product-form');
    const storeInput = document.getElementById('store-input');
    const handleInput = document.getElementById('handle-input');
    const messageArea = document.getElementById('message-area');

    const productInfoDiv = document.getElementById('product-info');
    const productTitle = document.getElementById('product-title');
    const productImage = document.getElementById('product-image');
    const productPrice = document.getElementById('product-price');
    const productLink = document.getElementById('product-link');

    productForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        const store = storeInput.value.trim();
        const handle = handleInput.value.trim();

        if (!store || !handle) {
            showMessage('Please enter both store and product handle.', 'error');
            return;
        }

        showMessage('Fetching product information...', 'loading');
        productInfoDiv.style.display = 'none'; // Hide previous results
        productImage.style.display = 'none';


        // Assuming the backend is running on http://localhost:5000
        const backendUrl = `http://localhost:5000/product?store=${encodeURIComponent(store)}&handle=${encodeURIComponent(handle)}`;

        try {
            const response = await fetch(backendUrl);
            const data = await response.json();

            if (response.ok) {
                productTitle.textContent = data.title;
                productPrice.textContent = `Price: ${data.price}`;

                if (data.image) {
                    productImage.src = data.image;
                    productImage.alt = data.title; // Set alt text
                    productImage.style.display = 'block';
                } else {
                    productImage.style.display = 'none';
                }

                productLink.href = data.link;
                productLink.textContent = `View "${data.title}" in store`;

                productInfoDiv.style.display = 'block';
                messageArea.textContent = ''; // Clear loading/error message
                messageArea.className = 'message'; // Reset class
            } else {
                // Handle errors from the backend (e.g., 404 Not Found, 400 Bad Request)
                const errorMessage = data.error || 'Product not found or an error occurred.';
                showMessage(errorMessage, 'error');
                productInfoDiv.style.display = 'none';
            }
        } catch (error) {
            // Handle network errors or other fetch issues
            console.error('Fetch error:', error);
            showMessage('Failed to connect to the backend. Make sure it is running.', 'error');
            productInfoDiv.style.display = 'none';
        }
    });

    function showMessage(message, type = 'info') {
        messageArea.textContent = message;
        messageArea.className = 'message'; // Reset
        if (type === 'error') {
            messageArea.classList.add('error');
        } else if (type === 'success') {
            messageArea.classList.add('success');
        } else if (type === 'loading') {
            messageArea.classList.add('loading');
        }
    }
});
