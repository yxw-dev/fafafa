import os
import re

#通过命令行获取usb相机端口信息
test = os.popen('ls -l /dev|grep _cam')
text = test.read()
print(text)

#拆分出端口号信息
words = []
index = 0
start = 0

while index < len(text):
    start = index
    while text[index] != " " and text[index] not in [",", ",", "\n"]:
        index += 1
        if index == len(text):
            break
    words.append(text[start:index])
    if index == len(text):
        break
    while text[index] == " " or text[index] in [",", ".", "\n"]:
        index += 1
        if index == len(text):
            break

print(words)
print(words.index('back_cam'))
print(words.index('frame_cam'))
video_frame = words[words.index('frame_cam') + 2]
video_back = words[words.index('back_cam') + 2]
if len(video_frame) < 7:
    num_frame = video_frame[5]
else:
    num_frame = video_frame[5:]
if len(video_back) < 7:
    num_back = video_back[5]
else:
    num_back = video_back[5:]
print(num_frame, num_back)


#判断端口好，生成opencv调用相机的序号都为偶数通过（/dev/frame_cam）调用，否则使用0,2调用
res_text = []
sum_num = int(num_back) + int(num_frame)
print(sum_num)
if sum_num % 2 < 1 and int(num_frame) % 2 < 1:
    res_text.append("/dev/frame_cam")
    res_text.append("/dev/back_cam")
elif num_frame < num_back:
    res_text.append(0)
    res_text.append(2)
else:
    res_text.append(2)
    res_text.append(0)
print(res_text)
