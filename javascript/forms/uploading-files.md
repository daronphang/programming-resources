## Uploading Files

Requires sending data as FormData, which is the equivalent of HTML form sent as multipart/form-data encoding.

```js
const formData = new FormData();
formData.append("key", "value of type string or blob");
httpClient.post(uri, formData).subscribe();
```

### Converting Objects to Files

Need to stringify into JSON and pack it into a Blob of mimetype JSON.

```js
const formData = new FormData();
const payload = { hello: "world!" };
formData.append("json", new Blob([JSON.stringify([payload])], { type: "application/json" }));
```
