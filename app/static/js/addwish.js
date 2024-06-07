document.addEventListener('DOMContentLoaded', function() {
    const addToTop10Btn = document.getElementById('addToWishlist');

    addToTop10Btn.addEventListener('click', function() {
        // Send a request to Flask route to add movie to user's top 10
        fetch('/add_to_wishlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ movieId: 615 }) // Hardcoded movie ID for now
        })
        .then(response => response.json())
        .then(data => {
            // Handle response if needed
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });


    
});