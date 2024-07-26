// URL to fetch the "hello" translation
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Function to fetch and display the "hello" translation
const fetchHello = () => {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      // Select the element with id hello
      const helloElement = document.getElementById('hello');
      // Update the text content of the hello element with the translation
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching the hello translation:', error);
    });
};

// Ensure the script runs when imported from the <head> tag
document.addEventListener('DOMContentLoaded', fetchHello);
