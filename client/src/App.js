import React, { useState } from 'react';
import Navbar from './components/Navbar';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Services from './components/pages/Services';
import Products from './components/pages/Products';
import SignUp from './components/pages/SignUp';
import Login from './components/pages/Login';
import SocialService from './components/pages/SocialService';
import Rps from './components/pages/Rps';
import Vp from './components/pages/Vp';
import Ssg1 from './components/pages/ssg1';
import Ssg2 from './components/pages/ssg2';
import VirtualMouse from './components/pages/Vm';
import VBVM from './components/pages/Vb';
import Tutorial from './components/pages/Tutorial';
function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/services' component={Services} />
          <Route path='/products' component={Products} />
          <Route path='/sign-up' component={SignUp} />
          <Route path='/login' component={Login} />
          <Route path='/SocialService' component={SocialService} />
          <Route path='/Rps' component={Rps} />
          <Route path='/vp' component={Vp} />
          <Route path='/ssg1' component={Ssg1} />
          <Route path='/ssg2' component={Ssg2} />
          <Route path='/vm' component={VirtualMouse} />
          {/* <Route path='/vb' component={VBVM} /> */}
          <Route path='/Tutorial' component={Tutorial} />

        </Switch>
      </Router>
    </>
  );
}

export default App;
