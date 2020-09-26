from colorama import Fore
print(Fore.MAGENTA+''' __  __                        ____          _      \n|  \/  | ___  _ __ ___  ___   / ___|___   __| | ___ \n| |\/| |/ _ \| '__/ __|/ _ \ | |   / _ \ / _` |/ _ \ \n| |  | | (_) | |  \__ \  __/ | |__| (_) | (_| |  __/\n|_|  |_|\___/|_|  |___/\___|  \____\___/ \__,_|\___|\n'''+Fore.RED)
print("Created by Manoj Paramsetti")
TextCode = ""
MorseCode =""
Text=""
try:
			
	def Morse(TextCode):	
		Morse = " "
		print(Morse)
		for Letter in TextCode:
			if (Letter == "A"):
				Morse += "._ "
			if (Letter == "B"):
				Morse += "_... "
			if (Letter == "C"):
				Morse += "_._. "
			if (Letter == "D"):
				Morse += "_.. "
			if (Letter == "E"):
				Morse += ". "
			if (Letter == "F"):
				Morse += ".._. "
			if (Letter == "G"):
				Morse += "__. "
			if (Letter == "H"):
				Morse += ".... "
			if (Letter == "I"):
				Morse += ".. "
			if (Letter == "J"):
				Morse += ".___ "
			if (Letter == "K"):
				Morse += "_._ "
			if (Letter == "L"):
				Morse += "._.. "
			if (Letter == "M"):
				Morse += "__ "
			if (Letter == "N"):
				Morse += "_. "
			if (Letter == "O"):
				Morse += "___ "
			if (Letter == "P"):
				Morse += ".__. "
			if (Letter == "Q"):
				Morse += "__._ "
			if (Letter == "R"):
				Morse += "._. "
			if (Letter == "S"):
				Morse += "... "
			if (Letter == "T"):
				Morse += "_ "
			if (Letter == "U"):
				Morse += ".._ "
			if (Letter == "V"):
				Morse += "..._ "
			if (Letter == "W"):
				Morse += ".__ "
			if (Letter == "X"):
				Morse += "_.._ "
			if (Letter == "Y"):
				Morse += "_.__ "
			if (Letter == "Z"):
				Morse += "__.. "
			if (Letter == " "):
				Morse += "/ "
			if (Letter == "1"):
				Morse += ".____ "
			if (Letter == "2"):
				Morse += "..___ "
			if (Letter == "3"):
				Morse += "...__ "
			if (Letter == "4"):
				Morse += "...._ "
			if (Letter == "5"):
				Morse += "..... "
			if (Letter == "6"):
				Morse += "_.... "
			if (Letter == "7"):
				Morse += "__... "
			if (Letter == "8"):
				Morse += "___.. "
			if (Letter == "9"):
				Morse += "____. "
			if (Letter == "0"):
				Morse += "_____ "
		print("*|--  Morse code ready  --|*")
		print(Morse)
	
	letter=""
	def Text(MorseCode):	
		Text = ""
		def test(Letter):			
			global letter
			if (Letter == "._"):
				letter += "A"
			if (Letter == "_..."):
				letter += "B"
			if (Letter == "_._."):
				letter += "C"
			if (Letter == "_.."):
				letter += "D"
			if (Letter == "."):
				letter += "E"
			if (Letter == ".._."):
				letter += "F"
			if (Letter == "__."):
				letter += "G"
			if (Letter == "...."):
				letter += "H"
			if (Letter == ".."):
				letter += "I"
			if (Letter == ".___"):
				letter += "J"
			if (Letter == "_._"):
				letter += "K"
			if (Letter == "._.."):
				letter += "L"
			if (Letter == "__"):
				letter += "M"
			if (Letter == "_."):
				letter += "N"
			if (Letter == "___"):
				letter += "O"
			if (Letter == ".__."):
				letter += "P"
			if (Letter == "__._"):
				letter += "Q"
			if (Letter == "._."):
				letter += "R"
			if (Letter == "..."):
				letter += "S"
			if (Letter == "_"):
				letter += "T"
			if (Letter == ".._"):
				letter += "U"
			if (Letter == "..._"):
				letter += "V"
			if (Letter == ".__"):
				letter += "W"
			if (Letter == "_.._"):
				letter += "X"
			if (Letter == "_.__"):
				letter += "Y"
			if (Letter == "__.."):
				letter += "Z"
			if (Letter == ".____"):
				letter += "1"
			if (Letter == "..___"):
				letter += "2"
			if (Letter == "...__"):
				letter += "3"
			if (Letter == "...._"):
				letter += "4"
			if (Letter == "....."):
				letter += "5"
			if (Letter == "_...."):
				letter += "6"
			if (Letter == "__..."):
				letter += "7"
			if (Letter == "___.."):
				letter += "8"
			if (Letter == "____."):
				letter += "9"
			if (Letter == "_____"):
				letter += "0"
			Text = ''

		
		for Letter in MorseCode:

			if Letter == " ":
				test(Text)
				Text=''

			elif Letter == "/":
				global letter
				test(Text)
				letter+=" "
				Text=''

			else:
				Text += Letter
		print("\n\n*|--  Text output is ready  --|*")
		print(letter)

	def Choice():
		if (MOD == 'M'):
			TextCode = input("\nEnter the Text to convert into Morse Code\n>>> ")		
			TextCode = TextCode.upper()
			Morse(TextCode)

		elif (MOD == "T"):
			MorseCode  = input("\nEnter the Morse Code to convert into to Text\n>>> ")
			MorseCode+=" ...."
			Text(MorseCode)
		else:
			print("\nOh! You entered wrong thing\n It's okay, I'll Call it again")
			Choice()

	MOD = input("To convert into Morse code Press M\nTo convert into Text Press T\n>>> ")
	MOD = MOD.upper()
	Choice()
#To Prevent KeyboardInterrupt and SystemExit
except (KeyboardInterrupt, SystemExit):
	print("\r\r\n\n*|--  Session is Closed  --|*")
