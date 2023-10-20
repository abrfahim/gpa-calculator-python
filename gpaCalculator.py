
B = int(float(input('Give Your Bengali Subject Marks: ')))
E = int(float(input('Give Your English Subject Marks: ')))
M = int(float(input('Give Your Mathematics Subject Marks: ')))
S = int(float(input('Give Your Science Subject Marks: ')))

def student_Mark(B, E, M, S):

    if (B or E or M or S) > 100:
        print("Individual Subject Marks can not be greater than 100")
        return student_Mark()

    avarge_marks = (B + E + M + S) / 4
    print("Your avarge marks is ", avarge_marks)

    if avarge_marks>=0 and avarge_marks<=40:
        print ("Your Grade-result is: F")
    elif avarge_marks>=41 and avarge_marks<=60:
        print("Your Grade-result is: D")
    elif avarge_marks>=61 and avarge_marks<=70:
        print("Your Grade-result is: C")
    elif avarge_marks>=71 and avarge_marks<=80:
        print("Your Grade-result is:B")
    elif avarge_marks>=81 and avarge_marks<=90:
        print("Your Grade-result is:A")
    elif avarge_marks>=91 and avarge_marks<=100:
        print("Your Grade-result is:A+")
    elif avarge_marks>100:
        print("Inavalid result")

student_Mark(B, E, M, S)
