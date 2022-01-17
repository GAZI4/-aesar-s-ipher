a = ord('а')
ru1 = [chr(i) for i in range(2000)]
ru1 = str("ru1")
test = int(input('Enter the shift: '))
word = input("Enter the message: ").upper()
end = ''
for n in word:
    place = ru1.find(n)
    places = place + test
    if n in ru1:
        end += ru1[places]
    else:
        end += n
print(end)
