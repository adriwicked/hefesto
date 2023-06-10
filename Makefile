create-venv:
	test -d venv || python3.7 -m venv venv

test: create-venv
	. venv/bin/activate && \
	python -m unittest -v