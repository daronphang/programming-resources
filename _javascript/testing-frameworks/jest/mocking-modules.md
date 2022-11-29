## Mocking Modules

### Example

```js
import { useSnackbar } from 'notistack';
```

```js
jest.mock('notistack', () => ({
  useSnackbar: () => {
    return {
      enqueueSnackbar: jest.fn((type, obj) => {}),
    };
  },
}));
```

### React Portals

Create actual instance of portal itself.

```js
const modalRoot = document.createElement('div');
modalRoot.setAttribute('id', 'modal-root');
document.body.appendChild(modalRoot);

const Modal = ({ children }) => {
  const el = document.createElement('div');

  useEffect(() => {
    modalRoot.appendChild(el);
    return () => modalRoot.removeChild(el);
  });

  return ReactDOM.createPortal(
    <div>
      <div onClick={(e) => e.stopPropagation()}>{children}</div>
    </div>,
    el
  );
};

const renderModal = (handleCloseModal) => {
  render(<Modal children={<GenericModal handleCloseModal={handleCloseModal} ChildModal={LoginModal} />} />);
};
```

## Bypassing Module Mocks

Sometimes may want to use parts of a mocked module i.e. accessing the original implementation.

```js
import fetch from 'node-fetch';

export const createUser = async () => {
  const response = await fetch('http://website.com/users', { method: 'POST' });
  const userId = await response.text();
  return userId;
};
```

```js
// alternative for bypassing module mocks
// jest.mock('node-fetch');
// import fetch from 'node-fetch';
// const {Response} = jest.requireActual('node-fetch');

jest.mock('node-fetch', () => {
  const { Response } = jest.requireActual('node-fetch');
  return {
    __esModule: true,
    Response,
    fetch: () => jest.fn(),
  };
});

import fetch, { Response } from 'node-fetch';
import { createUser } from './createUser';

test('createUser calls fetch with the right args and returns the user id', async () => {
  fetch.mockReturnValue(Promise.resolve(new Response('4')));

  const userId = await createUser();

  expect(fetch).toHaveBeenCalledTimes(1);
  expect(fetch).toHaveBeenCalledWith('http://website.com/users', {
    method: 'POST',
  });
  expect(userId).toBe('4');
});
```

## Redux Store

When mocking components, use real store so that you can test actions and reducers. If the actions are mocked without reducers, it may result in false positive.

```js
// uses references to actual reducers
export function createTestStore() {
  const store = createStore(
    combineReducers({
      user: userReducer,
      config: configReducer,
    })
  );
  return store;
}
```

```js
let store;
describe('Your test', () => {
  beforeEach(() => {
    store = createTestStore();
  });
  test('Your component with a full reducer flow', async () => {
    // Create a redux store
    const { findByText } = render(
      <Provider store={store}>
        <YourComponentToTest />
      </Provider>
    );
    await findByText('This text is now visible because your state was updated by the reducer');
  });
});
```

## Mock Implementation

```js
jest.mock('./components/navbar/navbar', () => ({
  __esModule: true,
  default: () => {
    return <div>NavigationBarMock</div>;
  },
}));
```
