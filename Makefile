install:
		pip install --upgrade pip &&\
				pip install -r requirements.txt &&\
				python download_model.py

test:
		python -m pytest -vv test_main.py

format:
		black *.py


lint:
		pylint --disable=R,C main.py

all: install lint format test
