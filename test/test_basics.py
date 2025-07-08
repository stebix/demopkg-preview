"""
Basic unit tests for the full package.
"""

class TestBasics:
    """
    Test class for basic functionality.
    """

    def test_import(self):
        """
        Test if the package can be imported without errors.
        """
        import demopkg  # noqa: F401

    def test_returns_five_ones(self):
        from demopkg.basics import returns_ones
        expected = [1, 1, 1, 1, 1]
        result = returns_ones(5)
        assert result == expected, f'Expected {expected}, got {result}'


    def test_returns_six_sixes(self):
        from demopkg.basics import returns_ones
        expected = [1, 1, 1, 1, 1, 1]
        result = returns_ones(6)
        assert result == expected, f'Expected {expected}, got {result}'