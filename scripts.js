// 🔗 API Gateway URL
var API = "https://78252oc566.execute-api.us-east-1.amazonaws.com/dev/employees";


// =====================
// ✅ CREATE (POST)
// =====================
function saveEmployee() {

    var data = {
        employeeId: document.getElementById("employeeId").value,
        name: document.getElementById("name").value,
        department: document.getElementById("department").value,
        salary: document.getElementById("salary").value
    };

    fetch(API, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
        document.getElementById("msg").innerText = "Employee Saved!";
        getEmployees(); // 🔥 auto refresh
    })
    .catch(() => {
        document.getElementById("msg").innerText = "Error saving employee";
    });
}


// =====================
// ✅ READ (GET)  🔥 FIXED
// =====================
function getEmployees() {

    fetch(API)
    .then(res => res.json())
    .then(response => {

        // 🔥 FIX: handle API response correctly
        let data = typeof response.body === "string"
            ? JSON.parse(response.body)
            : response;

        let table = document.getElementById("table");

        // Reset table
        table.innerHTML = `
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Salary</th>
        </tr>`;

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
    })
    .catch(() => {
        document.getElementById("msg").innerText = "Error loading employees";
    });
}


// =====================
// ✅ UPDATE (PUT)
// =====================
function updateEmployee() {

    var data = {
        employeeId: document.getElementById("employeeId").value,
        name: document.getElementById("name").value,
        department: document.getElementById("department").value,
        salary: document.getElementById("salary").value
    };

    fetch(API, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
        document.getElementById("msg").innerText = "Employee Updated!";
        getEmployees(); // 🔥 refresh
    })
    .catch(() => {
        document.getElementById("msg").innerText = "Error updating employee";
    });
}


// =====================
// ✅ DELETE (DELETE)
// =====================
function deleteEmployee() {

    var data = {
        employeeId: document.getElementById("employeeId").value
    };

    fetch(API, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
        document.getElementById("msg").innerText = "Employee Deleted!";
        getEmployees(); // 🔥 refresh
    })
    .catch(() => {
        document.getElementById("msg").innerText = "Error deleting employee";
    });
}