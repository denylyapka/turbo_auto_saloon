import React from "react";
import styled from "styled-components";
import SvgIconsAdditionals from "../../components/SVG/Additionals";

const SearchContainer = styled.div`
  position: relative;
  width: 400px;
`;

const SearchInputLong = styled.input`
  width: 400px;
  padding: 10px 35px 10px 15px; /* Изменил порядок padding */
  border: 1px solid #e0e0e0;
  border-radius: 20px;
  font-size: 14px;
  outline: none;
  transition: all 0.2s ease;
  box-sizing: border-box;
  background-color: #f5f5f5;
  height: 30px;

  &:focus {
    border-color: #4a90e2;
    background-color: #fff;
    box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
  }

  &::placeholder {
    color: #999;
    font-size: 13px;
  }
`;

const SearchIconWrapper = styled.div`
  position: absolute;
  right: 12px; /* Изменил left на right */
  top: 50%;
  transform: translateY(-50%);
  width: 14px;
  height: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const SearchComponent = ({ placeholder = "Поиск", value, onChange }) => {
  return (
    <SearchContainer>
      <SearchInputLong
        type="text"
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
      <SearchIconWrapper>
        <SvgIconsAdditionals iconName="search" />
      </SearchIconWrapper>
    </SearchContainer>
  );
};

export default SearchComponent;