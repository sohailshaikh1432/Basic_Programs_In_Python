from Log_Configuration import log_config_file
from OOPs_Programs.stock_details import StockDetails

logger = log_config_file.get_logger()

if __name__ == '__main__':
    try:
        StockDetails()
    except Exception as e:
        print('Oops! Exception occurred! Please try again!')
        logger.exception(e)
