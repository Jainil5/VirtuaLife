import React from 'react';
import { Link } from 'react-router-dom';

function CardItem(props) {
  return (
    <>
      <li className='cards__item'>
        <a href={props.path} className="cards__item__link">
          
        {/* <Link className='cards__item__link' to={props.path}> */}
          <figure className='cards__item__pic-wrap' data-category={props.label}>
            <img
              className='cards__item__img'
              alt='Travel '
              src={props.src}
            />
          </figure>
          <div className='cards__item__info'>
            <h5 className='cards__item__text'>{props.text}</h5>
          </div>
        {/* </Link> */}
        </a>
      </li>
    </>
  );
}

export default CardItem;
