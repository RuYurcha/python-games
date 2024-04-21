
def loadFile(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    result = []
    for s in lines:
        line = s.strip()
        if line == "":
            continue

        i = line.find(" ")
        if i < 0:
            continue 

        w = line[:i].strip().upper()
        q = line[i+1:].strip()
        
        j = q.find(" ")
        if j < 0:
            continue

        c = q[:j].strip() 

        p = q[j+1:].strip()

        wordObject = {}
        wordObject["word"] = w
        wordObject["pos"] = []
        wordObject["color"] = int(c, 16)
        wordObject["hidden"] = True
        for xy in p.split(" "):
            sPos = xy.split(",")
            posObject = {}
            posObject["row"] = int(sPos[0])
            posObject["col"] = int(sPos[1])
            wordObject["pos"].append(posObject)

        result.append(wordObject)

    return result


def fieldSize(field):
    n=0
    for w in field:
        for p in w["pos"]:
            if p["row"] > n:
                n = p["row"]
            if p["col"] > n:
                n = p["col"]
    return n+1

def testField(field):
    matrix = []
    size = fieldSize(field)
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matrix.append(row)

    for w in field:
        for i in range(0, len(w["word"])):
            p = w["pos"][i]
            matrix[p["row"]][p["col"]] += 1

    for i in range(size):
        for j in range(size):
            if matrix[i][j] > 1:
                return False, i, j, 2
            if matrix[i][j] == 0:
                return False, i, j, 0
            
    return True, 0, 0, 0


