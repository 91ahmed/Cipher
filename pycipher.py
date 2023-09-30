import random

class PyCiper:

	# Represent each character with a specific code composed of 3 digits.
	code = {
		'a':100, 'A':101, 'b':102, 'B':103, 'c':104, 'C':105, 
		'd':106, 'D':107, 'e':108, 'E':109, 'f':110, 'F':111,
		'g':112, 'G':113, 'h':114, 'H':115, 'i':116, 'I':117,
		'j':118, 'J':119, 'k':120, 'K':121, 'l':122, 'L':123, 
		'm':124, 'M':125, 'n':126, 'N':127, 'o':128, 'O':129,
		'p':130, 'P':131, 'q':132, 'Q':133, 'r':134, 'R':135, 
		's':136, 'S':137, 't':138, 'T':139, 'u':140, 'U':141, 
		'v':142, 'V':143, 'w':144, 'W':145, 'x':146, 'X':147, 
		'y':148, 'Y':149, 'z':150, 'Z':151, '@':152, '$':153,
		'&':154, '_':155, '-':156, '=':157, '+':158, '?':159,
		'%':160, '~':161, '`':162, '!':163, '#':164, '^':165,
		'*':166, '(':167, ')':168, '|':169, '\\':170, ']':171,
		'[':172, '{':173, '}':174, '<':175, '>':176, ':':177,
		';':178, '"':179, '\'':180, '/':181, ',':182, '.':183,
		'0':184, '1':185, '2':186, '3':187, '4':188, '5':189,
		'6':190, '7':191, '8':192, '9':193, ' ':194,
	}

	# Replace the code digits with a specific character
	chars = {
		0:'h', 1:'g', 2:'w', 3:'q', 4:'j', 5:'x',
		6:'p', 7:'r', 8:'y', 9:'d',
	}

	chars_reverse = {
		'h':0, 'g':1, 'w':2, 'q':3, 'j':4, 'x':5,
		'p':6, 'r':7, 'y':8, 'd':9,
	}

	cipher = {
		'h': ['u','0','b','µ','U','B'],
		'g': ['o','1','m','~','O','M'],
		'w': ['s','2','v','ς','S','V'],
		'q': ['a','3','f','β','A','F'],
		'j': ['k','4','t','^','K','T'],
		'x': ['c','5','z','#','C','Z'],
		'p': ['e','6','&','π','E','δ'],
		'r': ['i','7','$','£','I','λ'],
		'y': ['l','8','%','=','L','ξ'],
		'd': ['n','9','+','η','N','φ'],
	}

	cipher_reverse = {
		'u':'h','0':'h','b':'h','µ':'h','U':'h','B':'h',
		'o':'g','1':'g','m':'g','~':'g','O':'g','M':'g',
		's':'w','2':'w','v':'w','ς':'w','S':'w','V':'w',
		'a':'q','3':'q','f':'q','β':'q','A':'q','F':'q',
		'k':'j','4':'j','t':'j','^':'j','K':'j','T':'j',
		'c':'x','5':'x','z':'x','#':'x','C':'x','Z':'x',
		'e':'p','6':'p','&':'p','π':'p','E':'p','δ':'p',
		'i':'r','7':'r','$':'r','£':'r','I':'r','λ':'r',
		'l':'y','8':'y','%':'y','=':'y','L':'y','ξ':'y',
		'n':'d','9':'d','+':'d','η':'d','N':'d','φ':'d',
	}

	salt = [
		'h','g','w','q','j','x','p','r','y','d',
		'H','G','W','Q','J','X','P','R','Y','D',
	]

	def obtainCode (self, text):
		# List to store the final result
		result = []

		# Loop through each character and replace it with the corresponding code.
		for c in text:
			result.append(self.code[c])

		return result

	def obtainChar (self, text):
		text = self.obtainCode(text)
		# Convert array to string
		code_string = ''
		for code in text:
			code_string += str(code)
		# Split string
		code_list = []
		for li in code_string:
			code_list.append(li)
		# Replace digits with character
		code_char = ''
		for digit in code_list:
			ch = int(digit)
			code_char += self.chars[ch]
		# final result list
		result = []
		for i in range(0, len(code_char), 3):
		    result.append(code_char[i:i+3])

		return result

	def obtainCipher (self, text):
		text = self.obtainChar(text)
		# Convert array to string
		cipher_string = ''
		for t in text:
			cipher_string += t
		# Create cipher
		cipher = ''
		for ci in cipher_string:
			rand = random.randint(0,5)
			cipher += self.cipher[ci][rand]
		# Add Salt
		random.shuffle(self.salt)
		start_salt = self.salt[1]+self.salt[0] # Get start salt
		end_salt = self.salt[5]+self.salt[3] # Get end salt

		cipher = start_salt+cipher+end_salt

		return cipher

	def getCipherChar (self, value):
		for cip in self.code:
			if str(self.code[cip]) == str(value):
				return cip

	def encrypt (self, text):
		return self.obtainCipher(text)

	def decrypt (self, text):
		# Remove salt
		cipher_without_salt = ''
		for c in text:
			if c not in self.salt:
				cipher_without_salt += c
		# Convert cipher
		cipher_text = ''
		for ci in cipher_without_salt:
			cipher_text += self.cipher_reverse[ci]
		# Convert text to code
		cipher_code = ''
		for cg in cipher_text:
			st = self.chars_reverse[cg]
			cipher_code += str(st)
		# Add code to list
		code = []
		codeval = ''
		for dc in cipher_code:
			codeval += str(dc)
			if len(codeval) == 3:
				code.append(codeval)
				codeval = ''
		# Return real character
		result = ''
		for real in code:
			real = str(real)
			val = str(self.getCipherChar(real))
			result += val

		return result