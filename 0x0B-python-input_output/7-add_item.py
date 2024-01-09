#!/usr/bin/python3
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]
file_name = "add_item.json"
data = load_from_json_file(file_name)
data.extend(args)
save_to_json_file(data, file_name)
