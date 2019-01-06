import sudoku
from tkinter import *
from tkinter import messagebox

class Solver:

    def revise(self,csp, Xi, Xj, removals):
        di = csp.curr_domains[Xi]
        dj =csp.curr_domains[Xj]
        revised = False
        noValueSatisfies = True
        for vi in di:
            for vj in dj:
                if csp.constraints(Xi, vi, Xj, vj):
                    noValueSatisfies = False
            if noValueSatisfies:
                csp.prune(Xi, vi, removals)
                revised = True
            noValueSatisfies = True
        return revised


    def AC3(self, csp, removals=None, queue=None):

        queue = []
        for var in csp.variables:
            for neighboor in csp.neighbors[var]:
                queue.append([var, neighboor])
        while queue:
            xi = queue[0][0]
            xj = queue[0][1]
            del queue[0]

            if self.revise(csp, xi, xj, removals):
                if len(csp.curr_domains[xi]) == 0: return False
                for xk in csp.neighbors[xi]:
                    queue.append([xk, xi])
        return True

    def selectUnassigned(self, csp, assignment):
        for var in csp.variables:
            if var not in assignment: return var


    def backtrack(self, assignment, csp):
        if len(assignment) == 81: return assignment
        var = self.selectUnassigned(csp, assignment)
        for val in csp.curr_domains[var]:
            if csp.nconflicts(var, val, assignment) == 0:
                csp.assign(var, val, assignment)
                rm = csp.suppose(var, val)
                if self.AC3(csp,rm):
                    result = self.backtrack(assignment, csp)
                    if result is not False: return result
                csp.restore(rm)
            csp.unassign(var, assignment)

        return False

    def backtracking_search(self, csp):
        return self.backtrack({}, csp)


