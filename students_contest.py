n = int(input())
students = []
for _  in range(n):
    student = dict()
    data = input().split()
    for val in data:
        student['id'] = int(data[0])
        student['gender'] = data[1]
        student['grade'] = int(data[2])
        student['age'] = int(data[3])
        student['score'] = int(data[4])
    students.append(student)
m = int(input())
contests = []
for _ in range(m):
    contest = input()
    contests.append(contest)
students.sort( key=lambda x: (x['score']), reverse=True)
for contest in contests:
    print(contest)
    match contest:
        case 'IOI' | 'CEOI':
            std = students[0:4]
            for val in sorted(std, key=lambda x: x['id']):
                print(val['id'])
        case 'EGOI':
            std = [x for x in students if x['gender'] == 'female'][0:4]
            for val in sorted(std, key=lambda x: x['id']):
                print(val['id'])
        case 'EJOI':
            std = [x for x in students if x['age'] < 16][0:4]
            for val in sorted(std, key=lambda x: x['id']):
                print(val['id'])
        case 'BaltOI':
            std = students[0:6]
            for val in sorted(std, key=lambda x: x['id']):
                print(val['id'])
        case 'BalkOI':
            std = [x for x in students if x['grade'] != 11][0:4]
            for val in sorted(std, key=lambda x: x['id']):
                print(val['id'])
        case 'JBOI':
            std = [x for x in students if x['grade'] != 10 and x['grade'] != 11][0:4]
            for val in sorted(std, key=lambda x: x['id']):
                print(val['id'])

#print(students)