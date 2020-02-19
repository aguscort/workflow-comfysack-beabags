from datetime import datetime, timedelta
import json
import requests

#PARAMETERS
input_data = {
        'order_id': '',
        'password': '',
        'apikey': '',
        'shopname': ''}
# /PARAMETERS 

total_paid = 0
reference = ""
try:
    order_id = input_data['order_id']    
    url = 'https://' + input_data['shopname'] + '.myshopify.com/admin/orders/' + input_data['order_id'] + '/transactions.json'
    req = requests.get(url, auth=(input_data['apikey'], input_data['password'])).json()

    for i in range(len(req['transactions'])):
        print(req['transactions'][i])
        kind = str(req['transactions'][i]['kind']) 
        status = str(req['transactions'][i]['status'])
        amount = str(req['transactions'][i]['amount']) 
        if kind == "sale" and status == "success":
            total_paid += float(amount)
            try:
                reference = req['transactions'][i]['receipt']['x_reference']
            except: 
                pass
        elif kind == "refund" and status == "success": 
            total_paid -= float(amount)   
except:            
        pass
    
return {'total_amount': total_paid, 'reference' : reference}