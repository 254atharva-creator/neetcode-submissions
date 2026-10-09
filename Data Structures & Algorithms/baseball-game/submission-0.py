class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = []

        for i in range(len(ops)):
            if ops[i] == "+":
                t1 = stk.pop()
                t2 = stk[-1]
                stk.append(t1)
                stk.append(t1 + t2)

            elif ops[i] == "D":
                stk.append(stk[-1] * 2)

            elif ops[i] == "C":
                stk.pop()

            else:
                stk.append(int(ops[i]))

        res = 0
        for i in range(len(stk)):
            res += stk.pop()

        return res