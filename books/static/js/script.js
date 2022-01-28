import ChiefSlider from 'chief-slider.min.js';

document.addEventListener('DOMContentLoaded', function () {
      const slider = new ChiefSlider('.slider', {
        loop: true,
        autoplay: true,
        interval: 5000,
        refresh: true,
      });
    });