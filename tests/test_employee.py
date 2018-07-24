# from unittest import TestCase
# from unittest.mock import patch
# from Employee import Employee
#
# def mock_test()

# class EmployeeTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.employee = Employee("Amit", "Thapa")
#
#     # def test_fullname(self):
#     #     self.assertEqual(self.employee.get_fullname(), "Amit Thapa")
#
#     # @patch("Employee.Employee._set_firstname")
#     # @patch("Employee.Employee.okay")
#     # def test_fullname_2(self, da, o):
#     #     da.return_value = "Tani"
#     #     # self.employee.__lname = "Tani"
#     #     # da.return_value = f"{da.return_value}-Tani"
#     #     self.assertEqual(self.employee.get_fullname(), "Tani Thapa")
#     #     # self.assertEqual(self.employee.get_fullname(), "Tani Thapa")
#
#
#     @patch("main.Employee.get_test", side_effect=mock_test)
#     def test_ok(self):
#         self.assertEqual(self.employee.get_test("tests"), "qa_test")

    # def test_one(self):
    #     self.employee._set_firstname("Tani")
    #     self.assertEqual(self.employee.get_fullname(), "Tani Thapa")
    #
    # def test_two(self):
    #     self.assertEqual(self.employee.get_fullname(), "Amit Thapa")
