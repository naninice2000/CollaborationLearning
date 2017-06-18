We are going to learn how to create test framework with simple example. 

Building page object model. 
Test data readers from csv file
Test configuration reader from json file. 
Building test cases using pytest, selenium. 


Example we are going to consider www.twitter.com 


Folder Structure: 
data - test data will be place in this directory.
test - directory in which all test scripts will be there. 
lib - all utility python modules will be in this directory./ 


**********************************************
Setup Required: 
**********************************************
pip install pytest 
pip install selenium


How to run test script? 
pytest <testscrit_file>
$: pytest test_script.py


**********************************************
How to create test cases? 

class <Test Class Name>:
	
	def test_<test_module_name>(self):
		statement1 
		statement2
		assert <actual_result> = <expected_result>

**********************************************

