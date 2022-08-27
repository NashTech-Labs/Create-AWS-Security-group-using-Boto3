# # # import logging for get the logs in  execution
# import logging
# # import the boto3 which will use to interact  with the aws
# import boto3
# from botocore.exceptions import ClientError

# REGION = input("Please enter the REGION")
# # this is configuration for the logs 

# logger_for = logging.getLogger()
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s: %(levelname)s: %(message)s')

# client = boto3.resource("ec2", region_name=REGION)


# def create_grp(description, grpname, id):
#     try:
#         response = client.create_vpc(Description=description,
#                                                       GroupName=grpname,
#                                                       VpcId=id,
#                                                       TagSpecifications=[{
#                                                           'ResourceType':
#                                                           'security-group',
#                                                           'Tags': [{
#                                                               'Key':'SG',
#                                                               'Value':grpname
#                                                           }]
#                                                       }])

#     except ClientError:
#         logger_for.exception('Oops sorry, Your security grp can not be create.')
#         raise
#     else:
#         return response


# if __name__ == '__main__':
#     DES = input("Enter the description")
#     GRPNAME = input("enter the GROUP name")
#     ID = input('Enter your VPC ID')
#     logger_for.info(f'Please wait, Creating a security group...')
#     security_grp = create_grp(DES, GRPNAME, ID)
#     logger_for.info(f'Wow!! Your Security group created with ID: {security_grp.id}')



# # import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError

REGION = input("Please enter the REGION: ")
Tag=input("Enter the tag name: ")
Tag_Value=input("Enter the tag value: ")
# this is configuration for the logs 
logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_subnet = boto3.resource("ec2", region_name=REGION)


def security_group(description, grpname, id):
    try:
        res = vpc_subnet.create_security_group(Description=description,
                                                      GroupName=grpname,
                                                      VpcId=id,
                                                      TagSpecifications=[{
                                                          'ResourceType':
                                                          'security-group',
                                                          'Tags': [{
                                                              'Key':Tag,
                                                              'Value':Tag_Value
                                                          }]
                                                      }])

    except ClientError:
        logger_for.exception('Could not create a security group.')
        raise
    else:
        return res


if __name__ == '__main__':
    DESCRIPTION = input("Enter the description: ")
    GROUPNAME = input("enter the GROUP name: ")
    VPC_ID = input('Enter your VPC ID: ')
    logger_for.info(f'Please wait, Creating a security group...')
    security_group = security_group(DESCRIPTION, GROUPNAME, VPC_ID)
    logger_for.info(f'Wow!! Your Security group created with ID: {security_group.id}')