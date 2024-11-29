import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21893504"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "55312f2ea94f5e8d47febe4fdc93fa31")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://<db_username>:<db_password>@cluster0.g8i5q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
