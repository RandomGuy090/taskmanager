var ret = document.querySelectorAll('[class="cal"] > p');

ret.forEach(elem => {
	if(elem.innerHTML.length > 8){
		elem.innerHTML = elem.innerHTML.substring(0, 7) + "...";

	}
})