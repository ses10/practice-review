#In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
#different sizes which can slide onto any tower. The puzzle starts with disks sorted
#in ascending order of size from top to bottom (i.e., each disk sits on top of an even
#larger one). You have the following constraints:
#
#(T) Only one disk can be moved at a time.
#(2) A disk is slid off the top of one tower onto the next rod.
#(3) A disk can only be placed on top of a larger disk.
#
#Write a program to move the disks from the first tower to the last using Stacks.

### Solution
#Ex: We have at stack of 3 disks at A(origin), and want to move them all to C(dest)
#
#	1
#	2
#	3
#	A  B  C
#
# Solving this problem would just be to move the bottom disk to C and then the 
#	rest of the stack to C, however first we need to move the top n-1 disks to the buffer
#
#	   1
#	3  2
#	A  B  C
#
# Now we can move 3 over to C
#
#	   1
#	   2  3
#	A  B  C
#
# Finally for the rest of the disks at B we move them over to C using the same
# process but with B as origin, C as dest, and A as the buffer
#
#		  1	
#		  2
#         3
#	A  B  C


#given the number of disks to move & 3 stacks
#moves the top n disk of origin stack to dest stack 
#using buffer stack as buffer
def moveDisks(num, origin, dest, buffr):
	if num == 0:
		return

	#move the top n-1 disks to buffer using destination as buffer
	moveDisks(num-1, origin, buffr, dest)

	#move top disk to destination
	moveTop(origin, dest)

	#move the n-1 disk from buffer to destination using origin as buffer
	moveDisks(num-1, buffr, dest, origin)

#given origin and destination, moves top disk from origin to destination
#only if disk is less than the disk on top of dest stack
def moveTop(origin, dest):
	top = 0

	if len(dest) == 0:
		disk = origin.pop(top)
		dest.insert(top, disk)		

	elif origin[top] > dest[top]:
		print("Error moving stacks")

	else:
		disk = origin.pop(top)
		dest.insert(top, disk)

#the stacks are implemented with dynamic arrays with
#the first element representing the top of stack
def main():
	
	#the towers
	towers = []
	for i in range(3):
		towers.append([])

	#adding the disks
	for i in range(3):
		towers[0].append(i+1)

	print(towers)

	moveDisks(len(towers[0]), towers[0], towers[2], towers[1])

	print(towers)

main()
