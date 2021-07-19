/*tables*/
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
				/*window.location.reload()*/
/*				 var day = $("#sideDay").html();
   				 var monthX = $("#sideMonth").html();
   				 monthX = month.indexOf(monthX)+1
   				 var year = */
				fetchMonth(YEAR, MONTH)

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
	var errWin = document.getElementById("sendingError")

	if(opWind.style["visibility"] == "visible"){
		if (event.target.className.indexOf("nohid") == -1) {
			console.log("aaaa")
			
			$("#newTaskMenu").animate({
				bottom: "-40vh"
			},1000, function(){
				bottom: "0vh"
				opWind.style["visibility"] = "hidden";
			})
			
		}
	}else{
			console.log("bbbbbbbbb")
		if(event.target.id.indexOf("addNewNote") != -1){

			opWind.style["visibility"] = "visible";
			$("#newTaskMenu").animate({
				bottom: "0vh"
			},1000, function(){
				bottom: "-41vh"
			})

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


window.onload =  setTimeout(x=>{
		fetchMonth();
		changeMainColor()
	}
	, 1000)

function changeMainColor(){
	var color =  $("body").css("--3Col").substring(2);
	var x = Array()
	x.push(`${color[0]}${color[1]}`)

	x.push(`${color[2]}${color[3]}`)
	x.push(`${color[4]}${color[5]}`)
	console.log(x)
	/*css("background-color", "")*/
	if (x[0] == x[1] && x[0] == x[2]) {
		console.log("similar")
		/*$("body").css("--3Col", "#656565")*/
		  $("body").get(0).style.setProperty("--3Col", "#656565");
	}
}

function fetchMonth(year, month, day) { 
	console.log("fetch")

  	

	var lol = new Date()

  	var day = (typeof day !== 'undefined') ? day : lol.getDate();;
	var month = (typeof month !== 'undefined') ? month : lol.getMonth() + 1;
	var year = (typeof year !== 'undefined') ? year : lol.getFullYear();
	console.log(`${year} ${month} ${day}`)
	



	month = month +""
	


	var tableId = window.location.href.substring(window.location.href.lastIndexOf("/")+1)
	var url = window.location.origin + `/info/${tableId}`
	
	var ret = {
		"month": month,
		"year": year,
		"url": tableId,
		}
	$(".usedBy").empty()
		post(url, ret)
  	.then(data => {
  	data.json().then( data =>{
  		data = data["tasks"];
  		console.log(data)

  		for(i=0; i<data.length; i++){
  			var elem = data[i];
  			console.log(elem)

  			var day = elem["to_do_date"];
  			console.log(day)


  			day = day.split("-")[2].split("T")[0];
  			day = parseInt(day)
  			console.log(day)

  			
  			/*var divHandler = $(`dayCount_${day}`);*/
  			var divHandler = document.getElementsByClassName(`dayCount_${day}`)[0];
  			/*divHandler.innerHTML = ""*/

            var lol = document.createElement("div");
            lol.style["background-color"] = elem["task_color"]

  			
  			divHandler.append(lol)
  		
  		}
  	})

  });

      }