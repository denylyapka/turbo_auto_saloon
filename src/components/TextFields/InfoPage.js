import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const PageContainer = styled.div`
  max-width: 800px;
  padding: 20px 100px;
  font-family: Arial, sans-serif;
  line-height: 1.4;
  font-size: 2;
  color: #fff;

  @media (max-width: 768px) {
    padding: 20px 60px;
  }

  @media (max-width: 480px) {
    padding: 20px 40px;
    font-size: 11px;
  }

`;

const Title = styled.h1`
  font-size: 28px;
  margin-bottom: 30px;
  text-align: left;
  color: #222;
`;

const Section = styled.section`
  margin-bottom: 30px;
  padding-bottom: 15px;

  &:last-child {
    border-bottom: none;
  }
`;

const SectionTitle = styled.h2`
  font-size: 22px;
  margin-bottom: 15px;
  color: #fff;
`;

const Paragraph = styled.p`
  margin-bottom: 15px;
  color: #555;
  font-size: 16px;
`;

const List = styled.ul`
  margin: 15px 0;
  padding-left: 20px;
  list-style-type: none;
`;

const ListItem = styled.li`
  margin-bottom: 8px;
  position: relative;
  padding-left: 15px;

  &::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #666;
  }
`;

const TextPage = ({ pageData }) => {
  return (
    <PageContainer>
      <Title>{pageData.title}</Title>
      
      {pageData.sections.map((section, index) => (
        <Section key={`section-${index}`}>
          <SectionTitle>{section.title}</SectionTitle>
          
          {section.content.map((contentItem, contentIndex) => {
            if (Array.isArray(contentItem)) {
              return (
                <List key={`list-${index}-${contentIndex}`}>
                  {contentItem.map((item, itemIndex) => (
                    <ListItem key={`item-${index}-${contentIndex}-${itemIndex}`}>
                      {item}
                    </ListItem>
                  ))}
                </List>
              );
            }
            return (
              <Paragraph key={`para-${index}-${contentIndex}`}>
                {contentItem}
              </Paragraph>
            );
          })}
        </Section>
      ))}
    </PageContainer>
  );
};

TextPage.propTypes = {
  pageData: PropTypes.shape({
    title: PropTypes.string.isRequired,
    sections: PropTypes.arrayOf(
      PropTypes.shape({
        title: PropTypes.string.isRequired,
        content: PropTypes.arrayOf(
          PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
          ])
        ).isRequired
      })
    ).isRequired
  }).isRequired
};

export default TextPage;