# 📨 S3 to Email Automation with AWS Lambda & SES

This serverless data engineering pipeline automatically sends emails when a CSV is uploaded to an S3 bucket.

## 🔧 Tech Stack
- AWS S3
- AWS Lambda (Python)
- Amazon SES
- IAM

## 📦 Features
- Triggers on S3 file upload
- Reads CSV
- Sends email with attachment

## 🧪 Try It
1. Upload a file to S3
2. Lambda triggers
3. Email is sent via SES

## 📁 Structure
- `lambda_function.py`: Main Lambda code
- `iam-policy.json`: Permissions for S3 and SES
- `example.csv`: Sample file for testing

## 🔒 Note
Make sure your SES is in production mode or emails are verified if you're using the sandbox.
