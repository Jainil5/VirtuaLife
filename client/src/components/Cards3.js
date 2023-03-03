import React from 'react';
import './Cards3.css';
import CardItem from './CardItem';

function Cards3() {
  return (
    <div className='cards'>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='images/vm.jpg'
              text='Virtual Mouse'
              label='Interactive'
              path='/soon'
            />
            <CardItem
              src='images/vvcvb.jpg'
              text=' Virtual Brightness and volume control'
              label='Interactive'
              path='/vb'

            />
           
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards3;
