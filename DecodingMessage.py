# Daily Coding Problem [Medium]
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
# count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.


def decoding_message(s):
    mapping = {'1':'a', '2':'b', '3':'c','4':'d','5':'e','6':'f',
                '7':'g','8':'h','9':'i','10':'j','11':'k','12':'l',
                '13':'m','14':'n','15':'o','16':'p','17':'q','18':'r',
                '19':'s','20':'t','21':'u','22':'v','23':'w','24':'x',
                '25':'y','26':'z'}
    count = 0
    len_str = len(s)
    
    # Dynamic programming
    dp = [0 for i in range(len_str)]
    if s[0]!='0':
        dp[0]=1
    for i in range(1,len_str):
        x = int(s[i])
        y = int(s[i-1:i+1])
        if x>=1 and x<=9:
            dp[i]+=dp[i-1]
        if y>=10 and y<=26:
            if i-2>=0:
                dp[i]+=dp[i-2]
            else:
                dp[i]+=1
    return dp[-1]


if __name__ == "__main__":
    s = '12314'
    result = decoding_message(s)
    print(result)


# Example
# input = '111'
# 'aaa', 'ka', 'ak'
# return 3

# input = '21'
# 'ba', 'u'
# return 2

# input = '226'
# 'bz', 'vf', 'bbf'
# return 3

# input = '06'
# return 0


# Time complexity
# O(n)