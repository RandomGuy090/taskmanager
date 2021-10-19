import ServerStore from "../stores/ServerStore.jsx"
import UserStore from "../stores/UserStore.jsx"

class TablesStore{
	constructor(){
		this.tables = "";
		this.id = ""
	}


	fetchTables(state){
	        let res =  fetch(`${ServerStore.url}/api/tables/`, {
	      credentials: 'include',
	        method: "GET",
	        headers: {
	        "Authorization": `Token ${UserStore.token}`,
	      },
	        }).then(res => {         
	          return res.json()
	        }).then(res => {
	            state.setState({
	             loading: false
	         })
	            TablesStore.tables = res;

	           return this.state.tables
	    
	        });
	    }
	
}
export default new TablesStore();