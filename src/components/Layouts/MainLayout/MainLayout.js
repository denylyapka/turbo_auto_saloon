  import React, { useState, useEffect, useRef } from 'react';
  import SvgIconsLogo from 'components/SVG/Logos';
  import SvgIconsHeader from 'components/SVG/Header';
  import { useNavigate } from 'react-router-dom';
  import { ConstructionModal } from '../../PopUps/ModalTO/ModalTO';
  import { PHOTO_CATEGORIES } from '../../../Сonstants/Photos';
  import { MENU_ITEMS } from '../../../Сonstants/MenuItems';
  import { DropdownMenu, NavButtonWrapper, NavButton, DropdownItem, FullscreenCarousel } from './MainLayoutStyles';

  const HeaderGradient = ({ isMobile, onSelectCategory, onHoverCategory, activeItem }) => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [modalCategory, setModalCategory] = useState(null);
    const navigate = useNavigate();
    const navItems = [
      { name: 'Детейлинг', category: 'detailing' },
      { name: 'Услуги', category: 'services' },
      { name: 'Магазин', category: 'shop' },
      { name: 'Подбор авто', category: 'selection' }
    ];

    const handleCategoryClick = (category) => {
      console.log('Category clicked:', category);
      
      if (category === 'shop' || category === 'selection') {
        setModalCategory(category);
        setIsModalOpen(true);
        return;
      }

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

    return (
      <>
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

        <ConstructionModal 
          isOpen={isModalOpen} 
          onClose={() => setIsModalOpen(false)}
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
        // Предзагрузка всех изображений
        navItems.forEach(category => {
          preloadImages(category);
        });

        // Немедленно устанавливаем первый элемент
        const initialCategory = navItems[0];
        setActiveItem(initialCategory);
        setCurrentPhoto(getRandomPhoto(initialCategory));

        let currentIndex = 1; // Начинаем со следующего элемента
        let isFirstIteration = true;

        const cycleItems = () => {
          const category = navItems[currentIndex];
          setActiveItem(category);
          setCurrentPhoto(getRandomPhoto(category));
          currentIndex = (currentIndex + 1) % navItems.length;
          
          if (isFirstIteration) {
            isFirstIteration = false;
            // После первой итерации устанавливаем стандартный интервал
            clearInterval(intervalRef.current);
            intervalRef.current = setInterval(cycleItems, 5000);
          }
        };

        // Первый интервал с задержкой 4 секунды
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