import json
import os
import datetime
import boto3
import logging
import time
import urllib
import re
import tempfile
import importlib

cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

def lambda_handler(event, context):
    class AlarmDetails:
     def __init__(alarm,name,arn,stateValue,description,stateReason,timestamp,metricname,namespace):
        print("ctr")
        alarm.Name = name
        alarm.Arn=arn
        alarm.Description=description
        alarm.StateChange=stateValue
        alarm.StateChangeReason=stateReason
        alarm.StateUpdatedTimestamp=timestamp
        alarm.MetricName=metricname
        alarm.Namespace=namespace
        
    alarmslist = []    
    paginator = cloudwatch.get_paginator('describe_alarms')
    for response in paginator.paginate(StateValue='ALARM'):
       response = json.loads(
                json.dumps(
                    response['MetricAlarms'], default=datetime_converter
                )
            )
       print(response)        
       for message in response:
          
           alarmDetails = AlarmDetails(message['AlarmName'] , message['AlarmArn'] ,message['StateValue'],message['AlarmDescription'],message['StateReason'],message['StateUpdatedTimestamp'],message['MetricName'],message['Namespace'])          
          
           alarmslist.append(alarmDetails)
           print(message)
   
   
    jsonStr= ""
    for alarm in alarmslist:
      jsonStr += json.dumps(alarm.__dict__,indent=3) +'\n'+'\n'
      
    print(jsonStr)        
    sns.publish (
      TargetArn = "arn:aws:sns:ap-south-1:149736408060:CloudWatch_Alarms_Topic",
      Subject = "Cloudwatch Alarm In 'ALARM' State",
      Message = jsonStr
      )
def datetime_converter(field):
    #helper function to perform JSON dump on object containing datetime
    if isinstance(field, datetime.datetime):
        return field.__str__