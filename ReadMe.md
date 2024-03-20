# Serverless E-commerce Application with AWS Lambda and DynamoDB

This repository contains the source code for a serverless e-commerce application built using AWS Lambda, API Gateway, and DynamoDB. The application provides RESTful endpoints for managing orders, including creating, updating, retrieving, and deleting orders.

## Features

- **Create Order**: Endpoint for creating a new order with product details.
- **Update Order**: Endpoint for updating an existing order with new product details.
- **Get All Orders**: Endpoint for retrieving all orders stored in the database.
- **Delete Order**: Endpoint for deleting an existing order.

## Technologies Used

- **AWS Lambda**: Serverless compute service for executing code in response to events.
- **API Gateway**: Fully managed service for creating, publishing, maintaining, monitoring, and securing APIs.
- **DynamoDB**: Fully managed NoSQL database service provided by AWS.
- **Python**: Programming language used for writing Lambda functions.

## Deployment

The application is designed to be deployed using AWS CloudFormation or AWS SAM (Serverless Application Model) for easy setup and management. Follow the instructions below to deploy the application:

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/ngofficial99/Python-Ecom-serverless-app-and-CF-template
    ```

2. Deploy the application using AWS CloudFormation or AWS SAM.

3. Once deployed, you can access the API endpoints provided by API Gateway to interact with the application.

## Endpoints

### Create Order

- **Method**: POST
- **Path**: `/orders`
- **Request Body Example**:
    ```json
    {
        "id": "1",
        "product": "Product Name",
        "quantity": 2
    }
    ```

### Update Order

- **Method**: PUT
- **Path**: `/orders/{id}`
- **Request Body Example**:
    ```json
    {
        "product": "Updated Product Name",
        "quantity": 3
    }
    ```

### Get All Orders

- **Method**: GET
- **Path**: `/orders`

### Delete Order

- **Method**: DELETE
- **Path**: `/orders/{id}`

## Usage

Developers can use this project as a template for building their own serverless applications or as a learning resource for understanding AWS serverless architecture and services. Contributions and feedback are welcome!
