import './static/css/style.css';
import './static/css/homepage.css';
import 'react-calendar/dist/Calendar.css';
import './static/css/calendar.css';

import LeftPanel from './components/calendarComp/leftpanel.jsx'

import ServerStore from "./stores/ServerStore.jsx"
import UserStore from "./stores/UserStore.jsx"


import React from "react";
import $ from 'jquery'
import Calendar from 'react-calendar';




class TableMain extends React.Component {

	constructor(){
		super()
		var table = window.location.href
		console.log(table)
		table = table.split("/")
		console.log(table)
		this.tableID = table[table.indexOf("table")+1]
		console.log(this.tableID)
		this.state = {
			tableName: null,
			tableColor: null,
			tableColorBorder: null,
        	loading: true,

		}
		
	}
	componentWillMount(){
		this.fetchTable();
	}

	fetchTable(){
		const that = this;

        this.fetchLoop++
        let res =  fetch(`${ServerStore.url}/api/tables/${this.tableID}/`, {
      credentials: 'include',
        method: "GET",
        headers: {
        "Authorization": `Token ${UserStore.token}`,
      },
        }).then(res => {   
        console.log(res)  
        console.log(res.status)  

            if (res.status == 200){
                return res.json()
            }
            console.log("error")
            if(this.fetchLoop> 5){
            	console.log("error")
                throw new Error('loading error');
            }
            this.fetchTable()

        }).then((data) => {
        	console.log(data)
        	that.setState({
        		tableName: data.name,
        		tableColor: data.color,
        		tableColorBorder: data.border_color,
        		loading: false,
        	})
        	console.log(data)
           return data
    
        })
        .catch((error) => {
          console.log(error)
          return "error"
        });;
    }



	render(){
		if(!this.state.loading){
			return(
			<div class="tablesBG">
				<LeftPanel url={this.tableID} />

				<div>
					<h1>{this.state.tableName}</h1>
					<Calendar />
				</div>
			</div>
			)
		}else{
			return(
				<h1>LOADING.....</h1>
			)
		}
				
	}
}
export default TableMain