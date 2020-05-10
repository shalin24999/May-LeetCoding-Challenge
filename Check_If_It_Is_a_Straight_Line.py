'''
Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        mx=coordinates[0][0]-coordinates[1][0]
        my=coordinates[0][1]-coordinates[1][1]
        print(mx,my)
        for i in range(len(coordinates)-1):
            if (coordinates[i][1]-coordinates[i+1][1]) * mx != my * (coordinates[i][0]-coordinates[i+1][0]):
                return False
        return True
                
