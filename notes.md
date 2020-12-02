

# Debug Campaign
- ~~Null Terminator at the start leading to issues~~
    - Think overflow detection is wrong
    - ~~ Increment the subString ptr if its a null~~
        - ioctl error
- Is over flow detection working?
    - Yes?
- Why IS `overFlowString` null on when building with overFlow String?
```
In Overflow string building
overFlowIndex : 246 
overFlowBuffer = [ 2551049411 ]  
buffer =  
j = 0 
startIndex : 1 
subString:  
overFlowBuffer[LAST] == NULLTERM 
strcpy: overFlowString:  
overFlowString:  
```

# WTF moments
- innapropriate ioctl whenever dealing with `substring` outside of the for loop
- Moving `overFlowFlag = false;` made a difference even though there isnt any branching in the code

# Parallel Parsing
```C
ReadSet(const char *n, int column, const char *delim)
{
    //n = file name

    size_t fullSize;

    struct stat st;
    fstat(fd, &st);
    size_t fullSize = st.st_size;

    ...
    ...
    ...

    qsort(<...>);


}

//pthread Function
ReadPartition(int fd, size_t partitionSize, off_t startPoint)
{
    size_t totalBytesRead = 0;

    char * buffer = malloc(partitionSize); //Do Static Alloc for now

    off_t offset = start;

    size_t bytesRead = 0;
    while(totalBytes < partitionSize)
    {
        bytesRead = pread(fd, &buffer,BUFFER_SIZE, offset);
        offset += bytesRead;
            for(char *ptr = buffer; *ptr != '\0'; ++ptr)
            {
                ...
            }
        <OVFL DETECTION>
    }
    free(buffer);
}
```
