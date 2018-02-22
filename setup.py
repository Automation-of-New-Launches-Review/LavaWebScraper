from cx_Freeze import setup,Executable
setup(name='scrapper',
      version='0.1',
      description='scrap',
      executables=[Executable('billion.py')])
