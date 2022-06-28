'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        gas = list()
        cost = list()
        for item in lis:
            gas.append(item[0])
            cost.append(item[1])
        if sum(gas) - sum(cost) < 0:
            # this means we do not have solution
            return -1
        gas_tank,start = 0,0
        for i in range(n):
            gas_tank += gas[i] - cost[i]
            if gas_tank < 0:
                # this means that solution does not exist till i
                # will definitely exist between i+1 and n-1
                start = i+1
                gas_tank = 0
        return start

Solution().tour(
    [
        [4,6],[6,9],[20,3],[4,5]
    ],4
    )