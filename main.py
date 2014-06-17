import sys
import extractfactory
import bcolors

def main():

  if(len(sys.argv)!= 2):
    bcolors.cprint('WARNING',"usage: python main.py input_file")
    sys.exit(1)

  filename = sys.argv[1]
  bcolors.cprint('HEADER',"Input file is "+filename)
  filelist = sys.argv[1].split('.')
  bcolors.cprint('HEADER',"File suffix is "+filelist[-1])
  efactory = extractfactory.Extractfactory(filename,filelist[-1])
  efactory.extract_control()

if __name__ == "__main__":
   main()

