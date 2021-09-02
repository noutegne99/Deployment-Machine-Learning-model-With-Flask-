import numpy as np
from flask import Flask, request,jsonify,render_template
import pickle
from selenium import webdriver
import pandas as pd
import requests 
from bs4 import BeautifulSoup as bs
import random
import re
import csv
from PIL import Image
import dhash
from PIL import ImageFilter
import random
import tldextract
import requests
from urllib.parse  import urlparse
import hashlib
from random import sample 
import sys
from flask import request
sys.setrecursionlimit(10000)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('disable-infobars')

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


def func_urlAtSymbol(url):                                    #f2
	ats = url.count('@')
	if ats >=1 :
		return -1
	else:
		return 1
####################################### Function that counts the number of dash in the domain name. ########################
def func_urlDasheSymbol(url):
	tldextractdomain=tldextract.extract(url).domain
	tldextractsubdomain=tldextract.extract(url).subdomain    #f3
	Dashe = tldextractdomain.count('-') 
	Dashe1 = tldextractsubdomain.count('-')
	if (Dashe>1 ) or (Dashe1 >=4):
		return -1
	else:
		return 1
##############  Function that checks if the domain name is an IPV4 address ##############################
def func_ipAddress(url) :
	tldextractsubdomain=tldextract.extract(url).subdomain   #f8
	tldextractdomain=tldextract.extract(url).domain
	#print(tldextractsubdomain)
	#print(tldextractdomain)
	fffff = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', tldextract.extract(url).subdomain ))
	ffff = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', tldextract.extract(url).domain))
	#print(fffff)
	#print(ffff)
	if (fffff or ffff):
		return -1
	else:
		return 1
################ Funn that checks the length of an url ##################################################
def func_urLength(url):                                      #f9
	#for j in range(len(data)):
	urlength = len(url) 
	if(urlength > 80):
		return -1
	else:
		return 1 
##### Function that checks the number of dots the resource ################################
def func_urlDotSymbol(url):                                  #f4
	dots= urlparse(url).netloc
	if dots.count('.')<= 3 :
		return 1
	else:
		return -1
#######Decision groups########################################################################
def Goodfunc_urlAtSymbol(Feature2,Feature21,Feature22):
	if (Feature2==-1 or Feature21==-1 or Feature22 ==-1):
		return -1
	else:
		return 1

def Goodfunc_urlDasheSymbol(Feature3,Feature31,Feature32):
	if (Feature3==-1 or Feature31==-1 or Feature32 ==-1):
		return -1
	else:
		return 1

def Goodfunc_urlDotSymbol(Feature4,Feature41,Feature42):
	if (Feature4==-1 or Feature41==-1 or Feature42==-1):
		return -1
	else:
		return 1

def Goodfunc_CheckpasswordCreditcard(Feature5,Feature51,Feature52):
	if (Feature5==-1 or Feature51==-1 or Feature52 ==-1):
		return -1
	else:
		return 1
def Goodfunc_MatchDomainTitle(Feature6,Feature61,Feature62):
	if (Feature6==-1 or Feature61==-1 or Feature62==-1):
		return -1
	else:
		return 1
def Good_func_NRP(Feature7,Feature71,Feature72):
	if (Feature7 == -1) or (Feature71==-1 ) or (Feature72==-1):
		return -1
	else:
		return 1
def Good_func_ipAddress(Feature8,Feature81,Feature82):
	if (Feature8 ==-1) or (Feature81==-1 ) or (Feature82==-1):
		return -1
	else:
		return 1
def  Good_func_urLength(Feature9,Feature91,Feature92):
	if ((Feature9==-1 or Feature91 ==-1 or Feature92) ==-1):
		return 1
	else:
		return -1

def hamming_distance(string1, string2): 
	distance = 0
	L = len(string1)
	for i in range(L):
		if string1[i] != string2[i]:
			distance += 1
	return distance
