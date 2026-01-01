
const swiper = new Swiper('.testimonials-swiper', {

  loop: false,
  speed: 500,
  spaceBetween: 20,
  slidesPerView: 1,

  simulateTouch: true,
  touchRatio: 1,
  grabCursor: true,

  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    bulletElement: 'button',
    renderBullet: (index, className) => {
      // Accessible bullet
      return `<button class="${className}" aria-label="Перейти к странице ${index + 1}" title="Страница ${index + 1}"></button>`;
    }
  },

  //
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev'
  },

  //
  keyboard: {
    enabled: true,
    onlyInViewport: true
  },

  //
  breakpoints: {
    600: {
      slidesPerView: 2,
      spaceBetween: 24
    },
    900: {
      slidesPerView: 3,
      spaceBetween: 28
    }
  },


  a11y: {
    enabled: true,
    prevSlideMessage: 'Предыдущий отзыв',
    nextSlideMessage: 'Следующий отзыв',
    paginationBulletMessage: 'Перейти к отзыву {{index}}'
  }
});