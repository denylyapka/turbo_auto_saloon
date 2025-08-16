import React from 'react';
import PropTypes from 'prop-types';
import TextPage from '../components/TextFields/InfoPage';
import { PAGES_DATA } from 'Сonstants/PagesData';
import Footer from '../components/Menu/StandartFooterMenu';


const InformationPage = ({ pageType }) => {
  const pageData = PAGES_DATA[pageType] || PAGES_DATA.payment;

  return (
    <>
      <TextPage pageData={pageData} />
      <Footer />
    </>
  );
};

InformationPage.propTypes = {
  pageType: PropTypes.oneOf(['payment', 'delivery', 'returns'])
};

InformationPage.defaultProps = {
  pageType: PropTypes.oneOf(['payment', 'delivery', 'returns'])
};

export default InformationPage;