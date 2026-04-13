# Fixtures
import pytest

# @pytest.mark.smoke
def test_initialCheck(preWork):
    print("First test")


def test_secondCheck(preWork):
    assert 3 == 3
    print("Second test")

# @pytest.mark.smoke    
def test_thirdCheck(preWork):
    assert 3 == 3
    print("Third test")