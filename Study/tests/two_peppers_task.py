list_c = ['.csv', '.exe','.jpeg','.json','.mkv','.mp3', '.mp4', '.py','.xml','.zip']
list_c = sorted(list_c)
new_list = []
byte = ['K','KB','MB',"GB"]
size = []
with open('files.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        new_list.append(line.split(' '))
    new_list = sorted(new_list)
    for item in list_c:
        digit = 0
        for item_1 in new_list:
            if item_1[0].endswith(item):
                print(item_1[0])
                if item_1[2] == 'B':
                    digit += int(item_1[1])
                elif item_1[2] == 'KB':
                    digit += int(item_1[1])*1024
                elif item_1[2] == 'MB':
                    digit += int(item_1[1])*1024*1024
                elif item_1[2] == 'GB':
                    digit += int(item_1[1])*1024*1024*1024
        if digit >= 1073741824: # байт в гигабайте
            digit = digit//1024//1024//1024
            size = byte[3]
        elif digit >= 1048576: # байт в мегабайте
            digit = digit/1024/1024
            size = byte[2]
        elif digit >= 1024: # байт в килобайте
            digit = digit//1024
            size = byte[1]
        else:
            digit = digit
            size = byte[0]

        print(f"----------\nSummary: {round(digit)} {size}\n")