import matplotlib.pyplot as plt 
import datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

file_path = '/home/ec2-user/TickerBotProd/TickerPriceBot/image.jpg'

current_date = str(datetime.datetime.now()).split()[0]

# Graph Formating
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 10}

plt.rc('font', **font)


def create_graph(json_data, ticker, frequency):

    plt.clf()

    time_axis = []
    price_axis = []

    for timestamp in json_data:
        if timestamp.split()[0] == current_date:
            time_label = timestamp.split()[1].split(':')
            time_formated = float(time_label[0] + '.' + time_label[1])

            time_axis.append(time_formated)
            price_axis.append(float(json_data[timestamp]['4. close']))

    plt.plot(time_axis, price_axis)

    pp.pprint(json_data)

    plt.tick_params(axis='x', rotation=-90)
    plt.locator_params(axis='x', nbins='1')

    plt.title(f'{ticker} ({frequency})')
    plt.xlabel('time')
    plt.ylabel('price ($)')
    plt.savefig('image.jpg')

    return file_path