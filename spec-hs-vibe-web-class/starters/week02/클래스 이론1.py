class Stu:
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    def info(self):
        print(f"나의 이름은 {self.name}")
        print(f"나의 나이는 {self.age}")
        print(f"나의 학교는 {self.school}")

st1 = Stu("son",
          "3x",
          "ccube")
st2 = Stu("hong,",
          "13",
          "sinjung")

st1.info()
st2.info()