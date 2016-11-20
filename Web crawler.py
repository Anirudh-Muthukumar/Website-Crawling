import re,sys
from mechanize import Browser
from urllib2 import *
from bs4 import BeautifulSoup
import mechanize
br=Browser()
br.open("http://www.tccl.co.in")
assert br.viewing_html()
print br.title()
i=1
br.select_form(nr=0)
br["name"]="tdn126"
br["pass"]="cable@24"
login=br.submit()
print "\nLogged into TCCL successfully"

ch=input("1.Disconnection\n2.Reconnection\n3.Exit\nEnter the choice : ")
if ch==1 or ch==2:
    conn=br.open("http://www.tccl.co.in/customer/connection")
    print br.title()

    br.select_form(nr=0)
    box=raw_input("Please enter box no.: ")
    br["serial"]=box
    conn=br.submit()
    i=1
    suggested_box=[]
    suggested_name=[]
    suggested_status=[]
    soup=BeautifulSoup(conn.read(),"html.parser")
    rows=soup.findAll('tr')
    try :
        for i in range(1,len(rows)):
            cells = rows[i].findAll('td')
            suggested_box.append(cells[5].text)
            suggested_name.append(cells[1].text)
            suggested_status.append(cells[2].text)
    except IndexError:
        print "\n\tNo customer found!!!\n"
        br.open("http://www.tccl.co.in/user/logout")
        print "Logged out!!!\n"
        sys.exit(0)
    i=1
    
    if len(suggested_box)>0:
        print "\nAvailable customers :"
        print "\nNo "+"Customer name".ljust(23)+"Box no".rjust(10)+" Status".rjust(12)
        for box in suggested_box:  
            print str(i).rjust(2),suggested_name[i-1].ljust(23),box.rjust(11),
            print suggested_status[i-1].rjust(8)
            i+=1
        cust_ch=input("Enter the desired customer : ")
        if(cust_ch not in range(1,i)):
            print "Invalid choice!!!\n"
            br.open("http://www.tccl.co.in/user/logout")
            print "Logged out!!!\n"
    else:
        print "No customer found!!!\n"
        br.open("http://www.tccl.co.in/user/logout")
        print "Logged out!!!\n"
        sys.exit(0)
    
    try:
        i=1
        for links in br.links():
            i+=1
        customer=br.open("http://www.tccl.co.in"+links.url)
    except :
        print "\nTry again after sometime!!!!"
        br.open("http://www.tccl.co.in/user/logout")
        print "Logged out!!!\n"
        sys.exit(0)
    print br.title()
    br.select_form(nr=0)
    if ch==1:
        form=br.form
        form["reason"]=["NOPAY"]
        response=br.submit()
        print "\nBox disconnected successfully!!!\n"
    else:
        response=br.submit()
        print "\nBox reconnected successfully!!!\n"
   
    
    br.open("http://www.tccl.co.in/user/logout")
    print "\nLogged out!!\n"
    
'''    
elif ch==3:
    conn=br.open("http://www.tccl.co.in/customer/modify_package")
    print ""
    print br.title()
    br.select_form(nr=0)
    box=raw_input("Please enter box no.: ")
    br["serial"]=box
    conn=br.submit()
    
    #br.open("http://www.tccl.co.in/user/logout")
''' 
if ch==3:
    print "\n\tExiting......\n"
    br.open("http://www.tccl.co.in/user/logout")
    
if ch not in [1,2,3]:
    print "Wrong choice!!!\n"
    br.open("http://www.tccl.co.in/user/logout")


#print "Logged out\n!!!"
