import logo from './logo.svg';
import React from "react";
import { observer } from "mobx-react";
/*import './static/css/App.css';*/
import './static/css/style.css';
import './static/css/homepage.css';

import Block from "./components/block.jsx"

import MainPage from "./Mainpage.js"
import Page from './Page';

import LoignPage from './LoginPage.jsx';
import Logout from './logout.jsx';
import RegisterPage from './RegisterPage.jsx';

import UserStore from "./stores/UserStore.jsx"
import ServerStore from "./stores/ServerStore.jsx"

import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import Cookies from 'js-cookie';
import history from './components/history';


class App extends React.Component {
  constructor(){
    super()
    console.log()
    this.componentDidMount()

  } 


  componentDidMount(){
    try{
      //console.log(`${ServerStore.url}/api/user/`)
      UserStore.token = localStorage.getItem("token")
      let res = fetch(`${ServerStore.url}/api/user/`, {
      credentials: 'include',
      headers: {
        "Authorization": `Token ${UserStore.token}`,
      },
        method: "GET",
        }).then(res => {         
          return res.json()
        }).then((res) => {
          console.log(res)
          console.log(res)
          console.log(res)
            if(res.code == "201"){
              UserStore.isLogged = true;
              UserStore.username = res.username;
           
            }else{
              UserStore.isLogged = false
          }
    
        })
        .catch(err => {
          console.log(err)
          UserStore.isLogged = false
        });
      
    }catch(e){
      console.log(e)
    }
  }

 render(){

  function RenderMainPage(props){
    const isLogged = props.logged



  }

  return (
   <Router history={history}>
    <div className="App ">      
     <Switch>
    

      <Route exact path="/">
      {(UserStore.isLogged) ? <MainPage username={UserStore.username}/> : <LoignPage />}
       {/*<RenderMainPage logged={UserStore.isLogged} />*/}

      </Route>
      
      <Route path="/page">
          <Page />
      </Route>

       <Route path="/login">
          <LoignPage />
      </Route>

      <Route path="/register">
          <RegisterPage />
      </Route>

       <Route path="/logout">
          <Logout />
      </Route>

      <Route path="/table/">
          <h1>TABLES </h1>
      </Route>
    
     </Switch>
    

    </div>
   </Router>

  );
 }
}

export default observer(App);

