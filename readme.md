# Recurring Cloudwatch Notification using lambda Function :

1) The recurring system is implemented using an Eventbriedge consumed by a lambda function. CloudWatch alarm, whenever fired, will send the event directly to the  SNS 

2) create an eventbriedge rule for those who check the alarm every 6 hours and trigger the lambda function and the lambda function checks the Cloudwatch alarm event in the "ALARM" state.When the message is processed and the event is sent to SNS.

# References: 

https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/cw-example-creating-alarms.html

https://mklein.io/2020/12/08/recurrent-alarms/

https://docs.aws.amazon.com/sns/latest/dg/sns-publishing.html

https://aws.amazon.com/blogs/mt/customize-amazon-cloudwatch-alarm-notifications-to-your-local-time-zone-part-1/



