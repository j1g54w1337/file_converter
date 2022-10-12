#!/usr/bin/env python3
## Import modules
import pypandoc

def file_converter(file_name, convert_to, get_file):
  pypandoc.convert_file("./" + file_name, convert_to, outputfile=get_file + "." + convert_to)

def main():
  ## Open markdown file
  get_file = input("File to convert (without extension): ")
  get_type = input("Which file type (md, html): ")
  convert_to = input("Convert to (pdf, html): ")

  file_name = get_file + "." + get_type

  file_converter(file_name, convert_to, get_file)

if __name__ == "__main__":
  main()

