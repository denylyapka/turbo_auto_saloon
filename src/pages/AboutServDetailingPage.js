import React from 'react';
import styled from 'styled-components';
import ServiceDescription from 'components/TextFields/HeadPar';

import ImageGallery from 'components/Gallery/GallerySwiper';
import HeaderServiceIT from 'components/Headers/HeaderServiceImageText';

import { BookButtonWithModal } from 'components/Buttons/ServiceButton';
import { useParams } from 'react-router-dom';
import { SERVICES_DATA } from './ServicesPage';
import { DETAILING_DATA } from './DetailingPage';
import Footer from '../components/Menu/StandartFooterMenu';

// Общие стили
const PageContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 0;
  background-color: #1A1A1A;
  color: #ffffff;
`;

const ContentWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 40px;
`;

const ButtonContainer = styled.div`
  display: flex;
  justify-content: center;
  margin: 40px 0;
`;

// Общий компонент для страниц услуг
const ServicePageTemplate = ({ service_data }) => {
  const { id } = useParams();
  
  return (
    <PageContainer>
      <ContentWrapper>
        <HeaderServiceIT 
          imageUrl={service_data.sloganImageUrl} 
          slogan={service_data.slogan}
          nameService={service_data.title}
        />

        <ServiceDescription 
          nameModule={service_data.module}
          nameService={service_data.title}
          description={service_data.description}
          idService={id}
        />
        <ImageGallery images={service_data.images} />
        <ButtonContainer>
          <BookButtonWithModal />
        </ButtonContainer>
      </ContentWrapper>
    </PageContainer>
  );
};

// Компоненты страниц
export const AboutServicePage = () => {
  const { id } = useParams();
  const service = SERVICES_DATA.find(item => item.index === id) || SERVICES_DATA[0];
  
  return (
    <>
      <ServicePageTemplate service_data={{
    ...service
    }} />
      <Footer />
    </>
  );
};

export const AboutDetailingPage = () => {
  const { id } = useParams();
  const service = DETAILING_DATA.find(item => item.index === id) || DETAILING_DATA[0];

  return (
    <>
      <ServicePageTemplate service_data={{
    ...service
    }} />
      <Footer />
    </>
  );
};