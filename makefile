init : 
	python3 -m venv venv
	source venv/bin/activate
	pip3 install -r requirements.txt

run : 
	uvicorn app.main:app --reload

.PHONY: init run
