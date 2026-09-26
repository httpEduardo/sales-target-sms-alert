# Sales Target SMS Alert

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)

A reporting script that checks monthly Excel sales sheets for a target and sends an SMS when a seller exceeds the threshold.

## Setup

Install the dependencies and configure Twilio with fresh credentials in the environment:

```bash
pip install pandas openpyxl twilio
```

Set `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM_NUMBER`, and `TWILIO_TO_NUMBER`. Place the January through June workbooks (`janeiro.xlsx` through `junho.xlsx`) in the working directory, then run:

```bash
python sales_target_sms_alert.py
```

Use newly rotated Twilio credentials; credentials were previously committed in this repository's history.
