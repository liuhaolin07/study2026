scores = []
students = {}

while True:
    try:
        line = input("请输入姓名和成绩（直接回车结束）：").strip()
    except EOFError:
        break

    if not line:
        break

    name, score_text = line.split()
    score = int(score_text)
    students[name] = score
    scores.append(score)

if scores:
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    print("平均分：", average_score)
    print("最高分：", highest_score)
else:
    print("没有输入任何成绩")
