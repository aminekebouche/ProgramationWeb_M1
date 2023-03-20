document.addEventListener('DOMContentLoaded', function() {
    let clickCount = 0;
    let factList = document.getElementById('fact-list');
    let factButton = document.getElementById('new-fact-btn');
    let clickCountDisplay = document.getElementById('click-count');
    

    factButton.addEventListener('click', function() {
      clickCount++;

      clickCountDisplay.textContent = clickCount;
      
      fetch('https://catfact.ninja/fact')
        .then(function(response) {
          return response.json();
        })
        .then(function(data) {
          let newFactItem = document.createElement('li');
          newFactItem.classList.add('list-group-item');
          newFactItem.textContent = data.fact ;
          factList.insertBefore(newFactItem, factList.firstChild);
        })
        .catch(function(error) {
          console.log(error);
        });
    });
  });