
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


print(make_digrams(check_repetition("minus")))