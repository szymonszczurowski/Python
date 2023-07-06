message1 = 'Processing file %s' #literal
print(message1 % ('file_1.txt'))

message2 = 'File %s has size %d KB'
print(message2 % ('file_txt', 100))

message3 = 'File %20s has size %10d KB'#rezerwacja znaków
print(message3 % ('file.txt', 100))

#Nowszy sposób
message4 = 'Processing file {0:s}' #liczba to kolejność parametru
print(message4.format('file.txt'))

message5 = 'File {0:s} has size {1:d} KB'
print(message5.format('file_txt', 100))

#mozna zmienac kolejnosc
message6 = 'File {1:s} has size {0:d} KB'
print(message6.format(100, 'file_txt'))

message7 = 'File {0:20s} has size {1:10d} KB'
print(message7.format('file_txt', 100))