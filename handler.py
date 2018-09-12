import json
import boto3

lambda_client = boto3.client('lambda')


def hello(event, context):
    
    country = 'sg' #something for default
    if 'country' in event:
      country = event['country']
    
    lambda_function_name = ('crossvpc-dev-mongoconnect-%s' % country)
    invoke_response = lambda_client.invoke(FunctionName=lambda_function_name,
                                           InvocationType='RequestResponse'
                                           )
    data = invoke_response['Payload'].read()
    response = {
        "statusCode": 200,
        "body": data.decode('utf-8')
    }

    return response
