// @ts-nocheck

import React, { useState, useEffect, useRef } from 'react';
import styled from 'styled-components';
import { IosButton } from '../Buttons/iosButton';


const FullWidthCarousel = ({ images }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAutoPlay, setIsAutoPlay] = useState(false);
  const carouselRef = useRef(null);
  const intervalRef = useRef(null);

  // Автопрокрутка
  useEffect(() => {
    if (isAutoPlay) {
      intervalRef.current = setInterval(() => {
        goToNext();
      }, 5000);
    }
    return () => clearInterval(intervalRef.current);
  }, [isAutoPlay, currentIndex]);

  const goToSlide = (index) => {
    setCurrentIndex(index);
    setIsAutoPlay(false);
    setTimeout(() => setIsAutoPlay(true), 10000);
  };

  const goToPrev = () => {
    setCurrentIndex(prev => (prev - 1 + images.length) % images.length);
  };

  const goToNext = () => {
    setCurrentIndex(prev => (prev + 1) % images.length);
  };


  return (
    <CarouselContainer>
      <CarouselTrack
        ref={carouselRef}
        style={{ transform: `translateX(-${currentIndex * 100}%)` }}
      >
        {images.map((img, index) => (
          <Slide key={index}>
            <SlideImage src={img["link"]} alt={`Slide ${index + 1}`} />
          </Slide>
        ))}
      </CarouselTrack>

      {/* Кнопка "Назад" с эффектом LiquidGlass */}
      <IosButton top="50%" left="10%" children="Сюда" onClick={goToPrev} color="white"></IosButton>
      {/* Кнопка "Вперед" с эффектом LiquidGlass */}
      <IosButton top="50%" left="90%" children="Туда" onClick={goToNext} color="white"></IosButton>

      <Indicators>
        {images.map((_, index) => (
          <IndicatorLine
            key={index}
            $active={index === currentIndex}
            onClick={() => goToSlide(index)}
          />
        ))}
      </Indicators>
    </CarouselContainer>
  );
};

// Стили
const CarouselContainer = styled.div`
  position: relative;
  width: 100%;
  height: 300px;
  overflow: hidden;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
`;

const CarouselTrack = styled.div`
  display: flex;
  height: 100%;
  transition: transform 0.5s ease;
`;

const Slide = styled.div`
  min-width: 100%;
  height: 100%;
`;

const SlideImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
`;

const Indicators = styled.div`
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 8px;
  z-index: 10;
`;

const IndicatorLine = styled.div`
  width: 34px;
  height: ${props => props.$active ? '3px' : '2px'};
  background: ${props => props.$active ? 'white' : 'rgba(255, 255, 255, 0.5)'};
  cursor: pointer;
  transition: background 0.3s ease;
  border-radius: 2px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 1);

  &:hover {
    background: white;
  }
`;

export default FullWidthCarousel;