if __name__ == '__main__':

    window = Tk()
    window.title("Sudoku Solver")
    window.geometry('270x175')
    window.configure(background="#292930")
    window.resizable(0, 0)
    window.iconbitmap('favicon.ico')

    def solveClicked():
        board = str()
        for entry in range(1,82):
            currentCell = eval("number" + str(entry))
            cell = currentCell.get()
            if cell is "":
                cell = "."
            board = board + str(cell)
        if len(board) != 81:
            messagebox.showerror("Invalid Input", "Make sure each cell only has one number!")
        else:
            myboard = sudoku.Sudoku(board)
            solution = Solver()
            solution.backtracking_search(myboard)
            a = myboard.display(myboard)
            b = str(a)
            final = "0"
            for entry in b:
                if entry.isdigit():
                    final = final + str(entry)

            for entry in range(1, 82):
                currentCell = eval("number" + str(entry))
                currentCell.delete(0, END)
                currentCell.insert(0, final[entry])

    def clearClicked():
        for entry in range(1, 82):
            currentCell = eval("number" + str(entry))
            currentCell.delete(0,END)



    solveButton = Button(window, text="Solve!", width=5, bg="#3EB650", command=solveClicked)
    solveButton.place(x=215, y=50)

    clearButton = Button(window, text="Clear", width=5, bg="#FCC133", command=clearClicked)
    clearButton.place(x=215, y=90)



    number1 = Entry(window, width=3, justify='center')
    number2 = Entry(window, width=3, justify='center')
    number3 = Entry(window, width=3, justify='center')
    number4 = Entry(window, width=3, justify='center')
    number5 = Entry(window, width=3, justify='center')
    number6 = Entry(window, width=3, justify='center')
    number7 = Entry(window, width=3, justify='center')
    number8 = Entry(window, width=3, justify='center')
    number9 = Entry(window, width=3, justify='center')

    number10 = Entry(window, width=3, justify='center')
    number11 = Entry(window, width=3, justify='center')
    number12 = Entry(window, width=3, justify='center')
    number13 = Entry(window, width=3, justify='center')
    number14 = Entry(window, width=3, justify='center')
    number15 = Entry(window, width=3, justify='center')
    number16 = Entry(window, width=3, justify='center')
    number17 = Entry(window, width=3, justify='center')
    number18 = Entry(window, width=3, justify='center')

    number19 = Entry(window, width=3, justify='center')
    number20 = Entry(window, width=3, justify='center')
    number21 = Entry(window, width=3, justify='center')
    number22 = Entry(window, width=3, justify='center')
    number23 = Entry(window, width=3, justify='center')
    number24 = Entry(window, width=3, justify='center')
    number25 = Entry(window, width=3, justify='center')
    number26 = Entry(window, width=3, justify='center')
    number27 = Entry(window, width=3, justify='center')

    number28 = Entry(window, width=3, justify='center')
    number29 = Entry(window, width=3, justify='center')
    number30 = Entry(window, width=3, justify='center')
    number31 = Entry(window, width=3, justify='center')
    number32 = Entry(window, width=3, justify='center')
    number33 = Entry(window, width=3, justify='center')
    number34 = Entry(window, width=3, justify='center')
    number35 = Entry(window, width=3, justify='center')
    number36 = Entry(window, width=3, justify='center')

    number37 = Entry(window, width=3, justify='center')
    number38 = Entry(window, width=3, justify='center')
    number39 = Entry(window, width=3, justify='center')
    number40 = Entry(window, width=3, justify='center')
    number41 = Entry(window, width=3, justify='center')
    number42 = Entry(window, width=3, justify='center')
    number43 = Entry(window, width=3, justify='center')
    number44 = Entry(window, width=3, justify='center')
    number45 = Entry(window, width=3, justify='center')

    number46 = Entry(window, width=3, justify='center')
    number47 = Entry(window, width=3, justify='center')
    number48 = Entry(window, width=3, justify='center')
    number49 = Entry(window, width=3, justify='center')
    number50 = Entry(window, width=3, justify='center')
    number51 = Entry(window, width=3, justify='center')
    number52 = Entry(window, width=3, justify='center')
    number53 = Entry(window, width=3, justify='center')
    number54 = Entry(window, width=3, justify='center')

    number55 = Entry(window, width=3, justify='center')
    number56 = Entry(window, width=3, justify='center')
    number57 = Entry(window, width=3, justify='center')
    number58 = Entry(window, width=3, justify='center')
    number59 = Entry(window, width=3, justify='center')
    number60 = Entry(window, width=3, justify='center')
    number61 = Entry(window, width=3, justify='center')
    number62 = Entry(window, width=3, justify='center')
    number63 = Entry(window, width=3, justify='center')

    number64 = Entry(window, width=3, justify='center')
    number65 = Entry(window, width=3, justify='center')
    number66 = Entry(window, width=3, justify='center')
    number67 = Entry(window, width=3, justify='center')
    number68 = Entry(window, width=3, justify='center')
    number69 = Entry(window, width=3, justify='center')
    number70 = Entry(window, width=3, justify='center')
    number71 = Entry(window, width=3, justify='center')
    number72 = Entry(window, width=3, justify='center')

    number73 = Entry(window, width=3, justify='center')
    number74 = Entry(window, width=3, justify='center')
    number75 = Entry(window, width=3, justify='center')
    number76 = Entry(window, width=3, justify='center')
    number77 = Entry(window, width=3, justify='center')
    number78 = Entry(window, width=3, justify='center')
    number79 = Entry(window, width=3, justify='center')
    number80 = Entry(window, width=3, justify='center')
    number81 = Entry(window, width=3, justify='center')


    number1.grid(row=0,column=1)
    number2.grid(row=0,column=2)
    number3.grid(row=0,column=3, padx=(0,3))
    number4.grid(row=0,column=4)
    number5.grid(row=0,column=5)
    number6.grid(row=0,column=6, padx=(0,3))
    number7.grid(row=0,column=7)
    number8.grid(row=0,column=8)
    number9.grid(row=0,column=9)


    number10.grid(row=1,column=1)
    number11.grid(row=1,column=2)
    number12.grid(row=1,column=3, padx=(0,3))
    number13.grid(row=1,column=4)
    number14.grid(row=1,column=5)
    number15.grid(row=1,column=6, padx=(0,3))
    number16.grid(row=1,column=7)
    number17.grid(row=1,column=8)
    number18.grid(row=1,column=9)

    number19.grid(row=2,column=1, pady=(0,3))
    number20.grid(row=2,column=2, pady=(0,3))
    number21.grid(row=2,column=3, padx=(0,3), pady=(0,3))
    number22.grid(row=2,column=4, pady=(0,3))
    number23.grid(row=2,column=5, pady=(0,3))
    number24.grid(row=2,column=6, padx=(0,3), pady=(0,3))
    number25.grid(row=2,column=7, pady=(0,3))
    number26.grid(row=2,column=8, pady=(0,3))
    number27.grid(row=2,column=9, pady=(0,3))

    number28.grid(row=3,column=1)
    number29.grid(row=3,column=2)
    number30.grid(row=3,column=3, padx=(0,3))
    number31.grid(row=3,column=4)
    number32.grid(row=3,column=5)
    number33.grid(row=3,column=6, padx=(0,3))
    number34.grid(row=3,column=7)
    number35.grid(row=3,column=8)
    number36.grid(row=3,column=9)

    number37.grid(row=4,column=1)
    number38.grid(row=4,column=2)
    number39.grid(row=4,column=3, padx=(0,3))
    number40.grid(row=4,column=4)
    number41.grid(row=4,column=5)
    number42.grid(row=4,column=6, padx=(0,3))
    number43.grid(row=4,column=7)
    number44.grid(row=4,column=8)
    number45.grid(row=4,column=9)

    number46.grid(row=5,column=1, pady=(0,3))
    number47.grid(row=5,column=2, pady=(0,3))
    number48.grid(row=5,column=3, padx=(0,3), pady=(0,3))
    number49.grid(row=5,column=4, pady=(0,3))
    number50.grid(row=5,column=5, pady=(0,3))
    number51.grid(row=5,column=6, padx=(0,3), pady=(0,3))
    number52.grid(row=5,column=7, pady=(0,3))
    number53.grid(row=5,column=8, pady=(0,3))
    number54.grid(row=5,column=9, pady=(0,3))

    number55.grid(row=6,column=1)
    number56.grid(row=6,column=2)
    number57.grid(row=6,column=3, padx=(0,3))
    number58.grid(row=6,column=4)
    number59.grid(row=6,column=5)
    number60.grid(row=6,column=6, padx=(0,3))
    number61.grid(row=6,column=7)
    number62.grid(row=6,column=8)
    number63.grid(row=6,column=9)

    number64.grid(row=7,column=1)
    number65.grid(row=7,column=2)
    number66.grid(row=7,column=3, padx=(0,3))
    number67.grid(row=7,column=4)
    number68.grid(row=7,column=5)
    number69.grid(row=7,column=6, padx=(0,3))
    number70.grid(row=7,column=7)
    number71.grid(row=7,column=8)
    number72.grid(row=7,column=9)

    number73.grid(row=8,column=1)
    number74.grid(row=8,column=2)
    number75.grid(row=8,column=3, padx=(0,3))
    number76.grid(row=8,column=4)
    number77.grid(row=8,column=5)
    number78.grid(row=8,column=6, padx=(0,3))
    number79.grid(row=8,column=7)
    number80.grid(row=8,column=8)
    number81.grid(row=8,column=9)


    window.mainloop()
