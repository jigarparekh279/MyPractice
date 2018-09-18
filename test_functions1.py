import functions
from mock import *
#from mock patch, Mock
import time 

def test_awesome_function():
	expected_value = 412
	actual_value = functions.awesome_function()
	assert expected_value == actual_value

def test_text_analysis():
	wc = functions.do_text_analysis()
	return wc
	
# Fake calling to make testing faster
#@patch('functions.download_text_from_web')
#def test_text_analysis(mock_call):
#	mock_call.return_value.text = "some mock test"
#	wc = functions.do_text_analysis()
#	return wc
	
#@patch('requests.get')	
#def test_text_analysis(mock_call):
#	mock_call.return_value = Mock()
#	mock_call.return_value.text = "some mock test"
#	wc = functions.do_text_analysis()
#	return wc
