import React from 'react';
import styled from 'styled-components';
import DetailingCards from './DetailingCards';

const DetailingGrid = ({ services }) => {
  return (
    <div>
      <DetailingHeader>Детейлинг</DetailingHeader>
      <GridContainer>
        {services.map((service, index) => (
          <DetailingCards
            key={index}
            imageUrl={service.imageUrl}
            title={service.title}
          />
        ))}
      </GridContainer>
    </div>
  );
};

export default DetailingGrid;

// Стили для заголовка и сетки
const DetailingHeader = styled.h1`
  margin: 40px auto 10px auto;
  text-align: center;
  font-size: 2.5rem;
  color: #000;
  padding-bottom: 10px;
  position: relative;
  font-weight: 500;
`;

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 310px);
  justify-content: center;
  gap: 30px;
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;

  @media (max-width: 1000px) {
    grid-template-columns: 470px;
  }

  @media (max-width: 500px) {
    grid-template-columns: 1fr;
    padding: 20px 10px;
  }
`;