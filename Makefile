
venv:
	virtualenv --python=python3 venv

clean:
	rm -rf venv

develop: venv
	. venv/bin/activate; \
	python setup.py develop; \
	pip install mypy-lang

install: develop

noypc:
	find . -name '*.pyc' | xargs rm -f || true

