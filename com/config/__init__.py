# -*- coding: utf-8 -*
import os

curPath = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(curPath)[0]
from utils import utils

users_path = os.path.join(root_path, "config/users.json")
loginInfo_path = os.path.join(root_path, "config/loginInfo")
timeOut=20
loger = utils.get_log()
readFromLastChapter=True
readFrom0read=False
readTimelimit=60#单位second 0为无限制
