import os
import requests

def send_test_slack_message():
    slack_webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not slack_webhook_url:
        print("Please set the SLACK_WEBHOOK_URL environment variable.")
        return

    # Sample billing alert data
    billing_alert = {
        "costAmount": 100,
        "budgetDisplayName": "You have reached set threshold Budget",
        "alertThresholdExceeded": 0.5
    }

    slack_message = {
        "text": (
            f"💰 *GCP Billing Alert*\n"
            f"• *Budget*: `{billing_alert['budgetDisplayName']}`\n"
            f"• *Cost*: `${billing_alert['costAmount']}`\n"
            f"• *Threshold crossed*: `{billing_alert['alertThresholdExceeded'] * 100}%`"
        )
    }

    try:
        response = requests.post(slack_webhook_url, json=slack_message)
        response.raise_for_status()
        print("Slack billing alert message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Slack message: {e}")

if __name__ == "__main__":
    send_test_slack_message()
