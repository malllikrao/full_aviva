document.addEventListener('DOMContentLoaded', function() {
    const sliderContainer = document.querySelector('.slider-container');
    const sliderWrapper = document.querySelector('.slider-wrapper');
    const slides = document.querySelectorAll('.slide');
    let currentIndex = 0;

    function updateSlider() {
        const slideWidth = slides[0].offsetWidth;
        sliderWrapper.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    }

    document.querySelector('.prev').addEventListener('click', () => {
        currentIndex = Math.max(currentIndex - 1, 0);
        updateSlider();
    });

    document.querySelector('.next').addEventListener('click', () => {
        currentIndex = Math.min(currentIndex + 1, slides.length - 1);
        updateSlider();
    });

    // Initial setup
    updateSlider();
});