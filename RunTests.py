import unittest

dn = 'Tests'
loader = unittest.TestLoader()
suite = loader.discover(start_dir=dn, pattern=r'Test*.py', top_level_dir='.')

runner = unittest.TextTestRunner()
runner.run(suite)