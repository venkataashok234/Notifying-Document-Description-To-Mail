import json
import boto3

def lambda_handler(event, context):
    if event:
        s3=boto3.client('s3')
        # file_obj=event['Records'][0]
        # file_name= str(file_obj['s3']['object']['key'])
        
        data=s3.get_object(Bucket='b-06-08-2022',Key = 'numbers (1).txt')
        contents = data['Body'].read()
        res = len(contents.split())
        if event:
            client =boto3.client('sns')
            response = client.publish(
            TopicArn='arn:aws:sns:ap-south-1:273369647099:Word_Count_Result',
            
            # TargetArn='string',
            # PhoneNumber='string',   ,'numbers (1).txt',' is'+str( res) ,' .'
            
            
            Message='The Word count in the file numbers (1).txt is '+str(res),
            Subject='Word Count Result'
           )
        return 0