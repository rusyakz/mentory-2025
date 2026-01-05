// Плавная прокрутка для якорных ссылок + закрытие мобильного меню
document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener('click', (e) => {
    const target = document.querySelector(link.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Закрыть мобильное меню после клика
    const navList = document.getElementById('nav-list');
    navList?.classList.remove('open');
    const toggle = document.querySelector('.nav-toggle');
    toggle?.setAttribute('aria-expanded', 'false');
  });
});

// Мобильное меню
const toggle = document.querySelector('.nav-toggle');
const navList = document.getElementById('nav-list');
toggle?.addEventListener('click', () => {
  const isOpen = navList.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(isOpen));
});

// Анимация появления секций по мере прокрутки
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.classList.add('visible');
    });
  },
  { threshold: 0.15 }
);
document.querySelectorAll('.fade-in').forEach((el) => observer.observe(el));

// Валидация формы «на месте» + имитация отправки
const form = document.querySelector('.contact-form');
const status = document.querySelector('.form-status');

function setError(id, message = '') {
  const span = document.querySelector(`.error[data-for="${id}"]`);
  if (span) span.textContent = message;
}

form?.addEventListener('submit', async (e) => {
  e.preventDefault();

  const name = document.getElementById('name');
  const email = document.getElementById('email');
  const message = document.getElementById('message');

  let valid = true;

  if (!name.value.trim()) { setError('name', 'Введите имя'); valid = false; } else setError('name');
  if (!email.value.trim() || !/\S+@\S+\.\S+/.test(email.value)) {
    setError('email', 'Укажите корректный email'); valid = false;
  } else setError('email');

  if (!message.value.trim()) { setError('message', 'Напишите сообщение'); valid = false; } else setError('message');

  if (!valid) return;

  status.textContent = 'Отправка…';

  // Здесь интегрируйте реальный бэкенд (fetch на ваш endpoint)
  await new Promise((r) => setTimeout(r, 800));

  status.textContent = 'Сообщение отправлено! Я свяжусь с вами.';
  form.reset();
});

// Модальное увеличение изображений проектов
const modal = document.getElementById('image-modal');
const modalImg = document.getElementById('modal-image');

function openModal(src) {
  modalImg.src = src;
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}
function closeModal() {
  modal.setAttribute('aria-hidden', 'true');
  modalImg.src = '';
  document.body.style.overflow = '';
}

document.querySelectorAll('.zoom-btn').forEach((btn) => {
  btn.addEventListener('click', () => {
    const src = btn.getAttribute('data-modal-image');
    if (src) openModal(src);
  });
});

modal.addEventListener('click', (e) => {
  if (e.target.matches('[data-close-modal], .modal-backdrop')) {
    closeModal();
  }
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});







const track = document.querySelector('.carousel-track');
const slides = Array.from(track.children);
const prevBtn = document.querySelector('.carousel-btn.prev');
const nextBtn = document.querySelector('.carousel-btn.next');
const dotsNav = document.querySelector('.carousel-dots');

let currentIndex = 0;

// создаём буллеты
slides.forEach((_, i) => {
  const dot = document.createElement('button');
  if (i === 0) dot.classList.add('active');
  dotsNav.appendChild(dot);
  dot.addEventListener('click', () => {
    currentIndex = i;
    updateCarousel();
  });
});

function visibleCount() {
  if (window.innerWidth >= 960) return 3;
  if (window.innerWidth >= 600) return 2;
  return 1;
}

function updateCarousel() {
  const slideWidth = slides[0].getBoundingClientRect().width;
  track.style.transform = `translateX(-${slideWidth * currentIndex}px)`;

  dotsNav.querySelectorAll('button').forEach((dot, i) => {
    dot.classList.toggle('active', i === currentIndex);
  });
}

nextBtn.addEventListener('click', () => {
  const maxIndex = slides.length - visibleCount();
  if (currentIndex < maxIndex) currentIndex++;
  updateCarousel();
});

prevBtn.addEventListener('click', () => {
  if (currentIndex > 0) currentIndex--;
  updateCarousel();
});

window.addEventListener('resize', updateCarousel);

