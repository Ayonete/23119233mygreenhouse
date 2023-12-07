import boto3
from decimal import Decimal

def add_item_to_dynamodb(name, description, moisture, temperature):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('23119233-greenhouse-reco')
    response = table.put_item(
      Item={
            'name': name,
            'description': description,
            'moisture': Decimal(str(moisture)),  # Convert float to Decimal
            'temperature': Decimal(str(temperature))  # Convert float to Decimal
        }
    )
    return response

# def publish_to_sns(subject, message):
#     sns_client = boto3.client('sns')
#     response = sns_client.publish(
#         TopicArn='arn:aws:sns:us-west-2:250738637992:23119233-Greenhous-notifications',
#         Message='Hey, Your Plant might be at risk. Che',
#         Subject='New Crop Alert'
#     )
#     return response

class CropHealth:
    def __init__(self, moisture, temperature):
        self.moisture = moisture
        self.temperature = temperature

    def analyse_health(self):
        if self.moisture < 30:
            return "Health Risk: Low Moisture"
        elif self.temperature > 35:
            return "Health Risk: High Temperature"
        else:
            return "Healthy"
            
    def publish_to_sns(self, subject, message):
        sns_client = boto3.client('sns')
        TopicArn='arn:aws:sns:eu-west-1:250738637992:23119233-GREENHOUSE'
        response = sns_client.publish(
            TopicArn=TopicArn,
            Subject = subject,
            Message=message
        )
        return response
