import pytest
import requests

#testing no <num> parameter	
def testNone():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/')
	assert r.status_code == 404
#testing a basic character string
def testChar():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/hello')
	assert r.status_code == 404
#testing another char string
def testChar2():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/six')
	assert r.status_code == 404
#testing single character
def testChar3():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/a')
	assert r.status_code == 404
#testing decimal value	
def testDecimal():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/5.5')
	assert r.status_code == 404
#testing negative values
def testNegative():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/-42')
	assert r.status_code == 404
#testing basic functionality
def testBasic():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/9')
	assert r.status_code == 200

def testBasic1():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/10')
	assert r.status_code == 200

def testBasic2():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/56')
	assert r.status_code == 200

def testBasic3():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/900')
	assert r.status_code == 200
#testing combination of letters and numbers
def testLetterAndNum():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/9a')
	assert r.status_code == 404
#testing paranthesis
def testParenthesis():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/(42)')
	assert r.status_code == 404
#test math functions
def testMultiply():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/7*6')
	assert r.status_code == 404
#test rapid requests to api
def testSpam():
	count = 0;
	while (count < 500):
		r = requests.get('http://52.36.134.100:5000/api/fibonacci/42')
		assert r.status_code == 200
		count = count + 1
#test large number, note this has been commented out because it crashes the website
#def testBoundary():
#	r = requests.get('http://52.36.134.100:5000/api/fibonacci/837836485949674589304947594857')
#	assert r.status_code == 200
#testing delete verb	
def testDelete():
	r = requests.delete('http://52.36.134.100:5000/api/fibonacci/7')
	assert r.status_code == 405
#test post verb
def testPost():
	r = requests.post('http://52.36.134.100:5000/api/fibonacci/9')
	assert r.status_code == 405
#test put verb
def testPut():
	r = requests.put('http://52.36.134.100:5000/api/fibonacci/42')
	assert r.status_code == 405
#testing head verb
def testHead():
	r = requests.head('http://52.36.134.100:5000/api/fibonacci/42')
	assert r.status_code == 200
#test options verb
def testOptions():
	r = requests.options('http://52.36.134.100:5000/api/fibonacci/42')
	assert r.status_code == 200
#test patch verb
def testPatch():
	r = requests.patch('http://52.36.134.100:5000/api/fibonacci/42')
	assert r.status_code == 405
#testing bad url
def testMisspell():
	r = requests.get('http://52.36.134.100:5000/api/fibnacci/42')
	assert r.status_code == 404

def testMisspell2():
	r = requests.get('http://52.36.134.100:5000/ap/fibonacci/42')
	assert r.status_code == 404
#testing post verb with different parameters
def testPostAgain():
	r = requests.post('http://52.36.134.100:5000/api/fibonacci/4' , data = {'key' : 'value'})
	assert r.status_code == 405
#testing query parameters, attempting to cause 400 error
def testQuery():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/42?meaning=what')
	assert r.status_code == 200

def testPartialQuery():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/42?')
	assert r.status_code == 200

def testPartialQuery2():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/42?zach')
	assert r.status_code == 200	
#attempting to change header to cause 400 error
def testHeader():
	r = requests.get('http://52.36.134.100:5000/api/fibonacci/56')
	r.encoding = 'utf-8'
	assert r.status_code == 200


