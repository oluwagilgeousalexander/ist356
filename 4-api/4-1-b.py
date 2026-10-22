import requests 
import dotenv  
import os 

from weather import geocode, weather

dotenv.load_dotenv(".env")
CENT_API_KEY = os.getenv("CENT_API_KEY")