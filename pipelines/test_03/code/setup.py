from setuptools import setup, find_packages
setup(
    name = 'test_03',
    version = '1.0',
    packages = find_packages(include = ('test_03*', )) + ['prophecy_config_instances.test_03'],
    package_dir = {'prophecy_config_instances.test_03' : 'configs/resources/test_03'},
    package_data = {'prophecy_config_instances.test_03' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = test_03.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
