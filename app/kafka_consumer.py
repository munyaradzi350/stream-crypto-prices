from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# === Kafka Config ===
KAFKA_TOPIC = "crypto-prices"
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'

# === MongoDB Config ===
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "crypto_db"
MONGO_COLLECTION = "prices"

# Connect to MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Create Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='crypto-consumer-group'
)

print(f"📥 Listening to Kafka topic: {KAFKA_TOPIC}")

# Consume and insert into MongoDB
for message in consumer:
    data = message.value
    collection.insert_one(data)
    print(f"💾 Stored: {data['symbol']} → ${data['price']} at {data['timestamp']}")
