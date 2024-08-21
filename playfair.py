
def matrix(key):
	matrix=[]
	#ingresar clave
	for e in key.upper():
		if e not in matrix:
			matrix.append(e)
    
    #ingresar letras restantes
	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
	for e in alphabet:
		if e not in matrix:
			matrix.append(e)	
	
	#initialize a new list. Is there any elegant way to do that?
	matrix_group=[]

	#Break it into 5*5
	matrix_group.append(matrix[0:5])
	matrix_group.append(matrix[5:10])
	matrix_group.append(matrix[10:15])
	matrix_group.append(matrix[15:20])
	matrix_group.append(matrix[20:25])
	return matrix_group


def check_repetition(message_original):
	message = list(message_original)

	#If both letters are the same, add an "X" after the first letter.
	for i in range(0,len(message),2):
		#
		if i+1>= len(message):
			break
		if message[i]==message[i+1]:
			message.insert(i+1,'X')
			#
			check_repetition(message)
	return message

def make_digrams(message):
		#If it is odd digit, add an "X" at the end
	if len(message)%2==1:
		message.append("X")
	#Grouping
	digrams=[]
	for i in range(0,len(message),2):
		digrams.append(message[i:i+2])

	return digrams

def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j]==letter:
				x=i
				y=j

	return x,y

def encrypt(message, key):
	
	#mensaje en texto claro representado como pares
	message=make_digrams(check_repetition(message.upper()))

	key_matrix=matrix(key)
	cipher=[]
	for e in message:
		#inicializar lista de par
		pair = []
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		#validacion de fila
		if p1==p2:
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			#crear par de letras cifradas
			pair.append(key_matrix[p1][q1+1])
			pair.append(key_matrix[p1][q2+1])	
			#agregar par a la lista final
			cipher.append(pair)	
		#validacion de columna
		elif q1==q2:
			if p1==4:
				p1=-1
			if p2==4:
				p2=-1
			pair.append(key_matrix[p1+1][q1])
			pair.append(key_matrix[p2+1][q2])
			cipher.append(pair)	
        #validar rectangulo
		else:
			pair.append(key_matrix[p1][q2])
			pair.append(key_matrix[p2][q1])
			cipher.append(pair)	
	return cipher


def decrypt(cipher, key):
	
	#cipher es una lista de pares de letras
	key_matrix=matrix(key)
	plaintext=[]
	for e in cipher:
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		#validacion de fila
		if p1==p2:
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			plaintext.append(key_matrix[p1][q1-1])
			plaintext.append(key_matrix[p1][q2-1])	
		#validacion columna	
		elif q1==q2:
			if p1==4:
				p1=-1
			if p2==4:
				p2=-1
			plaintext.append(key_matrix[p1-1][q1])
			plaintext.append(key_matrix[p2-1][q2])
		#validacion rectangulo
		else:
			plaintext.append(key_matrix[p1][q2])
			plaintext.append(key_matrix[p2][q1])

	for letter in plaintext:
		if "X" == letter:
			plaintext.remove("X")
	return plaintext



def main():
    key = "monarchy"
    message = "attackf"
    print(encrypt(message, key))
    print(decrypt(encrypt(message, key), key ))


main()

