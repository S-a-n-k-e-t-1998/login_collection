import pymongo


client=pymongo.MongoClient('mongodb://localhost:27017/')
db=client["Student_Info"]
student=db["Student_Details"]

def Stdent_data(Name,Address,Mobile_Number,E_mail):
    student_email=student.find_one({"E-Mail":E_mail})
    print(student_email)
    if student_email:
        return "Details Alderly Present"
    else:
        student.insert_one({"Name of Student":Name,"Address":Address,"Mobile Number":Mobile_Number,"E-Mail":E_mail})
        return "Details Enter Successfully"
