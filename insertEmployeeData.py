import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employeeData')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        employee = {
            'employeeId': body['employeeId'],
            'name': body['name'],
            'department': body['department'],
            'salary': body['salary']
        }

        table.put_item(Item=employee)

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps("Employee added successfully!")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
