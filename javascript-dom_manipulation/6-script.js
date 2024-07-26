// URL to fetch the character data
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Select the element with id character
const characterElement = document.getElementById('character');

// Fetch the character data using the Fetch API
fetch(url)
  .then(response => response.json())
  .then(data => {
    // Update the text content of the character element with the character's name
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching the character data:', error);
  });
