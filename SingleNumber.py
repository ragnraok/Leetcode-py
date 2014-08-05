class Solution(object):
    #def singleNumber(self, A):
    #    result = None
    #    A.sort()
    #    for index in xrange(0, len(A) - 1, 2):
    #        curr_element = A[index]
    #        next_element = A[index + 1]
    #        if curr_element != next_element:
    #            result = curr_element
    #            break
    #    if result == None:
    #        result = A[len(A) - 1]

    #    return result

    def singleNumber(self, A):
        reuslt = None
        for i in A:
            result ^= i

        return result



if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1, 1, 2, 2, 4, 5, 5])
