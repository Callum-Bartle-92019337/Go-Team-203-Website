const BACKBTN = document.getElementById('BackButton');
// const ARTICLE = document.querySelector('.atmo article');

function backButton() {
  history.back();
};

function success() {
  document.querySelector('form').innerHTML = "Thankyou<br>";
}
if (BACKBTN) {
  BACKBTN.setAttribute("class", 'btn');
  BACKBTN.setAttribute("title", 'Back');
  BACKBTN.setAttribute("href", "#");
  BACKBTN.textContent = "< Back";
  BACKBTN.addEventListener('click', backButton);
};

const TITLEBUTTON = document.querySelector('#titleButton');
if (TITLEBUTTON) {
  TITLEBUTTON.addEventListener("mouseover", function () {
    TITLEBUTTON.style.backgroundColor = "rgba(200,71,70,0.41)"
  });
  TITLEBUTTON.addEventListener("mouseout", function () {
    TITLEBUTTON.style.backgroundColor = "rgba(0, 0, 0, 0.5)"
  });
}
