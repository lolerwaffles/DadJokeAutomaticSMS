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


schedule.every().day.at("12:00").do(sendDadJoke)

while True:
    schedule.run_pending()
    time.sleep(1)
    print("DadJokeAutoSender is running")