import boto3
import click

session = boto3.Session(profile_name='pythonAutomation1')
s3 = session.resource('s3')

@click.group()
def cli():
    "webotron deploys websites to aws"
    pass

@cli.command('list_buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()
