import json
import boto3
import requests

lambda_client = boto3.client('lambda')


def call_lambda_function(country):
  lambda_function_name = ('crossvpc-dev-mongoconnect-%s' % country)
  invoke_response = lambda_client.invoke(FunctionName=lambda_function_name,
                                          InvocationType='RequestResponse'
                                          )
  data = invoke_response['Payload'].read()
  return data


def hello(event, context):
    
    country = 'sg' #something for default
    if 'country' in event:
      country = event['country']
    
    data = call_lambda_function(country)

    r = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')
    apiresponse = r.json()

    response = {
        "statusCode": 200,
        "body": data.decode('utf-8'),
        "response": apiresponse
    }

    return response


def hi(event, context):

  data = call_lambda_function('sg')
  r = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')
  apiresponse = r.json()
  
  response = {
      "statusCode": 200,
      "body": data.decode('utf-8'),
      "response": apiresponse
  }

  return response



