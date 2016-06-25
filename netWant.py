print
net=raw_input('How much do you want net? ')
cleaningFee=44
housingDeduction=350
tax=0.229692671
hrRate=27
overRate=hrRate*1.5
workWeekHr=40
fullTimePayWeekly=hrRate*workWeekHr
gross=(float(net)+cleaningFee+housingDeduction)/(1-tax)
print 'You need to gross $'+str(gross)
print
print 'At $27/hr for a 40hr work week,'
print 'at $40.5/hr for overtime.'
print
if (gross-(2*fullTimePayWeekly))<=0:
	print 'You dont need any overtime!'
	print 'you need to work',workWeekHr+((gross%fullTimePayWeekly)/27),'hours over two weeks.'
	print 'or',(workWeekHr+((gross%fullTimePayWeekly)/27))/2,'hours/week'
else:
	overtimeHours=(gross-(2*fullTimePayWeekly))/overRate
	print 'You would need to work full time for 2 weeks (40 ea.)'
	print 'with',overtimeHours,'hours ovetime.'
	print 'or a full work week with',overtimeHours/2,'hours of overtime'
print

print 'FYI the breakeven point is:',(2*fullTimePayWeekly)*(1-tax)-cleaningFee-housingDeduction
print 'This is net of working two 40 hour week, no overtime.'
print