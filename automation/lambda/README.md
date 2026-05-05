\# Lambda Automated Response



This Lambda function is used to automatically block malicious IP addresses or remove insecure SSH access from an EC2 security group.



\## How it works

\- Triggered by CloudWatch Alarm

\- Identifies attacker IP

\- Removes SSH access rule



\## Environment Variables

\- SECURITY\_GROUP\_ID

\- PORT

\- CIDR\_TO\_REMOVE

