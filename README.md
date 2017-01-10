# pytimeout
[![Build Status](https://travis-ci.org/tsukachu/pytimeout.svg?branch=master)](https://travis-ci.org/tsukachu/pytimeout)

## Description
This package provides developers with a minimal timeout handling.  
If time is exceeded, raise TimeoutError.  

## Usage
pytest contains two functions.  
timeout() is a decorator. Add timeout when defining function.  
with_run() add a timeout when calling an already defined function.  

### argument

    pytimeout.timeout(sec)
    pytimeout.with_run(sec, func, *args, **kwargs)

## Installation

    $ pip install git+https://github.com/tsukachu/pytimeout

## Author
[tsukachu](http://tsukachu.hatenablog.com/)

## License
This is under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).

See [LICENSE](./LICENSE).