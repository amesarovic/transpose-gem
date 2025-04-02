from setuptools import setup, find_packages
setup(
    name = 'andre-transpose',
    version = '1.0',
    packages = find_packages(include = ('andretranspose*', )) + ['prophecy_config_instances.andretranspose'],
    package_dir = {'prophecy_config_instances.andretranspose' : 'configs/resources/andretranspose'},
    package_data = {'prophecy_config_instances.andretranspose' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = andretranspose.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
