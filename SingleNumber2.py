class Solution:
    def singleNumber(self, A):
        #result = None
        #A.sort()
        #for index in xrange(0, len(A) - 1, 3):
        #    curr_element = A[index]
        #    next_element = A[index + 1]
        #    if curr_element != next_element:
        #        result = curr_element
        #        break
        #if result == None:
        #    result = A[len(A) - 1]

        #return result
        ones, twos, threes = (0, 0, 0)
        for i in A:
            twos |= ones & i
            ones ^= i
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes

        return ones

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1, 1, 1, 2, 2, 2, 4, 5, 5, 5])
