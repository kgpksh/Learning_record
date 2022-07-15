def solution(record):
    id_list = {}
    answer = []
    tmp = []

    for i in range(len(record)):
        cut = record[i].split(" ")
        doing = cut[0]
        uid = cut[1]

        if doing == "Enter":
            tmp.append([uid, "in"])
            id_list[uid] = cut[2]
        elif doing == "Leave":
            tmp.append([uid, "out"])
        elif doing == "Change":
            id_list[uid] = cut[2]

    for i in tmp:
        text = id_list[i[0]] + "님이 "

        if i[1] == "in":
            text += "들어왔습니다."
        else:
            text += "나갔습니다."

        answer.append(text)

    return answer
