S = "00:01:07,400-234-090\n" + "00:05:01,701-080-080\n" + "00:05:00,400-234-090"
from collections import defaultdict

def Solution(S):
    lines = S.split('\n')

    phoneSec = defaultdict(int)
    # phoneSec = {}
    total = 0
    max_s = 0
    max_num = 999999

    for line in lines:
        arr = line.split(',')
        if len(arr) == 2:
            sec = toSec(arr[0])
            phnum = toNum(arr[1])

            if phnum in phoneSec:
                phoneSec[phnum] += sec
            else:
                phoneSec[phnum] = sec

    for p, s in phoneSec.items():
        if s >= max_s:
            max_s = s
            max_num = min(max_num, p)
        total += int(secsToCents(s))

    total -= int(secsToCents(max_s));

    return (total)


def secsToCents(sec):
    if sec < 300:
        return sec * 3
    else:
        if (sec % 60 == 0):
            return (sec / 60) * 150
        else:
            return ((sec / 60) + 1) * 150


def toSec(duration):
    arr = duration.split(":")

    if (len(arr) != 3):
        return 0
    sum = 0
    sum += int(arr[0]) * 3600
    sum += int(arr[1]) * 60
    sum += int(arr[2])
    return int(sum)


def toNum(phone):
    return int(phone.replace("-", ""))



print(Solution(S))

