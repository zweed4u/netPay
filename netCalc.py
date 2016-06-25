print

wage=27
oWage=wage*1.5
cleaningFee=44
housingDeduction=350
tax=0.229692671

wk1=raw_input('Hours worked week 1 excluding ovetime? ')
if wk1=='':
	wk1=40
else:
	wk1=int(wk1)
oWk1=raw_input('Hours worked overtime for week 1? ')
if oWk1=='':
	oWk1=0
else:
	oWk1=int(oWk1)
wk2=raw_input('Hours worked week 2 excluding ovetime? ')
if wk2=='':
	wk2=40
else:
	wk2=int(wk2)
oWk2=raw_input('Hours worked overtime for week 2? ')
if oWk2=='':
	oWk2=0
else:
	oWk2=int(oWk2)
gross=(wage*wk1)+(wage*wk2)+(oWage*oWk1)+(oWage*oWk2)
print
print 'Gross: $'+str(gross)
print 'Net: $'+str(gross*(1-tax)-cleaningFee-housingDeduction)
print