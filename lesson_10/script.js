// -----------------------------
// МОДАЛКИ
// -----------------------------
document.querySelectorAll('.modal').forEach(modal => {
  // Открытие модалки document.querySelector('[data-open-modal="id"]').addEventListener('click', () => modal.classList.add('open'));

  // Закрытие по клику на оверлей
  modal.addEventListener('click', (event) => {
    // Если клик произошёл внутри контента модалки — ничего не делать
    if (event.target.closest('.modal__content')) return;

    // Иначе — закрываем модалку (клик по оверлею или по самому .modal)
    modal.classList.remove('open');
  });

  // Закрытие по кнопке внутри модалки
  modal.querySelectorAll('.modal__close').forEach(btn => {
    btn.addEventListener('click', () => modal.classList.remove('open'));
  });

  // закрытие по Esc
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