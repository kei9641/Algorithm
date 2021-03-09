def solution(progresses, speeds):
    answer = []
    done = 0
    length = len(progresses)
    while done < length:
        for i in range(length):
            progresses[i] += speeds[i]
        complete = 0
        for j in range(done, length):
            if progresses[j] >= 100:
                complete += 1
                done += 1
            else:
                break
        if complete:
            answer.append(complete)
    return answer