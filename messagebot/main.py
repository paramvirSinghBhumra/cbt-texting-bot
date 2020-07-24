from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    #TODO: add code here for webhook logic
    user_incoming_mesg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    mesg = response.message()
    mesg.body("this is the response")
    # mesg.media("https://www.computersciencedegreehub.com/wp-content/uploads/2016/02/what-is-coding-1024x683.jpg")

    return str(response)




if __name__ == "__main__":
    app.run()
