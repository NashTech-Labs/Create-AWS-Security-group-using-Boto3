## Create a AWS security Group using boto3.

#### A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. You can follow this [link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) to know more.

-------------

**Files:** 
```
      create_security_grp.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to create a security group.

        python3 create_security_grp.py
