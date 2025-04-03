from setuptools import setup, find_packages
setup(
    name = 'test_01',
    version = '1.0',
    packages = find_packages(include = ('test_01*', )) + ['prophecy_config_instances.test_01'],
    package_dir = {'prophecy_config_instances.test_01' : 'configs/resources/test_01'},
    package_data = {'prophecy_config_instances.test_01' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = test_01.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
