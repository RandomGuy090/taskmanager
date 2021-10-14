import React from "react";
import UserPanel from './userpanel.jsx'

import ServerStore from "../../stores/ServerStore.jsx"
import UserStore from "../../stores/UserStore.jsx"

import { useState } from 'react';

class LeftPanel extends React.Component {
	constructor(props){
		super()
		console.log(props)
		this.tableID = props.url
		console.log(this.tableID)
		console.log(this.tableID)
		this.fetchLoop = 0;
		this.state = {
			loading: true,
			users: null,
		};
		this.fetchLoop = 0;
	}

	componentWillMount(){
		//this.fetchUsers()
		this.fetchUsers()


		console.log(this.state.users)
	}

	fetchUsers(){
		const that = this;

        this.fetchLoop++
        let res =  fetch(`${ServerStore.url}/api/tables/${this.tableID}/users/`, {
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
            this.fetchUsers()

        }).then((data) => {
        	that.setState({
        		users: data,
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

    asd(){
    	return(
    	this.state.users.map(users => (<UserPanel table={users} />))
    	)
    }
	render(){
    	if(this.state.loading){

			return(
				<div className="LeftPanel">

		          <h2>LOADING...</h2>
				</div>
	          	
				)
    		}else{
    		console.log(this.state.users)
    			return(
				<div className="LeftPanel">
		          	{
		          		this.state.users.map(user => {
		          			return <UserPanel user={ user } />

		          		})
		          	}
						
				</div>
	          	
				)

    		}
		}
}
export default LeftPanel

