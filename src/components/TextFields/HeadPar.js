import React from 'react';
import styled from 'styled-components';
import { Link, useNavigate } from 'react-router-dom';

const ServiceDescription = ({ nameModule, nameService, description, idService }) => {
  const navigate = useNavigate();

  const handleModuleClick = () => {
    // Проверяем название модуля и формируем соответствующий путь
    let path;
    
    if (nameModule === 'Услуги') {
      path = '/services';
    } else if (nameModule === 'Детейлинг') {
      path = '/detailing';
    } else {
      path = `/${nameModule.toLowerCase()}`;
    }
    navigate(path);
  };

  return (
    <ServiceContainer>
      <Breadcrumbs>
        <CrumbLink to="/">Turbo</CrumbLink>
        <Separator>/</Separator>
        <ModuleCrumb onClick={handleModuleClick}>
          {nameModule}
        </ModuleCrumb>
        <Separator>/</Separator>
        <CurrentCrumb>{nameService}</CurrentCrumb>
      </Breadcrumbs>

      <ServiceTitle>{nameService}</ServiceTitle>
      <ServiceText style={{ whiteSpace: 'pre-line' }}>
        {description}
      </ServiceText>
    </ServiceContainer>
  );
};

export default ServiceDescription;

// Стилизованные компоненты
const ServiceContainer = styled.div`
  max-width: 600px;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  font-size: 12px;
  padding: 0 100px;
  margin-bottom: 20px;

  @media (max-width: 768px) {
    padding: 0 60px;
  }

  @media (max-width: 480px) {
    padding: 0 40px;
    font-size: 11px;
  }
`;

const Breadcrumbs = styled.div`
  display: flex;
  align-items: center;
  font-size: 12px;
  color: #666;
  margin-bottom: 10px;
`;

const CrumbLink = styled(Link)`
  color: #fff;
  text-decoration: none;
  transition: color 0.2s;
  cursor: pointer;

  &:hover {
    color: #949494ff;
    text-decoration: underline;
  }
`;

const ModuleCrumb = styled.span`
  color: #fff;
  cursor: pointer;
  transition: color 0.2s;

  &:hover {
    color: #6e6e6eff;
    text-decoration: underline;
  }
`;

const Separator = styled.span`
  margin: 0 5px;
  color: #999;
`;

const CurrentCrumb = styled.span`
  color: #fff;
  font-weight: 500;
`;

const ServiceTitle = styled.h1`
  font-size: 28px;
  color: #fff;
  margin-bottom: 20px;
  font-weight: 600;
`;

const ServiceText = styled.p`
  font-size: 16px;
  line-height: 1.6;
  color: #fff;
  text-align: justify;
`;