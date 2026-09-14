from data_define import Record
import json
class FileReader:
    def read_data(self) -> list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path
    def read_data(self):
        record_list = []
        f = open(self.path,"r",encoding="UTF-8")
        for line in f.readlines():
            line = line.strip()#消除每一行数据中的\n
            line_list = line.split(",")
            record = Record(line_list[0],line_list[1],int(line_list[2]),line_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
            self.path = path
    def read_data(self):
        record_list = []
        f = open(self.path,"r",encoding="UTF-8")
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list

            





if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/Python学习/part3/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:/Python学习/part3/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for i in list1:
        print(i)

    for i in list2:
        print(i)