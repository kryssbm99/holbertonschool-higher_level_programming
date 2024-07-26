// Select the header element
const header = document.querySelector('header');

// Select the element with id update_header
const updateHeader = document.getElementById('update_header');

// Add a click event listener to the update_header element
updateHeader.addEventListener('click', () => {
  // Update the text content of the header element
  header.textContent = 'New Header!!!';
});
