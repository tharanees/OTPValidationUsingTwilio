from flask import Flask,render_template,request,redirect
import os
import random
from twilio.rest import Client

OTP = 0
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("login.html")

@app.route('/getOTP', methods=["GET","POST"])
def getOTP():
	number= "+447759500535"
	#FILL HERE THE PHONE NUMBER YOU WANT TO SEND SMS TO
	val=getOTPApi(number)
	if (val):
		return render_template("otp.html")

def generateOTP():
	return (random.randrange(100000, 999999))


def getOTPApi(number):
	global OTP
	account_sid = #FILL HERE YOUR TWILIO ACCOUNT SID
	auth_token = #FILL HERE YOUR TWILIO ACCOUNT AUTH TOKEN
	client = Client(account_sid,auth_token)
	OTP = generateOTP()
	body = "YOUR OTP IS "+str(OTP)
	message = client.messages.create(
							  from_= #FILL your Twilio phone number,
							  body = body,
							  to = number
						)
	if message.sid:
		return True
	else:
		return False



@app.route("/validateOTP", methods=["GET","POST"])
def validate():
	#if OTP entered is matched then return success else re-send a new OTP
	otp = request.form["otp"]
	if str(otp) == str(OTP):
		return("success")
	else:
		return redirect("/getOTP")

	
if __name__ == '__main__':
	app.run()