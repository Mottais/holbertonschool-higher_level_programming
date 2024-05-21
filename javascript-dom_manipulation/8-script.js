// DOMContentLoaded permet l'execution du script après le chargement du DOM
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(Objet => showObjet(Objet));

  function showObjet (Objet) {
    // pour voir le contenu de l'objet dans la console
    console.log(Objet);
    document.querySelector('#hello').textContent = Objet.hello;
  }
});
