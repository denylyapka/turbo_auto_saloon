// src/pages/shopPages.js
import React from 'react';
import styled from 'styled-components';
import FullWidthCarousel from '../components/Carousels/Carousels';
import PromotionsCarousel from '../components/Cards/ShopMain/ShopCardsSection';
import Footer from '../components/Menu/StandartFooterMenu';
import ShopChemGrid from 'components/Cards/ShopMain/ShopChem/ShopChemCardsSection';
import ShopPartsGrid from 'components/Cards/ShopMain/ShopParts/ShopPartsCardsSection';

// Общие данные и стили
const carouselImages = [
  {"link": "https://avatars.mds.yandex.net/get-yapic/25358/rEZhS8DXf85Y3srtGWvmOoLn3GU-1/orig", "color": "white"},
  {"link": "https://iphone24.ru/userfiles/images/all_colors__flhn5cmb1t26_large.jpeg", "color": "black"},
  {"link": "https://cdn-edge.kwork.ru/pics/t3/62/35000659-66b5265677b69.jpg", "color": "white"}
];

const productsData = [
  {
    imageUrl: 'https://redp.ru/upload/foto/000046/00004606/b-1.jpg',
    title: 'GReddy Проставка М20*1,5, под масляный фильтр с термостатом',
    price: '12 990',
    article: '8716984',
    availability: 'В наличии'
  },
  {
    imageUrl: 'https://a.d-cd.net/QyAAAgGGIuA-1920.jpg',
    title: 'Блок управления гбо',
    price: '8 490',
    article: '9548623',
    availability: 'В наличии'
  },
  {
    imageUrl: 'https://ford.sto-to-auto.ru/upload/iblock/de9/kiit108yw48084zme53qtrkfh702clb4.jpg',
    title: 'Блок управления двигателем',
    price: '35 990',
    article: '7591286',
    availability: 'В наличии'
  },
  {
    imageUrl: 'https://redp.ru/upload/foto/000046/00004606/b-1.jpg',
    title: 'GReddy Проставка М20*1,5, под масляный фильтр с термостатом',
    price: '12 990',
    article: '8716984',
    availability: 'В наличии'
  },
  {
    imageUrl: 'https://a.d-cd.net/QyAAAgGGIuA-1920.jpg',
    title: 'Блок управления гбо',
    price: '8 490',
    article: '9548623',
    availability: 'В наличии'
  },
  {
    imageUrl: 'https://ford.sto-to-auto.ru/upload/iblock/de9/kiit108yw48084zme53qtrkfh702clb4.jpg',
    title: 'Блок управления двигателем',
    price: '35 990',
    article: '7591286',
    availability: 'В наличии'
  }
];

// Общие стили
const PageContainer = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
`;

const ContentSection = styled.section`
  padding: 40px 0;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
`;

const SectionTitle = styled.h2`
  cursor: pointer;
  font-size: 12px;
  color: #212121CC;
  font-weight: 600;
  padding: 0 100px;
  margin-bottom: 20px;

  @media (max-width: 768px) {
    padding: 0 60px;
  }

  @media (max-width: 480px) {
    padding: 0 40px;
    font-size: 11px;
  }
`;

// Компонент-обертка для повторяющейся логики
const ShopPageLayout = ({ title, children }) => {
  return (
    <PageContainer>
      <FullWidthCarousel images={carouselImages} />
      <ContentSection>
        <SectionTitle>{title}</SectionTitle>
        {children}
      </ContentSection>
      <Footer />
    </PageContainer>
  );
};

// Страницы
export const ShopMainPage = () => (
  <ShopPageLayout title="Turbo /">
    <PromotionsCarousel nameBlock="Акции" promotions={productsData} />
    <PromotionsCarousel nameBlock="Новинки" promotions={productsData} />
  </ShopPageLayout>
);

export const ShopPartsPage = () => (
  <ShopPageLayout title="Turbo / Автозапчасти">
    <ShopPartsGrid nameBlock="Автозапчасти" promotions={productsData} />
  </ShopPageLayout>
);

export const ShopChemistryPage = () => (
  <ShopPageLayout title="Turbo / Автохимия и аксессуары">
    <ShopChemGrid nameBlock="Автохимия" promotions={productsData} />
    <ShopChemGrid    nameBlock="Аксессуары" promotions={productsData} />
  </ShopPageLayout>
);