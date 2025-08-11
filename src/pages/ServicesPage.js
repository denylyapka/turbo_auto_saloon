import React from 'react';
import styled from 'styled-components';
import FullWidthCarousel from '../components/Carousels/Carousels';
import ServicesGrid from '../components/Cards/Services/CardsSection';
import Footer from '../components/Menu/StandartFooterMenu';
import { MENU_ITEMS } from '../Сonstants/MenuItems';


// Константы вынесены за пределы компонента
const CAROUSEL_IMAGES = [
  {"link": "https://i.pinimg.com/736x/ee/78/75/ee7875cd6b66bf03d6936d8e8f9e0c07.jpg", "color": "white"},
  {"link": "https://avatars.mds.yandex.net/get-yapic/25358/rEZhS8DXf85Y3srtGWvmOoLn3GU-1/orig", "color": "white"},
  {"link": "https://iphone24.ru/userfiles/images/all_colors__flhn5cmb1t26_large.jpeg", "color": "black"},
  {"link": "https://cdn-edge.kwork.ru/pics/t3/62/35000659-66b5265677b69.jpg", "color": "white"}
];

// const CAROUSEL_IMAGES = [
//   'https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/Services/Diagnostica.png',
//   'https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/Services/chip%20tuning.png',
//   'https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/Services/russifikatsiya%20i%20doosnaschenie.png',
//   'https://76bc124c-fd15-4e7c-a17c-335e579ba1d7.selstorage.ru/Turbo/Services/tuning%20avtosveta.png',
// ];


export const SERVICES_DATA = MENU_ITEMS.services.items;

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