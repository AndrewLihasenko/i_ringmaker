"""
This script is convert .mp3 files to .m4r to make ringtone for iphone. 
Just run script and drop .mp3 file to commandline.

Autor: Andrew Lihasenko
"""


import subprocess
import os
import time
import re

path_name = os.path.split(
    input('Перетяните файл в окно теминала или введите вручную в формате: "путь/к/файлу/имя_файла.mp3" \n'))
# при перетаскивании, в путь с пробелами добавляется '\\', нужно их заменить на ''
file_path = path_name[0].replace('\\', '')
# при перетаскивании, в терминале в конце строки добавляется пробел, нужно от него избавиться 
if path_name[1].endswith(' '):
    file_name = path_name[1][:-1].replace('\\', '')
else:
    file_name = path_name[1].replace('\\', '')
name = os.path.splitext(file_name)

while True:
    value = input('Введите время начала рингтона в формате: "mm-ss" или "m:ss": ')
    if re.match(r'\d*\W\d*', value):
        time = re.split(r'\W', value)  # разделять по любому знаку, если не буква и не цифра
        if len(time[0]) == 2:
            start = "00:{}:{}".format(time[0], time[1])
        else:
            start = "00:0{}:{}".format(time[0], time[1])
        break
    else:
        print('Вы ввели некорректное время {}'.format(value), 'попробуйте еще раз')

os.chdir(file_path)
# ffmpeg -ss 00:00:10 -t 00:00:30 -i About_You_extract.mp3 -vn -acodec aac About_You_extract.m4a
subprocess.run(['ffmpeg', '-ss', start, '-t', '00:00:40', '-i', file_name, '-vn', '-acodec', 'aac', '%s_ringtone.m4a' %name[0]])

for f in os.listdir(file_path):
    if f == name[0] + '_ringtone.m4a':
        m4a_name = os.path.splitext(f)
        m4a_path = os.path.abspath(f)
        head = os.path.split(m4a_path)
        os.rename(m4a_path, os.path.join(head[0], m4a_name[0] + '.m4r'))