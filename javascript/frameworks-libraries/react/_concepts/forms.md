## Uncontrolled

In browser, forms maintain their own internal state. For uncontrolled, DOM manages and stores data and input is pulled from it through refs.

```js
return <input type="text" name="name" ref={this.nameInput} />;
```

## Controlled

It is convenient to have a JS function that handles the submission of the form and has access to the data that the user has entered. The standard way to achieve this is with a technique called "controlled components".

In HTML, form elements like <input> maintain their own state, while React updates with setState(). Can combine the both by making React state the "single source of truth" i.e. input form element value is controlled by React.

State is stored in the component that renders the input. Each input field accepts its current value as a prop and has callback function which is called when the state of input changes.

```javascript
const SimpleInput = (props) => {
  const [enteredName, setEnteredName] = useState('');
  const [inputValid, setInputValid] = useState(false);
  const [inputTouched, setInputTouched] = useState(false);
  const nameInputRef = useRef();

  const nameInputChangeHandler = event => {
    setEnteredName(event.target.value)
  }

  const nameInputBlurHandler = event => {
    setInputTouched(true);

    if (enteredName.trim() === '') {
      setInputValid(false);
      return;
    }
  }


  const formSubmissionHandler = event => {
    event.preventDefault();

    if (enteredName.trim() === '') {
      setInputValid(false);
      return;
    }

    setInputValid(true);

    setEnteredName('');
    // shouldnt use nameInputRef.current.value = '' as it directly manipulates to DOM, leave it to React
  }

  return (
    <form onSubmit={formSubmissionHandler}>
      <div class="form-control">
        <label>Your name</label>
        <input
          ref={nameInputRef}    // pointer to ref property
          type='text'
          id='name'
          value={enteredName}
          onChange={nameInputChangeHandler}
          onBlur={nameInputBlurHandler}
          />
          {!inputValid && inputTouched <p>Name must not be empty</p>}
      </div>
      <button>Submit</button>
    </form?
  )
}
```

### Form Reset

If uncontrolled, can use event.target.reset(). Else, need to setState.

```html
<form onSubmit="{handleSearch}">
  <StyledInputBase placeholder="Search something…" onChange={handleOnChange} value={searchValue} inputProps={{
  "aria-label": "search" }} />
</form>
```

## React-Hook-Form

Provides most of the abstraction with form validation, and embraces uncontrolled components and native inputs. When working with external controlled components, can use "Controller" wrapper to work with forms.

https://github.com/react-hook-form/react-hook-form/tree/master/examples

### Uncontrolled

Need register component's ref.

```js
// register API

const { onChange, onBlur, name, ref } = register('firstName');
// include type check against field path with the name you have supplied.

<input
  onChange={onChange} // assign onChange event
  onBlur={onBlur} // assign onBlur event
  name={name} // assign name prop
  ref={ref} // assign ref prop
/>
// same as above
<input {...register('firstName')} />
```

```js
import React from 'react';
import { useForm } from 'react-hook-form';

export default function App() {
  const { register, handleSubmit } = useForm();
  const onSubmit = (data) => console.log(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('firstName')} />
      <select {...register('gender')}>
        <option value="female">female</option>
        <option value="male">male</option>
        <option value="other">other</option>
      </select>
      <input type="submit" />
    </form>
  );
}
```

### Controlled

```js
import React from "react";
import TextField from "@material-ui/core/TextField";
import { useForm, Controller } from "react-hook-form";

const InputObjects = [
  {
    type: "username",
    placeholder: "Enter Username",
    errorMsg: "Please enter a username (5 characters or more).",
  },
  {
    type: "password",
    placeholder: "Enter Password",
    errorMsg: "Please enter a password (5 characters or more).",
  },
];

export default function LoginModal() {
  const {
    handleSubmit,
    control,
    formState: { errors },
  } = useForm({ mode: "onBlur" });

  const handleFinalSubmit = (data) => {
    console.log(data);
  };

  const renderInputFields = InputObjects.map((obj) => (
    <InputField>
      <Controller
        name={obj.type}
        control={control}
        defaultValue=""
        rules={{ required: true, minLength: 5 }}
        render={({ field }) => (
          <TextField
            {...field}
            error={errors[obj.type]}
            helperText={errors[obj.type] ? obj.errorMsg : null}
            style={InputFieldStyle}
            type="text"
            placeholder={obj.placeholder}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  {obj.type === "username" && <AccountCircle />}
                  {obj.type === "password" && <LockIcon />}
                </InputAdornment>
              ),
            }}
          />
        )}
      />
    </InputField>
  ));

  return (
    {renderInputFields}
  )

```
