// Saves options to localStorage.


function save_options() {
	var select = document.getElementById("showas");
	localStorage["show_as"] = select.children[select.selectedIndex].value;
	localStorage["shorten_url"] = document.getElementById("short").checked;
	
	// Update status to let user know options were saved.
	document.getElementById("status").innerHTML = "Options Saved.";
	setTimeout(function() {document.getElementById("status").innerHTML = "";}, 750);
}


// Restores select box state to saved value from localStorage.


function restore_options() {
	var show_as = localStorage["show_as"];
	if (show_as) {
		var select = document.getElementById("showas");
		for (var i = 0; i < select.children.length; i++) {
			var child = select.children[i];
			if (child.value == show_as) {
				child.selected = "true";
				break;
			}
		}
	}
	a = localStorage["shorten_url"]
	check = document.getElementById("short")
	if (a=="true"){
		check.checked = a;
	}
}
document.addEventListener('DOMContentLoaded', restore_options);
document.querySelector('#save').addEventListener('click', save_options);
