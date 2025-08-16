import React, { useState, useEffect, useRef } from 'react';
import SvgIconsLogo from 'components/SVG/Logos';
import SvgIconsHeader from 'components/SVG/Header';
import { useNavigate } from 'react-router-dom';
import { ConstructionModal } from '../../PopUps/ModalTO/ModalTO';
import { PHOTO_CATEGORIES } from '../../../Сonstants/Photos';
import { MENU_ITEMS } from '../../../Сonstants/MenuItems';
import { 
  DropdownMenu, NavButtonWrapper,
  NavButton, DropdownItem,
  FullscreenCarousel, HeaderContainer,
  LogoContainer, NavContainer,
  IconsContainer, BackButton,
  MenuListContainer, MenuListsWrapper
} from './MainLayoutStyles';
import SITE_CONSTANTS from 'Сonstants/siteConstants';

const MenuList = ({ items, onItemClick, onBack, isVisible, position }) => {
  return (
    <MenuListContainer $isVisible={isVisible} $position={position}>
      {items.map((item, index) => (
        <NavButtonWrapper key={index} $isMobile={true}>
          <NavButton 
            $isMobile={true}
            onClick={() => onItemClick(item.category)}
          >
            {item.name}
          </NavButton>
        </NavButtonWrapper>
      ))}
      
      {onBack && <BackButton onClick={onBack}>←</BackButton>}
    </MenuListContainer>
  );
};

const HeaderGradient = ({ isMobile, onSelectCategory, onHoverCategory, activeItem }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalCategory, setModalCategory] = useState(null);
  const [currentView, setCurrentView] = useState('main');
  const [selectedCategory, setSelectedCategory] = useState(null);
  const navigate = useNavigate();
  
  const mainNavItems = [
    { name: 'Детейлинг', category: 'detailing' },
    { name: 'Сервис', category: 'services' },
    { name: 'Магазин', category: 'shop' },
    { name: 'Подбор авто', category: 'selection' }
  ];

  const getSubItems = (category) => {
    return MENU_ITEMS[category]?.items?.map((item, index) => ({
      name: item.name,
      category: `${category}_${index}`,
      link: item.link
    })) || [];
  };

  const handleCategoryClick = (category) => {
    if (category === 'shop' || category === 'selection') {
      setModalCategory(category);
      setIsModalOpen(true);
      return;
    }

    if (category.includes('_')) {
      const [mainCategory, index] = category.split('_');
      const item = MENU_ITEMS[mainCategory]?.items[parseInt(index)];
      if (item) {
        navigate(item.link);
      }
      return;
    }

    if (isMobile) {
      if (currentView === 'main') {
        setSelectedCategory(category);
        setCurrentView(category);
      } else {
        navigate(MENU_ITEMS[selectedCategory]?.mainLink || '/');
      }
    } else {
      onSelectCategory(category);
    }
  };

  const handleBackClick = () => {
    setCurrentView('main');
  };

  const handleCategoryHover = (category) => {
    if (!isMobile) {
      onHoverCategory(category);
    }
  };

  return (
    <>
      <HeaderContainer $isMobile={isMobile}>
        {!isMobile ? (
          <>
            <LogoContainer $isMobile={isMobile}>
              <SvgIconsLogo iconName={"logo"} size={'40'}/>
            </LogoContainer>

            <NavContainer $isMobile={isMobile}>
              {mainNavItems.map((item, index) => (
                <NavButtonWrapper 
                  key={index} 
                  $isMobile={false}
                  onMouseEnter={() => handleCategoryHover(item.category)}
                >
                  <NavButton 
                    $isMobile={false}
                    onClick={() => handleCategoryClick(item.category)}
                  >
                    {item.name}
                  </NavButton>
                  
                  {MENU_ITEMS[item.category]?.items && (
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
            </NavContainer>

            <IconsContainer $isMobile={isMobile}>
              <SvgIconsHeader iconName="call" size="16"/>          
              <SvgIconsHeader iconName="user" size="22"/>
              <SvgIconsHeader iconName="map-pin" size="16" onClick={() => window.open(SITE_CONSTANTS.contacts.urlToAddress, '_blank')}/>
            </IconsContainer>
          </>
        ) : (
          <>
            <LogoContainer $isMobile={isMobile}>
              <SvgIconsLogo iconName={"logo"} size={'46'}/>
            </LogoContainer>

            <MenuListsWrapper>
              <MenuList
                items={mainNavItems}
                onItemClick={handleCategoryClick}
                isVisible={currentView === 'main'}
                position="left"
              />

              <MenuList
                items={getSubItems('detailing')}
                onItemClick={handleCategoryClick}
                onBack={handleBackClick}
                isVisible={currentView === 'detailing'}
                position="right"
              />

              <MenuList
                items={getSubItems('services')}
                onItemClick={handleCategoryClick}
                onBack={handleBackClick}
                isVisible={currentView === 'services'}
                position="right"
              />
            </MenuListsWrapper>

            <IconsContainer $isMobile={isMobile}>
              <SvgIconsHeader iconName="call" size="20"/>          
              <SvgIconsHeader iconName="user" size="26"/>
              <SvgIconsHeader iconName="map-pin" size="20"/>
            </IconsContainer>
          </>
        )}
      </HeaderContainer>

      <ConstructionModal 
        isOpen={isModalOpen} 
        onClose={() => setIsModalOpen(false)}
        category={modalCategory} // Передаем категорию в модальное окно
      />
    </>
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

  const preloadImages = (category) => {
    const photos = PHOTO_CATEGORIES[category] || [];
    photos.forEach(src => {
      new Image().src = src;
    });
  };

  const getRandomPhoto = (category) => {
    const photos = PHOTO_CATEGORIES[category] || [];
    return photos[Math.floor(Math.random() * photos.length)] || '';
  };

  useEffect(() => {
    if (isMobile) {
      navItems.forEach(category => {
        preloadImages(category);
      });

      const initialCategory = navItems[0];
      setActiveItem(initialCategory);
      setCurrentPhoto(getRandomPhoto(initialCategory));

      let currentIndex = 1;
      let isFirstIteration = true;

      const cycleItems = () => {
        const category = navItems[currentIndex];
        setActiveItem(category);
        setCurrentPhoto(getRandomPhoto(category));
        currentIndex = (currentIndex + 1) % navItems.length;
        
        if (isFirstIteration) {
          isFirstIteration = false;
          clearInterval(intervalRef.current);
          intervalRef.current = setInterval(cycleItems, 5000);
        }
      };

      intervalRef.current = setTimeout(() => {
        cycleItems();
      }, 6000);

      return () => {
        clearTimeout(intervalRef.current);
        clearInterval(intervalRef.current);
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