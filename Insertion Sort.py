def insertionSort(a):
   
    n= len(a)
r=""    
while r != 'n':    
        list = input('Enter a list of numbers seperated by commas:')
        a = list.split(',') 
        n= len(a)
        for i in range(1, n):
          
                key = a[i]
          
                j = i-1
                while j >=0 and key < a[j] :
                        a[j+1] = a[j]
                        j -= 1
                a[j+1] = key
        print ("Sorted array is:")
        for x in range(n):
                print (a[x])
        r=input("Do you want to sort another list? (y/n)")
