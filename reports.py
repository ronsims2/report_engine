import mysqlx
import sales

user = 'sigronadmin'
password = 'foobar123'
network_service = 'localhost'


creds = {
    'host': 'localhost',
    'port': 33060,
    'user': user,
    'password': password
}

sess = mysqlx.get_session(creds)
db = sess.get_schema('sig_ron')

corp = db.get_collection('corporations').find('True').execute().fetch_one()

regions_coll = db.get_collection('regions')
for region in corp['regions']:
    regions_coll.find('_id = region')


################################################################################
# This gets hierarchy sales for a given date range
################################################################################
start_date = '2018-01-01'
end_date = '2018-12-01'

sales_coll_range = sales.determine_sales_collections(start_date, end_date)
colls = db.get_collections()
sales_colls = [x for x in colls if x.get_name().find('sales_') > -1]
applicable_sales_colls = [x for x in sales_colls if x.get_name() in sales_coll_range]

regions_coll = db.get_collection('regions')
regions = regions_coll.find('').execute()

period_sales = []
crit = "`date` >= '{0}' and `date` <= '{1}'".format(start_date, end_date)

for sales_coll in applicable_sales_colls:
    store_sales = db.get_collection(sales_coll)\
        .find(crit)\
        .execute().fetch_all()
    period_sales.append(store_sales)

for sales_record in period_sales:
    print(sales_record)





