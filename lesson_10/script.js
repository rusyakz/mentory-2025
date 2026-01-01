// -----------------------------
// МОДАЛКИ
// -----------------------------
document.querySelectorAll('[data-open-modal]').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const modalId = trigger.getAttribute('data-open-modal');
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.add('open');
    }
  });
});

document.querySelectorAll('.modal').forEach(modal => {
  // Закрытие по клику на оверлей
  modal.addEventListener('click', (event) => {
    if (!event.target.closest('.modal__content')) {
      modal.classList.remove('open');
    }
  });

  // Закрытие по кнопке внутри модалки
  modal.querySelectorAll('.modal__close').forEach(btn => {
    btn.addEventListener('click', () => modal.classList.remove('open'));
  });

  // Закрытие по Esc
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      modal.classList.remove('open');
    }
  });
});

// -----------------------------
// АККОРДЕОН

document.addEventListener('click', function (event) {
  // Ищем ближайший header от места клика
  const header = event.target.closest('.accordion__header');
  if (!header) return; // клик не по заголовку аккордеона

  // Находим родительский блок аккордеона
  const block = header.closest('[accordion-id]');
  if (!block) return;

  // Находим контейнер аккордеона
  const container = block.closest('.accordion__container');
  const type = container?.getAttribute('accordion-type') ?? 'multi';

  // Если режим single — закрываем все остальные блоки в контейнере
  if (type === 'single' && container) {
    container.querySelectorAll('[accordion-id]').forEach(el => {
      if (el !== block) el.setAttribute('accordion-state', 'closed');
    });
  }

  // Переключаем состояние текущего блока
  const currentState = block.getAttribute('accordion-state') ?? 'closed';
  block.setAttribute('accordion-state', currentState === 'open' ? 'closed' : 'open');
});