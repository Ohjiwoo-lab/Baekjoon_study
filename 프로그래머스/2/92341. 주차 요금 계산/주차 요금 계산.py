from math import ceil

def solution(fees, records):
    answer = []
    
    car,result={},{}
    for record in records:
        time,num,op=record.split()
        h=int(time.split(':')[0])
        m=int(time.split(":")[1])
        
        if car.get(num) is None:
            car[num]=h*60+m
        elif result.get(num) is None:
            result[num]=(h*60+m)-car[num]
            del car[num]
        else:
            result[num]+=(h*60+m)-car[num]
            del car[num]
    
    # 출차 기록이 없는 것들.
    end=23*60+59   # 23:59
    for num, time in car.items():
        if result.get(num) is None:
            result[num]=(end-time)
        else:
            result[num]+=(end-time)
    
    result_sorted=sorted(result.items(), key=lambda x:x[0])
    for _, time in result_sorted:
        new_time = time-fees[0]
        if new_time<=0:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+ceil(new_time/fees[2])*fees[3])
    
    return answer