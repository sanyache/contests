max_score = int(input())
score = float(input())
score = (score/max_score) * 100
if score >=  90:
    print('OUTSTANDING')
elif 74 <= score < 90:
    print('EXCELLENT')
elif 60 <= score < 74:
    print('VERY GOOD')
else:
    print('PARTICIPANT')

