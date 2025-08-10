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

const App = () => {
  return (
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
          <ShopLayout>
            <InformationPage pageType="payment" />
          </ShopLayout>
        } />
        <Route path="/delivery" element={
          <ShopLayout>
            <InformationPage pageType="delivery" />
          </ShopLayout>
        } />
        <Route path="/return" element={
          <ShopLayout>
            <InformationPage pageType="returns" />
          </ShopLayout>
        } />
      </Routes>
    </BrowserRouter>
  );
};

export default App;