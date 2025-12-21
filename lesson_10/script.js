function toggleAccordion(event) {
  // Найдём контейнер аккордиона
  const accordionContainer = event.target.closest('[accordion-type]') ?? event.target.closest('.accordion__container');
  if (!accordionContainer) return;

  // Определим тип аккордиона (single или multi)
  const accordionType = accordionContainer.getAttribute('accordion-type') ?? 'multi';

  // Ищем ближайший элемент header — это решает проблему кликов по вложенным элементам
  const header = event.target.closest('.accordion__header');
  if (header) return; // если клик не по хедеру и не по его вложенным элементам — игнорируем

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
