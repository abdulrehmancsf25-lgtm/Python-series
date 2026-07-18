# Problem-5: Write a program with class Bill.
# The users have the option to pay the bill either by cheque or by cash. 
# Use the inheritance to model this situation.
class Bill:
    def __init__(self,amount):
        self.__amount = amount 
    # bill getter 
    def amount_to_pay(self):
        return self.__amount

# inheritance 
class cash_pay(Bill):
    def pay_bill(self):
        print("Bill payed through cash : ${}".format(self.amount_to_pay()))

class cheque_pay(Bill):
    def pay_bill(self):
        print("Bill payed through cheque : ${}".format(self.amount_to_pay()) )


# test
pay_1 = cash_pay(5000)
pay_2 = cheque_pay(5000)

pay_1.pay_bill()
pay_2.pay_bill()