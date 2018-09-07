# Function to formulate a response based on message input.
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc554c6bb13cac1e96af70982f93e1779"
# Your Auth Token from twilio.com/console
auth_token  = "264a946d54cbcfd3ff314d1c428905d0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2348165251963", 
    from_="+18575986012",
    body="Hello Mr. xxxxxx. We appreciate your unrelentless patronage with us.\nWe have an offer we won't like you to miss out on.\nWe are now giving ZERO - INTEREST LOANS\nif you are interested text YES to +18575986012 otherwise text NO")

print(message.sid)

