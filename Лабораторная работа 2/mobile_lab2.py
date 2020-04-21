#You should have these modules, otherwise program won't work.
#To install these modules, you should type these commands in terminal: pip install pandas; pip install matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# My data
my_ip = '217.15.20.194'
price = 0.5

def start():
    # Getting started
    text = []
    with open('nfcapd.txt', 'r', encoding='utf_8') as f:
        text = f.readlines()

    spaces = [' ' * n for n in range(20, 2, -1)]

    for i in range(len(text)):
        text[i] = text[i].replace('->', '')

    words = ['INVALID', 'XEvent', 'Ignore']
    for word in words:
        for i in range(len(text)):
            text[i] = text[i].replace(word, ' ' + word + ' ')

    for space in spaces:
        for i in range(len(text)):
            text[i] = text[i].replace(space, '  ')

    for i in range(len(text)):
        text[i] = text[i].replace('  ', ',')

    with open('new_nfcapd.txt', 'w', encoding='utf_8') as f:
        f.writelines(text)

    # Getting needed data
    df = pd.read_csv('new_nfcapd.txt', sep=',')

    total_traffic = df[(df['Src IP Addr:Port'].str.contains(my_ip)) | (
        df['Dst IP Addr:Port'].str.contains(my_ip))].reset_index(drop=True).copy()
    total_traffic['Date first seen'] = total_traffic['Date first seen'].apply(pd.to_datetime).copy()
    total_traffic['In Byte'] = total_traffic['In Byte'].apply(
        lambda x: float(x) if x[-1] != 'M' else float(x[:-1]) * 1024 * 1024).copy()
    result = sum(total_traffic['In Byte'].values)
    result = round((result / 1024), 2)
    print(f'Total size: {result}kb')

    # Showing graphics
    total_traffic['Date first seen'] = total_traffic['Date first seen'].apply(lambda x: str(x)[:str(x).find('.')]).copy()
    total_traffic['Date first seen'] = total_traffic['Date first seen'].apply(pd.to_datetime).copy()
    total_traffic['Date first seen'] = total_traffic['Date first seen'].apply(lambda x: str(x)[:-3]).copy()
    total_traffic['Date first seen'] = total_traffic['Date first seen'].apply(pd.to_datetime).copy()

    traffic_after_group = (total_traffic.groupby('Date first seen').aggregate(sum)).copy()

    plt.figure(figsize=(15, 100))
    plt.title('Minutes')
    plt.plot(traffic_after_group.index, traffic_after_group['In Byte'].values)

    plt.show()

    # Calculating
    total_price = result * price
    total_price = round(total_price, 2)

    print(f'Total cost: {total_price}')

start()