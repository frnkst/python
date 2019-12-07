# pip install pytest
# Run the file with 'pytest -q 24_a_simple_test.py'

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
