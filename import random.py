import random 

print("\n OTP VERIFICATION")
otp = random.randint(100000,999999)
#random.randint used for generate random otp

print("\n Your OTP is : = ", otp)
print("OTP SEND SUCCESSFULLY !")


print("\n RECEIVER ! ")
user_otp = input("Enter Your OTP := ")

if user_otp == str(otp):
    print("\n OTP RECEVIED SUCCESSFULLY !")

else:
    print("\n WRONG OTP : ")

print("ReadyWithCode")
