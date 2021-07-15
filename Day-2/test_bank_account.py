
# TDD Test Driven Development 
# 1. Write a failing test 
# 2. Make the test pass 
# 3. Refactor 
# 4. Repeat 

# UNIT TESTS RULES 
# 1. Unit Test should be independent 
# 2. Unit Test should NEVER wait for human input 
# 3. Unit Tests should be repeatable 

# WHAT TO TEST 
# 1. DOMAIN/MODELS/BUSINESS LOGIC 
# 2. You should write UI Test for your webpages, automated tests, integration tests 
# 3. Code Coverage refers to the code which is under test

# importing unitest module which contains classes/functions to help us test 
from bank_account import BankAccount 
import unittest 

class CalculaterTests(unitest.TestCase): 

    #def test_should_be_able_to_add_numbers(self): 
     #   calculator = Calculator() 
        ## a = int(input("Enter first number: "))  DON'T TAKE INPUT INSIDE TEST
     #   result = calculator.add(2,5)
     #   self.assertEqual(7, result)

class BankAccountTests(unittest.TestCase):

    # setUp is fired before running EACH TEST 
    def setUp(self): 
        self.bank_account = BankAccount()

    # make sure the test function begins with test word 
    def test_deposit_money_in_bank(self): 
        self.bank_account.deposit(100)
        self.assertEqual(100, self.bank_account.balance)
    
    def test_withdraw_money_from_bank(self): 
        self.bank_account.deposit(100)
        self.bank_account.withdraw(50)
        self.assertEqual(50, self.bank_account.balance)

    # tearDown is called after EACH TEST
    def tearDown(self): 
        print("TEAR DOWN")

unittest.main() # this is to run the test
