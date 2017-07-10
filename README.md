# Twitter-Personality-Analyzer
## Requirements
1. Python 2.7
2. Python packages 
	* python-twitter 
		```
		pip install python-twitter
		```
	* watson-developer cloud
		```
		pip install watson-developer-cloud
		```
3. Twitter API credentials
4. IBM Bluemix credentials

## How to run
1. Add credentials into analyze.py (lines 10-13, 34-35)
2. Enter Twitter handle (line 19)
	* Do not forget the '@'!
3. Run
	``` 
	python analyze.py
	```

## TODO
1. Create Django app
2. Integrate analyze.py to app
3. Visualize results on app using D3.js