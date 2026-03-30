#  Employee Management System (AWS Serverless - FULL CRUD)

A fully serverless web application to perform **CRUD operations (Create, Read, Update, Delete)** on employee data using:

* AWS Lambda
* API Gateway
* DynamoDB
* S3 Static Website Hosting

---

#  Architecture

Frontend (HTML/JS - S3)
⬇
API Gateway (REST API)
⬇
Lambda Functions (CRUD)
⬇
DynamoDB (employeeData)

---

#  Services Used

* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB
* Amazon S3
* IAM (Roles & Permissions)

---

#  Step 1: Create DynamoDB Table

1. Go to **AWS Console → DynamoDB**

2. Click **Create Table**

3. Enter:

   * Table Name: `employeeData`
   * Partition Key: `employeeId` (String)

4. Click **Create Table**

---

#  Step 2: Create IAM Role for Lambda

1. Go to **IAM → Roles → Create Role**

2. Select:

   * Trusted Entity: AWS Service
   * Use Case: Lambda

3. Attach Policies:

   * AmazonDynamoDBFullAccess
   * AWSLambdaBasicExecutionRole

4. Role Name: `Lambda-DynamoDB-Role`

5. Click **Create Role**

---

#  Step 3: Create Lambda Functions

---

##  1. Create Employee (POST)

* Function Name: `insertEmployeeData`
* Runtime: Python 3.x
* Role: `Lambda-DynamoDB-Role`

 Upload code from: `insertEmployeeData.py`
 Click **Deploy**

---

##  2. Get Employees (GET)

* Function Name: `getEmployees`

 Upload code from: `getEmployees.py`
 Deploy

---

##  3. Update Employee (PUT)

* Function Name: `updateEmployee`

 Upload code from: `updateEmployee.py`
 Deploy

---

##  4. Delete Employee (DELETE)

* Function Name: `deleteEmployee`

 Upload code from: `deleteEmployee.py`
 Deploy

---

#  Step 4: Create API Gateway

1. Go to **API Gateway → Create API**
2. Choose **REST API → Build**
3. API Name: `employee-api`
4. Click **Create API**

---

##  Add Methods

| Method | Lambda             |
| ------ | ------------------ |
| POST   | insertEmployeeData |
| GET    | getEmployees       |
| PUT    | updateEmployee     |
| DELETE | deleteEmployee     |

### Steps:

1. Select **Resources → Actions → Create Method**
2. Choose method (POST/GET/PUT/DELETE)
3. Integration Type: **Lambda**
4. Select respective Lambda
5. Click **Save**

---

#  Step 5: Enable CORS

1. Select resource `/`

2. Click **Actions → Enable CORS**

3. Enable for:

   * GET
   * POST
   * PUT
   * DELETE

4. Confirm changes

---

#  Step 6: Deploy API

1. Click **Actions → Deploy API**
2. Stage Name: `dev`
3. Copy **Invoke URL**

Example:

https://your-api-id.execute-api.region.amazonaws.com/dev

---

#  Step 7: Setup Frontend (S3)

---

## Create Bucket

1. Go to **S3 → Create Bucket**
2. Disable **Block Public Access**
3. Upload:

   * index.html
   * scripts.js

---

## Enable Static Website Hosting

1. Go to **Properties → Static Website Hosting**
2. Enable
3. Index Document: `index.html`

---

## Add Bucket Policy

Replace `<bucket-name>`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::<bucket-name>/*"
    }
  ]
}
```

---

#  Step 8: Update API URL

In `scripts.js`:

```javascript
var API = "YOUR_API_INVOKE_URL";
```

---

#  Usage

1. Open S3 website URL
2. Enter employee details
3. Click:

   * Save → Create
   * Load Employees → Read
   * Update → Modify data
   * Delete → Remove employee

---

#  Features

* Add Employee
* View Employees
* Update Employee
* Delete Employee
* Serverless Architecture

---

#  Project Structure

employee-management/
├── index.html
├── scripts.js
├── insertEmployeeData.py
├── getEmployees.py
├── updateEmployee.py
├── deleteEmployee.py
└── README.md

---

#  Future Enhancements

* Search Employee
* Filter by Department
* Pagination
* AWS Cognito Authentication
* Terraform Deployment
* CI/CD Pipeline

---

#  Resume Line

Developed a full CRUD Employee Management System using AWS Lambda, API Gateway, DynamoDB, and S3 with serverless architecture.

---
