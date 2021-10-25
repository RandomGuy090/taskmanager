import React from "react";
import UserPanel from './userpanel.jsx'

import ServerStore from "../../stores/ServerStore.jsx"
import UserStore from "../../stores/UserStore.jsx"
import CalendarStore from '../../stores/calendarStore.jsx'
import TablesStore from '../../stores/TablesStore.jsx'
import NewTask from "../createNewTask.jsx"

import { useState } from 'react';



class RightPanel extends React.Component {
	constructor(){
		super()
		this.state = {
			addNew: false,
		}
		this.openNewTask = this.openNewTask.bind(this)
	}
	openNewTask(event){
		console.log(event)
		console.log(this.state.addNew)
		this.setState({
			addNew: !this.state.addNew,
		})
		console.log(this.state.addNew)
	}

	render(){
		if(this.props.notes){
				return(
		          <>

				<div className="RightPanel">
		       		<div className="RightPanel-header" style={{backgroundColor: this.props.tableColor}}>
		       			<h1>{this.props.date.getDate()}/{this.props.date.getMonth() +1 }/{this.props.date.getFullYear()}</h1>
		       			<h3></h3>
		       		</div>
		       		<div className="panelNotes">

		          	{ 
		          		this.props.notes.map(note => {
		          			//return <UserPanel user={ note } />
		          			//retsurn <h1>{ note.table_note }</h1>
		          			var user = note.user_id
		          			var color = this.props.userData[user]

		          			return(
		          				<div className="taskContainer">
		          					<h3>{note.table_note}</h3>
		          					<h3>{note.user_id}</h3>
		          					<div style={{backgroundColor: color}}>
		          						<h3>{note.todo_date_start.split("T")[1].slice(0,5)}</h3>
		          					</div>
		          				</div>
		          				)
		          		})
		          	}
						<div className="add_new_task">
							Add new task
							<img className="add_new_task_img" src='/add_new_black.png' onClick={this.openNewTask}/>
						</div>
		       		</div>
				</div>
				{this.state.addNew ? <NewTask  state={this.state}/> : "" }
		          </>
	          	
				)

			}else{
				return (<h1>LOADING.....</h1>)
			}
		
		}
}
export default RightPanel

