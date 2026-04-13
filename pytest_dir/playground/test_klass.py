class TestSampleClass:
    def test_always_pass(self):
        assert True

    def test_always_fail(self):
        assert "a" in "coale"
