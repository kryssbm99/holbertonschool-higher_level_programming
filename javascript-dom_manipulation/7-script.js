// URL to fetch the movie data
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Select the ul element with id list_movies
const listMovies = document.getElementById('list_movies');

// Fetch the movie data using the Fetch API
fetch(url)
  .then(response => response.json())
  .then(data => {
    // Iterate over the movies and create an li element for each title
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching the movie data:', error);
  });
