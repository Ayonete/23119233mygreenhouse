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
            return "Health Risk: Low Moisture. Increase watering frequency"
        elif self.temperature > 35:
            return "Health Risk: High Temperature. Consider shading this crop"
        else:
            return "Healthy. Continue current routine"
            
    def publish_to_sns(self, subject, message):
        sns_client = boto3.client('sns')
        TopicArn='arn:aws:sns:eu-west-1:250738637992:23119233-GREENHOUSE'
        response = sns_client.publish(
            TopicArn=TopicArn,
            Subject = subject,
            Message=message
        )
        return response


class PlantDiagnosis:
        
    def diagnose(self, discoloration, deformed, region_affected):
        # Check for nitrogen deficiency
        if discoloration == "yellow patches" and deformed == "no" and region_affected == "all over":
            return "Your plant has a nitrogen deficiency."

        # Check for potassium deficiency
        elif discoloration == "yellow patches" and deformed == "no" and region_affected == "old leaves":
            return "Your plant has a potassium deficiency."

        # Check for magnesium deficiency
        elif discoloration == "yellow patches" and deformed == "no" and region_affected == "young leaves":
            return "Your plant has a magnesium deficiency."

        # Check for sulfur deficiency
        elif discoloration == "no discoloration" and deformed == "yes" and region_affected == "young leaves":
            return "Your plant has a sulfur deficiency."

        # Default case if none of the conditions are met
        else:
            return "No specific deficiency detected based on the given parameters."

    def publish_to_sns(self, subject, message):
        sns_client = boto3.client('sns')
        TopicArn='arn:aws:sns:eu-west-1:250738637992:23119233-GREENHOUSE'
        response = sns_client.publish(
            TopicArn=TopicArn,
            Subject = subject,
            Message=message
        )
        return response

