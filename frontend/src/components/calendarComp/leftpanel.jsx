import React from "react";
import UserPanel from './userpanel.jsx'

import ServerStore from "../../stores/ServerStore.jsx"
import UserStore from "../../stores/UserStore.jsx"
import TablesStore from "../../stores/TablesStore.jsx"
import UserCache from "../../stores/UserCacheStore.jsx"

import { useState } from 'react';

class LeftPanel extends React.Component {
/*	constructor(props){
		super()

		this.tableID = TablesStore.id

		this.fetchLoop = 0;
		this.state = {
			loading: true,
			users: null,
		};
		this.fetchLoop = 0;
	}
*/
	componentWillMount(){
		//this.fetchUsers()
		//this.fetchUsers()


		
	}

/*	fetchUsers(){
		const that = this;

        this.fetchLoop++
        let res =  fetch(`${ServerStore.url}/api/tables/${TablesStore.id}/users/`, {
      credentials: 'include',
        method: "GET",
        headers: {
        "Authorization": `Token ${UserStore.token}`,
      },
        }).then(res => {   
        

            if (res.status == 200){
                return res.json()
            }
            
            if(this.fetchLoop> 5){
            	
                throw new Error('loading error');
            }
            this.fetchUsers()

        }).then((data) => {
        	that.setState({
        		users: data,
        		loading: false,
        	})
        	
           return data
    
        })
        .catch((error) => {
          console.log(error)
          return "error"
        });;
    }
*/

	render(){
    	if(this.props.users == null){

			return(
				<div className="LeftPanel">

		          <h2>LOADING...</h2>
				</div>
	          	
				)
    		}else{
    		
    			return(
				<div className="LeftPanel">
		          	{
		          		this.props.users.map(user => {
		          			var data = {
		          				[user.user_id]:{
		          					color: user.color
		          				}
		          			}
		          			return <UserPanel user={ user } />

		          		})
		          	}
						
				</div>
	          	
				)

    		}
		}
}
export default LeftPanel

