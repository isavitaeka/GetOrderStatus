import json
import boto3
import base64
import string
import random
import uuid
import logging
logger = logging.getLogger()
logger.setLevel("INFO")
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

ORDER_TABLE = 'OrderDB'
response = ''
ddbclient = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb', 'eu-north-1')
paginator = ddbclient.get_paginator('scan')

def lambda_handler(event, context):
    logger.info("GetListOfOrder")
    logger.info(event);
    email = event['queryStringParameters']['email']

    logger.info ("GetListOfOrder" + email)


    #for page in iterator:
    #    for item in page['Items']:
    #        print (json.dumps(item))
    try:    
        #response = table.get_item(
        #    Key={
        #        'email' : 'savitasingh18@gmail.com'
        #        }
        #    )
            
        response = ddbclient.query(
            TableName=ORDER_TABLE,
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={
                ':email': {'S': email}
            }
        )
        logger.info (json.dumps(response))
        

    #logger.info(response)
    
    except Exception as err:
        logger.error(err)

    
    return {
         'statusCode' : 200,
        "headers": {
        "Access-Control-Allow-Origin": "*"
    },
         'body' : json.dumps(response)
        
    }
