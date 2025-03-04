# Fincode API Server

A comprehensive data analytics and reporting platform built with Flask.

## Deployment to Heroku

### Prerequisites

- A Heroku account
- Heroku CLI installed
- Git installed

### Steps to Deploy

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create a Heroku App**
   ```bash
   heroku create your-app-name
   ```

3. **Set Environment Variables**
   ```bash
   heroku config:set SMTP_SERVER=smtp.gmail.com
   heroku config:set SMTP_PORT=587
   heroku config:set SENDER_EMAIL=your-email@gmail.com
   heroku config:set SENDER_PASSWORD=your-password
   heroku config:set OPENAI_API_KEY=your-openai-key
   heroku config:set TWILIO_ACCOUNT_SID=your-twilio-sid
   heroku config:set TWILIO_AUTH_TOKEN=your-twilio-token
   heroku config:set TWILIO_WHATSAPP_NUMBER=your-twilio-number
   heroku config:set BASE_URL=https://your-app-name.herokuapp.com
   heroku config:set ENVIRONMENT=production
   ```

4. **Push to Heroku**
   ```bash
   git push heroku master
   ```

5. **Open the App**
   ```bash
   heroku open
   ```

## Troubleshooting

If you encounter any issues with the deployment, check the logs:
```bash
heroku logs --tail
```

## Local Development

To run the app locally:
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`

The app will be available at http://localhost:8501.

## Features

- Tableau integration
- Report scheduling
- Data visualization
- User management
- Email notifications
- WhatsApp notifications (via Twilio) 