#!/usr/bin/python3
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
args = len(sys.argv)
ls = []
file_name = "add_item.json"
for i in range(1, args):
    ls.append(sys.argv[i])
    save_to_json_file(ls, file_name)
    load_from_json_file(file_name)
