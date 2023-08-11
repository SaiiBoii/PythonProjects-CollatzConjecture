def sequence(n:(int or float)): #Gives Collatz Sequence for any positive real number 

    #Error Handling to see if n is an int or float
    if not(type(n)==float or type(n)==int): 
        raise TypeError('sequence() takes argument of type "int" or "float"')
    
    #Error Handling to see if n>0
    elif n<=0: 
        raise ValueError('sequence() takes argument n>0')
    
    collatz_list=[n] #Initializing list

    #While loop continues till n!=1 (basis of Collatz Conjecture)
    while n!=1:

        #If n is even, divide it by 2 and append it to collatz list
        if n%2==0:
            n/=2
            collatz_list.append(n)

        #If n is odd, multiply 3 then add 1 and append it to collatz list
        else: 
            n=3*n+1
            collatz_list.append(n)

    #Defining result as collatz list and its length and peak 
    result=(collatz_list,f'len={len(collatz_list)-1}', f'peak={max(collatz_list)}') 

    return result #Returning the list

def seqbet(start:int,end:int,step=1,iterate=True): #Gives Collatz Sequence for multiple numbers in a range (with step)
    
    #Error Handling to see if range bounds are integers
    if not(type(start)==type(end)==int):
        raise TypeError('seqbet() takes arguments of type "int" only') 
    
    #Error Handling to see if start is less than end
    elif start>=end:
        raise ValueError('range start must be less than end')
    
    #Error Handling to see if start>0
    elif start<=0:
        raise ValueError('range start must be greater than 0')
    
    #Error Handling to see if step>0
    elif step<=0 or type(step)!=int:
        raise ValueError('step must be an integer greater than 0')
        
    #(By default iterate set to true), Iterating all numbers in the range and calling sequence() function
    if iterate: 
        for n in range(start,end+1,step):
            print(n,':',sequence(n))        
    else:
        collatz_dict={} #Initializing dictionary

        #Looping through range and adding numbers and their sequences to dictionary
        for n in range(start,end+1,step):
          collatz_dict[n]=sequence(n)

        return collatz_dict #Returning the dictionary



def seqlen(start:int,end:int,step=1): #Gives sequence lengths of all the numbers in given range (with step) 

    #Error Handling to see if range bounds are integers
    if not(type(start)==type(end)==int): 
        raise TypeError('seqbet() takes arguments of type "int" only') 
    
    #Error Handling to see if start is less than end
    elif start>=end:
        raise ValueError('range start must be less than end')
    
    #Error Handling to see if start>0
    elif start<=0:
        raise ValueError('range start must be greater than 0')
    
    #Error Handling to see if step>0
    elif step<=0 or type(step)!=int:
        raise ValueError('step must be an integer greater than 0')
    
    #Looping through all numbers in range and calling 2nd element i.e 'len' of the sequence() function
    for n in range(start,end+1,step):
        print(n,':',sequence(n)[1])
    

def seqpeak(start:int(1),end:int,step=1): #Gives sequence peaks of all the numbers in given range (with step) 

    #Error Handling to see if range bounds are integers
    if not(type(start)==type(end)==int):
        raise TypeError('seqpeak() takes arguments of type "int" only')
     
    #Error Handling to see if start is less than end
    elif start>=end:
        raise ValueError('range start must be less than end')
    
    #Error Handling to see if start>0
    elif start<=0:
        raise ValueError('range start must be greater than 0')
    
    #Error Handling to see if step>0
    elif step<=0 or type(step)!=int:
        raise ValueError('step must be an integer greater than 0')
    
    #Looping through all numbers in range and calling 3nd/last element i.e 'peak' of the sequence() function
    for n in range(start,end+1,step):
        print(n,':',sequence(n)[-1])

    
def peaks(start:int,end:int,step=1,smallest=False): #Gives numbers with smallest/largest peak in a given range (with step) 

    #Error Handling to see if range bounds are integers
    if not(type(start)==type(end)==int):
        raise TypeError('peaks() takes arguments of type "int" only') 
    
    #Error Handling to see if start is less than end
    elif start>=end:
        raise ValueError('range start must be less than end')
    
    #Error Handling to see if start>0
    elif start<=0:
        raise ValueError('range start must be greater than 0')
    
    #Error Handling to see if step>0
    elif step<=0 or type(step)!=int:
        raise ValueError('step must be an integer greater than 0')
    
    peaks_dict={} #Initializing dictionary
    result=[] #Initializing result numbers list

    #Looping through range to fill the dictionary with numbers and their peaks
    for n in range(start,end+1,step):
        peaks_dict[n]=max(sequence(n)[0]) #Calling the max peak value through first function

    if not(smallest): #By default set to False. Setting peak choice the min/max based on 'smallest' argument
      choice_peak=max(peaks_dict.values())
    else:
      choice_peak=min(peaks_dict.values())

    #Looping over the dictionary keys and appending the key to result list if the key value pair is equal to min/max peak
    for key in peaks_dict:
        if peaks_dict[key]==choice_peak:
            result.append(key)
    
    return (result,f'peak={choice_peak}') #Returning the result list and the min/max peak they hit
  
def lens(start:int,end:int,step=1,smallest=False): #Same logic as peaks() but with lengths
    if not(type(start)==type(end)==int):
        raise TypeError('lens() takes arguments of type "int" only') 
    
    elif start>=end:
        raise ValueError('range start must be less than end')
    
    elif start<=0:
        raise ValueError('range start must be greater than 0') 
    
    #Error Handling to see if step>0
    elif step<=0 or type(step)!=int:
        raise ValueError('step must be an integer greater than 0')
    
    final={}
    result=[]
    for n in range(start,end+1,step):
        final[n]=len(sequence(n)[0])-1 #Selecting length of sequence

    if not(smallest):
      choice_len=max(final.values())
    else:
      choice_len=min(final.values())

    for key in final:
        if final[key]==choice_len:
            result.append(key)
    
    return (result,f'len={choice_len}')   


def stats(start:int,end:int,step=1): #Shows sequences and smallest/largest peak/length values of all numbers in range
    #Error Handling logic same as previous functions 
    if not(type(start)==type(end)==int):
        raise TypeError('lens() takes arguments of type "int" only') 
    
    elif start>=end:
        raise ValueError('range start must be less than end')
    
    elif start<=0:
        raise ValueError('range start must be greater than 0')
    
    #Error Handling to see if step>0
    elif step<=0 or type(step)!=int:
        raise ValueError('step must be an integer greater than 0')
    
    #Calling functions and printing values
    print(f'Collatz Sequences for numbers in range {start} to {end} with step {step} are:')
    print('')
    print(seqbet(start,end,step=step))
    print('')
    print('')
    print(f'Number(s) with the largest peak is/are: {peaks(start,end,step=step)}')
    print(f'Number(s) with the smallest peak is/are: {peaks(start,end,step=step,smallest=True)}')
    print('')
    print('')
    print(f'Number(s) with the largest length is/are: {lens(start,end,step=step)}')
    print(f'Number(s) with the smallest length is/are: {lens(start,end,step=step,smallest=True)}')



    