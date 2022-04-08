---
title: MockServiceWorker
tags:
- javscript
- testing
- tools
---
MockServiceWorker (MSW) is a Javascript tool that uses a service worker to mock HTTP requests.

[Webpage](https://mswjs.io/)

## How to use it for different tests
You can just define different handlers (responses generators) and add them to the appropriate test cases. Since the handlers are just code, you're free to have them internally share pieces, as long as they generate different responses.

[Source](https://www.wwt.com/article/using-mock-service-worker-to-improve-jest-unit-tests)

```javascript
// TaskList.test.js with MSW

import { render, screen } from '@testing-library/react';
import { tasksHandlerException } from './api-mocks/handlers';
import { mswServer } from './api-mocks/msw-server';
import TaskList from './TaskList';

describe('Component: TaskList', () => {
  it('displays returned tasks on successful fetch', async () => {
    render(<TaskList />);

    const displayedTasks = await screen.findAllByTestId(/task-id-\d+/);
    expect(displayedTasks).toHaveLength(2);
    expect(screen.getByText('Task Zero')).toBeInTheDocument();
    expect(screen.getByText('Task One')).toBeInTheDocument();
  });

  it('displays error message when fetching tasks raises error', async () => {
    mswServer.use(tasksHandlerException);
    render(<TaskList />);

    const errorDisplay = await screen.findByText('Failed to fetch tasks');
    expect(errorDisplay).toBeInTheDocument();

    const displayedTasks = screen.queryAllByTestId(/task-id-\d+/);
    expect(displayedTasks).toEqual([]);
  });
});
```