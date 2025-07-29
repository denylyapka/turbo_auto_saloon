// src/App.js
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainLayout from './components/Layouts/MainLayout';
import ServicesPage from './pages/ServicesPage';
import DetailingPage from './pages/DetailingPage';
import { ShopMainPage, ShopPartsPage, ShopChemistryPage } from './pages/ShopPage';
import DefaultLayout from 'components/Layouts/DefaultLayout';
import ShopLayout from 'components/Layouts/ShopLayout';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />} />


        <Route path="/detailing" element={
          <DefaultLayout>
            <DetailingPage />
          </DefaultLayout>
        } />


        <Route path="/services" element={
          <DefaultLayout>
            <ServicesPage />
          </DefaultLayout>
        } />


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


        <Route path="/pay-info" element={
          <ShopLayout>
            <h1>pay-info</h1>
          </ShopLayout>
        } />
        <Route path="/delivery" element={
          <ShopLayout>
            <h1>delivery</h1>
          </ShopLayout>
        } />
        <Route path="/return" element={
          <ShopLayout>
            <h1>return</h1>
          </ShopLayout>
        } />

      </Routes>
    </BrowserRouter>
  );
};

export default App;