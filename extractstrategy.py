#filename : extractstrategy.py
#created at : 2014.06.18
#functionality : using several approaches to extract name,email,phone number from text.

from timeout import timeout 
from bcolors import cprint
import re

class NameStrategy:

     def __init__(self,text):
         self.text = text

     def extract_name(self):
         print "pending..."

class EmailStrategy:

      def __init__(self,text):
          self.text = text
      
      @timeout(120)
      def extract_email_by_re(self):
         email = ''
         try:
           emailgrp = re.search("(\w+-*[.|\w]*)*@(\w+[.])*\w+",self.text)
           if emailgrp:
              email = emailgrp.group()
         except Exception,e:
           cprint("FAIL","Seaching email timeout,maybe there is no email info in this resume,please check it by yourself.")
         #if emailgrp:
            #email = emailgrp.group()
            #check1: the first letter would be digit
            #email_test_1 = emailgrp.group()
            #email_test_2 = ''
            #for i in range(0,len(email_test_1)):
            #  if not email_test_1[i].isdigit():
            #       email_test_2 = email_test_1[i:]
            #       break
            #check2:Top level domain check,remove other unnecessary characters.
            #email_slt = email_test_2.split('.')
            #top_level_domain = email_slt[-1]
            #domain_test = re.search("(?:[A-Z]{2}|cn|com|edu|us|tw|hk|net|uk|ws|de)",top_level_domain)  
            #if domain_test:
            #   if len(domain_test.group()) == len(top_level_domain):
            #       email = email_test_2
            #   else:
            #       email = email_slt[0] +'.'+ domain_test.group()
         
         return email   

      def extract_email_interface(self):
          email = self.extract_email_by_re()
          return email

                     
class PhoneStrategy:

      def __init__(self,text):
          self.text = text

      def extract_phone_by_re(self):
          phonegrp = re.search("([\(\+])?([0-9]{1,3}([\s])?)?([\+|\(|\-|\)|\s])?([0-9]{2,4})([\-|\)|\s]([\s])?)?([0-9]{2,4})+([\-|\s])?([0-9]{4,8})?([\-|\s])?([0-9]{3,8})",self.text)
          phone = ''
          if phonegrp:
               phone = phonegrp.group()

          return phone

      #directly read 11 numbers as a Chinese phone number
      def extract_phone_by_read11(self):
          phone_num_cnt = 0  #count phone number
          str_num_cnt = 0 #count string number
          phone = ''
          for i in range(0,len(self.text)):
             if self.text[i].isdigit() and self.text[i] == '1' :
                 phone_num_cnt = phone_num_cnt + 1
                 str_num_cnt = str_num_cnt + 1
                 for j in range(i+1,len(self.text)):
                      str_num_cnt = str_num_cnt + 1
                      if self.text[j].isdigit():
                         phone_num_cnt = phone_num_cnt +1
                      elif self.text[j].isspace() or self.text[j] == '-':
                         pass
                      else :
                          phone_num_cnt = 0
                          str_num_cnt = 0
                          break
                      
                      if phone_num_cnt == 11:
                         phone = self.text[i:i+str_num_cnt]
                         break
             if phone_num_cnt == 11:
                break
          phone1 = ''
          if phone :
             for i in range(0,len(phone)):
               if not phone[i].isspace() and not phone[i] == '-' :
                  phone1 = phone1 + phone[i]
          #Verify
          phone2 = ''
          if re.match("(?<!\\d)(?:(?:1[3458]\\d{9})|(?:861[358]\\d{9}))(?!\\d)",phone1):
              phone2 = phone1

          return phone2

      def extract_international_phone(self):
          phonegrp = re.search("1?\s*\W?\s*([2-9][0-8][0-9])\s*\W?\s*([2-9][0-9]{2})\s*\W?\s*([0-9]{4,8})(\se?x?t?(\d*))?",self.text)
          phone = ''
          phone1 = ''
          if phonegrp:
               phone = phonegrp.group()

          return phone 
          
           
      def extract_phone_interface(self):
          phone = self.extract_phone_by_re()
          #failed to extract phone with regular expression
          #if not phone:
          #  phone = self.extract_phone_by_read11()
          #if not phone:
          #  phone = self.extract_international_phone()
          phone1 = ''
          if phone :
             for i in range(0,len(phone)):
               if not phone[i].isspace() :
                  phone1 = phone1 + phone[i]
           
          return phone1



 


  





          
