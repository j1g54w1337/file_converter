#!/usr/bin/env python3
## Import modules
import pypandoc

## Open markdown file
get_file = input("File to convert (without extension): ")
get_type = input("Which file type (md, html): ")
convert_to = input("Convert to (pdf, html): ")

file_name = get_file + "." + get_type

#with open(file_name, 'r') as f:
#    print(f"Going to convert {file_name} to {convert_to}")
#    read_source = f.read()
#    pypandoc.convert_file("./" + read_source, convert_to, outputfile=get_file + "." + convert_to)

pypandoc.convert_file("./" + file_name, convert_to, outputfile=get_file + "." + convert_to)

#doc = pandoc.read(file)

#doc.save(get_file + "." + convert_to)

#print(f"Going to convert {file} to {convert_to}")
#pypandoc.convert_file(file, convert_to, outputfile=get_file + "." + convert_to)


