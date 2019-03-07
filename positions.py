# A structure list is an desending list of position in a hierarchy, each maps to a collection
feudalism = ["district", "region", "division", "corporate"]


def get_chunk_indexes(store_size, positions):
    stores_chunks = []

    chunk_count = len(positions)
    chunk_size = int(store_size / chunk_count)

    for i in range(chunk_count):
        start = (chunk_size * i)
        end = (chunk_size * i) + chunk_size

        if i == chunk_count - 1 and store_size % chunk_count:
            end += store_size % chunk_count

        stores_chunks.append((start, end))

    return stores_chunks


def create_district(name, stores):
    return {
        "name": name,
        "stores": stores
    }


def create_region(name, districts):
    return {
        "name": name,
        "districts": [x['_id'] for x in districts],
        "stores": [store for stores in [x['stores'] for x in districts] for store in stores]
    }


def create_division(name, regions):
    return {
        "name": name,
        "regions": [x['_id'] for x in regions],
        "districts": [district for districts in [x['districts'] for x in regions] for district in districts],
        "stores": [store for stores in [x['stores'] for x in regions] for store in stores]
    }

def create_corporate(name, divisions):
    return {
        "name": name,
        "divisions": [x['_id'] for x in divisions],
        "regions": [region for regions in [x['regions'] for x in divisions] for region in regions],
        "districts": [district for districts in [x['districts'] for x in divisions] for district in districts],
        "stores": [store for stores in [x['stores'] for x in divisions] for store in stores]
    }