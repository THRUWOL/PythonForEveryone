str = 'X-DSPAM-Confidence: 0.8475 '

number = float(str[str.find(':')+1:])

print(number)
