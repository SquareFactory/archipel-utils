# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [Unreleased]
- Complete refactor of worker creation to allow for parametrization of workers.
  The command starts a bash shell environment in the `/home/user/dev` folder with the following property : 
  - the dependencies available in the bash shell will be the one provided in the docker image [MODEL_TYPE].
  - the current directory will be mapped to the `/home/user/dev` folder inside the docker. Therefore any file modified in this folder will be repercuted in the host folder.
- We can now use i2 as a development environment thanks to the `i2 debug worker [MODEL_TYPE] -it` sub command. 
- New methods : `i2 build model dir ` and `i2 build model git `. This means that models can be build from any git or dir repo as long as they follow some requirements.
- Worker are named as follow `"{MODEL_TYPE}_{HASH}"`. The hash are the 8 first char of a sha512 of the parameters. 
- A model with no parameters has the following hash `01ba4719`. For example the standard worker for the mirror model is "mirror_01ba4719"
- `i2 debug` function improved. When running debug the structure is now as follow 
 - `/home/user/model` -> path to folder of the model 
 - `/home/user/dev`   -> path to $ARCHIPEL_DIR/tmp/dev 
- Management of worker arguments. This is done using a hashing of the parameters to name the workers. 
- When building a model you can check the model parameters with `i2 build model [MODEL_PARAMS] --help`
 - For example when building from a directory : `i2 build model dir ../models/hft_inference hftBearBull --help`
 - You can then use the command : `i2 build model dir ../models/hft_inference hftBearBull params [PARAMS_HERE]`
 - to create a worker for your specific parameters settings.
 - For example :  `i2 build model dir ../models/hft_inference hftBearBull params -bl v2_b2_mean_value-0.593.data -br v2_b2_mean_value-0.465.data`
   Which will create a worker `worker_aabbbaca.bash` where `aabbbaca.bash` is a hash generated from the parameter string.
