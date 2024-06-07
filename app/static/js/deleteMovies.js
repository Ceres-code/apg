document.addEventListener('DOMContentLoaded', function() {
    // Function to extract movie ID from image filename
    function getMovieIdFromImageName(imageSrc) {
        // Split the image filename by "/" to get the last part which contains the movie ID
        const filenameParts = imageSrc.split('/');
        // Get the last part of the filename
        const filename = filenameParts[filenameParts.length - 1];
        // Remove the file extension to get the movie ID
        const movieId = filename.split('.')[0];
        return movieId;
    }

    // Get all movie elements
    const movieElements = document.querySelectorAll('.movie');

    // Loop through each movie element
    movieElements.forEach(movieElement => {
        // Get the movie image element
        const movieImage = movieElement.querySelector('img');
        // Get the movie ID from the image filename
        const movieId = getMovieIdFromImageName(movieImage.src);
        // Set the movie ID as a data attribute on the movie element
        movieElement.dataset.movieId = movieId;
    });

    // Function to toggle delete mode
    function toggleDeleteMode() {
        movieElements.forEach(movieElement => {
            if (deleteModeEnabled) {
                // Add click event listener to delete movies
                movieElement.addEventListener('click', deleteMovie);
                // Highlight movie element (optional)
                movieElement.style.border = '2px solid red';
            } else {
                // Remove click event listener
                movieElement.removeEventListener('click', deleteMovie);
                // Remove highlight (optional)
                movieElement.style.border = 'none';
            }
        });

        // Toggle visibility of edit and done buttons
        editButton.style.display = deleteModeEnabled ? 'none' : 'block';
        doneButton.style.display = deleteModeEnabled ? 'block' : 'none';
    }

    // Function to delete a movie
    function deleteMovie(event) {
        // Get the movie element
        const movieElement = event.target.closest('.movie');
        if (movieElement) {
            // Get the movie ID from the movie element's data attribute
            const movieId = movieElement.dataset.movieId;

            // Remove the movie element from the DOM
            movieElement.remove();

            // Send a request to Flask to delete the movie from the database
            fetch('/delete_movie', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ movieId: movieId })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }

    // Get edit and done buttons
    const editButton = document.getElementById('editButton');
    const doneButton = document.getElementById('doneButton');

    // Flag to track delete mode state
    let deleteModeEnabled = false;

    // Toggle delete mode when edit button is clicked
    editButton.addEventListener('click', function() {
        deleteModeEnabled = true;
        toggleDeleteMode();
    });

    // Toggle delete mode when done button is clicked
    doneButton.addEventListener('click', function() {
        deleteModeEnabled = false;
        toggleDeleteMode();
    });
});
