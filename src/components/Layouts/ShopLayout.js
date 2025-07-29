// @ts-nocheck
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import Header from 'components/Headers/HeaderService';
import ShopLeftMenu from 'components/Menu/ShopLeftMenu';

const LayoutContainer = styled.div`
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
    padding: 0;
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

const DefaultLayout = ({ children }) => {
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

  console.log("говно")

  return (
    <LayoutContainer>
      <HeaderWrapper>
        <Header 
          onMenuToggle={toggleMenu} 
          isMobile={isMobile} 
          menuOpen={menuOpen}
          isShop={true}
        />
      </HeaderWrapper>

      <MainLayout>
        <SideMenuContainer $isMobile={isMobile} $menuOpen={menuOpen}>
          <ShopLeftMenu 
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
          {children}
        </ContentWrapper>
      </MainLayout>
    </LayoutContainer>
  );
};

export default DefaultLayout;