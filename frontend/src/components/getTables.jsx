/**//*import './static/css/App.css';*/
import React from "react";


import ServerStore from "../stores/ServerStore.jsx"

import Block from "../components/block.jsx"
import { Link } from 'react-router-dom'


class GetTables extends React.Component {
    constructor(){
        super()
        console.log("mainpage")
        this.fetchTables()

      this.state = {
        tables : null,
        loading: true
      };

    }

    componentWillMount(){
        this.fetchTables()
    }

   fetchTables(){
        let res =  fetch(`${ServerStore.url}/api/tables/`, {
      credentials: 'include',
        method: "GET",
        headers: {
        "Authorization": `Token 81951a633312e65914aa2416e6510063f4d7d739`,
      },
        }).then(res => {         
          return res.json()
        }).then(res => {
            var asd = res;
            console.log(res)
            this.setState({
             tables : asd, 
             loading: false
         })
           return this.state.tables
    
        });
    }

    render(){

        return ( 
      this.state.tables.map((tbl) => {  
        return  (
            <Block table={tbl} />
            )
          })
        )
        
    }

 

}

export default GetTables;
