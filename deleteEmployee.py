import json
import boto3

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employeeData')

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])

        # Extract employeeId
        employeeId = body['employeeId']

        # Delete item from DynamoDB
        table.delete_item(
            Key={
                'employeeId': employeeId
            },
            ConditionExpression="attribute_exists(employeeId)"  # Prevent deleting non-existing item
        )

        return {
            'statusCode': 200,
            'headers': {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "message": "Employee deleted successfully",
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

    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
        return {
            'statusCode': 404,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "error": "Employee not found"
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
