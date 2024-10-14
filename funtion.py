
#Example1
def CarInFo(model,year,price,mileage):
    print(f'Car_model =  {model}')
    print(f'year_of_manufacture = {year}')
    print(f'price = {price}')
    print(f'mileage = {mileage}')

    return{
        'model' : model,
        'year' : year,
        'price' : price,
        'mileage' : mileage
        
        }

print('------')
Car1=CarInFo('Tesla model', 2023, 35000, '30 MPG')
print('-------')
Car2=CarInFo('BMW model', 2024, 566000, '40 MPG')
print('------')
Car2=CarInFo('farari model', 2014, 900000, '50 MPG')


#Example2
def BankAccount(Accountholder,Accountnumber,Balance,Accounttype):
    print(f'Account_holder = {Accountholder}')
    print(f'Account_number = {Accountnumber}')
    print(f'Balance = {Balance}')
    print(f'Account_type = {Accounttype}')

    return{
        'Accountholder': Accountholder,
        'Accountnumber' : Accountnumber,
        'Balance' : Balance,
        'AccountType' : Accounttype        
        }

print('-------')
Account1=BankAccount('monisha',123456789,25000,'saving')
print('-------')
Account2=BankAccount('jayesh',123456786,1197000,'current')
print('-------')
Account3=BankAccount('abhishekh',123456799,85000,'saving')
print('----------')
Account4=BankAccount('shruti',123456776,75000,'current')