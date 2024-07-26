// Select the header element
const header = document.querySelector('header');

// Select the element with id toggle_header
const toggleHeader = document.getElementById('toggle_header');

// Add a click event listener to the toggle_header element
toggleHeader.addEventListener('click', () => {
  // Check the current class of the header and toggle it
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
