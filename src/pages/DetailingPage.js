// src/pages/DetailingPage.js
import React, { useEffect } from 'react';
import styled from 'styled-components';
import FullWidthCarousel from '../components/Carousels/Carousels';
import DetailingGrid from '../components/Cards/Detailing/CardsSection';
import Footer from '../components/Menu/StandartFooterMenu';
import { MENU_ITEMS } from '../Сonstants/MenuItems';

// Константы вынесены за пределы компонента
const CAROUSEL_IMAGES = [
  {"link": "https://i.pinimg.com/736x/ee/78/75/ee7875cd6b66bf03d6936d8e8f9e0c07.jpg", "color": "white"},
  {"link": "https://avatars.mds.yandex.net/get-yapic/25358/rEZhS8DXf85Y3srtGWvmOoLn3GU-1/orig", "color": "white"},
  {"link": "https://iphone24.ru/userfiles/images/all_colors__flhn5cmb1t26_large.jpeg", "color": "black"},
  {"link": "https://cdn-edge.kwork.ru/pics/t3/62/35000659-66b5265677b69.jpg", "color": "white"}
];

export const DETAILING_DATA = MENU_ITEMS.detailing.items;

const DetailingPage = () => {
  // useEffect(() => {
  //   const intervalId = setInterval(() => {
  //     window.location.reload();
  //   }, 5000); // Перезагрузка каждые 5 секунд

  //   return () => clearInterval(intervalId); // Очистка интервала при размонтировании
  // }, []);

  return (
    <>
      <FullWidthCarousel images={CAROUSEL_IMAGES} />
      <DetailingGrid services={DETAILING_DATA} />
      <Footer />
    </>
  );
};

export default DetailingPage;