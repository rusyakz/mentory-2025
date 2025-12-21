// Модалки продвинутые
const openModalButtons = document.querySelectorAll('[data-modal-action="open-modal"]');
const closeModalButtons = document.querySelectorAll('[data-modal-action="close-modal"]');
const modalWindows = document.querySelectorAll('[data-modal-action="modal"]');

openModalButtons.forEach((btn) => {
  btn.addEventListener('click', openModal);
});

closeModalButtons.forEach((btn) => {
  btn.addEventListener('click', closeModal);
});

modalWindows.forEach((modal) => {
  // Закрытие по клику на оверлей (тёмная область)
  modal.addEventListener('click', (event) => {
    if (event.target === modal) {
      modal.classList.remove('open');
    }
  });
});

function openModal(event) {
  modalWindows.forEach((modal) => {
    if (modal.getAttribute('data-modal') === event.target.getAttribute('data-modal')) {
      modal.classList.add('open');
    }
  });
}

function closeModal(event) {
  modalWindows.forEach((modal) => {
    if (modal.getAttribute('data-modal') === event.target.getAttribute('data-modal')) {
      modal.classList.remove('open');
    }
  });
}

// Аккордионы

const accordions = document.querySelectorAll('.accordion__container');

function toggleAccordion(event) {
  // Найдём контейнер аккордиона (в котором произошло событие)
  const accordionContainer = event.target.closest('[accordion-type]') ?? event.target.closest('.accordion__container');
  if (!accordionContainer) return;

  // Определим тип аккордиона (single или multi) — берём атрибут у контейнера
  const accordionType = accordionContainer.getAttribute('accordion-type') ?? 'multi';

  // Ищем ближайший элемент header — это решает проблему кликов по вложенным элементам
  const header = event.target.closest('.accordion__header');
  if (!header) return; // если клик не по хедеру и не по его вложенным элементам — игнорируем

  // Найдём блок-родитель с атрибутом accordion-id
  const parentElement = header.closest('[accordion-id]');
  if (!parentElement) return;

  const accordionState = parentElement.getAttribute('accordion-state');

  if (accordionType === 'single') {
    const allBlocks = accordionContainer.querySelectorAll('[accordion-id]');
    allBlocks.forEach((item) => {
      item.setAttribute('accordion-state', 'closed');
    });
  }

  if (accordionState === 'closed') {
    parentElement.setAttribute('accordion-state', 'open');
  } else {
    parentElement.setAttribute('accordion-state', 'closed');
  }
}

accordions.forEach((accordion) => {
  accordion.addEventListener('click', toggleAccordion);
});
