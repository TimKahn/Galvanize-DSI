## Python Practice

Today we're going to be practicing working with functions.

We're also going to be playing with lists and strings.

#### Interpretting test output

1. Run the test suite. You can do this by running `make practice` in the terminal (`iTerm`) while in the day1 directory.

    You should get something that looks like this:

    ```
    py.test test/unittests_practice.py -vv
    ================================================================================ test session starts ================================================================================
    platform darwin -- Python 2.7.12, pytest-2.8.5, py-1.4.31, pluggy-0.3.1 -- /Users/NR/anaconda/bin/python
    cachedir: test/.cache
    rootdir: /Users/NR/Desktop/Galvanize/DSR Projects/Update-Tests/python-workshop/day1/test, inifile:
    collected 4 items

    test/unittests_practice.py::TestPractice::test_1_sum_ints FAILED
    test/unittests_practice.py::TestPractice::test_2_min_and_max FAILED
    test/unittests_practice.py::TestPractice::test_3_are_palindromes FAILED
    test/unittests_practice.py::TestPractice::test_4_substrings FAILED
    ...
    ```

2. Look for the part of the output that looks like this: `  
  test/unittests_practice.py::TestPractice::test_1_sum_ints FAILED
  test/unittests_practice.py::TestPractice::test_2_min_and_max FAILED
  test/unittests_practice.py::TestPractice::test_3_are_palindromes FAILED
  test/unittests_practice.py::TestPractice::test_4_substrings FAILED`

    Notice that there are 4 `FAILED`s. This is because there are 4 problems and you have failed all of them (because you haven't written any code yet!).

    If you pass a test, instead of an `FAILED`, you will have a `PASSED`.

3. For each question that's not correct, there will be some more details. Note that they won't necessarily be in the same order since `make` shows the tests in alphabetical order

4. For failed tests, look for the line which says: `AssertionError:`. Here you will see your output and the expected output.

#### Write some functions

You are going to be writing the functions that will make the tests in `test_practice.py` pass!

1. Fill in the functions according to their docstrings in `practice.py`. If you are unsure how a function is called, check the example in `test_practice.py`.

2. Once you complete them, have an instructor review your code.
