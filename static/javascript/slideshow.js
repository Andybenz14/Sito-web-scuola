var slideIndex = 1
var timeoutHandle = setTimeout(plusOne, 5000);

function resetSlide(t) {
    clearTimeout(timeoutHandle);
    timeoutHandle = setTimeout((function() {
        plusOne();
        resetSlide(5000);}), t);
}

function plusOne() {
    plusSlides(1);}

function plusClick(n) {
    plusSlides(n);
    resetSlide(10000);
}
// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}

function helperClick(n) {
    showSlides(n);
    resetSlide(10000);
}
