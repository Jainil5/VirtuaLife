import React from 'react';
import './Cards3.css';
import CardItem from './CardItem';

function Cards4() {
  return (
    
    <div className='cards'>
      <div className='cards__container'>
        <div className='cards__wrapper'>
        
          <ul className='cards__items'>
            <CardItem
              src='images/YT.webp'
              text='About VirtuaLife'
              label='Informative'
              
              path="https://www.youtube.com/watch?v=pCpuH1hJ5RE"
              
            />
            <CardItem
              src='images/comingsoon2.jpg'
              text='Subscriptions'
              label='Informative'
              
            />

          </ul>
        </div>
      </div>
    </div>
    
  );
}

export default Cards4;
