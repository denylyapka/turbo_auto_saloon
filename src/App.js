// @ts-nocheck
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import StandartLeftMenu from 'components/Menu/StandartLeftMenu';
import Header from 'components/Headers/HeaderService';
import FullWidthCarousel from 'components/Carousels/Carousels';
import ServicesGrid from 'components/Cards/CardsSection';
import Footer from 'components/Menu/StandartFooterMenu';

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #f5f5f5;
`;

const HeaderWrapper = styled.header`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  z-index: 2;
  background: #1A1A1A;

  @media (min-width: 769px) {
    left: 280px;
  }
`;

const MainLayout = styled.div`
  display: flex;
  flex: 1;
  margin-top: 60px;
  flex-direction: column;
`;

const SideMenuContainer = styled.div`
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  bottom: 0;
  width: 280px;
  z-index: 900;
  transform: ${({ $isMobile, $menuOpen }) => 
    $isMobile ? `translateX(${$menuOpen ? '0' : '-100%'})` : 'translateX(0)'};
  transition: transform 0.3s ease;
  background-color: #1A1A1A;
  overflow-y: auto;

  @media (max-width: 768px) {
    box-shadow: ${({ $menuOpen }) => 
      $menuOpen ? '2px 0 10px rgba(0, 0, 0, 0.5)' : 'none'};
  }
`;

const ContentWrapper = styled.main`
  flex: 1;
  padding: 0;
  margin-left: ${({ $isMobile }) => $isMobile ? '0' : '280px'};
  background-color: #ffffff;
  min-height: calc(100vh - 60px);
  display: flex;
  flex-direction: column;

  @media (max-width: 768px) {
    padding: 15px;
  }
`;

const Overlay = styled.div`
  position: fixed;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 800;
  opacity: ${({ $isMobile, $menuOpen }) => ($isMobile && $menuOpen) ? '1' : '0'};
  visibility: ${({ $isMobile, $menuOpen }) => ($isMobile && $menuOpen) ? 'visible' : 'hidden'};
  transition: opacity 0.3s ease, visibility 0.3s ease;
`;

function App() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const checkMobile = () => {
      const mobile = window.innerWidth <= 768;
      setIsMobile(mobile);
      if (!mobile) {
        setMenuOpen(true);
      } else {
        setMenuOpen(false);
      }
    };

    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  const images = [
    {"link": "https://i.pinimg.com/736x/ee/78/75/ee7875cd6b66bf03d6936d8e8f9e0c07.jpg", "color": "white"},
    {"link": "https://avatars.mds.yandex.net/get-yapic/25358/rEZhS8DXf85Y3srtGWvmOoLn3GU-1/orig", "color": "white"},
    {"link": "https://iphone24.ru/userfiles/images/all_colors__flhn5cmb1t26_large.jpeg", "color": "black"},
    {"link": "https://cdn-edge.kwork.ru/pics/t3/62/35000659-66b5265677b69.jpg", "color": "white"}
  ];

  const servicesData = [
    {
      imageUrl: 'https://avatars.mds.yandex.net/get-altay/4365309/2a00000179c8a1bf373382f27b0484feb2c6/XXL_height',
      title: 'Полировка кузова'
    },
    {
      imageUrl: 'https://grass.su/upload/medialibrary/aed/sbnlyn07mv991c2n4jbpkplf2bosgbbu.jpg',
      title: 'Защитное покрытие'
    },
    {
      imageUrl: 'https://avatars.mds.yandex.net/get-altay/5585693/2a0000017d9fb4dc2a5b0a3e22501bfa9a21/XXXL',
      title: 'Удаление вмятин'
    },
    {
      imageUrl: 'https://avatars.mds.yandex.net/get-ydo/3614230/2a0000017ff3bffd99473c6cd9ecb9e1e016/diploma',
      title: 'Химчистка салона'
    }
  ];

  return (
    <AppContainer>
      <HeaderWrapper>
        <Header 
          onMenuToggle={toggleMenu} 
          isMobile={isMobile} 
          menuOpen={menuOpen}
        />
      </HeaderWrapper>

      <MainLayout>
        <SideMenuContainer $isMobile={isMobile} $menuOpen={menuOpen}>
          <StandartLeftMenu 
            iconName="logo" 
            onClose={() => setMenuOpen(false)}
          />
        </SideMenuContainer>

        {isMobile && (
          <Overlay 
            $isMobile={isMobile} 
            $menuOpen={menuOpen}
            onClick={() => setMenuOpen(false)}
          />
        )}

        <ContentWrapper $isMobile={isMobile}>
          <FullWidthCarousel images={images} />
          <ServicesGrid services={servicesData} />
          <Footer />
        </ContentWrapper>
      </MainLayout>
    </AppContainer>
  );
}

export default App;