# Exception handling in Python (Demos)

This repo does not contain a project. Rather it contains ideas for demonstrating exception handling.

These demos intend to demonstration will include:

* Handling an inspecific exception
* Handling built-in exceptions
* Handling multiple exceptions
* Getting more information from an Exception
* Raising exceptions
* The `finally` block
* Creating custom exceptions

## What is an exception

Exceptions are a means that Python uses to signal extraordinary events, typically errors.

We have all experiended crashes in Python, these have been examples of exceptions.

Exceptions are "raised" by code detecting the error or extraordinary condition.

Exceptions can be "handled" by code written by you. Handled exceptions do not cause crashes.

Handling exceptions is done by surrounding code which is likely to cause the exception with a `try` / `except` block.

There may be more than one `except` block per `try` so that more than one kind of exception can be handled.

There are many built-in exceptions.

You can `raise` or cause exceptions to be thrown on purpose.

An exception raised within a `try` block interrupts the `try` block. If there are things that absolutely must be done (clean-up for example), there exists an optional `finally` code block.

Exceptions percolate upward. If the current function does not handle an exception, the exception percolates upward to the calling function. This repeats until an exception handler is found or no exception handler is found (at which point the program crashes).

## Handling an inspecific exception

[Example 1](./example_01.py)

## Handling a built-in exception

[Example 2](./example_02.py)

## Handling more than one exception

[Example 3](./example_03.py)

## Getting more information from an Exception

[Example 4](./example_04.py)

## Raising exceptions

[Example 5](./example_05.py)

## Finally block

[Example 6](./example_06.py)

## Creating custom exceptions

This is a weird place to introduce *classes* for the first time. But here we are.

[Example 7](./example_07.py)
