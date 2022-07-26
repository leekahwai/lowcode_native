# lowcode_native
The general concept is to create a low code interface for native desktop and server applications. 
The project aims to create the neccessary code bases in C++ (maybe C, Java or Python in future)/ 

Currently, low-code platforms are targeted at delivering end-to-end solutions for customer facing business. They provide a user interface for the customers while also create backends to retrieve the transactions and orders. They are good for mobile and web platforms and typically customized for a consumer based web application. But this low code idea could eventually apply for embedded or high performance applications. We shall try to explore how we can reuse libraries in github and link them up using a web frontend. We're not replicating what the National Instrument is doing for Labview, but instead to generate native code such as C++ to allow integration to various targeted embedded systems or servers. 

Although the aim of the project is to create a low code native application which is based on either C++, the python programming language is chosen to be used for the development of this project. This is good enough for the project development. It doesn't require real-time processing and neither is it an enterprise level application. 

Project shall spin into various tracks. 
The team shall focus on the development in python first without the user interface to linked them yet. 

# Configuration Generation
There is a varied number of ways we read in configuration for our applications. We can choose either through the use of an xml file, a json file or ini file, etc. 
The typical configuration is a key-value pair. Therefore, an abstracted file which prompts to enter the type of key value pairs is sufficient to generate different types of configuration files. Unlike the other tracks, this is not a code generation but a file generation project. 

# Reading Configuration
Although written in python, the end objective is to produce C++ code. Therefore the understanding of the libraries used to read json, xml or ini file in C++ is importatnt. In C++, the use of tinyxpath, rapidjson, and minIni which are cross platform libraries are some suitable candidates. From the configuration generated above, by passing a sample configuration file, the appropriate C++ code that reads in the configuration file should be generated.  

# Interprocess Communication
TBD

# Data management
TBD

