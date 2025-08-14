import React from 'react';
import styled from 'styled-components';
import SvgIconsFooter from 'components/SVG/Footer';
import SITE_CONSTANTS from '../../Сonstants/siteConstants';

const Footer = () => {
  return (
    <FooterContainer>
      <FooterColumns>
        {/* Колонка 1: Полезные ссылки */}
        <FooterColumn>
          <ColumnTitle>Полезные ссылки</ColumnTitle>
          <LinkList>
            <LinkItem>Доставка</LinkItem>
            <LinkItem>Оплата</LinkItem>
            <LinkItem>Акции</LinkItem>
            <LinkItem>Политика конфиденциальности</LinkItem>
            <LinkItem>Пользовательское соглашение</LinkItem>
          </LinkList>
        </FooterColumn>

        {/* Колонка 2: Способы оплаты */}
        <FooterColumn>
          <ColumnTitle>Оплата</ColumnTitle>
          <LinkList>
            <LinkItem>QR-кодом на сайте (СБП)</LinkItem>
            <LinkItem>Банковской картой на сайте</LinkItem>
            <LinkItem>Наличными</LinkItem>
            <LinkItem>Банковской картой или QR-кодом при получении</LinkItem>
          </LinkList>
        </FooterColumn>

        {/* Колонка 3: Контакты */}
        <FooterColumn>
          <ColumnTitle>Контакты</ColumnTitle>
          <ContactList>
            <ContactItem onClick={() => window.location.href = `tel:${SITE_CONSTANTS.contacts.phone}`}>{SITE_CONSTANTS.contacts.phone}</ContactItem>
            <ContactItem>{SITE_CONSTANTS.contacts.email}</ContactItem>
          </ContactList>
        </FooterColumn>

        {/* Колонка 4: Соцсети */}
        <FooterColumn>
          <ColumnTitle>Социальные сети</ColumnTitle>
          <SocialIcons>
            {/* <SocialIcon href={SITE_CONSTANTS.socialLinks.youtube} aria-label="YouTube">
              <SvgIconsFooter iconName="youtube" />
            </SocialIcon> */}
            <SocialIcon href={SITE_CONSTANTS.socialLinks.telegram} aria-label="Telegram">
              <SvgIconsFooter iconName="telegram" />
            </SocialIcon>
            {/* <SocialIcon href={SITE_CONSTANTS.socialLinks.instagram} aria-label="Instagram">
              <SvgIconsFooter iconName="instagram" />
            </SocialIcon> */}
          </SocialIcons>
        </FooterColumn>
      </FooterColumns>

      <Divider />

      <Copyright>© Turbo 2025</Copyright>
    </FooterContainer>
  );
};

export default Footer;

// Стили компонента
const FooterContainer = styled.footer`
background: linear-gradient(-30deg, #1A1A1A, #282828ff);
  color: #ffffff;
  padding: 40px 20px 20px;
  margin-top: 100px;
`;

const FooterColumns = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;

  @media (max-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (max-width: 480px) {
    grid-template-columns: 1fr;
  }
`;

const FooterColumn = styled.div`
  display: flex;
  flex-direction: column;
`;

const ColumnTitle = styled.h3`
  font-size: 18px;
  margin-bottom: 20px;
  color: #ffffff;
  font-weight: 600;
`;

const LinkList = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
`;

const LinkItem = styled.li`
  font-size: 14px;
  color: #cccccc;
  line-height: 1.5;
  transition: color 0.2s;

  &:hover {
    color: #ffffff;
    cursor: pointer;
  }
`;

const ContactList = styled.div`
  display: flex;
  flex-direction: column;
  gap: 12px;
`;

const ContactItem = styled.div`
  font-size: 14px;
  color: #cccccc;
  line-height: 1.5;
`;

const SocialIcons = styled.div`
  display: flex;
  gap: 20px;
`;

const SocialIcon = styled.a`
  color: #ffffff;
  transition: opacity 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;

  &:hover {
    opacity: 0.8;
  }

  svg {
    width: 24px;
    height: 24px;
  }
`;

const Divider = styled.div`
  height: 1px;
  background-color: #fff;
  margin: 40px auto 20px;
  width: 90%;
  max-width: 1200px;
`;

const Copyright = styled.div`
  text-align: center;
  font-size: 14px;
  color: #999999;
  padding-top: 20px;
`;