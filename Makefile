.PHONY: test run
test:
	python -m pytest -vvv test/
run:
	FLASK_APP=twitch_rivals/app.py flask run