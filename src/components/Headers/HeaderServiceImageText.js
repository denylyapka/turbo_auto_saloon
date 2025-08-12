import React from 'react';
import styled from 'styled-components';

const HeaderServiceIT = ({ imageUrl, slogan, nameService }) => {
  return (
    <HeaderContainer>
      <HeaderImage src={imageUrl} alt={nameService} />
      <Slogan>{slogan}</Slogan>
    </HeaderContainer>
  );
};

export default HeaderServiceIT;

// Стилизованные компоненты
const HeaderContainer = styled.header`
  position: relative;
  width: 100%;
  height: 200px; /* Вы можете настроить высоту по своему усмотрению */
  overflow: hidden;
`;

const HeaderImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
`;

const Slogan = styled.div`
  position: absolute;
  bottom: 60px;
  right: 40px;
  max-width: 60%;
  padding: 20px;
  color: white;
  font-size: 24px;
  font-weight: bold;
  text-align: right;
  border-radius: 8px;
  
  @media (max-width: 768px) {
    font-size: 18px;
    bottom: 40px;
    right: 20px;
    max-width: 60%;
  }

  @media (max-width: 480px) {
    font-size: 16px;
    padding: 10px;
    bottom: 40px;
    right: 20px;
    max-width: 70%;
  }
`;