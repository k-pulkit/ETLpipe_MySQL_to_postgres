import sys, argparse
import logging, logging.config
from read import read_table, def_test_read_table
from write import load_table, test_load_table
from util import get_db_details
import pandas as pd

def main():
    logging.config.fileConfig("logging.cfg")
    logger = logging.getLogger(__name__)
    logger.info(f"Application has started - {sys.argv[0]}")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", help="enviroment of the application", required=True)
    args = parser.parse_args()
    
    env = args.env
    logger.info(f"Env has been set to : {env}")
    
    db_details = get_db_details(env)
    db_details_source = db_details["SOURCE_DB"]
    db_details_target = db_details["TARGET_DB"]
    
    # test the reading code
    logger.info("Test the reading module")
    def_test_read_table(db_details_source)
    
    # test the write code
    logger.info("Test the writing module")
    test_load_table(db_details_target)
    
    
    
if __name__ == "__main__":
    main()