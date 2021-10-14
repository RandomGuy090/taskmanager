import './static/css/clouds.css';
import './static/css/login.css';
import './static/css/cloudAnim.css';
import { Link } from 'react-router-dom'
import React from "react";
import { useState } from 'react';
import Cookies from 'js-cookie';
import CSEFToken from './components/CSRFtoken';
import history from './components/history';



import ServerStore from "./stores/ServerStore.jsx"
import UserStore from "./stores/UserStore.jsx"

import { Redirect, useHistory } from 'react-router-dom'
import { browserHistory } from 'react-router'
import Header from "./components/header.js"


let djangoURL = 'http://127.0.0.1:8000'
let defaultTimeout = 30000


class LoignPage extends React.Component {


    constructor({props}){
      super()
      //const { location, history } = this.props
    
      this.state = {
        username: '',
        password: '',
      }
     
      this.updateLogin = this.updateLogin.bind(this);
      this.updatePassword = this.updatePassword.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);


    }

  async loginUser(){

      var csrftoken = Cookies.get('csrftoken');

      var sessionid = Cookies.get('sessionid');

        const headers =  {     
          }
       const config = {
        headers
          
      };

      const body = JSON.stringify({
        username: this.state.username,
        password: this.state.password,
      })

 
      fetch(`${ServerStore.url}/api/token/`, {
          method: 'POST',
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },

          body: body,

      }).then((res) => {
          return res.json()
      }).then((res) => {
        console.log(res)
        if(res.token ){
          console.log("ad")
          UserStore.username = this.state.username;
          UserStore.loading = false;
          UserStore.isLogged = true;
          UserStore.token = res.token;
          localStorage.setItem('token', UserStore.token);
          history.push(`/`);




        }else{
          console.log("login failed")
          UserStore.loading = false;
          UserStore.isLogged = false;
          UserStore.username = false;
          UserStore.token = "";



        }

    });


  }
  updateLogin(event){
    this.setState({username : event.target.value})
  }
  updatePassword(event){
    this.setState({password : event.target.value})
  }

  handleSubmit(){
    
    this.loginUser()
    //this.props.router.push('/some/path')


  //Send state to the server code
  

  }   

  render(){

  return (

    <content className="tmp">
        <div className="temp-form">

            <div className="loginSpace">
                {/*<form method='POST' action="." enctype="multipart/form-data">*/}
                {/*<form>*/}
                < CSEFToken />
                <div className="mainform">
                  <p>
                    <label htmlFor="login">Username</label>
                    <input type="text" name="login" onChange={this.updateLogin} />
                  </p>
                    
                  <p>
                    <label htmlFor="password">Password</label>
                    <input type="password" name="password" onChange={this.updatePassword}/>
                  </p>
                    <Link to="/"> 
                    </Link>
                      <button type='submit' className='singup' value="Log in!" onClick={this.handleSubmit}>Log in!</button>
                    <Link  to="/register/" className="singupLink">
                        <input type="button" name="goToRegister" className="singup"value="Sing up!" />
                    </Link>
                {/*</form>*/}
                </div>

            </div>
            <div class="sky">
                <div className="cloud"></div>
                <div className="cloud"></div>
                <div className="cloud"></div>
            </div>
        </div>

    </content>
    

  );
  }
}

export default LoignPage;
