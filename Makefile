clean:
	rm -rf build/
	rm -rf dist/
	rm -rf python_geoacumen_city.egg-info

publish-test:
	@echo "Publishing to TestPyPI"
	@echo "Are you sure? [y/N] " && read ans && [ $${ans:-N} == y ]
	python3 setup.py sdist bdist_wheel
	twine upload --repository test dist/*

publish-pypi:
	@echo "Publishing to PyPI"
	@echo "ARE YOU ABSOLUTELY SURE? [y/N] " && read ans && [ $${ans:-N} == y ]
	python3 setup.py sdist bdist_wheel
	twine upload --repository pypi dist/*