import boto3
session = boto3.Session(profile_name='pythonAutomation1')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')

# to scale down
import boto3
session = boto3.Session(profile_name='pythonAutomation1')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Notifon Example', PolicyName='Scale Down')
