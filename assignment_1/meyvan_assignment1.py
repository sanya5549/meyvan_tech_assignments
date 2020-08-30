from zipfile import ZipFile
import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 

def open_zip_file(password):
	global is_password_found
	
	str_zipFile = os.path.dirname(os.path.abspath(__file__)) + '/assignment.zip'
	# str_zipFile = '/home/sanya/Documents/meyvan_tech_assignments/assignment_1/assignment.zip'
	prYellow("string password = " + password)
	with ZipFile(str_zipFile) as zipObj:
	  zipObj.extractall(pwd = bytes(password,'utf-8'))

	is_password_found = True
	return 


helper_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j' ,'k' ,'l' , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0','1', '2', '3', '4', '5', '6', '7', '8', '9']
is_password_found = False

def start():
	password = "Twg48wTM"
	final_password = ""
	for i in range(62):
		for j in range(62):
			if( is_password_found == True):
				break
			final_password = password + helper_list[i] + helper_list[j]
			try:
				open_zip_file(final_password)
			except:
				#print(e)
				continue
	if is_password_found:
		prCyan ("Password was found = " + final_password)
	else:
		prRed ("Password not found")


if __name__ == '__main__':

	start()
