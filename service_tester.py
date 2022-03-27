import json
import os

import boto3
from moto import mock_sns, mock_sqs
from service_handler import publish_message_to_sns, read_from_sqs_queue


@mock_sns
# Testing publish the msgs to SNS topic
def test_publish_message_to_sns():
    sns_resource = boto3.resource(
        "sns",
        region_name="eu-west-1"
    )
    topic = sns_resource.create_topic(
        Name="test-topic"
    )

    os.environ["sns_topic_arn"] = topic.arn
    test_message = "test_message"
    message_id = publish_message_to_sns(test_message)

@mock_sns
@mock_sqs
# Assigning SQS to SNS topic & read msgs from the Queue
def test_read_from_sqs_queue():
    sns_resource = boto3.resource(
        "sns",
        region_name="eu-west-1"
    )
    topic = sns_resource.create_topic(
        Name="test-topic"
    )

    sqs_resource = boto3.resource(
        "sqs",
        region_name="eu-west-1",
    )

    queue = sqs_resource.create_queue(
        QueueName="test-queue",
    )
    os.environ["sqs_queue_url"] = queue.url
    os.environ["sns_topic_arn"] = topic.arn

    topic.subscribe(
        Protocol="sqs",
        Endpoint=queue.attributes["QueueArn"],
    )

    test_message = "test_message"
    message_id = publish_message_to_sns(test_message)

    messages = read_from_sqs_queue()
    message_body = json.loads(messages["Messages"][0]["Body"])