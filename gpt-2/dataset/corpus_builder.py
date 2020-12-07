import csv
import random
def read_data(path):
	base = []
	with open(path, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['FalseSent'][-1] != '.':
				row['FalseSent'] += '.'
			base.append(row['FalseSent'])
	return base

def read_answers(path):
	answers = []
	with open(path, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
		for row in spamreader:
			for i in range(len(row)):
				if row[i][-1] != ".":
					row[i] += '.'
			answers.append(row)
	return answers



def main():
	bases = read_data('subtaskC_data_all.csv')
	answers = read_answers('subtaskC_answers_all.csv')

	contents = []
	for i in range(len(bases)):
		for answer in answers[i][1:]:
			contents.append(bases[i] + ' ' + answer+'<|endoftext|>\n')

	random.shuffle(contents)
	with open("data.txt","w") as f:
		for content in contents:
			f.write(content)





if __name__ == '__main__':
	main()