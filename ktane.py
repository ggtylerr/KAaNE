import sys
import webbrowser

# KTaNE by Steel Crate Games
# keypad code & needy knobs idea by Jonathan-Walsh
# rest by Gaming Guy Tyler
# this code is not intended to copy anything that could already be existing that's like this.

def ktane():
	print "Available Modules:"
	print "Simple Wires (w)"                # L74
	print "Button (b)"                      # L732
	print "Keypad (k)"                      # L809
	print "Simon Says (ss)"                 # L890
	print "Who's on First? (wf)"            # L944
	print "Memory (me)"                     # L1097
	print "Morse Code (mc)"                 # L1254
	print "Complicated Wires (cw)"          # L1339
	print "Wire Sequences (ws)"             # L1412
	print "Mazes (mz)"                      # L1811
	print "Passwords (pw)"                  # L2009
	print "Needy Gas (ng)"                  # L2101
	print "Capacitor Discharger (cd)"       # L2106
	print "Needy Knobs (nk)"                # L2110
	print "[MOD|WIP] Broken Buttons (bb)"   # L2128
	print "[MOD] Wire Placement (wp)"       # L3055
	print "[MOD|WIP] Adventure Game (ag)"   # L3141
	print "[MOD] Algebra (al)"		# L3509
	print "[MOD|WIP] The Bulb (tb)"         # L3662
	print ""
	x = raw_input("What Module? ")
	if x == "w":
		wires()
	if x == "b":
		button()
	if x == "k":
		keypad()
	if x == "ss":
		simonSays()
	if x == "wf":
		whosOnFirst()
	if x == "me":
		memory()
	if x == "mc":
		morseCode()
	if x == "cw":
		complicatedWires()
	if x == "ws":
		wireSequences()
	if x == "mz":
		mazes()
	if x == "pw":
		passwords()
	if x == "ng":
		gas()
	if x == "cd":
		capacitorDischarger()
	if x == "nk":
		knobs()
	if x == "bb":
		brokenButtons()
	if x == "wp":
		wirePlacement()
	if x == "ag":
		adventureGame()
	if x == "al":
		algebra()
	if x == "tb":
		theBulb()
	else:
		print "Invalid Module!"
		raw_input("Press any button to continue.")
		ktane()
