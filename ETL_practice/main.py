from etl.extract import Extractor
from etl.transform import Transformer
from etl.load import Loader
import time

def main():
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('Starting ETL process at ' + start_time + '\n' + '')

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('\n' + 'ETL process completed at ' + end_time)

if __name__ == "__main__":
    main()