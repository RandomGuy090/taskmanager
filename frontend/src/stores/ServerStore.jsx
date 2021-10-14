class ServerStore{
	constructor(){
		this.protocol = "http";
		this.address = "127.0.0.1";
		this.port = "8000";
		if(this.port !== ""){
			this.url = `${this.protocol}://${this.address}:${this.port}`
		}else{
			this.url = `${this.protocol}://${this.address}`
		}
	}

	
}
export default new ServerStore();