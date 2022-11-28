first_line = "Снова приоделись ели"
secondd_line = "В шубы с белой бахромой,"
third_line = "И метут, метут метели."
fourth_line = "Ох, как холодно зимой!"

f = open('file.txt', 'w')

f.writelines(list(map(lambda x: x+'\n', [first_line, secondd_line])))
f.close()


f = open('file.txt', 'a')

f.writelines(list(map(lambda x: x+'\n', [third_line, fourth_line])))
f.close()
