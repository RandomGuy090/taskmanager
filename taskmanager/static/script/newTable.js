/*var newTable = document.getElementById("new_table");*/

document.onclick = function(event){
	var fg_blurred = document.getElementById("new_table_menu");
	var bg = document.getElementById("background_blurred");
	if(event.target.className !== 'no_hid' && bg.style["visibility"] == "visible"){

		if(bg.style["visibility"] == "visible"){
			bg.style["visibility"]= "hidden";
			window.location.reload()
		}else{
			bg.style["visibility"]= "visible";
		}
    }
    /*console.log(event.target.className)*/
    if(event.target.className === 'add_new_img'){
		bg.style["visibility"]= "visible";
    }
}

/*_____ sending to server______*/
var send = document.getElementById("send")

send.addEventListener("click", sendTable)

function getVals(){
	var color = document.getElementsByName("color_main")[0].value
	var title = document.getElementsByName("name")[0].value
	var password = document.getElementsByName("password")[0].value
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value

	return {"color":color, 
			"title": title, 
			"password": password,
			'csrftoken': token
		}
	}

function sendTable(){
	var req = new XMLHttpRequest();
	var url = window.location.href + "create/"
	var vals = getVals();
	console.log(vals)
	
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value
	var header = {"X-CSRFToken": token};

	/*req.open('GET', url+'/', false);
	req.send(null);
	if(req.status == 200)
	  dump(req.responseText);*/

	post(url, header, vals)
  .then(response => response.json())
  .then(data => {
  	loadLink(window.location.href +"tables/"+ data["url"])
  	console.log(window.location.href +"tables/"+ data["url"])

  });

// ...
/*RUPnHJd1y6JfxD1TFXcqEt1q6EkFFypDbf1yL2mmBE1VoOx2M5hYoHfS93l4qzMC*/
	function loadLink(link){
		var show = document.getElementById("tableLink");
		show.innerHTML = link;
	}
}
	window.post = function(url, header, data) {

  return fetch(url, {method: "POST", header: JSON.stringify(header), body: JSON.stringify(data)});
}