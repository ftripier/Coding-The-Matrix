from GF2 import one, zero

message = [
  [one, zero, one, zero, one],
  [zero, zero, one, zero, zero],
  [one, zero, one, zero, one],
  [zero, one, zero, one, one],
  [one, one, zero, zero, one],
  [zero, zero, zero, one, one],
  [zero, one, zero, one, one],
  [one, zero, one, zero, one],
  [zero, zero, one, zero, zero],
  [one, one, zero, zero, one],
  [one, one, zero, one, zero],
]

def bits_to_number(bits):
  number = 0

  if bits[4]:
    number += 1
  if bits[3]:
    number += 2
  if bits[2]:
    number += 4
  if bits[1]:
    number += 8
  if bits[0]:
    number += 16
  
  return number


def number_to_bits(number):
  ints = [
    number & 16,
    number & 8,
    number & 4,
    number & 2,
    number & 1,
  ]

  return [ zero if x == 0 else one for x in ints]

numbers_to_letters_map = {
  "0": 'a',
  "1": 'b',
  "2": 'c',
  "3": 'd',

  "4": 'e',
  "5": 'f',
  "6": 'g',
  "7": 'h',

  "8": 'i',
  "9": 'j',
  "10": 'k',
  "11": 'l',

  "12": 'm',
  "13": 'n',
  "14": 'o',
  "15": 'p',

  "16": 'q',
  "17": 'r',
  "18": 's',
  "19": 't',

  "20": 'u',
  "21": 'v',
  "22": 'w',
  "23": 'x',
  "24": 'y',
  "25": 'z',
  "26": ' '
}

def number_to_letter(number):
  converted = str(number)
  return numbers_to_letters_map[converted]

def add_bits(a, bitmask):
  new_bits = []
  for bits in a:
    new_bits.append([
      bits[0] + bitmask[0],
      bits[1] + bitmask[1],
      bits[2] + bitmask[2],
      bits[3] + bitmask[3],
      bits[4] + bitmask[4],  
    ])
  
  return new_bits

for i in range(27):
  random_bits = number_to_bits(i)
  decrypted_message = add_bits(message, random_bits)

  message_numbers = map(lambda x: bits_to_number(x), decrypted_message)
  try:
    decoded_message = ''.join([number_to_letter(x) for x in message_numbers])
  except KeyError:
    continue
  print(decoded_message)


