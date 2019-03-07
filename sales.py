import random
import decimal
import datetime
from dateutil.relativedelta import relativedelta


def gen_sale(store_no, store_id, date):
    # double christmas eve, every other
    seasonality = 1

    if date[5:len(date) - 1] == '12-24':
        seasonality = 2
    elif int(date[5:7]) == 12:
        seasonality = 1.75
    elif int(date[5:7]) == 11:
        seasonality = 1.5
    elif int(date[5:7]) == 10:
        seasonality = 1.2

    amount = '{0:.2f}'.format(random.random() * 20000 * seasonality)

    try:
        sale = {
            'amount_1': amount,
            'amount_2': None,  # illustration of multiple different sales numbers for a store
            'sales_ticks': [],  # Sales by the minute
            'store_no': store_no,
            'date': date,
            'store_id': store_id
        }
    except AttributeError:
        pass

    return sale


def gen_sales(store):
    sale_records = []

    sd = [int(x) for x in store['open_date'].split('-')]
    start_date = datetime.date(year=sd[0], month=sd[1], day=sd[2])

    if store['close_date'] is None:
        close_date = datetime.date.today().isoformat()
    else:
        close_date = store['close_date']

    ed = [int(x) for x in close_date.split('-')]
    end_date = datetime.date(year=ed[0], month=ed[1], day=ed[2])

    while start_date <= end_date:
        sale_record = gen_sale(store['store_no'], store['_id'], start_date.isoformat())
        sale_records.append(sale_record)

        start_date += datetime.timedelta(days=1)

    return sale_records

# This method when passed the genesis of the business will create collection names for every month from then until today.
def gen_sales_collections(start_date_str):
    labels = []
    sd = [int(x) for x in start_date_str.split('-')]
    start_date = datetime.date(year=sd[0], month=sd[1], day=1)
    today = datetime.date.today()
    today = today - datetime.timedelta(days=(today.day -1))

    while start_date <= today:
        label = 'sales_{0}_{1}'.format(start_date.year, start_date.month)
        labels.append(label)
        start_date += relativedelta(months=1)

    return labels


def determine_sales_collections(start_date_str, end_date_str):
    labels = []
    sd = [int(x) for x in start_date_str.split('-')]
    start_date = datetime.date(year=sd[0], month=sd[1], day=1)
    ed = [int(x) for x in end_date_str.split('-')]
    end_date = datetime.date(year=ed[0], month=ed[1], day=1)

    while start_date <= end_date:
        label = 'sales_{0}_{1}'.format(start_date.year, start_date.month)
        labels.append(label)
        start_date += relativedelta(months=1)

    return labels


def add_store_id_to_sales(stores):
    pass

