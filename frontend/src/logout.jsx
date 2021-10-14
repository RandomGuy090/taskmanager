/**//*import './static/css/App.css';*/
import './static/css/style.css';
import './static/css/homepage.css';


//import './static/css/logout.css';
import React from "react";
import Header from "./components/header.js"

import ServerStore from "./stores/ServerStore.jsx"
import UserStore from "./stores/UserStore.jsx"
import { Link } from 'react-router-dom'




class Logout extends React.Component {
    constructor(){
        super()
        console.log("logout")
        this.doLogout()

      this.state = {
        login : true,
        loading: true
      };


    }

   doLogout(){
        let res =  fetch(`${ServerStore.url}/api/logout/`, {
      credentials: 'include',
        method: "GET",
        }).then(res => {         
          return res.json()
        }).then(res => {
            var asd = res;
            console.log(asd)
            console.log(asd)
            if(res.status_code == "201"){
                UserStore.username = "";
                UserStore.isLogged = false;
                UserStore.loading = false;
                UserStore.token = "";
                localStorage.removeItem("token")
            }
            else{
                console.log("error")
            }
       
    
        });
    }



    render(){


      return (  

            <content> 

                <Header />

                <h1>Logged out!</h1>
                <div className="logout-redirect">
                     <Link to="/login/"> 
                          <button type='submit' className='singup' value="Log in!" onClick={this.handleSubmit}>Log in!</button>
                        </Link>
                    <Link  to="/register/" className="singupLink">
                        <input type="button" name="goToRegister" className="singup"value="Sing up!" />
                    </Link>
                </div>

            </content>
        

      );
    }
}
//{this.state.tables != null ? this.tbl() : this.loading() }

export default Logout;
