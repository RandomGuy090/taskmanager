import React from "react";
import UserPanel from './userpanel.jsx'

import ServerStore from "../../stores/ServerStore.jsx"
import UserStore from "../../stores/UserStore.jsx"
import CalendarStore from '../../stores/calendarStore.jsx'
import TablesStore from '../../stores/TablesStore.jsx'

import { useState } from 'react';



class RightPanel extends React.Component {

	render(){
		if(this.props.notes){

				return(
				<div className="RightPanel">
		       		<div className="RightPanel-header">
		       			<h1>{this.props.date.getDate()}/{this.props.date.getMonth() +1 }/{this.props.date.getFullYear()}</h1>
		       			<h3></h3>
		       		</div>
		       		<div className="panelNotes">

		          	{

		          		this.props.notes.map(note => {
		          			//return <UserPanel user={ user } />
		          			return <h1>{ note.table_note }</h1>
		          		})
		          	}
						
		       		</div>
				</div>
	          	
				)

			}else{
				return (<h1>LOADING.....</h1>)
			}
		
		}
}
export default RightPanel
