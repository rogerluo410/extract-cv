#file name : extractfactory.py
#created at : 2014.06.17
#functionality : control extraction categories
import sys
from extract import ExtractPdf,ExtractDocx,ExtractTxt
from extractstrategy import NameStrategy,EmailStrategy,PhoneStrategy
from bcolors import cprint
sys.path.append(r'./')
from store import GFS

class ExtractFactory:

    def __init__(self,filename,suffix):
        self.filename = filename
        self.suffix = suffix

    def extract_control(self):
        gfs = GFS()        
        name = "tester"
        email = ''
        phonenum = ''
        if self.suffix == 'pdf':
          cprint("HEADER","Enter extract pdf...")
          pdf = ExtractPdf(self.filename)
          return_list = pdf.extract_text_from_pdf()
          if return_list[0]==0:
            #print pdf.get_all_text()
            cprint('OK',return_list[1])
            #extract phone number
            ps = PhoneStrategy(pdf.text)
            phone = ps.extract_phone_interface()
            if phone:
               cprint("OK","Phone:"+phone)
               phonenum = phone
            else:
               cprint("FAIL" "Extract phone number failed")
           
            #extract email
            es = EmailStrategy(pdf.text)
            email_tmp = es.extract_email_interface()
            if email_tmp:
               cprint("OK","Email:"+email_tmp)
               email = email_tmp
            else:
               cprint("FAIL", "Extract email failed")

            #import mongoDB
            gfs.store_2_db(name,email,phonenum,self.filename,pdf.text)

          elif return_list[0]==-1:
            cprint('WARNING',return_list[1]+',make sure the pdf file is not produced by images.')
          else :
            cprint('FAIL',return_list[1])

        elif self.suffix == 'docx':
          cprint("HEADER","Enter extract docx...")
          docx = ExtractDocx(self.filename)
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
            cprint('OK',return_list[1])
          elif return_list[0]==-1:
            cprint('WARNING',return_list[1]+',make sure the file is not empty.')
          else :
            cprint('FAIL',return_list[1])

        elif self.suffix == 'txt':
           cprint("HEADER","Enter extract txt...")
           txt = ExtractTxt(self.filename)
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
             cprint('OK',return_list[1])
           elif return_list[0]==-1:
             cprint('WARNING',return_list[1]+',make sure the file is not empty.')
           else :
             cprint('FAIL',return_list[1])

        elif self.suffix == 'doc':
           cprint("HEADER","Enter extract doc...")
           print "Pending.."
        else :
           cprint('WARNING',"Warning:Input a wrong formated file,currently,this tool only accept .pdf/.docx/.doc/.txt")
