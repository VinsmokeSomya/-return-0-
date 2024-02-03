import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
