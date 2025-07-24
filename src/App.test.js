import React, { useState } from 'react';
import SearchComponent from './components/Searchs/Search';
import ProductCard from './components/Cards/ProductCards';
import FullWidthCarousel from './components/Carousels/Carousels';

function App() {
  // Состояния для поиска
  const [searchValue, setSearchValue] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  
  // Состояния для тестовых товаров
  const [products] = useState([
    {
      id: 1,
      imageUrl: 'https://cdn1.ozone.ru/s3/multimedia-j/6410315419.jpg',
      price: '49 990',
      title: 'Смартфон Apple iPhone 14 pro',
      article: 'APL13123',
      availability: 'В наличии'
    },
    {
      id: 2,
      imageUrl: 'https://cdn1.ozone.ru/s3/multimedia-1-m/7501194274.jpg',
      price: '64 990',
      title: 'Смартфон Samsung Galaxy S21',
      article: 'SMG21892',
      availability: 'Под заказ'
    },
    {
      id: 3,
      imageUrl: 'https://avatars.mds.yandex.net/get-mpic/4372959/2a000001921f569f7277fd7e6e281ee4cde3/orig',
      price: '52 990',
      title: 'Смартфон Xiaomi 12',
      article: 'XM12001',
      availability: 'В наличии'
    }
  ]);

  // Изображения для карусели
  const carouselImages = [
    'https://avatars.mds.yandex.net/i?id=30e3fd08f47e27c863fcba8054a8132f_l-6071858-images-thumbs&n=13',
    'https://images.wallpaperscraft.com/image/single/paint_grunge_green_124502_2560x1024.jpg',
    'https://t3.ftcdn.net/jpg/04/74/44/82/360_F_474448281_7aHi35l75IQFuF3L6UgBkNhCVOD608sw.jpg'
  ];

  // Состояние для управления автопрокруткой карусели
  const [autoPlay, setAutoPlay] = useState(true);

  // Функция для имитации поиска
  const handleSearch = (value) => {
    setSearchValue(value);
    
    // Имитация результатов поиска
    if (value.length > 0) {
      const filtered = products.filter(product => 
        product.title.toLowerCase().includes(value.toLowerCase()) ||
        product.article.toLowerCase().includes(value.toLowerCase())
      );
      
      setSearchResults(filtered.length > 0 ? filtered : null);
    } else {
      setSearchResults(null);
    }
  };

  // Обработчик клика по карточке
  const handleProductClick = (productId) => {
    console.log('Выбрана карточка товара:', productId);
    // Здесь может быть переход на страницу товара или открытие модального окна
  };

    // Обработчики для теста кнопок
  const handleButtonClick = (buttonType) => {
    console.log(`Кнопка "${buttonType}" была нажата`);
    alert(`Вы нажали кнопку: ${buttonType}`);
  };


  return (
    <div style={{ padding: '10px', maxWidth: '1200px', margin: '0 auto' }}>
      <h1>Тестирование компонентов</h1>
      
      {/* Секция тестирования карусели */}
      {/* <div style={{ marginBottom: '40px', border: '1px solid #eee', padding: '20px', borderRadius: '8px' }}>
        <h2>Тест карусели:</h2>
        <div style={{ marginBottom: '20px' }}>
          <label>
            <input
              type="checkbox"
              checked={autoPlay}
              onChange={() => setAutoPlay(!autoPlay)}
              style={{ marginRight: '10px' }}
            />
            Автопрокрутка
          </label>
        </div>
        
        <div style={{ height: '400px', position: 'relative', marginBottom: '20px' }}>
          <FullWidthCarousel images={carouselImages} autoPlay={autoPlay} />
        </div>
        
        <div style={{ backgroundColor: '#f5f5f5', padding: '15px', borderRadius: '4px' }}>
          <h4>Тестируемые функции:</h4>
          <ul>
            <li>Автопрокрутка изображений (включена по умолчанию)</li>
            <li>Ручная навигация (кнопки влево/вправо)</li>
            <li>Индикаторы текущего слайда</li>
            <li>Плавные переходы между слайдами</li>
            <li>Адаптивность под размер контейнера</li>
          </ul>
        </div>
      </div> */}

      {/* Секция тестирования кнопок */}
      <div style={{ marginBottom: '40px', border: '1px solid #eee', padding: '20px', borderRadius: '8px' }}>
        <h2>Тест кнопок:</h2>
        
        <div style={{ display: 'flex', gap: '15px', marginBottom: '20px', flexWrap: 'wrap' }}>
          <button 
            style={{ padding: '10px 20px', background: '#007bff', color: 'white', border: 'none', borderRadius: '4px' }}
            onClick={() => handleButtonClick('Основная')}
          >
            Основная кнопка
          </button>
          
          <button 
            style={{ padding: '10px 20px', background: '#6c757d', color: 'white', border: 'none', borderRadius: '4px' }}
            onClick={() => handleButtonClick('Вторичная')}
          >
            Вторичная кнопка
          </button>
          
          <button 
            style={{ padding: '10px 20px', background: 'transparent', color: '#007bff', border: '1px solid #007bff', borderRadius: '4px' }}
            onClick={() => handleButtonClick('Контурная')}
          >
            Контурная кнопка
          </button>
        </div>
      </div>

      {/* Секция тестирования поиска */}
      <div style={{ marginBottom: '40px' }}>
        <h2>Тест поиска:</h2>
        <SearchComponent 
          placeholder="Поиск товаров..."
          value={searchValue}
          onChange={(e) => handleSearch(e.target.value)}
        />
        
        {searchResults && searchResults.length > 0 ? (
          <div style={{ marginTop: '20px' }}>
            <h3>Результаты поиска:</h3>
            <div style={{ 
              display: 'grid', 
              gridTemplateColumns: 'repeat(auto-fill, minmax(310px, 1fr))',
              gap: '20px',
              marginTop: '15px'
            }}>
              {searchResults.map(product => (
                <ProductCard
                  key={product.id}
                  onClick={() => handleProductClick(product.id)}
                  {...product}
                />
              ))}
            </div>
          </div>
        ) : searchValue && searchResults !== null ? (
          <div style={{ marginTop: '15px', color: '#666' }}>
            Ничего не найдено по запросу "{searchValue}"
          </div>
        ) : null}
      </div>

      {/* Секция тестирования карточек товаров */}
      <div>
        <h2>Тест карточек товаров:</h2>
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fill, minmax(310px, 0.4fr))',
          gap: '20px',
          marginTop: '15px'
        }}>
          {products.map(product => (
            <ProductCard
              key={product.id}
              onClick={() => handleProductClick(product.id)}
              {...product}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;