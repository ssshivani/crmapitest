import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

SUITE = {
    "description": "My suite"
}

@lcc.test("My test")
def my_test():
    check_that("value", "foo", equal_to("foo"))
