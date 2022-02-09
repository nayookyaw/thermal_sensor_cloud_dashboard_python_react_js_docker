import React, { Component } from "react";
import { Pagination } from "react-headless-pagination";

import { Table } from 'reactstrap';
import ToggleButton from "react-toggle-button";

import { FaAngleDoubleRight } from "react-icons/fa";

import axios from 'axios';

import { BACKEND_SERVER_URL, ROW_LIMIT } from '../../constant.js';

// include common pagination design
import '../../../src/assets/css/pagination/pagination.css';
import './Home.css';

class Home extends Component {

  constructor(props) {
    super(props);

    this.state = {
      resultSensorList: [],
      totalRecord: 0,
      totalPage: 0,
      currentPage: 0,
      offset: 0,
      limit: ROW_LIMIT,
      databaseSize: 0,
      isAutoSync: 0, // default is auto sync
      isBLockAllSensors: 1, // default is block
    };

    this.handlePageChange = this.handlePageChange.bind(this);
    this.getSensorCount = this.getSensorCount.bind(this);
    this.getSensorList = this.getSensorList.bind(this);
  }

  // best practice to call API for only one 
  componentDidMount() {
    this.getSensorCount();

    setTimeout(() => {
      this.getSensorManageStatus();
    }, 100);
  }

  getSensorCount() {
    axios.post(BACKEND_SERVER_URL + `/get/sensor/count`)
      .then(res => {
        if (res.data.data) {

          // if total is 0, don't call the list
          if (res.data.data.total_count > 0) {
            var tempTotal = Math.ceil(res.data.data.total_count / this.state.limit);
            this.setState({totalPage : tempTotal });

            this.setState({ totalRecord: res.data.data.total_count });
            this.setState({ databaseSize: res.data.data.database_size})

            this.getSensorList();
            
          }
        }
        
      })
      .catch(error => {
        console.log (error);
      });
  }

  getSensorList() {
    const req_data = {
      offset : this.state.offset,
      limit : this.state.limit
    }

    axios.post(BACKEND_SERVER_URL + `/get/sensor/list`, { req_data })
      .then(res => {
        this.setState({ resultSensorList : res.data.data});
      })
      .catch(error => {
        console.log (error);
      });
  }

  getSensorManageStatus() {
    axios.post(BACKEND_SERVER_URL + `/get/sensor/manage/status`)
      .then(res => {
        if (res.data && res.data.data) {
          let responseMS = res.data.data;

          // if sync has data and 1, set 1
          if (responseMS.auto_sync && responseMS.auto_sync === 1) {
            this.setState({ isAutoSync : 1 });
          } else {
            this.setState({ isAutoSync : 0 });
          }

          if (responseMS.block_all_sensor === 0) {
            this.setState({ isBLockAllSensors : 0 });
          } else {
            this.setState({ isBLockAllSensors : 1 });
          }

        }
      })
      .catch(error => {
        console.log (error);
      });
  }

  updateSensorMangeStatus(type, val) {
    val = val ? 1 : 0;

    const req_data = {
      type : type,
      value : val
    }
    
    axios.post(BACKEND_SERVER_URL + `/update/sensor/manage/status`, { req_data })
    .then(res => {
      this.getSensorManageStatus();
    })
    .catch(error => {
      console.log (error);
    });
  }

  linkDetailSensor(sensor_id) {
    window.location.replace("/sensor/detail/?id=" + sensor_id);
  }

  handlePageChange = (c_page) => {
    this.setState({ currentPage: c_page });

    const tempOffset = c_page * this.state.limit;

    this.setState({ offset : tempOffset } , () => {
      this.getSensorList();
    });
    
  };

  updateIsAllow(toggleVal, sensorId) {

    let req_data = {
      sensor_id : sensorId,
      is_allow : toggleVal ? 1 : 0
    }

    axios.post(BACKEND_SERVER_URL + `/update/sensor/allow`, { req_data })
      .then(res => {
        this.getSensorList()
      })
      .catch(error => {
        console.log (error);
      });
  }
  
  render() {
    const { resultSensorList, totalRecord, databaseSize, isAutoSync,
        isBLockAllSensors } = this.state;

    let sensorList = null;
    
    if (resultSensorList && resultSensorList.length > 0) {
      sensorList = resultSensorList.map((sensor, index) => (
        <tr key={index}>
          <td style={{ textAlign:"center"}}>{sensor.id}</td>
          <td style={{ textAlign:"center"}}>{sensor.mac_address}</td>
          <td style={{ textAlign:"center"}}>{ sensor.company_id ? sensor.company_id : "-" }</td>
          <td style={{ textAlign:"center"}}>{sensor.building_id ? sensor.building_id : "-"}</td>
          <td style={{ textAlign:"center"}}>{sensor.floor_id ? sensor.floor_id : "-"}</td>
          <td style={{ textAlign:"center"}}>
            <div style={{ display: "inline-block"}}>
              <ToggleButton
              value={ parseInt(sensor.is_block) || 0 }
              onToggle={(value) => {
                this.updateIsAllow(!value, sensor.id);
              }}
              /> 
            </div>
          </td>
          <td style={{ textAlign:"center"}}>
            <FaAngleDoubleRight style={{cursor:"pointer", fontSize: "30px"}}
              onClick={this.linkDetailSensor.bind(this, sensor.id)}
            />
          </td>
        </tr>
      ));
    } else {
      sensorList = 
      <tr >
        <td colSpan={7} style={{ textAlign:"center"}}>There is no data</td>
      </tr>
    }
    
    return (
      <>
        <div style={{ paddingBottom: "7px"}}>
          <div className="auto_manage">
            Auto Sync &nbsp;&nbsp;
            <ToggleButton
              value={ parseInt(isAutoSync) || 0 }
              onToggle={(value) => {
                this.updateSensorMangeStatus("sync", !value);
              }}
            />

            &nbsp;&nbsp;

            Block All Sensors &nbsp;&nbsp;
            <ToggleButton
              colors={{
                active: {
                  base: 'rgb(135, 45, 103)',
                  hover: 'rgb(177, 191, 215)',
                },
                inactive: {
                  base: 'rgb(121, 173, 29)',
                  hover: 'rgb(177, 191, 215)',
                }
              }}
              value={ parseInt(isBLockAllSensors) || 0 }
              onToggle={(value) => {
                this.updateSensorMangeStatus("block", !value);
              }}
            />
          </div>
          
          <div className="total_record_count">
            Total Record - {totalRecord} /
            <span className="size"> Size - {databaseSize} MB </span>
          </div>
        </div>

        <Table dark hover responsive>
            <thead>
              <tr>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Id</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>MAC Address</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Company</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Building</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Floor</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Allow</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Action</th>
              </tr>
            </thead>
            <tbody>
              { sensorList }
            </tbody>
        </Table>

        <Pagination
          currentPage={this.state.currentPage}
          setCurrentPage={this.handlePageChange}
          totalPages={this.state.totalPage}
          edgePageCount={2}
          middlePagesSiblingCount={1}
          className="paginationWrapper"
          truncableText="..."
          truncableClassName=""
        >
          <Pagination.PrevButton className="paginationPrev"> {"<<"} </Pagination.PrevButton>

          <div className="paginationBody">
            <Pagination.PageButton
              activeClassName="paginationActive"
              inactiveClassName="paginationInactive"
              className=""
            />
          </div>

          <Pagination.NextButton className="paginationNext"> {">>"} </Pagination.NextButton>
        </Pagination>
      </>
    );
  }
}

export default Home;
