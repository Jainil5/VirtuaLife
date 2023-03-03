import React from 'react';
import '../App.css';
import { Button } from './Button';
import './HeroSection.css';

function HeroSection() {
  return (
    <div className='hero-container'>
      <video src='/videos/VL1.mp4' autoPlay loop muted />
      <h1>VIRTUAL LIFE AWAITS</h1>
      
    </div>
  );
}

export default HeroSection;
