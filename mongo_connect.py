import logging
import json
import bson
import os
import datetime
from pymongo import MongoClient

# Logger settings - CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

config = {
  'sg' : 'mongodb://<username>:<password>@prod-mongo-3.shopback.sg:27017',
  'id' : 'mongodb://<username>:<password>@prod-mongo-3.shopback.co.id:27017'
}

# Set client 
country = os.environ.get('country')
client = MongoClient(config[country])

# Set database
db = client.paymentlinkedoffers

def handler(event, context):
    try:
      logger.info("Received event: " + json.dumps(event, indent=2))

      logger.info("initializing the collection")
      plooffers = db.activations


      # Get created document from the database using ID.
      plooffer = plooffers.find_one({ "_id": bson.ObjectId('5b8e0666935e3903f7d162fb') })
      return json.loads(json.dumps(plooffer, default=json_unknown_type_handler))
    except Exception as err:
      return json.loads(json.dumps({
        'error': str(err)
      }))

def json_unknown_type_handler(x):
    """
    JSON cannot serialize decimal, datetime and ObjectId. So we provide this handler.
    """
    if isinstance(x, bson.ObjectId) or isinstance(x, datetime.datetime):
        return str(x)
    raise TypeError("Unknown type")
