from flask import Flask, jsonify, abort, request, make_response, url_for, flash
from flask import render_template, redirect, session
import requests

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from getdynamo import ShareF_user


application = Flask(__name__)
application.secret_key = "super secret key"

@application.route('/', methods = ['GET', 'POST'])
def loginPage():
	if request.method == 'POST':
		result = request.form.to_dict()
		#This is User Input Data in forms of dictionary.
		
		ke = Key("userId").eq(result['inputEmail'].lower())
		#Change user Input Data to lower Case and save it as Key Condition Expression
		#Key Condition Expression will be Used when querying the data

		try:
			response = ShareF_user.query(
					KeyConditionExpression = ke, Limit = 1
				)
                        #print(response)
			#Query matching data from the data base by using Key Condition Expression

			if response['Items'][0]['Password'] == result['inputPassword']:
				#Check if queried data has same password as User Input data
				
				session['currentUser'] = response['Items'][0]['userId']
				#session['UserStatus'] = response['Items'][0]['Status']
				#Save current user to session. 
				#In other pages, session will be checked to see if user is logged in or not.

				#If everything matches up, redirect the page to /notification
				
                                print("success")
                                return redirect('/frontPage')
			else:
				flash("Wrong Password")
				#Flash is Flask provided method that is similar to alert() method in Javascript
				#Flash provides fast and easy way to notify the users

				return redirect('/')
		except Exception as err:
			flash("No such ID Found")
                        print("err", err)
			return redirect('/')
	else:
		#Render_templates takes html and feed the data from python script. 
		#provided by Flask
		#render_template(<htmlfile>, <datatoPushToHtml>)
		return render_template('login.html')

#front page after login
@application.route('/frontPage', methods = ['GET', 'POST'])
def mainPage():

    if request.method == 'POST':
        print("method is post")
    else:
        return render_template('selectScreen.html')

#page for buyers to search the food
@application.route('/buyer', methods = ['GET', 'POST'])
def buyerPage():

    if request.method == 'POST':
        print("method is post")
    else:
        return render_template('buyer.html')

#page for seller to upload the food
@application.route('/seller', methods = ['GET', 'POST'])
def sellerPage():

    if request.method == 'POST':
        print("method is post")
    else:
        return render_template('seller.html')

#page for seller to upload the food
@application.route('/sellerList2', methods = ['GET', 'POST'])
def sellerPage_afterUpload():

    if request.method == 'POST':
        print("method is post")
    else:
        return render_template('sellerList.html')

#page for seller to upload the food
@application.route('/sellerList', methods = ['GET', 'POST'])
def sellerPage():

    if request.method == 'POST':
        print("method is post")
    else:
        return render_template('sellerList_before.html')

if __name__ == '__main__':
	application.run(host = '0.0.0.0', port = 80)
