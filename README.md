# NucClade
---
A module to parse nuclear data from the [ENSDF](https://www.nndc.bnl.gov/ensarchivals/) and aimed at facilitating the use of the decay data flexibly for other purposes like representation and research. Initially, it is meant as a tool for building custom relational and/or decay diagrams, which motivates the name (combining the words **Nuclide** and **Clade**). Clade diagrams (cladograms) in biology represent ancestral relations between groups of species, and nuclide decay chains connecting parent and daughter nuclides are vissually and conceptually similar.

### Motivation

Nuclear data is compiled and available online through many sources. One of the most complete is provided by the [IAEA](https://www-nds.iaea.org/). Nuclear decay and structure data are available in the form of text files ([ENSDF](https://www.nndc.bnl.gov/ensarchivals/)) and also [utility programs](https://www-nds.iaea.org/public/ensdf_pgm/) are provided. 

Nevertheless, the utility programs **do not use a common framework for parsing**, **they are goal-specific** and they provide **processed information** which compromises extensibility (it is difficult to write code based on their output). Additionally, many are written in fixed format characteristic of old fortran versions, and as a researcher wanting to visualize and work with the data, using them to build a custom code would take too much of time while certainly carrying on some of the limitations.

Additionally there is [PyNE](https://pyne.io) which contains a module to parse and extract information from the [ENSDF](https://www.nndc.bnl.gov/ensarchivals/) files, but as of the beginning of 2020, extracted data **differs from the file considerably** and **parsing functions do not respect the structure** defined in the [ENSDF format manual](https://www.nndc.bnl.gov/nndcscr/documents/ensdf/ensdf-manual.pdf) which makes debugging a task of comparable magnitude to rewriting the code.

This module aims to help extracting the data contained in the [ENSDF](https://www.nndc.bnl.gov/ensarchivals/) files and facilitate its consolidation in any other form and/or its representation and such research related uses. It is a module I needed during my PhD work, which I wanted to make usable for others and that hopefully solves all the issues mentioned above.

### Design concept

The code is mindful of the [ENSDF format manual](https://www.nndc.bnl.gov/nndcscr/documents/ensdf/ensdf-manual.pdf). It is a data format that mixes **fixed positioned data** with **flexible length** of structures. For this reason, the code uses a combination of **fixed-length-string-cutting** and **regular expressions** to read the values/units and converting them into numeric or other types, preserving as much as possible the vocabulary and definitions used in the manual. This makes the code clear and helps resolving inconsistencies between extracted and tabulated values, which is an undesirable outcome but often tedious to resolve.

The parsing functions should be independent of the syntax-specific structures to facilitate development and debugging. A set of **syntax-specific expressions** and **string-cutting instructions** are defined in dictionaries used by the parser function, avoiding explicit dependencies on the syntax (such as *if*-clauses containing hard-coded expressions).

### Authors

*Leonel Morejon* and anyone interested in contributing

### References

- ENSDF manual (https://www.nndc.bnl.gov/nndcscr/documents/ensdf/ensdf-manual.pdf)

