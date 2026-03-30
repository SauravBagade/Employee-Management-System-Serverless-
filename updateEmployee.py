import json
import boto3

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employeeData')

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])

        # Extract fields
        employeeId = body['employeeId']
        name = body['name']
        department = body['department']
        salary = body['salary']

        # Update item in DynamoDB
        table.update_item(
            Key={'employeeId': employeeId},
            UpdateExpression="SET #n = :n, department = :d, salary = :s",
            ExpressionAttributeNames={
                '#n': 'name'   # 'name' is reserved keyword workaround
            },
            ExpressionAttributeValues={
                ':n': name,
                ':d': department,
                ':s': salary
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,
            'headers': {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "message": "Employee updated successfully",
                "employeeId": employeeId
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
