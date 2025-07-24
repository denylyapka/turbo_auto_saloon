// @ts-nocheck
import React from "react";
import styled from "styled-components";
import SearchComponent from "../Searchs/Search";
import SvgIconsHeader from "../SVG/Header";

const HeaderContainer = styled.header`
  background-color: #313131;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
  position: relative;
  z-index: 1001;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);

  @media (min-width: 769px) {
    padding: 0 30px;
  }
`;

const HeaderSection = styled.div`
  display: flex;
  align-items: center;
  gap: 15px;

  @media (min-width: 769px) {
    gap: 30px;
  }
`;

const IconsContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;

  @media (min-width: 769px) {
    gap: 20px;
  }
`;

const BurgerButton = styled.button`
  background: none;
  border: none;
  cursor: pointer;
  padding: 10px;
  display: ${({ $isMobile }) => $isMobile ? 'flex' : 'none'};
  flex-direction: column;
  justify-content: space-between;
  height: 24px;
  width: 30px;
  margin-right: 10px;
  z-index: 1002;

  @media (min-width: 769px) {
    margin-right: 0;
  }
`;

const BurgerLine = styled.span`
  display: block;
  width: 100%;
  height: 2px;
  background: white;
  transition: all 0.3s ease;
  transform-origin: center;
  
  &:nth-child(1) {
    transform: ${({ $menuOpen }) => $menuOpen ? 'rotate(45deg) translate(5px, 5px)' : 'none'};
  }
  
  &:nth-child(2) {
    opacity: ${({ $menuOpen }) => $menuOpen ? '0' : '1'};
    transform: ${({ $menuOpen }) => $menuOpen ? 'translateX(-20px)' : 'none'};
  }
  
  &:nth-child(3) {
    transform: ${({ $menuOpen }) => $menuOpen ? 'rotate(-45deg) translate(5px, -5px)' : 'none'};
  }
`;

const CartCounter = styled.span`
  position: absolute;
  top: -5px;
  right: -5px;
  background: #ff4d4d;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: bold;
`;

const CartIconWrapper = styled.div`
  position: relative;
  display: flex;
`;

const Header = ({ onMenuToggle, isMobile, menuOpen }) => {
  const [searchValue, setSearchValue] = React.useState("");
  const [cartItemsCount, setCartItemsCount] = React.useState(7); // Начальное значение


  const handleSearchChange = (e) => {
    setSearchValue(e.target.value);
  };

  return (
    <HeaderContainer>
      <HeaderSection>
        {/* Бургер-кнопка (только на мобильных) */}
        <BurgerButton 
          $isMobile={isMobile} 
          onClick={onMenuToggle}
          aria-label="Меню"
        >
          <BurgerLine $menuOpen={menuOpen} />
          <BurgerLine $menuOpen={menuOpen} />
          <BurgerLine $menuOpen={menuOpen} />
        </BurgerButton>

        {/* Поиск - скрываем на мобильных при открытом меню */}
        {(!isMobile || !menuOpen) && (
          <SearchComponent 
            placeholder="Поиск по сайту..." 
            value={searchValue}
            onChange={handleSearchChange}
            width={isMobile ? "180px" : "250px"}
          />
        )}
      </HeaderSection>

      <HeaderSection>
        <IconsContainer>
          
          <SvgIconsHeader iconName="user" size="18"/>
          
          <CartIconWrapper>
            <SvgIconsHeader iconName="cart" size="18"/>
            {cartItemsCount > 0 && <CartCounter>{cartItemsCount}</CartCounter>}
          </CartIconWrapper>
          
          <SvgIconsHeader iconName="call" size="14"/>
        
        </IconsContainer>
      </HeaderSection>
    </HeaderContainer>
  );
};

export default Header;