import datetime
def calculate_age(year, month, day):
    today_day = datetime.date.today()
    dob = datetime.date(year,month,day)
    age = int(((today_day- dob).days)/365)
    #print(age)
    return age

user_dob= input(" please enter your d-o-b in this format: YYYY-MM-DD \n")
dob= user_dob.split("-")
#print(dob)
year, month, day = int(dob[0]),int(dob[1]),int(dob[2])
your_age = calculate_age(year, month, day)
#print(your_age)

print( "\tHeyy Adam, let's celebrate you {a}th year Anniversary,\n\n\twishing you a day filled with joy and Laughter as you turn {a}".format(a = your_age))
print ("\nwith love and best wishes\nFrom Nunu")
