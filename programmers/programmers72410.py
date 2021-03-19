permit = ['-', '_', '.']

def changeLower(new_id):
    lower_id = ''
    for word in new_id:
        if word.isalpha():
            lower_id += word.lower()
        elif word.isdigit() or word in permit:
            lower_id += word
    return lower_id

def oneDot(new_id):
    deduplicate_id = new_id[0]
    for i in range(1, len(new_id)):
        if new_id[i] == '.' and deduplicate_id[-1] == '.':
            continue
        else:
            deduplicate_id += new_id[i]
    return deduplicate_id

def checkDot(new_id):
    return new_id.strip('.')

def notEmpty(new_id):
    if new_id == '':
        new_id += 'a'
    return new_id

def notExcess(new_id):
    return checkDot(new_id[:15])

def notUnder(new_id):
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id
    
def solution(new_id):
    answer = ''
    answer = notUnder(notExcess(notEmpty(checkDot(oneDot(changeLower(new_id))))))
    
    return answer