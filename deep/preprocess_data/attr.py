class Attr:
    file_name = list()
    file_attr = list()
    
    def __init__(self):
        f = open('list_attr_img.txt', 'r')
        self.lines = f.readlines()[2:]
    
    def parsing(self):
        for line in self.lines[:200]:
            line = line.rstrip('\n')
            jpg_position = line.find('jpg')
            name_length = jpg_position + 3
            self.file_name.append(line[:name_length])
            line = line[70:]
            tmp = list()
            for i in range(1000):
                if line[3 * i + 1] == '-':
                    tmp.append(0)
                else:
                    tmp.append(1)
            self.file_attr.append(tmp)

    def saving(self):
        try:
            f = open('mapper', 'w')
        except:
            f = open('mapper', 'a')
            f.seek(0)

        for i in range(len(self.file_name)):
            f.write(self.file_name[i])
            for val in self.file_attr[i]:
                f.write(","+str(val))
            f.write("\n")
        f.close()
