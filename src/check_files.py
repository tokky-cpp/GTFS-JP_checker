# -*- coding: utf-8 -*-

import configparser
import os

config = configparser.ConfigParser()
config.read("../config.txt")
data_path = "../" + config["DATA"]["PATH"] + "/"

require_files = open("require_files.txt", "r")

isOK = True

for file in require_files:
    if os.path.exists(data_path + file.rstrip("\n")) is False:
        print("必須ファイル" + file.rstrip("\n") + "がありません\n")
        isOK = False

require_files.close()

if isOK:
    print("必須ファイルが全てあることを確認しました。\n")
