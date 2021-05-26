# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo

import mysql.connector
import pymongo

class QuotetutorialPipeline:
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
        db = self.conn['myquotes']
        self.collection = db['quotes_tb']
# connection for sql
    # def process_item(self, item, spider):
    #     self.store_db_sql(item)
    #     return item

    def create_connection_sql(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='myquotes'
        )
        self.curr = self.conn.cursor()

    def create_table_sql(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_db""")
        self.curr.execute(""" create table quotes_db(
                        content text,
                        author text,
                        tag text
                        )""")

    def store_db_sql(self, item):
        self.curr.execute("""insert into quotes_db values (%s, %s, %s)""", (
            item['content'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
