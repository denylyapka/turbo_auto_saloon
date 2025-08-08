import React from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';

const ServiceCard = ({ key, service }) => {
  const navigate = useNavigate();

  const handleCardClick = () => {    // Формируем URL в формате /название_блока/название_услуги/view
    const urlParts = service.link.split('/').filter(Boolean);
    const blockName = urlParts[0];
    const serviceName = urlParts[1];
    navigate(`/${blockName}/${service.index}/view`);
  };

  return (
    <CardContainer onClick={handleCardClick}>
      <ImageWrapper>
        <ServiceImage src={service.imageUrl} alt={service.title} />
      </ImageWrapper>
      <Title>{service.title}</Title>
    </CardContainer>
  );
};

export default ServiceCard;

// Стили компонента
const CardContainer = styled.div`
  min-width: 300px;  
  max-width: 470px;
  height: 250px;
  position: relative;
  overflow: hidden;
  border-radius: 0;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;

  &:hover {
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    transform: translateY(-5px);
  }
`;

const ImageWrapper = styled.div`
  width: 100%;
  height: 100%;
  overflow: hidden;
`;

const ServiceImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;

  ${CardContainer}:hover & {
    transform: scale(1.05);
  }
`;

const Title = styled.h3`
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  margin: 0;
  padding: 20px;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
  color: white;
  font-size: 22px;
  font-weight: 600;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
`;