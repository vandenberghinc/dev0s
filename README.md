# dev0s
Author(s):  Daan van den Bergh.<br>
Copyright:  © 2020 Daan van den Bergh All Rights Reserved.<br>
Supported Operating Systems: macos & linux.<br>
<br>
<br>
<p align="center">
  <img src="https://raw.githubusercontent.com/vandenberghinc/public-storage/master/vandenberghinc/icon/icon.png" alt="Bergh-Encryption" width="50"> 
</p>

## Table of content:
  * [Description](#description)
  * [Installation](#installation)
  * [Code Examples](#code-examples)

# Description:
DevOS library.

# Installation:
Install the package.

	curl -s https://raw.githubusercontent.com/vandenberghinc/dev0s/master/dev0s/requirements/installer.remote | bash 

# Code Examples:

### Table of content:
- [__Array__](#array)
  * [save](#save)
  * [load](#load)
  * [string](#string)
  * [divide](#divide)
  * [remove](#remove)
  * [append](#append)
  * [pop](#pop)
  * [count](#count)
  * [check](#check)
  * [clean](#clean)
  * [iterate](#iterate)
  * [items](#items)
  * [keys](#keys)
  * [reversed](#reversed)
  * [sort](#sort)
  * [json](#json)
  * [serialize](#serialize)
  * [instance](#instance)
  * [assign](#assign)
  * [raw](#raw)
- [__Boolean__](#boolean)
  * [string](#string-1)
  * [instance](#instance-1)
  * [assign](#assign-1)
  * [raw](#raw-1)
- [__Bytes__](#bytes)
  * [load](#load-1)
  * [save](#save-1)
  * [instance](#instance-2)
  * [assign](#assign-2)
  * [raw](#raw-2)
- [__CLI__](#cli)
  * [stop](#stop)
  * [docs](#docs)
  * [invalid](#invalid)
- [__Color__](#color)
  * [remove](#remove-1)
  * [fill](#fill)
  * [boolean](#boolean)
- [__Console__](#console)
- [__Date__](#date)
  * [compare](#compare)
  * [increase](#increase)
  * [decrease](#decrease)
  * [to_seconds](#to_seconds)
  * [from_seconds](#from_seconds)
  * [convert](#convert)
  * [instance](#instance-3)
- [__Dictionary__](#dictionary)
  * [save](#save-2)
  * [load](#load-2)
  * [load_line](#load_line)
  * [check](#check-1)
  * [divide](#divide-1)
  * [append](#append-1)
  * [edit](#edit)
  * [unpack](#unpack)
  * [remove](#remove-2)
  * [count](#count-1)
  * [iterate](#iterate-1)
  * [items](#items-1)
  * [keys](#keys-1)
  * [values](#values)
  * [reversed](#reversed-1)
  * [sort](#sort-1)
  * [json](#json-1)
  * [serialize](#serialize-1)
  * [instance](#instance-4)
  * [assign](#assign-3)
  * [raw](#raw-3)
- [__Directory__](#directory)
  * [create](#create)
  * [delete](#delete)
  * [check](#check-2)
  * [load](#load-3)
  * [save](#save-3)
  * [paths](#paths)
  * [names](#names)
  * [oldest_path](#oldest_path)
  * [random_path](#random_path)
  * [generate_path](#generate_path)
  * [structured_join](#structured_join)
  * [contains](#contains)
  * [subpath](#subpath)
  * [fullpath](#fullpath)
  * [set_icon](#set_icon)
  * [index](#index)
  * [open](#open)
  * [find](#find)
  * [replace](#replace)
  * [join](#join)
  * [name](#name)
  * [base](#base)
  * [basename](#basename)
  * [instance](#instance-5)
  * [raw](#raw-4)
- [__Docs__](#docs)
- [__Exceptions__](#exceptions)
- [__File__](#file)
  * [load](#load-4)
  * [load_line](#load_line-1)
  * [save](#save-4)
  * [check](#check-3)
  * [instance](#instance-6)
  * [assign](#assign-4)
  * [raw](#raw-5)
- [__FilePath__](#filepath)
  * [join](#join-1)
  * [name](#name-1)
  * [extension](#extension)
  * [base](#base-1)
  * [basename](#basename-1)
  * [size](#size)
  * [exists](#exists)
  * [mount](#mount)
  * [directory](#directory)
  * [mtime](#mtime)
  * [clean](#clean-1)
  * [absolute](#absolute)
  * [module](#module)
  * [requirements](#requirements)
  * [delete](#delete-1)
  * [move](#move)
  * [copy](#copy)
  * [open](#open-1)
  * [create](#create-1)
  * [check](#check-4)
  * [split](#split)
  * [count](#count-2)
  * [replace](#replace-1)
  * [lower](#lower)
  * [upper](#upper)
  * [instance](#instance-7)
  * [assign](#assign-5)
  * [raw](#raw-6)
- [__Files__](#files)
  * [join](#join-2)
  * [load](#load-5)
  * [save](#save-5)
  * [delete](#delete-2)
  * [chmod](#chmod)
  * [chown](#chown)
  * [exists](#exists-1)
  * [directory](#directory-1)
  * [mounted](#mounted)
  * [create](#create-2)
  * [copy](#copy-1)
  * [move](#move-1)
- [__Formats__](#formats)
  * [check](#check-5)
  * [get](#get)
  * [initialize](#initialize)
  * [denitialize](#denitialize)
- [__Generate__](#generate)
  * [int](#int)
  * [string](#string-2)
- [__Image__](#image)
  * [load](#load-6)
  * [edit_pixel](#edit_pixel)
  * [instance](#instance-8)
  * [raw](#raw-7)
- [__Integer__](#integer)
  * [increase_version](#increase_version)
  * [round](#round)
  * [round_down](#round_down)
  * [generate](#generate)
  * [instance](#instance-9)
  * [assign](#assign-6)
  * [raw](#raw-8)
- [__Loader__](#loader)
  * [run](#run)
  * [stop](#stop-1)
  * [mark](#mark)
  * [hold](#hold)
  * [release](#release)
- [__Object__](#object)
  * [items](#items-2)
  * [keys](#keys-2)
  * [values](#values-1)
  * [assign](#assign-7)
  * [attributes](#attributes)
  * [dict](#dict)
  * [unpack](#unpack-1)
- [__OutputObject__](#outputobject)
  * [instance](#instance-10)
  * [response](#response)
- [__Ownership__](#ownership)
  * [get](#get-1)
  * [set](#set)
  * [check](#check-6)
- [__Parameters__](#parameters)
  * [get](#get-2)
  * [check](#check-7)
- [__Permission__](#permission)
  * [get](#get-3)
  * [set](#set-1)
  * [check](#check-8)
- [__ProgressLoader__](#progressloader)
  * [next](#next)
  * [stop](#stop-2)
- [__Requests__](#requests)
- [__ResponseObject__](#responseobject)
  * [clean](#clean-2)
  * [assign](#assign-8)
  * [crash](#crash)
  * [unpack](#unpack-2)
  * [remove](#remove-3)
  * [iterate](#iterate-2)
  * [items](#items-3)
  * [keys](#keys-3)
  * [values](#values-2)
  * [reversed](#reversed-2)
  * [sort](#sort-2)
  * [dict](#dict-1)
  * [json](#json-2)
  * [serialize](#serialize-2)
  * [instance](#instance-11)
  * [raw](#raw-9)
  * [response](#response-1)
- [__RestAPI__](#restapi)
  * [request](#request)
- [__Spawn__](#spawn)
  * [start](#start)
  * [expect](#expect)
  * [read](#read)
  * [kill](#kill)
  * [wait](#wait)
  * [crashed](#crashed)
  * [expecting](#properties)
- [__String__](#string)
  * [is_numerical](#is_numerical)
  * [bash](#bash)
  * [identifier](#identifier)
  * [variable_format](#variable_format)
  * [class_format](#class_format)
  * [capitalized_scentence](#capitalized_scentence)
  * [capitalized_word](#capitalized_word)
  * [generate](#generate-1)
  * [first_occurence](#first_occurence)
  * [before_after_first_occurence](#before_after_first_occurence)
  * [before_selected_after_first_occurence](#before_selected_after_first_occurence)
  * [before_after_last_occurence](#before_after_last_occurence)
  * [before_selected_after_last_occurence](#before_selected_after_last_occurence)
  * [between](#between)
  * [increase_version](#increase_version-1)
  * [slice_dict](#slice_dict)
  * [slice_array](#slice_array)
  * [slice_tuple](#slice_tuple)
  * [indent](#indent)
  * [line_indent](#line_indent)
  * [slice_indent](#slice_indent)
  * [first](#first)
  * [last](#last)
  * [remove_first](#remove_first)
  * [remove_last](#remove_last)
  * [split](#split-1)
  * [count](#count-3)
  * [replace](#replace-2)
  * [lower](#lower-1)
  * [upper](#upper-1)
  * [instance](#instance-12)
  * [assign](#assign-9)
  * [raw](#raw-10)
- [__Symbol__](#symbol)
- [__Thread__](#thread)
  * [run](#run-1)
  * [safe_start](#safe_start)
  * [safe_stop](#safe_stop)
  * [send_stop](#send_stop)
  * [send_crash](#send_crash)
  * [log](#log)
  * [run_permission](#properties-1)
- [__Traceback__](#traceback)
  * [traceback](#properties-2)
- [__Zip__](#zip)
  * [create](#create-3)
  * [extract](#extract)
  * [instance](#instance-13)
  * [raw](#raw-11)
- [____Defaults____](#__defaults__)
  * [operating_system](#operating_system)
  * [alias](#alias)
  * [source_path](#source_path)
  * [log_level](#log_level)
  * [pwd](#pwd)
  * [insert](#insert)
  * [site_packages](#site_packages)
  * [install_requirements](#install_requirements)
- [____Environment____](#__environment__)
  * [fill](#fill-1)
  * [import_](#import_)
  * [export](#export)
  * [get](#get-4)
  * [get_string](#get_string)
  * [get_boolean](#get_boolean)
  * [get_integer](#get_integer)
  * [get_array](#get_array)
  * [get_tuple](#get_tuple)
  * [get_dictionary](#get_dictionary)
  * [set](#set-2)
  * [set_string](#set_string)
  * [set_boolean](#set_boolean)
  * [set_integer](#set_integer)
  * [set_array](#set_array)
  * [set_tuple](#set_tuple)
  * [set_dictionary](#set_dictionary)
- [____Response____](#__response__)
  * [success](#success)
  * [error](#error)
  * [log](#log-1)
  * [load_logs](#load_logs)
  * [reset_logs](#reset_logs)
  * [serialize](#serialize-3)
  * [response](#response-3)

## Array:
The array object class.
``` python 

# initialize the array object class.
array = Array(
    # the array (param #1).
    array=[],
    # the path (param #2).
    path=False,
    # load the data on initialization.
    load=False,
    # the default array (will be created if file path does not exist).
    default=None, )

```

#### Functions:

##### save:
``` python

# call array.save.
_ = array.save(array=None, path=None, ensure_ascii=False, indent=4, sudo=False)

```
##### load:
``` python

# call array.load.
_ = array.load(default=None, sudo=False)

```
##### string:
``` python

# call array.string.
_ = array.string(joiner=" ", sum_first=False)

```
##### divide:
``` python

# call array.divide.
_ = array.divide(into=2)

```
##### remove:
``` python

# call array.remove.
_ = array.remove(indexes=[], values=[], update=True, save=False)

```
##### append:
``` python

# call array.append.
_ = array.append(var)

```
##### pop:
``` python

# call array.pop.
_ = array.pop(index)

```
##### count:
``` python

# call array.count.
_ = array.count(item=None)

```
##### check:
``` python

# call array.check.
_ = array.check(default=None, save=True)

```
##### clean:
``` python

# call array.clean.
_ = array.clean(
    # the string replacements.
    #    example:
    #        { "Hello":"hello" }
    #        [ ["Hello", "hello"] ]
    replacements={},
    # the first characters to remove (String & Array).
    remove_first=[],
    # the last characters to remove (String & Array).
    remove_last=[],
    # the first characters that are ensured (String & Array) (List: check is one of the list is ensured).
    ensure_first=[],
    # the last characters that are ensured (String & Array) (List: check is one of the list is ensured).
    ensure_last=[],
    # remove all values within the list from the array.
    remove_values=[],
    # update the self array.
    update=True,
    # the dicionary (leave None to use array.array).
    array=None, )

```
##### iterate:
``` python

# call array.iterate.
_ = array.iterate(sorted=False, reversed=False, array=None)

```
##### items:
``` python

# call array.items.
_ = array.items(sorted=False, reversed=False, array=None)

```
##### keys:
``` python

# call array.keys.
_ = array.keys(sorted=False, reversed=False, array=None)

```
##### reversed:
``` python

# call array.reversed.
_ = array.reversed(array=None)

```
##### sort:
``` python

# call array.sort.
_ = array.sort(alphabetical=True, ascending=False, reversed=False, array=None)

```
##### json:
``` python

# call array.json.
_ = array.json(sorted=False, reversed=False, indent=4, array=None, )

```
##### serialize:
``` python

# call array.serialize.
_ = array.serialize(sorted=False, reversed=False, json=False, array=None)

```
##### instance:
``` python

# call array.instance.
_ = array.instance()

```
##### assign:
``` python

# call array.assign.
_ = array.assign(array, save=False)

```
##### raw:
``` python

# call array.raw.
_ = array.raw()

```

## Boolean:
The boolean object class.
``` python 

# initialize the boolean object class.
boolean = Boolean(boolean=False)

```

#### Functions:

##### string:
``` python

# call boolean.string.
_ = boolean.string(true="True", false="False")

```
##### instance:
``` python

# call boolean.instance.
_ = boolean.instance()

```
##### assign:
``` python

# call boolean.assign.
_ = boolean.assign(boolean)

```
##### raw:
``` python

# call boolean.raw.
_ = boolean.raw()

```

## Bytes:
The bytes object class.
``` python 

# initialize the bytes object class.
bytes = Bytes(
    # the bytes (param #1).
    data=b"",
    # the file path.
    path=None, )

```

#### Functions:

##### load:
``` python

# call bytes.load.
_ = bytes.load(sudo=False)

```
##### save:
``` python

# call bytes.save.
_ = bytes.save(bytes=None, sudo=False)

```
##### instance:
``` python

# call bytes.instance.
_ = bytes.instance()

```
##### assign:
``` python

# call bytes.assign.
_ = bytes.assign(b)

```
##### raw:
``` python

# call bytes.raw.
_ = bytes.raw()

```

## CLI:
The cli object class.
``` python 

# initialize the cli object class.
cli = CLI(alias=None, modes={}, options={}, notes={}, executable=__file__, author="Daan van den Bergh")

```

#### Functions:

##### stop:
``` python

# call cli.stop.
_ = cli.stop(
    # success exit.
    success=True,
    # optional order 1 success message (overwrites success to response.success).
    response={},
    # optional order 2 success message (overwrites success to True).
    message=None,
    # optional order 3 message.
    error=None,
    # json format.
    json=False, )

```
##### docs:
``` python

# call cli.docs.
_ = cli.docs(
    # the chapter (optional).
    chapter=None,
    # the mode (optional).
    mode=None,
    # success exit.
    success=True,
    # optional order 1 success message (overwrites success to response.success).
    response={},
    # optional order 2 success message (overwrites success to True).
    message=None,
    # optional order 3 message.
    error=None,
    # json format.
    json=False,
    # stop after show.
    stop=True,
    # overwrite default notes (dict) (specify to use).
    notes=None, )

```
##### invalid:
``` python

# call cli.invalid.
_ = cli.invalid(error="Selected an invalid mode.", chapter=None, mode=None, json=False)

```

## Color:
The color object class.
``` python 

# import the color object class.
from dev0s import color

```

#### Functions:

##### remove:
``` python

# call color.remove.
_ = color.remove(string)

```
##### fill:
``` python

# call color.fill.
_ = color.fill(string)

```
##### boolean:
``` python

# call color.boolean.
_ = color.boolean(boolean, red=True)

```

## Console:
The console object class.
``` python 

# initialize the console object class.
console = Console

```
## Date:
The date object class.
``` python 

# initialize the date object class.
date = Date(
    #
    # Leave all parameters None to initialize a Date() object with the current date.
    #
    # Initialize a future / previous date.
    #   option 1:
    #     specify the timestamp to initialize a previous / future date (format required).
    timestamp=None,
    #     required for parameter [timestamp].
    format="%d-%m-%y %H:%M",
    #   options 2:
    #     initialize by seconds.
    seconds=None, )

```

#### Functions:

##### compare:
``` python

# call date.compare.
_ = date.compare(comparison=None, current=None, format="%d-%m-%y %H:%M")

```
##### increase:
``` python

# call date.increase.
_ = date.increase(string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M")

```
##### decrease:
``` python

# call date.decrease.
_ = date.decrease(string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M")

```
##### to_seconds:
``` python

# call date.to_seconds.
_ = date.to_seconds(string, format="%d-%m-%y %H:%M")

```
##### from_seconds:
``` python

# call date.from_seconds.
_ = date.from_seconds(seconds, format="%d-%m-%y %H:%M")

```
##### convert:
``` python

# call date.convert.
_ = date.convert(string, input="%d-%m-%y %H:%M", output="%Y%m%d")

```
##### instance:
``` python

# call date.instance.
_ = date.instance()

```

## Dictionary:
The dictionary object class.
``` python 

# initialize the dictionary object class.
dictionary = Dictionary(
    # the dictionary (param #1).
    dictionary={},
    # the file path (param #2).
    path=False,
    # load the file path dictionary on init.
    load=False,
    # specify default to check & create the dict.
    default=None, )

```

#### Functions:

##### save:
``` python

# call dictionary.save.
_ = dictionary.save(dictionary=None, path=None, ensure_ascii=False, indent=4, sudo=False)

```
##### load:
``` python

# call dictionary.load.
_ = dictionary.load(default=None, sudo=False)

```
##### load_line:
``` python

# call dictionary.load_line.
_ = dictionary.load_line(line_number, sudo=False)

```
##### check:
``` python

# call dictionary.check.
_ = dictionary.check(
    #   Option 1:
    key=None, # check a certain key, it appends if not present
    value=None, # check a certain key, append the value if not present (no format check)
    #   Option 2:
    default=None, # check based on a default dictionary, it appends it not present.
    #   Optionals:
    dictionary=None, # overwrite the start dictionary, leave None to use dictionary.dictionary.
    save=False, # saves the output & and sets the output to dictionary.dictionary. )

```
##### divide:
``` python

# call dictionary.divide.
_ = dictionary.divide(into=2)

```
##### append:
``` python

# call dictionary.append.
_ = dictionary.append(
    # by default it only overwrites if a key does not exist and sums the key if it is a str / int.
    #
    # a dictionary to append.
    dictionary,
    # the overwrite formats (add "*" for all).
    overwrite=[],
    # the sum formats (add "*" for all).
    sum=["int", "float"],
    # the banned dictionary keys.
    banned=[],
    # update the self dict.
    update=True,
    # save the new dict.
    save=False,
    # do not use.
    dictionary_=None, )

```
##### edit:
``` python

# call dictionary.edit.
_ = dictionary.edit(
    # the dictionary (leave None to use dictionary.dictionary).
    dictionary=None,
    # the edits (dict).
    #     adds / replaces the current (except the exceptions).
    edits={},
    # the edits key Exceptions.
    exceptions=[],
    # the edits value Exceptions.
    value_exceptions=[None],
    # the instances to overwrite (list[str]) (missing stands for the keys that are missing in the dictionary).
    overwite=["missing"],
    # the instances to combine (list[str]) (dict is always recursive).
    combine=["int", "float", "Integer", "list", "Array"],
    # save the edits.
    save=True,
    # the log level.
    log_level=-1, )

```
##### unpack:
``` python

# call dictionary.unpack.
_ = dictionary.unpack(
    # the key / keys / defaults parameter (#1).
    # str instance:
    #   unpack the str key
    # list instance:
    #   unpack all keys in the list.
    # dict instance:
    #   unpack all keys from the dict & when not present return the key's value as default.
    keys, )

```
##### remove:
``` python

# call dictionary.remove.
_ = dictionary.remove(keys=[], values=[], update=True, save=False, dictionary=None)

```
##### count:
``` python

# call dictionary.count.
_ = dictionary.count(item=None, values=False)

```
##### iterate:
``` python

# call dictionary.iterate.
_ = dictionary.iterate(sorted=False, reversed=False, dictionary=None)

```
##### items:
``` python

# call dictionary.items.
_ = dictionary.items(sorted=False, reversed=False, dictionary=None)

```
##### keys:
``` python

# call dictionary.keys.
_ = dictionary.keys(sorted=False, reversed=False, dictionary=None)

```
##### values:
``` python

# call dictionary.values.
_ = dictionary.values(sorted=False, reversed=False, dictionary=None)

```
##### reversed:
``` python

# call dictionary.reversed.
_ = dictionary.reversed(update=True, dictionary=None)

```
##### sort:
``` python

# call dictionary.sort.
_ = dictionary.sort(alphabetical=True, ascending=False, reversed=False, update=True, dictionary=None)

```
##### json:
``` python

# call dictionary.json.
_ = dictionary.json(sorted=False, reversed=False, indent=4, dictionary=None, )

```
##### serialize:
``` python

# call dictionary.serialize.
_ = dictionary.serialize(sorted=False, reversed=False, json=False, dictionary=None)

```
##### instance:
``` python

# call dictionary.instance.
_ = dictionary.instance(serialize=False)

```
##### assign:
``` python

# call dictionary.assign.
_ = dictionary.assign(dictionary, save=False)

```
##### raw:
``` python

# call dictionary.raw.
_ = dictionary.raw()

```

## Directory:
The directory object class.
``` python 

# initialize the directory object class.
directory = Directory(
    # the dirs file path (param #1).
    path=None,
    # the hierarchy to check / create.
    hierarchy={},
    # load the content.
    #load=False,
    # load recursive.
    #recursive=False, )

```

#### Functions:

##### create:
``` python

# call directory.create.
_ = directory.create(file_paths=[], path=None, sudo=False, owner=None, group=None, permission=None)

```
##### delete:
``` python

# call directory.delete.
_ = directory.delete(forced=False)

```
##### check:
``` python

# call directory.check.
_ = directory.check(
    #   Required:
    #   -   dictionary format:
    hierarchy=None,
    #   Optionals:
    #   -   string format:
    owner=None,
    group=None,
    #   -   boolean format:
    sudo=False,
    #   -   integer format:
    permission=None, # (octal format)
    recursive=False, # for permission/ownership
    silent=False, )

```
##### load:
``` python

# call directory.load.
_ = directory.load(path=None, format=str, default=None, sudo=False)

```
##### save:
``` python

# call directory.save.
_ = directory.save(path=None, data=None, format=str, sudo=False)

```
##### paths:
``` python

# call directory.paths.
_ = directory.paths(dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], banned_basenames=["__pycache__"], extensions=["*"])

```
##### names:
``` python

# call directory.names.
_ = directory.names(dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], extensions=["*"], remove_extensions=False)

```
##### oldest_path:
``` python

# call directory.oldest_path.
_ = directory.oldest_path()

```
##### random_path:
``` python

# call directory.random_path.
_ = directory.random_path()

```
##### generate_path:
``` python

# call directory.generate_path.
_ = directory.generate_path(length=24, type="/")

```
##### structured_join:
``` python

# call directory.structured_join.
_ = directory.structured_join(name, type="", structure="alphabetical", create_base=False, sudo=False, owner=None, group=None, permission=None)

```
##### contains:
``` python

# call directory.contains.
_ = directory.contains(name=None, type="/", recursive=False)

```
##### subpath:
``` python

# call directory.subpath.
_ = directory.subpath(fullpath)

```
##### fullpath:
``` python

# call directory.fullpath.
_ = directory.fullpath(subpath)

```
##### set_icon:
``` python

# call directory.set_icon.
_ = directory.set_icon(
    # the path to the .png / .jpg icon.
    icon=None,
    # the directory path (leave None to use directory.fp.path).
    path=None, )

```
##### index:
``` python

# call directory.index.
_ = directory.index(
    # the wanted options.
    metrics=[],
    options=["size", "mtime", "content", "name", "basename", "extension", "mount", "directory"],
    # optional path (leave None to use directory.path).
    path=None, )

```
##### open:
``` python

# call directory.open.
_ = directory.open(path=None, sudo=False)

```
##### find:
``` python

# call directory.find.
_ = directory.find(matches:list, path=None, recursive=False, log_level=0)

```
##### replace:
``` python

# call directory.replace.
_ = directory.replace(replacements:list, path=None, recursive=False, log_level=0)

```
##### join:
``` python

# call directory.join.
_ = directory.join(name=None, type="")

```
##### name:
``` python

# call directory.name.
_ = directory.name()

```
##### base:
``` python

# call directory.base.
_ = directory.base()

```
##### basename:
``` python

# call directory.basename.
_ = directory.basename()

```
##### instance:
``` python

# call directory.instance.
_ = directory.instance()

```
##### raw:
``` python

# call directory.raw.
_ = directory.raw()

```

## Docs:
The docs object class.
``` python 

# initialize the docs object class.
docs = Docs(
    # boolean inidicating if the object is initialized by default.
    initialized=True,
    # the full module path in import style (when initializing).
    module="Code.Docs",
    # the notes that will apread above the class_ initialization (leave [] to use default.
    notes=[], ):
    # attributes.
    docs.initialized = initialized
    docs.module = module
    docs.notes = notes
    # checks.
    if docs.notes in [None, False, ""]: docs.notes = []
    #

```
## Exceptions:
The exceptions object class.
``` python 

# initialize the exceptions object class.
exceptions = Exceptions

```
## File:
The file object class.
``` python 

# initialize the file object class.
file = File(path=None, data=None, load=False, default=None)

```

#### Functions:

##### load:
``` python

# call file.load.
_ = file.load(default=None, sudo=False)

```
##### load_line:
``` python

# call file.load_line.
_ = file.load_line(line_number, default=None, sudo=False)

```
##### save:
``` python

# call file.save.
_ = file.save(data=None, path=None, overwrite_duplicates=True, sudo=False)

```
##### check:
``` python

# call file.check.
_ = file.check(default=None, save=True)

```
##### instance:
``` python

# call file.instance.
_ = file.instance()

```
##### assign:
``` python

# call file.assign.
_ = file.assign(data)

```
##### raw:
``` python

# call file.raw.
_ = file.raw()

```

## FilePath:
The file_path object class.
``` python 

# initialize the file_path object class.
file_path = FilePath(path, default=False, check=False, load=False)

```

#### Functions:

##### join:
``` python

# call file_path.join.
_ = file_path.join(name=None, type="/")

```
##### name:
``` python

# call file_path.name.
_ = file_path.name(path=None, remove_extension=False,)

```
##### extension:
``` python

# call file_path.extension.
_ = file_path.extension(name=None, path=None)

```
##### base:
``` python

# call file_path.base.
_ = file_path.base(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the dirs back.
    back=1, )

```
##### basename:
``` python

# call file_path.basename.
_ = file_path.basename(back=1, path=None)

```
##### size:
``` python

# call file_path.size.
_ = file_path.size(mode="auto", options=["auto", "bytes", "kb", "mb", "gb", "tb"], format=str, path=None)

```
##### exists:
``` python

# call file_path.exists.
_ = file_path.exists(
    # the path (leave None to use file_path.path) (#1).
    path=None,
    # root permission required.
    sudo=False, )

```
##### mount:
``` python

# call file_path.mount.
_ = file_path.mount(
    # the path (leave None to use file_path.path) (#1).
    path=None, )

```
##### directory:
``` python

# call file_path.directory.
_ = file_path.directory(
    # the path (leave None to use file_path.path) (#1).
    path=None, )

```
##### mtime:
``` python

# call file_path.mtime.
_ = file_path.mtime(format='%d-%m-%y %H:%M.%S', path=None)

```
##### clean:
``` python

# call file_path.clean.
_ = file_path.clean(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the clean options.
    remove_double_slash=True,
    remove_first_slash=False,
    remove_last_slash=False,
    ensure_first_slash=False,
    ensure_last_slash=False, )

```
##### absolute:
``` python

# call file_path.absolute.
_ = file_path.absolute(
    # the path (leave None to use file_path.path) (param #1).
    path=None, )

```
##### module:
``` python

# call file_path.module.
_ = file_path.module(path=None)

```
##### requirements:
``` python

# call file_path.requirements.
_ = file_path.requirements(path=None, format="pip", include_version=True)

```
##### delete:
``` python

# call file_path.delete.
_ = file_path.delete(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the options.
    forced=False,
    sudo=False,
    silent=False, )

```
##### move:
``` python

# call file_path.move.
_ = file_path.move(path=None, sudo=False, silent=False)

```
##### copy:
``` python

# call file_path.copy.
_ = file_path.copy(path=None, sudo=False, silent=False)

```
##### open:
``` python

# call file_path.open.
_ = file_path.open(sudo=False)

```
##### create:
``` python

# call file_path.create.
_ = file_path.create(
    #   Option 1: (creating a directory)
    #   -   boolean format:
    directory=False,
    #   Option 2: (creating any file extension)
    #   -   string format:
    data="",
    #   Options:
    #   -   integer format:
    permission=None,
    #   -   string format:
    owner=None,
    group=None,
    #   -   boolean format:
    sudo=False, )

```
##### check:
``` python

# call file_path.check.
_ = file_path.check(
    #   Option 1: (creating a directory)
    #   -   boolean format:
    directory=False,
    #   Option 2: (creating any file extension)
    #   -   string format:
    data="",
    #   Options:
    #   -   integer format:
    permission=None,
    #   -   string format:
    owner=None,
    group=None,
    #   -   boolean format:
    sudo=False,
    silent=False,
    recursive=False, # for directories only (for permission & ownership check) )

```
##### split:
``` python

# call file_path.split.
_ = file_path.split(path)

```
##### count:
``` python

# call file_path.count.
_ = file_path.count(path)

```
##### replace:
``` python

# call file_path.replace.
_ = file_path.replace(from_, to_)

```
##### lower:
``` python

# call file_path.lower.
_ = file_path.lower(path)

```
##### upper:
``` python

# call file_path.upper.
_ = file_path.upper(path)

```
##### instance:
``` python

# call file_path.instance.
_ = file_path.instance()

```
##### assign:
``` python

# call file_path.assign.
_ = file_path.assign(path, load=False)

```
##### raw:
``` python

# call file_path.raw.
_ = file_path.raw()

```

## Files:
The files object class.
``` python 

# initialize the files object class.
files = Files(path=None, name=None, type="")

```

#### Functions:

##### join:
``` python

# call files.join.
_ = Files.join(path=None, name=None, type="")

```
##### load:
``` python

# call files.load.
_ = Files.load(path, data="not to be used", format="str", raw=False, sudo=False)

```
##### save:
``` python

# call files.save.
_ = Files.save(path, data, format="str", sudo=False, indent=4, ensure_ascii=False)

```
##### delete:
``` python

# call files.delete.
_ = Files.delete(
    # the path (param #1).
    path=None,
    # root permission required.
    sudo=False,
    # forced mode.
    forced=False,
    # hide logs.
    silent=False, )

```
##### chmod:
``` python

# call files.chmod.
_ = Files.chmod(
    # the path (param #1).
    path=None,
    # the new permission.
    permission=None,
    # recursive for entire dir.
    recursive=False,
    # root permission required.
    sudo=False, )

```
##### chown:
``` python

# call files.chown.
_ = Files.chown(
    # the path (param #1).
    path=None,
    # the new owner.
    owner=None,
    # the new group (optional).
    group=None,
    # recursive for entire dir.
    recursive=False,
    # root permission required.
    sudo=False, )

```
##### exists:
``` python

# call files.exists.
_ = Files.exists(path=None, sudo=False)

```
##### directory:
``` python

# call files.directory.
_ = Files.directory(
    # the path (#1).
    path=None,
    # root permission required.
    sudo=False, )

```
##### mounted:
``` python

# call files.mounted.
_ = Files.mounted(
    # the path (#1).
    path=None, )

```
##### create:
``` python

# call files.create.
_ = Files.create(
    # the path to the file (str) (REQUIRED) (#1).
    path=None,
    # the data (str) (optional).
    data=None,
    # path is directory (bool).
    directory=False,
    # the owner (str) (optional).
    owner=None,
    # the group (str) (optional).
    group=None,
    # the permission (int) (optional).
    permission=None,
    # root permission required.
    sudo=False, )

```
##### copy:
``` python

# call files.copy.
_ = Files.copy(
    # the from & to path (#1 & #2).
    from_, to_,
    # root permission required.
    sudo=False,
    # root permission required.
    log_level=0, )

```
##### move:
``` python

# call files.move.
_ = Files.move(
    # the from & to path (#1 & #2).
    from_, to_,
    # root permission required.
    sudo=False,
    # root permission required.
    log_level=0, )

```

## Formats:
The formats object class.
``` python 

# initialize the formats object class.
formats = Formats(i.upper())

```

#### Functions:

##### check:
``` python

# call formats.check.
_ = Formats.check(
    nones=None,
    booleans=None,
    none_allowed_booleans=None,
    strings=None,
    none_allowed_strings=None,
    integers=None,
    none_allowed_integers=None,
    bytes_=None,
    none_allowed_bytes=None,
    arrays=None,
    none_allowed_arrays=None,
    dictionaries=None,
    none_allowed_dictionaries=None, )

```
##### get:
``` python

# call formats.get.
_ = Formats.get(value, serialize=False)

```
##### initialize:
``` python

# call formats.initialize.
_ = Formats.initialize(
    # the object / value (#1 param).
    obj=None,
    # list / dict with objects.
    objects=None,
    # initialize file paths.
    file_paths=False,
    # the forced format.
    format=None, )

```
##### denitialize:
``` python

# call formats.denitialize.
_ = Formats.denitialize(
    # the object / value (#1 param).
    obj=None,
    # list / dict with objects.
    objects=None,
    # initialize file paths.
    file_paths=True, )

```

## Generate:
The generate object class.
``` python 

# initialize the generate object class.
generate = Generate()

```

#### Functions:

##### int:
``` python

# call generate.int.
_ = generate.int(length=6)

```
##### string:
``` python

# call generate.string.
_ = generate.string(length=6, capitalize=True, digits=True)

```

## Image:
The image object class.
``` python 

# initialize the image object class.
image = Image(path=None, image=None, load=False)

```

#### Functions:

##### load:
``` python

# call image.load.
_ = image.load(path=None)

```
##### edit_pixel:
``` python

# call image.edit_pixel.
_ = image.edit_pixel(pixel=[0, 0], new_pixel_tuple=None)

```
##### instance:
``` python

# call image.instance.
_ = image.instance()

```
##### raw:
``` python

# call image.raw.
_ = image.raw()

```

## Integer:
The integer object class.
``` python 

# initialize the integer object class.
integer = Integer(value=0, format="auto")

```

#### Functions:

##### increase_version:
``` python

# call integer.increase_version.
_ = integer.increase_version()

```
##### round:
``` python

# call integer.round.
_ = integer.round(decimals)

```
##### round_down:
``` python

# call integer.round_down.
_ = integer.round_down(decimals)

```
##### generate:
``` python

# call integer.generate.
_ = integer.generate(length=6)

```
##### instance:
``` python

# call integer.instance.
_ = integer.instance()

```
##### assign:
``` python

# call integer.assign.
_ = integer.assign(value)

```
##### raw:
``` python

# call integer.raw.
_ = integer.raw()

```

## Loader:
The loader object class.
``` python 

# initialize the loader object class.
loader = Loader(message, autostart=True, log_level=0, interactive=True)

```

#### Functions:

##### run:
``` python

# call loader.run.
_ = loader.run()

```
##### stop:
``` python

# call loader.stop.
_ = loader.stop(message=None, success=True, response=None, quiet=False)

```
##### mark:
``` python

# call loader.mark.
_ = loader.mark(new_message=None, old_message=None, success=True, response=None)

```
##### hold:
``` python

# call loader.hold.
_ = loader.hold()

```
##### release:
``` python

# call loader.release.
_ = loader.release()

```

## Object:
The object object class.
``` python 

# initialize the object object class.
object = Object(
    # attributes (dict) (#1)
    attributes={},
    # the imported traceback.
    traceback="Object",
    # the raw traceback.
    raw_traceback="syst3m.classes.objects.Object", )

```

#### Functions:

##### items:
``` python

# call object.items.
_ = object.items()

```
##### keys:
``` python

# call object.keys.
_ = object.keys()

```
##### values:
``` python

# call object.values.
_ = object.values()

```
##### assign:
``` python

# call object.assign.
_ = object.assign(
    # the dictionary to self assign.
    dictionary,
    # serialize dictionary from str to object.
    serialize=True,
    # the keys to get from the dict.
    keys=["*"],
    # safe disabled throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### attributes:
``` python

# call object.attributes.
_ = object.attributes(keys=[])

```
##### dict:
``` python

# call object.dict.
_ = object.dict(keys=[])

```
##### unpack:
``` python

# call object.unpack.
_ = object.unpack(
    # the key / keys / defaults parameter (#1).
    # str instance:
    #   unpack the str key
    # list instance:
    #   unpack all keys in the list.
    # dict instance:
    #   unpack all keys from the dict & when not present return the key's value as default.
    keys, )

```

## OutputObject:
The output_object object class.
``` python 

# initialize the output_object object class.
output_object = OutputObject(
    #
    # The return object from function: Code.execute
    # The OutputObject object is very similair to the ResponseObject.
    #
    # the success message (param #1).
    message=None,
    # the attributes (param #2).
    attributes={},
    # the error message (param #3).
    error=None,
    # the log level.
    log_level=Defaults.options.log_level, )

```

#### Functions:

##### instance:
``` python

# call output_object.instance.
_ = output_object.instance()

```
##### response:
``` python

# call output_object.response.
response = output_object.response()

```

## Ownership:
The ownership object class.
``` python 

# initialize the ownership object class.
ownership = Ownership(path=None, load=False)

```

#### Functions:

##### get:
``` python

# call ownership.get.
_ = ownership.get(path=None)

```
##### set:
``` python

# call ownership.set.
_ = ownership.set(
    # the permission (str) (#1).
    owner=None,
    # the group (str) (optional) (#2).
    group=None,
    # the path (optional) (overwrites ownership.path) (#3).
    path=None,
    # root permission required.
    sudo=False,
    # recursive.
    recursive=False,
    # silent.
    silent=False, )

```
##### check:
``` python

# call ownership.check.
_ = ownership.check(owner=None, group=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

```

## Parameters:
The Response.parameters object class.
``` python 

# import the Response.parameters object class.
from dev0s import Response.parameters

```

#### Functions:

##### get:
``` python

# call Response.parameters.get.
_ = Response.parameters.get(
    # the django request (1).
    request=None,
    # the identifiers (#2).
    #    str instance: return the parameters value.
    #    list instance: return a parameters object & return an error response when a parameter is undefined.
    #    dict instance: return a parameters object & return the parameter's value from the dict as a default when undefined.
    parameters=[],
    # default return value (dict instance of parameters overwrites the default parameter).
    default=None,
    # traceback id.
    traceback=None, )

```
##### check:
``` python

# call Response.parameters.check.
response = Response.parameters.check(
    # the parameters (dict) (#1).
    parameters={"parameter":None},
    # the recognizer value for when the parameters are supposed to be empty.
    default=None,
    # the traceback id.
    traceback=None, )

```

## Permission:
The permission object class.
``` python 

# initialize the permission object class.
permission = Permission(path=None, load=False)

```

#### Functions:

##### get:
``` python

# call permission.get.
_ = permission.get(path=None)

```
##### set:
``` python

# call permission.set.
_ = permission.set(
    # the permission (int) (#1).
    permission=None,
    # the path (optional) (overwrites permission.path) (#2).
    path=None,
    # root permission required.
    sudo=False,
    # recursive.
    recursive=False,
    # silent.
    silent=False, )

```
##### check:
``` python

# call permission.check.
_ = permission.check(permission=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

```

## ProgressLoader:
The progress_loader object class.
``` python 

# initialize the progress_loader object class.
progress_loader = ProgressLoader(message, index=0, max=10, log_level=0)

```

#### Functions:

##### next:
``` python

# call progress_loader.next.
_ = progress_loader.next(count=1, decimals=2)

```
##### stop:
``` python

# call progress_loader.stop.
_ = progress_loader.stop(message=None, success=True, response=None)

```

## Requests:
The requests object class.
``` python 

# initialize the requests object class.
requests = Requests

```
## ResponseObject:
The response_object object class.
``` python 

# initialize the response_object object class.
response_object = ResponseObject(
    #
    # Should be initialized with Response.success or Response.error.
    #
    # the response attributes.
    attributes={
        "success":False,
        "message":None,
        "error":None,
    },
    # import a dumped json response (str) (ignores attributes).
    json=None, )

```

#### Functions:

##### clean:
``` python

# call response_object.clean.
_ = response_object.clean(
    # the clean options, select * for all, options: [traceback].
    options=["*"],
    # serialize to ResponseObject (with serialize False the ResponseObject's values are not updated).
    serialize=True, )

```
##### assign:
``` python

# call response_object.assign.
_ = response_object.assign(dictionary)

```
##### crash:
``` python

# call response_object.crash.
_ = response_object.crash(error="ValueError", traceback=True, json=False)

```
##### unpack:
``` python

# call response_object.unpack.
_ = response_object.unpack(
    # the key / keys / defaults parameter (#1).
    # str instance:
    #   unpack the str key
    # list instance:
    #   unpack all keys in the list.
    # dict instance:
    #   unpack all keys from the dict & when not present return the key's value as default.
    keys, )

```
##### remove:
``` python

# call response_object.remove.
_ = response_object.remove(keys=[], values=[], save=False)

```
##### iterate:
``` python

# call response_object.iterate.
_ = response_object.iterate(sorted=False, reversed=False)

```
##### items:
``` python

# call response_object.items.
_ = response_object.items(sorted=False, reversed=False, dictionary=None)

```
##### keys:
``` python

# call response_object.keys.
_ = response_object.keys(sorted=False, reversed=False)

```
##### values:
``` python

# call response_object.values.
_ = response_object.values(sorted=False, reversed=False, dictionary=None)

```
##### reversed:
``` python

# call response_object.reversed.
_ = response_object.reversed(dictionary=None)

```
##### sort:
``` python

# call response_object.sort.
_ = response_object.sort(alphabetical=True, ascending=False, reversed=False, dictionary=None)

```
##### dict:
``` python

# call response_object.dict.
_ = response_object.dict(sorted=False, reversed=False, json=False)

```
##### json:
``` python

# call response_object.json.
_ = response_object.json(sorted=False, reversed=False, indent=4, dictionary=None, )

```
##### serialize:
``` python

# call response_object.serialize.
_ = response_object.serialize(sorted=False, reversed=False, json=False, dictionary=None)

```
##### instance:
``` python

# call response_object.instance.
_ = response_object.instance()

```
##### raw:
``` python

# call response_object.raw.
_ = response_object.raw()

```
##### response:
``` python

# call response_object.response.
_ = response_object.response()

```

## RestAPI:
The restapi object class.
``` python 

# initialize the restapi object class.
restapi = RestAPI(
    # the root url (optional).
    url=None,
    # the default data send with every request (will be appended to local data).
    data={
        "api_key":None,
    }, )

```

#### Functions:

##### request:
``` python

# call restapi.request.
_ = restapi.request(url="/", data={})

```

## Spawn:
The spawn object class.
``` python 

# initialize the spawn object class.
spawn = Spawn(
    #
    # Should be initialized with function: Code.execute
    #
    # the full command (str) (#1).
    command="ls",
    # asynchronous.
    async_=False,
    # the log level.
    log_level=Defaults.options.log_level,
    # additional attributes.
    attributes={},
    # system options.
    response_str=None, )

```

#### Functions:

##### start:
``` python

# call spawn.start.
response = spawn.start()

```
##### expect:
``` python

# call spawn.expect.
response = spawn.expect(
    # the expected data parameter (#1).
    #    str instantce: expect a single identifier.
    #    list instance: expect one of the provided identifiers & return the found one if success.
    expect=["Password*"],
    # the optional data to send (#2).
    #    none instance: do not send anything.
    #    str instance: the data to send.
    #    list/tuple instance: send value of index from expected expect (required expect to be a list, Array & the indexes of [expect, send] be match).
    send=None,
    # the timeout (float).
    timeout=1.0, )

```
##### read:
``` python

# call spawn.read.
response = spawn.read(
    # with await False it reads only the printed output regardless the status & never throws timeout.
    wait=False,
    # the timeout, leave None for no timeout.
    timeout=None,
    # the live boolean (bool) (prints live logs to console when enabled) (leave None to use spawn.log_level >= 1).
    live=None,
    # system variables.
    #   safe True always a response.output variable upon error the response.output is "".
    __safe__=False, )

```
##### kill:
``` python

# call spawn.kill.
response = spawn.kill()

```
##### wait:
``` python

# call spawn.wait.
_ = spawn.wait(
    # the live boolean (bool) (prints live logs to console when enabled) (leave None to use spawn.log_level >= 1).
    live=None,
    sleeptime=3,
    # the timeout (leave None to ignore).
    timeout=None, )

```
##### crashed:
``` python

# call spawn.crashed.
response = spawn.crashed()

```

#### Properties:
```python

# the expecting property.
expecting = spawn.expecting
```
```python

# the running property.
running = spawn.running
```
```python

# the exit status property.
exit_status = spawn.exit_status
```
```python

# the output property.
output = spawn.output
```

## String:
The string object class.
``` python 

# initialize the string object class.
string = String(string="")

```

#### Functions:

##### is_numerical:
``` python

# call string.is_numerical.
_ = string.is_numerical()

```
##### bash:
``` python

# call string.bash.
_ = string.bash()

```
##### identifier:
``` python

# call string.identifier.
_ = string.identifier()

```
##### variable_format:
``` python

# call string.variable_format.
_ = string.variable_format(
    exceptions={
        "smart_card":"smartcard",
        "smart_cards":"smartcards" ,
    }, )

```
##### class_format:
``` python

# call string.class_format.
_ = string.class_format()

```
##### capitalized_scentence:
``` python

# call string.capitalized_scentence.
_ = string.capitalized_scentence()

```
##### capitalized_word:
``` python

# call string.capitalized_word.
_ = string.capitalized_word()

```
##### generate:
``` python

# call string.generate.
_ = string.generate(
    # the length of the generated string.
    length=6,
    # include digits.
    digits=False,
    # include capital letters.
    capitalize=False,
    # include special characters.
    special=False, )

```
##### first_occurence:
``` python

# call string.first_occurence.
_ = string.first_occurence(charset=[" ", "\n"], reversed=False, string=None)

```
##### before_after_first_occurence:
``` python

# call string.before_after_first_occurence.
_ = string.before_after_first_occurence(slicer=" ", include=True, include_before=False, include_after=False, string=None)

```
##### before_selected_after_first_occurence:
``` python

# call string.before_selected_after_first_occurence.
_ = string.before_selected_after_first_occurence(slicer=" ", string=None)

```
##### before_after_last_occurence:
``` python

# call string.before_after_last_occurence.
_ = string.before_after_last_occurence(slicer=" ", include=True, include_before=False, include_after=False, string=None)

```
##### before_selected_after_last_occurence:
``` python

# call string.before_selected_after_last_occurence.
_ = string.before_selected_after_last_occurence(slicer=" ", string=None)

```
##### between:
``` python

# call string.between.
_ = string.between(identifiers=["{","}"], depth=1, include=True, string=None)

```
##### increase_version:
``` python

# call string.increase_version.
_ = string.increase_version()

```
##### slice_dict:
``` python

# call string.slice_dict.
_ = string.slice_dict(depth=1)

```
##### slice_array:
``` python

# call string.slice_array.
_ = string.slice_array(depth=1)

```
##### slice_tuple:
``` python

# call string.slice_tuple.
_ = string.slice_tuple(depth=1)

```
##### indent:
``` python

# call string.indent.
_ = string.indent(indent=4)

```
##### line_indent:
``` python

# call string.line_indent.
_ = string.line_indent(line="")

```
##### slice_indent:
``` python

# call string.slice_indent.
_ = string.slice_indent(indent=4, depth=1, string=None, remove_indent=True)

```
##### first:
``` python

# call string.first.
_ = string.first(count)

```
##### last:
``` python

# call string.last.
_ = string.last(count)

```
##### remove_first:
``` python

# call string.remove_first.
_ = string.remove_first(count)

```
##### remove_last:
``` python

# call string.remove_last.
_ = string.remove_last(count)

```
##### split:
``` python

# call string.split.
_ = string.split(string)

```
##### count:
``` python

# call string.count.
_ = string.count(string)

```
##### replace:
``` python

# call string.replace.
_ = string.replace(from_, to_)

```
##### lower:
``` python

# call string.lower.
_ = string.lower(string)

```
##### upper:
``` python

# call string.upper.
_ = string.upper(string)

```
##### instance:
``` python

# call string.instance.
_ = string.instance()

```
##### assign:
``` python

# call string.assign.
_ = string.assign(string)

```
##### raw:
``` python

# call string.raw.
_ = string.raw()

```

## Symbol:
The symbol object class.
``` python 

# import the symbol object class.
from dev0s import symbol

```
## Thread:
The thread object class.
``` python 

# initialize the thread object class.
thread = Thread(
    # the threads id (#1).
    id="Thread",
    # the imported traceback.
    traceback="Thread",
    # the raw traceback.
    raw_traceback="syst3m.classes.objects.Thread",
    # the threads log level.
    log_level=-1, )

```

#### Functions:

##### run:
``` python

# call thread.run.
_ = thread.run()

```
##### safe_start:
``` python

# call thread.safe_start.
response = thread.safe_start(timeout=120, sleeptime=1)

```
##### safe_stop:
``` python

# call thread.safe_stop.
response = thread.safe_stop(timeout=120, sleeptime=1)

```
##### send_stop:
``` python

# call thread.send_stop.
_ = thread.send_stop(
    # all optional.
    # option 1: the success message.
    message=None, # (1)
    args={}, # (2)
    # option 2: the error message.
    error=None,
    # option 3: the response object.
    response=None,
    # save the message/error/response.
    save=False,
    # the active log level (int) (leave None to use thread.log_level).
    log_level=None,
    # the required log level for when to print to console (leave None to use Response.log_level ; default: 0).
    required_log_level=Response.log_level, )

```
##### send_crash:
``` python

# call thread.send_crash.
_ = thread.send_crash(
    # all optional.
    # option 1: the success message.
    message=None, # (1)
    args={}, # (2)
    # option 2: the error message.
    error=None,
    # option 3: the response object.
    response=None,
    # save the message/error/response.
    save=False,
    # the active log level (int) (leave None to use thread.log_level).
    log_level=None,
    # the required log level for when to print to console (leave None to use Response.log_level ; default: 0).
    required_log_level=Response.log_level, )

```
##### log:
``` python

# call thread.log.
response = thread.log(
    # option 1:
    # the message (#1 param).
    message=None,
    # option 2:
    # the error.
    error=None,
    # option 3:
    # the response dict (leave message None to use).
    response={},
    # print the response as json.
    json=JSON,
    # optionals:
    # the active log level (leave None to use thread.log_level).
    log_level=None,
    # the required log level for when printed to console.
    required_log_level=0,
    # save to log file.
    save=False,
    # save errors always (for options 2 & 3 only).
    save_errors=None,
    # the log mode (leave None for default).
    mode=None, )

```

#### Properties:
```python

# the run permission property.
run_permission = thread.run_permission
```
```python

# the running property.
running = thread.running
```
```python

# the stopped property.
stopped = thread.stopped
```
```python

# the crashed property.
crashed = thread.crashed
```
```python

# the response property.
response = thread.response
```

## Traceback:
The traceback object class.
``` python 

# initialize the traceback object class.
traceback = Traceback(
    # the imported traceback (#1).
    traceback="Traceback",
    # the raw traceback (#2).
    raw_traceback="syst3m.classes.objects.Object", )

```
#### Properties:
```python

# the traceback property.
traceback = traceback.traceback
```

## Zip:
The zip object class.
``` python 

# initialize the zip object class.
zip = Zip(path=None, check=False)

```

#### Functions:

##### create:
``` python

# call zip.create.
_ = zip.create(
    # source can either be a string or an array.
    source=None,
    # remove the source file(s).
    remove=False,
    # sudo required to move/copy source files.
    sudo=False, )

```
##### extract:
``` python

# call zip.extract.
_ = zip.extract(
    # the base extract directory.
    base=None,
    # remove the zip after extraction.
    remove=False,
    # if sudo required for removing file path.
    sudo=False,)

```
##### instance:
``` python

# call zip.instance.
_ = zip.instance()

```
##### raw:
``` python

# call zip.raw.
_ = zip.raw()

```

## __Defaults__:
The Defaults object class.
``` python 

# import the Defaults object class.
from dev0s import Defaults

```

#### Functions:

##### operating_system:
``` python

# call Defaults.operating_system.
_ = Defaults.operating_system(supported=["*"])

```
##### alias:
``` python

# call Defaults.alias.
_ = Defaults.alias(
    # the source name.
    alias=None,
    # the source path.
    executable=None,
    # can use sudo.
    sudo=False,
    # overwrite.
    overwrite=False, )

```
##### source_path:
``` python

# call Defaults.source_path.
_ = Defaults.source_path(path, back=1)

```
##### log_level:
``` python

# call Defaults.log_level.
_ = Defaults.log_level(default=0)

```
##### pwd:
``` python

# call Defaults.pwd.
_ = Defaults.pwd()

```
##### insert:
``` python

# call Defaults.insert.
_ = Defaults.insert(path)

```
##### site_packages:
``` python

# call Defaults.site_packages.
_ = Defaults.site_packages()

```
##### install_requirements:
``` python

# call Defaults.install_requirements.
_ = Defaults.install_requirements(
    # the requirements (#1).
    #    str instance: path to file.
    #    list instance: pip requirements in list
    requirements,
    # the silent option.
    silent=False,
    # the log level (Leave None to use Defaults.options.log_level).
    log_level=None, )

```

## __Environment__:
The Environment object class.
``` python 

# import the Environment object class.
from dev0s import Environment

```

#### Functions:

##### fill:
``` python

# call Environment.fill.
_ = Environment.fill(string)

```
##### import_:
``` python

# call Environment.import_.
response = Environment.import_(env=None)

```
##### export:
``` python

# call Environment.export.
response = Environment.export(env=None, export=None)

```
##### get:
``` python

# call Environment.get.
_ = Environment.get(id, default=None, format="str")

```
##### get_string:
``` python

# call Environment.get_string.
_ = Environment.get_string(id, default=None)

```
##### get_boolean:
``` python

# call Environment.get_boolean.
_ = Environment.get_boolean(id, default=None)

```
##### get_integer:
``` python

# call Environment.get_integer.
_ = Environment.get_integer(id, default=None)

```
##### get_array:
``` python

# call Environment.get_array.
_ = Environment.get_array(id, default=None)

```
##### get_tuple:
``` python

# call Environment.get_tuple.
_ = Environment.get_tuple(id, default=None)

```
##### get_dictionary:
``` python

# call Environment.get_dictionary.
_ = Environment.get_dictionary(id, default=None)

```
##### set:
``` python

# call Environment.set.
_ = Environment.set(id, value, format="unknown")

```
##### set_string:
``` python

# call Environment.set_string.
_ = Environment.set_string(id, value)

```
##### set_boolean:
``` python

# call Environment.set_boolean.
_ = Environment.set_boolean(id, value)

```
##### set_integer:
``` python

# call Environment.set_integer.
_ = Environment.set_integer(id, value)

```
##### set_array:
``` python

# call Environment.set_array.
_ = Environment.set_array(id, value)

```
##### set_tuple:
``` python

# call Environment.set_tuple.
_ = Environment.set_tuple(id, value)

```
##### set_dictionary:
``` python

# call Environment.set_dictionary.
_ = Environment.set_dictionary(id, value, subkey="")

```

## __Response__:
The Response object class.
``` python 

# import the Response object class.
from dev0s import Response

```

#### Functions:

##### success:
``` python

# call Response.success.
_ = Response.success(
    # the message (must be param #1).
    message,
    # additional returnable functions (must be param #2).
    variables={},
    # log log level of the message (int).
    log_level=None,
    # the required log level for when printed to console (leave None to use Response.log_level).
    required_log_level=None,
    # save the error to the logs file.
    save=False,
    # return as a django JsonResponse.
    django=False, )

```
##### error:
``` python

# call Response.error.
_ = Response.error(
    # the error message.
    error="",
    # log log level of the message (int).
    log_level=None,
    # the required log level for when printed to console (leave None to use Response.log_level).
    required_log_level=None,
    # save the error to the erros file.
    save=False,
    # return as a django JsonResponse.
    django=False,
    # raise error for developer traceback.
    traceback=ERROR_TRACEBACK, )

```
##### log:
``` python

# call Response.log.
_ = Response.log(
    # option 1:
    # the message (#1 param).
    message=None,
    # option 2:
    # the error.
    error=None,
    # option 3:
    # the response dict (leave message None to use).
    response={},
    # print the response as json.
    json=False,
    # optionals:
    # the active log level.
    log_level=0,
    # the required log level for when printed to console (leave None to use Response.log_level).
    required_log_level=None,
    # save to log file.
    save=False,
    # save errors always (for options 2 & 3 only).
    save_errors=None,
    # the log mode (leave None for default).
    mode=None, )

```
##### load_logs:
``` python

# call Response.load_logs.
_ = Response.load_logs(format="webserver", options=["webserver", "cli", "array", "string"])

```
##### reset_logs:
``` python

# call Response.reset_logs.
_ = Response.reset_logs()

```
##### serialize:
``` python

# call Response.serialize.
response = Response.serialize(
    # the response (#1) (dict) (str repr of dict) (ResponseObject) (generator) .
    response={},
    # init to response object.
    init=True, )

```
##### response:
``` python

# call Response.response.
_ = Response.response(
    # the blank response (dict, str, generator) (#1).
    response={
        "success":False,
        "message":None,
        "error":None,
    }, )

```

#### argument_present:
The argument_present function.
``` python

# call argument_present.
_ = argument_present(arguments, default=False, count=1)

```
#### arguments_present:
The arguments_present function.
``` python

# call arguments_present.
_ = arguments_present(arguments, default=False, count=1)

```
#### execute:
The execute function.
``` python

# call execute.
response = execute(
    # Notes:
    #   returns a dev0s.Code.OutputObject object (very similair to ResponseObject).
    #
    # Mode:
    #   option 1:
    #     the command in str format, the command is saved to a script & then executed)

```
#### get_argument:
The get_argument function.
``` python

# call get_argument.
_ = get_argument(argument, required=True, index=1, count=1, default=None, )

```
