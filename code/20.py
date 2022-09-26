

def valid(str):

    instr = list(str)
    instr.reverse()
    tmp = []
    
    leftk = ["(","[","{"]
    for i in range(len(instr)):
        tmpin = instr.pop()
        if(tmpin in leftk):
            tmp.append(tmpin)
        else:
            if(len(tmp)==0):
                return False
            else:
                tmpout = tmp.pop()
                if(tmpout=="(" and tmpin==")"):
                    continue
                elif(tmpout=="[" and tmpin=="]"):
                    continue
                elif(tmpout=="{" and tmpin=="}"):
                    continue
                else:
                    return False
    return len(tmp)==0



    # tmp.append(instr.pop())
    # while(len(instr)!=0):
    #     if(len(tmp)==0):
    #         return False
    #     else:

    #         tmpin = instr.pop()
    #         tmpout = tmp.pop()

    #         if(tmpout=="(" and tmpin==")"):
    #             continue
    #         elif(tmpout=="[" and tmpin=="]"):
    #             continue
    #         elif(tmpout=="{" and tmpin=="}"):
    #             continue
    #         else:
    #             tmp.append(tmpout)
    #             tmp.append(tmpin)
    # return len(tmp)==0


s = "["
print(valid(s))