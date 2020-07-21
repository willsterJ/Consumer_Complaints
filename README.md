## Consumer Complaints Report
This project was written and compiled in Python 3.7.8

To run the program, from the main parent directory:
```
./run.sh
```
Input files should be put inside ./input/

Output files are found in ./output/

### Summary of design

The general approach I took to generate the report is to use a 
table data structure that will map corresponding keys to an
item object. Since our unique identifier is product and year
our mapping will constitute the following:

layer1[product] -> layer2[year] -> uniqueItem

Accessing the item takes constant time.
After processing all the rows in the input file, we then
proceed to sort the keys of the table by order of product
and then year before writing final result to report.