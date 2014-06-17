#file name : bcolors.py
#created at : 2014.06.17
#functionality : print in terminal with colors

class bcolors:
    HEADER = '\033[94m'
    OKBLUE = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def cprint(level , content):
    if content > 0 :
      if level =='HEADER':
        print bcolors.HEADER + '[HEADER]' + content + bcolors.ENDC
      elif level == 'OK':
        print bcolors.OKGREEN + '[SUCCESS]' + content + bcolors.ENDC
      elif level == 'WARNING':
        print bcolors.WARNING + '[WARNING]' + content + bcolors.ENDC
      elif level == 'FAIL':
        print bcolors.FAIL + '[FAIL]' + content + bcolors.ENDC
