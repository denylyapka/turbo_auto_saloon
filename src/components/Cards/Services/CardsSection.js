import React from 'react';
import styled from 'styled-components';
import ServiceCard from './ServiceCards';

const ServicesGrid = ({ services }) => {
  return (
    <div>
      <ServicesHeader>Услуги</ServicesHeader>
      <GridContainer>
        {services.map((service) => (
          <ServiceCard
            key={service.index} // Теперь key будет доступен
            service={service} // Передаем весь объект service
          />
        ))}
      </GridContainer>
    </div>
  );
};

export default ServicesGrid;

// Стили для заголовка и сетки
const ServicesHeader = styled.h1`
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
  grid-template-columns: repeat(2, 470px);
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