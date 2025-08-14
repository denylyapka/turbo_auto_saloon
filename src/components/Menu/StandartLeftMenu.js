// @ts-nocheck
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import SvgIconsLogo from 'components/SVG/Logos';
import SvgIconsFooter from 'components/SVG/Footer';
import SITE_CONSTANTS from '../../Сonstants/siteConstants';
import SVGButtons from 'components/Buttons/webSites';
import { useNavigate } from 'react-router-dom';

// Константы с ссылками
import { MENU_ITEMS } from '../../Сonstants/MenuItems';

const menuItems = [
  {
    title: "Детейлинг",
    category: "detailing",
    subItems: MENU_ITEMS.detailing.items
  },
  {
    title: "Услуги",
    category: "services",
    subItems: MENU_ITEMS.services.items
  },
  // {
  //   title: "Магазин",
  //   category: "shop",
  //   subItems: MENU_ITEMS.shop.items
  // },
  // {
  //   title: "Подбор авто",
  //   category: "selection",
  //   subItems: null
  // }
];

const StandartLeftMenu = ({ iconName, onClose }) => {
  const [isMobile, setIsMobile] = useState(false);
  const [openSubmenu, setOpenSubmenu] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const toggleSubmenu = (title) => {
    setOpenSubmenu(openSubmenu === title ? null : title);
  };

  const handleCategoryClick = (category) => {
    if (MENU_ITEMS[category]) {
      navigate(MENU_ITEMS[category].mainLink);
    }
    if (onClose) onClose();
  };

  const handleSubItemClick = (link, e) => {
    console.log("handleSubItemClick (link):", link);
    e.preventDefault();
    navigate(link);
    if (onClose) onClose();
  };

  return (
    <MenuContainer>
      <LogoContainer>
        <SVGButtons 
          svg={<SvgIconsLogo iconName={"logo"} size={36}/>} 
          link="/"
          title="Наш YouTube"
          className="social-button"
        />
      </LogoContainer>
      
      <MenuList>
        {menuItems.map((item) => (
          <MenuItem key={item.title}>
            {item.subItems ? (
              <>
                <MenuButton onClick={() => toggleSubmenu(item.title)}>
                  {item.title}
                  <DropdownArrow isOpen={openSubmenu === item.title} />
                </MenuButton>
                <Submenu isOpen={openSubmenu === item.title}>
                  {item.subItems.map((subItem) => (
                    <DropdownItem 
                      key={subItem.name} 
                      href={subItem.link}
                      onClick={(e) => handleSubItemClick(subItem.link, e)}
                    >
                      {subItem.name}
                    </DropdownItem>
                  ))}
                </Submenu>
              </>
            ) : (
              <MenuLink 
                href={MENU_ITEMS[item.category].mainLink} 
                onClick={(e) => {
                  e.preventDefault();
                  handleCategoryClick(item.category);
                }}
              >
                {item.title}
              </MenuLink>
            )}
            <MenuDivider />
          </MenuItem>
        ))}
      </MenuList>

      <BottomSection>
        <PhoneNumber onClick={() => window.location.href = `tel:${SITE_CONSTANTS.contacts.phone}`}>{SITE_CONSTANTS.contacts.phone}</PhoneNumber>
        <SocialIconsContainer>
          <SVGButtons 
            svg={<SvgIconsFooter iconName={"youtube"} />} 
            link={SITE_CONSTANTS.socialLinks.youtube}
            title="Наш YouTube"
            className="social-button"
          />
          <SVGButtons 
            svg={<SvgIconsFooter iconName={"telegram"} />} 
            link={SITE_CONSTANTS.socialLinks.telegram}
            title="Наш Telegram"
            className="social-button"
          />
          <SVGButtons 
            svg={<SvgIconsFooter iconName={"instagram"} />} 
            link={SITE_CONSTANTS.socialLinks.instagram}
            title="Наш Instagram"
            className="social-button"
          />
        </SocialIconsContainer>
      </BottomSection>
    </MenuContainer>
  );
};

// Стили компонента (остаются без изменений)
const MenuContainer = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 280px;
  height: 100vh;
  background-color: #1A1A1A;
  z-index: 900;
  display: flex;
  flex-direction: column;
  overflow: hidden;
`;

const LogoContainer = styled.div`
  padding: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: center;
`;

const MenuList = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
  flex-grow: 1;
`;

const MenuItem = styled.li`
  position: relative;
`;

const MenuLink = styled.a`
  display: block;
  padding: 15px 25px;
  color: #ecf0f1;
  text-decoration: none;
  font-size: 16px;
  transition: background-color 0.3s;
  cursor: pointer;
  
  &:hover {
    background-color: #2f2f2f;
  }
`;

const MenuButton = styled.button`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 15px 25px;
  color: #ecf0f1;
  text-decoration: none;
  font-size: 16px;
  transition: background-color 0.3s;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  
  &:hover {
    background-color: #2f2f2f;
  }
`;

const DropdownArrow = styled.span`
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 8px;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 5px solid #ecf0f1;
  transform: ${({ isOpen }) => isOpen ? 'rotate(180deg)' : 'rotate(0)'};
  transition: transform 0.3s ease;
`;

const Submenu = styled.div`
  max-height: ${({ isOpen }) => isOpen ? '500px' : '0'};
  overflow: hidden;
  transition: max-height 0.3s ease;
  background-color: #2a2a2a;
`;

const DropdownItem = styled.a`
  display: block;
  padding: 12px 25px 12px 35px;
  color: #ecf0f1;
  text-decoration: none;
  font-size: 14px;
  transition: background-color 0.3s;
  cursor: pointer;
  
  &:hover {
    background-color: #3a3a3a;
  }
`;

const MenuDivider = styled.div`
  height: 1px;
  background-color: rgba(255, 255, 255, 0.1);
  margin: 0 25px;
`;

const BottomSection = styled.div`
  margin-top: auto;
  padding: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
`;

const PhoneNumber = styled.div`
  color: #ecf0f1;
  font-size: 16px;
  text-align: center;
  margin-bottom: 20px;
  padding: 10px;
`;

const SocialIconsContainer = styled.div`
  display: flex;
  justify-content: center;
  gap: 20px;
`;

export default StandartLeftMenu;