import './static/css/style.css';
import './static/css/homepage.css';
import 'react-calendar/dist/Calendar.css';
import './static/css/calendar.css';

import LeftPanel from './components/calendarComp/leftpanel.jsx'

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
		
	}
//______________________________________-


//______________________________________

	render(){
		return(
		<div class="tablesBG">
			<LeftPanel url={this.tableID} />

			<div>
				<p>tableID = {this.tableID}</p>
				<Calendar />
			</div>
		</div>
		)
				
	}
}
export default TableMain