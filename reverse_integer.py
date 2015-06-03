#!/usr/bin/env python
#encoding : utf-8

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        b = x>0
        x = x if b else x * -1
        _list = list(str(x))
        for i in xrange(len(_list)/2):
            temp = _list[i]
            _list[i] = _list[len(_list)-1-i]
            _list[len(_list)-1-i] = temp
        out = "".join(_list)
        out = int(out) if b else int(out) * -1
        return out if out>=-2**31 and out <= 2**31-1 else 0


if __name__ == '__main__':
    print Solution().reverse(-2147483648)
    #print Solution().reverse(1534236469)
    
