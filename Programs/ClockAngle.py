def clockAngle(hour,min):
    # calculate the min hand movement per min. from 12oClock
    mm = min * (360/60)

    #     hour hand movement per/hour  = 30 (360/12)
    #     hour hand movement per/min = 30/60 = 0.5
    hm = (hour*60+min) * 0.5
    print(abs(mm - hm))

if __name__ == '__main__':
    clockAngle(6,15)
    clockAngle(12,55)
    clockAngle(3,00)
