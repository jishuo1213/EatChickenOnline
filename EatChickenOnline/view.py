import json
import random
import requests

from django.http import JsonResponse


def balls(request):
    c = request.GET['count']
    m_type = request.GET['type']
    res = []
    for _ in range(0, int(c)):
        item = {}
        if m_type == 'new':
            red_ball, blue_num = generate_code_new()
            item["red_ball"] = red_ball
            item["blue_ball"] = blue_num
            res.append(item)
        elif m_type == 'old':
            red_ball, blue_num = generate_code_old()
            item["red_ball"] = red_ball
            item["blue_ball"] = blue_num
            res.append(item)
        else:
            res = []

    print(res)
    response = JsonResponse(res, safe=False)
    return response


def generate_code_new():
    red_ball_nums = []
    blue_ball_nums = []
    red_num = 1
    while red_num <= 33:
        red_ball_nums.append(red_num)
        red_num = red_num + 1

    blue_num = 1
    while blue_num <= 16:
        blue_ball_nums.append(blue_num)
        blue_num = blue_num + 1

    system_random = random.SystemRandom()
    # red_list = []
    system_random.shuffle(red_ball_nums)
    # for index in range(0, 6):
    #     system_random.shuffle(red_ball_nums)
    #     select = system_random.randint(1, len(red_ball_nums))
    #     # print(red_ball_nums[select - 1], end='\t')
    #     red_list.append(red_ball_nums[select - 1])
    #     red_ball_nums.remove(red_ball_nums[select - 1])
    red_list = random.sample(red_ball_nums, 6)
    red_list.sort()
    system_random.shuffle(blue_ball_nums)
    return red_list, blue_ball_nums[system_random.randint(1, len(blue_ball_nums)) - 1]


def generate_code_old():
    red_ball_nums = []
    blue_ball_nums = []
    red_num = 1
    while red_num <= 33:
        red_ball_nums.append(red_num)
        red_num = red_num + 1

    blue_num = 1
    while blue_num <= 16:
        blue_ball_nums.append(blue_num)
        blue_num = blue_num + 1

    system_random = random.SystemRandom()
    red_list = []
    # system_random.shuffle(red_ball_nums)
    for index in range(0, 6):
        system_random.shuffle(red_ball_nums)
        select = system_random.randint(1, len(red_ball_nums))
        # print(red_ball_nums[select - 1], end='\t')
        red_list.append(red_ball_nums[select - 1])
        red_ball_nums.remove(red_ball_nums[select - 1])
    # red_list = random.sample(red_ball_nums, 6)
    red_list.sort()
    system_random.shuffle(blue_ball_nums)
    return red_list, blue_ball_nums[system_random.randint(1, len(blue_ball_nums)) - 1]


def get_last_twenty():
    res = requests.get('http://f.apiplus.net/ssq-20.json')
    json_res = res.json()

