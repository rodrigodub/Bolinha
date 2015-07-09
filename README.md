# Bolinha
*Bolinha is a script to process LAS files*

It will take a LAS 3.0 file as input, and will output as many CSV files as relevant, depending on each LAS file contents.

Bolinha will read each line of the input file. If line equals to **~PARAMETER INFORMATION** then it will collect all relevant COLLAR information and store it in a list, until it finds a line equals to '#------------------------------------------------------------'.

For each **~TOPS_DEFINITION[x]** section it will take the THIRD line to define what the new output will be called, and store all fieldnames as the first row in a list. After the next '#------------------------------------------------------------', it will store the data as subsequent rows of the same list, until it finds the next '#------------------------------------------------------------'.

For each **~LOG_DEFINITION[x]** section it will take the SECOND line to define what the new output will be called, and store all fieldnames as the first row in a list. After the next '#------------------------------------------------------------', it will store the data as subsequent rows of the same list, until it finds the next '#------------------------------------------------------------'.

After reaching the end of input file, Bolinha will then write all the collected lists as individual CSV files.
