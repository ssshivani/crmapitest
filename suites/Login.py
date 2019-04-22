import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

#
# @lcc.suite("My suite")
# class mysuite:
#     @lcc.test("My test")
#     def my_test(self):
#         check_that("value", "foo", equal_to("foo"))

@lcc.suite("Login",rank = 1)
class Login:
    @lcc.test("Crm login")
    def login(self):
