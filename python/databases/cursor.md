## Pandas

```py
cursor.execute(s)
df = pd.DataFrame()
while True:
    rows = cursor.fetchmany(10000) # Fetch 10k rows at a time
    if not rows:
        break
    _df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])
    df = pd.concat([df, _df])  # concat to primary dataframe
```


## In-Built Functions

```py
cursor.execute(s)
columns = [col[0] for col in cursor.description]
results = []
for row in cursor.fetchall():
    results.append(dict(zip(columns,row)))
return results
```
