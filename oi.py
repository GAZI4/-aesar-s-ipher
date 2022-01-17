test = (int(input('Enter the shift: ')))
word = (input('Enter the message: '))
rus = [chr(i) for i in range(2000)]
work = [rus[(i + test) % 2000] for i in range(2000)]
end = ''
for n in word:
	end += work[rus.index(n)]
print(end)
