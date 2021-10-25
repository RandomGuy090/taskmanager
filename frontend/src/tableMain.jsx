import './static/css/style.css';
import './static/css/homepage.css';
import 'react-calendar/dist/Calendar.css';
import './static/css/calendar.css';

import LeftPanel from './components/calendarComp/leftpanel.jsx'
import RightPanel from './components/calendarComp/rightpanel.jsx'

import ServerStore from "./stores/ServerStore.jsx"
import UserStore from "./stores/UserStore.jsx"
import TablesStore from "./stores/TablesStore.jsx"


import React from "react";
//import Calendar from './components/calendarComp/calendarpanel.jsx';
import Calendar from 'react-calendar';




class TableMain extends React.Component {

	constructor(){
		super()
		var table = window.location.href
		table = table.split("/")
		TablesStore.id = table[table.indexOf("table")+1]
		this.state = {
			tableName: null,
			tableColor: null,
			tableColorBorder: null,
        	
        	loadingNotes: true,
        	loadingTable: true,
        	loadingUsers: true,
        	
        	notes: null,
        	date: null,
        	users: null,

		}

		this.userColors = {}
		this.fetchLoop = 0
      
      this.dateChange = this.dateChange.bind(this);
      this.monthChange = this.monthChange.bind(this);	
	}

	componentWillMount(){
		var date = new Date()
		this.setState({
			date:date
		})

		this.fetchTable();
		this.fetchUsers()
		this.fetchNotes(0,date.getMonth()+1, date.getFullYear());

		
		/*this.interval = setInterval(() => {
			this.fetchTable();
			this.fetchUsers()
			this.fetchNotes(0,date.getMonth()+1, date.getFullYear());
		}, 2000);*/

	}
	
	componentWillUnmount() {
	  this.timer = null; // here...
	  //clearInterval(this.interval);

	}



	fetchTable(){
        this.fetchLoop++
        let res =  fetch(`${ServerStore.url}/api/tables/${TablesStore.id}/`, {
	      	credentials: 'include',
	        method: "GET",
	        headers: {
	        "Authorization": `Token ${UserStore.token}`,
	     	},
        }).then(res => {   
            if (res.status == 200){
                return res.json()
            }

            if(this.fetchLoop > 5){
                throw new Error('loading error');
            }

            this.fetchTable()

        }).then((data) => {
            this.setState({
        		tableName: data.name,
        		tableColor: data.color,
        		tableColorBorder: data.border_color,
        		loadingTable: false,
        	})
           return data
    
        })
        .catch((error) => {
        	return "error"
        });;
    }


    fetchNotes(day, month, year){
		let params = "?"

		if(day){
			params += `day=${day}&`
		}
		if(month){
			params+= `month=${month}&`
		}
		if (year){
			params+= `year=${year}&`
		}
        
        this.fetchLoop++
        let res =  fetch(`${ServerStore.url}/api/tables/${TablesStore.id}/notes/${params}`, {
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
            	console.log("error")
                throw new Error('loading error');
            }
            this.fetchNotes()
        }).then((data) => {
        	var firstRun = false
        	
        	if(this.state.notes == null){
        		firstRun = true
        	}
        	this.setState({
        		notes: data,
        		loginNotes: false,
        	})

        	if(firstRun){
	        	this.pushPerDay(data)
        	}    
        })
        .catch((error) => {
          console.log(error)
          return "error"
        });;
    }


	fetchUsers(){
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
        	this.setState({
        		users: data,
        		loadingUsers: false,
        	})
        	
        	for(var i = 0; i<data.length; i++){
        		var tmp = {}
        		this.userColors[data[i].user_id] = data[i].color
        	}
           return data
        })
        .catch((error) => {
          return "error"
        });;
    }


    monthChange(event){
    	var date = event.activeStartDate
    	this.setState({
    		notes: null,
    		date: event.activeStartDate
    	})

		this.fetchNotes(0,date.getMonth()+1, date.getFullYear());

    }	

	dateChange(event){
		this.setState({
			date:event
		})

		this.fetchNotes(event.getDate(), event.getMonth()+1, event.getFullYear());

	}
	pushPerDay(data){
		for(var i=0; i<data.length; i++){
			var start = new Date(data[i].todo_date_start)
			var end = new Date(data[i].todo_date_end)
			var user = data[i].user_id

			if(this.state.date.getMonth() < end.getMonth()){
				end = new Date(start.getFullYear(), start.getMonth(), 31, end.getHours(), end.getMinutes())
				
				if(end.getDate() != 31){
					end = new Date(start.getFullYear(), start.getMonth(), 30, end.getHours(), end.getMinutes())
				}
			}

			var dif = end.getDate() - start.getDate()

			if(dif < 0 ){
				
				if(this.state.date.getMonth() == start.getMonth()){

					var evenMonths = [2,4,6,9,11,]

					if (evenMonths.indexOf(start.getMonth()+1) ){
						dif = 30 - start.getDate()+1
					}else{
						dif = 31 - start.getDate()
					}

				}else if(this.state.date.getMonth() == end.getMonth()){
					dif = end.getDate()-1
				
					start = new Date(start.getFullYear(), start.getMonth()+1, 1 , start.getHours(), start.getMinutes())
				
				}	
			}
			if(dif == 0){
				var asd = this.getButtonByDay(start.getDate())
				this.createInnerElement(asd, data[i])
			
			}else{	
				for(var j = 0; j<=dif; j++){
					var asd = this.getButtonByDay(start.getDate()+j)
					this.createInnerElement(asd, data[i])	
				}
			}
		}
	}

	getButtonByDay(day){
		var monthName = document.getElementsByClassName("react-calendar__navigation__label__labelText react-calendar__navigation__label__labelText--from")[0].innerHTML
		var yearName = monthName.split(" ")[1]
		monthName = monthName.split(" ")[0]
		

		 var elem = document.getElementsByClassName("react-calendar__tile react-calendar__month-view__days__day")
		
		for(var i = 0; i<elem.length; i++){
			try{
				var txt = elem[i]

				txt = txt.firstElementChild
				txt = txt.ariaLabel

			}catch{
				console.log("error fucked")
			}

			if (txt == `${monthName} ${day}, ${yearName}`){
				return elem[i]
			}
		}
	}

	createInnerElement(mainDiv, data){
		var inner = mainDiv.getElementsByClassName("innerButton")
		if (inner.length == 0){
			inner = document.createElement("div")
			inner.className += "innerButton"
		}else{
			inner = inner[0]
		}


		var tmpDiv = document.createElement("div")
		tmpDiv.style.backgroundColor = this.userColors[data.user_id]
		inner.appendChild(tmpDiv)
		mainDiv.append(inner)

	}

	render(){
		return(
		<div class="tablesBG">
			{this.state.users != null ? <LeftPanel users={this.state.users} />  : <h1>Loading..</h1>}

			<div className="calendarDiv">
			
				<h1>{this.state.tableName}</h1>
				<Calendar onChange={this.dateChange} 
				locale="en-EN" 
				onActiveStartDateChange={this.monthChange}
				view="month"
				/> 				
			</div>
			{ this.state.date  != null? <RightPanel  
										date={this.state.date} 
										notes={this.state.notes}
										userData={this.userColors}
										tableColor={this.state.tableColor}
										 /> : <h1>Loading...</h1>
										}
										
		</div>
			)				
		}
}
export default TableMain