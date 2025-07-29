// @ts-nocheck
import React from 'react';
import styled from 'styled-components';
import ShopCard from '../ShopCard';

const ShopPartsGrid = ({ nameBlock, promotions }) => {
  return (
    <GridSection>
      <HeaderContainer>
        <PromotionsHeader>{nameBlock}</PromotionsHeader>
      </HeaderContainer>
      
      <CardsGrid>
        {promotions.map((promo, index) => (
          <ShopCard
            key={index}
            imageUrl={promo.imageUrl}
            title={promo.title}
            price={promo.price}
            article={promo.article}
            availability={promo.availability}
          />
        ))}
      </CardsGrid>
    </GridSection>
  );
};

export default ShopPartsGrid;

// Стили
const GridSection = styled.section`
  max-width: 1200px;
  margin: 0 auto 60px;
  padding: 0 20px;
  position: relative;
`;

const HeaderContainer = styled.div`
  padding: 0 80px;
  margin-bottom: 30px;

  @media (max-width: 768px) {
    padding: 0 40px;
  }

  @media (max-width: 480px) {
    padding: 0 20px;
  }
`;

const PromotionsHeader = styled.h2`
  cursor: pointer;
  font-size: 2rem;
  padding-bottom: 20px;
  color: #333;
  font-weight: 600;
  position: relative;
  display: inline-block;
  margin: 0;

  &::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: 15px;
    width: 100%;
    height: 2px;
    background-color: #1a1a1a;
    border-radius: 3px;
  }

  @media (max-width: 480px) {
    font-size: 1.7rem;
    padding-bottom: 15px;
  }
`;

const CardsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
  padding: 0 80px;

  @media (max-width: 768px) {
    padding: 0 40px;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }

  @media (max-width: 480px) {
    padding: 0 20px;
    grid-template-columns: 1fr;
  }
`;