import random
import locations
import datetime

def gen_loc_list(locations):
    return [(x, locations[x]) for x in locations]


def get_location(loc_list, num_of_locs):
    return loc_list[random.randint(0, num_of_locs - 1)]


def get_random_brand():
    brands = ['ACME', 'AJAX', 'Hudsucker', 'Blamo']
    return [brands[random.randint(0, len(brands) - 1)]][0]

def gen_random_open_date():
    num_of_days = random.randint(1, 3650)
    delta_of_days = datetime.timedelta(days=num_of_days)
    return datetime.date.today() - delta_of_days


def gen_random_close_date(open_date):
    end_date = None

    chance = random.randint(1, 1000)
    if chance == 42 or chance == 105 or chance == 216:
        num_of_days = random.randint(1, 3650)
        delta_of_days = datetime.timedelta(days=num_of_days)
        now = datetime.date.today()
        end_date_2 = open_date + delta_of_days

        if end_date_2 > now:
            end_date = now
        else:
            end_date = end_date_2

    return end_date


def create_store(store_no):
    store_model = {
        'store_no': store_no,
        'desc': 'Store: ' + str(store_no),
        'address': {
            'lines': [],
            'city': None,
            'state': None,
            'pc': None,
            'country': None,
            'planet': None
        },
        'brand': None,
        'open_date': None,
        'close_date': None,
        'phones': [],  # dict of numbers
        'emails': [],  # dict of emails,
        'people': [],  # dict of people related to the store
        'active': None,
    }

    return store_model


def gen_stores(store_count):
    stores = []
    locs = gen_loc_list(locations.city_to_state_dict)
    num_of_locs = len(locs)
    now = datetime.date.today()

    for i in range(store_count):
        store = create_store(i + 1)
        loc = get_location(locs, num_of_locs)
        store['address']['city'] = loc[0]
        store['address']['state'] = loc[1]
        store['address']['country'] = 'USA'
        store['brand'] = get_random_brand()
        open_date = gen_random_open_date()
        close_date = gen_random_close_date(open_date)
        store['open_date'] = open_date.isoformat()
        store['close_date'] = close_date.isoformat() if close_date else None
        store['active'] = False if close_date == now else True

        stores.append(store)

    return stores





