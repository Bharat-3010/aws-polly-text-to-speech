import boto3
import time
import json

# Initialize clients
polly = boto3.client("polly")
s3 = boto3.client("s3")

def lambda_handler(event, context):
    try:
        # Get file details from S3 trigger event
        record = event["Records"][0]["s3"]
        source_bucket = record["bucket"]["name"]
        file_key = record["object"]["key"]

        # Read text file from source bucket
        obj = s3.get_object(Bucket="txt-polly-s3-bucket", Key=file_key)
        text = obj["Body"].read().decode("utf-8")

        # Convert text to speech using Polly
        polly_response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )

        # Validate Polly response
        if "AudioStream" not in polly_response:
            raise Exception("Polly did not return audio data")

        # Read audio stream
        audio_bytes = polly_response["AudioStream"].read()

        # Generate unique audio file name
        audio_key = f"speech-{int(time.time() * 1000)}.mp3"

        # Destination bucket (you can also use env variable)
        destination_bucket = "twy-polly-audio-files-storage-bucket"

        # Upload audio file to S3
        s3.put_object(
            Bucket="speech-polly-s3-bucket",
            Key=audio_key,
            Body=audio_bytes,
            ContentType="audio/mpeg",
            ContentLength=len(audio_bytes)
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Conversion successful",
                "source_file": file_key,
                "audio_file": audio_key
            })
        }

    except Exception as e:
        print("Error:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }