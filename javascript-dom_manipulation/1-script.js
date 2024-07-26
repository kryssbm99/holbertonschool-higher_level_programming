// Select the header element
const header = document.querySelector('header');

// Select the element with id red_header
const redHeader = document.getElementById('red_header');

// Add a click event listener to the red_header element
redHeader.addEventListener('click', () => {
  // Update the text color of the header element to red
  header.style.color = '#FF0000';
});
