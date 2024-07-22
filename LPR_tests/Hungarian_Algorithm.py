
def getData():
    wTest=False
    hTest=False
    
    print("How many x elements do you have")
    width = input()
    while(wTest == False):
        try:
            width = int(width)
            wTest = True
        except:
            print("Please enter a number")
    print("How many y elements do you have")
    
    height = input()
    while(hTest == False):
        try:
            height= int(height)
            hTest = True
        except:
            print("Please input a number")
    arr = []
    row = []
    print(arr)
    for i in range(height):
        for j in range(width):
            inp = input("please insert your next value of row "+ str(j)+" and column "+ str(i) +":\t")
            row.append(inp)
        arr.append(row)
        row=[]
    return arr       
def row_reduction(arr):
    min = ""
    height = 0
    width =0
    for i in arr:
        
        width=0
        for el in i:
            if min == "":
                min = el
            elif el< min:
                min = el
            width+=1
        for el in i:
            arr[height][width] = int(el)-int(min)
        height+=1
    return arr
            

def hung_alg(arr):
    row_reduction(arr)




def main():
    print(row_reduction(getData()))
main()