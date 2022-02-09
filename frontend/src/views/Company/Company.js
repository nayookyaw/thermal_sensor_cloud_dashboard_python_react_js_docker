import React, { Component } from "react";
import { Pagination } from "react-headless-pagination";

import { Table } from 'reactstrap';

import { FaAngleDoubleRight } from "react-icons/fa";

import axios from 'axios';

import { BACKEND_SERVER_URL, ROW_LIMIT } from '../../constant.js';

// include common pagination design
import '../../../src/assets/css/pagination/pagination.css';
import './Company.css';

class Company extends Component {

  constructor(props) {
    super(props);

    this.state = {
        companyList: [],
        totalRecord: 0,
        totalPage: 0,
        currentPage: 0,
        offset: 0,
        limit: ROW_LIMIT,
    };

    this.handlePageChange = this.handlePageChange.bind(this);
    this.getSensorCount = this.getSensorCount.bind(this);
    this.getSensorList = this.getSensorList.bind(this);
  }

    // best practice to call API for only one 
    componentDidMount() {
        this.getSensorCount();
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

  
    render() {
        const { resultSensorList, totalRecord } = this.state;

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
                <FaAngleDoubleRight style={{cursor:"pointer", fontSize: "30px"}}
                onClick={this.linkDetailSensor.bind(this, sensor.id)}
                />
            </td>
            </tr>
        ));
        } else {
        sensorList = 
        <tr >
            <td colSpan={7} style={{ textAlign:"center"}}>There is no company</td>
        </tr>
        }
        
        return (
        <>
            
            <div className="total_record_count">
                Total Record - {totalRecord} 
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

export default Company;
