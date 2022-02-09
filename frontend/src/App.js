import React, {Component} from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Title from './views/Header/Title';
import Login from './views/Login/Login';
import Home from './views/Home/Home';
import SensorDetail from './views/Sensor/SensorDetail';
import Company from './views/Company/Company';

import './App.css';

class App extends Component {
  render () {
    return (
      <div className="">
        <Title/>

        <BrowserRouter>
          <div className="wrapper">
            <Routes>
              <Route path="/login" element={ <Login />} />
              <Route path="/" element={ <Home />} />
              <Route path="/sensor/detail" element={ <SensorDetail />} />
              <Route path="/company" element={ <Company />} />
            </Routes>
          </div>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;