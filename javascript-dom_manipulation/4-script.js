document.querySelector('#add_item').addEventListener('click', () => {
  document.querySelector('.my_list li').insertAdjacentHTML(
    'beforeend',
    '<li>Item</li>'
  );
});
