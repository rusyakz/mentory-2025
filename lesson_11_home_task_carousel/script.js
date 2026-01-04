'use strict';

// const swiper = new Swiper(".mySwiper", {
//   loop: true,
//   spaceBetween: 30,
//   pagination: {
//     el: ".swiper-pagination",
//     clickable: true,
//     dynamicBullets: true, //  адаптивные буллеты
//   },
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
//   breakpoints: {
//     320: { slidesPerView: 1 },
//     768: { slidesPerView: 2 },
//     1024: { slidesPerView: 4 }
//   }
// });



const swiper = new Swiper(".mySwiper", {
  loop: false, // если нужен точный подсчёт страниц, лучше выключить loop
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    320: { // телефон
      slidesPerView: 1,
      slidesPerGroup: 1
    },
    768: { // планшет
      slidesPerView: 3,
      slidesPerGroup: 3
    },
    1024: { // ПК
      slidesPerView: 5,
      slidesPerGroup: 5
    }
  }
});
