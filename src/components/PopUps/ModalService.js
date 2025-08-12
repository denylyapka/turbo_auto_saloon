// @ts-nocheck
import React, { useState, useRef } from 'react'
import styled, { css } from 'styled-components'
import Modal from 'react-responsive-modal'
import 'react-responsive-modal/styles.css'

// Styled Components
const StyledModal = styled(Modal).attrs({
  styles: {
    modal: {
      maxWidth: 'calc(100% - 80px)',
      width: '528px',
      padding: '20px',
      borderRadius: '8px',
      margin: '20px',
      overflowY: 'auto',
    }
  }
})`
  @media (min-width: 528px) {
    .react-responsive-modal-modal {
      max-width: 528px;
      height: auto;
      padding: 30px;
    }
  }
`;

const ModalContent = styled.div`
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
`;

const ModalTitle = styled.h2`
  text-align: center;
  margin-bottom: 20px;
  color: #fff;
  font-size: 22px;

  @media (max-width: 480px) {
    font-size: 18px;
    margin-bottom: 15px;
  }
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  width: 100%;
`;

const FormFieldContainer = styled.div`
  position: relative;
  margin-bottom: 15px;

  @media (max-width: 480px) {
    margin-bottom: 12px;
  }
`;

const FloatingLabel = styled.label`
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-20%);
  font-size: 16px;
  color: #999;
  pointer-events: none;
  transition: all 0.3s ease;
  background: white;
  padding: 0 5px;
  margin-top: -8px;

  ${props => props.focused && css`
    top: 0;
    font-size: 12px;
    transform: translateY(-100%);
    color: #666;
    margin-top: -8px;
    background: white;
    padding: 0 5px;
    z-index: 1;
  `}

  @media (max-width: 480px) {
    font-size: 14px;
  }
`;

const FormInput = styled.input`
  width: 92%;
  padding: 16px 15px 12px 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  transition: all 0.3s ease;
  background-color: white;
  -webkit-tap-highlight-color: transparent;
  
  &:focus {
    outline: none;
    border-color: #666;
    box-shadow: none;
    -webkit-box-shadow: none;
  }

  &:focus + ${FloatingLabel}, 
  &:not(:placeholder-shown) + ${FloatingLabel} {
    top: 0;
    font-size: 12px;
    transform: translateY(0);
    color: #666;
  }

  &:-webkit-autofill,
  &:-webkit-autofill:hover, 
  &:-webkit-autofill:focus {
    -webkit-text-fill-color: #fff;
    -webkit-box-shadow: 0 0 0px 1000px white inset;
    transition: background-color 5000s ease-in-out 0s;
  }

  @media (max-width: 480px) {
    padding: 14px 12px 10px;
    font-size: 14px;
  }
`;

const AgreementContainer = styled.div`
  display: flex;
  gap: 10px;
  margin: 15px 0;
  align-items: flex-start;

  @media (max-width: 480px) {
    margin: 12px 0;
  }
`;

const AgreementLabel = styled.label`
  font-size: 14px;
  color: #555;
  line-height: 1.4;

  @media (max-width: 480px) {
    font-size: 12px;
    line-height: 1.3;
  }
`;

const AgreementLink = styled.a`
  color: #0066cc;
  text-decoration: none;
  
  &:hover {
    text-decoration: underline;
  }
`;

const SubmitButton = styled.button`
  width: 100%;
  background: ${props => props.disabled ? '#ccc' : '#666'};
  color: white;
  border: none;
  padding: 14px;
  border-radius: 4px;
  font-size: 16px;
  cursor: ${props => props.disabled ? 'not-allowed' : 'pointer'};
  transition: background 0.3s;
  
  &:hover {
    background: ${props => props.disabled ? '#ccc' : '#555'};
  }

  @media (max-width: 480px) {
    padding: 12px;
    font-size: 14px;
  }
`;

// Компоненты
const FormField = ({ label, type = 'text', name, value, onChange }) => {
  const [focused, setFocused] = useState(false);
  const inputRef = useRef(null);

  return (
    <FormFieldContainer>
      <FormInput
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        required
        placeholder=" "
        ref={inputRef}
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
      />
      <FloatingLabel focused={focused || value}>
        {label}
      </FloatingLabel>
    </FormFieldContainer>
  );
}

const AgreementCheckbox = ({ checked, onChange }) => (
  <AgreementContainer>
    <input
      type="checkbox"
      name="agree"
      id="agreeCheckbox"
      checked={checked}
      onChange={onChange}
      required
    />
    <AgreementLabel htmlFor="agreeCheckbox">
      Я соглашаюсь на обработку персональных данных в соответствии с{' '}
      <AgreementLink href="/privacy-policy" target="_blank" rel="noopener noreferrer">
        Политикой обработки персональных данных
      </AgreementLink>{' '}
      и с{' '}
      <AgreementLink href="/offer-agreement" target="_blank" rel="noopener noreferrer">
        Договором-офертой
      </AgreementLink>
    </AgreementLabel>
  </AgreementContainer>
)

// Основной компонент
export const AppointmentModal = ({ open, onClose }) => {
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    agree: false
  })

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('Form submitted:', formData)
    onClose()
  }

  return (
    <StyledModal
      open={open}
      onClose={onClose}
      center
      classNames={{
        overlay: 'appointment-overlay',
        closeButton: 'close-btn'
      }}
      closeOnOverlayClick={false}
    >
      <ModalContent>
        <ModalTitle>Запись на услугу</ModalTitle>
        
        <Form onSubmit={handleSubmit}>
          <FormField 
            label="Имя Фамилия"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
                  
          <FormField 
            label="Номер телефона"
            type="tel"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
          />
          
          <AgreementCheckbox 
            checked={formData.agree}
            onChange={handleChange}
          />
          
          <SubmitButton disabled={!formData.agree}>
            Записаться
          </SubmitButton>
        </Form>
      </ModalContent>
    </StyledModal>
  )
}