// @ts-nocheck
import styled, { keyframes, css } from 'styled-components';

// Анимации
export const fadeIn = keyframes`
  from { opacity: 0; }
  to { opacity: 1; }
`;

export const fadeOut = keyframes`
  from { opacity: 1; }
  to { opacity: 0; }
`;

export const scaleIn = keyframes`
  from { transform: scale(0.9); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
`;

export const scaleOut = keyframes`
  from { transform: scale(1); opacity: 1; }
  to { transform: scale(0.9); opacity: 0; }
`;

// Стилизованные компоненты
export const ModalOverlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  animation: ${fadeIn} 0.3s ease-out forwards;

  ${props => props.$isClosing && css`
    animation: ${fadeOut} 0.2s ease-in forwards;
  `}
`;

export const ModalContent = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 12px;
  max-width: 400px;
  width: 70%;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  animation: ${scaleIn} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;

  ${props => props.$isClosing && css`
    animation: ${scaleOut} 0.2s ease-in forwards;
  `}
`;

export const Sticker = styled.div`
  font-size: 3rem;
  margin-bottom: 1rem;
`;

export const Head = styled.h2`
  margin: 0 0 1rem 0;
  color: #fff;
`;

export const Par = styled.p`
  margin: 0 0 1rem 0;
  color: #666;
  line-height: 1.5;
`;
