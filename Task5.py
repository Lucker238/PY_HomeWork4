# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

path1 = 'C:/Users/User/Desktop/Geekbrains/Python/HW4/file1.txt'
path2 = 'C:/Users/User/Desktop/Geekbrains/Python/HW4/file2.txt'
f1 = open(path1, 'r')
data1 = f1.read()
f1.close()
f2 = open(path2, 'r')
data2 = f2.read()
f2.close()

def create_dict(data):
    array = data.split(' + ')
    pows = []
    indxs = []
    result_dict = {}
    for i in array:
        mid = i.find('^')
        if mid != -1:
            pows.append(i[mid+1:])
            indxs.append(i[:mid-1])
            if not len(indxs[-1]):
                indxs[-1] = 1
            result_dict[int(pows[-1])] = int(indxs[-1])
        elif i.find('x') != -1:
            indxs.append(i[:i.find('x')])
            pows.append("1")
            if not len(indxs[-1]):
                indxs[-1] = 1
            result_dict[int(pows[-1])] = int(indxs[-1])
        else:
            indxs.append(i)
            pows.append('0')
            result_dict[int(pows[-1])] = int(indxs[-1])
    return result_dict


def sum_dict(dict1, dict2):
    return dict((x, dict1.get(x, 0) + dict2.get(x, 0)) for x in set(dict1)|set(dict2))

def make_final_polynomial(d: dict):
    result = []
    for i in d:
        if i == 0:
            result.append(str(d[i]))
        elif i == 1:
            if d[i] == 1:
                result.append('x')
            else:
                result.append(str(d[i])+'x')
        else:
            if d[i] == 1:
                result.append("x"+str(i))
            else:
                result.append(str(d[i])+"x^"+str(i))

    return ' + '.join(result[::-1]) 


d1 = create_dict(data1)
d2 = create_dict(data2)
sum_d = sum_dict(d1,d2)
print(make_final_polynomial(sum_d))
