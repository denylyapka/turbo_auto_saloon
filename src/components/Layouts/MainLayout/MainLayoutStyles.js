// @ts-nocheck
import styled, { css, keyframes } from 'styled-components';


// Анимации
export const slideAnimation = keyframes`
  0% { transform: translateX(0); opacity: 0; }
  5% { transform: translateX(0); opacity: 1; }
  96% { transform: translateX(-10%); opacity: 1; }
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
      animation: ${css`${underlineAnimation}`} 5s linear forwards;
      animation-delay: 0.1s;
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
      animation: ${css`${slideAnimation}`} 5s linear infinite;
      animation-delay: 1s;
    `}
    ${({ $isMobile }) => !$isMobile && css`
      width: 100%;
    `}
  }
`;


// Стилизованные компоненты
export const HeaderContainer = styled.header`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: ${({ $isMobile }) => $isMobile ? '100vh' : '80px'};
  background: linear-gradient(black, #00000020);
  display: flex;
  flex-direction: ${({ $isMobile }) => $isMobile ? 'column' : 'row'};
  justify-content: space-between;
  align-items: center;
  padding: ${({ $isMobile }) => $isMobile ? '20px' : '0 30px'};
  z-index: 2;
  box-sizing: border-box;
  overflow: ${({ $isMobile }) => $isMobile ? 'hidden' : 'visible'};
`;

export const LogoContainer = styled.div`
  margin-bottom: ${({ $isMobile }) => $isMobile ? '20px' : 0};
  margin-left: ${({ $isMobile }) => $isMobile ? "30px" : '20px'};
  margin-right: ${({ $isMobile }) => $isMobile ? "0" : '-60px'};
  align-self: ${({ $isMobile }) => $isMobile ? 'flex-start' : 'center'};
`;

export const NavContainer = styled.nav`
  display: flex;
  gap: ${({ $isMobile }) => $isMobile ? '15px' : '40px'};
  flex-direction: ${({ $isMobile }) => $isMobile ? 'column' : 'row'};
  align-items: center;
  margin-bottom: ${({ $isMobile }) => $isMobile ? '20px' : 0};
  width: ${({ $isMobile }) => $isMobile ? '100%' : 'auto'};
`;

export const IconsContainer = styled.div`
  display: flex;
  gap: ${({ $isMobile }) => $isMobile ? '30px' : '40px'};
  justify-content: ${({ $isMobile }) => $isMobile ? 'center' : 'flex-end'};
  width: ${({ $isMobile }) => $isMobile ? '100%' : 'auto'};
`;

export const MenuListContainer = styled.div`
  position: absolute;
  top: 0;
  left: ${({ $position }) => $position === 'left' ? '0' : '100%'};
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: 
    transform 0.3s ease,
    visibility 0s linear ${({ $isVisible }) => $isVisible ? '0s' : '0.5s'};
  padding: 20px;
  box-sizing: border-box;
  visibility: ${({ $isVisible }) => $isVisible ? 'visible' : 'hidden'};

  /* Основной список (left) */
  ${({ $position, $isVisible }) => $position === 'left' && `
    transform: ${$isVisible ? 'translateX(0)' : 'translateX(-100%)'};
  `}

  /* Подсписок (right) */
  ${({ $position, $isVisible }) => $position === 'right' && `
    transform: ${$isVisible ? 'translateX(-100%)' : 'translateX(0)'};
  `}
`;

export const BackButton = styled.button`
  position: absolute;
  left: 20px;
  bottom: 20px;
  background: transparent;
  border: none;
  color: white;
  font-size: 44px;
  display: flex;
  align-items: center;
  cursor: pointer;
`;

export const MenuListsWrapper = styled.div`
  position: relative;
  width: 100%;
  height: 100%;
  flex: 1;
`;