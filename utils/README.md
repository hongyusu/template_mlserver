#Configuration provider module

1.[Introduction](#introduction)  
2.[Config file](#config-file)  
3.[Environment variables](#environment-variables)  

##Introduction

This module provides [configurable/environment](tests/config.ini) variables as a Dictionary. 

##Config file

By default, the module reads the configuration file from [configs/config.ini](configs/config.ini), but you can specifiy a configuration file with an environment variable *CONFIG_FILE* to override it. 

## Environment variable

All the configuration in the above file can also be overwritten by defining environment varaibles before starting the servers up.



