# fil3s
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
Default python files & formats.

# Installation:
Install the package.

	pip3 install fil3s --upgrade

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
- [__Boolean__](#boolean)
  * [convert](#convert)
  * [instance](#instance-1)
  * [assign](#assign-1)
- [__Bytes__](#bytes)
  * [load](#load-1)
  * [save](#save-1)
  * [instance](#instance-2)
  * [assign](#assign-2)
- [__Date__](#date)
  * [compare](#compare)
  * [increase](#increase)
  * [decrease](#decrease)
  * [to_seconds](#to_seconds)
  * [from_seconds](#from_seconds)
  * [convert](#convert-1)
  * [instance](#instance-3)
- [__Dictionary__](#dictionary)
  * [save](#save-2)
  * [load](#load-2)
  * [load_line](#load_line)
  * [check](#check-1)
  * [divide](#divide-1)
  * [append](#append-1)
  * [unpack](#unpack)
  * [remove](#remove-1)
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
- [__Directory__](#directory)
  * [create](#create)
  * [delete](#delete)
  * [check](#check-2)
  * [paths](#paths)
  * [names](#names)
  * [oldest_path](#oldest_path)
  * [random_path](#random_path)
  * [generate_path](#generate_path)
  * [structured_join](#structured_join)
  * [join](#join)
  * [contains](#contains)
  * [subpath](#subpath)
  * [fullpath](#fullpath)
  * [index](#index)
  * [find](#find)
  * [replace](#replace)
  * [instance](#instance-5)
- [__File__](#file)
  * [load](#load-3)
  * [load_line](#load_line-1)
  * [save](#save-3)
  * [check](#check-3)
  * [instance](#instance-6)
  * [assign](#assign-4)
- [__FilePath__](#filepath)
  * [join](#join-1)
  * [name](#name)
  * [extension](#extension)
  * [base](#base)
  * [basename](#basename)
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
  * [open](#open)
  * [create](#create-1)
  * [check](#check-4)
  * [split](#split)
  * [count](#count-2)
  * [replace](#replace-1)
  * [lower](#lower)
  * [upper](#upper)
  * [instance](#instance-7)
  * [assign](#assign-5)
- [__Files__](#files)
  * [join](#join-2)
  * [load](#load-4)
  * [save](#save-4)
  * [delete](#delete-2)
  * [chmod](#chmod)
  * [chown](#chown)
  * [exists](#exists-1)
  * [directory](#directory-1)
- [__Formats__](#formats)
  * [check](#check-5)
  * [get](#get)
  * [initialize](#initialize)
  * [denitialize](#denitialize)
- [__Image__](#image)
  * [load](#load-5)
  * [edit_pixel](#edit_pixel)
  * [instance](#instance-8)
- [__Integer__](#integer)
  * [increase_version](#increase_version)
  * [round](#round)
  * [round_down](#round_down)
  * [generate](#generate)
  * [instance](#instance-9)
  * [assign](#assign-6)
- [__Ownership__](#ownership)
  * [get](#get-1)
  * [set](#set)
  * [check](#check-6)
- [__Permission__](#permission)
  * [get](#get-2)
  * [set](#set-1)
  * [check](#check-7)
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
  * [split](#split-1)
  * [count](#count-3)
  * [replace](#replace-2)
  * [lower](#lower-1)
  * [upper](#upper-1)
  * [instance](#instance-10)
  * [assign](#assign-7)
- [__Zip__](#zip)
  * [create](#create-2)
  * [extract](#extract)
  * [instance](#instance-11)

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
_ = array.load(default=None)

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

## Boolean:
The boolean object class.
``` python 

# initialize the boolean object class.
boolean = Boolean(boolean=False)

```

#### Functions:

##### convert:
``` python

# call boolean.convert.
_ = boolean.convert(true="True", false="False")

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
_ = bytes.load()

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

## Date:
The date object class.
``` python 

# initialize the date object class.
date = Date()

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
_ = dictionary.load(default=None)

```
##### load_line:
``` python

# call dictionary.load_line.
_ = dictionary.load_line(line_number)

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
    save=False, # saves the output & and sets the output to dictionary.dictionary.
    def __iterate_dict__(dictionary, default):
        #print("\niterating new dictionary: [{}] & default [{}]\n".format(dictionary, default))
        for identifier, item in default.items():
            if isinstance(item, dict):
                try: dictionary[identifier] = __iterate_dict__(dictionary[identifier], item)
                except KeyError: dictionary[identifier] = dict(item)
            elif isinstance(item, list):
                try: dictionary[identifier]
                except KeyError: dictionary[identifier] = list(item)
            else:
                try: dictionary[identifier]
                except KeyError: dictionary[identifier] = item
        return dictionary
    # init.
    if dictionary == None: dictionary = dictionary.dictionary
    #   -   option 1:
    if key == None and value != None: raise ValueError("Define both parameters: [key & value].")
    elif value == None and key != None: raise ValueError("Define both parameters: [key & value].")
    if key != None and value != None:
        try: dictionary[key]
        except KeyError: dictionary[key] = value
        return dictionary
    #   -   option 2:
    if default == None: default = dictionary.default
    if default == None: raise ValueError("Define both parameters: [key & value] or parameter [default].")
    dictionary = __iterate_dict__(dictionary, default)
    if save:
        dictionary.dictionary = dictionary
        dictionary.save()
    return dictionary

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
##### join:
``` python

# call directory.join.
_ = directory.join(name=None, type="")

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
##### instance:
``` python

# call directory.instance.
_ = directory.instance()

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
_ = file.load(default=None)

```
##### load_line:
``` python

# call file.load_line.
_ = file.load_line(line_number, default=None)

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
_ = file_path.name(remove_extension=False, path=None)

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
_ = files.join(path=None, name=None, type="")

```
##### load:
``` python

# call files.load.
_ = files.load(path, data="not to be used", format="str", raw=False)

```
##### save:
``` python

# call files.save.
_ = files.save(path, data, format="str", sudo=False, indent=4, ensure_ascii=False)

```
##### delete:
``` python

# call files.delete.
_ = files.delete(
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
_ = files.chmod(
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
_ = files.chown(
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
_ = files.exists(path=None, sudo=False)

```
##### directory:
``` python

# call files.directory.
_ = files.directory(
    # the path (leave None to use files.path) (#1).
    path=None, )

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
_ = formats.check(
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
_ = formats.get(value, serialize=False)

```
##### initialize:
``` python

# call formats.initialize.
_ = formats.initialize(
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
_ = formats.denitialize(
    # the object / value (#1 param).
    obj=None,
    # list / dict with objects.
    objects=None,
    # initialize file paths.
    file_paths=True, )

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
_ = ownership.set(owner=None, group=None, sudo=False, recursive=False, silent=False, path=None)

```
##### check:
``` python

# call ownership.check.
_ = ownership.check(owner=None, group=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

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
_ = permission.set(permission=None, sudo=False, recursive=False, silent=False, path=None)

```
##### check:
``` python

# call permission.check.
_ = permission.check(permission=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

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

