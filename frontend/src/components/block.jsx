import React from "react"
import { 
	Route, 
	Link, 
	BrowserRouter as Router, 
	useHistory
} from 'react-router-dom'




const Block = (props) => {
	const table = props.table
	const color = table.table_id.color
	const url = table.table_id.url
	const name = table.table_id.name
	const borderColor = table.table_id.border_color
	return(

	<Link to={`table/${url}`}>

			<div className="cal"
			style={{
	        backgroundColor: color ,
	        borderColor: borderColor ,
	      }}
	      >
				<p>{name}</p>

			</div>
		</Link>		
   )
}


export default Block
