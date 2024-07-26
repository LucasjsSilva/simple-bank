import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = Account(initial_balance=100)
        self.account2 = Account(initial_balance=100)
        self.account3 = None
    def test_withdraw_success(self):
        self.account1.withdraw(50)
        self.assertEqual(self.account1.balance, 50)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(150)

    def test_withdraw_negative_amount_and_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(-10)
        with self.assertRaises(ValueError):
            self.account1.withdraw(0)
      
    def test_deposit_success(self):
        self.account1.deposit(50)
        self.assertEqual(self.account1.balance, 150)
    
    def test_deposit_negative_amount_and_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(-10)
        with self.assertRaises(ValueError):
            self.account1.deposit(0)
    
    def test_transfer_success(self):
        self.account1.transfer(50, self.account2)
        self.assertEqual(self.account1.balance, 50)
        self.assertEqual(self.account2.balance, 150)

    def test_transfer_negative_and_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(-10, self.account2)
        with self.assertRaises(ValueError):
            self.account1.transfer(0, self.account2)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(150, self.account2)

    def test_transfer_invalid_destination_account(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(50, self.account3)

if __name__ == '__main__':
    unittest.main()
