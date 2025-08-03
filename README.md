# GCP-Billing-Alerts
This gives a complete idea about setting up a Budget alert.
# Configure GCP Billing Alerts to Slack via Pub/Sub & Cloud Function

This project sends GCP budget alerts to a Slack channel using Pub/Sub and Cloud Functions.

---

## 📊 Step-by-Step Workflow

### 1. Billing Alert Triggered
- A GCP Budget alert threshold is reached (e.g., 50%, 75%, 100% of budget).
- GCP Billing sends a message to the configured **Pub/Sub topic**.

### 2. Pub/Sub Topic (`billing-alerts-topic`)
- Receives the billing alert message in **JSON format**.
- Holds the message until a subscriber consumes it.

### 3. Cloud Function
- **Auto-triggered** when a new message arrives in the topic.
- The function:
  - Parses the alert message.
  - Extracts details like:
    - `budgetDisplayName`
    - `costAmount`
    - `alertThresholdExceeded`
  - Constructs a human-readable Slack message.
  - Sends it via HTTP POST to the **Slack Webhook URL**.

### 4. Slack Incoming Webhook
- Receives the POST request from the Cloud Function.
- Posts the message in your specified **Slack channel**.

---

## 🖇️ Architecture Diagram

[GCP Billing Alert to Slack](./flowchart.pdf)

---

## Outcome
- Fully serverless and scalable.
- Real-time budget alerts in your Slack workspace.
- Uses only native GCP services (Pub/Sub, Cloud Functions).
