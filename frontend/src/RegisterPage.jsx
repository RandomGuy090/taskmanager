import './static/css/clouds.css';
import './static/css/login.css';
import './static/css/cloudAnim.css';
import { Link } from 'react-router-dom'
import React from "react";


class RegisterPage extends React.Component {


  render(){

    return (
      <content className="tmp">
          <div className="temp-form">

              <div className="loginSpace">
                  <form method='POST' action="." enctype="multipart/form-data">
                    <p>
                      <label htmlFor="login">Username</label>
                      <input type="text" name="login"/>
                    </p>
                      
                    <p>
                      <label htmlFor="password">Password</label>
                      <input type="password" name="password"/>
                    </p>
                    <p>
                      <label htmlFor="password2">Password again</label>
                      <input type="password" name="password2"/>
                    </p>
                      
                    <button type='submit' className='singup' value="Sign Up!">Sign Up!</button>
                  </form>

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


export default RegisterPage;