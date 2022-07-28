# # import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError

AWS_REGION = input("Please enter the AWS_REGION")
# this is configuration for the logs 

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_resource = boto3.resource("ec2", region_name=AWS_REGION)


def create_security_group(description, groupname, vpc_id):
    try:
        response = vpc_resource.create_security_group(Description=description,
                                                      GroupName=groupname,
                                                      VpcId=vpc_id,
                                                      TagSpecifications=[{
                                                          'ResourceType':
                                                          'security-group',
                                                          'Tags': [{
                                                              'Key':'SG',
                                                              'Value':groupname
                                                          }]
                                                      }])

    except ClientError:
        logger.exception('Could not create a security group.')
        raise
    else:
        return response


if __name__ == '__main__':
    DESCRIPTION = 'Hey, Security group created for Techhub'
    GROUPNAME = 'Knoldus_Techhub_template'
    VPC_ID = input('Enter your VPC ID')
    logger.info(f'Please wait, Creating a security group...')
    security_group = create_security_group(DESCRIPTION, GROUPNAME, VPC_ID)
    logger.info(f'Wow!! Your Security group created with ID: {security_group.id}')