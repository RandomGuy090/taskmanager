


var ret = document.querySelectorAll('[class="cal"] > p');

ret.forEach(elem => {
	if(elem.innerHTML.length > 8){
		elem.innerHTML = elem.innerHTML.substring(0, 7) + "...";

	}
})



/*get tables list*/
//
//

function push_elements(elem){
	var a = document.createElement("a");
	a.href = `tables/${elem.table_id.url}`
	console.log(elem)
	var div = document.createElement("div");
	div.className += "cal";
	div.style.backgroundColor = elem.table_id.color;
	div.style.borderColor = elem.table_id.border_color;
	var p = document.createElement("p");
	p.innerText = elem.table_id.name;

	div.appendChild(p);
	a.appendChild(div);
	console.log(a)
	console.log(a)
	var home = document.getElementsByTagName("content")[0]
	home.appendChild(a);



}

function get_tables(){

	var request = new XMLHttpRequest()

	request.open('GET', 'http://127.0.0.1:8000/api/tables', true)
	request.onload = function () {
	  // Begin accessing JSON data here
	  var data = JSON.parse(this.response)

	  if (request.status >= 200 && request.status < 400) {

	      /*console.log(this.response)*/
	      console.log(data)
	      data.forEach (asd => {
	      	push_elements(asd)

	      })

	  } else {
	    console.log('error')
	  }
	}

	request.send()

}
get_tables()