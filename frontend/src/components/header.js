import React from "react"
import UserStore from "../stores/UserStore.jsx"


/*const Header = ({ username }) => {
	return (
		<header>
			<a href="/api/logout" className="logout">
				<div>Logout</div>
			</a>
			<p> { username }</p>
			<img src='/profile.png' />
		</header>

	)
}

*/
class Header extends React.Component  {

	constructor(){
		super()

		}


	render(){

		return (
			<header>
				<a href="/logout" className="logout">
					<div>Logout</div>
				</a>
				<p> { UserStore.username }</p>
				<img src='/profile.png' />
			</header>

		)
	}

}


export default Header;