def wires():
	# Simple Wires
	# Red: "r"
	# White: "w"
	# Blue: "bu"
	# Black: "ba"
	# Yellow: "y"
	# Variable [A]lpha: 1st wire
	# Variable [B]ravo: 2nd wire
	# Variable [C]harlie: 3rd wire
	# Variable [D]elta: 4th wire
	# Variable [E]cho: 5th wire
	# Variable [F]oxtrot: 6th wire
	x = input("How many wires? ")
	if x == 3:
		print "Red: r"
		print "White: w"
		print "Blue: bu"
		print "Black: ba"
		print "Yellow: y"
		a = raw_input("What color is the 1st wire? ")
		b = raw_input("2nd? ")
		c = raw_input("3rd? ")
		if not a == "r":
			if not b == "r":
				if not c == "r":
					print "Cut the 2nd wire."
					raw_input("Press any button to continue.")
					ktane()
		if c == "w":
			print "Cut the 3rd wire."
			raw_input("Press any button to continue.")
			ktane()
		if a == "bu" and b == "bu":
			print "Cut the 2nd wire."
			raw_input("Press any button to continue.")
			ktane()
		if a == "bu" and c == "bu":
			print "Cut the 3rd wire."
			raw_input("Press any button to continue.")
			ktane()
		if b == "bu" and c == "bu":
			print "Cut the 3rd wire."
			raw_input("Press any button to continue.")
			ktane()
		else:
			print "Cut the 3rd wire."
			raw_input("Press any button to continue.")
			ktane()
	if x == 4:
		print "Red: r"
		print "White: w"
		print "Blue: bu"
		print "Black: ba"
		print "Yellow: y"
		a = raw_input("What color is the 1st wire? ")
		b = raw_input("2nd? ")
		c = raw_input("3rd? ")
		d = raw_input("4th? ")
		if a == "r" and b == "r":
			x = raw_input("Is the last digit of the SN odd? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				if d == "r":
					print "Cut the 4th wire."
					raw_input("Press any button to continue.")
					ktane()
				if c == "r":
					print "Cut the 3rd wire."
					raw_input("Press any button to continue.")
					ktane()
				if b == "r":
					print "Cut the 2nd wire."
					raw_input("Press any button to continue.")
					ktane()
		if a == "r" and c == "r":
			x = raw_input("Is the last digit of the SN odd? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				if d == "r":
					print "Cut the 4th wire."
					raw_input("Press any button to continue.")
					ktane()
				if c == "r":
					print "Cut the 3rd wire."
					raw_input("Press any button to continue.")
					ktane()
		if b == "r" and c == "r":
			x = raw_input("Is the last digit of the SN odd? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				if d == "r":
					print "Cut the 4th wire."
					raw_input("Press any button to continue.")
					ktane()
				if c == "r":
					print "Cut the 3rd wire."
					raw_input("Press any button to continue.")
					ktane()
		if b == "r" and d == "r":
			x = raw_input("Is the last digit of the SN odd? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				print "Cut the 4th wire."
				raw_input("Press any button to continue.")
				ktane()
		if c == "r" and d == "r":
			x = raw_input("Is the last digit of the SN odd? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				print "Cut the 4th wire."
				raw_input("Press any button to continue.")
				ktane()
		if d == "y":
			if not a == "r":
				if not b == "r":
					if not c == "r":
						print "Cut the 1st wire."
						raw_input("Press any button to continue.")
						ktane()
		if a == "bu":
			if not b == "bu":
				if not c == "bu":
					if not d == "bu":
						print "Cut the 1st wire."
						raw_input("Press any button to continue.")
						ktane()
		if b == "bu":
			if not a == "bu":
				if not c == "bu":
					if not d == "bu":
						print "Cut the 1st wire."
						raw_input("Press any button to continue.")
						ktane()
		if c == "bu":
			if not a == "bu":
				if not b == "bu":
					if not d == "bu":
						print "Cut the 1st wire."
						raw_input("Press any button to continue.")
						ktane()
		if d == "bu":
			if not a == "bu":
				if not b == "bu":
					if not c == "bu":
						print "Cut the 1st wire."
						raw_input("Press any button to continue.")
						ktane()
		if a == "y" and b == "y":
			print "Cut the 4th wire."
			raw_input("Press any button to continue.")
			ktane()
		if a == "y" and c == "y":
			print "Cut the 4th wire."
			raw_input("Press any button to continue.")
			ktane()
		if a == "y" and d == "y":
			print "Cut the 4th wire."
			raw_input("Press any button to continue.")
			ktane()
		if b == "y" and c == "y":
			print "Cut the 4th wire."
			raw_input("Press any button to continue.")
			ktane()
		if b == "y" and d == "y":
			print "Cut the 4th wire."
			raw_input("Press any button to continue.")
			ktane()
		if c == "y" and d == "y":
			print "Cut the 4th wire."
			raw_input("Press any button to continue.")
			ktane()
		else:
			print "Cut the 2nd wire."
			raw_input("Press any button to continue.")
			ktane()
	if x == 5:
		print "Red: r"
		print "White: w"
		print "Blue: bu"
		print "Black: ba"
		print "Yellow: y"
		a = raw_input("What color is the 1st wire? ")
		b = raw_input("2nd? ")
		c = raw_input("3rd? ")
		d = raw_input("4th? ")
		e = raw_input("5th? ")
		if e == "ba":
			x = raw_input("Is the last digit of the SN odd? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				print "Cut the 4th wire."
				raw_input("Press any button to continue.")
				ktane()
		if a == "r":
			if not b == "r":
				if not c == "r":
					if not d == "r":
						if not e == "r":
							if b == "y" and c == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if c == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if c == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if d == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
		if b == "r":
			if not a == "r":
				if not c == "r":
					if not d == "r":
						if not e == "r":
							if a == "y" and c == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if c == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if c == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if d == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
		if c == "r":
			if not a == "r":
				if not b == "r":
					if not d == "r":
						if not e == "r":
							if a == "y" and b == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if d == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
		if d == "r":
			if not a == "r":
				if not b == "r":
					if not c == "r":
						if not e == "r":
							if a == "y" and b == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and c == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and c == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if c == "y" and e == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
		if e == "r":
			if not a == "r":
				if not b == "r":
					if not c == "r":
						if not d == "r":
							if a == "y" and b == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and c == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if a == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and c == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if b == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
							if c == "y" and d == "y":
								print "Cut the 1st wire."
								raw_input("Press any button to continue.")
								ktane()
		if not a == "ba":
			if not b == "ba":
				if not c == "ba":
					if not d == "ba":
						if not e == "ba":
							print "Cut the 2nd wire."
							raw_input("Press any button to continue.")
							ktane()
		print "Cut the 1st wire."
		raw_input("Press any button to continue.")
		ktane()
	if x == 6:
		print "Red: r"
		print "White: w"
		print "Blue: bu"
		print "Black: ba"
		print "Yellow: y"
		a = raw_input("What color is the 1st wire? ")
		b = raw_input("2nd? ")
		c = raw_input("3rd? ")
		d = raw_input("4th? ")
		e = raw_input("5th? ")
		f = raw_input("6th? ")
		if not a == "y":
			if not b == "y":
				if not c == "y":
					if not d == "y":
						if not e == "y":
							if not f == "y":
								x = raw_input("Is the last digit of the SN odd? ")
								if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
									print "Cut the 3rd wire."
									raw_input("Press any button to continue.")
									ktane()
		if a == "y":
			if not b == "y":
				if not c == "y":
					if not d == "y":
						if not e == "y":
							if not f == "y":
								if b == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if e == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
		if b == "y":
			if not a == "y":
				if not c == "y":
					if not d == "y":
						if not e == "y":
							if not f == "y":
								if a == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if e == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
		if c == "y":
			if not a == "y":
				if not b == "y":
					if not d == "y":
						if not e == "y":
							if not f == "y":
								if a == "w" and b == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if e == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
		if d == "y":
			if not a == "y":
				if not b == "y":
					if not c == "y":
						if not e == "y":
							if not f == "y":
								if a == "w" and b == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if e == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
		if e == "y":
			if not a == "y":
				if not b == "y":
					if not c == "y":
						if not d == "y":
							if not f == "y":
								if a == "w" and b == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and f == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
		if f == "y":
			if not a == "y":
				if not b == "y":
					if not c == "y":
						if not d == "y":
							if not e == "y":
								if a == "w" and b == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if a == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and c == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if b == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and d == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if c == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
								if d == "w" and e == "w":
									print "Cut the 4th wire."
									raw_input("Press any button to continue.")
									ktane()
		if not a == "r":
			if not b == "r":
				if not c == "r":
					if not d == "r":
						if not e == "r":
							if not f == "r":
								print "Cut the 6th wire."
								raw_input("Press any button to continue.")
								ktane()
		print "Cut the 4th wire."
		raw_input("Press any button to continue.")
		ktane()
	print "Invalid Number!"
	raw_input("Press any button to continue.")
	ktane()
def button():
	# Button
	# Button Colors:
	# Blue: b
	# White: w
	# Yellow: y
	# Red: r
	# Button Text has no caps.
	# Strip Color:
	# Variable [A]lpha: Button Color
	# Variable [B]ravo: Button Text
	# Variable [C]harlie: Batteries
	print "Colors:"
	print "Blue: b"
	print "White: w"
	print "Yellow: y"
	print "Red: r"
	print "Other: o"
	print "Type the button text without any caps."
	a = raw_input("What is the button color? ")
	b = raw_input("What is the button text? ")
	if a == "b" and b == "abort":
		print "Hold down the button."
		print "If the color is blue, release on 4."
		print "If the color is yellow, release on 5."
		print "Otherwise, release on 1."
		raw_input("Press any button to continue.")
		ktane()
	if b == "detonate":
		c = input("How many batteries? ")
		if c >= 2:
			print "Press and immediately release."
			raw_input("Press any button to continue.")
			ktane()
	if a == "w":
		x = raw_input("Is there a CAR lit indicator? ")
		if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
			print "Hold down the button."
			print "If the color is blue, release on 4."
			print "If the color is yellow, release on 5."
			print "Otherwise, release on 1."
			raw_input("Press any button to continue.")
			ktane()
	try:
		if c >= 2:
			x = raw_input("Is there a FRK lit indicator? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				print "Press and immediately release."
				raw_input("Press any button to continue.")
				ktane()
	except NameError:
		c = input("How many batteries? ")
		if c >= 2:
			x = raw_input("Is there a FRK lit indicator? ")
			if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
				print "Press and immediately release."
				raw_input("Press any button to continue.")
				ktane()
	if a == "y":
		print "Hold down the button."
		print "If the color is blue, release on 4."
		print "If the color is yellow, release on 5."
		print "Otherwise, release on 1."
		raw_input("Press any button to continue.")
		ktane()
	if a == "y":
		if b == "hold":
			print "Press and immediately release."
			raw_input("Press any button to continue.")
			ktane()
	else:
		print "Hold down the button."
		print "If the color is blue, release on 4."
		print "If the color is yellow, release on 5."
		print "Otherwise, release on 1."
		raw_input("Press any button to continue.")
		ktane()
def keypad():
	# Keypad
	# Character guide can be found at ./characterguide.png
	# Most of the code from Jonathan-Walsh
	img = input("Display images?" + "\n" + "1 = Yes" + "\n" + "2 = No" + "\n")
	if img == 1:
		guide = "characterguide.png"
		webbrowser.open(guide)
	print "Please type in lower caps."
	print ""
	allSymbols = ["tennis","at","lambda","n","spaceship","h","lc","euro","co","star","?","copyright","w","xi","low c","6","paragraph","tb","smiley","chandelier","rc","snake","star 2","piece","ae","hat n","omega"]
	#Possible lists of symbols
	symbols1 = ["tennis","at","lambda","n","spaceship","h","lc"]
	symbols2 = ["euro","tennis","lc","co","star","h","?"]
	symbols3 = ["copyright","w","co","xi","low c","lambda","star"]
	symbols4 = ["6","paragraph","tb","spaceship","xi","?","smiley"]
	symbols5 = ["chandelier","smiley","tb","rc","paragraph","snake","star 2"]
	symbols6 = ["6","euro","piece","ae","chandelier","hat n","omega"]
	symbols = [symbols1,symbols2,symbols3,symbols4,symbols5,symbols6]
	#Setup
	sortTemp = 0
	indexTemp = 0
	symbolsList = []
	indexList = [0,0,0,0]
	sortList = [1,2,3,4]
	symbolsCount = 0
	listFound = "false"
	#Ask for symbols
	firstSymbol = raw_input("First symbol: ").lower()
	secondSymbol = raw_input("Second symbol: ").lower()
	thirdSymbol = raw_input("Third symbol: ").lower()
	fourthSymbol = raw_input("Fourth symbol: ").lower()
	#Loop to find correct list
	for i in xrange(0,len(symbols)):
		symbolsList = symbols[i]
		symbolsCount = 0
		for j in xrange(0,len(symbols1)):
			if firstSymbol == symbols[i][j]:
				symbolsCount += 1
			elif secondSymbol == symbols[i][j]:
				symbolsCount += 1
			elif thirdSymbol == symbols[i][j]:
				symbolsCount += 1
			elif fourthSymbol == symbols[i][j]:
				symbolsCount += 1
		if symbolsCount == 4:
			listFound = "true"
			break
	#Case where something was incorrectly entered
	if listFound == "false":
		print "Your entries did not match any of the lists. Try again."
		symbols()
	#Finding symbol indices in the list
	for i in xrange(0,len(symbols1)):
		if symbolsList[i] == firstSymbol:
			indexList[0] = i
		elif symbolsList[i] == secondSymbol:
			indexList[1] = i
		elif symbolsList[i] == thirdSymbol:
			indexList[2] = i
		elif symbolsList[i] == fourthSymbol:
			indexList[3] = i
	#Swapping to find correct order
	for i in xrange(0,4):
		for j in xrange(0,3):
			if indexList[j] > indexList[j+1]:
				indexList[j],indexList[j+1] = indexList[j+1],indexList[j]
				sortList[j],sortList[j+1] = sortList[j+1],sortList[j]
	#Correct order
	print "Correct order:",
	for i in xrange(len(sortList)):
		if sortList[i] == 1:
			print firstSymbol,
		if sortList[i] == 2:
			print secondSymbol,
		if sortList[i] == 3:
			print thirdSymbol,
		if sortList[i] == 4:
			print fourthSymbol,
	raw_input("Press any button to continue.")
	ktane()
def simonSays():
	# Simon Says
	# Variable [A]lpha: SN Vowel
	# Variable [B]ravo: Strikes
	a = raw_input("Does the SN contain a vowel? ")
	b = input("How many strikes are there? ")
	if b >= 3 or b <= -1:
		print "Unless you mistyped, good luck getting out with that many strikes."
		raw_input("Press any button to continue.")
		ktane()
	if a == "y" or a == "yes" or a == "Y" or a == "Yes" or a == "YES":
		if b == 0:
			print "Red = Blue"
			print "Blue = Red"
			print "Green = Yellow"
			print "Yellow = Green"
			raw_input("Press any button to continue.")
			ktane()
		if b == 1:
			print "Red = Yellow"
			print "Blue = Green"
			print "Green = Blue"
			print "Yellow = Red"
			raw_input("Press any button to continue.")
			ktane()
		if b == 2:
			print "Red = Green"
			print "Blue = Red"
			print "Green = Yellow"
			print "Yellow = Blue"
			raw_input("Press any button to continue.")
			ktane()
	else:
		if b == 0:
			print "Red = Blue"
			print "Blue = Yellow"
			print "Green = Green"
			print "Yellow = Red"
			raw_input("Press any button to continue.")
			ktane()
		if b == 1:
			print "Red = Red"
			print "Blue = Blue"
			print "Green = Yellow"
			print "Yellow = Green"
			raw_input("Press any button to continue.")
			ktane()
		if b == 2:
			print "Red = Yellow"
			print "Blue = Green"
			print "Green = Blue"
			print "Yellow = Red"
			raw_input("Press any button to continue.")
			ktane()
def whosOnFirst():
	# Who's on First?
	# Variable [A]lpha: Word 1
	# Variable [B]ravo: Word 2
	# Variable [C]harlie: Position
	print "Please type in lower caps."
	print "For no word, leave a space."
	a = raw_input("What is the word on display? ")
	if a == "ur":
		c = 1
	if a == "first" or a == "okay" or a == "c":
		c = 2
	if a == "nothing" or a == "led" or a == "they are" or a == "yes":
		c = 3
	if a == "blank" or a == "read" or a == "red" or a == "you" or a == "your" or a == "you're" or a == "their":
		c = 4
	if a == " " or a == "reed" or a == "leed" or a == "they're":
		c = 5
	if a == "display" or a == "says" or a == "no" or a == "lead" or a == "hold on" or a == "you are" or a == "there" or a == "see" or a == "cee":
		c = 6
	try:
		if c == 1:
			b = raw_input("What is the word in the 1st position? ")
	except NameError:
		print "Unknown word. Please try again."
		raw_input("Press any button to continue.")
		ktane()
	if c == 2:
		b = raw_input("What is the word in the 2nd position? ")
	if c == 3:
		b = raw_input("What is the word in the 3rd position? ")
	if c == 4:
		b = raw_input("What is the word in the 4th position? ")
	if c == 5:
		b = raw_input("What is the word in the 5th position? ")
	if c == 6:
		b = raw_input("What is the word in the 6th position?")
	if b == "ready":
		print "Yes, Okay, What, Middle, Left, Press, Right, Blank, Ready"
		raw_input("Press any button to continue.")
		ktane()
	if b == "first":
		print "Left, Okay, Yes, Middle, No, Right, Nothing, Uhhh, Wait, Ready, Blank, What, Press, First"
		raw_input("Press any button to continue.")
		ktane()
	if b == "no":
		print "Blank, Uhhh, Wait, First, What, Ready, Right, Yes, Nothing, Left, Press, Okay, No"
		raw_input("Press any button to continue.")
		ktane()
	if b == "blank":
		print "Wait, Right, Okay, Middle, Blank"
		raw_input("Press any button to continue.")
		ktane()
	if b == "nothing":
		print "Uhhh, Right, Okay, Middle, Yes, Blank, No, Press, Left, What, Wait, First, Nothing"
		raw_input("Press any button to continue.")
		ktane()
	if b == "yes":
		print "Okay, Right, Uhhh, Middle, First, What, Press, Ready, Nothing, Yes"
		raw_input("Press any button to continue.")
		ktane()
	if b == "what":
		print "Uhhh, What"
		raw_input("Press any button to continue.")
		ktane()
	if b == "uhhh":
		print "Ready, Nothing, Left, What, Okay, Yes, Right, No, Press, Blank, Uhhh"
		raw_input("Press any button to continue.")
		ktane()
	if b == "left":
		print "Right, Left"
		raw_input("Press any button to continue.")
		ktane()
	if b == "right":
		print "Yes, Nothing, Ready, Press, No, Wait, What, Right"
		raw_input("Press any button to continue.")
		ktane()
	if b == "middle":
		print "Blank, Ready, Okay, What, Nothing, Press, No, Wait, Left, Middle"
		raw_input("Press any button to continue.")
		ktane()
	if b == "okay":
		print "Middle, No, First, Yes, Uhhh, Nothing, Wait, Okay"
		raw_input("Press any button to continue.")
		ktane()
	if b == "wait":
		print "Uhhh, No, Blank, Okay, Yes, Left, First, Press, What, Wait"
		raw_input("Press any button to continue.")
		ktane()
	if b == "press":
		print "Right, Middle, Yes, Ready, Press"
		raw_input("Press any button to continue.")
		ktane()
	if b == "you":
		print "Sure, You are, Your, You're, Next, Uh Huh, Ur, Hold, What? , You"
		raw_input("Press any button to continue.")
		ktane()
	if b == "you are":
		print "Your, Next, Like, Uh Huh, What? , Done, Uh Uh, Hold, You, U, You're, Sure, Ur, You Are"
		raw_input("Press any button to continue.")
		ktane()
	if b == "your":
		print "Uh Uh, You Are, Uh Huh, Your"
		raw_input("Press any button to continue.")
		ktane()
	if b == "you're":
		print "You, You're"
		raw_input("Press any button to continue.")
		ktane()
	if b == "ur":
		print "Done, U, Ur"
		raw_input("Press any button to continue.")
		ktane()
	if b == "u":
		print "Uh Huh, Sure, Next, What? , You're, Ur, Uh Uh, Done, U"
		raw_input("Press any button to continue.")
		ktane()
	if b == "uh huh":
		print "Uh Huh"
		raw_input("Press any button to continue.")
		ktane()
	if b == "uh uh":
		print "Ur, U, You are, You're, Next, Uh Uh"
		raw_input("Press any button to continue.")
		ktane()
	if b == "what?":
		print "You, Hold, You're, Your, U, Done, Uh Uh, Like, You Are, Uh Huh, Ur, Next, What?"
		raw_input("Press any button to continue.")
		ktane()
	if b == "done":
		print "Sure, Uh Huh, Next, What? , Your, Ur, You're, Hold, Like, You, U, You Are, Uh Uh, Done"
		raw_input("Press any button to continue.")
		ktane()
	if b == "next":
		print "What? , Uh Huh, Uh Uh, Your, Hold, Sure, Next"
		raw_input("Press any button to continue.")
		ktane()
	if b == "hold":
		print "You Are, U, Done, Uh Uh, You, Ur, Sure, What? , You're, Next, Hold"
		raw_input("Press any button to continue.")
		ktane()
	if b == "sure":
		print "You Are, Done, Like, You're, You, Hold, Uh Huh, Ur, Sure"
		raw_input("Press any button to continue.")
		ktane()
	if b == "like":
		print "You're, Next, U, Ur, Hold, Done, Uh Uh, What? , Uh Huh, You, Like"
		raw_input("Press any button to continue.")
		ktane()
	else:
		print "Invalid Word. Please Try Again."
		raw_input("Press any button to continue.")
		ktane()
def memory():
	# Memory
	# Variable [A]lpha: Current Display Number
	# Variable [B]ravo: 1st Position
	# Variable [C]harlie: 2nd Position
	# Variable [D]elta: 1st Label
	# Variable [E]cho: 2nd Label
	# Variable [F]oxtrot: 3rd Label
	# Variable [G]olf: 4th Label
	print "Stage 1."
	try:
		a = input("What is the Display Number? ")
	except NameError:
		print "Please only use numbers! Please try again."
		raw_input("Press any button to continue.")
		ktane()
	if a == 1 or a == 2:
		b = 2
		d = input("What is the button on the 2nd position? ")
		print "Press the button on the 2nd position." + "\n"
	if a == 3:
		b = 3
		d = input("What is the button on the 3rd position? ")
		print "Press the button on the 3rd position." + "\n"
	if a == 4:
		b = 4
		d = input("What is the button on the 4th position? ")
		print "Press the button on the 4th position." + "\n"
	try:
		if b == 2 or b == 3 or b == 4:
			print "Stage 2"
	except NameError:
		print "Unknown Number. Please try again."
		raw_input("Press any button to continue.")
		ktane()
	try:
		a = input("What is the Display Number? ")
	except NameError:
		print "Please only use numbers! Please try again."
		raw_input("Press any button to continue.")
		ktane()
	if a == 1:
		e = 4
		c = input("What is the position of the button labeled \"4\"? ")
		print "Press the button with the label 4." + "\n"
	if a == 2:
		c = b
		if b == 2:
			e = input("What is the button on the 2nd position? ")
		if b == 3:
			e = input("What is the button on the 3rd position? ")
		if b == 4:
			e = input("What is the button on the 4th position? ")
		print "Press the button with the label ", e
	if a == 3:
		c = 1
		e = input("What is the button in the 1st position? ")
		print "Press the button in the 1st position."
	if a == 4:
		c = b
		if b == 2:
			e = input("What is the button on the 2nd position? ")
		if b == 3:
			e = input("What is the button on the 3rd position? ")
		if b == 4:
			e = input("What is the button on the 4th position? ")
		print "Press the button."
	try:
		if c == 1 or c == 2 or c == 3 or c == 4 or e == 1 or e == 2 or e == 3 or e == 4:
			print "Stage 3"
	except NameError:
		print "Unknown Number. Please try again."
		raw_input("Press any button to continue.")
		ktane()
	try:
		a = input("What is the Display Number? ")
	except NameError:
		print "Please only use numbers! Please try again."
		raw_input("Press any button to continue.")
		ktane()
	if a == 1:
		f = e
		print "Press the button with the label ", e
	if a == 2:
		f = d
		print "Press the button with the label ", d
	if a == 3:
		f = input("What is the button on the 3rd position? ")
		print "Press the button on the 3rd position."
	if a == 4:
		f = 4
		print "Press the button with the label \"4\"."
	try:
		if f == 1 or f == 2 or f == 3 or f == 4:
			print "Stage 4"
	except NameError:
		print "Unknown Number. Please try again."
		raw_input("Press any button to continue.")
		ktane()
	try:
		a = input("What is the Display Number? ")
	except NameError:
		print "Please only use numbers! Please try again."
		raw_input("Press any button to continue.")
		ktane()
	if a == 1:
		if b == 1:
			g = input("What is the button on the 1st position? ")
			print "Press the button on the 1st position.\n"
		if b == 2:
			g = input("What is the button on the 2nd position? ")
			print "Press the button on the 2nd position.\n"
		if b == 3:
			g = input("What is the button on the 3rd position? ")
			print "Press the button on the 3rd position.\n"
		if b == 4:
			g = input("What is the button on the 4th position? ")
			print "Press the button on the 4th position.\n"
	if a == 2:
		g = input("What is the button on the 1st position?")
		print "Press the button on the 1st position.\n"
	if a == 3 or a == 4:
		if c == 1:
			g = input("What is the button on the 1st position? ")
			print "Press the button on the 1st position.\n"
		if c == 2:
			g = input("What is the button on the 2nd position? ")
			print "Press the button on the 2nd position.\n"
		if c == 3:
			g = input("What is the button on the 3rd position? ")
			print "Press the button on the 3rd position.\n"
		if c == 4:
			g = input("What is the button on the 4th position? ")
			print "Press the button on the 4th position.\n"
	try:
		if g == 1 or g == 2 or g == 3 or g == 4:
			print "Stage 5"
	except NameError:
		print "Unknown Number. Please try again."
		raw_input("Press any button to continue.")
		ktane()
	try:
		a = input("What is the Display Number? ")
	except NameError:
		print "Please only use numbers! Please try again."
		raw_input("Press any button to continue.")
		ktane()
	if a == 1:
		print "Press the button with the label ", d
	if a == 2:
		print "Press the button with the label ", e
	if a == 3:
		print "Press the button with the label ", g
	if a == 4:
		print "Press the button with the label ", f
	raw_input("Press any button to continue.")
	ktane()
def morseCode():
	# Morse Code
	# Variable [A]lpha: 1st letter
	# Variable [B]ravo: 2nd letter
	# Variable [C]harlie: 3rd letter
	print "Please don't seperate dots and dashes with spaces."
	a = raw_input("What is the first letter? ")
	if a == "..-.":
		print "3.555 MHz"
		raw_input("Press any button to continue.")
		ktane()
	if a == "....":
		print "3.515 MHz"
		raw_input("Press any button to continue.")
		ktane()
	if a == ".-..":
		print "3.542 MHz"
		raw_input("Press any button to continue.")
		ktane()
	if a == "-":
		print "3.532 MHz"
		raw_input("Press any button to continue.")
		ktane()
	if a == "...-":
		print "3.595 MHz"
		raw_input("Press any button to continue.")
		ktane()
	if a == "-...":
		b = raw_input("What is the second letter? ")
		if b == ".":
			print "3.600 MHz"
			raw_input("Press any button to continue.")
			ktane()
		if b == "..":
			print "3.552 MHz"
			raw_input("Press any button to continue.")
			ktane()
		if b == "---":
			c = raw_input("What is the third letter? ")
			if c == "--":
				print "3.565 MHz"
				raw_input("Press any button to continue.")
				ktane()
			if c == "-..-":
				print "3.535 MHz"
				raw_input("Press any button to continue.")
				ktane()
		if b == ".-.":
			c = raw_input("What is the third letter? ")
			if c == ".":
				print "3.572 MHz"
				raw_input("Press any button to continue.")
				ktane()
			if c == "..":
				print "3.575 MHz"
				raw_input("Press any button to continue.")
				ktane()
	if a == "...":
		b = raw_input("What is the second letter? ")
		if b == "....":
			print "3.505 MHz"
			raw_input("Press any button to continue.")
			ktane()
		if b == ".-..":
			print "3.522 MHz"
			raw_input("Press any button to continue.")
			ktane()
		if b == "-":
			c = raw_input("What is the third letter? ")
			if c == ".":
				print "3.582 MHz"
				raw_input("Press any button to continue.")
				ktane()
			if c == "..":
				print "3.592 MHz"
				raw_input("Press any button to continue.")
				ktane()
			if c == ".-.":
				print "3.545 MHz"
				raw_input("Press any button to continue.")
				ktane()
	else:
		print "Invalid letter. Please try again."
		raw_input("Press any button to continue.")
		ktane()
def complicatedWires():
	# Complicated Wires
	# Variable [A]lpha: Red Coloring
	# Variable [B]ravo: Blue Coloring
	# Variable [C]harlie: LED
	# Variable [D]elta: Star
	print "For \"yes\", please respond with \"y\"."
	print "For \"no\", please respond with \"n\"."
	a = raw_input("Does the wire have red coloring? ")
	b = raw_input("Does the wire have blue coloring? ")
	if a == "n":
		c = raw_input("Does the wire have it's LED on? ")
		if b == "n" and c == "n":
			print "Cut."
			raw_input("Press any button to continue.")
			ktane()
		if b == "y" and c == "y":
			print "Cut if there's a Parallel Port. (They're the pink ones)"
			raw_input("Press any button to continue.")
			ktane()
		d = raw_input("Does the wire have a star? ")
		if b == "n" and c == "y" and d == "n":
			print "Don't cut."
			raw_input("Press any button to continue.")
			ktane()
		if b == "n" and c == "y" and d == "y":
			print "Cut if there are more than 2 batteries."
			raw_input("Press any button to continue.")
			ktane()
		if b == "y" and c == "n" and d == "n":
			print "Cut if the last digit of the SN is even."
			raw_input("Press any button to continue.")
			ktane()
		if b == "y" and c == "n" and d == "y":
			print "Don't cut."
			raw_input("Press any button to continue.")
			ktane()
	if a == "y":
		c = raw_input("Does the wire have a star? ")
		if b == "y" and c == "n":
			print "Cut if the last digit of the SN is even."
			raw_input("Press any button to continue.")
			ktane()
		d = raw_input("Does the wire have it's LED on? ")
		if b == "n" and c == "n" and d == "n":
			print "Cut if the last digit of the SN is even."
			raw_input("Press any button to continue.")
			ktane()
		if b == "n" and c == "n" and d == "y":
			print "Cut if there are more than 2 batteries."
			raw_input("Press any button to continue.")
			ktane()
		if b == "n" and c == "y" and d == "n":
			print "Cut."
			raw_input("Press any button to continue.")
			ktane()
		if b == "n" and c == "y" and d == "y":
			print "Cut if there are more than 2 batteries."
			raw_input("Press any button to continue.")
			ktane()
		if b == "y" and c == "y" and d == "n":
			print "Cut if there's a Parallel Port. (They're the pink ones)"
			raw_input("Press any button to continue.")
			ktane()
		if b == "y" and c == "y" and d == "y":
			print "Don't cut."
			raw_input("Press any button to continue.")
			raw_input("Press any button to continue.")
			ktane()
	else:
		print "Invalid response! Please try again."
		raw_input("Press any button to continue.")
		ktane()
def wireSequences():
	# Wire Sequences
	# Variable [A]lpha: Red occurrences
	# Variable [B]ravo: Blue occurrences
	# Variable [C]harlie: Black occurrences
	# Variable [D]elta + Number: Wires
	a = 0
	b = 0
	c = 0
	print "\"r\" for Red"
	print "\"bu\" for Blue"
	print "\"ba\" for Black"
	print "\"n\" for nothing"
	# 1st Stage
	d1 = raw_input("What is the color for the 1st wire? ")
	d2 = raw_input("2nd? ")
	d3 = raw_input("3rd? ")
	if d1 == "r":
		a = a + 1
		print "Cut the 1st wire if it's connected to C."
	if d1 == "bu":
		b = b + 1
		print "Cut the 1st wire if it's connected to B."
	if d1 == "ba":
		c = c + 1
		print "Cut the 1st wire."
	if d2 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 2nd wire if it's connected to C."
		if a == 2:
			print "Cut the 2nd wire if it's connected to B."
	if d2 == "bu":
		b = b + 1
		if b == 1:
			print "Cut the 2nd wire if it's connected to B."
		if b == 2:
			print "Cut the 2nd wire if it's connected to A or C."
	if d2 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 2nd wire."
		if c == 2:
			print "Cut the 2nd wire if it's connected to A or C."
	if d3 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 3rd wire if it's connected to C."
		if a == 2:
			print "Cut the 3rd wire if it's connected to B."
		if a == 3:
			print "Cut the 3rd wire if it's connected to A."
	if d3 == "bu":
		b = b + 1
		if b == 1 or b == 3:
			print "Cut the 3rd wire if it's connected to B."
		if b == 2:
			print "Cut the 3rd wire if it's connected to A or C."
	if d3 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 3rd wire."
		if c == 2:
			print "Cut the 3rd wire if it's connected to A or C."
		if c == 3:
			print "Cut the 3rd wire if it's connected to B."
	# Stage 2
	print "Next Stage.\n"
	d4 = raw_input("What is the color for the 4th wire? ")
	d5 = raw_input("5th? ")
	d6 = raw_input("6th? ")
	if d4 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 4th wire if it's connected to C."
		if a == 2:
			print "Cut the 4th wire if it's connected to B."
		if a == 3:
			print "Cut the 4th wire if it's connected to A."
		if a == 4:
			print "Cut the 4th wire if it's connected to A or C."
	if d4 == "bu":
		b = b + 1
		if b == 1 or b == 3:
			print "Cut the 4th wire if it's connected to B."
		if b == 2:
			print "Cut the 4th wire if it's connected to A or C."
		if b == 4:
			print "Cut the 4th wire if it's connected to A."
	if d4 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 4th wire."
		if c == 2 or c == 4:
			print "Cut the 4th wire if it's connected to A or C."
		if c == 3:
			print "Cut the 4th wire if it's connected to B."
	if d5 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 5th wire if it's connected to C."
		if a == 2 or a == 5:
			print "Cut the 5th wire if it's connected to B."
		if a == 3:
			print "Cut the 5th wire if it's connected to A."
		if a == 4:
			print "Cut the 5th wire if it's connected to A or C."
	if d5 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 5th wire if it's connected to B."
		if b == 2:
			print "Cut the 5th wire if it's connected to A or C."
		if b == 4:
			print "Cut the 5th wire if it's connected to A."
	if d5 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 5th wire."
		if c == 2 or c == 4:
			print "Cut the 5th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 5th wire if it's connected to B."
	if d6 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 6th wire if it's connected to C."
		if a == 2 or a == 5:
			print "Cut the 6th wire if it's connected to B."
		if a == 3:
			print "Cut the 6th wire if it's connected to A."
		if a == 4 or a == 6:
			print "Cut the 6th wire if it's connected to A or C."
	if d6 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 6th wire if it's connected to B."
		if b == 2:
			print "Cut the 6th wire if it's connected to A or C."
		if b == 4:
			print "Cut the 6th wire if it's connected to A."
		if b == 6:
			print "Cut the 6th wire if it's connected to B or C."
	if d6 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 6th wire."
		if c == 2 or c == 4:
			print "Cut the 6th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 6th wire if it's connected to B."
		if c == 6:
			print "Cut the 6th wire if it's connected to B or C."
	# Stage 3
	print "Next Stage.\n"
	d7 = raw_input("What is the color for the 7th wire? ")
	d8 = raw_input("8th? ")
	d9 = raw_input("9th? ")
	if d7 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 7th wire if it's connected to C."
		if a == 2 or a == 5:
			print "Cut the 7th wire if it's connected to B."
		if a == 3:
			print "Cut the 7th wire if it's connected to A."
		if a == 4 or a == 6:
			print "Cut the 7th wire if it's connected to A or C."
		if a == 7:
			print "Cut the 7th wire."
	if d7 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 7th wire if it's connected to B."
		if b == 2:
			print "Cut the 7th wire if it's connected to A or C."
		if b == 4:
			print "Cut the 7th wire if it's connected to A."
		if b == 6:
			print "Cut the 7th wire if it's connected to B or C."
		if b == 7:
			print "Cut the 7th wire if it's connected to C."
	if d7 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 7th wire."
		if c == 2 or c == 4:
			print "Cut the 7th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 7th wire if it's connected to B."
		if c == 6:
			print "Cut the 7th wire if it's connected to B or C."
		if c == 7:
			print "Cut the 7th wire if it's connected to A or B."
	if d8 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 8th wire if it's connected to C."
		if a == 2 or a == 5:
			print "Cut the 8th wire if it's connected to B."
		if a == 3:
			print "Cut the 8th wire if it's connected to A."
		if a == 4 or a == 6:
			print "Cut the 8th wire if it's connected to A or C."
		if a == 7:
			print "Cut the 8th wire."
		if a == 8:
			print "Cut the 8th wire if it's connected to A or B."
	if d8 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 8th wire if it's connected to B."
		if b == 2 or b == 8:
			print "Cut the 8th wire if it's connected to A or C."
		if b == 4:
			print "Cut the 8th wire if it's connected to A."
		if b == 6:
			print "Cut the 8th wire if it's connected to B or C."
		if b == 7:
			print "Cut the 8th wire if it's connected to C."
	if d8 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 8th wire."
		if c == 2 or c == 4:
			print "Cut the 8th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 8th wire if it's connected to B."
		if c == 6:
			print "Cut the 8th wire if it's connected to B or C."
		if c == 7:
			print "Cut the 8th wire if it's connected to A or B."
		if c == 8:
			print "Cut the 8th wire if it's connected to C."
	if d9 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 9th wire if it's connected to C."
		if a == 2 or a == 5 or a == 9:
			print "Cut the 9th wire if it's connected to B."
		if a == 3:
			print "Cut the 9th wire if it's connected to A."
		if a == 4 or a == 6:
			print "Cut the 9th wire if it's connected to A or C."
		if a == 7:
			print "Cut the 9th wire."
		if a == 8:
			print "Cut the 9th wire if it's connected to A or B."
	if d9 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 9th wire if it's connected to B."
		if b == 2 or b == 8:
			print "Cut the 9th wire if it's connected to A or C."
		if b == 4 or b == 9:
			print "Cut the 9th wire if it's connected to A."
		if b == 6:
			print "Cut the 9th wire if it's connected to B or C."
		if b == 7:
			print "Cut the 9th wire if it's connected to C."
	if d9 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 9th wire."
		if c == 2 or c == 4:
			print "Cut the 9th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 9th wire if it's connected to B."
		if c == 6:
			print "Cut the 9th wire if it's connected to B or C."
		if c == 7:
			print "Cut the 9th wire if it's connected to A or B."
		if c == 8 or c == 9:
			print "Cut the 9th wire if it's connected to C."
	# Stage 4
	print "Next Stage.\n"
	d10 = raw_input("What is the color for the 10th wire? ")
	d11 = raw_input("11th? ")
	d12 = raw_input("12th? ")
	if d10 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 10th wire if it's connected to C."
		if a == 2 or a == 5 or a == 9:
			print "Cut the 10th wire if it's connected to B."
		if a == 3:
			print "Cut the 10th wire if it's connected to A."
		if a == 4 or a == 6:
			print "Cut the 10th wire if it's connected to A or C."
		if a == 7:
			print "Cut the 10th wire."
		if a == 8:
			print "Cut the 10th wire if it's connected to A or B."
	if d10 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 10th wire if it's connected to B."
		if b == 2 or b == 8:
			print "Cut the 10th wire if it's connected to A or C."
		if b == 4 or b == 9:
			print "Cut the 10th wire if it's connected to A."
		if b == 6:
			print "Cut the 10th wire if it's connected to B or C."
		if b == 7:
			print "Cut the 10th wire if it's connected to C."
	if d10 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 10th wire."
		if c == 2 or c == 4:
			print "Cut the 10th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 10th wire if it's connected to B."
		if c == 6:
			print "Cut the 10th wire if it's connected to B or C."
		if c == 7:
			print "Cut the 10th wire if it's connected to A or B."
		if c == 8 or c == 9:
			print "Cut the 10th wire if it's connected to C."
	if d11 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 11th wire if it's connected to C."
		if a == 2 or a == 5 or a == 9:
			print "Cut the 11th wire if it's connected to B."
		if a == 3:
			print "Cut the 11th wire if it's connected to A."
		if a == 4 or a == 6:
			print "Cut the 11th wire if it's connected to A or C."
		if a == 7:
			print "Cut the 11th wire."
		if a == 8:
			print "Cut the 11th wire if it's connected to A or B."
	if d11 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 11th wire if it's connected to B."
		if b == 2 or b == 8:
			print "Cut the 11th wire if it's connected to A or C."
		if b == 4 or b == 9:
			print "Cut the 11th wire if it's connected to A."
		if b == 6:
			print "Cut the 11th wire if it's connected to B or C."
		if b == 7:
			print "Cut the 11th wire if it's connected to C."
	if d11 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 11th wire."
		if c == 2 or c == 4:
			print "Cut the 11th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 11th wire if it's connected to B."
		if c == 6:
			print "Cut the 11th wire if it's connected to B or C."
		if c == 7:
			print "Cut the 11th wire if it's connected to A or B."
		if c == 8 or c == 9:
			print "Cut the 11th wire if it's connected to C."
	if d12 == "r":
		a = a + 1
		if a == 1:
			print "Cut the 12th wire if it's connected to C."
		if a == 2 or a == 5 or a == 9:
			print "Cut the 12th wire if it's connected to B."
		if a == 3:
			print "Cut the 12th wire if it's connected to A."
		if a == 4 or a == 6:
			print "Cut the 12th wire if it's connected to A or C."
		if a == 7:
			print "Cut the 12th wire."
		if a == 8:
			print "Cut the 12th wire if it's connected to A or B."
	if d12 == "bu":
		b = b + 1
		if b == 1 or b == 3 or b == 5:
			print "Cut the 12th wire if it's connected to B."
		if b == 2 or b == 8:
			print "Cut the 12th wire if it's connected to A or C."
		if b == 4 or b == 9:
			print "Cut the 12th wire if it's connected to A."
		if b == 6:
			print "Cut the 12th wire if it's connected to B or C."
		if b == 7:
			print "Cut the 12th wire if it's connected to C."
	if d12 == "ba":
		c = c + 1
		if c == 1:
			print "Cut the 12th wire."
		if c == 2 or c == 4:
			print "Cut the 12th wire if it's connected to A or C."
		if c == 3 or c == 5:
			print "Cut the 12th wire if it's connected to B."
		if c == 6:
			print "Cut the 12th wire if it's connected to B or C."
		if c == 7:
			print "Cut the 12th wire if it's connected to A or B."
		if c == 8 or c == 9:
			print "Cut the 12th wire if it's connected to C."
def mazes():
	# Mazes
	# Variable [A]lpha: 1st Indicator
	# Variable [B]ravo: 2nd Indicator
	print "[1A][1B][1C][1D][1E][1F]"
	print "[2A][2B][2C][2D][2E][2F]"
	print "[3A][3B][3C][3D][3E][3F]"
	print "[4A][4B][4C][4D][4E][4F]"
	print "[5A][5B][5C][5D][5E][5F]"
	print "[6A][6B][6C][6D][6E][6F]"
	print "Responses are case-sensitive and are meant to be typed with ALL CAPS."
	a = raw_input("Where is the 1st Indicator? ")
	b = raw_input("Where is the 2nd Indicator? ")
	if a == "2A" and b == "3F":
		print "! = indicators"
		print " .  _._  . | .  _.___._"
		print " ! | .  _._|_.___._  ."
		print " . |_._  . | .  _._  !"
		print " . |_.___.___._|_._  ."
		print " .  _._  . | .  _._| ."
		print " .   . | .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "4B" and b == "2E":
		print "! = indicators"
		print "_._  .  _._| .   .  _._"
		print " .  _._| .  _._|_!_  ."
		print " . | .  _._| .  _._  ."
		print " .  _!_| .  _._| . | ."
		print " . | . | . | .  _._| ."
		print " . | .   . | .   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "4D" and b == "4F":
		print "! = indicators"
		print " .  _._  . | . | .   ."
		print "_._| . | . |_.___._| ."
		print " .   . | . | .   . | ."
		print " . | . | . | ! | . | !"
		print " . |_.___._| . | . | ."
		print " .   .   .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "1A" and b == "4A":
		print "! = indicators"
		print " !   . |_.___.___._  ."
		print " . | . | .  _.___._  ."
		print " . |_.___._| .  _._| ."
		print " ! |_.___.___.___._  ."
		print " .  _.___.___._  . | ."
		print " .   .   . | .   . | ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "3E" and b == "6D":
		print "! = indicators"
		print "_.___.___.___._  .   ."
		print " .  _.___._  .  _._|_._"
		print " .   . |_.___._| !   ."
		print " . |_.___._  . |_._| ."
		print " . | .  _.___.___._| ."
		print " . | .   .   !   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "1E" and b == "5C":
		print "! = indicators"
		print " . | .   . |_._  !   ."
		print " . | . | . | .  _._| ."
		print " .  _._|_._| . | .  _._"
		print "_._  . | .   . | . | ."
		print " .  _._|_!_| . |_._  ."
		print " .   .   .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "1B" and b == "6B":
		print "! = indicators"
		print " .  _!___._  . | .   ."
		print " . | .  _._|_.___._| ."
		print "_.___._| .  _._| .  _._"
		print " .   . | .  _.___._| ."
		print " . |_._|_.___._  . | ."
		print " .   !   .   .   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "1D" and b == "4C":
		print "! = indicators"
		print " . | .  _._  ! | .   ."
		print " .  _.___._|_.___._| ."
		print " . | .  _.___._  . | ."
		print " . |_._  ! |_.___.___._"
		print " . | . |_.___.___.___._"
		print " .   .   .   .   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "2C" and b == "5A":
		print "! = indicators"
		print " . | .  _.___._  .   ."
		print " . | . | !  _._| . | ."
		print " .  _.___._| .  _._| ."
		print " . | . | .  _._|_._  ."
		print " ! | . | . | .   . |_._"
		print " .   . | .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	# Reversed
	if a == "3F" and b == "2A":
		print "! = indicators"
		print " .  _._  . | .  _.___._"
		print " ! | .  _._|_.___._  ."
		print " . |_._  . | .  _._  !"
		print " . |_.___.___._|_._  ."
		print " .  _._  . | .  _._| ."
		print " .   . | .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "2E" and b == "4B":
		print "! = indicators"
		print "_._  .  _._| .   .  _._"
		print " .  _._| .  _._|_!_  ."
		print " . | .  _._| .  _._  ."
		print " .  _!_| .  _._| . | ."
		print " . | . | . | .  _._| ."
		print " . | .   . | .   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "4F" and b == "4D":
		print "! = indicators"
		print " .  _._  . | . | .   ."
		print "_._| . | . |_.___._| ."
		print " .   . | . | .   . | ."
		print " . | . | . | ! | . | !"
		print " . |_.___._| . | . | ."
		print " .   .   .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "4A" and b == "1A":
		print "! = indicators"
		print " !   . |_.___.___._  ."
		print " . | . | .  _.___._  ."
		print " . |_.___._| .  _._| ."
		print " ! |_.___.___.___._  ."
		print " .  _.___.___._  . | ."
		print " .   .   . | .   . | ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "6D" and b == "3E":
		print "! = indicators"
		print "_.___.___.___._  .   ."
		print " .  _.___._  .  _._|_._"
		print " .   . |_.___._| !   ."
		print " . |_.___._  . |_._| ."
		print " . | .  _.___.___._| ."
		print " . | .   .   !   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "5C" and b == "1E":
		print "! = indicators"
		print " . | .   . |_._  !   ."
		print " . | . | . | .  _._| ."
		print " .  _._|_._| . | .  _._"
		print "_._  . | .   . | . | ."
		print " .  _._|_!_| . |_._  ."
		print " .   .   .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "6B" and b == "1B":
		print "! = indicators"
		print " .  _!___._  . | .   ."
		print " . | .  _._|_.___._| ."
		print "_.___._| .  _._| .  _._"
		print " .   . | .  _.___._| ."
		print " . |_._|_.___._  . | ."
		print " .   !   .   .   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "4C" and b == "1D":
		print "! = indicators"
		print " . | .  _._  ! | .   ."
		print " .  _.___._|_.___._| ."
		print " . | .  _.___._  . | ."
		print " . |_._  ! |_.___.___._"
		print " . | . |_.___.___.___._"
		print " .   .   .   .   .   ."
		raw_input("Press anything to continue.")
		ktane()
	if a == "5A" and b == "2C":
		print "! = indicators"
		print " . | .  _.___._  .   ."
		print " . | . | !  _._| . | ."
		print " .  _.___._| .  _._| ."
		print " . | . | .  _._|_._  ."
		print " ! | . | . | .   . |_._"
		print " .   . | .   . | .   ."
		raw_input("Press anything to continue.")
		ktane()
	else:
		print "Incorrect positions!"
		raw_input("Press anything to continue.")
		mazes()
def passwords():
	# Passwords
	# Variable [A]lpha + Number: 3rd letter
	# Variable [B]ravo + Number: 5th letter
	print "Please leave responses in lower caps."
	a1 = raw_input("What is the 1st letter of the 3rd set? ")
	a2 = raw_input("What is the 2nd letter of the 3rd set? ")
	a3 = raw_input("What is the 3rd letter of the 3rd set? ")
	a4 = raw_input("What is the 4th letter of the 3rd set? ")
	a5 = raw_input("What is the 5th letter of the 3rd set? ")
	a6 = raw_input("What is the 6th letter of the 3rd set? ")
	b1 = raw_input("What is the 1st letter of the 5th set? ")
	b2 = raw_input("What is the 2nd letter of the 5th set? ")
	b3 = raw_input("What is the 3rd letter of the 5th set? ")
	b4 = raw_input("What is the 4th letter of the 5th set? ")
	b5 = raw_input("What is the 5th letter of the 5th set? ")
	b6 = raw_input("What is the 6th letter of the 5th set? ")
	if a1 == "a" or a2 == "a" or a3 == "a" or a4 == "a" or a5 == "a" or a6 == "a":
		if b1 == "e" or b2 == "e" or b3 == "e" or b4 == "e" or b5 == "e" or b6 == "e":
			print "PLACE"
		if b1 == "n" or b2 == "n" or b3 == "n" or b4 == "n" or b5 == "n" or b6 == "n":
			print "AGAIN"
			print "LEARN"
		if b1 == "l" or b2 == "l" or b3 == "l" or b4 == "l" or b5 == "l" or b6 == "l":
			print "SMALL"
		if b1 == "t" or b2 == "t" or b3 == "t" or b4 == "t" or b5 == "t" or b6 == "t":
			print "PLANT"
	if a1 == "e" or a2 == "e" or a3 == "e" or a4 == "e" or a5 == "e" or a6 == "e":
		if b1 == "e" or b2 == "e" or b3 == "e" or b4 == "e" or b5 == "e" or b6 == "e":
			print "THERE"
			print "THESE"
			print "WHERE"
		if b1 == "l" or b2 == "l" or b3 == "l" or b4 == "l" or b5 == "l" or b6 == "l":
			print "SPELL"
		if b1 == "r" or b2 == "r" or b3 == "r" or b4 == "r" or b5 == "r" or b6 == "r":
			print "THEIR"
		if b1 == "t" or b2 == "t" or b3 == "t" or b4 == "t" or b5 == "t" or b6 == "t":
			print "GREAT"
		if b1 == "y" or b2 == "y" or b3 == "y" or b4 == "y" or b5 == "y" or b6 == "y":
			print "EVERY"
	if a1 == "g" or a2 == "g" or a3 == "g" or a4 == "g" or a5 == "g" or a6 == "g":
		if b1 == "t" or b2 == "t" or b3 == "t" or b4 == "t" or b5 == "t" or b6 == "t":
			print "RIGHT"
	if a1 == "h" or a2 == "h" or a3 == "h" or a4 == "h" or a5 == "h" or a6 == "h":
		if b1 == "r" or b2 == "r" or b3 == "r" or b4 == "r" or b5 == "r" or b6 == "r":
			print "OTHER"
	if a1 == "i" or a2 == "i" or a3 == "i" or a4 == "i" or a5 == "i" or a6 == "i":
		if b1 == "e" or b2 == "e" or b3 == "e" or b4 == "e" or b5 == "e" or b6 == "e":
			print "WRITE"
		if b1 == "g" or b2 == "g" or b3 == "g" or b4 == "g" or b5 == "g" or b6 == "g":
			print "THING"
		if b1 == "h" or b2 == "h" or b3 == "h" or b4 == "h" or b5 == "h" or b6 == "h":
			print "WHICH"
		if b1 == "k" or b2 == "k" or b3 == "k" or b4 == "k" or b5 == "k" or b6 == "k":
			print "THINK"
		if b1 == "l" or b2 == "l" or b3 == "l" or b4 == "l" or b5 == "l" or b6 == "l":
			print "STILL"
		if b1 == "t" or b2 == "t" or b3 == "t" or b4 == "t" or b5 == "t" or b6 == "t":
			print "POINT"
	if a1 == "l" or a2 == "l" or a3 == "l" or a4 == "l" or a5 == "l" or a6 == "l":
		if b1 == "w" or b2 == "w" or b3 == "w" or b4 == "w" or b5 == "w" or b6 == "w":
			print "BELOW"
	if a1 == "o" or a2 == "o" or a3 == "o" or a4 == "o" or a5 == "o" or a6 == "o":
		if b1 == "t" or b2 == "t" or b3 == "t" or b4 == "t" or b5 == "t" or b6 == "t":
			print "ABOUT"
	if a1 == "r" or a2 == "r" or a3 == "r" or a4 == "r" or a5 == "r" or a6 == "r":
		if b1 == "d" or b2 == "d" or b3 == "d" or b4 == "d" or b5 == "d" or b6 == "d":
			print "WORLD"
		if b1 == "e" or b2 == "e" or b3 == "e" or b4 == "e" or b5 == "e" or b6 == "e":
			print "LARGE"
			print "THREE"
		if b1 == "t" or b2 == "t" or b3 == "t" or b4 == "t" or b5 == "t" or b6 == "t":
			print "FIRST"
	if a1 == "t" or a2 == "t" or a3 == "t" or a4 == "t" or a5 == "t" or a6 == "t":
		if b1 == "r" or b2 == "r" or b3 == "r" or b4 == "r" or b5 == "r" or b6 == "r":
			print "WATER"
			print "AFTER"
	if a1 == "u" or a2 == "u" or a3 == "u" or a4 == "u" or a5 == "u" or a6 == "u":
		if b1 == "d" or b2 == "d" or b3 == "d" or b4 == "d" or b5 == "d" or b6 == "d":
			print "COULD"
			print "FOUND"
			print "SOUND"
			print "WOULD"
		if b1 == "e" or b2 == "e" or b3 == "e" or b4 == "e" or b5 == "e" or b6 == "e":
			print "HOUSE"
		if b1 == "y" or b2 == "y" or b3 == "y" or b4 == "y" or b5 == "y" or b6 == "y":
			print "STUDY"
	if a1 == "v" or a2 == "v" or a3 == "v" or a4 == "v" or a5 == "v" or a6 == "v":
		if b1 == "r" or b2 == "r" or b3 == "r" or b4 == "r" or b5 == "r" or b6 == "r":
			print "NEVER"
	raw_input("Press any button to continue.")
	ktane()
def gas():
	print "Detonate - N"
	print "Vent Gas - Y"
	raw_input("Press any button to continue.")
	ktane()
def capacitorDischarger():
	print "Pull down the lever whenever you can."
	raw_input("Press any button to continue.")
	ktane()
def knobs():
	print "Up Position:"
	print "001011      101010"
	print "111101      011011"
	print ""
	print "Down Position:"
	print "011001      101010"
	print "111101      010001"
	print ""
	print "Left Position:"
	print "000010      000010"
	print "100111      000110"
	print ""
	print "Right Position:"
	print "101111      101100"
	print "111010      111010"
	raw_input("Press any button to continue.")
	ktane()
def brokenButtons():
	# Broken Buttons
	# Mod by samfun123 and can be downloaded here: https://steamcommunity.com/sharedfiles/filedetails/?id=817404979
	# Variable [A]lpha + Number: 1st row
	# Variable [B]ravo + Number: 2nd row
	# Variable [C]harlie + Number: 3rd row
	# Variable [D]elta + Number: 4th row
	# Variable [E]cho + Number: Presses
	# Variable [F]oxtrot: Correct Submit Button. 1 is Left and 2 is Right
	# Variable [G]olf: Duplicate Checker
	# Variable [H]otel: Locations for 1st duplicate button
	# Variable [I]ndia: Location Checker
	# Variable [J]uliett: Letter E Checker (If it's in the first button pressed)
	# Possible Words: https://pastebin.com/GvFCF0Pm
	e = 0
	g = 0
	f = 1
	j = 0
	print "Please respond in lower caps."
	print "If blank, respond with a space."
	print "If there's a hyphen (-) inbetween, please use a hyphen and not an underscore (_)"
	a1 = raw_input("What is the 1st button? ")
	a2 = raw_input("2nd? ")
	a3 = raw_input("3rd? ")
	b1 = raw_input("4th? ")
	b2 = raw_input("5th? ")
	b3 = raw_input("6th? ")
	c1 = raw_input("7th? ")
	c2 = raw_input("8th? ")
	c3 = raw_input("9th? ")
	d1 = raw_input("10th? ")
	d2 = raw_input("11th? ")
	d3 = raw_input("12th? ")
	# If it's sea, press it.
	if a1 == "sea" or a2 == "sea" or a3 == "sea" or b1 == "sea" or b2 == "sea" or b3 == "sea" or c1 == "sea" or c2 == "sea" or c3 == "sea" or d1 == "sea" or d2 == "sea" or d3 == "sea":
		print "Press the button with the word \"sea\""
		e = e + 1
		if e == 1:
			j = 1
		# Text change
		if a1 == "sea":
			a1 = raw_input("What is the button's text now? ")
		if a2 == "sea":
			a2 = raw_input("What is the button's text now? ")
		if a3 == "sea":
			a3 = raw_input("What is the button's text now? ")
		if b1 == "sea":
			b1 = raw_input("What is the button's text now? ")
		if b2 == "sea":
			b2 = raw_input("What is the button's text now? ")
		if b3 == "sea":
			b3 = raw_input("What is the button's text now? ")
		if c1 == "sea":
			c1 = raw_input("What is the button's text now? ")
		if c2 == "sea":
			c2 = raw_input("What is the button's text now? ")
		if c3 == "sea":
			c3 = raw_input("what is the button's text now? ")
		if d1 == "sea":
			d1 = raw_input("What is the button's text now? ")
		if d2 == "sea":
			d2 = raw_input("What is the button's text now? ")
		if d3 == "sea":
			d3 = raw_input("What is the button's text now? ")
	# If any button on the 1st or 3rd row starts with T, press it.
	if a1 == "that" or a2 == "that" or a3 == "that" or c1 == "that" or c2 == "that" or c3 == "that":
		print "Press the button with the word \"that\" (The one that's in the 1st or 3rd row if there are multiple ones)"
		e = e + 1
		# Text change
		if a1 == "that":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "that":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "that":
			a3 = raw_input("What is the button's text now? ")
		elif c1 == "that":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "that":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "that":
			c3 = raw_input("What is the button's text now? ")
	if a1 == "thing" or a2 == "thing" or a3 == "thing" or c1 == "thing" or c2 == "thing" or c3 == "thing":
		print "Press the button with the word \"thing\" (The one that's in the 1st or 3rd row if there are multiple ones)"
		e = e + 1
		# Text change
		if a1 == "thing":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "thing":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "thing":
			a3 = raw_input("What is the button's text now? ")
		elif c1 == "thing":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "thing":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "thing":
			c3 = raw_input("What is the button's text now? ")
	if a1 == "this" or a2 == "this" or a3 == "this" or c1 == "this" or c2 == "this" or c3 == "this":
		print "Press the button with the word \"this\" (The one that's in the 1st or 3rd row if there are multiple ones)"
		e = e + 1
		# Text change
		if a1 == "this":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "this":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "this":
			a3 = raw_input("What is the button's text now? ")
		elif c1 == "this":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "this":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "this":
			c3 = raw_input("What is the button's text now? ")
	if a1 == "three" or a2 == "three" or a3 == "three" or c1 == "three" or c2 == "three" or c3 == "three":
		print "Press the button with the word \"three\" (The one that's in the 1st or 3rd row if there are multiple ones)"
		e = e + 1
		# Text change
		if a1 == "three":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "three":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "three":
			a3 = raw_input("What is the button's text now? ")
		elif c1 == "three":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "three":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "three":
			c3 = raw_input("What is the button's text now? ")
	if a1 == "to" or a2 == "to" or a3 == "to" or c1 == "to" or c2 == "to" or c3 == "to":
		print "Press the button with the word \"to\" (The one that's in the 1st or 3rd row if there are multiple ones)"
		e = e + 1
		# Text change
		if a1 == "to":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "to":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "to":
			a3 = raw_input("What is the button's text now? ")
		elif c1 == "to":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "to":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "to":
			c3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	if a1 == "too" or a2 == "too" or a3 == "too" or c1 == "too" or c2 == "too" or c3 == "too":
		print "Press the button with the word \"too\" (The one that's in the 1st or 3rd row if there are multiple ones)"
		e = e + 1
		# Text change
		if a1 == "too":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "too":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "too":
			a3 = raw_input("What is the button's text now? ")
		elif c1 == "too":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "too":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "too":
			c3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	if a1 == "two" or a2 == "two" or a3 == "two" or c1 == "two" or c2 == "two" or c3 == "two":
		print "Press the button with the word \"two\" (The one that's in the 1st or 3rd row if there are multiple ones)"
		e = e + 1
		# Text change
		if a1 == "two":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "two":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "two":
			a3 = raw_input("What is the button's text now? ")
		elif c1 == "two":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "two":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "two":
			c3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If "one" and "submit" shows up, the correct submit button is the left one, and then press "one"
	if a1 == "one" or a2 == "one" or a3 == "one" or b1 == "one" or b2 == "one" or b3 == "one" or c1 == "one" or c2 == "one" or c3 == "one" or d1 == "one" or d2 == "one" or d3 == "one":
		if a1 == "submit" or a2 == "submit" or a3 == "submit" or b1 == "submit" or b2 == "submit" or b3 == "submit" or c1 == "submit" or c2 == "submit" or c3 == "submit" or d1 == "submit" or d2 == "submit" or d3 == "submit":
			print "Press the button with the word \"one\""
			e = e + 1
			f = 1
			# Text change
			if a1 == "one":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "one":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "one":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "one":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "one":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "one":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "one":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "one":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "one":
				c3 = raw_input("what is the button's text now? ")
			elif d1 == "one":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "one":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "one":
				d3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If it's literally blank, press it.
	if a1 == " " or a2 == " " or a3 == " " or b1 == " " or b2 == " " or b3 == " " or c1 == " " or c2 == " " or c3 == " " or d1 == " " or d2 == " " or d3 == " ":
		print "Press the button that's literally blank."
		e = e + 1
		# Text change
		if a1 == " ":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == " ":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == " ":
			a3 = raw_input("What is the button's text now? ")
		elif b1 == " ":
			b1 = raw_input("What is the button's text now? ")
		elif b2 == " ":
			b2 = raw_input("What is the button's text now? ")
		elif b3 == " ":
			b3 = raw_input("What is the button's text now? ")
		elif c1 == " ":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == " ":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == " ":
			c3 = raw_input("what is the button's text now? ")
		elif d1 == " ":
			d1 = raw_input("What is the button's text now? ")
		elif d2 == " ":
			d2 = raw_input("What is the button's text now? ")
		elif d3 == " ":
			d3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If it's "other", the correct submit button is the opposite of the current one. Press it as well.
	if a1 == "other" or a2 == "other" or a3 == "other" or b1 == "other" or b2 == "other" or b3 == "other" or c1 == "other" or c2 == "other" or c3 == "other" or d1 == "other" or d2 == "other" or d3 == "other":
		print "Press the button with the word \"other\""
		if f == 1:
			f = 2
		elif f == 2:
			f = 1
		e = e + 1
		if e == 1:
			j = 1
		if a1 == "other":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "other":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "other":
			a3 = raw_input("What is the button's text now? ")
		elif b1 == "other":
			b1 = raw_input("What is the button's text now? ")
		elif b2 == "other":
			b2 = raw_input("What is the button's text now? ")
		elif b3 == "other":
			b3 = raw_input("What is the button's text now? ")
		elif c1 == "other":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "other":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "other":
			c3 = raw_input("what is the button's text now? ")
		elif d1 == "other":
			d1 = raw_input("What is the button's text now? ")
		elif d2 == "other":
			d2 = raw_input("What is the button's text now? ")
		elif d3 == "other":
			d3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If there's a duplicate, press one of the duplicates.
	g = raw_input("Is there a duplicate? ")
	if g == "y" or g == "yes" or g == "Y" or g == "YES" or g == "Yes":
		print "Please respond in numbers for the next question."
		h = input("What location is the first duplicate button? ")
		print "Press the first one."
		if h == 1:
			a1 = raw_input("What is the button's text now? ")
		if h == 2:
			a2 = raw_input("What is the button's text now? ")
		if h == 3:
			a3 = raw_input("What is the button's text now? ")
		if h == 4:
			b1 = raw_input("What is the button's text now? ")
		if h == 5:
			b2 = raw_input("What is the button's text now? ")
		if h == 6:
			b3 = raw_input("What is the button's text now? ")
		if h == 7:
			c1 = raw_input("What is the button's text now? ")
		if h == 8:
			c2 = raw_input("What is the button's text now? ")
		if h == 9:
			c3 = raw_input("What is the button's text now? ")
		if h == 10:
			d1 = raw_input("What is the button's text now? ")
		if h == 11:
			d2 = raw_input("What is the button's text now? ")
		if h == 12:
			d3 = raw_input("What is the button's text now? ")
		g = raw_input("Did that make another duplicate? ")
		if g == "y" or g == "yes" or g == "Y" or g == "YES" or g == "Yes":
			print "Please respond in numbers for the next question."
			h = input("What location is the first duplicate button? ")
			print "Press the first one."
			if h == 1:
				a1 = raw_input("What is the button's text now? ")
			if h == 2:
				a2 = raw_input("What is the button's text now? ")
			if h == 3:
				a3 = raw_input("What is the button's text now? ")
			if h == 4:
				b1 = raw_input("What is the button's text now? ")
			if h == 5:
				b2 = raw_input("What is the button's text now? ")
			if h == 6:
				b3 = raw_input("What is the button's text now? ")
			if h == 7:
				c1 = raw_input("What is the button's text now? ")
			if h == 8:
				c2 = raw_input("What is the button's text now? ")
			if h == 9:
				c3 = raw_input("What is the button's text now? ")
			if h == 10:
				d1 = raw_input("What is the button's text now? ")
			if h == 11:
				d2 = raw_input("What is the button's text now? ")
			if h == 12:
				d3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If there's a port name and the word port or module appear, press the port name button.
	if a1 == "rj-45" or a2 == "rj-45" or a3 == "rj-45" or b1 == "rj-45" or b2 == "rj-45" or b3 == "rj-45" or c1 == "rj-45" or c2 == "rj-45" or c3 == "rj-45" or d1 == "rj-45" or d2 == "rj-45" or d3 == "rj-45":
		if a1 == "port" or a2 == "port" or a3 == "port" or b1 == "port" or b2 == "port" or b3 == "port" or c1 == "port" or c2 == "port" or c3 == "port" or d1 == "port" or d2 == "port" or d3 == "port":
			e = e + 1
			print "Press the button with the word \"RJ-45\""
			if a1 == "rj-45":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "rj-45":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "rj-45":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "rj-45":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "rj-45":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "rj-45":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "rj-45":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "rj-45":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "rj-45":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "rj-45":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "rj-45":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "rj-45":
				d3 = raw_input("What is the button's text now? ")
		elif a1 == "module" or a2 == "module" or a3 == "module" or b1 == "module" or b2 == "module" or b3 == "module" or c1 == "module" or c2 == "module" or c3 == "module" or d1 == "module" or d2 == "module" or d3 == "module":
			e = e + 1
			print "Press the button with the word \"RJ-45\""
			if a1 == "rj-45":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "rj-45":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "rj-45":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "rj-45":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "rj-45":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "rj-45":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "rj-45":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "rj-45":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "rj-45":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "rj-45":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "rj-45":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "rj-45":
				d3 = raw_input("What is the button's text now? ")
	elif a1 == "dvi-d" or a2 == "dvi-d" or a3 == "dvi-d" or b1 == "dvi-d" or b2 == "dvi-d" or b3 == "dvi-d" or c1 == "dvi-d" or c2 == "dvi-d" or c3 == "dvi-d" or d1 == "dvi-d" or d2 == "dvi-d" or d3 == "dvi-d":
		if a1 == "port" or a2 == "port" or a3 == "port" or b1 == "port" or b2 == "port" or b3 == "port" or c1 == "port" or c2 == "port" or c3 == "port" or d1 == "port" or d2 == "port" or d3 == "port":
			e = e + 1
			print "Press the button with the word \"DVI-D\""
			if a1 == "dvi-d":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "dvi-d":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "dvi-d":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "dvi-d":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "dvi-d":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "dvi-d":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "dvi-d":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "dvi-d":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "dvi-d":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "dvi-d":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "dvi-d":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "dvi-d":
				d3 = raw_input("What is the button's text now? ")
		elif a1 == "module" or a2 == "module" or a3 == "module" or b1 == "module" or b2 == "module" or b3 == "module" or c1 == "module" or c2 == "module" or c3 == "module" or d1 == "module" or d2 == "module" or d3 == "module":
			e = e + 1
			print "Press the button with the word \"DVI-D\""
			if a1 == "dvi-d":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "dvi-d":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "dvi-d":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "dvi-d":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "dvi-d":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "dvi-d":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "dvi-d":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "dvi-d":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "dvi-d":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "dvi-d":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "dvi-d":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "dvi-d":
				d3 = raw_input("What is the button's text now? ")
	elif a1 == "rca" or a2 == "rca" or a3 == "rca" or b1 == "rca" or b2 == "rca" or b3 == "rca" or c1 == "rca" or c2 == "rca" or c3 == "rca" or d1 == "rca" or d2 == "rca" or d3 == "rca":
		if a1 == "port" or a2 == "port" or a3 == "port" or b1 == "port" or b2 == "port" or b3 == "port" or c1 == "port" or c2 == "port" or c3 == "port" or d1 == "port" or d2 == "port" or d3 == "port":
			e = e + 1
			print "Press the button with the word \"RCA\""
			if a1 == "rca":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "rca":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "rca":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "rca":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "rca":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "rca":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "rca":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "rca":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "rca":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "rca":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "rca":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "rca":
				d3 = raw_input("What is the button's text now? ")
		elif a1 == "module" or a2 == "module" or a3 == "module" or b1 == "module" or b2 == "module" or b3 == "module" or c1 == "module" or c2 == "module" or c3 == "module" or d1 == "module" or d2 == "module" or d3 == "module":
			e = e + 1
			print "Press the button with the word \"RCA\""
			if a1 == "rca":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "rca":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "rca":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "rca":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "rca":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "rca":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "rca":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "rca":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "rca":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "rca":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "rca":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "rca":
				d3 = raw_input("What is the button's text now? ")
	elif a1 == "ps/2" or a2 == "ps/2" or a3 == "ps/2" or b1 == "ps/2" or b2 == "ps/2" or b3 == "ps/2" or c1 == "ps/2" or c2 == "ps/2" or c3 == "ps/2" or d1 == "ps/2" or d2 == "ps/2" or d3 == "ps/2":
		if a1 == "port" or a2 == "port" or a3 == "port" or b1 == "port" or b2 == "port" or b3 == "port" or c1 == "port" or c2 == "port" or c3 == "port" or d1 == "port" or d2 == "port" or d3 == "port":
			e = e + 1
			print "Press the button with the word \"PS/2\""
			if a1 == "ps/2":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "ps/2":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "ps/2":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "ps/2":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "ps/2":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "ps/2":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "ps/2":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "ps/2":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "ps/2":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "ps/2":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "ps/2":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "ps/2":
				d3 = raw_input("What is the button's text now? ")
		elif a1 == "module" or a2 == "module" or a3 == "module" or b1 == "module" or b2 == "module" or b3 == "module" or c1 == "module" or c2 == "module" or c3 == "module" or d1 == "module" or d2 == "module" or d3 == "module":
			e = e + 1
			print "Press the button with the word \"PS/2\""
			if a1 == "ps/2":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "ps/2":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "ps/2":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "ps/2":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "ps/2":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "ps/2":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "ps/2":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "ps/2":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "ps/2":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "ps/2":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "ps/2":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "ps/2":
				d3 = raw_input("What is the button's text now? ")
	elif a1 == "serial" or a2 == "serial" or a3 == "serial" or b1 == "serial" or b2 == "serial" or b3 == "serial" or c1 == "serial" or c2 == "serial" or c3 == "serial" or d1 == "serial" or d2 == "serial" or d3 == "serial":
		if a1 == "port" or a2 == "port" or a3 == "port" or b1 == "port" or b2 == "port" or b3 == "port" or c1 == "port" or c2 == "port" or c3 == "port" or d1 == "port" or d2 == "port" or d3 == "port":
			e = e + 1
			print "Press the button with the word \"SERIAL\""
			if a1 == "serial":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "serial":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "serial":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "serial":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "serial":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "serial":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "serial":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "serial":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "serial":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "serial":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "serial":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "serial":
				d3 = raw_input("What is the button's text now? ")
		elif a1 == "module" or a2 == "module" or a3 == "module" or b1 == "module" or b2 == "module" or b3 == "module" or c1 == "module" or c2 == "module" or c3 == "module" or d1 == "module" or d2 == "module" or d3 == "module":
			e = e + 1
			print "Press the button with the word \"SERIAL\""
			if a1 == "serial":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "serial":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "serial":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "serial":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "serial":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "serial":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "serial":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "serial":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "serial":
				c3 = raw_input("What is the button's text now? ")
			elif d1 == "serial":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "serial":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "serial":
				d3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If it's less than 3 chracters, press it.
	# I'm not sure if it counts blank buttons. This part needs more debugging to confirm.
	if a1 == " " or a2 == " " or a3 == " " or b1 == " " or b2 == " " or b3 == " " or c1 == " " or c2 == " " or c3 == " " or d1 == " " or d2 == " " or d3 == " ":
		print "Press the button that's literally blank."
		e = e + 1
		# Text change
		if a1 == " ":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == " ":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == " ":
			a3 = raw_input("What is the button's text now? ")
		elif b1 == " ":
			b1 = raw_input("What is the button's text now? ")
		elif b2 == " ":
			b2 = raw_input("What is the button's text now? ")
		elif b3 == " ":
			b3 = raw_input("What is the button's text now? ")
		elif c1 == " ":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == " ":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == " ":
			c3 = raw_input("what is the button's text now? ")
		elif d1 == " ":
			d1 = raw_input("What is the button's text now? ")
		elif d2 == " ":
			d2 = raw_input("What is the button's text now? ")
		elif d3 == " ":
			d3 = raw_input("What is the button's text now? ")
	elif a1 == "to" or a2 == "to" or a3 == "to" or b1 == "to" or b2 == "to" or b3 == "to" or c1 == "to" or c2 == "to" or c3 == "to" or d1 == "to" or d2 == "to" or d3 == "to":
		print "Press the button with the word \"TO\""
		e = e + 1
		# Text change
		if a1 == "to":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "to":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "to":
			a3 = raw_input("What is the button's text now? ")
		elif b1 == "to":
			b1 = raw_input("What is the button's text now? ")
		elif b2 == "to":
			b2 = raw_input("What is the button's text now? ")
		elif b3 == "to":
			b3 = raw_input("What is the button's text now? ")
		elif c1 == "to":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "to":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "to":
			c3 = raw_input("what is the button's text now? ")
		elif d1 == "to":
			d1 = raw_input("What is the button's text now? ")
		elif d2 == "to":
			d2 = raw_input("What is the button's text now? ")
		elif d3 == "to":
			d3 = raw_input("What is the button's text now? ")
	elif a1 == "c" or a2 == "c" or a3 == "c" or b1 == "c" or b2 == "c" or b3 == "c" or c1 == "c" or c2 == "c" or c3 == "c" or d1 == "c" or d2 == "c" or d3 == "c":
		print "Press the button with the word \"C\""
		e = e + 1
		# Text change
		if a1 == "c":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "c":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "c":
			a3 = raw_input("What is the button's text now? ")
		elif b1 == "c":
			b1 = raw_input("What is the button's text now? ")
		elif b2 == "c":
			b2 = raw_input("What is the button's text now? ")
		elif b3 == "c":
			b3 = raw_input("What is the button's text now? ")
		elif c1 == "c":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "c":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "c":
			c3 = raw_input("what is the button's text now? ")
		elif d1 == "c":
			d1 = raw_input("What is the button's text now? ")
		elif d2 == "c":
			d2 = raw_input("What is the button's text now? ")
		elif d3 == "c":
			d3 = raw_input("What is the button's text now? ")
	elif a1 == "no" or a2 == "no" or a3 == "no" or b1 == "no" or b2 == "no" or b3 == "no" or c1 == "no" or c2 == "no" or c3 == "no" or d1 == "no" or d2 == "no" or d3 == "no":
		print "Press the button with the word \"NO\""
		e = e + 1
		# Text change
		if a1 == "no":
			a1 = raw_input("What is the button's text now? ")
		elif a2 == "no":
			a2 = raw_input("What is the button's text now? ")
		elif a3 == "no":
			a3 = raw_input("What is the button's text now? ")
		elif b1 == "no":
			b1 = raw_input("What is the button's text now? ")
		elif b2 == "no":
			b2 = raw_input("What is the button's text now? ")
		elif b3 == "no":
			b3 = raw_input("What is the button's text now? ")
		elif c1 == "no":
			c1 = raw_input("What is the button's text now? ")
		elif c2 == "no":
			c2 = raw_input("What is the button's text now? ")
		elif c3 == "no":
			c3 = raw_input("what is the button's text now? ")
		elif d1 == "no":
			d1 = raw_input("What is the button's text now? ")
		elif d2 == "no":
			d2 = raw_input("What is the button's text now? ")
		elif d3 == "no":
			d3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If "bomb" and "boom" are present, press "boom"
	if a1 == "bomb" or a2 == "bomb" or a3 == "bomb" or b1 == "bomb" or b2 == "bomb" or b3 == "bomb" or c1 == "bomb" or c2 == "bomb" or c3 == "bomb" or d1 == "bomb" or d2 == "bomb" or d3 == "bomb":
		if a1 == "boom" or a2 == "boom" or a3 == "boom" or b1 == "boom" or b2 == "boom" or b3 == "boom" or c1 == "boom" or c2 == "boom" or c3 == "boom" or d1 == "boom" or d2 == "boom" or d3 == "boom":
			e = e + 1
			# Text change
			if a1 == "boom":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "boom":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "boom":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "boom":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "boom":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "boom":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "boom":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "boom":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "boom":
				c3 = raw_input("what is the button's text now? ")
			elif d1 == "boom":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "boom":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "boom":
				d3 = raw_input("What is the button's text now? ")
	if e == 5:
		if f == 1:
			print "Press the left submit button."
			raw_input("Press any button to continue.")
			ktane()
		if f == 2:
			print "Press the right submit button."
			raw_input("Press any button to continue.")
			ktane()
	# If "submit" and "button" are present, press the correct submit button.
	if a1 == "submit" or a2 == "submit" or a3 == "submit" or b1 == "submit" or b2 == "submit" or b3 == "submit" or c1 == "submit" or c2 == "submit" or c3 == "submit" or d1 == "submit" or d2 == "submit" or d3 == "submit":
		if a1 == "button" or a2 == "button" or a3 == "button" or b1 == "button" or b2 == "button" or b3 == "button" or c1 == "button" or c2 == "button" or c3 == "button" or d1 == "button" or d2 == "button" or d3 == "button":
			if f == 1:
				print "Press the left submit button."
				raw_input("Press any button to continue.")
				ktane()
			if f == 2:
				print "Press the right submit button."
				raw_input("Press any button to continue.")
				ktane()
	# If "column" and either "seven" or "two" are present, press "column"
	if a1 == "column" or a2 == "column" or a3 == "column" or b1 == "column" or b2 == "column" or b3 == "column" or c1 == "column" or c2 == "column" or c3 == "column" or d1 == "column" or d2 == "column" or d3 == "column":
		if a1 == "seven" or a2 == "seven" or a3 == "seven" or b1 == "seven" or b2 == "seven" or b3 == "seven" or c1 == "seven" or c2 == "seven" or c3 == "seven" or d1 == "seven" or d2 == "seven" or d3 == "seven":
			e = e + 1
			# Text change
			if a1 == "column":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "column":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "column":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "column":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "column":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "column":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "column":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "column":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "column":
				c3 = raw_input("what is the button's text now? ")
			elif d1 == "column":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "column":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "column":
				d3 = raw_input("What is the button's text now? ")
		if a1 == "two" or a2 == "two" or a3 == "two" or b1 == "two" or b2 == "two" or b3 == "two" or c1 == "two" or c2 == "two" or c3 == "two" or d1 == "two" or d2 == "two" or d3 == "two":
			e = e + 1
			# Text change
			if a1 == "column":
				a1 = raw_input("What is the button's text now? ")
			elif a2 == "column":
				a2 = raw_input("What is the button's text now? ")
			elif a3 == "column":
				a3 = raw_input("What is the button's text now? ")
			elif b1 == "column":
				b1 = raw_input("What is the button's text now? ")
			elif b2 == "column":
				b2 = raw_input("What is the button's text now? ")
			elif b3 == "column":
				b3 = raw_input("What is the button's text now? ")
			elif c1 == "column":
				c1 = raw_input("What is the button's text now? ")
			elif c2 == "column":
				c2 = raw_input("What is the button's text now? ")
			elif c3 == "column":
				c3 = raw_input("what is the button's text now? ")
			elif d1 == "column":
				d1 = raw_input("What is the button's text now? ")
			elif d2 == "column":
				d2 = raw_input("What is the button's text now? ")
			elif d3 == "column":
				d3 = raw_input("What is the button's text now? ")
	# If a button has not been pressed yet, press the 3rd button in the 2nd row.
	if e == 0:
		print "Press the 3rd button in the 2nd row."
		b3 == raw_input("What is the button before you pressed it? ")
		if b3 == "wire" or b3 == "module" or b3 == "led" or b3 == "serial" or b3 == "one" or b3 == "three" or b3 == "five" or b3 == "seven" or b3 == "eight" or b3 == "size" or b3 == "other" or b3 == "broken" or b3 == "yes" or b3 == "see" or b3 == "sea" or b3 == "late":
			j = 1
	# If the first button that was pressed had the letter E in it, the right submit button is correct.
	if j == 1:
		f = 2
	# Press the correct submit button.
	# DEBUG NOTE: MOST TIMES THIS SIMPLY GIVES A STRIKE! THIS IS BECAUSE IT SAYS TO "REPEAT THE RULES UNTIL IT SAYS TO PRESS THE CORRECT SUBMIT BUTTON" BUT THE LAST RULE IS TO PRESS IT!
	# THE MANUAL IS UNCLEAR ABOUT THIS, AND I'M NOT SURE HOW TO REALLY FIX THIS.
	# HELP IS GREATLY APPRECIATED!
	if f == 1:
		print "Press the left submit button."
		raw_input("Press any button to continue.")
		ktane()
	if f == 2:
		print "Press the right submit button."
		raw_input("Press any button to continue.")
		ktane()
def wirePlacement():
	# Wire Placement
	# Mod by lumbud84 and implemented by Timwi. Can be downloaded here: https://steamcommunity.com/sharedfiles/filedetails/?id=836617860
	print "Black - \"ba\""
	print "Blue - \"bu\""
	print "Red - \"r\""
	print "White - \"w\""
	print "Yellow - \"y\""
	x = raw_input("What color is the wire that's connected to C3? ")
	# Fastest way to do this is to simply tell all the wire cuts.
	# If not, then it's the fastest and shortest way to program this!
	if x == "ba":
		print "Cuts:"
		print "D2 - Yellow"
		print "A2 - Blue"
		print "D3 - White"
		print "B2 - White"
		print "A1 - Red"
		print "C3 - Blue"
		print "B1 - Black"
		print "C4 - Red"
		print "A3 - Yellow"
		print "D1 - Yellow"
		raw_input("Press any button to continue.")
		ktane()
	if x == "bu":
		print "Cuts:"
		print "D1 - Yellow"
		print "C4 - Blue"
		print "D2 - White"
		print "C1 - White"
		print "B3 - Red"
		print "C2 - Blue"
		print "D4 - Black"
		print "D3 - Red"
		print "C3 - Yellow"
		print "A1 - Yellow"
		raw_input("Press any button to continue.")
		ktane()
	if x == "r":
		print "Cuts:"
		print "D2 - Yellow"
		print "A1 - Blue"
		print "D4 - White"
		print "B4 - White"
		print "C4 - Red"
		print "C1 - Blue"
		print "A4 - Black"
		print "B1 - Red"
		print "A2 - Yellow"
		print "B2 - Yellow"
		raw_input("Press any button to continue.")
		ktane()
	if x == "w":
		print "Cuts:"
		print "A2 - Yellow"
		print "C4 - Blue"
		print "B3 - White"
		print "A1 - White"
		print "B2 - Red"
		print "D3 - Blue"
		print "D2 - Black"
		print "C1 - Red"
		print "A4 - Yellow"
		print "B4 - Yellow"
		raw_input("Press any button to continue.")
		ktane()
	if x == "y":
		print "Cuts:"
		print "D1 - Yellow"
		print "D4 - Blue"
		print "B2 - White"
		print "C1 - White"
		print "B3 - Red"
		print "B1 - Blue"
		print "B4 - Black"
		print "C2 - Red"
		print "A3 - Yellow"
		print "A4 - Yellow"
		raw_input("Press any button to continue.")
		ktane()
	else:
		print "Unknown Response!"
		print "Please try again."
		raw_input("Press any button to continue.")
		ktane()
def adventureGame():
	# Adventure Game
	# Mod by Spare Wizard and can be downloaded here: https://steamcommunity.com/sharedfiles/filedetails/?id=747854140
	# Variable STR [Sierra, Tango, Romeo] - Strength Statistic
	# Variable DEX [Delta, Echo, X-ray] - Dexterity Statistic
	# Variable INT [India, November, Tango] - Intelligence Statistic
	# Variable HT [Hotel, Tango] + Number - Height Statistic [Displayed in Feet and Inches, 1st being Feet and 2nd being Inches]
	# Variable TMP [Tango, Mike, Papa] - Temperature Statistic [Displayed in Celsius]
	# Variable FOG [Foxtrot, Oscar, Golf] - Force of Gravity Statistic [Displayed in meters per second squared, or m/s^2]
	# Variable APS [Alpha, Papa, Sierra] - Atmospheric Pressure Statistic [Displayed in kilopascals, or kPa]
	# Variable IT [India, Tango] + Number - Items
	# Variable EN [Echo, November] - Enemy
	# Variable WP [Whiskey, Papa] + Number - Weapons
	# Variable ENSTR [Echo, November, Sierra, Tango, Romeo] - Strength of Enemy
	# Variable ENDEX [Echo, November, Delta, Echo, X-ray] - Dexterity of Enemy
	# Variable ENINT [Echo, November, India, November, Tango] - Intelligence of Enemy
	# Variable STRM1 [Sierra, Tango, Romeo, Mike] - STR when minused by 1.
	# Variable STRM2 [Sierra, Tango, Romeo, Mike] - STR when minused by 2.
	# Variable DEXM1 [Delta, Echo, X-ray, Mike] - DEX when minused by 1.
	# Variable DEXM2 [Delta, Echo, X-ray, Mike] - DEX when minused by 2.
	# Variable INTM1 [India, November, Tango, Mike] - INT when minused by 1.
	# Variable INTM2 [India, November, Tango, Mike] - INT when minused by 2.
	it1 = 0
	it2 = 0
	it3 = 0
	it4 = 0
	it5 = 0
	wp1 = 0
	wp2 = 0
	wp3 = 0
	print "If one of your items is a Potion, use it."
	str = input("What is the STR of the player? ")
	dex = input("What is the DEX of the player? ")
	int = input("What is the INT of the player? ")
	ht1 = input("How Tall is the player, Feet wise? ")
	ht2 = input("How Tall is the player, Inch wise? ")
	tmp = input("What is the Temperature (C)? ")
	fog = input("What is the Force of Gravity (m/s^2)? ")
	aps = input("What is the Atmosphere Pressure (kPa)? ")
	print "Please respond to the next 9 questions in lower case."
	x = raw_input("What is the first item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		wp1 = x
	x = raw_input("What is the second item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		if it1 == "balloon" or it1 == "battery" or it1 == "bellows" or it1 == "cheat code" or it1 == "crystal ball" or it1 == "feather" or it1 == "hard drive" or it1 == "lamp" or it1 == "moonstone" or it1 == "small dog" or it1 == "stepladder" or it1 == "sunstone" or it1 == "symbol" or it1 == "ticket" or it1 == "trophy":
			it2 = x
		else:
			it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		if wp1 == "broadsword" or wp1 == "caber" or wp1 == "nasty knife" or wp1 == "longbow" or wp1 == "magic orb" or wp1 == "grimoire":
			wp2 = x
		else:
			wp1 = x
	x = raw_input("What is the third item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		if it1 == "balloon" or it1 == "battery" or it1 == "bellows" or it1 == "cheat code" or it1 == "crystal ball" or it1 == "feather" or it1 == "hard drive" or it1 == "lamp" or it1 == "moonstone" or it1 == "small dog" or it1 == "stepladder" or it1 == "sunstone" or it1 == "symbol" or it1 == "ticket" or it1 == "trophy":
			if it2 == "balloon" or it2 == "battery" or it2 == "bellows" or it2 == "cheat code" or it2 == "crystal ball" or it2 == "feather" or it2 == "hard drive" or it2 == "lamp" or it2 == "moonstone" or it2 == "small dog" or it2 == "stepladder" or it2 == "sunstone" or it2 == "symbol" or it2 == "ticket" or it2 == "trophy":
				it3 = x
			else:
				it2 = x
		else:
			it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		if wp1 == "broadsword" or wp1 == "caber" or wp1 == "nasty knife" or wp1 == "longbow" or wp1 == "magic orb" or wp1 == "grimoire":
			if wp2 == "broadsword" or wp2 == "caber" or wp2 == "nasty knife" or wp2 == "longbow" or wp2 == "magic orb" or wp2 == "grimoire":
				wp3 = x
			else:
				wp2 = x
		else:
			wp1 = x
	x = raw_input("What is the fourth item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		if it1 == "balloon" or it1 == "battery" or it1 == "bellows" or it1 == "cheat code" or it1 == "crystal ball" or it1 == "feather" or it1 == "hard drive" or it1 == "lamp" or it1 == "moonstone" or it1 == "small dog" or it1 == "stepladder" or it1 == "sunstone" or it1 == "symbol" or it1 == "ticket" or it1 == "trophy":
			if it2 == "balloon" or it2 == "battery" or it2 == "bellows" or it2 == "cheat code" or it2 == "crystal ball" or it2 == "feather" or it2 == "hard drive" or it2 == "lamp" or it2 == "moonstone" or it2 == "small dog" or it2 == "stepladder" or it2 == "sunstone" or it2 == "symbol" or it2 == "ticket" or it2 == "trophy":
				if it3 == "balloon" or it3 == "battery" or it3 == "bellows" or it3 == "cheat code" or it3 == "crystal ball" or it3 == "feather" or it3 == "hard drive" or it3 == "lamp" or it3 == "moonstone" or it3 == "small dog" or it3 == "stepladder" or it3 == "sunstone" or it3 == "symbol" or it3 == "ticket" or it3 == "trophy":
					it4 = x
				else:
					it3 = x
			else:
				it2 = x
		else:
			it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		if wp1 == "broadsword" or wp1 == "caber" or wp1 == "nasty knife" or wp1 == "longbow" or wp1 == "magic orb" or wp1 == "grimoire":
			if wp2 == "broadsword" or wp2 == "caber" or wp2 == "nasty knife" or wp2 == "longbow" or wp2 == "magic orb" or wp2 == "grimoire":
				wp3 = x
			else:
				wp2 = x
		else:
			wp1 = x
	x = raw_input("What is the fifth item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		if it1 == "balloon" or it1 == "battery" or it1 == "bellows" or it1 == "cheat code" or it1 == "crystal ball" or it1 == "feather" or it1 == "hard drive" or it1 == "lamp" or it1 == "moonstone" or it1 == "small dog" or it1 == "stepladder" or it1 == "sunstone" or it1 == "symbol" or it1 == "ticket" or it1 == "trophy":
			if it2 == "balloon" or it2 == "battery" or it2 == "bellows" or it2 == "cheat code" or it2 == "crystal ball" or it2 == "feather" or it2 == "hard drive" or it2 == "lamp" or it2 == "moonstone" or it2 == "small dog" or it2 == "stepladder" or it2 == "sunstone" or it2 == "symbol" or it2 == "ticket" or it2 == "trophy":
				if it3 == "balloon" or it3 == "battery" or it3 == "bellows" or it3 == "cheat code" or it3 == "crystal ball" or it3 == "feather" or it3 == "hard drive" or it3 == "lamp" or it3 == "moonstone" or it3 == "small dog" or it3 == "stepladder" or it3 == "sunstone" or it3 == "symbol" or it3 == "ticket" or it3 == "trophy":
					if it4 == "balloon" or it4 == "battery" or it4 == "bellows" or it4 == "cheat code" or it4 == "crystal ball" or it4 == "feather" or it4 == "hard drive" or it4 == "lamp" or it4 == "moonstone" or it4 == "small dog" or it4 == "stepladder" or it4 == "sunstone" or it4 == "symbol" or it4 == "ticket" or it4 == "trophy":
						it5 = x
					else:
						it4 = x
				else:
					it3 = x
			else:
				it2 = x
		else:
			it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		if wp1 == "broadsword" or wp1 == "caber" or wp1 == "nasty knife" or wp1 == "longbow" or wp1 == "magic orb" or wp1 == "grimoire":
			if wp2 == "broadsword" or wp2 == "caber" or wp2 == "nasty knife" or wp2 == "longbow" or wp2 == "magic orb" or wp2 == "grimoire":
				wp3 = x
			else:
				wp2 = x
		else:
			wp1 = x
	x = raw_input("What is the sixth item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		if it1 == "balloon" or it1 == "battery" or it1 == "bellows" or it1 == "cheat code" or it1 == "crystal ball" or it1 == "feather" or it1 == "hard drive" or it1 == "lamp" or it1 == "moonstone" or it1 == "small dog" or it1 == "stepladder" or it1 == "sunstone" or it1 == "symbol" or it1 == "ticket" or it1 == "trophy":
			if it2 == "balloon" or it2 == "battery" or it2 == "bellows" or it2 == "cheat code" or it2 == "crystal ball" or it2 == "feather" or it2 == "hard drive" or it2 == "lamp" or it2 == "moonstone" or it2 == "small dog" or it2 == "stepladder" or it2 == "sunstone" or it2 == "symbol" or it2 == "ticket" or it2 == "trophy":
				if it3 == "balloon" or it3 == "battery" or it3 == "bellows" or it3 == "cheat code" or it3 == "crystal ball" or it3 == "feather" or it3 == "hard drive" or it3 == "lamp" or it3 == "moonstone" or it3 == "small dog" or it3 == "stepladder" or it3 == "sunstone" or it3 == "symbol" or it3 == "ticket" or it3 == "trophy":
					if it4 == "balloon" or it4 == "battery" or it4 == "bellows" or it4 == "cheat code" or it4 == "crystal ball" or it4 == "feather" or it4 == "hard drive" or it4 == "lamp" or it4 == "moonstone" or it4 == "small dog" or it4 == "stepladder" or it4 == "sunstone" or it4 == "symbol" or it4 == "ticket" or it4 == "trophy":
						it5 = x
					else:
						it4 = x
				else:
					it3 = x
			else:
				it2 = x
		else:
			it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		if wp1 == "broadsword" or wp1 == "caber" or wp1 == "nasty knife" or wp1 == "longbow" or wp1 == "magic orb" or wp1 == "grimoire":
			if wp2 == "broadsword" or wp2 == "caber" or wp2 == "nasty knife" or wp2 == "longbow" or wp2 == "magic orb" or wp2 == "grimoire":
				wp3 = x
			else:
				wp2 = x
		else:
			wp1 = x
	x = raw_input("What is the seventh item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		if it1 == "balloon" or it1 == "battery" or it1 == "bellows" or it1 == "cheat code" or it1 == "crystal ball" or it1 == "feather" or it1 == "hard drive" or it1 == "lamp" or it1 == "moonstone" or it1 == "small dog" or it1 == "stepladder" or it1 == "sunstone" or it1 == "symbol" or it1 == "ticket" or it1 == "trophy":
			if it2 == "balloon" or it2 == "battery" or it2 == "bellows" or it2 == "cheat code" or it2 == "crystal ball" or it2 == "feather" or it2 == "hard drive" or it2 == "lamp" or it2 == "moonstone" or it2 == "small dog" or it2 == "stepladder" or it2 == "sunstone" or it2 == "symbol" or it2 == "ticket" or it2 == "trophy":
				if it3 == "balloon" or it3 == "battery" or it3 == "bellows" or it3 == "cheat code" or it3 == "crystal ball" or it3 == "feather" or it3 == "hard drive" or it3 == "lamp" or it3 == "moonstone" or it3 == "small dog" or it3 == "stepladder" or it3 == "sunstone" or it3 == "symbol" or it3 == "ticket" or it3 == "trophy":
					if it4 == "balloon" or it4 == "battery" or it4 == "bellows" or it4 == "cheat code" or it4 == "crystal ball" or it4 == "feather" or it4 == "hard drive" or it4 == "lamp" or it4 == "moonstone" or it4 == "small dog" or it4 == "stepladder" or it4 == "sunstone" or it4 == "symbol" or it4 == "ticket" or it4 == "trophy":
						it5 = x
					else:
						it4 = x
				else:
					it3 = x
			else:
				it2 = x
		else:
			it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		if wp1 == "broadsword" or wp1 == "caber" or wp1 == "nasty knife" or wp1 == "longbow" or wp1 == "magic orb" or wp1 == "grimoire":
			if wp2 == "broadsword" or wp2 == "caber" or wp2 == "nasty knife" or wp2 == "longbow" or wp2 == "magic orb" or wp2 == "grimoire":
				wp3 = x
			else:
				wp2 = x
		else:
			wp1 = x
	x = raw_input("What is the eighth item/weapon? ")
	if x == "balloon" or x == "battery" or x == "bellows" or x == "cheat code" or x == "crystal ball" or x == "feather" or x == "hard drive" or x == "lamp" or x == "moonstone" or x == "small dog" or x == "stepladder" or x == "sunstone" or x == "symbol" or x == "ticket" or x == "trophy":
		if it1 == "balloon" or it1 == "battery" or it1 == "bellows" or it1 == "cheat code" or it1 == "crystal ball" or it1 == "feather" or it1 == "hard drive" or it1 == "lamp" or it1 == "moonstone" or it1 == "small dog" or it1 == "stepladder" or it1 == "sunstone" or it1 == "symbol" or it1 == "ticket" or it1 == "trophy":
			if it2 == "balloon" or it2 == "battery" or it2 == "bellows" or it2 == "cheat code" or it2 == "crystal ball" or it2 == "feather" or it2 == "hard drive" or it2 == "lamp" or it2 == "moonstone" or it2 == "small dog" or it2 == "stepladder" or it2 == "sunstone" or it2 == "symbol" or it2 == "ticket" or it2 == "trophy":
				if it3 == "balloon" or it3 == "battery" or it3 == "bellows" or it3 == "cheat code" or it3 == "crystal ball" or it3 == "feather" or it3 == "hard drive" or it3 == "lamp" or it3 == "moonstone" or it3 == "small dog" or it3 == "stepladder" or it3 == "sunstone" or it3 == "symbol" or it3 == "ticket" or it3 == "trophy":
					if it4 == "balloon" or it4 == "battery" or it4 == "bellows" or it4 == "cheat code" or it4 == "crystal ball" or it4 == "feather" or it4 == "hard drive" or it4 == "lamp" or it4 == "moonstone" or it4 == "small dog" or it4 == "stepladder" or it4 == "sunstone" or it4 == "symbol" or it4 == "ticket" or it4 == "trophy":
						it5 = x
					else:
						it4 = x
				else:
					it3 = x
			else:
				it2 = x
		else:
			it1 = x
	if x == "broadsword" or x == "caber" or x == "nasty knife" or x == "longbow" or x == "magic orb" or x == "grimoire":
		if wp1 == "broadsword" or wp1 == "caber" or wp1 == "nasty knife" or wp1 == "longbow" or wp1 == "magic orb" or wp1 == "grimoire":
			if wp2 == "broadsword" or wp2 == "caber" or wp2 == "nasty knife" or wp2 == "longbow" or wp2 == "magic orb" or wp2 == "grimoire":
				wp3 = x
			else:
				wp2 = x
		else:
			wp1 = x
	en = raw_input("What is the Enemy? ")
	# Use the Balloon if the Gravity is less than 9.3 m/s^2 or the Pressure is greater than 110 kPa, and not fighting an Eagle.
	if it1 == "balloon" or it2 == "balloon" or it3 == "balloon" or it4 == "balloon" or it5 == "balloon":
		if fog <= 9.3 or aps >= 110:
			if not en == "eagle":
				print "Use the Balloon."
	# Use the Battery if there is at most 1 battery on the bomb, and not fighting a Golem or Wizard.
	if it1 == "battery" or it2 == "battery" or it3 == "battery" or it4 == "battery" or it5 == "battery":
		if not en == "golem":
			if not en == "wizard":
				print "Use the Battery if there is at most 1 battery on the bomb."
	# Use the Bellows if the pressure is greater than 105 kPa when fighting a Dragon or Eagle. Otherwise, use if the pressure is less than 95 kPa when fighting another enemy.
	if it1 == "bellows" or it2 == "bellows" or it3 == "bellows" or it4 == "bellows" or it5 == "bellows":
		if en == "dragon" or en == "eagle":
			if aps >= 105:
				print "Use the Bellows."
		else:
			if aps <= 95:
				print "Use the Bellows."
	# Throwaway the Cheat Code, essentially. "Cheaters Never Prosper" except this code IS kind of a cheat, and I managed to beat "One with Everything" with this, so...
	# Use the Crystal Ball if the INT is greater than the last digit of the serial number, and not fighting a Wizard.
	if it1 == "crystal ball" or it2 == "crystal ball" or it3 == "crystal ball" or it4 == "crystal ball" or it5 == "crystal ball":
		if not en == "wizard":
			x = input("What is the last digit of the SN? ")
			if int >= x:
				print "Use the Crystal Ball."
	# Use the Feather if DEX is greater than either STR or INT.
	if it1 == "feather" or it2 == "feather" or it3 == "feather" or it4 == "feather" or it5 == "feather":
		if dex >= str or dex >= int:
			print "Use the Feather."
	# Use the Hard Drive if there are two or more of the same port on the bomb.
	if it1 == "hard drive" or it2 == "hard drive" or it3 == "hard drive" or it4 == "hard drive" or it5 == "hard drive":
		print "Use the Hard Drive if there are two or more of the same port on the bomb."
	# Use the Lamp if the Temperature is less than 12*C, and not fighting a Lizard.
	if it1 == "lamp" or it2 == "lamp" or it3 == "lamp" or it4 == "lamp" or it5 == "lamp":
		if tmp >= 12:
			if not en == "lizard":
				print "Use the Lamp."
	# Use the Moonstone if there are at least two unlit indcators on the bomb.
	if it1 == "moonstone" or it2 == "moonstone" or it3 == "moonstone" or it4 == "moonstone" or it5 == "moonstone":
		print "Use the Moonstone if there are at least two unlit indactors on the bomb."
	# Potion should already be used by now. If not, then the user is an idiot.
	# Use the Small Dog to get your balls stolen. I mean, Use it if not fighting a Demon, Dragon, or Troll.
	if it1 == "small dog" or it2 == "small dog" or it3 == "small dog" or it4 == "small dog" or it5 == "small dog":
		if not en == "demon":
			if not en == "dragon":
				if not en == "troll":
					print "Use the Small Dog."
	# Use the Stepladder if the player is shorter than 4' and not fighting a Goblin or Lizard.
	if it1 == "stepladder" or it2 == "stepladder" or it3 == "stepladder" or it4 == "stepladder" or it5 == "stepladder":
		if ht1 == 4:
			if not en == "goblin":
				if not en == "lizard":
					print "Use the Stepladder."
	# Use the Sunstone if there are at least two lit indicators on the bomb.
	if it1 == "sunstone" or it2 == "sunstone" or it3 == "sunstone" or it4 == "sunstone" or it5 == "sunstone":
		print "Use the Sunstone if there are at least two lit indicators on the bomb."
	# Use the Symbol if fighting a Demon or Golem, or if the temperature is greater than 31*C.
	if it1 == "symbol" or it2 == "symbol" or it3 == "symbol" or it4 == "symbol" or it5 == "symbol":
		if en == "demon" or en == "golem" or tmp >= 31:
			print "Use the Symbol."
	# Use the Ticket if the player is 4'6" or taller, and gravity is between 9.2 m/s^2 and 10.4 m/s^2.
	if it1 == "ticket" or it2 == "ticket" or it3 == "ticket" or it4 == "ticket" or it5 == "ticket":
		if ht1 == 4:
			if ht1 >=6:
				if fog <= 9.2 and fog >= 10.4:
					print "Use the Ticket."
		if ht1 >= 5:
			if fog <= 9.2 and fog >= 10.4:
				print "Use the Ticket."
	# Use the Trophy if the STR is greater than the first numeric digit of the serial number, or if fighting a Troll.
	if it1 == "trophy" or it2 == "trophy" or it3 == "trophy" or it4 == "trophy" or it5 == "trophy":
		if en == "troll":
			print "Use the Trophy."
		else:
			x = input("What is the first numeric digit of the SN? ")
			if str >= x:
				print "Use the Trophy."
	# Combat Time!
	# Establish STR, DEX, and INT of enemies.
	if en == "demon":
		enstr = 50
		endex = 50
		enint = 50
	if en == "dragon":
		enstr = 10
		endex = 11
		enint = 13
	if en == "eagle":
		enstr = 4
		endex = 7
		enint = 3
	if en == "goblin":
		enstr = 3
		endex = 6
		enint = 5
	if en == "golem":
		enstr = 9
		endex = 4
		enint = 7
	if en == "troll":
		enstr = 8
		endex = 5
		enint = 4
	if en == "lizard":
		enstr = 4
		endex = 6
		enint = 3
	if en == "wizard":
		enstr = 4
		endex = 3
		enint = 8
	strm1 = str - 1
	strm2 = str - 2
	dexm1 = dex - 1
	dexm2 = dex - 2
	intm1 = int - 1
	intm2 = int - 2
	x = 0
	# If the Enemy's STR is lower or the same as the Player's STR, then use a Broadsword.
	if enstr <= str:
		if wp1 == "broadsword" or wp2 == "broadsword" or wp3 == "broadsword":
			print "Use the Broadsword."
			x = 1
	# If the Enemy's STR is the same as the Player's STR when minused by 1 or 2, then use a Caber.
	if x == 0:
		if enstr == strm1 or enstr == strm2:
			if wp1 == "caber" or wp2 == "caber" or wp3 == "caber":
				print "Use the Caber."
				x = 1
	# If the Enemy's DEX is lower or the same as the Player's DEX, then use a Nasty Knife.
	if x == 0:
		if endex <= dex:
			if wp1 == "nasty knife" or wp2 == "nasty knife" or wp3 == "nasty knife":
				print "Use the Nasty Knife."
				x = 1
	# If the Enemy's DEX is the same as the Player's DEX when minused by 1 or 2, then use a Longbow.
	if x == 0:
		if endex == dexm1 or enstr == dexm2:
			if wp1 == "longbow" or wp2 == "longbow" or wp3 == "longbow":
				print "Use the Longbow."
				x = 1
	# If the Enemy's INT is lower or the same as the Player's INT, then use a Magic Orb.
	if x == 0:
		if enint <= int:
			if wp1 == "magic orb" or wp2 == "magic orb" or wp3 == "magic orb":
				print "Use the Magic Orb."
				x = 1
	# If the Enemy's INT is the same as the Player's INT when minused by 1 or 2, then use a Grimoire.
	if x == 0:
		if enint == intm1 or enint == intm2:
			if wp1 == "grimoire" or wp2 == "grimoire" or wp3 == "grimoire":
				print "Use the Grimoire."
				x = 1
	# If all else fails, use the one with the least disadvantage.
	# This part needs work, since I don't exactly know how to program this into Python.
	if x == 0:
		if wp1 == "caber" or wp2 == "caber" or wp3 == "caber":
			if wp1 == "longbow" or wp2 == "longbow" or wp3 == "longbow":
				if wp1 == "grimoire" or wp2 == "grimoire" or wp3 == "grimoire":
					print "Use either the Caber, Longbow, or Grimoire."
				else:
					print "Use either the Caber or Longbow"
			else:
				if wp1 == "grimoire" or wp2 == "grimoire" or wp3 == "grimoire":
					print "Use either the Caber or Grimoire."
				else:
					print "Use the Caber."
		else:
			if wp1 == "longbow" or wp2 == "longbow" or wp3 == "longbow":
				if wp1 == "grimoire" or wp2 == "grimoire" or wp3 == "grimoire":
					print "Use either the Longbow or Grimoire."
				else:
					print "Use the Longbow."
			else:
				if wp1 == "grimoire" or wp2 == "grimoire" or wp3 == "grimoire":
					print "Use the Grimoire."
				else:
					print "Use either the Broadsword, Nasty Knife or Magic Orb."

	raw_input("Press enter to continue.")
	ktane()
def algebra():
	# Algebra
	# Oh boy is this going to be a fun one to program.
	# Mod by Royal_Flu$h and can be downloaded here: http://steamcommunity.com/sharedfiles/filedetails/?id=1272897891
	# Variable [E]cho: Throaway variable (For inputs)
	# Variable [F]oxtrot + Number: Throwaway variable (For multiple inputs)
	# Variable [G]olf: Throwaway variable #1 (First number)
	f1 = 0
	f2 = 0
	f3 = 0
	# x = n
	# n = sum of digits in the serial number
	# x + 2 = 3 or more battery holders present
	# x - 1 = RJ-45 port present
	# x + 4 = Lit BOB indicator present
	# x - 3 = Serial number contains a vowel
	e = input("How many digits are there in the SN? ")
	if e == 1:
		f1 = input("What is the digit? ")
	if e == 2:
		f1 = input("What is the first digit? ")
		f2 = input("What is the second digit? ")
	if e == 3:
		f1 = input("What is the first digit? ")
		f2 = input("What is the second digit? ")
		f3 = input("What is the third digit? ")
	n = f1 + f2 + f3
	x = n
	e = raw_input("Is there 3 or more battery holders present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		x = x + 2
	e = raw_input("Is there a RJ-45 port (The one that looks like an Ethernet Port) present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		x = x - 1
	e = raw_input("Is there a lit BOB indicator present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		x = x + 4
	e = raw_input("Does the SN contain a vowel? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		x = x - 3
	# y = i - p
	# i = number of indicators
	# p = number of ports
	# y - 2 = 2 or fewer battery holders present
	# y + 3 = Serial port present
	# y - 5 = Unlit FRQ indicator present
	# y + 4 = Sum of the serial number digits is prime
	i = input("How many indicators are there? ")
	p = input("How many ports are there? ")
	y = i - p
	e = raw_input("Are there 2 or fewer battery holders present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		y = y - 2
	e = raw_input("Is there a serial port (The one that looks like a short VGA port) present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		y = y + 3
	e = raw_input("Is there an unlit FRQ indicator present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		y = y - 5
	e = f1 + f2 + f3
	if e == 2 or e == 3 or e == 5 or e == 7 or e == 11 or e == 13 or e == 17 or e == 19 or e == 23:
		y = y + 4
	# z = m + t * d
	# m = number of modules
	# t = number of AA batteries
	# d = number of D batteries
	# z + 3 = No battery holders present
	# z - 6 = Parrallel port present
	# z + 2 = Lit MSA indicator present
	# z + 1 = Sum of the SN digits is divisible by 3
	m = input("How many modules are there? ")
	t = input("How many AA batteries are there? ")
	d = input("How many D batteries are there? ")
	z = m + t * d
	e = raw_input("Are there no battery holders present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		z = z + 3
	e = raw_input("Is there a Parrallel port (They're the pink ones) present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		z = z - 6
	e = raw_input("Is there a lit MSA indicator present? ")
	if e == "y" or e == "Y" or e == "Yes" or e == "yes" or e == "YES":
		z = z + 2
	e = f1 + f2 + f3
	if e == 3 or e == 6 or e == 9 or e == 12 or e == 15 or e == 18 or e == 21 or e == 24 or e == 27:
		z = z + 1
	print "x is", x
	print "y is", y
	print "z is", z
	# Level 1 Formulae
	a = x + 1
	print "a = x + 1 is", a
	a = 6 - x
	print "a = 6 - x is", a
	a = 7 * x
	print "a = 7x is", a
	a = x / 2.0
	print "a = x / 2 is", a
	a = 5 + y
	print "a = 5 + y is", a
	a = y - 2
	print "a = y - 2 is", a
	a = 8 * y
	print "a = 8y is", a
	a = y / 4.0
	print "a = y / 4 is", a
	a = 9 + z
	print "a = 9 + z is", a
	a = z - 7
	print "a = z - 7 is", a
	a = 3 * z
	print "a = 3z is", a
	a = z / 10.0
	print "a = z / 10 is", a
	# Level 2 Formulae
	b = (x * y) - (2 + x)
	print "b = xy - (2 + x) is", b
	b = ((2 * x) / 10.0) - y
	print "b = (2x / 10) - y is", b
	b = (z - y) / 2.0
	print "b = (z - y) / 2 is", b
	b = x * y * z
	print "b = xyz is", b
	b = (y / 2.0) - z
	print "b = (y / 2) - z is", b
	b = (z * y) - (2 * x)
	print "b = zy - 2x is", b
	b = (x + y) - (z / 2.0)
	print "b = (x + y) - (z / 2) is", b
	b = (7 * x) * y
	print "b = 7xy is", b
	b = (2 * z) + 7
	print "b = 2z + 7 is", b
	b = 2 * (z + 7)
	print "b = 2 * (z + 7) is", b
	# Level 3 Formulae
	c = x - (2 * y) + z
	print "x - 2y = c - z is", c
	c = ((x * y) - z) * 10
	print "xy = z + c / 10 is", c
	c = ((y / 2.0 + 7) - z) / 4.0
	print "y / 2 + 7 = 4c + z is", c
	c = (x * 8) - z + y
	print "8x - z = c - y is", c
	c = (2 + y) / 10.0 - (x * 3) + (z / 4.0)
	print "3x - ((2 + y) / 10) = z / 4 - c is", c
	c = 9 * (y / 2.0) + (x * y) / 4.0
	print "9(y / 2) = c - xy/4 is", c
	c = ((z / 2.0) - (x / 4.0) + z) / 4.0
	print "(z / 2) - (x / 4) = 4c - z is", c
	c = (x * (y / 2.0) + 11) * (y * 2) - 4
	print "x(y/2) + 11 = (4 + c) / 2y is", c
	raw_input("Press enter to continue.")
	ktane()
def theBulb():
	# The Bulb
	# Mod made by Timwi and can be downloaded here: http://steamcommunity.com/sharedfiles/filedetails/?id=788980366
	# Variable MAT [Mike, Alpha, Tango]: Material is either see-through or opaque.
	# Variable COL [Charlie, Oscar, Lima]: Color is either Blue, Green, Purple, Red, White or Yellow.
	# Variable AN1 [Alpha, November, One]: Answer in step 1.
	# Variable A23 [Alpha, Two, Three]: Answer in either step 2 or step 3.
	# Variable IND [India, November, Delta]: Indicator
	x = 0
	y = "n"
	print "Please input in lower case."
	print "Valid responses: see-through s opaque o"
	mat = raw_input("Is the bulb see-through or opaque? ")
	print "Valid responses: blue b green g purple p red r white w yellow y"
	col = raw_input("What is the color of the bulb? ")
	# Step 1
	if lgt == "on" and mat == "see-through":
		print "Press I."
		y = raw_input("Did the light go off? ")
		an1 = "i"
		x = 2
	if lgt == "on" and mat == "s":
		print "Press I."
		y = raw_input("Did the light go off? ")
		an1 = "i"
		x = 2
	if lgt == "on" and mat == "opaque":
		print "Press O."
		y = raw_input("Did the light go off? ")
		an1 = "o"
		x = 3
	if lgt == "on" and mat == "o":
		print "Press O."
		y = raw_input("Did the light go off? ")
		an1 = "o"
		x = 3
	if lgt == "off":
		print "Unscrew the bulb."
		x = 4
	# Step 2
	if x == 2:
		if col == "r" or col == "red":
			print "Press I."
			print "Unscrew the bulb."
			y = raw_input("Did the light go off? ")
			a23 = "i"
			x = 5
		if col == "w" or col == "white":
			print "Press O."
			print "Unscrew the bulb."
			a23 = "o"
			x = 6
		if x == 2:
			print "Unscrew the bulb."
			x = 7
	# Step 3
	if x == 3:
		if col == "g" or col == "green":
			print "Press I."
			print "Unscrew the bulb."
			y = raw_input("Did the light go off? ")
			a23 = "i"
			x = 6
		if col == "p" or col == "purple":
			print "Press O."
			print "Unscrew the bulb."
			a23 = "o"
			x = 5
		if x == 3:
			print "Unscrew the bulb."
	# Step 4
	if x == 4:
		z = raw_input("Does the bomb have the following indicators: CAR, IND, MSA, or SND? ")
		if z == "y" or z == "Y" or z == "yes" or z == "Yes" or z == "YES":
			print "Press I."
			x = 9
		else:
			print "Press O."
			x = 10
	# Step 5
	if x == 5:
		if y == "y" or y == "Y" or y == "yes" or y == "Yes" or y == "YES":
			if an1 == "i":
				print "Press I."
				print "Screw the bulb back in."
			if an1 == "o":
				print "Press O."
				print "Screw the bulb back in."
		else:
			if an1 == "i":
				print "Press O."
				print "Screw the bulb back in."
			if an1 == "o":
				print "Press I."
				print "Screw the bulb back in."
	# Step 6
	if x == 6:
		if y == "y" or y == "Y" or y == "yes" or y == "Yes" or y == "YES":
			if a23 == "i":
				if an1 == "i":
					print "Press I."
					print "Screw the bulb back in."
				if an1 == "o":
					print "Press O."
					print "Screw the bulb back in."
			else:
				print "Press O."
				print "Screw the bulb back in."
		else:
			if a23 == "i":
				print "Press I."
				print "Screw the bulb back in."
			if a23 == "o":
				print "Press O."
				print "Screw the bulb back in."
	# Step 7
	if x == 7:
		if col == "g" or col == "green":
			print "Press I."
			ind = "sig"
			x = 11
		if col == "p" or col == "purple":
			print "Press I."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 12
		if col == "b" or col == "blue":
			print "Press O."
			ind = "clr"
			x = 11
		if x == 7:
			print "Press O."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 13
	# Step 8
	if x == 8:
		if col == "w" or col == "white":
			print "Press I."
			ind = "frq"
			x = 11
		if col == "r" or col == "red":
			print "Press I."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 13
		if col == "y" or col == "yellow":
			print "Press O."
			ind = "frk"
			x = 11
		if x == 8:
			print "Press O."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 12
	# Step 9
	if x == 9:
		if col == "b" or col == "blue":
			print "Press I."
			x = 14
		if col == "g" or col == "green":
			print "Press I."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 12
		if col == "y" or col == "yellow":
			print "Press O."
			x = 15
		if col == "w" or col == "white":
			print "Press O."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 13
		if col == "p" or col == "purple":
			print "Screw the bulb back in."
			print "Press I."
			y = raw_input("Is the light now on? ")
			x = 12
		if x == 9:
			print "Screw the bulb back in."
			print "Press O."
			y = raw_input("Is the light now on? ")
			x = 13
	# Step 10
	if x == 10:
		if col == "p" or col == "purple":
			print "Press I."
			x = 14
		if col == "r" or col == "red":
			print "Press I."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 13
		if col == "b" or col == "blue":
			print "Press O."
			x = 15
		if col == "y" or col == "yellow":
			print "Press O."
			print "Screw the bulb back in."
			y = raw_input("Is the light now on? ")
			x = 12
		if col == "g" or col == "green":
			print "Screw the bulb back in."
			print "Press I."
			y = raw_input("Is the light now on? ")
			x = 13
		if x == 10:
			print "Screw the bulb back in."
			print "Press O."
			y = raw_input("Is the light now on? ")
			x = 12
	# Step 11
	if x == 11:
		if ind == "sig":
			y = raw_input("Does the bomb have the indicator labeled \"SIG\"? ")
		if ind == "clr":
			y = raw_input("Does the bomb have the indicator labeled \"CLR\"? ")
		if ind == "frq":
			y = raw_input("Does the bomb have the indicator labeled \"FRQ\"? ")
		if ind == "frk":
			y = raw_input("Does the bomb have the indicator labeled \"FRK\"? ")
		if y == "y" or y == "Y" or y == "yes" or y == "Yes" or y == "YES":
			print "Press I."
			print "Screw the bulb back in."
		else:
			print "Press O."
			print "Screw the bulb back in."
	# Step 12
	if x == 12:
		if y == "y" or y == "Y" or y == "yes" or y == "Yes" or y == "YES":
			print "Press I."
		else:
			print "Press O."
	# Step 13
	if x == 13:
		if y == "y" or y == "Y" or y == "yes" or y == "Yes" or y == "YES":
			print "Press O."
		else:
			print "Press I."
	# Step 14
	if x == 14:
		if mat == "o" or mat == "opaque":
			print "Press I."
			print "Screw the bulb back in."
		else:
			print "Press O."
			print "Screw the bulb back in."
	# Step 15
	if x == 15:
		if mat == "s" or mat == "see-through":
			print "Press I."
			print "Screw the bulb back in."
		else:
			print "Press O."
			print "Screw the bulb back in."
	raw_input("Press enter to continue.")
	ktane()
ktane()
# ....is some good shit
