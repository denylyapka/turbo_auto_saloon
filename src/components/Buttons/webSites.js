// @ts-nocheck

import React from 'react';
import PropTypes from 'prop-types';

/**
 * Компонент для отображения кликабельных SVG-иконок
 * @param {Object} props - Пропсы компонента
 * @param {React.ReactNode} props.svg - SVG-элемент или компонент
 * @param {string} props.link - Ссылка для перехода
 * @param {string} [props.className] - Дополнительные CSS-классы
 * @param {string} [props.title] - Текст подсказки при наведении
 * @param {string} [props.target] - Атрибут target для ссылки (по умолчанию '_blank')
 * @param {Object} [props.style] - Инлайн-стили для обертки
 */
export function SVGButtons ({ 
  svg, 
  link, 
  className = '', 
  title = '', 
  target = '_blank', 
  style = {},
  rel = 'noopener noreferrer'
}) {
  if (!svg || !link) {
    console.error('SVGButtons: Не переданы обязательные пропсы svg или link');
    return null;
  }

  return (
    <a
      href={link}
      target={target}
      rel={rel}
      className={`svg-button ${className}`}
      title={title}
      style={style}
      aria-label={title || 'Ссылка на социальную сеть'}
    >
      {React.cloneElement(svg, {
        className: 'svg-button__icon',
        'aria-hidden': true,
        focusable: false
      })}
    </a>
  );
};

SVGButtons.propTypes = {
  svg: PropTypes.element.isRequired,
  link: PropTypes.string.isRequired,
  className: PropTypes.string,
  title: PropTypes.string,
  target: PropTypes.string,
  style: PropTypes.object,
  rel: PropTypes.string
};

export default SVGButtons