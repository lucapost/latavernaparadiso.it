function listswitch() { 
	element = document.querySelectorAll("li.listswitch");
	if (element) { 
		var list=new Array(); 
		for (var i = 0; i < element.length; i++) 
		{ 
			list[i] = element[i].innerHTML 
		} 
		for (var i = 0; i < list.length; i++) 
		{ 
			element[i].innerHTML = list[list.length-(i+1)]; 
		} 
	} 
} 
window.onload = listswitch; 
