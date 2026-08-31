def hospital(func):
    def wrapper(self):
        print("----------------------------------")
        print("CITY CARE HOSPITAL")
        print("----------------------------------")
        func(self)
    return wrapper


class Report:
    def __init__(self):
        self.report=""
        
    def create(self):
        name=input("Enter your patient name:")
        age=input("Enter age:")
        gender=input("Enter gender:")
        problem=input("Enter problem:")
        diagnosis=input("Enter diagnosis:")
        medicine=input("Enter medicine:")
      
      
        self.report+="MEDICAL REPORT\n"
        self.report +="---------------------------\n"
        
        self.report +="Name:"+ name + "\n"
        self.report +="Age:"+ age + "\n"
        self.report +="Gender:"+ gender + "\n"
        self.report +="Problem:"+ problem + "\n"
        self.report +="Diagnosis:"+ diagnosis + "\n"
        self.report +="Medicine:"+ medicine + "\n"
        self.report +="Doctor: Dr.Priya Sharma"
        
    @hospital   
    def display(self):
        print(self.report)
        
    def save(self):
        file=open("medical_report.txt","w")
        file.write(self.report)
        file.close()
        print("Report saved successfully.")

obj = Report()

while True:
    print("\n 1.Create Report")
    print("2. Display Report")
    print("3. Save Report")
    print("4. Exit")
    
    ch= int(input("Enter your choice:"))
    
    if ch==1:
        obj.create()
    elif ch==2:
        obj.display()
    elif ch==3:
        obj.save()
    elif ch==4:
        break
    else:
        print("Invalid choice")

        
        
