
$("#send_task").click((event)=>{
	var time = $("#hour_task").val();
	var day = $("#day_task").val();
	var task = $("#task_name").val();

	/*
	day = day.split("-");
	day = `${day[2]}-${day[1]}-${day[0]}`*/
	ret = {
		"time": time,
		"day": day,
		"task": task
	}
	var tableId = window.location.href.substring(window.location.href.lastIndexOf("/")+1)
	var url = window.location.origin + `/create/task/${tableId}`

	
	post(url, ret)
	.then(data =>{
		
		data.json().then(d => {
			
			if (d["success"]) {
				window.location.reload()
			}else if(d["success"] == false){
				var errDiv = document.getElementById("sendingError")
				errDiv.style["visibility"] = "visible";
				errDiv.innerHTML = d["error"];
			}
		})
	})
})



document.onclick = function(event){
	var opWind =  document.getElementById("newTaskMenu")
	
	if(opWind.style["visibility"] == "visible"){
		if (event.target.className.indexOf("nohid") == -1) {
			opWind.style["visibility"] = "hidden";
		}
	}else{
		if(event.target.id.indexOf("addNewNote") != -1){
			opWind.style["visibility"] = "visible";

		}

	}
}




function click(day, month, year){
	/*post to http://base/info/url*/
	var day = (typeof day !== 'undefined') ? day : "";
	var month = (typeof month !== 'undefined') ? month : "";
	var year = (typeof year !== 'undefined') ? year : "";
	$(".notes").empty();
	month = month +""
	
	if (month.length == 1) {
		month = "0"+month;
	}
	if (day.length == 1) {
		day = "0"+day;
	}


	console.log(`${year}-${month}-${day}`)
	$("#day_task").val(`${year}-${month}-${day}`);


	var tableId = window.location.href.substring(window.location.href.lastIndexOf("/")+1)
	var url = window.location.origin + `/info/${tableId}`
	var ret = {
		"day": day,
		"month": month,
		"year": year,
		"url": tableId,

	}
/*get tasks on day*/
	post(url, ret)
  .then(data => {
  	data.json().then( data =>{
  		pushDayNotes(data["tasks"])
  	})

  });
}


function pushDayNotes(data){
	var maindiv = $(".notes");

	for (var i = 0; i < data.length; i++) {
		var divInput = document.createElement("div");
		divInput.className = "note"

		var x = `
				<div class="hour" style="background-color: ${data[i]["task_color"]}" >${parseTime(data[i]["to_do_date"])}</div>
				<div class="author">${data[i]["user"]}</div>
				<div class="task">${data[i]["note"]}</div>
		`
		divInput.innerHTML = x
		maindiv.append(divInput)

		
	}
}
function parseTime(time){
	time = time.substring(time.indexOf("T")+1)
	time = time.substring(0, 5)
	return time
}


window.onload =  setTimeout(fetchMonth(), 1000)



function fetchMonth(year, month, day) { 
  	

	var lol = new Date()

  	var day = (typeof day !== 'undefined') ? day : lol.getDate();;
	var month = (typeof month !== 'undefined') ? month : lol.getMonth() + 1;
	var year = (typeof year !== 'undefined') ? year : lol.getFullYear();

	



	month = month +""
	


	var tableId = window.location.href.substring(window.location.href.lastIndexOf("/")+1)
	var url = window.location.origin + `/info/${tableId}`
	
	var ret = {
		"month": month,
		"year": year,
		"url": tableId,
		}
		post(url, ret)
  	.then(data => {
  	data.json().then( data =>{
  		data = data["tasks"];

  		for(i=0; i<data.length; i++){
  			var elem = data[i];
  			var day = elem["to_do_date"];
  			day = day.split("-")[2].split("T")[0];
  			
  			/*var divHandler = $(`dayCount_${day}`);*/
  			var divHandler = document.getElementsByClassName(`dayCount_${day}`)[0];

            var lol = document.createElement("div");
            lol.style["background-color"] = elem["task_color"]
  			divHandler.append(lol)
  		
  		}
  	})

  });

      }