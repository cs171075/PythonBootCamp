students_record = {
    "**roll_num**" : "CSxxxxxx",
    "**name**" : "XXX",
    "**age**" : 18,
    "**marks**(out of 100)" : 0
}
total_students = [students_record]

n=input("Enter the number of students")
for h in range(n):
    s1=input("Enter name")
    total_students[n]["**name**"]=s1
    s2=input("Enter roll no")
    total_students[n]["**roll_nume**"]=s2
    s3=input("Enter age")
    total_students[n]["**age**"]=s3
    s4=input("Enter marks")
    total_students[n]["**marks**"]=s4