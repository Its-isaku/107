
#? Configuration file for MongoDB connection      
import pymongo
import certifi

#? MongoDB connection string
con_str = "mongodb+srv://test:test123@cluster0.pscxmkd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#? MongoDB client initialization
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

#? Database name
db = client.get_database("ChipisFarm")
