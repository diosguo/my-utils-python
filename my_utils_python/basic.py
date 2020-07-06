import json
import os
import sys


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





