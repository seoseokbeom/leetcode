
from collections import defaultdict


def solution(n, customers):
    kioskarr = [0 for _ in range(n)]
    kioskcntdic = defaultdict(int)
    for i, customer in enumerate(customers):
        datestr, timestr, timecoststr = customer.split()
        customer_s = sec_representation(datestr, timestr)
        # print("sec representation:", customer_s)
        # find 운영 오래 안된 kiosk
        kiosktime, kioskidx = (findmin(kioskarr))
        kioskcntdic[kioskidx] += 1
        # print(finishtime(customer_s, kiosktime, timecoststr))
        print('고객도착:', customer_s, '매칭키오스크:',
              kioskidx+1, '키오스크운영시작:', kiosktime)
        kioskarr[kioskidx] = finishtime(customer_s, kiosktime, timecoststr)
        print('소요시간:', timecoststr, '키오스크 운영 완료(예정):', kioskarr[kioskidx])

    count = 0
    for key, val in kioskcntdic.items():
        if val > count:
            count = val
    return count


def findmin(arr):
    mn = arr[0]
    idx = 0
    for i, v in enumerate(arr):
        if v < mn:
            mn, idx = v, i
    return [mn, idx]


def finishtime(sec, kiosktime, timecoststr):

    return max(sec, kiosktime)+60*int(timecoststr)


def sec_representation(datestr, timestr):
    # datestr, timestr = timestr.split()
    month, d = datestr.split('/')
    h, m, s = timestr.split(':')
    # print(month, d, h, m, s)
    sec = 0
    sec += int(s)
    sec += 60*int(m)
    sec += 60*60*int(h)
    sec += 24*60*60*int(d)
    sec += 31*24*60*60*int(month)
    return sec
    # for i in [month, d, h, m, s]:
    #     seseci

    # print(timearr)


print(sec_representation('10/02', '00:15:45'))

# print(solution(2, ["02/28 23:59:00 03",
#                    "03/01 00:00:00 02", "03/01 00:05:00 01"]))


print(solution(3, ['10/01 23:20:25 30', '10/01 23:25:50 26', "10/01 23:31:00 05",
                   "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", '10/01 23:59:39 03', "10/02 00:10:00 10"]))
# print(solution(3, ['10-01 23:20:25 30']))
# print(sec_representation('10-01 23:20:25'))
