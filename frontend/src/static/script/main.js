window.post = function(url,data) {
	header = "";
	if (header === "undefined"){
		header= ""
}else{
		header= JSON.stringify(header)

	}
  return fetch(url, {method: "POST", body: JSON.stringify(data)});
}