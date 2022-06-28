class Solution:

    def printSequence(self,S):
        # code here
        d = dict()
        d['A'] = '2'
        d['B'] = '22'
        d['C'] = '222'
        d['D'] = '3'
        d['E'] = '33'
        d['F'] = '333'
        d['G'] = '4'
        d['H'] = '44'
        d['I'] = '444'
        d['J'] = '5'
        d['K'] = '55'
        d['L'] = '555'
        d['M'] = '6'
        d['N'] = '66'
        d['O'] = '666'
        d['P'] = '7'
        d['Q'] = '77'
        d['R'] = '777'
        d['S'] = '7777'
        d['T'] = '8'
        d['U'] = '88'
        d['V'] = '888'
        d['W'] = '9'
        d['X'] = '99'
        d['Y'] = '999'
        d['Z'] = '9999'
        d[' '] = '0'
        
        ans = ''
        for item in S:
            ans += d[item]
        return ans