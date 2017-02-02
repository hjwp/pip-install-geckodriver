# Pip install geckodriver!

The idea is that you should be able to install geckodriver with just a 

    pip install geckodriver
    # or
    pip install --user geckodriver

For any platform.  Releases will track https://github.com/mozilla/geckodriver/releases

## TODOS

* be more clever so the user doesn't have to download all 27MB of binaries for every platform before getting
  just the one they want
  
* write a script to automatically update when geckodriver do a new release

* older versions

* tests -- a simple selenium script that tries to load firefox should be enough of a litmus test,
  plus maybe a check on the location of the geckodriver executable
  
