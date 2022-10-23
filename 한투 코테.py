##date로부터 k 일 전 사이에 구매가 된 제품 중 재구매된 확률이 높은 순, 총 구매횟수 높은 순, pid가 낮은 순으로 출력

records = ['2020-02-25 uid1 pid1','2020-02-26 uid1 pid1','2020-02-26 uid1 pid1','2020-02-26 uid2 pid1','2020-02-27 uid2 pid1','2020-02-27 uid1 pid2',
           '2020-02-28 uid2 pid2','2020-02-30 uid2 pid2','2020-02-30 uid3 pid3','2020-02-30 uid3 pid3','2020-03-05 uid3 pid4','2020-02-26 uid1 pid5', '2020-03-06 uid6 pid6',
           '2020-03-04 uid3 pid1','2020-03-03 uid8 pid1','2020-03-02 uid3 pid1','2020-03-05 uid6 pid1','2020-03-03 uid3 pid2','2020-03-02 uid6 pid7','2020-03-02 uid6 pid5']

# records = ['2020-03-06 uid6 pid6']

k= 10
date ='2020-03-05'

def solution(records,k,date):
    ### date의 1년 전인 19년 부터로 가정 19*12*30 = 19년 총 일 수

    day = 19*12*30 + int(date[5:7])*30 + int(date[8:])
    product={}
    for record in records:
        record_date, user_id, product_id = record.split(' ')
        product[product_id] ={}

    for record in records:
        record_date, user_id, product_id = record.split(' ')
        record_day = 19 * 12 * 30 + int(record_date[5:7]) * 30 + int(record_date[8:])
        if day - record_day < k and day >=record_day :
            product[product_id][user_id] = product[product_id].get(user_id,0) +1

    result = {}
    for pid in product:
        more_than_one_time = 0
        total = 0
        for uid in product[pid]:
            if product[pid][uid] >1:
                more_than_one_time +=1
            total += product[pid][uid]
        if len(product[pid])>0:
            result[pid] = (more_than_one_time/len(product[pid]), total)

    result = sorted(result.items(),key = lambda x:(x[1][0],x[1][1],-int(x[0][3:])), reverse=True)
    answer= []
    print(result)
    for i in result:
        answer.append(i[0])
    if answer:
        print(answer)
    else:
        print("no result")
solution(records,k,date)
