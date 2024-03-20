import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('OrdersTable')  # Replace 'OrdersTable' with your DynamoDB table name
