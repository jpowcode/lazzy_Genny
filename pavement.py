from paver.tasks import task
from paver.easy import sh

@task
def unit_tests():
	sh('nosetests --with-coverage -s seqpy_tests.py')
	
@task
def run_pylint():
	try:
		sh('pylint --msg-template="{path}:{line}:
		[{msg_id}({symbol}), {obj}] {msg}" bank/ > pylint.txt')
	except BuildFailure:
		pass
		
@needs('unit_tests',  'run_pylint')
@task
def default():
	pass
