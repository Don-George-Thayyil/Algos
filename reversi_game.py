from 2Darray import array2d

class ReversiGame:
    
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self._grid = array2d(self.row,self.column)
        self._grid.clear(0)

    def get_p1_points(self):
        self.count1 = 0
        for row in self._grid.row_num:
            for item in row:
                if row == 1:
                    self.count1 += 1
        return self.count1

     def get_p2_points(self):
        self.count2 = 0
        for row in self._grid.row_num:
            for item in row:
                if row == 2:
                    self.count2 += 1
        return self.count2
    
    def is_legal(self,tuple_index):
        assert len(tuple_index) ==2, "Array subscript out of range (is legal)"
        value =self._grid._getitem(tuple_index)
        if value != 0:
            return False
        else:
            return True

    def the_logic(self,tuple_index):
        assert len(tuple_index) == 2, "Array subscript out of range (the logic)" 
        row = tuple_index[0]
        col = tuple_index[1]
        chance = self.chance()
        assert row >= 0 and row < self.grid.num_of_rows() and col >= 0 and col < self.grid.num_of_columns(),"Array subscript out of range (the logic 2)"
        for i in range(self.grid.num_of_rows()):
            for k in range(self.grid.num_of_columns()):
                if self.grid[row + i for i in range(i)] == chance and self.grid[row - i for i in range(i)] == chance or self.grid[col + i for i in range(i)] == chance and self.grid[col - i for i in range(i)] == chance:
                    
