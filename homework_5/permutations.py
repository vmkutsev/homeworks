from tracer import trace
import pytest

def permutos(nums):
    @trace
    def shift(nightguy):
        if nightguy == len(nums):
            result.append(nums[:])
            return nums[:]

        for i in range(nightguy, len(nums)):
            nums[i], nums[nightguy] = nums[nightguy], nums[i]
            shift(nightguy + 1)
            nums[i], nums[nightguy] = nums[nightguy], nums[i]

    result = []
    shift(0)
    return result

def test_permutos():
    assert(sorted(permutos([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]))
    assert sorted(permutos([0, 1])) == sorted([[0, 1], [1, 0]])
    assert permutos([0]) == [[0]]
    assert permutos([]) == [[]]