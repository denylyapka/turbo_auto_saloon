import React from 'react';
import styled from 'styled-components';
import DetailingCard from './DetailingCards';

const DetailingGrid = ({ services }) => {
  return (
    <div>
      <DetailingHeader>Детейлинг</DetailingHeader>
      <GridContainer>
        {services.map((service) => (
          <DetailingCard
            key={service.index}
            service={service}
          />
        ))}
      </GridContainer>
    </div>
  );
};

export default DetailingGrid;

// Стили для заголовка и сетки (адаптированы под новую логику)
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
  grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
  justify-content: center;
  gap: 30px;
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;

  @media (max-width: 768px) {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  }

  @media (max-width: 480px) {
    grid-template-columns: 1fr;
    padding: 20px 50px;
  }
`;