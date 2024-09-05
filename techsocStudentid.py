import os
import json
class user:
    def __init__(self,username,password,role):
        self.username=username
        self.password=password
        self.role=role
    #should have function like login , logout, register 
    def load_data(self):
        with open("data.json","r") as file:
            data_combined=json.load(file)
    def save_data(self,data):
        with open("data.json","w") as file:
            json.dump(data,file)
def print_colored(text,text_color_code,bg_color_code=None):
    if bg_color_code:
        print(f"\033[{text_color_code};{bg_color_code}m{text}\033[0m")
    else:
        print(f"\033[{text_color_code}m{text}\033[0m")
class Admin(user):
    def __init__(self,username,password):
        super().__init__(username,password,role="admin")
        #should have features like adding , removing students grades and updating it
    def convert_to_dictionary(self):
        return {
            "username":self.username ,
            "password":self.password ,
            "role":"admin"
        }
class Student(user):
    def __init__(self,username,password):
        super().__init__(username,password,role="student")
        #should have features like viewing grades 
    def convert_to_dictionary(self):
        return {
            "username":self.username ,
            "password":self.password ,
            "role":"student" ,
            "CPI":"Nill" ,
            "SPI":"Nill" , 
            "Attendence":"Nill"
        }
def load_data_into_list(existing_data):
    with open("data.json","r") as file:
        existing_data=json.load(file)
def dump_data_into_json(data):
    with open("data.json","w") as file:
        json.dump(data,file)
def some_function():
    with open("Studentdata.json","r") as file:
        existing_Student_data=json.load(file)
    result=[studentdata for studentdata in existing_Student_data if username_providedadmin in studentdata["username"]]
    result1=result[0] #now result1 is {}
    result1_username=result1["username"]
    result1_password=result1["password"]
    result1_role=result1["role"]
    result1_CPI=result1["CPI"]
    result1_SPI=result1["SPI"]
    result1_attendence=result1["Attendence"]
#will try to improve by defining functions and loading/saving file by using function directly , 
#currently getting an unexpected result for some reason
data_combined=[{"username": "Nill", "password": "Nill", "role": "Nill", "CPI": "Nill", "SPI": "Nill", "Attendence": "Nill"}]
data_student=[{"username": "Nill", "password": "Nill", "role": "Nill", "CPI": "Nill", "SPI": "Nill", "Attendence": "Nill"}]
#did this so that ki error na aae , aage code me json.load hai usme error aarhi thi
if not os.path.exists("data.json"): #creating the json file if it doesn't exist
    with open("data.json","w") as file:
        json.dump(data_combined,file)
if not os.path.exists("Studentdata.json"):
    with open("Studentdata.json","w") as file:
        json.dump(data_student,file)
