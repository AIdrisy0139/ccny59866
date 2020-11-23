

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
