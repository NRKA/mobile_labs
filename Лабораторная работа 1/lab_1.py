import pandas as pd

def tariff(number):
    # Reading csv file
    data = pd.read_csv('data.csv')
   
    # Copying data from csv file
    outgoing = data[data['msisdn_origin'] == 915783624].copy()
    incoming = data[data['msisdn_dest'] == 915783624].copy() 

    # Geting needed data
    out_calls = outgoing['call_duration'].values
    sms = outgoing['sms_number'].values
    in_calls = incoming['call_duration'].values
    
    # Calculating result
    out_calls_sum = sum([value * 2 for value in out_calls])
    in_calls_sum = 0
    sms_sum = sum([10*0 + (value-10)*1 if value>=10 else 0 for value in sms])
    result = out_calls_sum + in_calls_sum + sms_sum
    
    return result

result = tariff(915783624)

print(f"Total cost: {result}")