print_colored("1.Register\n2.Login\n3.Exit",32)
Select=int(input("Select an operation:"))
while Select !=3:
    if Select==1:
        username=input("Username:")
        password=input("Password:")
        print("1.Admin\n2.Student")
        role=int(input("Select an option:"))
        if role==1:
            passcode_admin=int(input("Enter admin passcode:"))
            if passcode_admin==5451:
                print_colored("You have entered the correct passcode.",94)
                data_single=Admin(username,password)   
                data_single_dictionary=data_single.convert_to_dictionary()
                data_list=[]
                data_list.append(data_single_dictionary)
                with open("data.json","r") as file:
                    existing_data=json.load(file)
                data_combined=existing_data+data_list
                print(data_combined)
                dump_data_into_json(data_combined)
                print("User have been successfully registered.")
                print_colored("1.Register\n2.Login\n3.Exit",32)
                Select=int(input("Select an operation:"))
            else:
                print_colored("You have entered wrong password.",94)
                print_colored("Admin verficiation completed.",40,91)
                print_colored("1.Register\n2.Login\n3.Exit",32)
                Select=int(input("Select an operation:"))
        elif role==2:
            passcode_student=int(input("Enter student passcode:"))
            if passcode_student==5452:
                print_colored("You have entered the correct passcode.",94)
                print_colored("Student verficiation completed.",40,91)
                data_single=Student(username,password) #created an instance for using the class functions
                data_single_dictionary=data_single.convert_to_dictionary() #used the class function that i created above in the line
                data_list=[]
                student_list=[]
                data_list.append(data_single_dictionary)
                with open("data.json","r") as file:
                    existing_data=json.load(file) #json.load(file) will provide result in list format only 
                data_combined=existing_data+data_list
                print(data_combined)
                dump_data_into_json(data_combined)
                with open("Studentdata.json","r") as file:
                    existing_Student_data=json.load(file)           
                student_list.append(data_single_dictionary) #made a list of single student data only [{}] soemthing like this
                student_data_combined=student_list+existing_Student_data
                with open("Studentdata.json","w") as file:
                    json.dump(student_data_combined,file)
                print("User have been successfullt registered.")
                print_colored("1.Register\n2.Login\n3.Exit",32)
                Select=int(input("Select an operation:"))
            else:
                print_colored("You have entered wrong password.",94)
                print_colored("Student varification not completed",40,91)
                print_colored("1.Register\n2.Login\n3.Exit",32)
                Select=int(input("Select an operation:"))
        else:
            print_colored("Please Select a valid option.",40,91)
            print_colored("1.Register\n2.Login\n3.Exit",32)
            Select=int(input("Select an operation:"))
    elif Select==2:
        print("You have chosen the login option")
        username_login=input("Username:")
        password_login=input("Password:")
        print("1.Admin\n2.Student",)
        role=int(input("Select an option:"))
        if role==1:
            passcode_admin=int(input("Enter passcode for admin:"))
        elif role==2:
            passcode_student=int(input("Enter passcode for student:"))
        else:
            print_colored("Please Select an Valid Option.",40,91)
            print_colored("1.Register\n2.Login\n3.Exit",32)
            Select=int(input("Select an operation:"))
        with open("data.json","r") as file:
            existing_data=json.load(file)
        result=[data for data in existing_data if username_login == data["username"]]
        if not result:
            print_colored("Username not found.",40,91)
            print_colored("1.Register\n2.Login\n3.Exit",32)
            Select=int(input("Select an operation:"))
        else:
            result_dictionary=result[0] #{'username':username_input,'password':password_input,'role':'admin\student'}
            password_actual=result_dictionary["password"]
        if password_actual==password_login:
            print("you have entered the correct password")
            if role==1:
                if result_dictionary["role"]=="admin":
                    if passcode_admin==5451:
                        print_colored("you have entered the correct passcode.",94)
                        print_colored("You are allowed to use the Admin functions.",94)
                        print_colored("1.View all Students data\n2.View Some Specific Student's data\n3.Edit Data of Some Specific Student",94)
                        select_admin=int(input("Select an Operation:"))
                        if select_admin==1:
                            print_colored("You have chosen the first option",94)
                            with open("Studentdata.json","r") as file:
                                existing_Student_data=json.load(file)
                            print(existing_Student_data)
                        elif select_admin==2:
                            print_colored("You have chosen the first option",94)
                            with open("Studentdata.json","r") as file:
                                existing_Student_data=json.load(file)
                            username_providedadmin=input("Enter username of the student:")
                            result=[studentdata for studentdata in existing_Student_data if username_providedadmin == studentdata["username"]]
                            result1=result[0] #[{}]-->{}
                            result1_username=result1["username"]
                            result1_password=result1["password"]
                            result1_role=result1["role"]
                            result1_CPI=result1["CPI"]
                            result1_SPI=result1["SPI"]
                            result1_attendence=result1["Attendence"] #accessed individual elements of students data
                            result_list=[{f"username":result1_username,"password":"can't show","role":result1_role,"CPI":result1_CPI,"SPI":result1_SPI,"Attendence":result1_attendence}]
                            print(result_list) #yaha pe direct dictionary bhi define kar skte the but i prefer uniformity thorughout the code islie [{}] format me print karaya
                        elif select_admin==3:
                            print_colored("You have chosen the third option.",94)
                            with open("Studentdata.json","r") as file:
                                existing_Student_data=json.load(file)
                            username_providedadmin=input("Enter the Username of The student:")
                            result=[studentdata for studentdata in existing_Student_data if username_providedadmin == studentdata["username"]]
                            result1=result[0] #now result1 is {}
                            result1_username=result1["username"]
                            result1_password=result1["password"]
                            result1_role=result1["role"]
                            result1_CPI=result1["CPI"]
                            result1_SPI=result1["SPI"]
                            result1_attendence=result1["Attendence"]
                            print("1.CPI\n2.SPI\n3.Attendence\n4.All")
                            choose_edit=int(input("Select an option which you want to edit:"))
                            if choose_edit==1:
                                some_function()
                                CPI_new=float(input("Enter CPI:"))
                                result_list=[{f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":CPI_new,"SPI":result1_SPI,"Attendence":result1_attendence}]
                                result_list_toprint=result_list=[{f"username":result1_username,"password":"can't show","role":result1_role,"CPI":CPI_new,"SPI":result1_SPI,"Attendence":result1_attendence}]
                                print("The Student data has been successfully edited.")
                                print(result_list_toprint)
                                #updating this data into the json file
                                index_to_delete=existing_Student_data.index(result1)
                                existing_Student_data.pop(index_to_delete) #deleting the previous data of that student
                                result_dictionary=result_list[0]
                                updated_single_student_data={f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":CPI_new,"SPI":result1_SPI,"Attendence":result1_attendence}
                                existing_data.insert(index_to_delete,updated_single_student_data)
                                with open("Studentdata.json","w") as file:
                                    json.dump(existing_data,file)
                                print_colored("1.Register\n2.Login\n3.Exit",32)
                                Select=int(input("Select an operation:"))
                            elif choose_edit==2:
                                some_function()
                                SPI_new=float(input("Enter SPI:"))
                                result_list=[{f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":result1_CPI,"SPI":SPI_new,"Attendence":result1_attendence}]
                                result_list_toprint=[{f"username":result1_username,"password":"can't show","role":result1_role,"CPI":result1_CPI,"SPI":SPI_new,"Attendence":result1_attendence}]
                                print("The Student data has been successfully edited.")
                                print(result_list_toprint)
                                index_to_delete=existing_Student_data.index(result1)
                                existing_Student_data.pop(index_to_delete) 
                                result_dictionary=result_list[0]
                                updated_single_student_data={f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":result1_CPI,"SPI":SPI_new,"Attendence":result1_attendence}
                                existing_data.insert(index_to_delete,updated_single_student_data)
                                with open("Studentdata.json","w") as file:
                                    json.dump(updated_single_student_data,file)
                                print_colored("1.Register\n2.Login\n3.Exit",32)
                                Select=int(input("Select an operation:"))
                            elif choose_edit==3:
                                some_function()
                                Attendece_new=float(input("Enter attendence(in %):"))
                                result_list=[{f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":result1_CPI,"SPI":result1_SPI,"Attendence":Attendece_new}]
                                result_list_toprint=[{f"username":result1_username,"password":"can't show","role":result1_role,"CPI":result1_CPI,"SPI":result1_SPI,"Attendence":Attendece_new}]
                                print("The Student data has been successfully edited")
                                print(result_list_toprint)
                                index_to_delete=existing_Student_data.index(result1)
                                existing_Student_data.pop(index_to_delete)
                                result_dictionary=result_list[0]
                                updated_single_student_data={f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":result1_CPI,"SPI":result1_SPI,"Attendence":Attendece_new}
                                existing_Student_data.insert(index_to_delete,updated_single_student_data)
                                with open("Studentdata.json","w") as file:
                                    json.dump(existing_Student_data,file)
                                print_colored("1.Register\n2.Login\n3.Exit",32)
                                Select=int(input("Select an operation:"))
                            elif choose_edit==4:
                                some_function()
                                CPI_new=float(input("Enter CPI:"))
                                SPI_new=float(input("Enter SPI:"))
                                Attendece_new=float(input("Enter attendence(in %):"))
                                result_list=[{f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":CPI_new,"SPI":SPI_new,"Attendence":Attendece_new}]
                                result_list_toprint=[{f"username":result1_username,"password":"Can't Show","role":result1_role,"CPI":CPI_new,"SPI":SPI_new,"Attendence":Attendece_new}]
                                print("The Student data has been successfully edited")
                                print(result_list_toprint)
                                index_to_delete=existing_Student_data.index(result1)
                                existing_Student_data.pop(index_to_delete)
                                updated_single_student_data={f"username":result1_username,"password":result1_password,"role":result1_role,"CPI":CPI_new,"SPI":SPI_new,"Attendence":Attendece_new}
                                existing_Student_data.insert(index_to_delete,updated_single_student_data)
                                with open("Studentdata.json","w") as file:
                                    json.dump(existing_Student_data,file)
                                print_colored("1.Register\n2.Login\n3.Exit",32)
                                Select=int(input("Select an operation:"))
                            else:
                                print("Please Select a valid option.")
                                print_colored("1.Register\n2.Login\n3.Exit",32)
                                Select=int(input("Select an operation:"))
                        #admin functions:editing cpi,spi,attendence , deleting a student data completely 
                        #this deleted student datas should be preferably dumped to another data file such that its recoverbale when necessary
                        #will add admin functions here
                        #basically only this block will be able to acess these student functions
                        print_colored("1.Register\n2.Login\n3.Exit",32)
                        Select=int(input("Select an operation:"))
                    else:
                        print_colored("you have entered wrong passcode.",40,91)
                        print_colored("Admin verification unsuccessful,redirecting to first page.",40,91)
                        print_colored("1.Register\n2.Login\n3.Exit",32)
                        Select=int(input("Select an operation:"))
                else:
                    print("you are not registered as an admin.")
                    print_colored("1.Register\n2.Login\n3.Exit",32)
                    Select=int(input("Select an operation:"))
            elif role==2:
                if result_dictionary["role"]=="student":
                    if passcode_student==5452:
                        print_colored("you have entered the correct passcode.",94)
                        print_colored("You are allowed to use the Student functions.",94)
                        print_colored("You can see your Performance data.",94)
                        with open("Studentdata.json","r") as file:
                            existing_Student_data=json.load(file)
                        result=[studentdata for studentdata in existing_Student_data if username_login == studentdata["username"]]
                        result_dictionary=result[0] #this will provide a particular students data in [{}] format so to get in {} format i acessed the first element of the list
                        #again this is not taking care of the fact if two students are with same name , will solve this issue later
                        print(f"Username:{result_dictionary["username"]}")
                        print(f"CPI:{result_dictionary["CPI"]}")
                        print(f"SPI:{result_dictionary["SPI"]}")
                        print(f"Attendence:{result_dictionary["Attendence"]}")
                        #will add student functions here
                        #basically only this block will be able to acess these student functions
                        print_colored("1.Register\n2.Login\n3.Exit",32)
                        Select=int(input("Select an operation:"))
                    else:
                        print_colored("you have entered wrong passcode.",40,91)
                        print_colored("Admin verification unsuccessful,redirecting to first page.",40,91)
                        print_colored("1.Register\n2.Login\n3.Exit",32)
                        Select=int(input("Select an operation:"))
                else:
                    print("you are not registered an a student.")
                    print_colored("1.Register\n2.Login\n3.Exit",32)
                    Select=int(input("Select an operation:"))
        else:
            print_colored("You have entered the wrong password",40,91)
            print_colored("login failed, redirecting to the initial page",40,91)
            print_colored("1.Register\n2.Login\n3.Exit",32)
            Select=int(input("Select an operation:"))
    elif Select==3:
        print("You have exitted from the program")
    else:
        print_colored("Please Select a valid option.",40,91)
        print_colored("1.Register\n2.Login\n3.Exit",32)
        Select=int(input("Select an operation:"))
#i didnt cater the problem if admin and student have the same username , it will select the first one to register 
#by defsult
#idea to improve this is to restrict user to register with same username
#by now i also have not cater the problem if when trying to login , if tthere doesnt exist any username with that name 
#this code will give error if thats the case , i will have to handle those errors
#if when selecting options , make sure it the code redirect to the first page if the user enters something other than an integer
#exit option is not working at some places
#choose_edit ---> loop not working properly
#some fucntions not working proprely, like when admin/student tries to login as student/admin it the code exachnges data between two json files 
 

