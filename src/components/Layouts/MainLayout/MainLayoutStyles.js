// @ts-nocheck
import styled, { css, keyframes } from 'styled-components';


// Анимации
export const slideAnimation = keyframes`
  0% { transform: translateX(0); opacity: 0; }
  5% { transform: translateX(0); opacity: 1; }
  98% { transform: translateX(-20%); opacity: 1; }
  100% { opacity: 0; }
`;

export const underlineAnimation = keyframes`
  from { width: 0; }
  to { width: 100%; }
`;

// Стилизованные компоненты
export const DropdownMenu = styled.div`
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.8);
  min-width: 200px;
  border-radius: 4px;
  padding: 8px 0;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 10;

  ${({ $isMobile }) => $isMobile && css`
    display: none;
  `}
`;

export const NavButtonWrapper = styled.div`
  position: relative;
  display: inline-flex;
  flex-direction: column;
  align-items: center;

  &:hover ${DropdownMenu} {
    opacity: 1;
    visibility: visible;
  }

  ${({ $isMobile }) => $isMobile && css`
    width: 100%;
  `}
`;

export const NavButton = styled.button`
  background: none;
  border: none;
  color: white;
  font-size: ${({ $isMobile }) => $isMobile ? '28px' : '18px'};
  cursor: pointer;
  padding: 8px 12px;
  position: relative;
  transition: all 0.3s ease;
  white-space: nowrap;
  text-align: center;
  display: inline-block;

  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: white;
    transition: all 0.3s ease;
    ${({ $active, $isMobile }) => $active && $isMobile && css`
      animation: ${css`${underlineAnimation}`} 10s linear forwards;
    `}
  }

  &:hover {
    opacity: 0.9;
    &::after {
      width: 100%;
    }
  }

  ${({ $isMobile }) => $isMobile && css`
    width: auto;
    padding: 12px 0;
    white-space: nowrap;
    text-align: center;
    display: inline-block;
  `}
`;

export const DropdownItem = styled.a`
  display: block;
  padding: 10px 20px;
  color: white;
  text-decoration: none;
  transition: background-color 0.2s;

  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
`;

export const FullscreenCarousel = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1;
  overflow: hidden;

  .photo-container {
    position: absolute;
    width: 100%;
    height: 100%;
  }

  img {
    position: absolute;
    height: 100%;
    object-fit: cover;
    ${({ $isMobile }) => $isMobile && css`
      animation: ${css`${slideAnimation}`} 10s linear infinite;
    `}
    ${({ $isMobile }) => !$isMobile && css`
      width: 100%;
    `}
  }
`;
