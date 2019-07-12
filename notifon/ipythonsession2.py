# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation1')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
  
get_ipython().run_line_magic('ls' '-l python_automation_key.pem')
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-09ff6a63071e9b2b1')
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img.name
ec2_ap2 = ec2_apse2.Img('ami-09ff6a63071e9b2b1')
img_apse2 = ec2_apse2.Img('ami-09ff6a63071e9b2b1')
img_apse2 = ec2_apse2.Image('ami-09ff6a63071e9b2b1')
img_apse2.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-09ff6a63071e9b2b1')
img_apse2.name
img = ec2.Image('ami-0d8f6eb4f641ef691')
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-0d8f6eb4f641ef691')
img_apse2.name
img.name
ami_name = 'amzn2-ami-hvm-2.0.20190618-x86_64-gp2'
filets = [{'Name': 'name', 'Values': [ami_name]}]
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters = filters))
img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-0336e6bdbb4d16192')
inst = instances[0]
inst.terminate()
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.wait_until_running()
inst.wait_until_running()
inst.wait_until_running()
inst.reload()
inst.public_dns_name
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'TopPort': 22, 'IpProtocal': 'TCP' , 'IpRanges': ['CidrIp': '172.31.85.64/00']}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'TopPort': 22, 'IpProtocal': 'TCP' , 'IpRanges': [{'CidrIp': '172.31.85.64/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'TopPort': 22, 'IpProtocal': 'TCP' , 'IpRanges': [{'CidrIp': '172.31.85.64/00'}]}])
