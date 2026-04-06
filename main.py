from fetch_data import fetch_earthquake_data
from transform import transform_data
import logging


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def main():
    data = fetch_earthquake_data()
    if data is None:
        logger.error("Failed to fetch data")
        return
    for batch in transform_data(data):
        logger.info(batch)



if __name__ == '__main__':
    main()