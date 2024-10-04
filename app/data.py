from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    A class to create a MongoDB database.

    ...

    Methods
    -------
    seed(amount)
        Insert documents into collection.
    reset()
        Delete all documents from collection.
    count()
        Return number of documents in collection.
    dataframe()
        Return documents in colection as a Dataframe.
    html_table()
        Return dataframe as an html table.
    """

    load_dotenv()
    db = MongoClient(getenv('MongoDB_connection_string'),
                     tlsCAFile=where())["Bander_Database"]

    def __init__(self):
        """
        construct db and col attributes for Database object.

        Set db attribute to database 'Bander_Database' from MongoClient
        Set col attribute to collection 'monster_collection' from db
        """

        self.db = self.db
        self.col = self.db['monster_collection']

    def seed(self, amount):
        """
        Insert data into 'monster_collection'

        Crate data using monster_to_dict function.

        Parameters
        ----------
        amount : int
            Number of monster documents to insert.
        """

        if amount < 1:
            return 'No monsters created.'
        if amount == 1:
            self.col.insert_one(monster_to_dict())
            return 'One monster created'
        doc_list = []
        for _ in range(amount):
            doc_list.append(monster_to_dict())
        self.col.insert_many(doc_list)
        return f"{amount} monsters created."

    def reset(self):
        """Delete all data in collection"""
        self.col.delete_many({})

    def count(self) -> int:
        return self.col.count_documents({})

    def dataframe(self) -> DataFrame:
        """Return data in collection as a Pandas DataFrame."""
        df = DataFrame(self.col.find({}))
        return df.drop(columns="_id")

    def html_table(self) -> str:
        """Return data in collection as an html table."""
        return self.dataframe().to_html()


def monster_to_dict():
    """Create a Monster object and return as a dictionary."""
    mon = Monster()
    dict = {"Name": mon.name,
            "Type": mon.type,
            "Level": mon.level,
            "Rarity": mon.rarity,
            "Damage": mon.damage,
            "Health": mon.health,
            "Energy": mon.energy,
            "Sanity": mon.sanity,
            "Timestamp": mon.timestamp}
    return dict


if __name__ == '__main__':
    df = Database().dataframe()
    print(df.head())
