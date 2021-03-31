from Log_Configuration import log_config_file
from OOPs_Programs.inventory_details import InventoryDetails

logger = log_config_file.get_logger()

if __name__ == '__main__':
    try:
        InventoryDetails()
    except Exception as e:
        print('Oops! Something went wrong! Please try again!')
        logger.exception(e)
