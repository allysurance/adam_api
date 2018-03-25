from django.shortcuts import render


from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
import sys
import base64

# Create your views here.
from api_ai import natural_text

import json 
import requests

from api.models import user








@csrf_exempt
def messeage(request):
	

	try:
		########################### EITHER YOU WILL HAVE YOUR POST REQUEST DATA IN REQUEST.BODY AND REQUEST.POST FROM WHERE YOU CAN PARSE it #######
		x = json.loads(request.body)
		sender_id = x['sender_id']
		user_details = user.objects.get_or_create(sender_id = sender_id)[0]
		headers = {'Content-type': 'application/json'}


		url = 'https://calc-uat.api-hdfclife.com/graphql'

		body = {
    "query": "query($data :Quote!){quote(data : $data)}",
      "variables": {
	"data": {
    "generatequoteReq": {
      "head": {
        "userid": "kuliza_ocp_001",
        "source": "OCP_ONLINE",
        "txnid": "FIN-81989"
      },
      "body": {
        "quotedtls": {
          "jnk": "N",
          "sumAssured": str(user_details.lumpsum),
          "term" : str(user_details.premium_term),
          "ppt": "20",
          "freq": "FREQ_1",
          "product": "C2P3DPER",
          "option": "3D Life",
          "pptOption": "REGULAR",
          "touchpoint": "OCP",
          "tobstatus": str(user_details.smoking_status),
          "lifeassured": {
            "dob": "06/01/1993",
            "gender": "GEN_F",
            "email": "test@tester.com",
            "mobno": "9999999999"
          }
        },
        "outputFmt": "JSON",
        "generateonlyflag": "Y",
        "agentcd": "00488538"
      }
    }
  }
}
}

		text = x['text']
		
		reply = natural_text(sender_id,text)
		q = requests.post(url , headers = headers , data=json.dumps(body))
		a  = json.loads(q.text)

		premium = a['data']['quote']['lifeassured'][0]['premium']

		response = {'reply' : reply , 'sender_id' : sender_id , 'premium' : premium , 'sumAssured' : user_details.lumpsum  }

		responseobj = json.dumps(response, indent = 4)
			
	except Exception as e:

		print e
		return HttpResponse("some error")
	return HttpResponse(responseobj,content_type = "application/json")