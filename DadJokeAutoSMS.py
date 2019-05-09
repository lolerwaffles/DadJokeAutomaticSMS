from twilio.rest import Client
import requests,json,schedule,time

def sendDadJoke():		
	url = "https://icanhazdadjoke.com/"

	headers = {
	    'accept': "application/json"
	    }

	response = requests.request("GET", url, headers=headers)

	message = json.loads(response.text)["joke"]

	#Twillo Account Info Here
	account_sid = ""
	auth_token  = ""

	client = Client(account_sid, auth_token)

	#Twillo phone number and SMS reciver number
	message = client.messages.create(
	    to="", 
	    from_="",
	    body=message)

	print(message.sid)

#Time to send SMS every day
schedule.every().day.at("12:00").do(sendDadJoke)

while True:
    schedule.run_pending()
    time.sleep(1)
    #print a reminder that this is running, just as a visual aid
    print("DadJokeAutoSender is running")
