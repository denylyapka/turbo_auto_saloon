import React, { useState } from 'react';
import styled from 'styled-components';

const ProductCard = ({ 
  imageUrl, 
  price, 
  title, 
  article, 
  availability,
  onClick 
}) => {
  const [isPressed, setIsPressed] = useState(false);

  const handleClick = () => {
    setIsPressed(true);
    setTimeout(() => setIsPressed(false), 200);
    if (onClick) onClick();
  };

  return (
    <StyledCardContainer 
      style={{ transform: isPressed ? 'scale(0.98)' : 'scale(1)' }}
      onClick={handleClick}
    >
      <ImageContainer>
        <ProductImage src={imageUrl} alt={title} />
      </ImageContainer>
      
      <DetailsContainer>
        <Price>{price} ₽</Price>
        <Title>{title}</Title>
        <Article>{article}</Article>
        <Availability style={{ color: availability === 'В наличии' ? '#4CAF50' : '#FF9800' }}>
          {availability}
        </Availability>
      </DetailsContainer>
    </StyledCardContainer>
  );
};

// Стилизованные компоненты
const StyledCardContainer = styled.div`
  width: 310px;
  height: 380px;
  background: white;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s ease;
  
  &:hover {
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
  }
`;

const ImageContainer = styled.div`
  width: 100%;
  height: 190px;
  overflow: hidden;
`;

const ProductImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
  
  ${StyledCardContainer}:hover & {
    transform: scale(1.05);
  }
`;

const DetailsContainer = styled.div`
  width: 100%;
  height: 190px;
  padding: 20px;
  background: #494949;
  margin-top: -10px;
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
`;

const Price = styled.h1`
  font-size: 22px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 10px 0;
`;

const Title = styled.h2`
  font-size: 16px;
  font-weight: 500;
  color: #fff;
  margin: 0 0 8px 0;
  flex-grow: 0.5;
`;

const Article = styled.p`
  font-size: 14px;
  color: #fff;
  margin: 0 0 8px 0;
`;

const Availability = styled.p`
  font-size: 14px;
  font-weight: 500;
  margin: 0;
`;

export default ProductCard;