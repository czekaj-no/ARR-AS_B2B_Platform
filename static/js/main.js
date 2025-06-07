document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector('.carousel-track');
  const items = document.querySelectorAll('.carousel-item');
  const prevBtn = document.querySelector('.carousel-btn.carousel-prev');
  const nextBtn = document.querySelector('.carousel-btn.carousel-next');

  let index = 0;
  const visibleItems = 3;

  const updateCarousel = () => {
    const itemWidth = items[0].offsetWidth + 20;
    const offset = index * itemWidth;
    track.style.transform = `translateX(-${offset}px)`;
  };

  nextBtn.addEventListener('click', () => {
    if (index < items.length - visibleItems) {
      index++;
      updateCarousel();
    }
  });

  prevBtn.addEventListener('click', () => {
    if (index > 0) {
      index--;
      updateCarousel();
    }
  });
});



document.addEventListener("DOMContentLoaded", () => {
  const faqItems = document.querySelectorAll(".faq-item");

  faqItems.forEach((item) => {
    const button = item.querySelector(".faq-question");

    button.addEventListener("click", () => {
      item.classList.toggle("active");
    });
  });
});
