def calc_average(list):
    # Cette fonction calcule la moyenne des notes et retourne la moyenne
    avrg = sum(list)/len(list)
    return avrg

def input_grades():
    # Cette fonction crée la liste de notes et retourne cette liste
    grades = []
    n = 4 # Qty of grades to enter.
    print("Entrez 4 notes d'un étudiant: ")
    for i in range(0,n):
        ele = int(input())
        grades.append(ele)
    return grades

def question_check(average):
    # Cette fonction verifie si la moyenne est supérieur à 60%
    if average > 60:
        return True
    else:
        return False

def main():
    grades = input_grades()
    average = calc_average(grades)
    print(f"The average is {average}% ")
    print()
    print("Est-ce que l'étudiant a une moyenne supérieur à 60% ? ")
    question = question_check(average)
    if question == True:
        print("YES")
    else:
        print("NO")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

   main()

