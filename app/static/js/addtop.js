document.addEventListener('DOMContentLoaded', function() {
    const movieContainer = document.querySelector('.movie-container');
    const movieId = movieContainer.getAttribute('data-movie-id'); // Correctly retrieving the movie ID

    const addToTop10Btn = document.getElementById('addToTop10');
    const addToWishlistBtn = document.getElementById('addToWishlist');
    const addToTop5Btn = document.getElementById('addToTop5')

    addToTop10Btn.addEventListener('click', function() {
        fetch('/add_to_top_10', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({ movieId: movieId }), // Using movieId in the request
            credentials: 'include',
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                alert('Movie has been added to your top 10!');
            } else {
                alert('Failed to add movie to top 10.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    addToWishlistBtn.addEventListener('click', function() {
        fetch('/add_to_wishlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({ movieId: movieId }), // Using movieId in the request
            credentials: 'include',
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                alert('Movie has been added to your wishlist!');
            } else {
                alert('Failed to add movie to wishlist.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    addToTop5Btn.addEventListener('click', function() {
        fetch('/add_top_dir', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({ movieId: movieId }), // Using movieId in the request
            credentials: 'include',
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                alert('Director has been added to your top 5!');
            } else {
                alert('Failed to add Director.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

    // Submitting Ratings with Alert
    document.addEventListener('DOMContentLoaded', function() {
        const movieContainer = document.querySelector('.movie-container');
        const movieId = movieContainer.getAttribute('data-movie-id'); // Retrieve the movie ID
    
        const ratingForm = document.getElementById('ratingForm');
    
        ratingForm.addEventListener('submit', function(e) {
            e.preventDefault();
    
            const formData = new FormData(ratingForm);
            const rating = formData.get('rating');
    
            fetch(`/rate_movie/${movieId}`, { // Use the correct movie ID in the URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({ rating: rating }),
                credentials: 'include'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Rating submitted successfully!');
                    // Optionally, update the displayed average rating
                    // Note: Implement logic on the server to calculate and return the new average
                    document.getElementById('averageRating').textContent = `Average Rating: ${data.new_average ? data.new_average : 'Updated'}`;
                } else {
                    alert('Failed to submit rating. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Failed to submit rating. Please try again.');
            });
        });
    });



    
    window.addEventListener('DOMContentLoaded', (event) => {
        const movieId = document.querySelector('.movie-container').getAttribute('data-movie-id');
        fetch(`/api/cast/${movieId}`)
            .then(response => response.json())
            .then(data => {
                const castContainer = document.getElementById('cast-container');
                castContainer.innerHTML = '<h2>Cast</h2>'; // Optionally add a header
                data.forEach(({image_id, name}) => {
                    const castMemberDiv = document.createElement('div');
                    castMemberDiv.className = 'cast-member';
                    castMemberDiv.innerHTML = `
                        <div class="cast-image-container">
                            <img src="/static/cast_images/${image_id}.jpg" alt="${name}">
                        </div>
                        <div class="cast-name">${name}</div>
                    `;
                    castContainer.appendChild(castMemberDiv);
                });
            })
            .catch(error => console.error('Error fetching cast details:', error));
    });

    window.addEventListener('DOMContentLoaded', (event) => {
        const movieId = document.querySelector('.movie-container').getAttribute('data-movie-id');
        fetch(`/api/director/${movieId}`)
            .then(response => response.json())
            .then(data => {
                const directorContainer = document.getElementById('director-container');
                directorContainer.innerHTML = '<h2>Director</h2>'; // Optionally add a header
                data.forEach(({image_id, name}) => {
                    const directorMemberDiv = document.createElement('div');
                    directorMemberDiv.className = 'director-member';
                    directorMemberDiv.innerHTML = `
                        <div class="director-image-container">
                            <img src="/static/director_images/${image_id}.jpg" alt="${name}">
                        </div>
                        <div class="director-name">${name}</div>
                    `;
                    directorContainer.appendChild(directorMemberDiv);
                });
            })
            .catch(error => console.error('Error fetching director details:', error));
    });

    
    
    
