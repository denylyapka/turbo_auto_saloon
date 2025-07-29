// @ts-nocheck
import React, { useState } from 'react';
import styled from 'styled-components';
import ShopCard from './ShopCard';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';

const PromotionsCarousel = ({ nameBlock, promotions }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  
  const visibleCards = 3;
  
  const nextSlide = () => {
    setCurrentIndex(prev => Math.min(prev + 1, promotions.length - visibleCards));
  };
  
  const prevSlide = () => {
    setCurrentIndex(prev => Math.max(prev - 1, 0));
  };

  return (
    <CarouselSection>
      <HeaderContainer>
        <PromotionsHeader>{nameBlock}</PromotionsHeader>
      </HeaderContainer>
      
      <ContentWrapper>
        <CarouselContainer>
          <CardsWindow>
            <CardsTrack style={{ transform: `translateX(-${currentIndex * 330}px)` }}>
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
            </CardsTrack>
          </CardsWindow>
        </CarouselContainer>

        <ButtonsContainer>
          <NavButton 
            onClick={prevSlide} 
            disabled={currentIndex === 0}
            aria-label="Предыдущие акции"
          >
            <FaChevronLeft />
          </NavButton>
          <NavButton 
            onClick={nextSlide} 
            disabled={currentIndex >= promotions.length - visibleCards}
            aria-label="Следующие акции"
          >
            <FaChevronRight />
          </NavButton>
        </ButtonsContainer>
      </ContentWrapper>
    </CarouselSection>
  );
};

export default PromotionsCarousel;

// Стили
const CarouselSection = styled.section`
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

const ContentWrapper = styled.div`
  padding: 0 80px;

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

const CarouselContainer = styled.div`
  margin-bottom: 20px;
  width: 100%;
`;

const CardsWindow = styled.div`
  width: 100%;
  max-width: 990px;
  overflow: hidden;
  margin: 0 auto;
`;

const CardsTrack = styled.div`
  display: flex;
  gap: 30px;
  transition: transform 0.4s ease-out;
  width: max-content;
`;

const ButtonsContainer = styled.div`
  display: flex;
  justify-content: flex-end;
  gap: 15px;
  margin-top: 20px;
  width: 100%;
`;

const NavButton = styled.button`
  background: #555555;
  border: none;
  border-radius: 5px;
  width: 86px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s;
  
  &:hover {
    background: #626262;
    scale: 1.1;
  }
  
  &:disabled {
    opacity: 0.3;
    cursor: not-allowed;
    scale: 1;
  }
  
  svg {
    color: #fff;
    font-size: 1.2rem;
  }

  @media (max-width: 700px) {
    width: 40px;
    height: 40px;
    background: #555555;
  }
`;