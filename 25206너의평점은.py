# 학점 계산
# 1. 과목별 점수 * 과목의 학점을 곱하기
# 2. 총합을 구하기
# 3. 전체 학점수로 나누기
# 배운점 -> split의 용도, 딕셔너리에서 키에 해당하는 값 꺼내기
object_list = []
total_points = 0.0
total_scores = 0.0

grade_dict={
    'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0
}

for i in range(20):
    temp = input()
    object_list.append(temp)

for x in object_list:
    temp = x.split(' ', 2)
    # print('corse: ',temp[0], 'score: ',temp[1],'grade: ',temp[2])
    score = float(temp[1])
    grade = temp[2]

    if grade in grade_dict:
        grade_score = grade_dict[grade]
        total_points += grade_score * score
        total_scores += score

gpa = total_points / total_scores
print(round(gpa, 6))






