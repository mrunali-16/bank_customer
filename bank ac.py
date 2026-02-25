customer = {}
def add_customer (c_account,name,balance):
    if c_account in customer:
        print ("customer already exists!")
    else:
        customer[c_account]={"name":name,"balance":balance}
        print ("account added successfully!")
add_customer(101,"john",10000)
def view_account():
    print(".......account details of customer.......")
for c_account,info in customer.items():
    print(f"account_number:{c_account} | name:{info["name"]} | balance:{info["balance"]}")
    view_account()
def search_customer(account_number):
        print("....customer details using account number.....")
        if account_number in customer:
             print(f"name:{customer[account_number]["name"]} |balance:{customer[account_number]["balance"]}")
        else:
             print("customer is not exists!!!")



def main():
     while True:
          print("1.Add customer\n2.view customer Table\n3.Search customer\n4.Exit")

          choose_number = int(input("choose what you want to do:"))
          if choose_number == 1:
               add_customer(101, "John"  , 20)
               add_customer(102, "John"  , 200)
               add_customer(103, "John"  , 2000)
               add_customer(104, "John"  , 20000)
          if choose_number == 2:
               view_account()
          if choose_number == 3:
               account_number = int(input("Enter Account Number : "))
               search_customer(account_number)   
          if choose_number == 4:
               break
main()  
               