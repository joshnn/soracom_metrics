# How to setup Jupyter Notebook

Take a firebase credential JSON from Firebase environment and place it in the same folder. The JSON typically contains the following lines:

```
  "type": "service_account",
  "project_id": "YOUR_PROJECT_ID",
  "private_key_id": "YOUR_PRIVATE_KEY_ID",
  "private_key": "YOUR_PRIVATE_KEY",
  "client_email": "YOUR_CLIENT_EMAIL",
  "client_id": "YOUR_CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/YOUR_SERVICE_ACCOUNT_URL"
```

Create an .env file that contains the following lines:

```
DATABASE_URL=YOUR_FIREBASE_REALTIME_DB_URL
CERTIFICATE_JSON=YOUR_FIREBASE_CREDENTIAL_JSON
TARGET_WEBSITE=www.google.com
```

Then open realtime_analytics.ipynb with viewer such as VS code.