/**//*import './static/css/App.css';*/
import React from "react";

import '../static/css/loading.css';
import '../static/css/loadingAnim.css';
import ServerStore from "../stores/ServerStore.jsx"
import UserStore from "../stores/UserStore.jsx"

import Block from "../components/block.jsx"
import CreateNewForm from "../components/createNewForm.jsx"
import { Link } from 'react-router-dom'


class Tables extends React.Component {
    constructor(){
        super()
        console.log("mainpage")
        
      this.state = {
        tables : null,
        loading: true
      };
      this.fetchLoop = 0;

    }

    componentWillMount(){
        /*this.setState({data : fetchTables()});*/
        this.state.loading = true;

        this.fetchTables()
    }

   fetchTables(){
        this.fetchLoop++
        let res =  fetch(`${ServerStore.url}/api/tables/`, {
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
                throw new Error('loading error');

            }
            this.fetchTables()


        }).then(res => {
            var asd = res;
            console.log(res)
            this.setState({
             tables : asd, 
             loading: false
         })
           return this.state.tables
    
        })
        .catch((error) => {
          console.log(error)
        });;
    }
    addNew(){
        return(

            <Link to="/page" className="new_table">
              <div className="cal new_cal">
                <img className="add_new_img" src="/add_new.png" />
              </div>
            </Link>

            )
    }
     loading(){
       return( <h3>Loding</h3> )
    }

    render(){
        console.log("tbl")
        console.log(this.state.tables)
        if(this.state.loading == true || this.state.tables == null){
            console.log("loading")
            return this.loading()
        }else{
            console.log(this.state.tables)
            return ( 
          this.state.tables.map((tbl) => {  
            return <Block table={tbl} />
              })
            )
        }
    }

   

 }

export default Tables;
