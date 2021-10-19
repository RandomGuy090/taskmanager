class UserCache{
	constructor(){
		this.users = {}
	}
}

//localStorage.getItem('token')  ? null : ""
export default new UserCache();