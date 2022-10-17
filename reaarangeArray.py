def moveNegative(self, arr):
 
        last_negative_index = -1
 
        for i in range(len(arr)):
            if arr[i] < 0:
                last_negative_index += 1
                arr[i], arr[last_negative_index] = arr[last_negative_index], arr[i]
 
                
                if i - last_negative_index >= 2:
                    self.rotateSubArray(arr, last_negative_index+1, i)
 
        return arr
