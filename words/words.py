with open('660000_parole_italiane.txt', 'r') as reader:
    with open('five-char-words.txt', 'a') as a_writer:
        line = reader.readline()
        while line != '':
            if len(line) == 6:  # 5 character + \n
                a_writer.write(line)
            line = reader.readline()
