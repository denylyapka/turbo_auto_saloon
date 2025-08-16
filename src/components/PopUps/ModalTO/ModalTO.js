import React, { useRef, useEffect, useState } from 'react';
import { ModalOverlay, ModalContent, Sticker, Head, Par } from './ModalTOStyles';

// Компонент модального окна
const Modal = ({ onClose, children }) => {
  const modalRef = useRef(null);
  const [isClosing, setIsClosing] = useState(false);

  const handleClose = () => {
    setIsClosing(true);
    setTimeout(() => onClose(), 200); // Должно совпадать с длительностью анимации
  };

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (modalRef.current && !modalRef.current.contains(event.target)) {
        handleClose();
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [onClose]);

  return (
    <ModalOverlay $isClosing={isClosing}>
      <ModalContent ref={modalRef} $isClosing={isClosing}>
        {React.cloneElement(children, { onClose: handleClose })}
      </ModalContent>
    </ModalOverlay>
  );
};

// Компонент ConstructionModal с полной анимацией
export const ConstructionModal = ({ isOpen, onClose }) => {
  const [shouldRender, setShouldRender] = useState(false);

  useEffect(() => {
    if (isOpen) {
      setShouldRender(true);
    }
  }, [isOpen]);


  const handleAnimationEnd = () => {
    if (!isOpen) {
      setShouldRender(false);
    }
  };

  if (!shouldRender && !isOpen) return null;

  return (
    <Modal 
      onClose={() => {
        setShouldRender(false);
        onClose();
      }}
    >
      <>
        <Sticker>🚧</Sticker>
        <Head>Пока в разработке</Head>
        <Par>
          Приносим извинения за временные неудобства.
          Мы работаем над тем, чтобы сделать сервис лучше для вас!
        </Par>
      </>
    </Modal>
  );
};
