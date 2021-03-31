from Log_Configuration import log_config_file
logger = log_config_file.get_logger()

from OOPs_Programs.inventory_details import InventoryDetails

if __name__ == '__main__':
    try:
        InventoryDetails().json_handler()
    except Exception as e:
        print('Oops! Something went wrong! Please try again!')
        logger.exception(e)





