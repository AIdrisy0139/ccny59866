import os
import matplotlib.pyplot as plt
import numpy
import time

results = {}

def runInputDeck():
    global results
    ministatPath = "/home/aidrisy/ministat"
    inputFilesPath = "~/ccny59866/inputFiles"
        

    files = os.listdir("inputFiles")
    os.chdir(ministatPath)
    print(f"CWD Changed to :: {os.getcwd()}")
    for x in files:
        iFile = os.path.join(inputFilesPath,x)
        start = time.time()
        os.system(f"./ministat -q {iFile}")
        end = time.time()
        elapsed = end - start
        print(f"Time elapsed for {iFile} = {elapsed}")
        results[int(x)] = elapsed
    
    keys = results.keys()

    times = []
    for key in keys:
        times.append(results[key])
        
    return keys, times

def sortAndPlot(keys,times):
    keys = list(keys)
    keys.sort()
    print(f"Keys = {keys}")
    #print(f"Times = {times}")
    plotTimes = []
    for k in keys:
        plotTimes.append(results[k])

    print(plotTimes)
    plt.title("Original Ministat")
    plt.xlabel("Size of file in ints")
    #plt.xticks(keys)
    plt.ylabel("Running Time (Secs)")
    plt.plot(keys,plotTimes,'x--')
    #plt.scatter(keys,plotTimes)
    plt.savefig("plot.png")

def main():
    
    keys, times = runInputDeck()
    os.chdir("/home/aidrisy/ccny59866")
    print(f"CWD Changed to :: {os.getcwd()}")
    sortAndPlot(keys,times)

main()