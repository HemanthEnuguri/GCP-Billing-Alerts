import base64
import json
import os
import requests

def slack_billing_alert(event, context):
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']

    try:
        message_data = base64.b64decode(event['data']).decode('utf-8')
        billing_alert = json.loads(message_data)

        cost_amount = billing_alert.get('costAmount', 'N/A')
        budget_name = billing_alert.get('budgetDisplayName', 'Unknown')
        threshold = billing_alert.get('alertThresholdExceeded', 'N/A')

        slack_message = {
            "text": f"💰 *GCP Billing Alert*\n• *Budget*: `{budget_name}`\n• *Cost*: `${cost_amount}`\n• *Threshold crossed*: `{float(threshold) * 100}%`"
        }

        response = requests.post(slack_webhook_url, json=slack_message)
        response.raise_for_status()
    except Exception as e:
        print(f"Error: {e}")
        raise
