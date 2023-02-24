wordsDict = {}  # global words dict
lettersDict = {}  # global letter dict


def readFiles(filename):  # readFiles function which opens the file & iterates each line through handle
    handle = open(filename, 'r')  # open file and set it to handle
    for line in handle:  # for loop which un-packages handle into line
        stripped_line = cleanupLine(line)  # sets stripped_line to the function cleanupLine
        countWords(stripped_line)  # calls countWords with stripped_line
        countLetters(stripped_line)  # calls countLetters with stripped_line


def countWords(line):  # countWords function which sets line to lowercase and counts the words which are put in dict
    line = line.lower()  # sets anything in line to lowercase
    text_list = line.split()  # splits anything in line and puts it in text_list
    for word in text_list:  # for loop that un-packages anything in text_list and puts it in word
        wordsDict[word] = wordsDict.get(word, 0) + 1  # gets words from word inside of text_list and puts in dict


def countLetters(line):  # countWords function which sets line to lowercase and counts the letters which are put in dict
    line = line.lower()  # sets anything in line to lowercase
    for string in '0123456789. "' + "'":  # replaces 0-9, ., ", ', or space with empty string
        line = line.replace(string, '')   # replace the parameters mentioned above with empty string
    text_list = line.strip()  # sets strips the line and puts it in text_list
    for letter in text_list:  # for loop that un-packages anything in text_list and puts it in word
        lettersDict[letter] = lettersDict.get(letter, 0) + 1  # gets letters from letter inside of text_list
        # & put in dict


def cleanupLine(line):  # cleanupLine function which removes unwanted characters and replaces them with space
    for string in '-,_/*+?><;:[]{}`~"!@#$%^&*()|.=':  # for loop with the removed characters
        line = line.replace(string, ' ')  # replaces the removed characters with space
    return line  # returns the line with the unwanted characters removed


def results():  # results function where readFiles is called and values are printed into a list
    readFiles('text1.txt')  # calls readFiles and passes text1.txt
    result = []  # creates list called result
    letter_value = lettersDict['e']  # find key e and put the value into the variable
    word_value = wordsDict['to']  # find key to and put the value into the variable
    wordsDict.clear()  # clears dict
    lettersDict.clear()  # clears dict
    readFiles('text2.txt')  # calls readFiles and passes text2.txt
    letter_value2 = lettersDict['t']  # find key t and put the value into the variable
    word_value2 = wordsDict['the']  # find key the and put the value into the variable
    lettersDict.clear()  # clears dict
    wordsDict.clear()  # clears dict
    readFiles('text3.txt')  # calls readFiles and passes text3.txt
    letter_value3 = lettersDict['w']  # find key w and put the value into the variable
    word_value3 = wordsDict['computer']  # find key computer and put the value into the variable
    result.append(letter_value)  # append value into list
    result.append(letter_value2)  # append value into list
    result.append(letter_value3)  # append value into list
    result.append(word_value)  # append value into list
    result.append(word_value2)  # append value into list
    result.append(word_value3)  # append value into list
    print(result)  # print the list


results()  # calls the function result to start the program
