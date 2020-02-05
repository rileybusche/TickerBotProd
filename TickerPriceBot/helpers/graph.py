import matplotlib.pyplot as plt 
import datetime

file_path = '/home/ec2-user/TickerBotProd/TickerPriceBot/image.jpg'

current_date = str(datetime.datetime.now()).split()[0]


def create_graph(json_data, ticker):

    time_axis = []
    price_axis = []

    for timestamp in json_data:
        if timestamp.split()[0] == current_date:
            time_label = timestamp.split()[1].split(':')
            time_formated = time_label[0] + ':' + time_label[1]
            time_axis.append(time_formated)
            price_axis.append(json_data[timestamp]['4. close])

            print(timestamp)
            print(time_formated)
            print("**********")

    plt.plot(time_axis, price_axis)

    plt.xlabel('time')
    plt.ylabel('price ($)')
    plt.savefig('image.jpg')

    return file_path