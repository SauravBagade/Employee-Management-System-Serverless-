#  Employee Management System (AWS Serverless)

A fully serverless web application to manage employee data using **AWS Lambda, API Gateway, DynamoDB, and S3 Static Website Hosting**.

---

#  Architecture

Frontend (HTML/JS - S3)
⬇

API Gateway (REST API)
⬇

Lambda Functions (GET & POST)
⬇

DynamoDB (employeeData)

---

#  Services Used

* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB
* Amazon S3 (Static Hosting)
* IAM (Roles & Permissions)

---

#  Step 1: Create DynamoDB Table

1. Go to AWS Console → DynamoDB

2. Click **Create Table**

3. Enter details:

   * Table Name: `employeeData`
   * Partition Key: `employeeId` (String)

4. Click **Create Table**

---

#  Step 2: Create IAM Role for Lambda

1. Go to IAM → Roles → Create Role

2. Select:

   * Trusted Entity: AWS Service
   * Use Case: Lambda

3. Attach Permissions:

   * AmazonDynamoDBFullAccess
   * AWSLambdaBasicExecutionRole

4. Role Name: `Lambda-DynamoDB-Role`

5. Click **Create Role**

---

#  Step 3: Create Lambda Functions

---

##  1. Insert Employee Data (POST)

1. Go to Lambda → Create Function

2. Select **Author from scratch**

   * Function Name: `insertEmployeeData`
   * Runtime: Python 3.x
   * Permissions: Use existing role → `Lambda-DynamoDB-Role`

3. Click **Create Function**

4. Paste code from `insertEmployeeData.py`

5. Click **Deploy**

---

##  2. Get Employee Data (GET)

1. Go to Lambda → Create Function

2. Select **Author from scratch**

   * Function Name: `getEmployees`
   * Runtime: Python 3.x
   * Permissions: Use existing role → `Lambda-DynamoDB-Role`

3. Click **Create Function**

4. Paste code from `getEmployees.py`

5. Click **Deploy**

---

#  Step 4: Create API Gateway

1. Go to API Gateway → Create API
2. Select **REST API → Build**
3. API Name: `employee-api`
4. Click **Create API**

---

##  Create POST Method

1. Select **Resources → Actions → Create Method → POST**
2. Integration Type: Lambda
3. Select `insertEmployeeData`
4. Save & Test

---

##  Create GET Method

1. Select **Resources → Actions → Create Method → GET**
2. Integration Type: Lambda
3. Select `getEmployees`
4. Save & Test

---

##  Enable CORS

1. Select Resource `/`
2. Click **Actions → Enable CORS**
3. Apply for:

   * GET
   * POST

---

#  Step 5: Deploy API

1. Click **Actions → Deploy API**
2. Stage Name: `dev`
3. Copy **Invoke URL**

Example:

[https://your-api-id.execute-api.region.amazonaws.com/dev](https://your-api-id.execute-api.region.amazonaws.com/dev)

---

#  Step 6: Setup Frontend (S3)

1. Go to S3 → Create Bucket
2. Disable **Block Public Access**
3. Upload files:

   * index.html
   * scripts.js

---

## Enable Static Hosting

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

#  Step 7: Update API in scripts.js

```javascript
var API = "YOUR_API_INVOKE_URL";
```

---

#  Usage

1. Open S3 Website URL
2. Enter Employee Details
3. Click **Save** → Data stored in DynamoDB
4. Click **Load Employees** → Fetch all records

---

#  Features

* Add Employee
* View Employees
* Serverless Architecture
* Scalable & Cost Efficient

---

#  Future Enhancements

* Update Employee
* Delete Employee
* Search/Filter
* AWS Cognito Authentication
* Terraform (Infrastructure as Code)
* CI/CD Pipeline

---

#  Resume Line

Built a serverless Employee Management System using AWS Lambda, API Gateway, DynamoDB, and S3 with REST APIs and static frontend hosting.

---

#  Project Structure

employee-management/
├── index.html
├── scripts.js
├── insertEmployeeData.py
├── getEmployees.py
└── README.md

---

---
