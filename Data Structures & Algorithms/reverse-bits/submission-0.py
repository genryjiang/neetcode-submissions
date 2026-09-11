class Solution:
    def reverseBits(self, n: int) -> int:
        # get bit rep, strip the 0b from [2:]
        bit = str(bin(n))[2:].zfill(32)
        reversed_bit = bit[::-1]
        return int(reversed_bit,2)