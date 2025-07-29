import React from 'react';
import LiquidGlass from 'liquid-glass-react';

// Стилизованная кнопка iOS
export function IosButton({ children, top = '', left = '', onClick, color }) {
  const containerRef = React.useRef(null);

  return (
    <LiquidGlass
      displacementScale={Math.floor(Math.random() * 15) + 12}
      blurAmount={0}
      saturation={130}
      aberrationIntensity={10}
      elasticity={0.85}
      cornerRadius={10}
      padding="8px 16px"
      onClick={onClick}
      mode="standard"  // "standard" | "polar" | "prominent" | "shader"
      mouseContainer={containerRef}
      style={{ position: 'absolute', top: top, left: left }}
    >
      <span style={{ 
        color: color, 
        fontWeight: 500,
        cursor: 'pointer',
        fontSize: '16px',
        verticalAlign: 'top',
      }}>
        {children || 'Кнопка'}
      </span>
    </LiquidGlass>
  );
}
