import { Component } from "react";

import SensorLogo from '../../assets/img/sensor_logo.png';

import './Title.css';

class Title extends Component {

    render() {

        return (
            <div className="console_title_wrapper">
                <div>
                    <img className='sensor_logo' src={SensorLogo} alt="sensor_logo" />
                    <h3>Sensor Management Console</h3>
                    
                </div>
            </div>
        )

    }
}

export default Title;