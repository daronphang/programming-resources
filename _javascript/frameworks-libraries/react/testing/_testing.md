## Tests

### Unittesting

Testing individual building blocks (functions, components) in isolation.

### Integration

Test the combination of multiple building blocks.

### End-to-End

Test a series of steps i.e. logging in and navigating to page.

### Tools

Use Jest for running tests and asserting results, and React Testing Library for simulating/rendering React app/components. Both are setup when using "create-react-app".

Tests are not executed in browser but in Jest environment and hence, do not need to import expect() or describe() as they are already available globally in Jest environment.

https://jestjs.io/docs/expect

https://jestjs.io/docs/mock-function-api

## Testing Philosophy

- Many integration tests, no snapshot tests, few unit tests, few e-to-e tests.
- Write mostly integration and not unit as they don't really resemble the way your end user interacts with the app.
- Do not test implementation details such as name of functions and variables, and whether nested components are rendered, or how many times they are rendered.
- shallow() for unittesting and mount/render() for integration testing.
- Tests should test functionality of app, that mimic how it will be used by end users.
- Leave 3rd party library tests to authors.
- Should not test event handlers like handleClose, onSubmit, change as they can safely be expected to be called; instead, test the after-effect of them being called.
- Functions defined in functional components are closed scope and hence, inaccessible; don't test if the method was called but rather if changes like useState are expected.
- Testing MUI may be difficult as they are React components and cannot be represented by regular html elements.

https://kentcdodds.com/blog/avoid-nesting-when-youre-testing

## Why Testing Implementation Details is Bad

Implementation details are things which users of your code (end users and developers) will not typically use, see or even know about.

1. Can break when you refactor application code. False negatives.
2. May not fail when you break application code. False positives.

Everytime a change is made to the code, the tests break; however, this is because the test is broken, but not the application. This leads to brittle and frustrating tests.

https://kentcdodds.com/blog/testing-implementation-details

```js
import * as React from 'react';
// if you're wondering why not shallow,
// then please read https://kcd.im/shallow
import Enzyme, { mount } from 'enzyme';
import EnzymeAdapter from 'enzyme-adapter-react-16';
import Accordion from '../accordion';

// Setup enzyme's react adapter
Enzyme.configure({ adapter: new EnzymeAdapter() });

// users do not care what state the openIndex is
test('setOpenIndex sets the open index state properly', () => {
  const wrapper = mount(<Accordion items={[]} />);
  expect(wrapper.state('openIndex')).toBe(0);
  wrapper.instance().setOpenIndex(1);
  expect(wrapper.state('openIndex')).toBe(1);
});

test('Accordion renders AccordionContents with the item contents', () => {
  const hats = { title: 'Favorite Hats', contents: 'Fedoras are classy' };
  const footware = {
    title: 'Favorite Footware',
    contents: 'Flipflops are the best',
  };
  const wrapper = mount(<Accordion items={[hats, footware]} />);
  expect(wrapper.find('AccordionContents').props().children).toBe(hats.contents);
});
```

```js
// not testing implementation details
import '@testing-library/jest-dom/extend-expect';
import * as React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Accordion from '../accordion';

test('can open accordion items to see the contents', () => {
  const hats = { title: 'Favorite Hats', contents: 'Fedoras are classy' };
  const footware = {
    title: 'Favorite Footware',
    contents: 'Flipflops are the best',
  };
  render(<Accordion items={[hats, footware]} />);

  expect(screen.getByText(hats.contents)).toBeInTheDocument();
  expect(screen.queryByText(footware.contents)).not.toBeInTheDocument();

  userEvent.click(screen.getByText(footware.title));

  expect(screen.getByText(footware.contents)).toBeInTheDocument();
  expect(screen.queryByText(hats.contents)).not.toBeInTheDocument();
});
```

## Example

Arrange, your app is in a certain original state. Act, then something happens like click event, input, etc. Lastly assert, or make a hypothesis of the new state of your app.

```js
import { render, screen, cleanup } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Greeting from './Greeting';

afterEach(cleanup);

// describe is for testing suite
describe('Greeting component', () => {
  test('some testing', () => {
    render(<Greeting />);
    const helloWorldElement = screen.getByText('Hello world', { exact: false });
    expect(helloWorldElement).not.toBeInTheDocument();
  });

  test('testing user interaction and state', () => {
    render(<Greeting />);
    // userEvent helps to trigger events on screen
    const buttonElement = screen.getByRole('button');
    userEvent.click(buttonElement);

    // getByText will fail if not found, use queryByText instead which returns null
    const output = screen.queryByText('hello');
    expect(output).toBeNull();
  });

  test('async component', async () => {
    // overriding built in fetch()
    window.fetch = jest.fn();
    window.fetch.mockResolvedValueOnce({
      json: async () => ['hello', 'world'],
    });

    render(<Async />);

    // if expect multiple list items, need getAllByRole instead of getByRole
    const listItemElements = await screen.getAllByRole('listitem');
    expect(listItemElements).not.toHaveLength(0);
  });
});
```
