from setuptools import setup, find_packages
setup(
    name = 'sql-gem-test',
    version = '1.0',
    packages = find_packages(include = ('sqlgemtest*', )) + ['prophecy_config_instances.sqlgemtest'],
    package_dir = {'prophecy_config_instances.sqlgemtest' : 'configs/resources/sqlgemtest'},
    package_data = {'prophecy_config_instances.sqlgemtest' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = sqlgemtest.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
