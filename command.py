import os

print("Extracting vcd file")
os.system('python vcd_extract_bin.py')

print('Editing c template file.')
os.system('python ctransf.py')
print('File transfer finish')

print('Compiling C file')
os.system('gcc -o runme test.c')

print('start running')
os.system('./runme')

print('showing the result')
os.system('cat result.txt')