#PARAMETERS
input_data = {
'prod': '',
'quant': '',
'': '0,
'': ''}
# /PARAMETERS 
from datetime import datetime, timedelta
import json
import requests

total_amount = 0
try:
        order_id = input_data['order_id']    
        url = 'https://' + input_data['shopname'] + '.myshopify.com/admin/orders/' + input_data['order_id'] + '/transactions.json'
        req = requests.get(url, auth=(input_data['apikey'], input_data['password'])).json()

        for i in range(len(req['transactions'])):
                kind = str(req['transactions'][i]['kind']) 
                print(kind)
                status = str(req['transactions'][i]['status']) 
                print(status)
                amount = str(req['transactions'][i]['amount']) 
                if kind == "sale" and status == "success":
                        total_paid += float(amount)
                elif  kind == "refund" and status == "success": 
                total_paid -= float(amount)   
except:
        pass

return {'total_amount': total_amount}
