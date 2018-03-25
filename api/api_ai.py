"""
Documentation for this module:
This module has the full implementation and integration of api.ai handling events, queries and datapoints interception to send data. 
"""
import apiai as ai
import json 
import requests
import re
## This is the token you can obtain from your app's dashboard
# from messengerbot.models import user , status_code , status , type_of_service , mode_of_contact , type_of_shipment , type_of_collection , type_of_box , address , language , country , place , order
# import sys
# print sys.path

from api.models import user


  
def database_intercept(context,response ,sender_id):
    """
    This function intercepts the request from api.ai saves the data to the databse and then resumes the request so we store data of the users for booking orders and learning purposes . 
    """  
    user_details = user.objects.get_or_create(sender_id = sender_id)[0]
    
    if context == "smoker":
        # print "checking database intercept"  + str(response)
        print "this is the premium term is : "   + str(response['result']['contexts'][0]['parameters']['duration']['amount'])
        user_details.premium_term = response['result']['contexts'][0]['parameters']['duration']['amount']
        
        user_details.save()

    elif context == "lumpsum":
        # print "checking database intercept"  + str(response)
        print "this is the maturity term is : "   + str(response['result']['contexts'][0]['parameters']['duration']['amount'])
        
        user_details.maturity_term = response['result']['contexts'][0]['parameters']['duration']['amount']
        
        user_details.save()
    elif context == "premiumafford":
        print "this is smoking status"  + str(response['result']['resolvedQuery'])
        text = response['result']['resolvedQuery']

        if "yes" in text : 
            status = 'Y'

        else:
            status = 'N'    

        user_details.smoking_status = status
        
        user_details.save()

    elif context == "policies":
        print "this is lumpsum ammount"  + str(response['result']['contexts'][0]['parameters']['number'])
        
        user_details.lumpsum = response['result']['contexts'][0]['parameters']['number']
        
        user_details.save()

    elif context == "end":
        print "this is premium he can afford ammount"  + str(response['result']['contexts'][0]['parameters']['number'])   

        user_details.premium_afford = response['result']['contexts'][0]['parameters']['number']
        
        user_details.save()





def natural_text(sender_id,text):
    """
    This function handles all types of text queries makes a request to api.ai comes up with the reply with text messages and custom payloads which are parsed and framed according to facebook and then put in a dict and passed to views.py module
    """    
    CLIENT_ACCESS_TOKEN="c19e4faa73a94f8caa516266f6538805"
    
    headers = {"Authorization" : "Bearer c19e4faa73a94f8caa516266f6538805"  , "Content-Type": "application/json; charset=utf-8"}
    url  = "https://api.dialogflow.com/v1/query?v=20150910"
    data  = {
                "query": [
                    text 
                ],
                
                "timezone": "America/New_York",
                "lang": "en",
                "sessionId": sender_id 
            }
    data = json.dumps(data)
    response = requests.post(url, headers=headers , data = data )
    response = json.loads(response.text)
    print "this is response" + str(response)
    try:
        context = response['result']['contexts'][0]["name"]
        print "this is context"  + str(context)
        database_intercept(context , response, sender_id)
    except Exception as e:

                        print "this is exception"  + str(e)
                        pass  
   
    return response['result']['fulfillment']["messages"][0]["speech"]








