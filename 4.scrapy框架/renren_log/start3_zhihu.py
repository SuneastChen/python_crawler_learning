from scrapy import cmdline  
#需要输出那种格式的数据，打开哪个命令前的注释  
#编译执行  
cmdline.execute("scrapy crawl log3zhihu" .split())  
#输出json数据  
#cmdline.execute("scrapy crawl scrapy_name -o ductdetail.json" .split())  
#输出excle表格数据  
# cmdline.execute("scrapy crawl scrapy_name -o LJductdetail.csv -t csv" .split()) 