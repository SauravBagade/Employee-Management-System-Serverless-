import json
import boto3

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employeeData')

def lambda_handler(event, context):
    try:
        # Parse request body from API Gateway
        body = json.loads(event['body'])

        # Extract fields
        employee = {
            'employeeId': body['employeeId'],
            'name': body['name'],
            'department': body['department'],
            'salary': body['salary']
        }

        # Insert into DynamoDB
        table.put_item(Item=employee)

        return {
            'statusCode': 200,
            'headers': {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "message": "Employee added successfully",
                "data": employee
            })
        }

    except KeyError as e:
        return {
            'statusCode': 400,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "error": f"Missing field: {str(e)}"
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "error": str(e)
            })
        }
