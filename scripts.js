var API = "YOUR_API_URL_HERE";

// SAVE
function saveEmployee() {

    var data = {
        employeeId: document.getElementById("employeeId").value,
        name: document.getElementById("name").value,
        department: document.getElementById("department").value,
        salary: document.getElementById("salary").value
    };

    fetch(API, {
        method: "POST",
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
        document.getElementById("msg").innerText = "Saved!";
    });
}

// GET
function getEmployees() {

    fetch(API)
    .then(res => res.json())
    .then(data => {

        let table = document.getElementById("table");
        table.innerHTML += "";

        data.forEach(emp => {
            let row = `
            <tr>
                <td>${emp.employeeId}</td>
                <td>${emp.name}</td>
                <td>${emp.department}</td>
                <td>${emp.salary}</td>
            </tr>`;
            table.innerHTML += row;
        });
    });
}
