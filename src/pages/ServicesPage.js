import React from 'react';
import styled from 'styled-components';
import FullWidthCarousel from '../components/Carousels/Carousels';
import ServicesGrid from '../components/Cards/Services/CardsSection';
import Footer from '../components/Menu/StandartFooterMenu';

// Константы вынесены за пределы компонента
const CAROUSEL_IMAGES = [
  {"link": "https://i.pinimg.com/736x/ee/78/75/ee7875cd6b66bf03d6936d8e8f9e0c07.jpg", "color": "white"},
  {"link": "https://avatars.mds.yandex.net/get-yapic/25358/rEZhS8DXf85Y3srtGWvmOoLn3GU-1/orig", "color": "white"},
  {"link": "https://iphone24.ru/userfiles/images/all_colors__flhn5cmb1t26_large.jpeg", "color": "black"},
  {"link": "https://cdn-edge.kwork.ru/pics/t3/62/35000659-66b5265677b69.jpg", "color": "white"}
];

export const SERVICES_DATA = [
  {
    imageUrl: 'https://avatars.mds.yandex.net/get-altay/4365309/2a00000179c8a1bf373382f27b0484feb2c6/XXL_height',
    title: 'Диагностика и ремонт',
    link: '/services/1/view',
    module: 'Услуги',
    index: '0'
  },
  {
    imageUrl: 'https://grass.su/upload/medialibrary/aed/sbnlyn07mv991c2n4jbpkplf2bosgbbu.jpg',
    title: 'Программный чип тюнинг',
    link: '/services/2/view',
    module: 'Услуги',
    index: '1'
  },
  {
    imageUrl: 'https://avatars.mds.yandex.net/get-altay/5585693/2a0000017d9fb4dc2a5b0a3e22501bfa9a21/XXXL',
    title: 'Русификация и дооснащение',
    link: '/services/3/view',
    module: 'Услуги',
    index: '2'
  },
  {
    imageUrl: 'https://avatars.mds.yandex.net/get-ydo/3614230/2a0000017ff3bffd99473c6cd9ecb9e1e016/diploma',
    title: 'Тюнинг автосвета',
    link: '/services/4/view',
    module: 'Услуги',
    index: '3'
  }
];

const ServicesPage = () => {
  return (
    <>
      <FullWidthCarousel images={CAROUSEL_IMAGES} />
      <ServicesGrid services={SERVICES_DATA} />
      <Footer />
    </>
  );
};

export default ServicesPage;