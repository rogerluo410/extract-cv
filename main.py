import sys
from extractfactory import ExtractFactory
from bcolors import cprint

def main():

  if(len(sys.argv)!= 2):
    bcolors.cprint('WARNING',"usage: python main.py input_file")
    sys.exit(1)

  filename = sys.argv[1]
  cprint('HEADER',"Input file is "+filename)
  filelist = sys.argv[1].split('.')
  cprint('HEADER',"File suffix is "+filelist[-1])
  efactory = ExtractFactory(filename,filelist[-1])
  efactory.extract_control()

if __name__ == "__main__":
   main()

