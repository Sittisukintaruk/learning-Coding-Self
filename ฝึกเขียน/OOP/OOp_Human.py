class Hunmun :
    Gender = ""
    def __init__(self,name, age ,heigt, weight,gender):
        self.name = name
        self.age = age
        self.heigt = heigt
        self.weight = weight
        self.gender = gender

    def Say(self, Message):
        self.Message = Message

        print("Human Say %s" % self.Message)



    def checkGender(self):
        if self.gender == "M":
            self.gender =  "ผู้ชาย"
        else:
            self.gender =  "ผู้หญิง"
   
    def Detail_human(self):
        
        print(" My name is %s \n My Gender is %s \n age : %d\n heigt : %d \n weight : %d " % (self.name ,self.gender, self.age , self.heigt , self.weight))

    def BMI(self):
        if self.age >= 20 :

            bmi = float(self.weight) /pow ((float(self.heigt) * 0.01 ) ,2)
            SumWeight =""        
            if(bmi > 18.5 and bmi < 25):
                SumWeight = "น้ำหนักปกติ"
            elif(bmi >= 25.0 and bmi < 30.0):
                SumWeight = "น้ำหนักเกิน"
            elif(bmi >= 30.0 and bmi < 39.9):
                SumWeight = "โรคอ้วน"
            else:
                SumWeight = "โรคอ้วนขั้นรุนแรง"

            print("ค่า BMI ของคุณเท่ากับ : %f " % bmi)
            print("คุณอยู่ในเกณฑ์ : %s " % SumWeight)
        else :
            print("คุณอายุไม่ถึง 20 ปีตามมาตรฐาน BMI")


def getinput():
    Name = input("What is you name : ")
    if(Name.isdigit()):
        while Name.isdigit():
            print("กรุณาระบุเป็นตัวหนังสือ !! ")
            Name = input("What is you name : ")
    age = int(input("What is you age : "))
    gender = input("What is you gender(M/F): ")

    if(gender != "M" or gender != "F"):
        while gender != "M" :
            if gender == "F":
                break
            else:
                print("กรุณาระบุเป็นตัวหนังสือ  M(ผู้ชาย) หรือ F(ผู้หญิง) !! ")
                gender = input("What is you gender(M/F): ")

    heigt = int(input("What is you heigt : "))
    weight = int(input("What is you weight : "))

    return Hunmun(Name , age , heigt , weight , gender)


beer = getinput()
#beer.Say(input("Say Something !! : "))
beer.checkGender()
beer.Detail_human()
beer.BMI()

