#file name : extractfactory.py
#created at : 2014.06.17
#functionality : control extraction categories

import extract
import bcolors

class Extractfactory:

    def __init__(self,filename,suffix):
        self.filename = filename
        self.suffix = suffix

    def extract_control(self):
        if self.suffix == 'pdf':
          bcolors.cprint("HEADER","Enter extract pdf...")
          pdf = extract.ExtractPdf(self.filename)
          return_list = pdf.extract_text_from_pdf()
          if return_list[0]==0:
            print pdf.get_all_text()
            phone = pdf.extract_phonenum_from_text()
            if phone[0] == 0:
               print "phone:"+phone[1]
            else:
               print "extract phone number failed"
            email = pdf.extract_email_from_text()
            if email[0] == 0:
               print "email:"+email[1]
            else:
               print "extract email failed"
            bcolors.cprint('OK',return_list[1])
          elif return_list[0]==-1:
            bcolors.cprint('WARNING',return_list[1]+',make sure the pdf file is not produced by images.')
          else :
            bcolors.cprint('FAIL',return_list[1])

        elif self.suffix == 'docx':
          bcolors.cprint("HEADER","Enter extract docx...")
          docx = extract.ExtractDocx(self.filename)
          return_list = docx.extract_text_from_docx()
          if return_list[0]==0:
            print docx.get_all_text()
            phone = docx.extract_phonenum_from_text()
            if phone[0] == 0:
               print "phone:"+phone[1]
            else:
               print "extract phone number failed"
            email = docx.extract_email_from_text()
            if email[0] == 0:
               print "email:"+email[1]
            else:
               print "extract email failed"
            bcolors.cprint('OK',return_list[1])
          elif return_list[0]==-1:
            bcolors.cprint('WARNING',return_list[1]+',make sure the file is not empty.')
          else :
            bcolors.cprint('FAIL',return_list[1])

        elif self.suffix == 'txt':
           bcolors.cprint("HEADER","Enter extract txt...")
           txt = extract.ExtractTxt(self.filename)
           return_list = txt.extract_text_from_txt()
           if return_list[0]==0:
             print txt.get_all_text()
             phone = txt.extract_phonenum_from_text()
             if phone[0] == 0:
               print "phone:"+phone[1]
             else:
               print "extract phone number failed"
             email = txt.extract_email_from_text()
             if email[0] == 0:
               print "email:"+email[1]
             else:
               print "extract email failed"
             bcolors.cprint('OK',return_list[1])
           elif return_list[0]==-1:
             bcolors.cprint('WARNING',return_list[1]+',make sure the file is not empty.')
           else :
             bcolors.cprint('FAIL',return_list[1])

        elif self.suffix == 'doc':
           bcolors.cprint("HEADER","Enter extract doc...")
           print "Pending.."
        else :
           bcolors.cprint('WARNING',"Warning:Input a wrong formated file,currently,this tool only accept .pdf/.docx/.doc/.txt")
