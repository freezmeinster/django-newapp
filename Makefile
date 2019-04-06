build_wheel:
	@python setup.py bdist_wheel
upload:
	@python -m twine upload dist/*
