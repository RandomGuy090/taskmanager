import {extendObservable} from "mobx";

class UserStore{
	constructor(){
		extendObservable(this,{
			loading: true,
			isLogged: false,
			username: "",
			token: localStorage.getItem("token"),
		})
	}
}

//localStorage.getItem('token')  ? null : ""
export default new UserStore();