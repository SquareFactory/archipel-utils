# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [0.1.8] - 2022-01-25

### Improvements

- improve gpu utils (#8)


## [0.1.7] - 2022-01-25

### Improvements

- simplify serialization/deserialization of np.ndarray (#7)


## [0.1.6] - 2021-12-01

### Improvements

- remove cv2 dependencies and use pillow instead (#6)


## [0.1.5] - 2021-09-16

### Features

- get vram and ram from a or more pids (#5)


## [0.1.4] - 2021-09-03

### Features

- context manager `cd` to change the current working folder (no revert needed) (#4)


## [0.1.3] - 2021-08-13

### Features

- add `get_obj_size` function which return bytes size of an object (#3)


## [0.1.2] - 2021-08-04

### Features

- add `sanitize_inputs` function which remove special characters from a string

### Fixes

- CI no running because of a branch missmatch (`main` != `master`)
