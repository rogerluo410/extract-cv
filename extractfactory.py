#file name : extractfactory.py
#created at : 2014.06.17
#functionality : control extraction categories
import sys
from extract import ExtractPdf,ExtractDocx,ExtractTxt,ExtractDoc
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
        if self.suffix == 'pdf':
          cprint("HEADER","Enter extract pdf...")
          pdf = ExtractPdf(self.filename)
          return_list = pdf.extract_text_from_pdf1()
          if return_list[0]==0:
            print pdf.get_all_text()
            cprint('OK',return_list[1])
            #extract name, email, phone number
            info_list = self.extract_info(pdf.text)
            #import mongoDB
            if info_list[0] and info_list[1] and info_list[2]:
               gfs.store_2_db(info_list[0],info_list[1],info_list[2],self.filename,pdf.text)

          elif return_list[0]==-1:
            cprint('WARNING',return_list[1]+',make sure the pdf file is not produced by scanned images and no space/special characters in file name as well.')
          else :
            cprint('FAIL',return_list[1])

        elif self.suffix == 'docx':
          cprint("HEADER","Enter extract docx...")
          docx = ExtractDocx(self.filename)
          return_list = docx.extract_text_from_docx1()
          if return_list[0]==0:
            print docx.get_all_text()
            cprint('OK',return_list[1])
            #extract name, email, phone number
            info_list = self.extract_info(docx.text)
            #import mongoDB
            if info_list[0] and info_list[1] and info_list[2]:
               gfs.store_2_db(info_list[0],info_list[1],info_list[2],self.filename,docx.text)

          elif return_list[0]==-1:
           cprint('WARNING',return_list[1]+',make sure the file is not empty and no space/special characters in file name as well.')
          else :
            cprint('FAIL',return_list[1])

        elif self.suffix == 'txt':
           cprint("HEADER","Enter extract txt...")
           txt = ExtractTxt(self.filename)
           return_list = txt.extract_text_from_txt()
           if return_list[0]==0:
              #print txt.get_all_text()
              cprint('OK',return_list[1])
              #extract name, email, phone number
              info_list = self.extract_info(txt.text)
              #import mongoDB
              if info_list[0] and info_list[1] and info_list[2]:
                gfs.store_2_db(info_list[0],info_list[1],info_list[2],self.filename,txt.text)

           elif return_list[0]==-1:
             cprint('WARNING',return_list[1]+',make sure the file is not empty and no space/special characters in file name as well.')
           else :
             cprint('FAIL',return_list[1])

        elif self.suffix == 'doc':
           cprint("HEADER","Enter extract doc...")
           doc = ExtractDoc(self.filename)
           return_list = doc.extract_text_from_doc()
           if return_list[0]==0:
              print doc.get_all_text()
              cprint('OK',return_list[1])
              #extract name, email, phone number
              info_list = self.extract_info(doc.text)
              #import mongoDB
              if info_list[0] and info_list[1] and info_list[2]:
                 gfs.store_2_db(info_list[0],info_list[1],info_list[2],self.filename,doc.text)
           elif return_list[0]==-1:
                cprint('WARNING',return_list[1]+',make sure the file is not empty and no space/special characters in file name as well.')
           else :
                cprint('FAIL',return_list[1])
        else :
           cprint('WARNING',"Warning:Input a wrong formated file,currently,this tool only accept .pdf/.docx/.doc/.txt")

    def extract_info(self,text):
          name = 'tester'
          phonenum = ''
          email = ''
          #extract phone number
          ps = PhoneStrategy(text)
          phone = ps.extract_phone_interface()
          if phone:
               cprint("OK","Phone:"+phone)
               phonenum = phone
          else:
               cprint("FAIL","Extract phone number failed")

          #extract email
          es = EmailStrategy(text)
          email_tmp = es.extract_email_interface()
          if email_tmp:
               cprint("OK","Email:"+email_tmp)
               email = email_tmp
          else:
               cprint("FAIL", "Extract email failed")

          #extract name
          ns = NameStrategy(text)
          name_tmp = ns.extract_name_interface()
          if name_tmp:
              cprint("OK","Name:"+name_tmp)
              name = name_tmp
          else:
               cprint("FAIL", "Extract name failed") 
          return [name,email,phonenum]
