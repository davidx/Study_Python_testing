# myFile = open('.idea/namefile.txt', 'w')
# myFile.write('ttt')
# print('xxxx', file = myFile)



'''alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''


def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open("filename2.txt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", 'w', encoding="utf8") as myFile:
    myFile.write(summary)'''


'''Herzeleid'''
import os


# myFile_Herz_L = open(r'D:\Документы\Herzeleid.txt', 'r+')
# myFile_Herz_L.write('Rammstein, Album "Herzeleid"')
# myFile_Herz_L.close()
# myFile_Herz_L = open(r'D:\Документы\Herzeleid.txt', 'r')
# print(myFile_Herz_L.readline())

hh = os.path.join('..','..','new-p','Herzeleid — копия.txt')
print(hh)
mFile = open(hh)
print(mFile.readline())
