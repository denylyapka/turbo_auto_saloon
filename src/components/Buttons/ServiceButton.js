import React, { useState } from 'react';
import styled from 'styled-components';
import { AppointmentModal } from '../PopUps/ModalService';

// Стилизованная кнопка
const StyledBookButton = styled.button`
  background: #ff5050ff;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  
  &:hover {
    background: rgba(255, 64, 64, 1);
    scale: 1.1;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  &:active {
    transform: translateY(0);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
  }
`;

export const BookButtonWithModal = ( moduleService, nameService ) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleBookClick = () => {
    console.log(1); // Выводим 1 в консоль
    function encodeRussianToPercent(text) {
      return encodeURIComponent(text)
        .replace(/'/g, "%27")
        .replace(/!/g, "%21");
    }

    // Пример использования:
    const russianText = `Привет, хочу записаться на услугу!\n\n${moduleService} - ${nameService}`;
    const encoded = encodeRussianToPercent(russianText);
    console.log(encoded); 
    window.location.href=`https://t.me/TS_turbo?text=${encoded}`
  };

  return (
    <>
      <StyledBookButton onClick={handleBookClick}>
        Записаться на услугу
      </StyledBookButton>

      <AppointmentModal
        open={isModalOpen}
        onClose={() => setIsModalOpen(false)}
      />
    </>
  );
};