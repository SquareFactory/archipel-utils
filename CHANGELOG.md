# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).


## [0.2.0](https://github.com/SquareFactory/archipel-utils/compare/v0.1.8...v0.2.0) (2022-10-26)


### Features

* **ci:** release please ([#11](https://github.com/SquareFactory/archipel-utils/issues/11)) ([b9afa34](https://github.com/SquareFactory/archipel-utils/commit/b9afa3493936aef0642989c7ebeca35c3f52f7d2))
* **serialization/deserialization:** fully compatible with base64 ([#10](https://github.com/SquareFactory/archipel-utils/issues/10)) ([98377fe](https://github.com/SquareFactory/archipel-utils/commit/98377fecdad5ca27a1087076019dce8f014724ea))

## [0.1.9] - 2022-07-22

### Improvements

- use psutil for get ram (#9)

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
