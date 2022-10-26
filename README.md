# SudokuValidation
A Sudoku puzzle uses a 9 × 9 grid in which each column and row, as well as
each of the nine 3 × 3 subgrids, must contain all digits from 1 t 9 without repetition.
It also checks whether all the numbers are in range.

This project consists of designing a multithreaded application written in Python that determines whether the solution to
a Sudoku puzzle is valid.
The strategy used for multithreading in this application is as follows:- 

* Nine threads to check that each column contains the digits 1 through 9
* Nine threads to check that each row contains the digits 1 through 9
* Nine threads to check that each of the 3 × 3 subgrids contains the digits 1
through 9

This would result in a total of 27 separate threads for validating a Sudoku puzzle solution.
The python libraries used in this project are colorama, pyfiglet and threading.

colorama and pyfiglet can be installed as follows:

```
pip install colorama
pip install pyfiglet
```
