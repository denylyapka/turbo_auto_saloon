import React from 'react';
import styled from 'styled-components';
import ServiceDescription from 'components/TextFields/HeadPar';
import FullWidthCarousel from 'components/Carousels/Carousels';
import { BookButtonWithModal } from 'components/Buttons/ServiceButton';
import { useParams } from 'react-router-dom';
import { SERVICES_DATA } from './ServicesPage';
import { DETAILING_DATA } from './DetailingPage';

// Общие стили
const PageContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 0;
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
const ServicePageTemplate = ({ serviceData }) => {
  const { id } = useParams();
  
  return (
    <PageContainer>
      <ContentWrapper>
        <FullWidthCarousel images={serviceData.images} />
        <ServiceDescription 
          nameModule={serviceData.module}
          nameService={serviceData.title}
          idService={id}
        />
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
  
  return <ServicePageTemplate serviceData={{
    ...service,
    images: [
      {"link": 'https://wallpapers.com/images/featured/garage-pictures-6nzenybxfuxbfaar.jpg', "color": "white"},
      {"link": 'https://i2.wp.com/www.bobygarage.com/blog/wp-content/uploads/2019/01/shutterstock_666932353.jpeg', "color": "white"},
      {"link": 'https://www.sportcar-center.com/files/391515/Service_vesna_h.jpg', "color": "white"},
      {"link": 'https://findesk.ru/upload/iblock/815/8156a7adf565b08d8266330e17f095a2.jpg', "color": "white"}
    ]
  }} />;
};

export const AboutDetailingPage = () => {
  const { id } = useParams();
  const service = DETAILING_DATA.find(item => item.index === id) || DETAILING_DATA[0];
  
  return <ServicePageTemplate serviceData={{
    ...service,
    images: [
      {"link": 'https://wallpapers.com/images/featured/garage-pictures-6nzenybxfuxbfaar.jpg', "color": "white"},
      {"link": 'https://i2.wp.com/www.bobygarage.com/blog/wp-content/uploads/2019/01/shutterstock_666932353.jpeg', "color": "white"},
      {"link": 'https://www.sportcar-center.com/files/391515/Service_vesna_h.jpg', "color": "white"},
      {"link": 'https://findesk.ru/upload/iblock/815/8156a7adf565b08d8266330e17f095a2.jpg', "color": "white"}
    ]
  }} />;
};