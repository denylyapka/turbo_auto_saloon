import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import styled from 'styled-components';

const CarouselContainer = styled.div`
  width: 100%;
  height: 100%;
  position: relative;

  .swiper {
    width: 100%;
    height: 100%;
  }

  .swiper-slide {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #000;
  }

  .swiper-slide img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .swiper-button-prev,
  .swiper-button-next {
    color: white;
    background: rgba(0, 0, 0, 0.5);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    &:after {
      font-size: 20px;
    }
  }

  .swiper-pagination-bullet {
    background: white;
    opacity: 0.5;
    &-active {
      opacity: 1;
    }
  }
`;

const ImageCarousel = ({ images = [] }) => {
  if (!images || images.length === 0) {
    return <div>No images available</div>;
  }

  return (
    <CarouselContainer>
      <Swiper
        modules={[Navigation, Pagination, Autoplay]}
        spaceBetween={0}
        slidesPerView={1}
        navigation
        pagination={{ clickable: true }}
        loop={true}
        autoplay={{
          delay: 5000,
          disableOnInteraction: false,
        }}
      >
        {images.map((image, index) => (
          <SwiperSlide key={index}>
            <img 
              src={image} 
              alt={`Service ${index + 1}`} 
              loading="lazy"
            />
          </SwiperSlide>
        ))}
      </Swiper>
    </CarouselContainer>
  );
};

export default ImageCarousel;