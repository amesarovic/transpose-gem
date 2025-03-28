from setuptools import setup, find_packages
setup(
    name = 'andre-test',
    version = '1.0',
    packages = find_packages(include = ('andretest*', )) + ['prophecy_config_instances.andretest'],
    package_dir = {'prophecy_config_instances.andretest' : 'configs/resources/andretest'},
    package_data = {'prophecy_config_instances.andretest' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = andretest.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
