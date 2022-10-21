import math

def solution(fees, records):
    answer = []
    time_record = {}
    fee_record = {}
    for i in records:
        time,car,status = map(str,i.split())
        minute = 60*int(time[:2])+int(time[3:])
        if status == "IN":
            if car in time_record: 
                time_record[car][0] += minute
                time_record[car][2] +=1
            else:
                time_record[car] = [minute,0,1,0] ## 입차,출차,입차횟수,출차횟수
        elif status =="OUT":
            time_record[car][1] += minute
            time_record[car][3] +=1
        
    for car,record in time_record.items():
        if record[3] != record[2]:
            result = (60*23 + 59 + record[1]) -record[0]
        else:
            result = record[1]-record[0]
        
        if result <=fees[0]:
            fee_record[car] = fee_record.get(car,0) + fees[1]
        else:
            fee_record[car] = fee_record.get(car,0) + fees[1] + math.ceil((result-fees[0])/fees[2]) * fees[3]
            
    fee_record = sorted(fee_record.items(), key = lambda x: x[0])
    for i in fee_record:
        answer.append(i[1])
    return answer
