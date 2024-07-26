// Select the ul element with the class my_list
const myList = document.querySelector('.my_list');

// Select the element with id add_item
const addItem = document.getElementById('add_item');

// Add a click event listener to the add_item element
addItem.addEventListener('click', () => {
  // Create a new li element
  const newItem = document.createElement('li');
  
  // Set the text content of the new li element
  newItem.textContent = 'Item';
  
  // Append the new li element to the ul element
  myList.appendChild(newItem);
});
