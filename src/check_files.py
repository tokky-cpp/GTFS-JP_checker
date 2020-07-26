# -*- coding: utf-8 -*-

import configparser
import os
import logging
import logging.config

config = configparser.ConfigParser()
config.read("../config.txt")
data_path = "../" + config["DATA"]["PATH"] + "/"

logging.config.fileConfig("../logging.conf", disable_existing_loggers=False)
logger = logging.getLogger('conf')

require_files = open("require_files.txt", "r")

isOK = True

for file in require_files:
    if os.path.exists(data_path + file.rstrip("\n")) is False:
        print("必須ファイル" + file.rstrip("\n") + "がありません\n")
        logging.error("必須ファイル" + file.rstrip("\n") + "がありません\n")
        isOK = False

require_files.close()

if isOK:
    print("必須ファイルが全てあることを確認しました。\n")
    logging.info("必須ファイルが全てあることを確認しました。\n")


logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
