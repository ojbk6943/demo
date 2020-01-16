import csv
list = ['1', '2', '3', '4', '5']
outfile = 'h:/test.csv'
out = open(outfile, 'a')
csv_writer = csv.writer(out)
csv_writer.writerow(list)
out.close()
# out = open(outfile, 'a', newline='')
# csv_writer = csv.writer(out)
# csv_writer.writerow(list)
