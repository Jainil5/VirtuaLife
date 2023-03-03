import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards() {
  return (
    <div className='cards'>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>

            <CardItem
              src='images/fc.jpg'
              text='Virtual Voice Assisted Finger Counter'
              label='Adventure'
              path='/counter' />
            <CardItem
              src='images/RPS.png'
              text='Explore Rock Paper and Scissors'
              label='Interactive'
              path='/soon' />
            <CardItem
              src='images/vp.jpg'
              text='Explore Virtual Painting'
              label='Comfort Painting'
              path='/soon' />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='images/VQ.jpg'
              text='Virtual Quiz'
              label='Mystery'
              path='/video_quiz' />
            <CardItem
              src='images/img-8.jpg'
              text='Explore the Game 5(yet to release)'
              label='Adrenaline'
              path='/soon' />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
