##1.send a email

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@example.com"
password = "your_email_password"  # For Gmail, use an app password if 2FA is enabled

# Create message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email from Python"

# Email body content
body = "Hello, this is a test email sent from Python!"

# Attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# Set up the server and send the email
try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection

    # Login to the server
    server.login(sender_email, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the server connection
    server.quit()


#2.Send SMS message using python code
from twilio.rest import Client

# Your Twilio credentials
account_sid = 'your_account_sid'  # Found in your Twilio console
auth_token = 'your_auth_token'    # Found in your Twilio console

# Create a Twilio client
client = Client(account_sid, auth_token)

# Message details
from_phone_number = 'your_twilio_phone_number'  # Twilio phone number
to_phone_number = 'receiver_phone_number'       # Receiver's phone number
message_body = 'Hello, this is a test message from Python using Twilio!'

# Send the message
message = client.messages.create(
    body=message_body,
    from_=from_phone_number,
    to=to_phone_number
)

# Print message SID for confirmation
print(f"Message sent! SID: {message.sid}")

##4.Scrap top5 search results from google using the python code

from serpapi import GoogleSearch

# Your SerpApi API key
api_key = "your_serpapi_api_key"

# Define the search query
query = "Python programming tutorials"

# Set up the parameters for the search
params = {
    "q": query,  # The search query
    "api_key": api_key,  # Your API key
}

# Send the request to SerpApi
search = GoogleSearch(params)
results = search.get_dict()

# Extract the top 5 search results
top_5_results = results.get('organic_results', [])[:5]

# Print the top 5 results
for i, result in enumerate(top_5_results, 1):
    print(f"{i}. Title: {result['title']}")
    print(f"   Link: {result['link']}")
    print(f"   Snippet: {result.get('snippet', 'No snippet available')}\n")

##4.Find the current geo coordinates and location using the Python code 
import geocoder

# Get the current location based on IP address
g = geocoder.ip('me')

# Print out the geo coordinates and location details
print("Latitude:", g.latlng[0] if g.latlng else "Not available")
print("Longitude:", g.latlng[1] if g.latlng else "Not available")
print("City:", g.city)
print("State:", g.state)
print("Country:", g.country)
print("Address:", g.address)

#5.Convert text-to-audio using the python code

from gtts import gTTS
import os

text = "Hello, this is a text-to-speech conversion using Python."

language = 'en'


tts = gTTS(text=text, lang=language, slow=False)
tts.save("output.mp3")
os.system("start output.mp3")  


##6.Control volume of you laptop using python.

from pycaw.pycaw import AudioUtilities
from pycaw.constants import AUDIO_VOLUME_NOTIFICATION_TYPE

def set_volume(volume_level):
    # Get the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        AudioUtilities.IID_IAudioEndpointVolume,  # Volume control interface
        1,  # Activate the interface
        None
    )
    volume = interface.QueryInterface(AudioUtilities.IID_IAudioEndpointVolume)
    
    # Set volume level (from 0.0 to 1.0)
    volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)

def get_current_volume():
    # Get the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        AudioUtilities.IID_IAudioEndpointVolume,  # Volume control interface
        1,  # Activate the interface
        None
    )
    volume = interface.QueryInterface(AudioUtilities.IID_IAudioEndpointVolume)
    
    # Get current volume level as a percentage (0-100)
    current_volume = volume.GetMasterVolumeLevelScalar() * 100
    return current_volume

# Example usage:
set_volume(50)  # Set volume to 50%
current_volume = get_current_volume()
print(f"Current Volume: {current_volume}%")

##7.Connect to your mobile and send sms from your mobile messaging app using python.

from twilio.rest import Client

# Your Twilio account SID and Auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body="Hello, this is a test message sent from Python!",
    from_='+1234567890',  # Your Twilio number
    to='+0987654321'  # Recipient's phone number
)

# Print the message SID to confirm the message was sent
print(f"Message SID: {message.sid}")



##8.Create a function to Send bulk email using python.
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_bulk_email(sender_email, password, subject, body, recipient_list):
    """
    Function to send bulk email via SMTP.
    
    Args:
    sender_email (str): Sender's email address.
    password (str): Sender's email password (use App Password for Gmail if 2FA is enabled).
    subject (str): Subject of the email.
    body (str): Body content of the email.
    recipient_list (list): List of recipient email addresses.
    
    Returns:
    None
    """
    # Set up the SMTP server and port (Gmail example)
    smtp_server = "smtp.gmail.com"
    smtp_port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Establish connection to the email server
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, password)

            # Loop through the recipient list and send emails
            for recipient_email in recipient_list:
                # Create the email message
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = recipient_email
                message["Subject"] = subject

                # Attach the body content
                message.attach(MIMEText(body, "plain"))

                # Send the email
                server.sendmail(sender_email, recipient_email, message.as_string())
                print(f"Email sent to {recipient_email}")

    except Exception as e:
        print(f"Error: {e}")
    else:
        print("All emails sent successfully!")

# Example usage
sender_email = "your_email@gmail.com"
password = "your_email_password_or_app_password"  # Use app password if using Gmail 2FA
subject = "Your Subject Here"
body = "This is the email body. Customize as needed."
recipient_list = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]

send_bulk_email(sender_email, password, subject, body, recipient_list)

