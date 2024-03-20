import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('OrdersTable')  # Replace 'OrdersTable' with your DynamoDB table name

def create_order(event):
    """
    Creates a new order.

    Parameters:
    - event: API Gateway event object containing order details.

    Returns:
    - response: API Gateway response object.
    """
    try:
        order_data = json.loads(event['body'])
        # Validate order data here if needed

        response = table.put_item(Item=order_data)
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Order created successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }