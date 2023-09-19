database=[["aakash","hello@11"],["abhinav","abhinav@21"]]



def login(username,password):
    for user_detail in database:
        if user_detail[0]==username and user_detail[1]==password:
            user_detail[2]=1
            print("Login Successfull")


#testcase
user_detail=login("aakash","hello@11")
print("Status: ",user_detail[2])