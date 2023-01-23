# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).


## [0.3.0](https://github.com/SquareFactory/archipel-utils/compare/v0.2.3...v0.3.0) (2023-01-23)


### Features

* **data:** decode img from list of int ([b378749](https://github.com/SquareFactory/archipel-utils/commit/b37874994f66200507df96c3e706519abab26ee4))


### Bug Fixes

* **process:** add exception when nvidia not available ([53e75ab](https://github.com/SquareFactory/archipel-utils/commit/53e75abc6f9d605825aeffacf21cc70b3054f658))

### [0.2.3](https://github.com/SquareFactory/archipel-utils/compare/v0.2.2...v0.2.3) (2022-12-15)


### Bug Fixes

* **data:** lost dimension when grayscale ([#17](https://github.com/SquareFactory/archipel-utils/issues/17)) ([6ad3542](https://github.com/SquareFactory/archipel-utils/commit/6ad3542716f2ff5069a73272208c207fb22b1179))

### [0.2.2](https://github.com/SquareFactory/archipel-utils/compare/v0.2.1...v0.2.2) (2022-10-26)


### Bug Fixes

* **ci:** version file for rebase ([#15](https://github.com/SquareFactory/archipel-utils/issues/15)) ([3df588d](https://github.com/SquareFactory/archipel-utils/commit/3df588d8cc7f6a9f631fc2a01e52edfdcbe3c3f0))

### [0.2.1](https://github.com/SquareFactory/archipel-utils/compare/v0.2.0...v0.2.1) (2022-10-26)


### Bug Fixes

* **ci:** missing extra files in release please ([#13](https://github.com/SquareFactory/archipel-utils/issues/13)) ([65b012a](https://github.com/SquareFactory/archipel-utils/commit/65b012a415257e277a3229a679c693428b55d8bb))

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
