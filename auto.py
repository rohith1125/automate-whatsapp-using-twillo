from twilio.rest import Client 
 
account_sid = '' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 def send_msg():
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='The message you want to send',      
                              to='whatsapp:target phone number' 
                          ) 
 
print(message.sid)