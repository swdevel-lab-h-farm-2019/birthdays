import unittest
import birthdays
import os

class TestBirthdays(unittest.TestCase):
    
    def setUp(self):
        self.temporary_file = "/tmp/emptyfile"
        f = open(self.temporary_file, 'w')
        f.close()
  
    def test_reject_name_if_lower_case(self):
        #Assume
        name = "donald trump"

        #Action
        result = birthdays.name_is_valid(name)

        #Assert
        self.assertFalse(result)

    def test_reject_name_if_too_long(self):
        #Assume
        name = "Thisnameexceedstwentycharacters"

        #Action
        result = birthdays.name_is_valid(name)

        #Assert
        self.assertFalse(result)

    def test_accept_name_if_in_birthdays(self):
        #Assume
        name = 'Donald Trump'

        #Action
        result = birthdays.name_is_valid(name)

        #Assert
        self.assertTrue(result)

    def test_just_the_surname(self):
        #Assume
        name = 'Albert Einstein'

        #Action
        result = birthdays.just_the_surname(name)

        #Assert
        self.assertEqual(result,"Einstein")

    def tearDown(self):
        os.remove(self.temporary_file)



if __name__ == '__main__':       # When running the module directly, run the code within the conditional
    unittest.main()
