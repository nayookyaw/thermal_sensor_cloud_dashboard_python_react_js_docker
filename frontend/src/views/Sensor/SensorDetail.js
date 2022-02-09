import React, { Component } from "react";
import { Pagination } from "react-headless-pagination";

import { Table, Breadcrumb, BreadcrumbItem } from 'reactstrap';
import moment from 'moment'

import axios from 'axios';

import { BACKEND_SERVER_URL, ROW_LIMIT } from '../../constant.js';

// include common pagination design
import '../../../src/assets/css/pagination/pagination.css';
import './SensorDetail.css';

class SensorDetail extends Component {

  constructor(props) {
    super(props);

    this.state = {
      resultSensorCollection: [],
      totalRecord: 0,
      totalPage: 0,
      currentPage: 0,
      offset: 0,
      limit: ROW_LIMIT,
      sensorId: 0,
    };

    this.handlePageChange = this.handlePageChange.bind(this);
    this.getSensorCollCount = this.getSensorCollCount.bind(this);
    this.getSensorCollection = this.getSensorCollection.bind(this);
    this.getUrlVars = this.getUrlVars.bind(this);
  }

  // best practice to call API for only one 
  componentDidMount() {
    this.getSensorCollCount();
  }

  getUrlVars() {
    var vars = {};
    window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
      vars[key] = value;
    });

    return vars;
  }

  // check the id from url
  getValidateSensorId() {
    var urlVal = this.getUrlVars();

    if (urlVal.id && parseInt(urlVal.id) > 0) {
      this.setState({sensorId : urlVal.id });

      return parseInt(urlVal.id);
    } else {
      return 0;
    }
  }

  getSensorCollCount() {
    if (!this.getValidateSensorId()) {
      return
    }
    
    const req_data = {
      sensor_id : this.getValidateSensorId()
    }

    axios.post(BACKEND_SERVER_URL + `/get/sensor/collection/count`, { req_data })
      .then(res => {
        if (res.data.data) {

          // if total is 0, don't call the list
          if (res.data.data > 0) {
            var tempTotal = Math.ceil(res.data.data / this.state.limit);
            this.setState({totalPage : tempTotal });

            this.setState({ totalRecord: res.data.data });

            this.getSensorCollection();
          }
          
        }
        
      })
      .catch(error => {
        console.log (error);
      });
  }

  getSensorCollection() {
    const req_data = {
      offset : this.state.offset,
      limit : this.state.limit,
      sensor_id : this.getValidateSensorId()
    }

    axios.post(BACKEND_SERVER_URL + `/get/sensor/collection`, { req_data })
      .then(res => {
        this.setState({ resultSensorCollection : res.data.data});
      })
      .catch(error => {
        console.log (error);
      });
  }

  handlePageChange = (c_page) => {
    this.setState({ currentPage : c_page });

    const tempOffset = c_page * this.state.limit;

    this.setState({ offset : tempOffset } , () => {
      this.getSensorCollection();
    });   
    
  };
  
  render() {
    const { resultSensorCollection, totalRecord } = this.state;

    let sensorCol = null;

    if (resultSensorCollection.length > 0) {
      sensorCol = resultSensorCollection.map((sensor, index) => {
        var modified_sensor_d = null;

        if (sensor.sensor_data) {
            modified_sensor_d = sensor.sensor_data.replace(/(.{10})/g, "$1\n");
        }

        return (
            <tr key={index}>
            <td style={{ textAlign:"center"}}>{sensor.id}</td>
            <td style={{ textAlign:"center", width: "15%"}}>{moment((sensor.created_at)).format('YYYY-MM-DD HH:mm:ss')}</td>
            <td> 
                { modified_sensor_d ? 
                    modified_sensor_d
                    : "-" }
                </td>
            </tr>
        )
      });
    } else {
      sensorCol = 
      <tr>
        <td colSpan={5} style={{ textAlign:"center"}}>There is no data</td>
      </tr>
    }
    
    return (
      <>
        <span>
          <Breadcrumb listTag="div">
            <BreadcrumbItem
              href="/"
              tag="a"
            >
              Home
            </BreadcrumbItem>
            <BreadcrumbItem
              active
              tag="span"
            >
              Sensor ID - { this.state.sensorId }
            </BreadcrumbItem>
          </Breadcrumb>

          <div className="total_record_count">
            Total Record - {totalRecord}
          </div>

        </span>      

        <Table dark hover responsive>
            <thead>
              <tr>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Id</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Date</th>
                <th style={{ textAlign:"center", backgroundColor:"rgb(85 90 89)"}}>Sensor Data</th>
              </tr>
            </thead>
            <tbody>
                { sensorCol }
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

export default SensorDetail;
