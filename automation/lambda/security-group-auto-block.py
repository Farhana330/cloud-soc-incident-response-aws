import boto3
import os
import json

# Connect to EC2 service

ec2 = boto3.client('ec2')

SECURITY_GROUP_ID = os.environ['SECURITY_GROUP_ID']
PORT = int(os.environ.get('PORT', '22'))
CIDR_TO_REMOVE = os.environ['CIDR_TO_REMOVE']

# Main Lambda function

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    try:
        # Remove insecure SSH rule (block attacker IP)
        response = ec2.revoke_security_group_ingress(
            GroupId=SECURITY_GROUP_ID,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': PORT,
                    'ToPort': PORT,
                    'IpRanges': [
                        {'CidrIp': CIDR_TO_REMOVE}
                    ]
                }
            ]
        )

        print(f"Removed access for {CIDR_TO_REMOVE} on port {PORT} from {SECURITY_GROUP_ID}")

        return {
            'statusCode': 200,
            'body': f'Access removed for {CIDR_TO_REMOVE} on port {PORT}'
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }