from setuptools import setup

setup(
  author           = 'Luis Mayorga',
  author_email     = 'lmo0@lm3corp.com',
  description      = 'CLI Utility',
  license          = 'LM3CORP',
  name             = 'cliutil',
  version          = '0.0.1',
  packages         = ['cliutil'],
  install_requires = [
        'Click',
        'PyYAML'
  ],
  entry_points='''
    [console_scripts]
    cliutil=cliutil.cliutil:cli
    ''',
)
