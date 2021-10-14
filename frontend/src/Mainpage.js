/**//*import './static/css/App.css';*/
import './static/css/homepage.css';
import './static/css/style.css';

import React from "react";
import Header from "./components/header.js"
import Tables from "./components/tables.jsx"

import ServerStore from "./stores/ServerStore.jsx"
import UserStore from "./stores/UserStore.jsx"
import TablesStore from "./stores/TablesStore.jsx"

import CreateNewForm from "./components/createNewForm.jsx"
import Block from "./components/block.jsx"
import { Link } from 'react-router-dom'



/*let tables = null;*/

class MainPage extends React.Component {
    constructor(){
        super()
        console.log("mainpage")
        //this.fetchTables()

      this.state = {
        tables : null,
        loading: true,
        addNewTable: false,
      };
      console.log()


    }
/*    componentWillMount(){
       // this.setState({data : fetchTables()});
        this.fetchTables()
    }

   fetchTables(){
            console.log(UserStore.token)
            console.log(UserStore.token)
        let res =  fetch(`${ServerStore.url}/api/tables/`, {
      credentials: 'include',
      headers: {
        "Authorization": `Token 81951a633312e65914aa2416e6510063f4d7d739`,
      },
        method: "GET",
        }).then(res => {         
          return res.json()
        }).then(res => {

            var asd = res;
            this.setState({
             data : asd,
             //tables : asd, 
             loading: false
         })
            console.log(this.state)
    
        });
    }
*/

    loading(){
       return(  <h1>Loding</h1>)
    }
            // <Link to="/page" className="new_table">
            // </Link>

 
    addNew(event) {
        if(this.state.addNewTable){
            if(event.nativeEvent.path[0].id == "background_blurred"){
                this.setState({
                    addNewTable: false
                })

                console.log("FETCHHHH")
                
                }
        }else{
            if(this.state.addNewTable){
                this.setState({
                    addNewTable: false
                })
            }else{
                this.setState({
                    addNewTable: true
                })
        }
    }
        
}


    render(){
      return (  
    <div className="asd">
            <content > 

            { this.state.addNewTable &&  <div onClick={this.addNew.bind(this)}> <CreateNewForm /> </div>}
            <Header />
              <div className="cal new_cal" onClick={this.addNew.bind(this)}>
                <img className="add_new_img" src="/add_new.png" />
              </div>

            <Tables />

            </content>
    </div>      

      );
    }
}


export default MainPage;
