fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(Objet => showObjet(Objet));

function showObjet (Objet) {
  // pour voir le contenu de l'objet dans la console
  console.log(Objet);
  Objet.results.forEach(filme => {
    document.querySelector('#list_movies').insertAdjacentHTML(
      'beforeend',
      `<li>${filme.title}</li>`
    );
  });
}
