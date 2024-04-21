import curses

def printGameField(field, scr, error=None):
    for w in field:
        for i in range(0, len(w["word"])):
            p = w["pos"][i]
            if error == None:
                if w["hidden"] == True:
                    color = curses.color_pair(16)
                else:
                    color = curses.color_pair(1+w["color"])
                scr.addstr(p["row"], 2*p["col"], w["word"][i:i+1], color)
            else:
                if p["row"] == error["row"] and p["col"] == error["col"]:
                    scr.addstr(p["row"], 2*p["col"], w["word"][i:i+1], curses.color_pair(17))
                else:
                    scr.addstr(p["row"], 2*p["col"], w["word"][i:i+1], curses.color_pair(1+w["color"]))

