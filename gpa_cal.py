from tmp import sub_code
# marks1[sub-code, sub-name, internal-marks,external-marks,total-marks,P/F,updated-on]

def gpa(marks1):
    earned_cre=0
    cre_sum=0
    sem5={'18CS51':3,'18CS52':4,'18CS53':4,'18CS54':3,'18CS55':3,'18CS56':3,'18CSL57':2,'18CSL58':2,'18CIV59':1,
          '18MAT41': 0, '18CS45': 0, '18CS46': 0, '18CS33': 0, '18CSL38': 0, '18ELE13': 0, '18MAT31': 3, '18CS32': 3, '18CS33': 3, '18CS34': 3, 
          }
    gpa_table=[]
    for row in marks1:
        data=[]
        data.extend([row[0],row[1]])
        total_credits=sub_code[row[0]]
        data.append(total_credits)
        data.append(int(row[4]))
        gl,gp=grade(int(row[4]))
        data.extend([gl,gp])
        
        credit_point=total_credits*gp
        data.append(credit_point)

        earned_cre+=credit_point
        cre_sum+=total_credits
        gpa_table.append(data)
    return [gpa_table,earned_cre,cre_sum]

#Grade point and grade letter 
def grade(m): #m -> marks
    grade_point = 0
    grade_letter = ''
    if m >= 90:
        grade_letter += 'O'
        grade_point = 10
    elif m >= 80:
        grade_letter += 'S'
        grade_point = 9
    elif m >= 70:
        grade_letter += 'A'
        grade_point = 8
    elif m >= 60:
        grade_letter += 'B'
        grade_point = 7
    elif m >= 50:
        grade_letter += 'C'
        grade_point = 6
    elif m >= 45:
        grade_letter += 'D'
        grade_point = 5
    elif m >= 40:
        grade_letter += 'E'
        grade_point = 4
    elif m >= 0:
        grade_letter += 'F'
        grade_point = 0
    elif m == -1:
        grade_letter += 'Ab'
        grade_point = 0
    return grade_letter, grade_point

