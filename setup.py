from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

setup(
    name = 'greeter',
    packages = ['greeter'],
    version = '1.0',
    author = 'ts123',
    url = 'https://github.com/ts123',
    cmdclass = {'test': PyTest},
    ) 

