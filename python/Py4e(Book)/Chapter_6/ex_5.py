data = "X-DSPAM-Confidence: 0.8475"

length = data.find(":") + 1

value = float(data[length:])

print(value)