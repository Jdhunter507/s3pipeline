import boto3
import os
import email
from email.message import EmailMessage

s3 = boto3.client('s3')
ses = boto3.client('ses')

SENDER = os.environ['SENDER_EMAIL']
RECIPIENT = os.environ['RECIPIENT_EMAIL']

def lambda_handler(event, context):
    # Extract bucket and file key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download the file
    tmp_path = f"/tmp/{key.split('/')[-1]}"
    s3.download_file(bucket, key, tmp_path)

    # Read file contents
    with open(tmp_path, 'rb') as f:
        attachment = f.read()

    # Compose email
    msg = EmailMessage()
    msg['Subject'] = f'New File Uploaded: {key}'
    msg['From'] = SENDER
    msg['To'] = RECIPIENT
    msg.set_content(f'The file {key} has been uploaded to your S3 bucket.')
    msg.add_attachment(attachment, maintype='application', subtype='csv', filename=key)

    # Send email
    response = ses.send_raw_email(
        Source=SENDER,
        Destinations=[RECIPIENT],
        RawMessage={'Data': msg.as_bytes()}
    )
    return {"status": "Email sent", "message_id": response['MessageId']}
