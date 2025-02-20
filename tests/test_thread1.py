from hamcrest import assert_that, equal_to


class TestThread1():
    def test_it_works(self):
        assert_that(1, equal_to(1))
