class student:
    def __init__(self, kor, eng, mat):
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        
    def get_total(self):
        return self.__kor + self.__eng + self.__mat
    
score = input().split(', ')
scores = list(map(int, score))
result = student(scores[0], scores[1], scores[2])
print('국어, 영어, 수학의 총점: {}' .format(result.get_total()))