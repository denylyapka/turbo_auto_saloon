import React from 'react';
import styled from 'styled-components';

const ServiceDescription = ({ nameModule, nameService, idService }) => {
  const dataService = {
    title: nameService,
    description: 'Проснувшись однажды утром после беспокойного сна, Грегор Замза обнаружил, что он у себя в постели превратился в страшное насекомое. Лежа на панцирнотвердой спине, он видел, стоило ему приподнять голову, свой коричневый, выпуклый, разделенный дугообразными чешуйками живот, на верхушке которого еле держалось готовое вот-вот окончательно сползти одеяло. Его многочисленные, убого тонкие по сравнению с остальным телом ножки беспомощно копошились у него перед глазами. «Что со мной случилось?» – подумал он. Это не было сном. Его комната, настоящая, разве что слишком маленькая, но обычная комната, мирно покоилась в своих четырех хорошо знакомых стенах. Над столом, где были разложены распакованные образцы сукон – Замза был коммивояжером, – висел портрет, который он недавно вырезал из иллюстрированного журнала и вставил в красивую золоченую рамку. На портрете была изображена дама в меховой шляпе и боа, она сидела очень прямо и протягивала зрителю тяжелую меховую муфту, в которой целиком исчезала ее рука. Затем взгляд Грегора устремился в окно, и пасмурная погода – слышно было, как по жести подоконника стучат капли дождя – привела его и вовсе в грустное настроение. «Хорошо бы еще немного поспать и забыть всю эту чепуху», – подумал он, но это было совершенно неосуществимо, он привык спать на правом боку, а в теперешнем своемx',
  }
  return (
    <ServiceContainer>
      <Breadcrumbs>Turbo / {nameModule} / {nameService}</Breadcrumbs>
      <ServiceTitle>{nameService}</ServiceTitle>
      <ServiceText>
        {dataService.description}
      </ServiceText>
    </ServiceContainer>
  );
};

export default ServiceDescription;

// Стили
const ServiceContainer = styled.div`
  max-width: 800px;
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
  font-size: 12px;
  color: #666;
  margin-bottom: 10px;
  cursor: pointer;
`;

const ServiceTitle = styled.h1`
  font-size: 28px;
  color: #333;
  margin-bottom: 20px;
  font-weight: 600;
`;

const ServiceText = styled.p`
  font-size: 16px;
  line-height: 1.6;
  color: #444;
  text-align: justify;
`;