# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC2b2ff16bffadb44d431da26113c19cf6"
auth_token = "2c8c0992334dfbc921c1298f46beb2cf"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+13203857028",
  to="+351968195476"
)
print(message.sid)