"""
"""
class Solution(object):
    def reconstructQueue(self, people):
        res = []
        #  assuming input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        for k, g in itertools.groupby(sorted(people, key=lambda p: (-p[0], p[1])), key=lambda p: p[0]):
            #debugging
            #print "------------------"
            #print k

            #  list(g) would be in every iteration 
            #    first : [[7,0], [7,1]]
            #    second : [[6,1]]
            #    third : [[5,0],[5,1]]
            #    fourth : [[4,4]]
            for ip in list(g):
                # number of person in front of can be used a index to insert into res
                # first   res = [].insert(0,[7,0])
                # second  res.insert(1,[7,1])
                # third   res.insert(1,[6,1])
                # fourth  res.insert(0,[5,0])
                # fifth   res.insert(1,[5,1])
                # sixth`  res.insert(4,[4,4])
                res.insert(ip[1], ip) 

        return res


"""
Greedy Algorithm.
Try to fulfill each person step by step in the order of ascending k
Failed solution
"""
class Solution_2(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        #return list 
        res = []

        #bubble sort people by k (the # of people taller or equal height) in ascending order
        for i in xrange(0, len(people)-2):
            for j in xrange(0, len(people) - i - 1):
                #compare and swap if the current one is larger than the next one
                #thus sink the largest one to bottom
                cp, np = people[j], people[j+1]

                if cp[1] > np[1]:
                    swap0, swap1 = np[0], np[1]
                    people[j+1][0], people[j+1][1] = people[j][0], people[j][1]
                    people[j][0], people[j][1] = swap0, swap1


        #pick a people with smallest k in the rest persons and insert into right position of desired list 
        for p in people:

            if not res: # if result list is empty, push the first person
                res.append(p)
            else: #find the right positon in result list which doesn't violate any constrains that are already in the list for the current person
                cnt = 0
                for i in xrange(0, len(res)):
                    r = res[i] #current person to be compared in result list

                    if cnt == p[1]:
                        if p[0] < r[0]:
                            res.insert(i, p)
                            break
                        else:
                            continue
                    elif cnt == p[1] and p[0] >= r[0]:
                        continue
                    elif cnt < p[1]:
                        if r[0] >= p[0]:
                            cnt += 1
                        else:
                            continue

                if i == len(res)-1:
                    res.append(p)
        
        return res
