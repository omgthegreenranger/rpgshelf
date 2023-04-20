import React, { useState } from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import { Col, Row } from 'react-bootstrap';

import Home from './components/home';

export default function App() {
  return (
    <> 
       <Home />
    </>
  )
}