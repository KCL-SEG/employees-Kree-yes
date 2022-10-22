"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):

    def __init__(self, name, salary, bonusCommission=0, contractCommissions=0, contractCommissionRate=0):
        super().__init__(name)
        self.salary = salary

        self.bonusCommission = bonusCommission
        self.contractCommissions = contractCommissions
        self.contractCommissionRate = contractCommissionRate

    def get_pay(self):
        return self.salary + self.bonusCommission + (self.contractCommissions * self.contractCommissionRate)

    def __str__(self):
        if (not self.bonusCommission) and (not self.bonusCommission) and (not self.contractCommissions or not self.contractCommissionRate):
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."
        elif self.bonusCommission:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contractCommissions} contract(s) at {self.contractCommissionRate}/contract. Their total pay is {self.get_pay()}."


class ContractEmployee(Employee):
    
    def __init__(self, name, contractHours, contractRate, bonusCommission=0, contractCommissions=0, contractCommissionRate=0):
        super().__init__(name)
        self.contractHours = contractHours
        self.contractRate = contractRate

        self.bonusCommission = bonusCommission
        self.contractCommissions = contractCommissions
        self.contractCommissionRate = contractCommissionRate

    def get_pay(self):
        return (self.contractHours * self.contractRate) + self.bonusCommission + (self.contractCommissions * self.contractCommissionRate)

    def __str__(self):
        if (not self.bonusCommission) and (not self.bonusCommission) and (not self.contractCommissions or not self.contractCommissionRate):
            return f"{self.name} works on a contract of {self.contractHours} hours at {self.contractRate}/hour. Their total pay is {self.get_pay()}."
        elif self.bonusCommission:
            return f"{self.name} works on a contract of {self.contractHours} hours at {self.contractRate}/hour and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.contractHours} hours at {self.contractRate}/hour and receives a commission for {self.contractCommissions} contract(s) at {self.contractCommissionRate}/contract. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 150, 25, 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 120, 30, 600)
