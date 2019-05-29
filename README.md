###STAR GROUP AUTOMATION FRAMEWORK

An automated test framework checking basic snapshot of Star Group's internal Sky Bet Trading Engine.
The tests have been written in **Python 3.7** using Python's unittest test framework and Python requests
library for API calls.


To run the tests:

1. create a Python virtual environment. To do that, you need to have Python 3.7 installed. Then just follow this tutorial:
https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3
    
    Remember to switch to the virtual environment and run the API suite that generates fixtures
2. move to the project directory and execute the command 
        
        pip install -r requirements.txt
        
    This will install all the project dependencies required to run the tests.
    
3. on command line, after moving to the project directory, run the following command. It will run all the tests:
        
        python -m unittest
        
Then the tests should run.

