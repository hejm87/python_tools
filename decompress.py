#!/usr/bin/python3

import sys
import functools
import os.path

# 解压命令
def decompress_zip_cmd(file_path):
    return f'unzip {file_path}'

def decompress_tar_cmd(file_path):
    return f'tar -xvf {file_path}'

def decompress_tar_gz_cmd(file_path):
    return f'tar -zxvf {file_path}'

def decompress_tar_bz2_cmd(file_path):
    return f'tar -xjf {file_path}'

dc_suffixs = {
    'zip': decompress_zip_cmd,
    'tar': decompress_tar_cmd,
    'tar.gz': decompress_tar_gz_cmd,
    'tar.bz2': decompress_tar_bz2_cmd
}

# 获取压缩后缀名
def cmp_str(a, b):
    return len(a) >= len(b)

def get_match_suffix_name(file_path):
    keys = sorted(
        dict.keys(dc_suffixs),
        key = functools.cmp_to_key(cmp_str)
    )
    suffix_name = ''
    for x in keys:
        pos = file_path.find(x)
        if pos + len(x) == len(file_path):
            suffix_name = x
            break
    return suffix_name

if len(sys.argv) != 2:
    print("argv[0]: file path")
    sys.exit()

print(f"argv:{sys.argv}")

file_path = sys.argv[1]

if os.path.isfile(file_path) == False:
    print(f"not exist file:{file_path}")
    sys.exit()

suffix = get_match_suffix_name(file_path)
if suffix == '':
    print(f"没有找对匹配的后缀名，{file_path}")
    sys.exit()

dc_func = dc_suffixs.get(suffix)
if dc_func != None:
    dc_cmd = dc_func(file_path)
    os.system(dc_cmd)
    cmd = dc_func(file_path)
    print(f"cmd:{cmd}")
    if os.system(cmd) == 0:
        print(f"解压完成，{file_path} ^_^")
    else:
        print(f"解压失败，{file_path} T_T")
else:
    print(f"没有找到对应后缀名{suffix}解压方法 T_T")