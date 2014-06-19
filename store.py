from pymongo import Connection
from pymongo import MongoClient
from gridfs import * 
from bson.objectid import ObjectId
import os
import datetime
import time
import StringIO
import threading, time
from bcolors import cprint


class GFS:
    conn = None
    db = None
    fs = None
    instance = None
    locker = threading.Lock()


    @staticmethod
    def _connect():
        if  not GFS.conn:
              try:
                 #GFS.conn = Connection("localhost",27017)
                  GFS.conn = MongoClient('localhost', 27017)
                  GFS.db = GFS.conn['test_database']
                  GFS.fs = GridFS(GFS.db,collection='cvfiles')
              except Exception as e:
                  print "Exception ==>> %s " % e
                  quit();
              

         
    def unconnect():
       disconnect()
 

    def __init__(self):
        cprint("HEADER","__init__")
        GFS._connect()
        cprint("HEADER","server info " + " * " * 40)
        cprint("HEADER",str(GFS.conn.server_info) )
        cprint("HEADER","server info " + " * " * 40)


    @staticmethod
    def getInstance():
        GFS.locker.acquire()
        try:
            GFS.instance
            if not GFS.instance:
                GFS.instance = GFS()
            return GFS.instance
        finally:
            GFS.locker.release()


#delete file
    def remove(self,name):
        GFS.fs.remove(name)

#get file list
    def list(self):
        return GFS.fs.list()



    #write file (data from GFS)
    def store_2_filesystem(filename,data):
       output = open(filename, 'wb')
       output.write(data)
       output.close()



    def store_2_db(self,name,email,phone,filepath,filetext):
       cprint("HEADER",'**************************************')
       cprint("OK",name)
       cprint("OK",email)
       cprint("OK",phone)
       cprint("OK",filepath)
       cprint("HEADER",'**************************************')
       #store file
       cprint("OK","File size : "+str(os.path.getsize( filepath )) + " bytes" )
       fileID = GFS.fs.put( open( filepath, 'rb')  )
       cprint("OK","File ID MD5 : "+str(fileID) )
### 
#       out = fs.get(fileID)
#       output = open(name+email+'.doc', 'wb')
#       output.write(out.read())
#       output.close() 
#       print out.length
### 
      #get one collection
      # print GFS.db.collection_names() 
       posts = GFS.db.cvtext
       strlist = filepath.split('.')
       filename=name+'_'+email+'_'+phone+'.'+strlist.pop()
       cprint("OK","Create new file name : "+filename)
       post = {"name": name,"email": email,"phone": phone,"filename":filename,"filetext": filetext,"fileid":fileID}
       cprint("OK","Record MD5 : "+str(posts.insert(post)) )


    def search_cv(keywords , *args):
       print args
       querystr=''
       for k in args:
          querystr=querystr+"'$regex':"+"'"+k+"'" +','

       strq = "{'filetext': {"+querystr[0:(len(querystr)-1)] + "}}"
       print strq 
       for cv in  GFS.db.cvtext.find(eval(strq)):
           print cv


##get one recorder
#posts.find_one()
#print posts.find_one({"name": "garfield"})


#Bulk Inserts
#new_posts = [{"author": "Mike","text": "Another post!","tags": ["bulk", "insert"],"date": datetime.datetime(2009, 11, 12, 11, 14)},{"author": "Eliot", "title": "MongoDB is fun","text": "and pretty easy too!","date": datetime.datetime(2009, 11, 10, 10, 45)}]
#posts.insert(new_posts)

##insert large amount data
#index=0
#start = time.time()
#for i in range (0,1000000):
#        post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
#        posts.insert(post)
#        index=index+1
#        if index % 1000 == 0 :
#                print "inserted %d post" %index
#print "inserted %d post totally" %index
#print "Elapsed Time: %s" % (time.time() - start)
#start = time.time()
#index=0
#for post in posts.find():
#        posts.remove(post)
#        index=index+1
#        if index % 1000 == 0 :
#                print "remove %d post" %index
#print "removed %d post totally" %index
#print "Elapsed Time: %s" % (time.time() - start)
