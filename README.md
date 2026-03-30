#  AWS Serverless Employee Management System (AWS Setup Guide)

##  Overview

This document explains how to create a **serverless backend on AWS** using:

* Amazon DynamoDB
* AWS Lambda
* Amazon API Gateway
* Amazon S3 (for hosting frontend)

---

#  Step 1: Create DynamoDB Table

1. Go to **AWS Console**
2. Navigate to **DynamoDB**
3. Click **Create Table**

### Configuration:

* Table Name: `employeeData`
* Partition Key: `employeeId` (String)
* Keep default settings

4. Click **Create Table**

---

#  Step 2: Create IAM Role for Lambda

1. Go to **IAM → Roles**
2. Click **Create Role**

### Select:

* Trusted Entity: **AWS Service**
* Use Case: **Lambda**

3. Click **Next**

### Attach Permissions:

* `AmazonDynamoDBFullAccess`
* `AWSLambdaBasicExecutionRole`

4. Role Name:

```text
Lambda-DynamoDB-Role
```

5. Click **Create Role**

---

#  Step 3: Create Lambda Functions

Create the following 4 Lambda functions:

---

## 1️⃣ Insert Employee

* Name: `insertEmployeeData`
* Runtime: Python 3.x
* Architecture: x86_64
* Execution Role: `Lambda-DynamoDB-Role`

👉 Deploy the function code

---

## 2️⃣ Get Employees

* Name: `getEmployees`
* Runtime: Python 3.x
* Role: Same IAM role

👉 Deploy the function code

---

## 3️⃣ Update Employee

* Name: `updateEmployee`
* Runtime: Python 3.x
* Role: Same IAM role

👉 Deploy the function code

---

## 4️⃣ Delete Employee

* Name: `deleteEmployee`
* Runtime: Python 3.x
* Role: Same IAM role

👉 Deploy the function code

---

#  Step 4: Create API Gateway (REST API)

1. Go to **API Gateway**
2. Click **Create API**
3. Choose **REST API → Build**

---

## API Configuration

* API Name: `employee-api`
* Endpoint Type: Regional

Click **Create API**

---

## ➤ Create Resource

1. Click **Actions → Create Resource**

### Enter:

* Resource Name: `employees`
* Resource Path: `/employees`

Click **Create Resource**

---

##  Create Methods

Create the following methods under `/employees`:

---

### 🔹 GET Method

* Integration Type: Lambda
* Lambda Function: `getEmployees`
* Enable: ✅ Lambda Proxy Integration

---

### 🔹 POST Method

* Integration Type: Lambda
* Lambda Function: `insertEmployeeData`
* Enable: ✅ Lambda Proxy Integration

---

### 🔹 PUT Method

* Integration Type: Lambda
* Lambda Function: `updateEmployee`
* Enable: ✅ Lambda Proxy Integration

---

### 🔹 DELETE Method

* Integration Type: Lambda
* Lambda Function: `deleteEmployee`
* Enable: ✅ Lambda Proxy Integration

---

#  Step 5: Enable CORS

1. Select `/employees`
2. Click **Actions → Enable CORS**

### Allow:

* Methods: GET, POST, PUT, DELETE
* Headers: Default
* Origin:

```text
*
```

3. Click **Enable CORS and replace existing headers**

---

# 🚢 Step 6: Deploy API

1. Click **Actions → Deploy API**

### Configuration:

* Stage Name: `dev`

2. Click **Deploy**

---

##  Invoke URL

After deployment, you will get:

```text
https://<api-id>.execute-api.<region>.amazonaws.com/dev/employees
```

---

#  Step 7: Setup S3 (Frontend Hosting)

1. Go to **S3 → Create Bucket**

### Configuration:

* Bucket Name: `employee-management-frontend`
* Region: Same as API

---

## Disable Public Access

* Uncheck **Block all public access**
* Acknowledge warning

---

## Upload Files

Upload:

* `index.html`
* `scripts.js`

---

## Enable Static Website Hosting

1. Go to **Properties**
2. Enable **Static Website Hosting**

### Configuration:

* Index Document: `index.html`

---

## Add Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::<bucket-name>/*"
    }
  ]
}
```

---

#  Step 8: Testing

1. Open S3 website URL
2. Perform operations:

   * Add Employee
   * View Employees
   * Update Employee
   * Delete Employee

---

#  Common Issues & Fixes

| Issue            | Solution               |
| ---------------- | ---------------------- |
| API not working  | Deploy API again       |
| CORS error       | Enable CORS + redeploy |
| Lambda error     | Check CloudWatch logs  |
| Data not showing | Verify API URL         |

---

# 👨‍💻 Author

**Saurav Bagade**

---
