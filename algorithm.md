# Algorithm Document

purpose: get the area of the room  
name: floor size   
parameter: room number  
return: calculated area  
algorithm:
1. ask user the width of the room
2. while width is not digit
   3. output invalid input
   4. prompt user to enter width
2. ask user the length of the room
2. while length is not digit
   3. output invalid input
   4. prompt user to enter length
2. calculate area = length * width

purpose: find out type of flooring  
name: floor style
parameter: room number  
return: floor type  
algorithm:
1. ask user what floor type
2. while floor type not 'hardwood', 'carpet', or 'tile':
   3. output invalid floor type
   4. ask user to input floor type
3. return floor type 

purpose: calculate cost per room  
name: room cost  
parameter: floor type, area   
return: cost per room  
algorithm:  
1. set hardwood cost to 1.39
2. set carpet cost to 3.99
3. set tile cost to 4.99
4. if floor type is hardwood:
   1. room cost hardwood = area * hardwood cost 
5. otherwise if floor type is carpet:
   1. room cost carpet = area * carpet cost
6. otherwise if floor type is tile:
   1. room cost tile = area * tile cost

purpose: 
name: main
parameter:  
return: 
1. set count to 0
2. while count is less than or equal to 5:
   3. 