from itemadapter import ItemAdapter
import csv
import os

class CsvWriterPipeline:
	def open_spider(self, spider):
		self.file_name = 'data/deputies.csv';
		self.file = open(self.file_name, 'a+')
		self.csvwriter = csv.writer(self.file)
		self.has_header = os.stat(self.file_name).st_size != 0

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		if (not self.has_header):
			header_keys = list(ItemAdapter(item).asdict().keys())
			self.csvwriter.writerow(header_keys)
			self.has_header = True
		self.csvwriter.writerow([item[key] for key in item.keys()])
		return item