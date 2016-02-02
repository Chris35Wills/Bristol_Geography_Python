# Python testing 

Notes adapted from: http://katyhuff.github.io/python-testing/04-units.html
Further reading: http://pythontesting.net/framework/nose/nose-introduction/
Material: http://katyhuff.github.io/python-testing/index.html

Unit tests are essentially functions which compare observed and expected values e.g.

	def test_ints():
	    num_list = [1, 2, 3, 4, 5]
	    obs = mean(num_list)
	    exp = 3
	    assert obs == exp

The above function test_ints will fail should obs (observed) not be equal to exp (expected) due to the use of the assert command.

For any function you develop, you can write a set of appropriate tests and run them individually - perhaps putting all test functions into a module and going: module.test_1(), module.test_2(), module.test_n() ... However, this manual approach is unnecessary (and boring and inefficient and...)

## A better way... nosetests

Make two .py files - one containing a function called mean (see numeric_functions.py) and one a list of functions (see test_mean.py)

The command line tool *nosetests* is a useful way of running your tests as it uses the python package [nose](https://nose.readthedocs.org/en/latest/) to search and run all python tests within a directory - that is, all files and functions containing the string [Tt]est[-_]*

NB: you don't need to be in Python to do this, in a bash terminal, just tell nosetests where to work e.g.:

	> nosetests Bristol_Geography_Python/testing/

This then runs all tests it can find and prints out a log telling you whther the tests passed or failed.

If things fail, work out why, fiux them and re-run the tests using nosetests again.

## Enter the Travis/Git tag team

Now this is the cool part, say you are building soemthing bigger than our previously established "mean function" module with code changing all the time as you develop it. If you have a number of basic functions, you need to know that they are still workign as expected and consequently you need to be testing your code frequently.

For starters, in such a situation you need version control for reasons including: somewhere that log specific changes, opportunity to revert to old versions, have a backup in case your computer goes down etc. etc. (see [here](http://chryswoods.com/beginning_git/index.html) for some more info).

Assuming you have github, adding your code each day, you can sync this with Travis which can then run your tests automatically, emailing you the test results.

1. Go to [https://travis-ci.org](https://travis-ci.org) 
..- can sign in with github
..- go to your profile
..- **tick** which repo you want to watch

2. You need another file in your repo to instruct travis what to do each time you commit something - call this ".travis.yml" - here you'll tell travis what language and version you want it to deal with for a given repo that it is watching e.g.

	.travis.yml

	language: python
	python:
	    - "2.7"
	    - "nightly"
	install:
	    - "pip install -r requirements.txt"
	script: nosetests

3. Another file is also required to tell travis what needs to be installed to run your tests e.g.

	requirements.txt

	    nose
	    numpy

4. Add, commit and push your .travis.yml and requirments.txt files to the github repo you have asked travis to watch