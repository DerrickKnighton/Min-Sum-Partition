# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:09:14 2019

@author: Derrick

Found this problem online for interview prep and it didnt
seem too bad so i gave it a try didnt take super long

"""




class Min_Sum_Partition():
    
    import numpy as np
    
    def create_Random_Array(self,range_Of_Ints,size_Of_Arr):
        #creates random array 
        #range_Of_Ints is [0,num you chose) 
        arr = np.random.randint(range_Of_Ints, size=size_Of_Arr)
        return arr
    
    def Partition(self,arr):
        #split array into 2 sub arrays such that the summation of he 2 is minimized
        #Algo idea find max in array put in one of the subarrays
        #then remove max find new max and put that in other subarray
        #continue until arr is size 0
        
        sub_arr_one = np.ndarray([0])
        sub_arr_two = np.ndarray([0])
        
        
        #this algo works with only posiive numbers to init max to negative
        max = -1000
        num_to_add = -1000
        
        #bool to flip flop between sub_arr_one and two
        add_to_arr = True
        
        while max != 0:
            
            max = np.argmax(arr)
            
            #####################################################
            #if statements take max in arr add to one sub_arr delete the max element in
            #arr and change the bool so next max is added to other sub arr
            #let it be known it is completely unesscessary to add these vals to arrays
            #this could be accomplished more efficiently by just summing the values
            #immediately and that would take up less space i just wanted to
            #do it his way
            if add_to_arr == True:
                num_to_add = arr[max] 
                sub_arr_one = np.append(sub_arr_one,[num_to_add])
                add_to_arr = False
                arr[max] = 0
                
            elif add_to_arr == False:
                num_to_add = arr[max]
                sub_arr_two = np.append(sub_arr_two,[num_to_add])
                add_to_arr = True
                arr[max] = 0
            #####################################################
        return sub_arr_one, sub_arr_two   
    
    def Min_Sum(self,sub_arr_one, sub_arr_two):
        
        ##########################################################
        #sum sub arrs and take difference
        sum1 = np.sum(sub_arr_one)
        sum2 = np.sum(sub_arr_two)
        
        
        final_Answer = np.abs(sum1 - sum2)
        
        ##########################################################
        return(final_Answer)
    

if __name__ == "__main__":
    run = Min_Sum_Partition()
    arr = run.create_Random_Array(100,100)
    sub_arr_one, sub_arr_two = run.Partition(arr)
    print(run.Min_Sum(sub_arr_one,sub_arr_two))
    
    
    
    
    