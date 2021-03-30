"""
Step 1 : Save file using prefix a test_functionName.py
Step 2 : Go to terminal --> $ py.test -v
        -v : Verbose --> detail message in terminal
                            OR
        Go to terminal --> $ pytest -q fileName.py
"""


def func(x):
    """
    :param x: argument from te user
    :return: function(x) + 1 value
    """
    return x + 1


def test_answer():
    """
    asert function which using to verify te function output
    :return: 'nothing'
    """
    assert func(3) == 5
