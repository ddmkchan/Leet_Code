#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        _map = {}
        for i in xrange(len(num)):
            if (target - num[i]) in _map:
                return (_map.get((target - num[i])), i+1)
            _map[num[i]] = i+1
        return (-1, -1)


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    print Solution().twoSum(numbers, 9)
