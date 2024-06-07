document.addEventListener("DOMContentLoaded", function () {
    let movies = [
     {'title': 'Barbie', 'genre': 'Comedy', 'actor': 'Margot Robbie', 'image':'barbie-p1599238.jpg'},
     {'title': 'The Super Mario Bros. Movie', 'genre': 'Animation', 'actor': 'Chris Pratt', 'image': 'the_super_mario_bros_movie-p1460781.jpg'},
     {'title': 'Across the Spider-Verse', 'genre': 'Animation', 'actor': 'Oscar Isaac', 'image': 'spider_man_across_the_spider_verse-p1597805.jpg'},
     {'title': 'Guardians of the Galaxy Vol. 3', 'genre':'Action', 'actor': 'Chris Pratt', 'image': 'guardians_of_the_galaxy_vol_3-p1530629.jpg'}, 
     {'title': 'Oppenheimer', 'genre': 'Drama', 'actor': 'Robert Downey Jr.', 'image': 'oppenheimer-p1598268.jpg'},
     {'title': 'Priscilla', 'genre': 'Musical', 'actor': 'Jacob Elordi', 'image':'priscilla-p1611369.jpg'}
    
    ];

    // Sample questions
    const questions = [
        { question: 'Do you enjoy watching action movies?', genre: 'Action', actor: 'Chris Pratt', answer: 'Yes'  },
        { question: 'Are you a fan of romantic films?', genre: 'Romance', actor: 'Margot Robbie', answer: 'Yes'  },
        { question: 'Do you like science fiction movies?', genre: 'Sci-Fi', actor: 'Chris Pratt', answer: 'Yes'  },
        { question: 'Are you interested in historical or period dramas?', actor: 'Robert Downey Jr.', genre: 'Drama', answer: 'Yes'  },
        { question: 'Do you enjoy watching animated or animated films?', genre: 'Animation', actor: 'Chris Pratt', answer: 'Yes'  },
        { question: 'Do you prefer comedy films?', genre: 'Comedy', actor: 'Margot Robbie', answer: 'Yes'  },
        { question: 'Are you a fan of Margot Robbie?', genre: 'Comedy', actor: 'Margot Robbie', answer: 'Yes'  },
        { question: 'Do you enjoy watching crime or thriller movies?', genre: 'Crime/Thriller', actor: 'Robert Downey Jr.', answer: 'Yes'  },
        { question: 'Are you a fan of fantasy films?', genre: 'Fantasy', actor: 'Chris Pratt', answer: 'Yes'  },
        { question: 'Do you enjoy watching movies based on true stories or events?', genre: 'Based on True Stories', actor: 'Robert Downey Jr.', answer: 'Yes'  }
    ];

    // Declare these variables outside the askQuestion function to make them accessible across calls
    let yesButton, noButton;

    function askQuestion() {
        const question = questions.shift(); // Get the next question from the array

        if (question) {
            const quizContainer = document.getElementById('quiz-container');
            const questionText = document.getElementById('question-text');



            // Display the question on the page
            questionText.textContent = question.question;

            // Create Yes and No buttons dynamically
            quizContainer.innerHTML = `
                <button id="yes-btn">Yes</button>
                <button id="no-btn">No</button>
            `;

            // Remove existing event listeners before attaching new ones
            if (yesButton) {
                yesButton.removeEventListener('click', yesButtonClickHandler);
            }

            if (noButton) {
                noButton.removeEventListener('click', noButtonClickHandler);
            }

            // Attach event listeners to the buttons
            yesButton = document.getElementById('yes-btn');
            noButton = document.getElementById('no-btn');

            yesButton.addEventListener('click', yesButtonClickHandler);
            noButton.addEventListener('click', noButtonClickHandler);
        } else {
            displaySuggestions();
        }
    }

    function displaySuggestions() {
        const resultContainer = document.getElementById('result-container');

        // Display recommended movies on the page
        resultContainer.innerHTML = '<h2>Recommended Movies:</h2>';
        if (movies.length > 0) {
            const recommendedMovie = movies[0];
            resultContainer.innerHTML += `
                <div>
                    <img src="${recommendedMovie.image}" alt="${recommendedMovie.title}">
                    <p>${recommendedMovie.title} (${recommendedMovie.genre})</p>
                </div>`;
        } else {
            resultContainer.innerHTML += '<p>No matching movies found.</p>';
        }
    }

    // Function to filter movies based on answers
    function answerQuestion(answer) {
        const question = questions[0];

        if (answer === question.answer) {
            // Filter movies based on additional conditions
            movies = movies.filter(movie => movie.actor === question.actor);
            movies = movies.filter(movie => movie.genre === question.genre);
        }

        // Ask the next question or display suggestions
        askQuestion();
    }

    // Event handler functions
    function yesButtonClickHandler() {
        console.log('Yes button clicked!');
        answerQuestion('Yes');
    }
    
    function noButtonClickHandler() {
        console.log('No button clicked!');
        answerQuestion('No');
    }

    // Start the questionnaire
    askQuestion();
});
