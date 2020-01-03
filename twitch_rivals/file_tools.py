import json
import os
import sys
import argparse
from datetime import datetime
import logging


def json_validator(json_path):
    """Validate and upload json data

    param_1: json_path - [String] Path to json file.
    return: json_data - [Dictionary] Json content.
    """
    logging.info("Opening json")
    if os.path.exists(json_path):
        try:
            logging.info("Reading json")
            with open(json_path) as upload:
                json_data = json.load(upload)
            upload.close()
            log_json(json_data)
            return json_data
        except json.decoder.JSONDecodeError as e:
            print(e)
    print("Json format is not valid")


def get_options(args):
    """ Parse args from system.

    param_1 : args - [Dictionary] Map of system params.
    return: [argparse.Namespace] Class containing all params.
    """
    parser = argparse.ArgumentParser(description="Title")
    parser.add_argument("-j", "--json", type=str, help="Your input json file.")
    options_in = parser.parse_args(args)
    return options_in


def open_logger():
    """ Create logger for the project."""
    current_path = os.path.dirname(os.path.abspath(__file__))
    # Hardcoded line! Warning moving this file may cause log problem.
    log_dir_path = os.path.join(current_path, '..\\..\\Logs\\')
    today_ob = datetime.today()
    date_string = today_ob.strftime("%d-%m-%Y_%H-%M-%S.log")
    log_path = os.path.join(log_dir_path, date_string)
    log_path = os.path.abspath(log_path)
    log_format = '%(levelname)s - %(funcName)s():%(lineno)i: %(message)s'
    try:
        logging.basicConfig(filename=log_path, filemode='w', format=log_format)
        logging.getLogger().setLevel(logging.INFO)
        logging.info("Log started at {0}".format(date_string.replace(".log", "")))
        print("Log path: {0}\n".format(log_path))
    except FileExistsError as e:
        print("The path {0} not valid - Error: {1}".format(os.path.basename(log_path), e))


def exit_with_error(msg, error_code, extra_msg=None):
    """ Error & Exit with msg and code.

    param_1: msg - [String] massage to log.
    param_2: error_code - [ErrorEnum] Error Enum code
    param_3: extra_msg - [String] Extra field for another massage

    System will exit the code at the end of this function.
    """
    logging.error(msg)
    logging.error("Code: {0}".format(error_code))
    if extra_msg:
        logging.error(extra_msg)
    logging.error("Exits..")
    sys.exit(error_code)


def log_json(json_data):
    """ Log json data.

    param_1: json data - [Dictionary] Json content.
    """
    logging.info("Json attributes: ")
    for attr in json_data.keys():
        logging.info("\t\t{0} : {1}".format(attr, json_data[attr]))
