from setuptools import setup, find_packages
setup(
    name = 'transpose-gem-pipeline',
    version = '1.0',
    packages = find_packages(include = ('transposegempipeline*', )) + ['prophecy_config_instances.transposegempipeline'],
    package_dir = {'prophecy_config_instances.transposegempipeline' : 'configs/resources/transposegempipeline'},
    package_data = {'prophecy_config_instances.transposegempipeline' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = transposegempipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
