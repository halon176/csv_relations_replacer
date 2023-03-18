## CSV Rlations Replacer

The script takes as input two CSV files (located in the same folder), then offers the possibility to replace a
column of the first file with one from the second, taking as a reference the values in the table that indicate
a correlation.

### Requirements
The script may work with any version of [Python 3](https://github.com/python/cpython).

### Example
In the same folder as the script, we have two files: <code>games.csv</code> and <code>geners.csv</code>. The script
automatically detects them and offers us the option to select which one to modify and which one to use as a reference.

| id  | game      | ref_gen |
|-----|-----------|---------|
| 1   | Lineage 2 | 1       |
| 2   | Warcraft  | 1       |
| 3   | Patrician | 2       |


| id  | gener           |
|-----|-----------------|
| 1   | MMORPG          |
| 2   | Strategy        |
| 3   | Text adventures |


As we can see, in the games table there is a column called "ref_gen" which is a reference to the primary key of
the geners table. 

At this point, the script will ask us 
1. the column of table <code>games</code> to replace
2. the column of table <code>generes</code> to use as a reference
3. the column with which we want to replace the column with the references in the games table.

As a result, we will have a new CSV file (the input files will not be modified) that is the outcome of this
modification. In our example, it is the replacement of <code>games.ref_gen</code> with <code>geners.name</code>.

| id  | game      | ref_gen  |
|-----|-----------|----------|
| 1   | Lineage 2 | MMORPG   |
| 2   | Warcraft  | MMORPG   |
| 3   | Patrician | Strategy |

