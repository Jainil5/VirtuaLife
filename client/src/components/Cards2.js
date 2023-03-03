import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards2() {
  return (
    <div className='cards'>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='images/fc.jpg'
              text='Virtual Voice assisted finger counting'
              label='Interactive'
              //path='/ssg1'
              path='/counter'
            />
            <CardItem
              src='images/vr.webp'
              text=' VirtualRemote '
              label='Interactive'
              // path='/ssg2'
              path='/remote'
            />
           
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards2;
