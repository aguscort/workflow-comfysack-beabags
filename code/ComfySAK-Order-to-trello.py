#PARAMETERS
input_data = {
    'prod': '',
    'quant': ''}
# /PARAMETERS 


list_names = list(input['prod'].split(','))
list_quant = list(input['quant'].split(','))
j = 0
final_text = ''

for i in list_names:
    final_text += '**Product:** '+ i +'\n**Quantity:** '+ list_quant[j] + '\n\n'
    j += 1

return {'final_text_output': final_text}
