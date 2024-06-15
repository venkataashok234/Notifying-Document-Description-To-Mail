The File "AWS Lambda Function.py" is consists of lambda function code
This AWS Lambda function is designed to process an S3 event, read the contents of a specific text file stored in an S3 bucket, calculate the word count of the file , and publish the result to an SNS topic. Below is a detailed description of the function's operations and components
Detailed Steps
Event Check:

The function starts by checking if an event has triggered the function. The if event: statement ensures the function proceeds only when an event is present.
S3 Client Initialization:

A boto3 S3 client is initialized using s3 = boto3.client('s3').
Retrieve the File from S3:

The function fetches the file numbers (1).txt from the specified S3 bucket b-06-08-2022 using the get_object method.
data = s3.get_object(Bucket='b-06-08-2022', Key='numbers (1).txt').
Read File Contents:

The contents of the file are read into a variable contents using data['Body'].read().
Calculate Word Count:

The number of words in the file is calculated by splitting the contents by spaces and counting the resulting elements.
res = len(contents.split()).
SNS Client Initialization:

If the event check is still valid, an SNS client is initialized using client = boto3.client('sns').
Publish Result to SNS:

The word count result is published to the specified SNS topic arn:aws:sns:ap-south-1:273369647099:Word_Count_Result.
The message includes the file name and the word count.
response = client.publish(TopicArn='arn:aws:sns:ap-south-1:273369647099:Word_Count_Result', Message='The Word count in the file numbers (1).txt is ' + str(res), Subject='Word Count Result').
