##Input array with n elements. Array is sorted. Remove all duplicate elements from the array. 
# Return int k such that k is the total number of unique elements in the array


#key logic - array is sorted. use del list to delete items in array
def removeDuplicates(nums):
    #1 1 2 3 3 4
    # loop thru array if u find a number add it to unique count once and continue
    # until u find a number different from previous number 
    # move till the end and return count value
    
    index = 0
    for i in range (1, len(nums)):
        #print(index,i, nums[index] , nums[i],  nums)
        if (nums[index] != nums[i]):
            #print('not same')
            index += 1
            nums[index] = nums[i]
        # else:
            #print('same')
    print(nums)
    nums = list(nums[0:index+1])
    print(nums[0:index+1])
    print(index+1)
    return index+1


                 
    # current_item = 0
    # i = 0
    # while True:
    #     if i < len(nums):
    #         if (i == 0 or nums[i] != current_item):
    #             current_item = nums[i]
    #             i+= 1
    #         else:
    #             del nums[i] 
            
    #     else:
    #         break   
            
    return len(nums)

if __name__ == '__main__':
    arr = [1 , 1, 2, 3, 3, 4, 5, 5 ]
    print('before ', arr)
    removeDuplicates(arr)
    print('after ', arr)
