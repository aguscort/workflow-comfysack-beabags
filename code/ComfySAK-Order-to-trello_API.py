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

order_details_str = ''
try:
    order_id = input_data['order_id']    
    url = 'https://' + input_data['shopname'] + '.myshopify.com/admin/orders/' + input_data['order_id'] + '.json'
    req = requests.get(url, auth=(input_data['apikey'], input_data['password'])).json()

    for i in range(len(req['order']['line_items'])):
        title = str(req['order']['line_items'][i]['name']) 
        quantity = str(req['order']['line_items'][i]['quantity']) 
        #price = str(req['order']['line_items'][i]['price']) 
        order_details_str += '**Name:** ' + title + '\n**Qty:** ' + quantity + '\n\n'
except:    
    order_details_str = 'There was an error retrerving the data lines from this Order, please check.'
    order_id = None    

return {'orderID': order_id, 'orderDetails':  order_details_str }                
