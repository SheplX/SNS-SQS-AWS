import os

import boto3

# Publishing a msgs to SNS topic
def publish_message_to_sns(message: str): 
    topic_arn = os.environ["sns_topic_arn"]

    sns_client = boto3.client(
        "sns",
        region_name="eu-west-1",
    )

    message_id = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
    )

    return message_id

# Reading the recieved msgs to the Queue
def read_from_sqs_queue():
    queue_url = os.environ["sqs_queue_url"]
    sqs_client = boto3.client(
        "sqs",
        region_name="eu-west-1",
    )

    messages = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
    )

    return messages