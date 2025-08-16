import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainLayout from './components/Layouts/MainLayout/MainLayout';
import ServicesPage from './pages/ServicesPage';
import DetailingPage from './pages/DetailingPage';
import { ShopMainPage, ShopPartsPage, ShopChemistryPage } from './pages/ShopPage';
import DefaultLayout from 'components/Layouts/DefaultLayout';
import ShopLayout from 'components/Layouts/ShopLayout';
import { AboutServicePage, AboutDetailingPage } from './pages/AboutServDetailingPage';
import InformationPage from './pages/InformationPage';
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    background-color: #1A1A1A;
    margin: 0;
    font-family: 'Gilroy', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: white; /* Добавляем белый цвет текста по умолчанию */
  }

  /* Дополнительно: убедимся, что корневой div занимает всю высоту */
  #root {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
`;

const App = () => {
  return (
    <>
      <GlobalStyle />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<MainLayout />} />

          {/* Детейлинг раздел */}
          <Route path="/detailing" element={
            <DefaultLayout>
              <DetailingPage />
            </DefaultLayout>
          } />
          <Route 
            path="/detailing/:id/view" 
            element={
              <DefaultLayout>
                <AboutDetailingPage />
              </DefaultLayout>
            } 
          />

          {/* Сервис раздел */}
          <Route path="/services" element={
            <DefaultLayout>
              <ServicesPage />
            </DefaultLayout>
          } />
          <Route 
            path="/services/:id/view" 
            element={
              <DefaultLayout>
                <AboutServicePage />
              </DefaultLayout>
            } 
          />

          {/* Магазин */}
          <Route path="/shop" element={
            <ShopLayout>
              <ShopMainPage />
            </ShopLayout>
          } />
          <Route path="/shop/kxhimiya" element={
            <ShopLayout>
              <ShopChemistryPage />
            </ShopLayout>
          } />
          <Route path="/shop/zapchasti" element={
            <ShopLayout>
              <ShopPartsPage />
            </ShopLayout>
          } />

          {/* Информационные страницы */}
          <Route path="/pay-info" element={
            <DefaultLayout>
              <InformationPage pageType="payment" />
            </DefaultLayout>
          } />
          <Route path="/delivery" element={
            <DefaultLayout>
              <InformationPage pageType="delivery" />
            </DefaultLayout>
          } />
          <Route path="/return" element={
            <DefaultLayout>
              <InformationPage pageType="returns" />
            </DefaultLayout>
          } />
        </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;