def concat_ints(a, b):
	return a*(10**len(str(b)))+b

def codescore1(score1): 
	if( score1 == 0 or score1>10 or score1<-10):
		score1 = -1
	else:
		score1 = 1
	return score1

def codetestscore1(testscore1):
	if( testscore1 == 0 or testscore1>5 or testscore1<-5):
		testscore1 = -1
	else:
		testscore1 = 1
	return testscore1
def func_NRP(RP1):
    if len(RP1)>=1:
        return -1
    else:
        return 1
def selct_url(links,url):
    list11=[]
    if(len(links)>=2):
        list_of_random_items=random.sample(links,2)
        newLink=list_of_random_items[0]
        newLinktext1=list_of_random_items[1]
        list11.append(newLink) 
        list11.append(newLinktext1)
    elif(len(links) ==1):
        list_of_random_items=random.sample(links,1)
        newLink=list_of_random_items[0]
        newLinktext1= url
        list11.append(newLink) 
        list11.append(newLinktext1)
    else:
        newLink= url
        newLinktext1 = url
        list11.append(newLink) 
        list11.append(newLinktext1)
        #print(list11)
    return list11
############################################ First check on the URL
def checonnection(data):
	for j in range(len(data)):
		urlj = data[j]
		try :
			request = requests.get(urlj)
			if request.status_code == 200:
				 data1.append(urlj)
		except:
			print("Fail connection")
	return data1
####### Test on the page content  ##############################
def func_CheckpasswordCreditcard3(url3):            #f6
    response3 = requests.get(url3)
    html3 = response3.text
    soup3 = bs(html3, 'lxml')
    pwdCredit3 = ([input.get('type') for input in soup3.findAll('input', attrs={'type': re.compile("^idcard")} )] or
    [input.get('type') for input in soup3.findAll('input', attrs={'type': re.compile("^password")} )]or
                         [label.get('for') for label in soup3.findAll('label', attrs={'for': re.compile("^j_pin")} )]or
    [label.get('for') for label in soup3.findAll('label', attrs={'for': re.compile("^j_username")} )] or
    [label.get('for') for label in soup3.findAll('label', attrs={'for': re.compile("^j_user_no")} )])
    if (len(pwdCredit3) == 0):
        return 1
    else:
        return -1
def func_MatchDomainTitle3(url3): #f5

    subdm3 = tldextract.extract(url3).subdomain
    dmr3 = tldextract.extract(url3).domain
    consubdm3 =''.join(e for e in subdm3.lower() if e.isalnum())
    consdmr3 = ''.join(e for e in dmr3.lower() if e.isalnum())
    response3 = requests.get(url3)
    html3 = response3.text
    soup3 = bs(html3, 'lxml')
    try :
        if ((soup3.title.string) and (soup3.title.string.lower())):
                #lisdmr = re.search(consdmr , ''.join(e for e in soup.title.string.lower() if e.isalnum()))
            if (re.search(consdmr3 , ''.join(e for e in soup3.title.string.lower() if e.isalnum()))==None):
                result1 = -1
            else:
                result1 = 1
            result= result1
        else:
            result = -1
    except:
        result = -1
    return result
        #print(lisdmr)
    #print(lisdmr2)
#print(newLink3)
#driver3.close()

