import curses
import sys
import argparse
import words_parser
import graph_funcs

def main(stdscr):
    stdscr.clear()

    for i in range(0, 15):
        curses.init_pair(i+1, i, 0)

    curses.init_pair(17, 0, 1)

    field = words_parser.loadFile(args.file)
    size = words_parser.fieldSize(field)

    if args.test:
        r, i, j, k = words_parser.testField(field)
        if r == True:
            stdscr.addstr(0, 0, "Field test success")
            stdscr.refresh()
            stdscr.getkey()
            return

        error = {"row": i, "col": j, "type": k}
        graph_funcs.printGameField(field, stdscr, error)
    else:
        graph_funcs.printGameField(field, stdscr, None)

        openWordCount = 0
        stdscr.addstr(0, size * 2 + 8, "Your words:", curses.color_pair(16))
        while True:
            curses.echo()
            stdscr.addstr(openWordCount + 1, size * 2 + 8, str(openWordCount + 1) + ":                                                                ", curses.color_pair(15))
            w = stdscr.getstr(openWordCount + 1, size * 2 + 11).decode('utf-8')
            hasHidden = False
            for s in field:
                if s["hidden"] == True:
                    if s["word"].casefold() == w.casefold():
                        stdscr.addstr(openWordCount + 1, size * 2 + 11, s["word"], curses.color_pair(1+s["color"]))
                        openWordCount = openWordCount + 1
                        s["hidden"] = False
                        graph_funcs.printGameField(field, stdscr, None)
                        if hasHidden == True:
                            break
                    else:
                        hasHidden = True

            if not hasHidden:
                break


    stdscr.refresh()
    stdscr.getkey()



argParser = argparse.ArgumentParser(description='Welcome to the Game "Filwords"!')
argParser.add_argument("-t", "--test", required=False, action="store_true", help="only test game file")
argParser.add_argument("file", help="name of file where the game defined")
args = argParser.parse_args()


    
# print()

curses.wrapper(main)
