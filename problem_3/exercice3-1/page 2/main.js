const form = document.querySelector('form');
const nameInput = document.querySelector('#name-input');
const resultDiv = document.querySelector('#result');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const name = nameInput.value;
  if (name) {
    const response = await fetch(`https://api.genderize.io/?name=${name}`);
    const data = await response.json();
    const { name: predictedName, gender, probability } = data;
    const probabilityString = (probability * 100).toFixed(2);
    resultDiv.textContent = `The name "${predictedName}" is predicted to be ${gender} with ${probabilityString}% probability.`;
  } else {
    resultDiv.textContent = 'Please enter a name.';
  }
});
