## Router

Use MemoryRouter as the source of truth for React Router's tests. It stores its locations internally in an array and is not tied to an external source, like the history stack in a browser. Hence, this makes it ideal for testing scenarios.

```js
jest.mock('./components/navbar/navbar', () => ({
  __esModule: true,
  default: () => {
    return <div>NavigationBarMock</div>;
  },
}));

it('should show navbar', () => {
  const { getByText } = render(
    <MemoryRouter>
      <App />
    </MemoryRouter>
  );
  expect(getByText(/NavigationBarMock/i)).toBeTruthy();
});
```

```js
import * as React from 'react';
import { create } from 'react-test-renderer';
import { MemoryRouter, Routes, Route } from 'react-router-dom';

describe('My app', () => {
  it('renders correctly', () => {
    let renderer = create(
      <MemoryRouter initialEntries={['/users/mjackson']}>
        <Routes>
          <Route path="users" element={<Users />}>
            <Route path=":id" element={<UserProfile />} />
          </Route>
        </Routes>
      </MemoryRouter>
    );

    expect(renderer.toJSON()).toMatchSnapshot();
  });
});
```
