
#defining a matrix
class matrix(list):
    def __init__(self, cols, rows, fill=None):
        list.__init__(self, range(rows))
        self.rows, self.cols = rows, cols
        for columns in range(rows):
            self[columns] = list([fill for x in range(cols)])
    def __dim__(self):
        return [self.cols, self.rows]

    def __RowsCols__(self):
        return list(zip(*self))

# functions that are applied to a matrix
def rowsCols(matrix):
    return matrix.__RowsCols__()
def dim(matrix):
    try:
        return matrix.__dim__()
    except AttributeError:
        raise TypeError(" object of "+type(matrix)+" has no dim()")
