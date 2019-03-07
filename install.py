import getpass
import requests
import keyring
import mysqlx
import stores
import sales
import positions

user = 'sigronadmin'
password = 'foobar123'
network_service = 'localhost'

if password is None:
    try:
        user = getpass.getuser()
        password = keyring.get_credential(network_service, user)
    except:
        if password is None:
            password = getpass.getpass('Please Enter your password: ')


creds = {
    'host': 'localhost',
    'port': 33060,
    'user': user,
    'password': password
}

sess = mysqlx.get_session(creds)
db = sess.get_schema('sig_ron')

# Generate stores
# my_stores = stores.gen_stores(5000)

#Get store collection
#stores_coll = db.get_collection('stores')

# Insert stores
# stores_coll.add(my_stores).execute()

################################################################################

# find the first the first store opened based on open and close dates to gen sales collections
# start_date_store = stores_coll.find('').sort(['open_date asc']).limit(1).execute()
# day_one = start_date_store.fetch_one()['open_date']
# table_names = sales.gen_sales_collections(day_one)

# Create monthly sales collection
# for table_name in table_names:
#     db.create_collection(table_name)
#     print(table_name + ' created!')


################################################################################
# Generate sales and insert

# my_stores = db.get_collection('stores').find('store_no > 4000').sort('store_no asc').limit(1000).execute().fetch_all()
# # for store in my_stores:
# #     print(store['desc'])
#
# my_coll = None
# sales_coll = None
#
# for store in my_stores:
#     print(store)
#     my_sales = sales.gen_sales(store)
#     for sale in my_sales:
#         sale_date = [int(x) for x in sale['date'].split('-')]
#         year = sale_date[0]
#         month = sale_date[1]
#         label = 'sales_{0}_{1}'.format(year, month)
#
#         if my_coll == label:
#             # Reuses collection
#             sales_coll.add(sale).execute()
#         else:
#             # Get a new collection
#             my_coll = label
#             sales_coll = db.get_collection(label)
#             sales_coll.add(sale).execute()

################################################################################

# Assign stores to districts
# districts_coll = db.create_collection('districts')
# districts_coll = db.get_collection('districts')
# my_stores = db.get_collection('stores').find('').fields('_id').execute().fetch_all()
# store_ids = [x['_id'] for x in my_stores]
# my_pos = ['district_{0}'.format(x + 1) for x in range(100)]
# chunks = positions.get_chunk_indexes(5000, my_pos)
#
# for i, pos in enumerate(my_pos):
#     mp = chunks[i]
#     ids = store_ids[mp[0]:mp[1]]
#     my_district = positions.create_district(pos, ids)
#     print(my_district["stores"])
#     districts_coll.add(my_district).execute()

################################################################################

# Assign stores and districts to regions
# my_districts = db.get_collection('districts').find('').execute().fetch_all()
# my_regions = ['region_{0}'.format(x + 1) for x in range(10)]
# chunks = positions.get_chunk_indexes(len(my_districts), my_regions)
# region_coll = db.create_collection('regions')
#
# for i, region in enumerate(my_regions):
#     mr = chunks[i]
#     reg_districts = my_districts[mr[0]:mr[1]]
#     my_region = positions.create_region(region, reg_districts)
#     region_coll.add(my_region).execute()
#     print(my_region)

################################################################################

# Assign stores  divisions and regions to divisions
# my_regions = db.get_collection('regions').find('').execute().fetch_all()
# my_divisions = ['division_{0}'.format(x + 1) for x in range(3)]
# chunks = positions.get_chunk_indexes(len(my_regions), my_divisions)
# print(chunks)
# div_coll = db.create_collection('divisions')
#
# for i, div in enumerate(my_divisions):
#     md = chunks[i]
#     div_regions = my_regions[md[0]:md[1]]
#     my_div = positions.create_division(div, div_regions)
#     div_coll.add(my_div).execute()
#     print(my_div)

################################################################################

# Assign divisions, regions, districts and stores to corporate
# my_divisions = db.get_collection('divisions').find('').execute().fetch_all()
# corporate = 'corporation_1'
# # corporate_coll = db.create_collection('corporations')
# corporate_coll = db.get_collection('corporations')
#
# my_corp = positions.create_corporate(corporate, my_divisions)
# corporate_coll.add(my_corp).execute()
# print(my_corp)

################################################################################

# This updates the sales records to add the store id to each sale for convenience

# stores_coll = db.get_collection('stores')
# stores = stores_coll.find('').sort('store_no asc').execute().fetch_all()
#
# colls = db.get_collections()
# sales_colls = [x for x in colls if x.get_name().find('sales_') > -1]
#
# for sc in sales_colls:
#     for i in range(5000):
#         print('Fixing: ' + sc.get_name() + str(i+1))
#         sc.modify('store_no = {0}'.format(i + 1)).set('store_id', stores[i]['_id']).execute()

