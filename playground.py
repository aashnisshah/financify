import csv

# variables
dateBlock = []
transactionTypeBlock = []
debitTransBlock = []
creditTransBlock = []
currentBalanceBlock = []
finData = [dateBlock, transactionTypeBlock, debitTransBlock, creditTransBlock, currentBalanceBlock]



def readData(filename):
	mortgageTotal = 0
	condofeesTotal = 0
	miscTotal = 0

	with open(filename, 'rb') as csvfile:
		dataReader = csv.reader(csvfile, delimiter=',')
		for row in dataReader:
			dateBlock.append(row[0])
			transactionTypeBlock.append(row[1])
			debitTransBlock.append(row[2])
			creditTransBlock.append(row[3])
			currentBalanceBlock.append(row[4])

			# mortgage for Toronto Condo
			if "Electronic Funds Transfer MORTGAGE PAYMENT MTG" in row[1]:
				mortgageData = [dateBlock, transactionTypeBlock, debitTransBlock, creditTransBlock, currentBalanceBlock]
				mortgageTotal = mortgageTotal + convertDollarToInt(row[2])

			# Toronto condo fees
			elif "Electronic Funds Transfer PREAUTHORIZED DEBIT 000000000000000" in row[1]:
				condofeesData = [dateBlock, transactionTypeBlock, debitTransBlock, creditTransBlock, currentBalanceBlock]
				condofeesTotal = condofeesTotal + convertDollarToInt(row[2])

			else:
				miscData = [dateBlock, transactionTypeBlock, debitTransBlock, creditTransBlock, currentBalanceBlock]
				miscTotal = miscTotal + convertDollarToInt(row[2])
		
		printTotals(mortgageTotal, condofeesTotal, miscTotal)

		finData = [dateBlock, transactionTypeBlock, debitTransBlock, creditTransBlock, currentBalanceBlock]
		return finData

def printTotals(mortgageTotal, condofeesTotal, miscTotal):
	print "Mortgage Total: ", mortgageTotal
	print "Condo Fees Total: ", condofeesTotal
	print "Misc Total: ", miscTotal


def convertDollarToInt(value):
	if value == "":
		return 0

	value = value.replace("$","").replace(",","")
	return float(value)



def main():
	data = readData('acc.csv')
	#print data


if __name__ == "__main__":
    main()