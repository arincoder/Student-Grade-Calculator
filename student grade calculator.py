def get_scores(num_subject):
    """ Collects the scores of the given number fo subjects """
    scores = []
    for i in range(num_subject) :
      score = int(input(f"Subject {i+1} grade: "))  
    
      while score > 100 or score < 0:
        print("Invalid score. Score must be between 0 and 100 inclusive")
        score = int(input(f"Subject {i+1} grade: "))
      scores.append(score)
      
    return scores

def total_scores(scores):
    """Returns the sum of the scores of each subject"""
    return sum(scores)

def average_score(scores):
    """ Returns the average of the scores at one decimal place"""
    average = sum(scores) / len(scores)
    return round(average, 2)

def grade(scores):
    """Determines the grade based on average score"""
    mean = average_score(scores)
    if mean >= 85:
      result = "A"
    elif mean >= 65:
      result = "B" 
    else:
      result = "F"
    return result

def status(scores):
    """Determines whether it is a pass or fail"""
    mean = average_score(scores)
    if mean >=  65:
      status = "PASS"
    else:
      status = "FAIL"
    return status

def highest(scores):
    """Returns the highest score obtained"""
    return max(scores)

def lowest(scores):
    """Returns the lowest score obtained"""
    return min(scores)
    

while True:
  print("\nStudent Grade Calculator")
  student_name = input("Enter student name: ").title()
  num_subject = int(input("How many subjects: "))
  scores = get_scores(num_subject)

  print("\n----REPORT----")
  print(f"\nStudent: {student_name}")
  print("Scores: ")
  for score in scores:
    print(score)

  print(f"\nTotal: {total_scores(scores)}")
  print(f"Highest score: {highest(scores)}")
  print(f"Lowest score: {lowest(scores)}")
  print(f"\nAverage: {average_score(scores)}")
  print(f"\nGrade: {grade(scores)}")
  print(f"\nStatus: {status(scores)}")

  #Ask if the student wants to check another person's grades
  inquire = input("Do you want to check another student's grade?(yes/no): ").lower()
  while inquire not in ("yes","no"):
    print("Please enter a yes or a no")
    inquire = input("Do you want to check another student's grade?(yes/no): ").lower()
  if inquire == "no":
    break

