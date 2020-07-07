#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File   :   my_utils_python\basic.py
@Time   :   2020/7/6 16:19
@Auther :   DiosGuo
@Contact:   guoxuyang5@jd.com
@Version:   0.0.1
@Desc   :   basic
"""
import json
import os
import logging
import logging.handlers
import datetime
import pickle


def load_json_from_file(file_path: str, encoding='utf-8'):
    """
    Load Json data from file
    :param file_path: path to json file
    :param encoding: encoding of json file
    :return: a json read in object list or dict
    """
    with open(file_path, 'r', encoding=encoding) as fin:
        return json.load(file_path)


def save_json_to_file(obj: object, file_path: str, encoding='utf-8'):
    """
    Save Json data to file
    :param obj: the object data you want to save
    :param file_path: the file path you want to save to
    :param encoding: the file encoding
    :return: None
    """
    base_dir = os.path.dirname(file_path)
    if base_dir:
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

    with open(file_path,'w',encoding=encoding) as fou:
        json.dump(obj, fou)


def load_pkl(file_path: str):
    with open(file_path, 'rb') as fin:
        return pickle.load(fin)


def save_pkl(obj, file_path: str):
    with open(file_path, 'wb') as fou:
        pickle.dump(obj, file_path)


def get_logger_with_common_config(logger_name='logger', log_dir='./log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Console
    c_handler = logging.StreamHandler()
    c_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    c_handler.setLevel(logging.DEBUG)

    # all.log
    rf_handler = logging.handlers.TimedRotatingFileHandler(os.path.join(log_dir, 'all.log'),
                                                           when='midnight',
                                                           encoding='utf-8',
                                                           interval=1,
                                                           backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # error.log
    f_handler = logging.FileHandler(os.path.join(log_dir, 'error.log'), encoding='utf-8')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(c_handler)
    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger
