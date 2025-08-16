import React from 'react';
import styled from 'styled-components';
import SvgIconsFooter from 'components/SVG/Footer';
import SITE_CONSTANTS from '../../Сonstants/siteConstants';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <FooterContainer>
      <FooterColumns>
        {/* Колонка 1: Полезные ссылки */}
        <FooterColumn>
          <ColumnTitle>Полезные ссылки</ColumnTitle>
          <LinkList>
            <LinkItem>
              <StyledLink to="/delivery">Доставка</StyledLink>
            </LinkItem>
            <LinkItem>
              <StyledLink to="/pay-info">Оплата</StyledLink>
            </LinkItem>
            <LinkItem>
              <StyledLink to="/return">Возврат</StyledLink>
            </LinkItem>
            <LinkItem>
              <StyledLink to="/privacy">Политика конфиденциальности</StyledLink>
            </LinkItem>
            <LinkItem>
              <StyledLink to="/agreement">Пользовательское соглашение</StyledLink>
            </LinkItem>
          </LinkList>
        </FooterColumn>

        {/* Колонка 2: Способы оплаты */}
        <FooterColumn>
          <ColumnTitle>Оплата</ColumnTitle>
          <LinkList>
            <LinkItem>
              <StyledLink to="/pay-info">QR-кодом на сайте (СБП)</StyledLink>
            </LinkItem>
            <LinkItem>
              <StyledLink to="/pay-info">Банковской картой на сайте</StyledLink>
            </LinkItem>
            <LinkItem>
              <StyledLink to="/pay-info">Банковской картой или QR-кодом при получении</StyledLink>
            </LinkItem>
          </LinkList>
        </FooterColumn>

        {/* Колонка 3: Контакты */}
        <FooterColumn>
          <ColumnTitle>Контакты</ColumnTitle>
          <ContactList>
            <ContactItem onClick={() => window.location.href = `tel:${SITE_CONSTANTS.contacts.phone}`}>
              {SITE_CONSTANTS.contacts.phone}
            </ContactItem>
            <ContactItem onClick={() => window.location.href = `mailto:${SITE_CONSTANTS.contacts.email}`}>
              {SITE_CONSTANTS.contacts.email}
            </ContactItem>
          </ContactList>
        </FooterColumn>

        {/* Колонка 4: Соцсети */}
        <FooterColumn>
          <ColumnTitle>Социальные сети</ColumnTitle>
          <SocialIcons>
            <SocialIcon href={SITE_CONSTANTS.socialLinks.telegram} aria-label="Telegram" target="_blank" rel="noopener noreferrer">
              <SvgIconsFooter iconName="telegram" />
            </SocialIcon>
          </SocialIcons>
        </FooterColumn>
      </FooterColumns>

      <Divider />

      <Copyright>© Turbo 2025</Copyright>
    </FooterContainer>
  );
};

export default Footer;

// Новый стиль для ссылок
const StyledLink = styled(Link)`
  color: inherit;
  text-decoration: none;
  display: block;
  width: 100%;
  height: 100%;

  &:hover {
    color: inherit;
  }
`;

// Остальные стили остаются без изменений
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
  cursor: pointer;

  &:hover {
    color: #ffffff;
  }
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
  width: 100%;
  max-width: 1200px;
`;

const Copyright = styled.div`
  text-align: left;
  font-size: 14px;
  color: #999999;
  padding-top: 20px;
`;