import sys, argparse
import logging, logging.config
from config import DB_DETAILS
from util import get_tables

def main():
    logging.config.fileConfig("logging.cfg")
    logger = logging.getLogger(__name__)
    logger.info(f"Application has started - {sys.argv[0]}")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", help="enviroment of the application", required=True)
    args = parser.parse_args()
    
    env = args.env
    logger.info(f"Env has been set to : {env}")
    
    print(DB_DETAILS.get(env, None))
    
    for idx, table in get_tables().iterrows():
        print(idx, table)
    
if __name__ == "__main__":
    main()