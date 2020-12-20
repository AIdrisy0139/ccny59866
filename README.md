# CCNY 59866 Senior Design Project
Fall 2020 Semester

## Members: 
	- Arikuzzaman Idrisy
	- Ersi Nurcellari
	- Fathima Reeza
	- Haibin Mai

## Goal: 
Increase the performance of pre-existing ministat program. The objective was two fold, one, execute micro-optimizations uncovered through framegraph analysis, two, introduce mutli-threading for parallel execution.

## Proposed Micro-Optimizations
- Reading the file contents.
Use read / write / open systems calls directly to read larger blocks of data at a time. 
	- Hurdle: Seems the gain is very minimal and not less than CPU Noise
	- Solution: Dont use it?
<img src="micro_vs_stock.png">
- String tokenization
strtok is not is fast nor thread safe. Swap it out and use strsep instead or use memchr.
- String to double conversion.
Replace the standard C library strtod function with an open-source alternative.
- qsort 
Replace the standard C library qsort with a faster inline sorting algorthim. https://github.com/appnexus/acf/blob/master/common/an_qsort.inc

## Multi Threading Schema
### Parallel File Parsing
- Objective: For a single file passed to ministat have multiple threads simultaneously read from the file
- Requires reworking the raw I/O micro-optimization to use pread for thread safety
	- Solved by manually keeping track of the cursor point
- Partitoning scheme was a bit counterintuive. Instead of each partion being equal number of bytes, they are set to hold whole integers. This requries looking ahead to find a \n character and adjusting the end and start points of the partitions accodingly
- Hurdle: Using one `struct dataset` per file is two slow. Using a mutex to protect writing to the dataset marginilzes any gains obtained from parallelizations.
	- Solution: Have each thread work on their own local `struct dataset`. Create the thread local datasets in the `ReadSet` function and pass it in `partition` to the `ReadPartition` function. When joining the threads call `MergeDataset` which will merge the thread local datasets to the dataset for the file. 
	- __This shows performance gains.__

<img src="images/parallel_vs_stock.png">

This graph shows interesting behavior, 6 threads is higher than the baseline `ministat` edition. Two and four threads almost equaly performant as the baseline. Eight threads shows a clear performance gain on large file sizes.



---

# Pre-Existing README
## ministat
A small tool to do the statistics legwork on benchmarks etc.

Written by Poul-Henning Kamp, lured into a dark Linux alley and clubbed over the head and hauled away to Github by yours truly.

## Build & Install

There should be no dependencies besides the standard libraries and a functional tool-chain.

	$ cd ministat/
	$ make
	$ make PREFIX=/usr install
	install -m 0755 ministat  /usr/bin/ministat

## Usage
The FreeBSD man page is very relevant, pursue it [here](http://www.freebsd.org/cgi/man.cgi?ministat).

	Usage: ministat [-C column] [-c confidence] [-d delimiter(s)] [-ns] [-w width] [file [file ...]]
		confidence = {80%, 90%, 95%, 98%, 99%, 99.5%}
		-C : column number to extract (starts and defaults to 1)
		-d : delimiter(s) string, default to " \t"
		-n : print summary statistics only, no graph/test
		-q : print summary statistics and test only, no graph
		-s : print avg/median/stddev bars on separate lines
		-w : width of graph/test output (default 74 or terminal width)

## Example
From the FreeBSD [man page](http://www.freebsd.org/cgi/man.cgi?ministat)

	$ cat << EOF > iguana
	50
	200
	150
	400
	750
	400
	150
	EOF

	$ cat << EOF > chameleon
	150
	400
	720	
	500
	930
	EOF

	$ ministat -s -w 60 iguana chameleon
	x iguana
	+ chameleon
	+------------------------------------------------------------+
	|x      *  x	     *	       +	   + x	            +|
	| |________M______A_______________|			     |
	| 	      |________________M__A___________________|      |
	+------------------------------------------------------------+
	    N	  Min	     Max     Median	   Avg	     Stddev
	x   7	   50	     750	200	   300	  238.04761
	+   5	  150	     930	500	   540	  299.08193
	No difference proven at 95.0% confidence
