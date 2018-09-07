# import all the libraries we will be using
import pandas as pd
from datetime import datetime
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client



def getReply(message):
    
    answer = ""
    if message in  ['1', '2', '3', '4', '5']:
        answer = 'Thank you for banking with us. Your satisfaction is paramount to us'

    else:
        message = message.lower().strip()
        
        if message == 'yes':
            answer = 'Thank you Mr. XXXXXX. Please call +01-27-34-86 to proceed with your offer.\nKindly rate our services on a scale of 1-5\n'
                
        elif message == 'no':
            answer = "Thank you Mr. XXXXXX. Please reply to our support via - +18575986012 with offers/services you would prefer in the format\ne.g CAR LOAN or MORTGAGE"

        else:
            answer = 'Thank you Mr. xxxxxx. Our Customer Service would be in touch with you shortly.\nDo Have a nice Day.\nKindly rate our services on a scale of 1-5'
    
    return answer





def write_logs(cid,cph,off,crt,cr,rep):
        f = open('rm_logs.txt', 'a+')
        logs = '\n'+cid+','+cph+','+off+','+crt+','+cr+','+rep
        for i in range(1):
            f.write(logs)

        f.close()



# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)
    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def sms():
    customer_id = '12345'
    customer_phone = '+18575986012'
    offer = 'ZERO - INTEREST LOANS'
    resp_time = str(datetime.now())
    
    # Get the text in the message sent
    message_body = request.form['Body']
    cust_resp = message_body
    # Create a Twilio response object to be able to send a reply back (as per         # Twilio docs)
    resp = MessagingResponse()
    
    # Send the message body to the getReply message, where 
    # we will query the String and formulate a response
    replyText = getReply(message_body)
    Reply = replyText
    # Text back our response!
    resp.message(replyText)
    write_logs(customer_id, customer_phone, offer, resp_time, cust_resp, Reply)
    # dm = pd.DataFrame(messages.sid)
    # dm.to_csv('messages.csv')
    return str(resp)
    

    # pd.DataFrame(messages.to_csv('messages.csv')
# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()