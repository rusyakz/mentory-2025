const swiper = new Swiper(".mySwiper", {
  loop: false,             // подсчет страниц
  spaceBetween: 20,        // отступ между карточками
  pagination: {
    el: ".swiper-pagination",
    clickable: true
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  },

  // Группировка по количеству видимых карточек
  breakpoints: {
    0: {                   // телефон
      slidesPerView: 1,
      slidesPerGroup: 1
    },
    768: {                 // планшет
      slidesPerView: 3,
      slidesPerGroup: 3
    },
    1024: {                // ПК
      slidesPerView: 5,
      slidesPerGroup: 5
    }
  }
});
