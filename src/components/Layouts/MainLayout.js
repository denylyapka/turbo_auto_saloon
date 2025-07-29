// @ts-nocheck
import React, { useState, useEffect } from 'react';
import styled, { css } from 'styled-components';
import SvgIconsLogo from 'components/SVG/Logos';
import SvgIconsHeader from 'components/SVG/Header';
import { useNavigate } from 'react-router-dom';

// Константы с фотографиями
const PHOTO_CATEGORIES = {
  general: ['https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/mainPage/Group%20304.png'],
  detailing: ['https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/mainPage/avtoremontnaa_masterskaa_s_masinami_na_zadnem_plane_cistaa_i_arkaa.jpg'],
  services: ['https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/mainPage/uslugi-po-remontu-i-obsluzivaniu-avtomobilei-v-garaze%20(1).jpg'],
  shop: ['https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/mainPage/uslugi-po-remontu-i-obsluzivaniu-avtomobilei-v-garaze.jpg'],
  selection: ['https://i.pinimg.com/originals/9d/d0/55/9dd055a5e9d594b0df8a0524a72da390.jpg']
};

// Данные для выпадающих меню и страниц
const MENU_ITEMS = {
  detailing: {
    items: [
      { name: 'Полировка', link: '/detailing' },
      { name: 'Оклейка пленкой', link: '/detailing' },
      { name: 'PDR выпрямление вмятин ', link: '/detailing' },
      { name: 'Локальная окраска ', link: '/detailing' },
      { name: 'Химчистка ', link: '/detailing' },
      { name: 'Реставрации салона ', link: '/detailing' }
    ],
    mainLink: '/detailing'
  },
  services: {
    items: [
      { name: 'Диагностика и ремонт', link: '/services' },
      { name: 'Программный чип тюнинг', link: '/services' },
      { name: 'Русификация и дооснащение', link: '/services' },
      { name: 'Тюнинг автосвета', link: '/services' }
    ],
    mainLink: '/services'
  },
  shop: {
    items: [
      { name: 'Автозапчасти', link: '/shop/zapchasti' },
      { name: 'Автохимия и аксессуары', link: '/shop/kxhimiya' }
    ],
    mainLink: '/shop'
  },
  selection: {
    mainLink: '/selection'
  }
};

// Стилизованные компоненты
const DropdownMenu = styled.div`
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

const NavButtonWrapper = styled.div`
  position: relative;
  display: inline-block;

  &:hover ${DropdownMenu} {
    opacity: 1;
    visibility: visible;
  }

  ${({ $isMobile }) => $isMobile && css`
    width: 100%;
  `}
`;

const NavButton = styled.button`
  background: none;
  border: none;
  color: white;
  font-size: ${({ $isMobile }) => $isMobile ? '20px' : '18px'};
  cursor: pointer;
  padding: 8px 12px;
  position: relative;
  transition: all 0.3s ease;
  white-space: nowrap;

  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 1px;
    background: white;
    transition: all 0.3s ease;
    transform: translateX(-50%);
  }

  &:hover {
    opacity: 0.9;
    &::after {
      width: ${({ $isMobile }) => $isMobile ? '0' : '100%'};
    }
  }

  ${({ $isMobile }) => $isMobile && css`
    width: 100%;
    padding-left: 0;
    white-space: normal;
  `}
`;

const DropdownItem = styled.a`
  display: block;
  padding: 10px 20px;
  color: white;
  text-decoration: none;
  transition: background-color 0.2s;

  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
`;

const FullscreenCarousel = ({ currentPhoto }) => {
  if (!currentPhoto) return null;
  
  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      width: '100vw',
      height: '100vh',
      zIndex: 1
    }}>
      <img 
        src={currentPhoto} 
        alt="Background" 
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover'
        }}
      />
    </div>
  );
};

const HeaderGradient = ({ isMobile, onSelectCategory }) => {
  const navigate = useNavigate();
  const navItems = [
    { name: 'Детейлинг', category: 'detailing' },
    { name: 'Услуги', category: 'services' },
    { name: 'Магазин', category: 'shop' },
    { name: 'Подбор авто', category: 'selection' }
  ];

  const handleCategoryClick = (category) => {
    if (isMobile) {
      navigate(MENU_ITEMS[category].mainLink);
    } else {
      onSelectCategory(category);
    }
  };

  return (
    <header style={{
      position: 'fixed',
      top: 0,
      left: 0,
      width: '100%',
      height: isMobile ? '100vh' : '80px',
      background: 'linear-gradient(black, #00000020)',
      display: 'flex',
      flexDirection: isMobile ? 'column' : 'row',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: isMobile ? '20px' : '0 30px',
      zIndex: 2,
      boxSizing: 'border-box'
    }}>
      <div style={{ 
        marginBottom: isMobile ? '20px' : 0, 
        marginLeft: isMobile ? "30px" : '20px', 
        marginRight: isMobile ? "0" : '-60px'
      }}>
        <SvgIconsLogo iconName={"logo"} size={isMobile ? '30' : '40'}/>
      </div>

      <nav style={{
        display: 'flex',
        gap: isMobile ? '15px' : '40px',
        flexDirection: isMobile ? 'column' : 'row',
        alignItems: 'center',
        marginBottom: isMobile ? '20px' : 0,
        width: isMobile ? '100%' : 'auto'
      }}>
        {navItems.map((item, index) => (
          <NavButtonWrapper key={index} $isMobile={isMobile}>
            <NavButton 
              $isMobile={isMobile}
              onClick={() => handleCategoryClick(item.category)}
            >
              {item.name}
            </NavButton>
            
            {!isMobile && MENU_ITEMS[item.category]?.items && (
              <DropdownMenu>
                {MENU_ITEMS[item.category].items.map((dropdownItem, idx) => (
                  <DropdownItem 
                    key={idx} 
                    href={dropdownItem.link}
                    onClick={(e) => {
                      e.preventDefault();
                      navigate(dropdownItem.link);
                    }}
                  >
                    {dropdownItem.name}
                  </DropdownItem>
                ))}
              </DropdownMenu>
            )}
          </NavButtonWrapper>
        ))}
      </nav>

      <div style={{
        display: 'flex',
        gap: isMobile ? '20px' : '40px',
        justifyContent: isMobile ? 'center' : 'flex-end',
        width: isMobile ? '100%' : 'auto'
      }}>
        <SvgIconsHeader iconName="call" size="18"/>          
        <SvgIconsHeader iconName="user" size="18"/>
        <SvgIconsHeader iconName="map-pin" size="14"/>
      </div>
    </header>
  );
};

const MainLayout = () => {
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);
  const [currentCategory, setCurrentCategory] = useState('general');
  const [currentPhoto, setCurrentPhoto] = useState('');

  const getRandomPhoto = (category) => {
    const photos = PHOTO_CATEGORIES[category] || [];
    return photos[Math.floor(Math.random() * photos.length)] || '';
  };

  useEffect(() => {
    setCurrentPhoto(getRandomPhoto(currentCategory));
  }, [currentCategory]);

  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth < 768);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <div style={{ position: 'relative', height: '100vh', width: '100vw' }}>
      <FullscreenCarousel currentPhoto={currentPhoto} />
      <HeaderGradient 
        isMobile={isMobile} 
        onSelectCategory={setCurrentCategory} 
      />
    </div>
  );
};

export default MainLayout;