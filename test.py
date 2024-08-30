from twilio.rest import Client

account_sid = 'AC9785235242abb5dac0e80e1eea0fd994'
auth_token = '2b6123aeb8127de59c82e4d6e248d68c'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+201119394466'
)

print(message.sid)
