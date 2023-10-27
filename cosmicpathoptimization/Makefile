MAIN = main.py
TESTMAIN = test_main.py
PY = python3

all: check_style fix_style check_types local unittest clean
	@echo "All tests passed!"

local:
	@cat ./1.in | $(PY) $(MAIN) | diff - ./1.ans
	@echo "All local tests passed!"

unittest:
ifeq ($(shell which pytest), )
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest -v --hypothesis-show-statistics --hypothesis-seed=100 $(TESTMAIN)

check_style:
	flake8 $(MAIN) --count --show-source --statistics
	flake8 $(TESTMAIN) --count --show-source --statistics

fix_style:
	autopep8 --in-place --recursive --aggressive --aggressive $(MAIN)
	autopep8 --in-place --recursive --aggressive --aggressive $(TESTMAIN)

check_types:
	mypy --disallow-untyped-defs --strict $(MAIN)
	mypy --disallow-untyped-defs --strict $(TESTMAIN)

submit:
	kattis --problem cosmicpathoptimization --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis