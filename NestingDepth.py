output=""
T = int(raw_input())
for i in range(T):
    t = str(raw_input())
    output += "Case #"+str(i+1)+": "
    openBrackets = 0
    for d in t:
        d = int(d)
        if d>openBrackets:
            for bracket in range(d- openBrackets):
                output += "("
                openBrackets+=1
        elif d<openBrackets:
            for bracket in range(openBrackets- d):
                output += ")"
                openBrackets-=1
        output += str(d);
    for bracket in range(openBrackets):
        output += ")"
        openBrackets-=1
    
    print(output)
    output = ""