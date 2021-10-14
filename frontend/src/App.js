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
import TableMain from './tableMain.jsx'

import UserStore from "./stores/UserStore.jsx"
import ServerStore from "./stores/ServerStore.jsx"

import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import Cookies from 'js-cookie';
import history from './components/history';


class App extends React.Component {
  constructor(){
    super()
    this.componentDidMount()

  } 


  componentDidMount(){
    try{
      let headers = {}
      //console.log(`${ServerStore.url}/api/user/`)
      UserStore.token = localStorage.getItem("token")
      if(UserStore.token != null){
        headers = {
        "Authorization": `Token ${UserStore.token}`,
        }
      }
     
      let res = fetch(`${ServerStore.url}/api/user/`, {
      credentials: 'include',
        method: "GET",
        headers: headers,
        }).then(res => {         
          return res.json()
        }).then((res) => {
            if(res.code == "201"){
              UserStore.isLogged = true;
              UserStore.username = res.username;
           
            }else{
              UserStore.isLogged = false
          }
    
        })
        .catch(err => {
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
          <TableMain />
      </Route>
    
     </Switch>
    

    </div>
   </Router>

  );
 }
}

export default observer(App);

