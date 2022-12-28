import dotenv
from src.handler import handler

dotenv.load_dotenv()

if __name__ == '__main__':
    handler(event=None, context=None)