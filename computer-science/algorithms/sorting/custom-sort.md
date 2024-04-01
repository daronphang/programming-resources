## Custom sort strategy

- When you add a new row at the end, assign its order of the previous row + N, where N is fixed value e.g. 10,000
- When you insert a row between two rows, assign the average of the order of those two rows i.e. split the gap evenly
- Have a housekeeping procedure that restores a gap of N, which can be run periodically or during 'emergency' when the gap between two rows is 1
- Insertion that you can perform without reordering is log2(N)
