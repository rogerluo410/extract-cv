import os
import sys
import re

def main():

  if(len(sys.argv)!= 2):
    sys.exit(1)

  filename = sys.argv[1]
  content = os.system('pdftotext '+filename+' '+filename+'.txt' )
  print content

  str1 = 'rwerweew   (Tel) 408-323-9197 rewr'
  test =  re.search('([\(\+])?([0-9]{1,3}([\s])?)?([\+|\(|\-|\)|\s])?([0-9]{2,4})([\-|\)|\.|\s]([\s])?)?([0-9]{2,4})?([\.|\-|\s])?([0-9]{4,8})?([\.|\-|\s])?([0-9]{3,8})',str1)
  print test.group()
 
  str2 = 'Personal Information: Name: Lei Xia Gender: Male Working Experience: 1 years'
  #for i in range(0,len(str2)):
       
  test2 = re.search('(name|Name|NAME)+',str2)
  print test2.group()
  test1 = re.search('(name|Name|NAME)+([\:|\s])+([A-Z]{1}[a-z]+\s{1})([A-Z]{1}[a-z]+)',str2)
  print test1.group()


if __name__ == "__main__":
   main()

