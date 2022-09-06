# Objective:
#   To put the names of columns in quote

import os

def add_quote(in_file, out_file):
    i=0
    with open(in_file, "r") as in_f:
        with open(out_file, "w") as out_f:
            for line in in_f.readlines():
                if i==0:
                    line=line.strip("\n")
                    columns = line.split(",")
                    out_line = ""
                    for col in columns:
                        if '"' not in col:
                            out_line += '"' + col + '",'
                        else:
                            out_line += col + ","
                    out_line = out_line.strip(',')
                    out_line+="\n"
                else:
                    out_line = line
                out_f.write(out_line)
                i+=1


class CSVColumnQuotePlugin:
    def input(self, infile):
       self.in_folder = infile
       #self.in_folder = "../PlumaPipline/MultiOmics/no_quotes"

    def run(self):
        pass

    def output(self, outputfile):
      #out_folder = "../PlumaPipline/MultiOmics"
      out_folder = outputfile
      files = os.listdir(self.in_folder)

      for f in files:
        if f!= ".DS_Store":
           in_file = os.path.join(self.in_folder, f)
           if (not os.path.isdir(in_file)):
              out_file = os.path.join(out_folder, f)
              add_quote(in_file, out_file)
