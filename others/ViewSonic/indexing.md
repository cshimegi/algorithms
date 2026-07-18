# TableA
| a   | b   | c   |
|-----|-----|-----|
| 1   | 1   | 999 |
| 2   | 2   | 999 |
| 3   | 3   | 998 |
| ... | ... | ... |
| 999 | 999 | 1   |

a, b, c are all integers satisfying 1 <= a, b, c <= 999
TableA includes all combinations of (a,b,c).

# Q1
If we have a SQL frequently used, how will you make the indices?
```sql
select * from TableA where a = ? and b = ? and c = ?
```

# Q2
If we have a SQL frequently used, how will you make the indices?
```sql
select * from TableA where a > ? and b > ? and c = ?
```
