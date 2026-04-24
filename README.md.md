# AWS Polly Text-to-Speech (Serverless Project)

## 📌 Overview
This project demonstrates a serverless application using AWS services where a text file uploaded to S3 is automatically converted into speech using AWS Polly.

## ⚙️ Services Used
- AWS Lambda
- Amazon S3
- Amazon Polly
- IAM

## 🔄 Workflow
1. Upload `.txt` file to S3 bucket
2. S3 triggers Lambda function
3. Lambda reads text file
4. AWS Polly converts text to speech
5. Audio file (.mp3) is stored in another S3 bucket

## 📁 Project Structure
- `lambda_function.py` → Main Lambda code
- `requirements.txt` → Dependencies

## 🚀 How to Deploy
1. Create two S3 buckets:
   - Source bucket (for text files)
   - Destination bucket (for audio files)
2. Create Lambda function
3. Add IAM permissions (S3 + Polly)
4. Configure S3 trigger
5. Upload `.txt` file → MP3 generated automatically

## 🎯 Key Learnings
- Event-driven architecture
- Serverless computing
- AWS Polly integration
- S3 triggers and automation