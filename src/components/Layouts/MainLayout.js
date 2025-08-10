// @ts-nocheck
import React, { useState, useEffect, useRef } from 'react';
import styled, { css, keyframes } from 'styled-components';
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

// Анимации
const slideAnimation = keyframes`
  0% { transform: translateX(0); opacity: 0; }
  5% { transform: translateX(0); opacity: 1; }
  98% { transform: translateX(-20%); opacity: 1; }
  100% { opacity: 0; }
`;

const underlineAnimation = keyframes`
  from { width: 0; }
  to { width: 100%; }
`;

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

const NavButton = styled.button`
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

const FullscreenCarousel = styled.div`
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

const HeaderGradient = ({ isMobile, onSelectCategory, onHoverCategory, activeItem }) => {
  const navigate = useNavigate();
  const navItems = [
    { name: 'Детейлинг', category: 'detailing' },
    { name: 'Услуги', category: 'services' },
    { name: '⛔ Магазин 🛠️', category: 'shop' },
    { name: '⛔ Подбор авто 🛠️', category: 'selection' }
  ];

  const handleCategoryClick = (category) => {
    if (isMobile) {
      navigate(MENU_ITEMS[category].mainLink);
    } else {
      onSelectCategory(category);
    }
  };

  const handleCategoryHover = (category) => {
    if (!isMobile) {
      onHoverCategory(category);
    }
  };

  const handleCategoryLeave = () => {
    if (!isMobile) {
      onHoverCategory('general');
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
        <SvgIconsLogo iconName={"logo"} size={isMobile ? '46' : '40'}/>
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
          <NavButtonWrapper 
            key={index} 
            $isMobile={isMobile}
            onMouseEnter={() => handleCategoryHover(item.category)}
          >
            <NavButton 
              $isMobile={isMobile}
              $active={isMobile && activeItem === item.category}
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
        gap: isMobile ? '30px' : '40px',
        justifyContent: isMobile ? 'center' : 'flex-end',
        width: isMobile ? '100%' : 'auto'
      }}>
        <SvgIconsHeader iconName="call" size="20"/>          
        <SvgIconsHeader iconName="user" size="26"/>
        <SvgIconsHeader iconName="map-pin" size="20"/>
      </div>
    </header>
  );
};

const MainLayout = () => {
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);
  const [currentCategory, setCurrentCategory] = useState('general');
  const [hoverCategory, setHoverCategory] = useState(null);
  const [activeItem, setActiveItem] = useState(null);
  const [currentPhoto, setCurrentPhoto] = useState('');
  const intervalRef = useRef(null);

  const navItems = ['detailing', 'services', 'shop', 'selection'];
  
  const getRandomPhoto = (category) => {
    const photos = PHOTO_CATEGORIES[category] || [];
    return photos[Math.floor(Math.random() * photos.length)] || '';
  };

  // Автоматическая смена пунктов меню на мобильной версии
  useEffect(() => {
    if (isMobile) {
      let currentIndex = 0;
      
      const cycleItems = () => {
        const category = navItems[currentIndex];
        setActiveItem(category);
        setCurrentPhoto(getRandomPhoto(category));
        
        currentIndex = (currentIndex + 1) % navItems.length;
      };

      // Начинаем с первого элемента
      cycleItems();
      
      // Устанавливаем интервал для смены элементов
      intervalRef.current = setInterval(cycleItems, 10000);
      
      return () => {
        if (intervalRef.current) {
          clearInterval(intervalRef.current);
        }
      };
    }
  }, [isMobile]);

  useEffect(() => {
    if (!isMobile) {
      const activeCategory = hoverCategory || currentCategory;
      setCurrentPhoto(getRandomPhoto(activeCategory));
    }
  }, [currentCategory, hoverCategory, isMobile]);

  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth < 768);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <div style={{ position: 'relative', height: '100vh', width: '100vw' }}>
      <FullscreenCarousel $isMobile={isMobile}>
        <div className="photo-container">
          {currentPhoto && <img src={currentPhoto} alt="Background" />}
        </div>
      </FullscreenCarousel>
      <HeaderGradient 
        isMobile={isMobile} 
        onSelectCategory={setCurrentCategory}
        onHoverCategory={setHoverCategory}
        activeItem={activeItem}
      />
    </div>
  );
};

export default MainLayout;