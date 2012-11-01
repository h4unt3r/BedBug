def upLabel(label):
	if label == "zzzz":
		raise OverflowError("Reached label limit :P")
	label = list(label)
	for i in range(-1, -(len(label)+1), -1):
		if label[i] < "z" and label[i].isalpha():
			label[i] = chr(ord(label[i]) + 1)
			for j in range(i + 1, 0):
				label[j] = "a"
			return "".join(label)

if __name__ == "__main__":
	import time
	label = "aaaa"
	while not "zzzz" in label:
		print label
		time.sleep(0.1)
		label = upLabel(label)
