import React from "react";
import $ from 'jquery'


class UserPanel extends React.Component {
	constructor(props){
		super()
		this.user = props.user
		console.log("user props")
	
	}


	render(){
		return(
			<div className="user">
				<img className="user-prof" src='/profile.png' />
				<p className="user-name">{this.user.user_id}</p>
				<div className="user-color" style={{backgroundColor: this.user.color }}></div>
			</div>
		)
	}
}
export default UserPanel

