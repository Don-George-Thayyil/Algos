from the_array import TheArray

class array2d:

    def __init__(self,row_num,col_num):
        self.row_num = TheArray(row_num)
        for i in range(row_num):
            self.row_num[i] = TheArray(col_num)
    
    def num_of_rows(self):
        return len(self.row_num)

    def num_of_columns(self):
        return len(self.row_num[0])

    def clear(self,value):
        for row in range(self.row_num):
            row.clear(value)

    def _getitem(self,tuple_index):
        assert len(tuple_index) == 2, "Subscript out of range"
        row_index = tuple_index[0]
        col_index = tuple_index[1]
        assert row_index >=0 and row_index < self.num_of_rows() and col_index >= 0 and col_index < self.num_of_columns(), "Array subscript out of range"
        row = self.row_num[row_index]
        item = row[col_index]
        return item

    def _setitem(self,tuple_index,value):
        assert len(tuple_index) == 2,"Array subscript out of range"
        row_index = tuple_index[0]
        col_index = tuple_index[1]
        assert row_index >=0 and row_index < self.num_of_rows() and col_index >= 0 and col_index < self.num_of_columns(), "Array subscript of out of range"
        row = self.row_num[row_index]
        row[col_index] = value

