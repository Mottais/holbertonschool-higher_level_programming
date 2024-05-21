fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(Objet => showObjet(Objet));

function showObjet (Objet) {
  // pour voir le contenu de l'objet dans la console
  console.log(Objet);
  document.querySelector('#character').textContent = `${Objet.name}`;
}
