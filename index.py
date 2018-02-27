import json
import datetime
import boto3

rekog = boto3.client('rekognition')

response = rekog.recognize_celebrities(
    Image={
        
        'S3Object': {
          
            'Name': 'kognition',
            'Version': 'bp.jpg'
        }
    }
)

def handler(event, context):
    data = {
        'output': str(response),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
