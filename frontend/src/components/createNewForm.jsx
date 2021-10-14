/**//*import './static/css/App.css';*/
import React from "react";

import '../static/css/loading.css';
import '../static/css/loadingAnim.css';
import ServerStore from "../stores/ServerStore.jsx"
import UserStore from "../stores/UserStore.jsx"

import Block from "../components/block.jsx"
import { Link, Redirect } from 'react-router-dom'

import history from './history';



class CreateNewForm extends React.Component {
    constructor(){
        super()

      this.state = {
        name: "",
        password: "",
        color: "#000000",
        link: "",
        tableUrl: ""

      };
      this.handleName = this.handleName.bind(this)
      this.handlePassword = this.handlePassword.bind(this)
      this.handleColor = this.handleColor.bind(this)
      this.handleLink = this.handleLink.bind(this)
      this.handleJoin = this.handleJoin.bind(this)
      this.handleCreate = this.handleCreate.bind(this)

    }
    handleName(event){
    	this.setState({name: event.target.value})
    }
    handleColor(event){
    	this.setState({color: event.target.value})
    }
    handlePassword(event){
    	this.setState({password: event.target.value})
    }
    handleLink(event){
    	this.setState({link: event.target.value})
 
    }

    errorMsgCreate(){
    	console.log("errr create: no enough data")
    }

    errorMsgJoin(){
    	console.log("errr create: no enough data")
    }

   handleCreate(event){
   	console.log(this.state.name, this.state.color,this.state.password)
	/*history.push(`/tables/${this.state.tableUrl}`);*/
   	if(this.state.name == ""){
   		this.errorMsgCreate()
   		return
   	}
 
   	
   		var asd = false;

   		fetch(`${ServerStore.url}/api/tables/`,{
   			method: "POST",
   			credentials: "same-origin",
   			headers:{
   				Accept: 'application/json',
			    'Content-Type': 'application/json',
			    "Authorization": `Token ${UserStore.token}`
   			},
			body: JSON.stringify({
	   			"name": this.state.name,
	   			"color": this.state.color,
	   			"password": this.state.password
   				}
   			)
   		})
   		.then(res => {
   			return res.json()
   		})
   		.then(res => {
   			console.log(res)
   			console.log(res.url)
   			this.setState({
   				tableUrl: `${res.url}`
   			})
   			console.log(this.state.tableUrl)
   			asd = res;
   			console.log(asd)
   			/*history.push(`tables/${this.state.tableUrl}`)*/
   			return res.url   		
   		})
   		.then(url => {
			if(url){
				fetch(`${ServerStore.url}/api/tables/${url}/join/`,{
	   			method: "POST",
	   			credentials: "same-origin",
	   			headers:{
	   				Accept: 'application/json',
				    "Content-Type": "application/json",
				    "Authorization": `Token ${UserStore.token}`
	   			},
				body: JSON.stringify({
					"password": this.state.password
				})
		   		})
		   		.then(res => {
		   			return res.json()
		   		})
		   		.then(res => {
		   			console.log(res)

		   		})

			}else{
				console.log(url)
			}

   		})
	
   }
   handleJoin(event){
   	console.log(this.state.link)

   	if(this.state.link == ""){
   		this.errorMsgJoin()

   	}else{

		console.log("LINK")
		/*window.location.href = `/tables/${this.state.link}`*/
		//history.push(`/table/${this.state.link}`);
   	}
   }
    
    render(){
    	if(this.state.tableUrl != ""){
    		console.log("REDIRECT------s")
    		var url = `/table/${this.state.tableUrl}`
    		return <Redirect to={url} push={true} />

    	}
    	return (
		<div id="background_blurred">
			<div id="new_table_menu" className="no_hid">
				<div className="no_hid">
					
					<div className="no_hid">
						<h1 className="no_hid" >CREATE NEW</h1>
					</div>
					
					
					<div className="no_hid">
						<h1 className="no_hid">JOIN</h1>
					</div>
				</div>
				
				<div className="no_hid">
					<div className="no_hid" id="create_new_data" >

						
						<input type="text" name="name" className="no_hid" placeholder="name" autoComplete="off" onChange={this.handleName} />


						
						<input type="password" name="password" className="no_hid" placeholder="password" onChange={this.handlePassword}/>

						<div className="no_hid">
							<label htmlFor="color_main" className="no_hid"> color </label>	
							<input type="color" name="color_main" className="no_hid" placeholder="color" onChange={this.handleColor} />
						</div>
						

							<input type="button" id="send" name="send" value="create" className="no_hid" onClick={this.handleCreate}/>

					 </div>
					
					<div className="no_hid add_new_cal">
						<input type="text" autoComplete="off" id="join_table" name="join_table" className="no_hid" placeholder="link to calendar" onChange={this.handleLink} />
						<input type="button" id="join" name="join" value="join" className="no_hid" onClick={this.handleJoin} />

					</div>				
				</div>

				

				
			</div>
		</div>
        
        
    		)}
    }




export default CreateNewForm;


