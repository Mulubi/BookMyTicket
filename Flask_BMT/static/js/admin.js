// Array to store surgical procedures
var procedures = [];

// Function to add a surgical procedure
function addProcedure() {
	// Get form values
	var theatre = document.getElementById("theatre").value;
	var procedure = document.getElementById("procedure").value;
	var surgeon = document.getElementById("surgeon").value;
	var nurse = document.getElementById("nurse").value;
	var date = document.getElementById("date").value;
	var time = document.getElementById("time").value;

	// Create procedure object
	var procedureObj = {
		theatre: theatre,
		procedure: procedure,
		surgeon: surgeon,
		nurse: nurse,
		date: date,
		time: time
	};

	// Add procedure to array
	procedures.push(procedureObj);

	// Display procedures in table
	displayProcedures();
}

// Function to display surgical procedures in table
function displayProcedures() {
	// Get procedure list table body
	var procedureList = document.getElementById("procedure-list");

	// Clear table body
	procedureList.innerHTML = "";

	// Loop through procedures and add to table
	for (var i = 0; i < procedures.length; i++) {
		var procedure = procedures[i];

		// Create table row
		var row = document.createElement("tr");

		// Add data cells to row
		var theatreCell = document.createElement("td");
		theatreCell.textContent = procedure.theatre;
		row.appendChild(theatreCell);

		var procedureCell = document.createElement("td");
		procedureCell.textContent = procedure.procedure;
		row.appendChild(procedureCell);

		var surgeonCell = document.createElement("td");
		surgeonCell.textContent = procedure.surgeon;
		row.appendChild(surgeonCell);

		var nurseCell = document.createElement("td");
		nurseCell.textContent = procedure.nurse;
		row.appendChild(nurseCell);

		var dateCell = document.createElement("td");
		dateCell.textContent = procedure.date;
		row.appendChild(dateCell);

		var timeCell = document.createElement("td");
		timeCell.textContent = procedure.time;
		row.appendChild(timeCell);

		// Add row to table body
		procedureList.appendChild(row);
	}
}
