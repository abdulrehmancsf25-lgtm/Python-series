from pymongo import MongoClient
import certifi

# 1. Get the path to the trusted certificate bundle
ca = certifi.where()

# 2. Your MongoDB connection string
# IMPORTANT: Replace <username> and <password> with your actual database credentials
uri = uri = "mongodb+srv://abdulrehmancsf25_db_user:KKa94Fbs46pKmUty@abdul-data-base.zsaiqz8.mongodb.net/?appName=Abdul-Data-Base"

# 3. Initialize the client, passing the certificates to fix the SSL error
client = MongoClient(uri, tlsCAFile=ca)

# 4. Test the connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"The following error occurred: {e}")