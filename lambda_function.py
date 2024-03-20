import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('OrdersTable')  # Replace 'OrdersTable' with your DynamoDB table name

def lambda_handler(event, context):
    """
    Handles incoming API Gateway requests.

    Parameters:
    - event: API Gateway event object containing request details.
    - context: Lambda function runtime information.

    Returns:
    - response: API Gateway response object.
    """
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        return create_order(event)
    elif http_method == 'PUT':
        return update_order(event)
    elif http_method == 'GET':
        return get_all_orders()
    elif http_method == 'DELETE':
        return delete_order(event)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method Not Allowed'})
        }


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
        
def update_order(event):
    """
    Updates an existing order.

    Parameters:
    - event: API Gateway event object containing updated order details.

    Returns:
    - response: API Gateway response object.
    """
    try:
        order_id = event['queryStringParameters']['id']
        updated_data = json.loads(event['body'])
        # Validate updated data here if needed

        response = table.update_item(
            Key={'id': order_id},
            UpdateExpression='SET #data = :val1',
            ExpressionAttributeNames={'#data': 'data'},
            ExpressionAttributeValues={':val1': updated_data}
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Order updated successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
def get_all_orders():
    """
    Retrieves all orders from the database.

    Returns:
    - response: API Gateway response object.
    """
    try:
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
        
def delete_order(event):
    """
    Deletes an order.

    Parameters:
    - event: API Gateway event object containing order ID.

    Returns:
    - response: API Gateway response object.
    """
    try:
        order_id = event['queryStringParameters']['id']

        response = table.delete_item(Key={'id': order_id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Order deleted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

