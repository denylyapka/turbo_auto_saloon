import styled from 'styled-components';
import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination, A11y, Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/autoplay';

const ImageGallery = ({ images }) => {
  return (
    <SwiperContainer>
      <Swiper
        modules={[Navigation, Pagination, A11y, Autoplay]}
        spaceBetween={0}
        slidesPerView={1}
        navigation
        pagination={{ clickable: true }}
        loop={true}
        autoplay={{ delay: 5000 }}
        onSwiper={(swiper) => console.log(swiper)}
        onSlideChange={() => console.log('slide change')}
      >
        {images.map((img, index) => (
          <SwiperSlide key={index}>
            <SlideImage src={img} alt={`Slide ${index}`} />
          </SwiperSlide>
        ))}
      </Swiper>
    </SwiperContainer>
  );
};

export default ImageGallery;

// Стили
const SwiperContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  
  .swiper-button-prev,
  .swiper-button-next {
    color: white;
    background: rgba(0, 0, 0, 0.5);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    transition: all 0.3s;
    
    &:hover {
      background: rgba(0, 0, 0, 0.8);
    }
    
    &::after {
      font-size: 1.2rem;
    }
  }
  
  .swiper-pagination-bullet {
    background: rgba(255, 255, 255, 0.5);
    opacity: 1;
    
    &-active {
      background: white;
    }
  }
`;

const SlideImage = styled.img`
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
`;