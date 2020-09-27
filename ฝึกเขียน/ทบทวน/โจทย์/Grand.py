GPA = 0.0
def Gpa(*kids):
  Sum = 0.0
  for i in kids:
    Sum += i
  return Sum / len(kids)
    
  

Thai = float(input(""))
MATH = float(input(""))
ENGLISH = float(input(""))
SCIENCE = float(input(""))
SPORT = float(input(""))

print("THAI =",Thai)
print("MATH =",MATH)
print("ENGLISH =",ENGLISH)
print("SCIENCE =",SCIENCE)
print("SPORT =",SPORT)
print("---")

GPA = Gpa(Thai,MATH,ENGLISH,SCIENCE,SPORT)

print("GPA =",GPA)
