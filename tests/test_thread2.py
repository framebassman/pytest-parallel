from hamcrest import assert_that, equal_to


class TestThread2():
    def test_it_works(self, logger):
        logger.info("Logs from TestThread2")
        assert_that(1, equal_to(1))
