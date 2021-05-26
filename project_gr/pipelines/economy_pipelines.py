import pymongo

class EconomyPipeline:
    def __init__(self):

        self.create_connection()
        # self.create_table()

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def create_connection(self):
        self.conn = pymongo.MongoClient (
            'localhost',
            27017
        )
        db = self.conn['economy']
        self.collection = db['vneconomy']