######### Closing the last web page##################################
######## hash of the second link select on url##########################
def checonnectionurll4(urll):
    try :
        request = requests.get(urll)
        if request.status_code == 200:
            urll1 = urll
    except:
        print("Fail connection")
        urll1 = url

    return urll1
            #return url2

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/', methods=['GET', 'POST'])
def predict():
    data1 = []
    links =[]
    RP1=[]
    link2 =[]
    RP3=[]
    links3 =[]
    RP3=[]
    #results = {}
    errors = []
    if request.method == 'POST':
        url1 = request.form['url']
        data1 = [('{}'.format(url1))]
    else:   #except:
        errors.append("Unable to get URL. Please make sure it's valid and try again.")
            #return render_template('index.html')#try:
    for n in range(len(data1)):
        urldata = data1[n]
        url = urldata
		#try :
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(2) 
        resp= driver.get(url)
        driver.get_screenshot_as_file('screenshot1.png')
        driver.close()
        response = requests.get(url)
        html = response.text         
        soup = bs(html, 'lxml')
        links = ([a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^https://")} )] or
        [a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^http://")} )] or
        [a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^#")} )] or 
        [a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^/")} )] or 
        [a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^[A-Za-z0-9]")} )] or 
        [a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^https://[A-Za-z0-9]")} )] or
        [a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^http://[A-Za-z0-9]")} )]   or
        [link.get('href') for link in soup.findAll('link', attrs={'href': re.compile("^http://[A-Za-z0-9]")} )] or 
        [script.get('src') for script in soup.findAll('script', attrs={'src': re.compile("^http://[A-Za-z0-9]")})] or
        [link.get('href') for link in soup.findAll('link', attrs={'href': re.compile("^https://[A-Za-z0-9]")} )] or 
        [script.get('src') for script in soup.findAll('script', attrs={'src': re.compile("^https://[A-Za-z0-9]")} )]or
        [link.get('href') for link in soup.findAll('link', attrs={'href': re.compile("^#")} )] or 
        [script.get('src') for script in soup.findAll('script', attrs={'src': re.compile("^#")})]or
        [link.get('href') for link in soup.findAll('link', attrs={'href': re.compile("^[A-Za-z0-9]")} )] or 
        [script.get('src') for script in soup.findAll('script', attrs={'src': re.compile("^[A-Za-z0-9]")} )])
        #print(links)
        RP1 =([a.get('href') for a in soup.findAll('a', attrs={'href': re.compile("^#")} )] or
         [link.get('href') for link in soup.findAll('link', attrs={'href': re.compile("^#")} )]or
         [script.get('src') for script in soup.findAll('script', attrs={'src': re.compile("^#")})])

        hash_object = hashlib.sha3_224(soup.encode()).hexdigest()
        #print(hash_object.hexdigest())
        print(url)
		#except:
		#	pass
        newL =[]
        newL= selct_url(links,url)   
		newLink = newL[0] 
		newLinktext1=newL[1]
		#print(newLinktext1)
		#print(newLinktext2)
		######################## #### ################################################
		Feature2 = func_urlAtSymbol(url)
		Feature3 = func_urlDasheSymbol(url)
		Feature4 = func_urlDotSymbol(url)  
		Feature8 = func_ipAddress(url)
		Feature9 = func_urLength(url)

		#### Test on the content of the page #############################################
		###### Function that verifies if the page asks for the password ###################
		def func_CheckpasswordCreditcard(url):            #f6
			response = requests.get(url)
			html = response.text
			soup = bs(html, 'lxml')
			pwdCredit =( [input.get('type') for input in soup.findAll('input', attrs={'type': re.compile("^idcard")} )] or 
			[input.get('type') for input in soup.findAll('input', attrs={'type': re.compile("^password")} )]or
			[label.get('for') for label in soup.findAll('label', attrs={'for': re.compile("^j_pin")} )]or
			[label.get('for') for label in soup.findAll('label', attrs={'for': re.compile("^j_username")} )] or
			[label.get('for') for label in soup.findAll('label', attrs={'for': re.compile("^j_user_no")} )])
			if (len(pwdCredit) == 0):
				return 1
			else:
				return -1
		def func_MatchDomainTitle(url): #f5
			import tldextract
			import requests
			from bs4 import BeautifulSoup as bs
			subdm = tldextract.extract(url).subdomain
			#print(subdm)
			dmr = tldextract.extract(url).domain
			#print(dmr)
			consubdm =''.join(e for e in subdm.lower() if e.isalnum())
			consdmr = ''.join(e for e in dmr.lower() if e.isalnum())
			response = requests.get(url)
			html = response.text
			soup = bs(html, 'lxml')
			try :
				if (soup.title.string):
						#lisdmr = re.search(consdmr , ''.join(e for e in soup.title.string.lower() if e.isalnum()))
					if (re.search(consdmr , ''.join(e for e in soup.title.string.lower() if e.isalnum()))==None):
						result1 = -1
					else:
						result1 = 1
					result= result1
				else:
					result = -1
			except:
				  result = -1
			return result
		Feature5 = func_CheckpasswordCreditcard(url)
		Feature6 = func_MatchDomainTitle(url)
		Feature7 = func_NRP(RP1)
		#print(url)
		##$$print(newLink)
		##$$print(newLinktext1)
		### Closing the first page #########################################################
		links2 =[]
		RP2=[]
		def checonnectionurll2(urll):
			try :
				request = requests.get(urll)
				if request.status_code == 200:
					urll1 = urll
			except:
				print("Fail connection")
				urll1= url

			return urll1

		try:    
			url2 = checonnectionurll2(newLink)
			driver2 = webdriver.Chrome('chromedriver.exe')
			driver2.implicitly_wait(2) 
			resp2= driver2.get(url2)
			driver2.get_screenshot_as_file('screenshot2.png')
			driver2.close()
			response2 = requests.get(url2)
			html2 = response2.text
			soup2 = bs(html2, 'lxml')                                                     
			#links = soup.find_all('href')
			links2 = ([a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^https://")} )] or 
			[a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^http://")} )]  or 
			[a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^#")} )] 
			or [a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^/")} )] or 
			[a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^[A-Za-z0-9]")} )] or 
			[a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^https://[A-Za-z0-9]")} )] or
			[a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^http://[A-Za-z0-9]")} )] or
			[link.get('href') for link in soup2.findAll('link', attrs={'href': re.compile("^http://[A-Za-z0-9]")} )] or 
			[script.get('src') for script in soup2.findAll('script', attrs={'src': re.compile("^http://[A-Za-z0-9]")})] or
			[link.get('href') for link in soup2.findAll('link', attrs={'href': re.compile("^https://[A-Za-z0-9]")} )] or 
			[script.get('src') for script in soup2.findAll('script', attrs={'src': re.compile("^https://[A-Za-z0-9]")} )]or
			[link.get('href') for link in soup2.findAll('link', attrs={'href': re.compile("^#")} )] or 
			[script.get('src') for script in soup2.findAll('script', attrs={'src': re.compile("^#")})]or
			[link.get('href') for link in soup2.findAll('link', attrs={'href': re.compile("^[A-Za-z0-9]")} )] or 
			[script.get('src') for script in soup2.findAll('script', attrs={'src': re.compile("^[A-Za-z0-9]")} )])
			##$$links2
			RP2 =([a.get('href') for a in soup2.findAll('a', attrs={'href': re.compile("^#")} )] or
			 [link.get('href') for link in soup2.findAll('link', attrs={'href': re.compile("^#")} )]or
			 [script.get('src') for script in soup2.findAll('script', attrs={'src': re.compile("^#")})])
			hash_object2 = hashlib.sha3_224(soup2.encode())
			#print(hash_object2.hexdigest())
		except:
			pass
		def func_NRP2(RP2):
			if len(RP2)>=1:
				return -1
			else:
				return 1


		def selct_url2(links2, newLink):
			if(len(links2)>=2):
				list_of_random_items2=random.sample(links2,2)
				newLink2=list_of_random_items2[0]
			elif(len(links2) ==1):
				list_of_random_items2=random.sample(links2,1)
				newLink2=list_of_random_items2[0]
			else:
				newLink2= newLink
				#newLinktext1 = url
			return newLink2
		newLink2 = selct_url2(links2, newLink)
		############################ Test on url ############################################
		Feature21 = func_urlAtSymbol(url2)
		Feature31 = func_urlDasheSymbol(url2)
		Feature41= func_urlDotSymbol(url2)  
		Feature81 = func_ipAddress(url2)
		Feature91 = func_urLength(url2)

		#### Test on the content of the page ######################################################
		def func_CheckpasswordCreditcard2(url2):            #f6
			response2 = requests.get(url2)
			html2 = response2.text
			soup2 = bs(html2, 'lxml')
			pwdCredit2 =( [input.get('type') for input in soup2.findAll('input', attrs={'type': re.compile("^idcard")} )] or
			[input.get('type') for input in soup2.findAll('input', attrs={'type': re.compile("^password")} )] or 
			[label.get('for') for label in soup2.findAll('label', attrs={'for': re.compile("^j_pin")} )]or
			[label.get('for') for label in soup2.findAll('label', attrs={'for': re.compile("^j_username")} )] or
			[label.get('for') for label in soup2.findAll('label', attrs={'for': re.compile("^j_user_no")} )])
			if (len(pwdCredit2) == 0):
				return 1
			else:
				return -1
		def func_MatchDomainTitle2(url2):                  #f5

			subdm2 = tldextract.extract(url2).subdomain
			dmr2 = tldextract.extract(url2).domain
			consubdm2 =''.join(e for e in subdm2.lower() if e.isalnum())
			consdmr2 = ''.join(e for e in dmr2.lower() if e.isalnum())
			response2 = requests.get(url2)
			html2 = response2.text
			soup2 = bs(html2, 'lxml')
			try :
				if ((soup2.title.string) and (soup2.title.string.lower())):
						#lisdmr = re.search(consdmr , ''.join(e for e in soup.title.string.lower() if e.isalnum()))
					if (re.search(consdmr2 , ''.join(e for e in soup2.title.string.lower() if e.isalnum()))==None):
						result1 = -1
					else:
						result1 = 1
					result= result1
				else:
					result = -1
			except:
				result = -1
			return result
					#print(lisdmr
		##$$print(newLink2)
		#driver2.close()

		Feature51 = func_CheckpasswordCreditcard2(url2)
		Feature61 = func_MatchDomainTitle2(url2)
		Feature71 = func_NRP(RP2)
		#### Closing of the second web page#######################################################

		def checonnectionurll3(urll):
			try :
				request = requests.get(urll)
				if request.status_code == 200:
					urll1 = urll
			except:
				print("Fail connection")
				urll1 = url2

			return urll1
		try:
			url3 = checonnectionurll3(newLink2)
			driver3 = webdriver.Chrome('chromedriver.exe')
			driver3.implicitly_wait(2) 
			resp3= driver3.get(url3)
			driver3.get_screenshot_as_file('screenshot3.png')
			driver3.close()
			response3 = requests.get(url3)
			html3 = response3.text
			soup3 = bs(html3, 'lxml')
			RP3 =([a.get('href') for a in soup3.findAll('a', attrs={'href': re.compile("^#")} )] or
			 [link.get('href') for link in soup3.findAll('link', attrs={'href': re.compile("^#")} )]or
			 [script.get('src') for script in soup3.findAll('script', attrs={'src': re.compile("^#")})])
		except:
			pass
		#hash_object3 = hashlib.md5(soup3.encode())
		#print(hash_object3.hexdigest())
		def func_NRP3(RP3):
			if len(RP3)>=1:
				return -1
			else:
				return 1

		Feature22 = func_urlAtSymbol(url3)
		Feature32 = func_urlDasheSymbol(url3)
		Feature42 = func_urlDotSymbol(url3) 
		Feature82 = func_ipAddress(url3)
		Feature92 = func_urLength(url3)
        
        
        Feature52 = func_CheckpasswordCreditcard3(url3)
        Feature62 = func_MatchDomainTitle3(url3)
        Feature72 = func_NRP3(RP3)
        try:
            newLinktext1 = checonnectionurll4((newLinktext1))
            response4 = requests.get(newLinktext1)
            html4 = response4.text
            soup4 = bs(html4, 'lxml')
            hash_object4 = hashlib.sha3_224(soup4.encode())
           # print(hash_object4.hexdigest())
        except:
            pass
		
		GFeature2 = Goodfunc_urlAtSymbol(Feature2,Feature21,Feature22)
		GFeature3 = Goodfunc_urlDasheSymbol(Feature3,Feature31,Feature32)
		GFeature4 = Goodfunc_urlDotSymbol(Feature4,Feature41,Feature42)
		GFeature5 = Goodfunc_CheckpasswordCreditcard(Feature5,Feature51,Feature52)
		GFeature6 = Goodfunc_MatchDomainTitle(Feature6,Feature61,Feature62)
		#GFeature7 = Good_func_NRP(Feature7,Feature71,Feature72)
		GFeature8 = Good_func_ipAddress(Feature8,Feature81,Feature82)
		GFeature9 = Good_func_urLength(Feature9,Feature91,Feature92)


		with Image.open("screenshot1.png") as H1 :
			row, col = dhash.dhash_row_col(H1 )
			#hash1.show() 
			hash1= dhash.format_hex(row, col)
	   # print(hash1)
		with Image.open("screenshot2.png") as H2 :
			row2, col2 = dhash.dhash_row_col(H2 )
			#hash1.show() 
			hash2= dhash.format_hex(row2, col2)
	  #   print(hash2)
		with Image.open("screenshot3.png") as H3 :
			row3, col3 = dhash.dhash_row_col(H3 )
			#hash1.show() 
			hash3= dhash.format_hex(row3, col3)
	  #  print(hash3)
		import csv

		###### Text on similarity #############################################################
		Htesttext2 = hamming_distance(hashlib.sha3_224(soup4.encode()).hexdigest(),hashlib.sha3_224(bs(requests.get(url).text, 'lxml').encode()).hexdigest())
		Hreftext1 = hamming_distance(hashlib.sha3_224( bs(requests.get(url2).text, 'lxml').encode()).hexdigest(),hashlib.sha3_224(soup4.encode()).hexdigest())

		testscore1 = (Htesttext2 - Hreftext1)

	   ############## perceptual similarity###################
		Href = hamming_distance(hash2,hash3)
		Htest = hamming_distance(hash3,hash1)
		score1 = (Htest - Href)

		#'URL','URL': url,

		with open('CheckData.csv', mode='w') as score_file:
			fieldnames = ['Perceptual_similarity','Text_similarity','TesturlAtSymbol','TesturlDasheSymbol','TesturlDotSymbol',
						  'TestGoodCheckpwdCreditcard','TestGoodMatchDomainTitle','TestIPAdress','TestGoodurLength']
			writer = csv.DictWriter(score_file, fieldnames=fieldnames)

			writer.writerow({'Perceptual_similarity': codescore1(score1),'Text_similarity': codetestscore1(testscore1),'TesturlAtSymbol':GFeature2, 'TesturlDasheSymbol':GFeature3,
							 'TesturlDotSymbol':GFeature4,'TestGoodCheckpwdCreditcard': GFeature5,'TestGoodMatchDomainTitle':GFeature6,
							 'TestIPAdress':GFeature8,'TestGoodurLength':Feature9})

		score_file.close()
                    
    def RunData(file):
        model = pickle.load(open('model.pkl','rb'))
        with open('CheckData.csv', 'r') as f:
            ligne = f.readline()
            ElementData = ligne.split(',')[0:10]
            converted_list = []
            for element in ElementData:
                converted_list.append(element.strip())
                features = [converted_list]
            prediction = model.predict(features)
            if (prediction[0] == 1):
                text = 'secured '
            else:
                text = 'not secured '
        return text
    return render_template('index.html', prediction_text=' This website is {}'.format(RunData('CheckData.csv')))

if __name__ == "__main__":
    app.run(debug=True)
