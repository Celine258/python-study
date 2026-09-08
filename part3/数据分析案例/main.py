from data_define import Record
from file_define import TextFileReader,JsonFileReader
from pyecharts.charts import Bar
from pyecharts import options as opts 
from pyecharts.globals import ThemeType
text_file_reader = TextFileReader("D:/Python学习/part3/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/Python学习/part3/2011年2月销售数据JSON.txt")
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
all_data = jan_data + feb_data

#开始进行数据计算
date_dict = {}
for record in all_data:
    if record.date in date_dict:
        date_dict[record.date] += record.money
    else:
        date_dict[record.date] = record.money

bar = Bar(init_opts=opts.InitOpts(ThemeType.LIGHT))
bar.add_xaxis(list(date_dict.keys()))
bar.add_yaxis("money",list(date_dict.values()),label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="每日营业额")
)
bar.render("柱状图.html")
print(date_dict.keys())