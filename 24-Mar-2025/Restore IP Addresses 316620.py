# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_ip = []
        answer = []
        def backtrack(start):
            if len(valid_ip) == 4 and start == len(s):
                answer.append(".".join(valid_ip))
                return
            
            if start >= len(s) or len(valid_ip) == 4:
                return

            for i in range(start+1, start + 4):
                num = s[start:i]
                # print(num, valid_ip)
                if int(num) > 255 or len(str(int(num))) != len(num):
                    break
                valid_ip.append(num)
                backtrack(i)
                valid_ip.pop()
        backtrack(0)
        return answer