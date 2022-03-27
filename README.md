![Image](https://github.com/SheplX/SNS-SQS-AWS/blob/main/SNS%20-%20SQS.png)

# SNS and SQS (AWS)
- A simple tutorial to set up SQS queue to subscribe to SNS Topic using python.
- Before we start, if u are interested to know more about SQS & SNS, [this](https://www.beabetterdev.com/2021/08/08/aws-sns-vs-sqs-whats-the-difference/) is a cool guild for u.
- In the handler file, u will find 2 functions, the first is for publishing msgs to SNS topic, this function should have some basic metadata like a client and a topic ARN.
- After subscribing SQS Queue to the SNS topic, we will need another function for reading the received msgs to the Queue, so it's the second function there.
- In the tester file, we will just be testing those functions above, the first one will publish the msgs to the SNS topic, the sec one will just subscribe SQS Queue to the SNS topic for reading the msgs from the Queue.
# Dependencies:
- boto3 > AWS SDK for Python (Boto3) to create, configure, and manage AWS services.
- moto > A library that allows you to easily mock out tests based on AWS infrastructure (so u don't need a real AWS service, just use moto and generate decorators for any resource u like !).
# Installation:
- for boto3, if u are using vscode, u need to install python Interpreter first coz u will need pip tool to be able to install boto3:
```pip install boto3```
- for moto, u will need python (pip) too:
```pip install moto```
- Important note, sometimes pip only won't work with u, You may have mixed up Python and pip versions on your machine (this happened with me on win 10). In this case, to install boto3 for Python 3, you may want to try python3 -m or pip3 before every command, and u should be ready to go!
