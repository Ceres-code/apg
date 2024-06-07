console.log("Script is running");

document.addEventListener("DOMContentLoaded", function() {
    let movies = [
        {'title': 'Barbie', 'genre': 'Comedy', 'actor': 'Margot Robbie', 'image':'barbie-p1599238.jpg'}, {'title': 'The Super Mario Bros. Movie'}, {'title': 'Across the Spider-Verse'}, {'title': 'Guardians of the Galaxy Vol. 3'}, {'title': 'Oppenheimer'}, {'title': 'The Little Mermaid'}, {'title': 'Wonka'}, {'title': 'Quantumania'}, {'title': 'Chapter 4'}, {'title': 'Sound of Freedom'}, {'title': 'M3GAN'}, {'title': 'The Old Way'}, {'title': 'The Devil Conspiracy'}, {'title': 'Plane'}, {'title': 'House Party'}, {'title': 'Sick'}, {'title': 'The Drop'}, {'title': 'Dog Gone'}, {'title': "There's Something Wrong with the Children"}, {'title': 'Missing'}, {'title': 'The Son'}, {'title': 'When You Finish Saving the World'}, {'title': 'Independence'}, {'title': 'Kids vs. Aliens'}, {'title': 'The Movie'}, {'title': 'You People'}, {'title': 'Shotgun Wedding'}, {'title': 'Maybe I Do'}, {'title': 'Life Upside Down'}, {'title': 'Fear'}, {'title': 'Knock at the Cabin'}, {'title': '80 for Brady'}, {'title': 'The Locksmith'}, {'title': 'Baby Ruby'}, {'title': "Freedom's Path"}, {'title': 'The Wedding Hustler'}, {'title': "Magic Mike's Last Dance"}, {'title': 'Sharper'}, {'title': 'Your Place or Mine'}, {'title': 'Somebody I Used to Know'}, {'title': 'Consecration'}, {'title': 'The Outwaters'}, {'title': 'Quantumania'}, {'title': 'Cocaine Bear'}, {'title': 'We Have a Ghost'}, {'title': 'The Fallen Sun'}, {'title': 'Jesus Revolution'}, {'title': 'Bruiser'}, {'title': 'Linoleum'}, {'title': 'Creed III'}, {'title': 'Ruse de Guerre'}, {'title': 'A Little White Lie'}, {'title': 'Children of the Corn'}, {'title': 'Palm Trees and Power Lines'}, {'title': 'The Year Between'}, {'title': 'Unseen'}, {'title': 'Craving'}, {'title': 'Scream VI'}, {'title': '65'}, {'title': 'Champions'}, {'title': 'Chang Can Dunk'}, {'title': 'Shazam! Fury of the Gods'}, {'title': 'Boston Strangler'}, {'title': "The Magician's Elephant"}, {'title': 'Moving On'}, {'title': 'Wildflower'}, {'title': 'Supercell'}, {'title': 'The Man Who Saved the Game'}, {'title': 'Chapter 4'}, {'title': 'A Good Person'}, {'title': 'The Tutor'}, {'title': 'Adalynn'}, {'title': 'Honor Among Thieves'}, {'title': 'Murder Mystery 2'}, {'title': 'Tetris'}, {'title': 'Spinning Gold'}, {'title': 'Space Oddity'}, {'title': 'A Thousand and One'}, {'title': 'Assassin'}, {'title': 'Acidman'}, {'title': 'Malum'}, {'title': 'Miracle at Manchester'}, {'title': 'The Super Mario Bros. Movie'}, {'title': 'Air'}, {'title': 'Praise This'}, {'title': 'Showing Up'}, {'title': 'Paint'}, {'title': 'On a Wing and a Prayer'}, {'title': 'Chupa'}, {'title': 'How to Blow Up a Pipeline'}, {'title': 'One True Loves'}, {'title': 'Beautiful Disaster'}, {'title': 'Renfield'}, {'title': 'Beau Is Afraid'}, {'title': "The Pope's Exorcist"}, {'title': 'Mafia Mamma'}, {'title': 'Sweetwater'}, {'title': 'Nefarious'}, {'title': 'Quasi'}, {'title': 'Evil Dead Rise'}, {'title': "Guy Ritchie's The Covenant"}, {'title': 'Ghosted'}, {'title': 'Chevalier'}, {'title': 'Somewhere in Queens'}, {'title': 'Carmen'}, {'title': "A Tourist's Guide to Love"}, {'title': 'The Artifice Girl'}, {'title': 'Peter Pan & Wendy'}, {'title': "Are You There God? It's Me, Margaret."}, {'title': 'Big George Foreman'}, {'title': 'Sisu'}, {'title': 'Clock'}, {'title': 'Guardians of the Galaxy Vol. 3'}, {'title': 'Love Again'}, {'title': 'The Next Chapter'}, {'title': 'The Mother'}, {'title': "Fool's Paradise"}, {'title': 'Hypnotic'}, {'title': 'Crater'}, {'title': 'Knights of the Zodiac'}, {'title': 'Monica'}, {'title': 'The Starling Girl'}, {'title': 'Rally Road Racers'}, {'title': 'Fast X'}, {'title': "White Men Can't Jump"}, {'title': 'Master Gardener'}, {'title': 'Sanctuary'}, {'title': 'Robots'}, {'title': 'Moon Garden'}, {'title': 'The Little Mermaid'}, {'title': 'About My Father'}, {'title': 'Kandahar'}, {'title': 'The Machine'}, {'title': 'You Hurt My Feelings'}, {'title': 'The Wrath of Becky'}, {'title': 'Reality'}, {'title': 'Across the Spider-Verse'}, {'title': 'The Boogeyman'}, {'title': 'Past Lives'}, {'title': 'Shooting Stars'}, {'title': 'Rise of the Beasts'}, {'title': "Flamin' Hot"}, {'title': 'Dalíland'}, {'title': 'Jagged Mind'}, {'title': 'The Flash'}, {'title': 'Elemental'}, {'title': 'Asteroid City'}, {'title': 'Extraction 2'}, {'title': 'The Blackening'}, {'title': 'Surrounded'}, {'title': 'No Hard Feelings'}, {'title': 'The Perfect Find'}, {'title': "World's Best"}, {'title': 'God Is a Bullet'}, {'title': 'Wonderwell'}, {'title': 'Indiana Jones and the Dial of Destiny'}, {'title': 'Ruby Gillman, Teenage Kraken'}, {'title': 'Nimona'}, {'title': 'Confidential Informant'}, {'title': "Prisoner's Daughter"}, {'title': 'Sound of Freedom'}, {'title': 'The Red Door'}, {'title': 'Joy Ride'}, {'title': 'The Out-Laws'}, {'title': 'Earth Mama'}, {'title': 'Biosphere'}, {'title': 'Impossible – Dead Reckoning Part One'}, {'title': 'They Cloned Tyrone'}, {'title': 'Theater Camp'}, {'title': 'Barbie'}, {'title': 'Oppenheimer'}, {'title': 'Cobweb'}, {'title': 'The Beanie Bubble'}, {'title': 'Haunted Mansion'}, {'title': 'Sympathy for the Devil'}, {'title': 'Circus Maximus'}, {'title': 'Happiness for Beginners'}, {'title': 'War Pony'}, {'title': 'The Unknown Country'}, {'title': 'The Disappearance of Nick Brandreth'}, {'title': 'Mutant Mayhem'}, {'title': 'Mike & Fred vs The Dead'}, {'title': 'The Trench'}, {'title': 'Shortcomings'}, {'title': "Dreamin' Wild"}, {'title': 'Corner Office'}, {'title': 'What Comes Around'}, {'title': 'The Passenger'}, {'title': 'The Last Voyage of the Demeter'}, {'title': 'Heart of Stone'}, {'title': 'Red, White & Royal Blue'}, {'title': 'Jules'}, {'title': 'Inside Man'}, {'title': 'Blue Beetle'}, {'title': 'Strays'}, {'title': 'The Monkey King'}, {'title': 'Landscape with Invisible Hand'}, {'title': 'Back on the Strip'}, {'title': 'The Adults'}, {'title': 'Gran Turismo'}, {'title': 'Retribution'}, {'title': 'Vacation Friends 2'}, {'title': 'You Are So Not Invited to My Bat Mitzvah'}, {'title': 'Bottoms'}, {'title': 'Golda'}, {'title': 'The Hill'}, {'title': 'The Equalizer 3'}, {'title': 'The Good Mother'}, {'title': 'All Fun and Games'}, {'title': 'Under the Sky'}, {'title': 'The Nun II'}, {'title': 'My Big Fat Greek Wedding 3'}, {'title': 'Sitting in Bars with Cake'}, {'title': 'Aristotle and Dante Discover the Secrets of the Universe'}, {'title': 'After Everything'}, {'title': 'A Haunting in Venice'}, {'title': 'Dumb Money'}, {'title': 'Love at First Sight'}, {'title': 'A Million Miles Away'}, {'title': 'The Retirement Plan'}, {'title': 'Outlaw Johnny Black'}, {'title': 'Camp Hideout'}, {'title': 'Expend4bles'}, {'title': 'Armageddon'}, {'title': 'Reptile'}, {'title': 'Cassandro'}, {'title': 'Flora and Son'}, {'title': 'No One Will Save You'}, {'title': 'It Lives Inside'}, {'title': 'Everybody Dies by the End'}, {'title': 'The Kill Room'}, {'title': 'The Creator'}, {'title': 'Saw X'}, {'title': 'Fair Play'}, {'title': 'The Re-Education of Molly Singer'}, {'title': 'Deliver Us'}, {'title': 'Oracle'}, {'title': 'Believer'}, {'title': 'Bloodlines'}, {'title': 'Totally Killer'}, {'title': 'V/H/S/85'}, {'title': 'The Caine Mutiny Court-Martial'}, {'title': 'The Musical'}, {'title': 'Foe'}, {'title': 'She Came to Me'}, {'title': 'The Burial'}, {'title': 'Desperation Road'}, {'title': "Miranda's Victim"}, {'title': 'Cat Person'}, {'title': 'The Mill'}, {'title': 'Down Low'}, {'title': 'Dark Harvest'}, {'title': 'The Eras Tour'}, {'title': 'Dear David'}, {'title': 'Divinity'}, {'title': 'In the Fire'}, {'title': 'Killers of the Flower Moon'}, {'title': 'Pain Hustlers'}, {'title': 'Nyad'}, {'title': 'Old Dads'}, {'title': "Butcher's Crossing"}, {'title': 'The Other Zoey'}, {'title': 'Sick Girl'}, {'title': 'The Persian Version'}, {'title': "Five Nights at Freddy's"}, {'title': 'Freelance'}, {'title': 'The Killer'}, {'title': 'Under the Boardwalk'}, {'title': 'Priscilla'}, {'title': 'The Holdovers'}, {'title': 'Fingernails'}, {'title': 'Suitable Flesh'}, {'title': 'Sight'}, {'title': 'The Carmichael Manor'}, {'title': 'Quiz Lady'}, {'title': 'Rustin'}, {'title': "The Marsh King's Daughter"}, {'title': 'What Happens Later'}, {'title': 'All Dirt Roads Taste of Salt'}, {'title': "Helen's Dead"}, {'title': 'Rumble Through the Dark'}, {'title': 'The Marvels'}, {'title': 'Dream Scenario'}, {'title': 'Journey to Bethlehem'}, {'title': 'Your Lucky Day'}, {'title': "It's a Wonderful Knife"}, {'title': 'Manodrome'}, {'title': 'Part One'}, {'title': 'Best. Christmas. Ever!'}, {'title': 'The Ballad of Songbirds & Snakes'}, {'title': 'Trolls Band Together'}, {'title': 'Thanksgiving'}, {'title': 'Next Goal Wins'}, {'title': 'Saltburn'}, {'title': 'May December'}, {'title': 'Dashing Through the Snow'}, {'title': 'The Treasure of Foggy Mountain'}, {'title': 'Leo'}, {'title': 'Wish'}, {'title': 'Napoleon'}, {'title': 'Maestro'}, {'title': 'Leave the World Behind'}, {'title': 'Good Burger 2'}, {'title': 'Genie'}, {'title': 'Family Switch'}, {'title': 'A Film by Beyoncé'}, {'title': 'Silent Night'}, {'title': 'Candy Cane Lane'}, {'title': 'Eileen'}, {'title': 'The Shift'}, {'title': 'Holiday Twist'}, {'title': 'Abigail'}, {'title': 'The Musical'}, {'title': 'Poor Things'}, {'title': 'Origin'}, {'title': 'Cabin Fever'}, {'title': 'Our Son'}, {'title': 'The Cello'}, {'title': 'Craig Before the Creek'}, {'title': 'Wonka'}, {'title': 'Dawn of the Nugget'}, {'title': 'Rebel Moon'}, {'title': 'American Fiction'}, {'title': 'The Family Plan'}, {'title': 'Finestkind'}, {'title': 'The Zone of Interest'}, {'title': 'City of Love'}, {'title': 'Aquaman and the Lost Kingdom'}, {'title': 'Migration'}, {'title': 'Anyone but You'}, {'title': 'The Iron Claw'}, {'title': "Freud's Last Session"}, {'title': 'Memory'}, {'title': 'The Color Purple'}, {'title': 'The Boys in the Boat'}, {'title': 'Ferrari'}, {'title': 'Good Grief'}
    ];

    const questions = [
        { question: 'Do you enjoy watching action movies?', genre: 'Action', answer: 'Yes'  },
        { question: 'Are you a fan of romantic films?', genre: 'Romance', answer: 'Yes'  },
        { question: 'Do you like science fiction movies?', genre: 'Sci-Fi', answer: 'Yes'  },
        { question: 'Are you interested in historical or period dramas?', genre: 'Drama (Historical/Period)', answer: 'Yes'  },
        { question: 'Do you enjoy watching animated or animated films?', genre: 'Animation', answer: 'Yes'  },
        { question: 'Are you a fan of horror movies?', genre: 'Horror', answer: 'Yes'  },
        { question: 'Do you prefer comedy films?', genre: 'Comedy', actor: 'Margot Robbie', answer: 'Yes'  },
        { question: 'Are you a fan of Margot Robbie?', genre: 'Comedy', actor: 'Margot Robbie', answer: 'Yes'  },
        { question: 'Are you interested in documentaries?', genre: 'Documentary', answer: 'Yes'  },
        { question: 'Do you enjoy watching crime or thriller movies?', genre: 'Crime/Thriller', answer: 'Yes'  },
        { question: 'Are you a fan of fantasy films?', genre: 'Fantasy', answer: 'Yes'  },
        { question: 'Do you prefer watching movies in a specific language or languages?', genre: 'Language Preference', answer: 'Yes'  },
        { question: 'Are you interested in films directed by a specific director? (Specify the director\'s name)', genre: 'Director Preference', answer: 'Yes'  },
        { question: 'Do you like classic movies from the golden era of cinema?', genre: 'Classic', answer: 'Yes'  },
        { question: 'Are you a fan of independent or art-house films?', genre: 'Independent/Art-house', answer: 'Yes'  },
        { question: 'Do you enjoy watching movies based on true stories or events?', genre: 'Based on True Stories', answer: 'Yes'  }
    ];
    

    function askQuestion() {
        const question = questions[0]; // Get the current question from the array

        if (question) {
            const quizContainer = document.getElementById('quiz-container');
            const questionText = document.getElementById('question-text');

            if (!questionText) {
                console.error("Error: 'question-text' element not found.");
                return;
            }

            // Display the question on the page
            questionText.textContent = question.question;

            // Create Yes and No buttons dynamically
            quizContainer.innerHTML = `
                <button id="yes-btn" onclick="answerQuestion('Yes')">Yes</button>
                <button id="no-btn" onclick="answerQuestion('No')">No</button>
            `;
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

    function answerQuestion(answer) {
        const question = questions[0]; // Get the current question from the array

        if (answer === question.answer) {
            // Filter movies based on additional conditions
            movies = movies.filter(movie => movie.actor === question.actor);
            movies = movies.filter(movie => movie.genre === question.genre);
        }

        // Remove the current question from the array
        questions.shift();

        // Ask the next question or display suggestions
        askQuestion();
    }

    // Start the questionnaire
    askQuestion();
});
