import React from 'react';
import Calendar from 'react-calendar';

import ServerStore from "../../stores/ServerStore.jsx"
import UserStore from "../../stores/UserStore.jsx"
import CalendarStore from '../../stores/calendarStore.jsx'
import TablesStore from '../../stores/TablesStore.jsx'

class CalendarPanel extends React.Component {
	constructor(props){
		super()
		this.tableID = TablesStore.id
		this.fetchLoop = 0
		this.notes = props.notes
		this.state = {
			day: null,
			month: null,
			year: null,

		}
      this.dateChange = this.dateChange.bind(this);

	}

/*	componentWillMount(){
		var date = new Date()
		this.dateChange(date)
	}*/

	fetchNotes(date){
		const that = this;
		let params = "?"
		params += `year=${date.getFullYear()}&`
		params+= `month=${date.getMonth() + 1}&`
		params+= `day=${date.getDate()}&`
	

		console.log(params)
        this.fetchLoop++
        let res =  fetch(`${ServerStore.url}/api/tables/${this.tableID}/notes/${params}`, {
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
        	this.setState({
        		tasks: data
        	}) 
        	this.notes = data;
        	console.log(this.notes)
   
    
        })
        .catch((error) => {
          console.log(error)
          return "error"
        });;
    }


	dateChange(event){
		console.log(event)
		this.setState({
			day: event.getDate(),
			month: event.getMonth() + 1,
			year: event.getFullYear(),
		})
		
		this.fetchNotes(event);

	}
	render(){
		return(
			<Calendar
				onChange={this.dateChange}

			 />
			)
	}

}

export default CalendarPanel