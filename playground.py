import csv

# variables
dateBlock = []
transactionTypeBlock = []
debitTransBlock = []
creditTransBlock = []
currentBalanceBlock = []
finData = [dateBlock, transactionTypeBlock, debitTransBlock, creditTransBlock, currentBalanceBlock]


def readData(filename):
	with open(filename, 'rb') as csvfile:
		dataReader = csv.reader(csvfile, delimiter=',')
		for row in dataReader:
			dateBlock.append(row[0])
			transactionTypeBlock.append(row[1])
			debitTransBlock.append(row[2])
			creditTransBlock.append(row[3])
			currentBalanceBlock.append(row[4])

		finData = [dateBlock, transactionTypeBlock, debitTransBlock, creditTransBlock, currentBalanceBlock]
		return finData


def convertDollarToInt(value):
	value = value.replace("$","").replace(",","")
	return value



def main():
	data = readData('acc.csv')
	print data


if __name__ == "__main__":
    main()