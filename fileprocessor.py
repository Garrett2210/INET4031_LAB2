#!/usr/bin/env python3

def process_file(filename):
	with open(filename, 'r') as file:
		lines = file.readlines()

	data = []
	hashtag_data = []

	for line in lines:
		if not line.startswith("#"):
			data.append(line.strip().split(":"))
		else:
			hashtag_data.append(line.strip().split(":"))

	print("Printing out User Data:\n")
	for item in data:
		print(f"The user {item[0]} has a password of {item[1]} and has userid {item[2]} and groupid {item[3]}")
	for item in hashtag_data:
		print(f"\n{item[0]} is skipped because it starts with a hashtag (is commented out)")
	print("\nEnd of User Data")

if __name__ == "__main__":
	process_file("fileprocessor.input")

