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
- [__AES__](#aes)
  * [encrypt](#encrypt)
  * [decrypt](#decrypt)
  * [get_key](#get_key)
  * [generate_salt](#generate_salt)
- [__Agent__](#agent)
  * [generate](#generate)
  * [activate](#activate)
  * [encrypt](#encrypt-1)
  * [decrypt](#decrypt-1)
  * [activated](#properties)
- [__Array__](#array)
  * [load](#load)
  * [save](#save)
- [__AsymmetricAES__](#asymmetricaes)
  * [generate_keys](#generate_keys)
  * [edit_passphrase](#edit_passphrase)
  * [load_keys](#load_keys)
  * [load_private_key](#load_private_key)
  * [load_public_key](#load_public_key)
  * [encrypt](#encrypt-2)
  * [decrypt](#decrypt-2)
  * [encrypt_file](#encrypt_file)
  * [decrypt_file](#decrypt_file)
  * [encrypt_directory](#encrypt_directory)
  * [decrypt_directory](#decrypt_directory)
  * [activated](#properties-1)
- [__Boolean__](#boolean)
  * [string](#string)
  * [instance](#instance)
  * [assign](#assign)
  * [raw](#raw)
- [__Browser__](#browser)
  * [get](#get)
  * [get_element](#get_element)
- [__Bytes__](#bytes)
  * [load](#load-1)
  * [save](#save-1)
  * [instance](#instance-1)
  * [assign](#assign-1)
  * [raw](#raw-1)
- [__CLI__](#cli)
  * [stop](#stop)
  * [docs](#docs)
  * [invalid](#invalid)
- [__Color__](#color)
  * [remove](#remove)
  * [fill](#fill)
  * [boolean](#boolean)
- [__Database__](#database)
  * [activate](#activate-1)
  * [check](#check)
  * [load](#load-2)
  * [save](#save-2)
  * [activated](#properties-2)
- [__Date__](#date)
  * [compare](#compare)
  * [increase](#increase)
  * [decrease](#decrease)
  * [to_seconds](#to_seconds)
  * [from_seconds](#from_seconds)
  * [convert](#convert)
  * [instance](#instance-2)
- [__Defaults__](#defaults)
  * [operating_system](#operating_system)
  * [alias](#alias)
  * [source_path](#source_path)
  * [log_level](#log_level)
  * [pwd](#pwd)
  * [insert](#insert)
  * [site_packages](#site_packages)
  * [install_requirements](#install_requirements)
  * [interactive](#interactive)
- [__Dictionary__](#dictionary)
  * [load](#load-3)
  * [save](#save-3)
- [__Directory__](#directory)
  * [create](#create)
  * [delete](#delete)
  * [check](#check-1)
  * [load](#load-4)
  * [save](#save-4)
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
  * [instance](#instance-3)
  * [raw](#raw-2)
- [__Disks__](#disks)
  * [list](#list)
  * [erase](#erase)
  * [partition](#partition)
  * [format](#format)
  * [mount](#mount)
  * [unmount](#unmount)
- [__Docs__](#docs)
- [__Encryption__](#encryption)
- [__Env__](#env)
  * [fill](#fill-1)
  * [import_](#import_)
  * [export](#export)
  * [get](#get-1)
  * [get_string](#get_string)
  * [get_boolean](#get_boolean)
  * [get_integer](#get_integer)
  * [get_array](#get_array)
  * [get_tuple](#get_tuple)
  * [get_dictionary](#get_dictionary)
  * [set](#set)
  * [set_string](#set_string)
  * [set_boolean](#set_boolean)
  * [set_integer](#set_integer)
  * [set_array](#set_array)
  * [set_tuple](#set_tuple)
  * [set_dictionary](#set_dictionary)
- [__File__](#file)
  * [load](#load-5)
  * [save](#save-5)
- [__FilePath__](#filepath)
  * [join](#join-1)
  * [name](#name-1)
  * [extension](#extension)
  * [base](#base-1)
  * [basename](#basename-1)
  * [size](#size)
  * [exists](#exists)
  * [mount](#mount-1)
  * [directory](#directory)
  * [mtime](#mtime)
  * [clean](#clean)
  * [absolute](#absolute)
  * [module](#module)
  * [requirements](#requirements)
  * [delete](#delete-1)
  * [move](#move)
  * [copy](#copy)
  * [open](#open-1)
  * [create](#create-1)
  * [check](#check-2)
  * [split](#split)
  * [count](#count)
  * [replace](#replace-1)
  * [lower](#lower)
  * [upper](#upper)
  * [instance](#instance-4)
  * [assign](#assign-2)
  * [raw](#raw-3)
- [__Files__](#files)
  * [join](#join-2)
  * [load](#load-6)
  * [save](#save-6)
  * [delete](#delete-2)
  * [chmod](#chmod)
  * [chown](#chown)
  * [exists](#exists-1)
  * [directory](#directory-1)
  * [mounted](#mounted)
  * [create](#create-2)
  * [copy](#copy-1)
  * [move](#move-1)
- [__FireWall__](#firewall)
  * [enable](#enable)
  * [disable](#disable)
  * [allow](#allow)
  * [deny](#deny)
  * [allow_all](#allow_all)
  * [deny_all](#deny_all)
  * [set_default](#set_default)
  * [info](#info)
- [__Formats__](#formats)
  * [check](#check-3)
  * [get](#get-2)
  * [initialize](#initialize)
  * [denitialize](#denitialize)
- [__Generate__](#generate)
  * [int](#int)
  * [string](#string-1)
- [__Group__](#group)
  * [create](#create-3)
  * [delete](#delete-3)
  * [check](#check-4)
  * [list_users](#list_users)
  * [delete_users](#delete_users)
  * [add_users](#add_users)
  * [check_users](#check_users)
- [__Image__](#image)
  * [load](#load-7)
  * [edit_pixel](#edit_pixel)
  * [convert](#convert-1)
  * [replace_pixels](#replace_pixels)
  * [replace_colors](#replace_colors)
  * [rgb_to_hex](#rgb_to_hex)
  * [hex_to_rgb](#hex_to_rgb)
  * [instance](#instance-5)
  * [raw](#raw-4)
- [__Integer__](#integer)
  * [increase_version](#increase_version)
  * [round](#round)
  * [round_down](#round_down)
  * [generate](#generate-1)
  * [instance](#instance-6)
  * [assign](#assign-3)
  * [raw](#raw-5)
- [__Loader__](#loader)
  * [run](#run)
  * [stop](#stop-1)
  * [mark](#mark)
  * [hold](#hold)
  * [release](#release)
- [__Network__](#network)
  * [info](#info-1)
  * [convert_dns](#convert_dns)
  * [ping](#ping)
  * [port_in_use](#port_in_use)
  * [free_port](#free_port)
- [__Object__](#object)
  * [items](#items)
  * [keys](#keys)
  * [values](#values)
  * [assign](#assign-4)
  * [attributes](#attributes)
  * [dict](#dict)
  * [unpack](#unpack)
- [__OutputObject__](#outputobject)
  * [instance](#instance-7)
  * [response](#response)
- [__Ownership__](#ownership)
  * [get](#get-3)
  * [set](#set-1)
  * [check](#check-5)
- [__Parameters__](#parameters)
  * [get](#get-4)
  * [check](#check-6)
- [__Permission__](#permission)
  * [get](#get-5)
  * [set](#set-2)
  * [check](#check-7)
- [__ProgressLoader__](#progressloader)
  * [next](#next)
  * [stop](#stop-2)
- [__RSA__](#rsa)
  * [generate_keys](#generate_keys-1)
  * [load_keys](#load_keys-1)
  * [load_public_key](#load_public_key-1)
  * [load_private_key](#load_private_key-1)
  * [edit_passphrase](#edit_passphrase-1)
  * [encrypt_string](#encrypt_string)
  * [encrypt_file](#encrypt_file-1)
  * [encrypt_directory](#encrypt_directory-1)
  * [decrypt_string](#decrypt_string)
  * [decrypt_file](#decrypt_file-1)
  * [decrypt_directory](#decrypt_directory-1)
  * [activated](#properties-3)
- [__Requests__](#requests)
  * [encode](#encode)
  * [get](#get-6)
- [__Response__](#response)
  * [success](#success)
  * [error](#error)
  * [log](#log)
  * [load_logs](#load_logs)
  * [reset_logs](#reset_logs)
  * [serialize](#serialize)
  * [response](#response-1)
  * [log_to_file](#log_to_file)
- [__ResponseObject__](#responseobject)
  * [clean](#clean-1)
  * [assign](#assign-5)
  * [crash](#crash)
  * [unpack](#unpack-1)
  * [remove](#remove-1)
  * [iterate](#iterate)
  * [items](#items-1)
  * [keys](#keys-1)
  * [values](#values-1)
  * [reversed](#reversed)
  * [sort](#sort)
  * [dict](#dict-1)
  * [json](#json)
  * [serialize](#serialize-1)
  * [instance](#instance-8)
  * [raw](#raw-6)
  * [response](#response-2)
- [__RestAPI__](#restapi)
  * [request](#request)
- [__Service__](#service)
  * [create](#create-4)
  * [check](#check-8)
  * [delete](#delete-4)
  * [start](#start)
  * [stop](#stop-3)
  * [restart](#restart)
  * [status](#status)
  * [reset_logs](#reset_logs-1)
  * [tail](#tail)
- [__Spawn__](#spawn)
  * [start](#start-1)
  * [expect](#expect)
  * [read](#read)
  * [kill](#kill)
  * [wait](#wait)
  * [crashed](#crashed)
  * [expecting](#properties-4)
- [__String__](#string)
  * [is_numerical](#is_numerical)
  * [bash](#bash)
  * [identifier](#identifier)
  * [variable_format](#variable_format)
  * [class_format](#class_format)
  * [capitalized_scentence](#capitalized_scentence)
  * [capitalized_word](#capitalized_word)
  * [generate](#generate-2)
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
  * [count](#count-1)
  * [replace](#replace-2)
  * [lower](#lower-1)
  * [upper](#upper-1)
  * [instance](#instance-9)
  * [assign](#assign-6)
  * [raw](#raw-7)
- [__Symbol__](#symbol)
- [__System__](#system)
- [__Thread__](#thread)
  * [run](#run-1)
  * [safe_start](#safe_start)
  * [safe_stop](#safe_stop)
  * [send_stop](#send_stop)
  * [send_crash](#send_crash)
  * [log](#log-1)
  * [run_permission](#properties-5)
- [__Traceback__](#traceback)
  * [traceback](#properties-6)
- [__UnixManager__](#unixmanager)
- [__User__](#user)
  * [create](#create-5)
  * [delete](#delete-5)
  * [check](#check-9)
  * [set_password](#set_password)
  * [add_groups](#add_groups)
  * [delete_groups](#delete_groups)
- [__WebServer__](#webserver)
  * [set](#set-3)
  * [get](#get-7)
  * [app](#app)
  * [run](#run-2)
  * [fork](#fork)
  * [stop](#stop-4)
  * [start_thread](#start_thread)
  * [get_thread](#get_thread)
  * [token](#properties-7)
- [__Zip__](#zip)
  * [create](#create-6)
  * [extract](#extract)
  * [instance](#instance-10)
  * [raw](#raw-8)

## AES:
The aes object class.
``` python 

# initialize the dev0s.encryption.AES object class.
aes = dev0s.encryption.AES(passphrase=None)

```

#### Functions:

##### encrypt:
``` python

# call dev0s.encryption.AES.encrypt.
_ = dev0s.encryption.AES.encrypt(raw)

```
##### decrypt:
``` python

# call dev0s.encryption.AES.decrypt.
_ = dev0s.encryption.AES.decrypt(enc)

```
##### get_key:
``` python

# call dev0s.encryption.AES.get_key.
_ = dev0s.encryption.AES.get_key(salt=None)

```
##### generate_salt:
``` python

# call dev0s.encryption.AES.generate_salt.
_ = dev0s.encryption.AES.generate_salt()

```

## Agent:
The agent object class.
``` python 

# initialize the dev0s.encryption.Agent object class.
agent = dev0s.encryption.Agent(
    # the encryption & webserver's id (str).
    id="dev0s-agent",
    # the path to the encrypted database (str, String, FilePath).
    database=None,
    # the webserver's host (str).
    host="127.0.0.1",
    # the webserver's port (int).
    port=56000,
    # the path to the private key / the raw private key (str).
    private_key=None,
    # the path to the public key / the raw public key (str).
    public_key=None,
    # the passphrase (optional to prompt) (str).
    passphrase=None,
    # the encryption key in memory only (enable when you passed the private_key & public_key in raw format and the file path) (bool).
    memory=False,
    # the interactive mode (prompt for password) (bool).
    interactive=True,
    # the object traceback (str).
    traceback="dev0s.encryption.Agent", )

```

#### Functions:

##### generate:
``` python

# call dev0s.encryption.Agent.generate.
_ = dev0s.encryption.Agent.generate(
    # the passphrase (optional to prompt) (str).
    passphrase=None,
    # the verify passphrase (optional).
    verify_passphrase=None,
    # interactive (optional).
    interactive=None )

```
##### activate:
``` python

# call dev0s.encryption.Agent.activate.
_ = dev0s.encryption.Agent.activate(
    # the key's passphrase (optional to retrieve from webserver) (str).
    passphrase=None,
    # interactive (optional)
    interactive=None, )

```
##### encrypt:
``` python

# call dev0s.encryption.Agent.encrypt.
_ = dev0s.encryption.Agent.encrypt(string, decode=False)

```
##### decrypt:
``` python

# call dev0s.encryption.Agent.decrypt.
_ = dev0s.encryption.Agent.decrypt(string, decode=False)

```

#### Properties:
```python

# the encryption property.
encryption = dev0s.encryption.Agent.activated
```
```python

# the encryption property.
encryption = dev0s.encryption.Agent.public_key_activated
```
```python

# the encryption property.
encryption = dev0s.encryption.Agent.private_key_activated
```
```python

# the encryption property.
encryption = dev0s.encryption.Agent.generated
```

## Array:
The array object class.
``` python 

# initialize the Array object class.
array = Array(
    # the path.
    path=None,
    # the default data, specify to call array.check() automatically.
    default=None,
    # the aes object.
    aes=None, )

```

#### Functions:

##### load:
``` python

# call Array.load.
_ = Array.load()

```
##### save:
``` python

# call Array.save.
_ = Array.save()

```

## AsymmetricAES:
The asymmetricaes object class.
``` python 

# initialize the dev0s.encryption.AsymmetricAES object class.
asymmetricaes = dev0s.encryption.AsymmetricAES(
    # the public key (str).
    public_key=None,
    # the private key (str).
    private_key=None,
    # the key passphrase (str / null).
    passphrase=None,
    # enable memory when the keys are not saved.
    memory=False, )

```

#### Functions:

##### generate_keys:
``` python

# call dev0s.encryption.AsymmetricAES.generate_keys.
_ = dev0s.encryption.AsymmetricAES.generate_keys()

```
##### edit_passphrase:
``` python

# call dev0s.encryption.AsymmetricAES.edit_passphrase.
_ = dev0s.encryption.AsymmetricAES.edit_passphrase(passphrase=None)

```
##### load_keys:
``` python

# call dev0s.encryption.AsymmetricAES.load_keys.
_ = dev0s.encryption.AsymmetricAES.load_keys()

```
##### load_private_key:
``` python

# call dev0s.encryption.AsymmetricAES.load_private_key.
_ = dev0s.encryption.AsymmetricAES.load_private_key()

```
##### load_public_key:
``` python

# call dev0s.encryption.AsymmetricAES.load_public_key.
_ = dev0s.encryption.AsymmetricAES.load_public_key()

```
##### encrypt:
``` python

# call dev0s.encryption.AsymmetricAES.encrypt.
_ = dev0s.encryption.AsymmetricAES.encrypt(string, decode=False)

```
##### decrypt:
``` python

# call dev0s.encryption.AsymmetricAES.decrypt.
_ = dev0s.encryption.AsymmetricAES.decrypt(string, decode=False)

```
##### encrypt_file:
``` python

# call dev0s.encryption.AsymmetricAES.encrypt_file.
_ = dev0s.encryption.AsymmetricAES.encrypt_file(input=None, output=None, remove=False, base64_encoding=False)

```
##### decrypt_file:
``` python

# call dev0s.encryption.AsymmetricAES.decrypt_file.
_ = dev0s.encryption.AsymmetricAES.decrypt_file(input=None, output=None, remove=False, base64_encoding=False)

```
##### encrypt_directory:
``` python

# call dev0s.encryption.AsymmetricAES.encrypt_directory.
_ = dev0s.encryption.AsymmetricAES.encrypt_directory(input=None, output=None, remove=False)

```
##### decrypt_directory:
``` python

# call dev0s.encryption.AsymmetricAES.decrypt_directory.
_ = dev0s.encryption.AsymmetricAES.decrypt_directory(input=None, output=None, remove=False)

```

#### Properties:
```python

# the encryption property.
encryption = dev0s.encryption.AsymmetricAES.activated
```
```python

# the encryption property.
encryption = dev0s.encryption.AsymmetricAES.public_key_activated
```
```python

# the encryption property.
encryption = dev0s.encryption.AsymmetricAES.private_key_activated
```

## Boolean:
The boolean object class.
``` python 

# initialize the Boolean object class.
boolean = Boolean(boolean=False)

```

#### Functions:

##### string:
``` python

# call Boolean.string.
_ = Boolean.string(true="True", false="False")

```
##### instance:
``` python

# call Boolean.instance.
_ = Boolean.instance()

```
##### assign:
``` python

# call Boolean.assign.
_ = Boolean.assign(boolean)

```
##### raw:
``` python

# call Boolean.raw.
_ = Boolean.raw()

```

## Browser:
The browser object class.
``` python 

# initialize the dev0s.system.Browser object class.
browser = dev0s.system.Browser(
    # the driver.
    driver="chromedriver", )

```

#### Functions:

##### get:
``` python

# call dev0s.system.Browser.get.
_ = dev0s.system.Browser.get(url)

```
##### get_element:
``` python

# call dev0s.system.Browser.get_element.
_ = dev0s.system.Browser.get_element(
    # the element type.
    element="input",
    # the attribute name.
    attribute="name",
    # the attributes value.
    value="username",
    # the parent element (default is browser.driver).
    parent=None, )

```

## Bytes:
The bytes object class.
``` python 

# initialize the Bytes object class.
bytes = Bytes(
    # the bytes (param #1).
    data=b"",
    # the file path.
    path=None, )

```

#### Functions:

##### load:
``` python

# call Bytes.load.
_ = Bytes.load(sudo=False)

```
##### save:
``` python

# call Bytes.save.
_ = Bytes.save(bytes=None, sudo=False)

```
##### instance:
``` python

# call Bytes.instance.
_ = Bytes.instance()

```
##### assign:
``` python

# call Bytes.assign.
_ = Bytes.assign(b)

```
##### raw:
``` python

# call Bytes.raw.
_ = Bytes.raw()

```

## CLI:
The cli object class.
``` python 

# initialize the CLI object class.
cli = CLI(alias=None, modes={}, options={}, notes={}, executable=__file__, author="Daan van den Bergh")

```

#### Functions:

##### stop:
``` python

# call CLI.stop.
_ = CLI.stop(
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

# call CLI.docs.
_ = CLI.docs(
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

# call CLI.invalid.
_ = CLI.invalid(error="Selected an invalid mode.", chapter=None, mode=None, json=False)

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

## Database:
The database object class.
``` python 

# initialize the dev0s.encryption.Database object class.
database = dev0s.encryption.Database(
    # the aes object class.
    aes=None,
    # the root path of the database.
    path=None, )

```

#### Functions:

##### activate:
``` python

# call dev0s.encryption.Database.activate.
_ = dev0s.encryption.Database.activate(
    # the key;s passphrase (optional).
    passphrase=None, )

```
##### check:
``` python

# call dev0s.encryption.Database.check.
_ = dev0s.encryption.Database.check(
    # the subpath of the content (! param number 1).
    path=None,
    # the default content data (! param number 2).
    default=None,
    # save the changes.
    save=True, )

```
##### load:
``` python

# call dev0s.encryption.Database.load.
_ = dev0s.encryption.Database.load(
    # the subpath of the content (! param number 1).
    path=None,
    # the default data, specify to call database.check() automatically on the data object.
    default=None, )

```
##### save:
``` python

# call dev0s.encryption.Database.save.
_ = dev0s.encryption.Database.save(
    # the content object (! param number 1).
    content=None, )

```

#### Properties:
```python

# the encryption property.
encryption = dev0s.encryption.Database.activated
```
```python

# the encryption property.
encryption = dev0s.encryption.Database.public_key_activated
```
```python

# the encryption property.
encryption = dev0s.encryption.Database.private_key_activated
```

## Date:
The date object class.
``` python 

# initialize the Date object class.
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

# call Date.compare.
_ = Date.compare(comparison=None, current=None, format="%d-%m-%y %H:%M")

```
##### increase:
``` python

# call Date.increase.
_ = Date.increase(string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M")

```
##### decrease:
``` python

# call Date.decrease.
_ = Date.decrease(string, weeks=0, days=0, hours=0, minutes=0, seconds=0, format="%d-%m-%y %H:%M")

```
##### to_seconds:
``` python

# call Date.to_seconds.
_ = Date.to_seconds(string, format="%d-%m-%y %H:%M")

```
##### from_seconds:
``` python

# call Date.from_seconds.
_ = Date.from_seconds(seconds, format="%d-%m-%y %H:%M")

```
##### convert:
``` python

# call Date.convert.
_ = Date.convert(string, input="%d-%m-%y %H:%M", output="%Y%m%d")

```
##### instance:
``` python

# call Date.instance.
_ = Date.instance()

```

## Defaults:
The defaults object class.
``` python 

# import the dev0s.defaults object class.
from dev0s import dev0s

```

#### Functions:

##### operating_system:
``` python

# call dev0s.defaults.operating_system.
_ = dev0s.defaults.operating_system(supported=["*"])

```
##### alias:
``` python

# call dev0s.defaults.alias.
_ = dev0s.defaults.alias(
    # the source name.
    alias=None,
    # the source path.
    executable=None,
    # can use sudo.
    sudo=False,
    # overwrite.
    overwrite=False,
    # the venv path (leave None to ignore).
    venv=None, )

```
##### source_path:
``` python

# call dev0s.defaults.source_path.
_ = dev0s.defaults.source_path(path, back=1)

```
##### log_level:
``` python

# call dev0s.defaults.log_level.
_ = dev0s.defaults.log_level(default=0)

```
##### pwd:
``` python

# call dev0s.defaults.pwd.
_ = dev0s.defaults.pwd()

```
##### insert:
``` python

# call dev0s.defaults.insert.
_ = dev0s.defaults.insert(path)

```
##### site_packages:
``` python

# call dev0s.defaults.site_packages.
_ = dev0s.defaults.site_packages()

```
##### install_requirements:
``` python

# call dev0s.defaults.install_requirements.
_ = dev0s.defaults.install_requirements(
    # the requirements (#1).
    #    str instance: path to file.
    #    list instance: pip requirements in list
    requirements,
    # the silent option.
    silent=False,
    # the log level (Leave None to use defaults.options.log_level).
    log_level=None, )

```
##### interactive:
``` python

# call dev0s.defaults.interactive.
_ = dev0s.defaults.interactive(default=False)

```

## Dictionary:
The dictionary object class.
``` python 

# initialize the Dictionary object class.
dictionary = Dictionary(
    # the path.
    path=None,
    # the default data, specify to call dictionary.check() automatically.
    default=None,
    # the aes object.
    aes=None, )

```

#### Functions:

##### load:
``` python

# call Dictionary.load.
_ = Dictionary.load()

```
##### save:
``` python

# call Dictionary.save.
_ = Dictionary.save()

```

## Directory:
The directory object class.
``` python 

# initialize the Directory object class.
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

# call Directory.create.
_ = Directory.create(file_paths=[], path=None, sudo=False, owner=None, group=None, permission=None)

```
##### delete:
``` python

# call Directory.delete.
_ = Directory.delete(forced=False)

```
##### check:
``` python

# call Directory.check.
_ = Directory.check(
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

# call Directory.load.
_ = Directory.load(path=None, format=str, default=None, sudo=False)

```
##### save:
``` python

# call Directory.save.
_ = Directory.save(path=None, data=None, format=str, sudo=False)

```
##### paths:
``` python

# call Directory.paths.
_ = Directory.paths(dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], banned_basenames=["__pycache__"], extensions=["*"])

```
##### names:
``` python

# call Directory.names.
_ = Directory.names(dirs_only=False, files_only=False, empty_dirs=True, recursive=False, path=None, banned=[], banned_names=[".DS_Store"], extensions=["*"], remove_extensions=False)

```
##### oldest_path:
``` python

# call Directory.oldest_path.
_ = Directory.oldest_path()

```
##### random_path:
``` python

# call Directory.random_path.
_ = Directory.random_path()

```
##### generate_path:
``` python

# call Directory.generate_path.
_ = Directory.generate_path(length=24, type="/")

```
##### structured_join:
``` python

# call Directory.structured_join.
_ = Directory.structured_join(name, type="", structure="alphabetical", create_base=False, sudo=False, owner=None, group=None, permission=None)

```
##### contains:
``` python

# call Directory.contains.
_ = Directory.contains(name=None, type="/", recursive=False)

```
##### subpath:
``` python

# call Directory.subpath.
_ = Directory.subpath(fullpath)

```
##### fullpath:
``` python

# call Directory.fullpath.
_ = Directory.fullpath(subpath)

```
##### set_icon:
``` python

# call Directory.set_icon.
_ = Directory.set_icon(
    # the path to the .png / .jpg icon.
    icon=None,
    # the directory path (leave None to use directory.fp.path).
    path=None, )

```
##### index:
``` python

# call Directory.index.
_ = Directory.index(
    # the wanted options.
    metrics=[],
    options=["size", "mtime", "content", "name", "basename", "extension", "mount", "directory"],
    # optional path (leave None to use directory.path).
    path=None, )

```
##### open:
``` python

# call Directory.open.
_ = Directory.open(path=None, sudo=False)

```
##### find:
``` python

# call Directory.find.
_ = Directory.find(matches:list, path=None, recursive=False, log_level=0)

```
##### replace:
``` python

# call Directory.replace.
_ = Directory.replace(replacements:list, path=None, recursive=False, log_level=0)

```
##### join:
``` python

# call Directory.join.
_ = Directory.join(name=None, type="")

```
##### name:
``` python

# call Directory.name.
_ = Directory.name()

```
##### base:
``` python

# call Directory.base.
_ = Directory.base()

```
##### basename:
``` python

# call Directory.basename.
_ = Directory.basename()

```
##### instance:
``` python

# call Directory.instance.
_ = Directory.instance()

```
##### raw:
``` python

# call Directory.raw.
_ = Directory.raw()

```

## Disks:
The disks object class.
``` python 

# import the dev0s.system.disks object class.
from dev0s import dev0s

```

#### Functions:

##### list:
``` python

# call dev0s.system.disks.list.
_ = dev0s.system.disks.list()

```
##### erase:
``` python

# call dev0s.system.disks.erase.
_ = dev0s.system.disks.erase(
    # the device without partition number (/dev/sdb).
    device=None, )

```
##### partition:
``` python

# call dev0s.system.disks.partition.
_ = dev0s.system.disks.partition(
    # the device without partition number (/dev/sdb).
    device=None, )

```
##### format:
``` python

# call dev0s.system.disks.format.
_ = dev0s.system.disks.format(
    # the device with partition number (/dev/sdb1).
    device=None,
    # the assigned label (name).
    label=None, )

```
##### mount:
``` python

# call dev0s.system.disks.mount.
_ = dev0s.system.disks.mount(
    # the device with partition number (/dev/sdb1).
    device=None,
    # the mountpoint path.
    path=None, )

```
##### unmount:
``` python

# call dev0s.system.disks.unmount.
_ = dev0s.system.disks.unmount(
    # the mountpoint path.
    path=None, )

```

## Docs:
The docs object class.
``` python 

# initialize the Docs object class.
docs = Docs(
    # boolean inidicating if the object is initialized by default.
    initialized=True,
    # the full module path in import style (when initializing).
    module="dec0s.Docs",
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
## Encryption:
The encryption object class.
``` python 

# initialize the Encryption object class.
encryption = Encryption

```
## Env:
The env object class.
``` python 

# import the dev0s.system.env object class.
from dev0s import dev0s

```

#### Functions:

##### fill:
``` python

# call dev0s.system.env.fill.
_ = dev0s.system.env.fill(string)

```
##### import_:
``` python

# call dev0s.system.env.import_.
_ = dev0s.system.env.import_(env=None)

```
##### export:
``` python

# call dev0s.system.env.export.
_ = dev0s.system.env.export(
    # the environment to export (dict).
    env=None,
    # the export path (str) or paths (list).
    # the paths must have .json / .sh extension or be named 'json' / 'bash' when parameter [format] is undefined.
    export=None,
    # the export format (str) (leave None to be detected by parameter [export]).
    format=None, )

```
##### get:
``` python

# call dev0s.system.env.get.
_ = dev0s.system.env.get(id, default=None, format="str")

```
##### get_string:
``` python

# call dev0s.system.env.get_string.
_ = dev0s.system.env.get_string(id, default=None)

```
##### get_boolean:
``` python

# call dev0s.system.env.get_boolean.
_ = dev0s.system.env.get_boolean(id, default=None)

```
##### get_integer:
``` python

# call dev0s.system.env.get_integer.
_ = dev0s.system.env.get_integer(id, default=None)

```
##### get_array:
``` python

# call dev0s.system.env.get_array.
_ = dev0s.system.env.get_array(id, default=None)

```
##### get_tuple:
``` python

# call dev0s.system.env.get_tuple.
_ = dev0s.system.env.get_tuple(id, default=None)

```
##### get_dictionary:
``` python

# call dev0s.system.env.get_dictionary.
_ = dev0s.system.env.get_dictionary(id, default=None)

```
##### set:
``` python

# call dev0s.system.env.set.
_ = dev0s.system.env.set(id, value, format="unknown")

```
##### set_string:
``` python

# call dev0s.system.env.set_string.
_ = dev0s.system.env.set_string(id, value)

```
##### set_boolean:
``` python

# call dev0s.system.env.set_boolean.
_ = dev0s.system.env.set_boolean(id, value)

```
##### set_integer:
``` python

# call dev0s.system.env.set_integer.
_ = dev0s.system.env.set_integer(id, value)

```
##### set_array:
``` python

# call dev0s.system.env.set_array.
_ = dev0s.system.env.set_array(id, value)

```
##### set_tuple:
``` python

# call dev0s.system.env.set_tuple.
_ = dev0s.system.env.set_tuple(id, value)

```
##### set_dictionary:
``` python

# call dev0s.system.env.set_dictionary.
_ = dev0s.system.env.set_dictionary(id, value, subkey="")

```

## File:
The file object class.
``` python 

# initialize the File object class.
file = File(
    # the path.
    path=None,
    # the default data, specify to call file.check() automatically.
    default=None,
    # the aes object.
    aes=None, )

```

#### Functions:

##### load:
``` python

# call File.load.
_ = File.load()

```
##### save:
``` python

# call File.save.
_ = File.save()

```

## FilePath:
The file_path object class.
``` python 

# initialize the FilePath object class.
file_path = FilePath(path, default=False, check=False, load=False)

```

#### Functions:

##### join:
``` python

# call FilePath.join.
_ = FilePath.join(name=None, type="/")

```
##### name:
``` python

# call FilePath.name.
_ = FilePath.name(path=None, remove_extension=False,)

```
##### extension:
``` python

# call FilePath.extension.
_ = FilePath.extension(name=None, path=None)

```
##### base:
``` python

# call FilePath.base.
_ = FilePath.base(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the dirs back.
    back=1, )

```
##### basename:
``` python

# call FilePath.basename.
_ = FilePath.basename(back=1, path=None)

```
##### size:
``` python

# call FilePath.size.
_ = FilePath.size(mode="auto", options=["auto", "bytes", "kb", "mb", "gb", "tb"], format=str, path=None)

```
##### exists:
``` python

# call FilePath.exists.
_ = FilePath.exists(
    # the path (leave None to use file_path.path) (#1).
    path=None,
    # root permission required.
    sudo=False, )

```
##### mount:
``` python

# call FilePath.mount.
_ = FilePath.mount(
    # the path (leave None to use file_path.path) (#1).
    path=None, )

```
##### directory:
``` python

# call FilePath.directory.
_ = FilePath.directory(
    # the path (leave None to use file_path.path) (#1).
    path=None, )

```
##### mtime:
``` python

# call FilePath.mtime.
_ = FilePath.mtime(format='%d-%m-%y %H:%M.%S', path=None)

```
##### clean:
``` python

# call FilePath.clean.
_ = FilePath.clean(
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

# call FilePath.absolute.
_ = FilePath.absolute(
    # the path (leave None to use file_path.path) (param #1).
    path=None, )

```
##### module:
``` python

# call FilePath.module.
_ = FilePath.module(path=None)

```
##### requirements:
``` python

# call FilePath.requirements.
_ = FilePath.requirements(path=None, format="pip", include_version=True)

```
##### delete:
``` python

# call FilePath.delete.
_ = FilePath.delete(
    # the path (leave None to use file_path.path) (param #1).
    path=None,
    # the options.
    forced=False,
    sudo=False,
    silent=False, )

```
##### move:
``` python

# call FilePath.move.
_ = FilePath.move(path=None, sudo=False, silent=False)

```
##### copy:
``` python

# call FilePath.copy.
_ = FilePath.copy(path=None, sudo=False, silent=False)

```
##### open:
``` python

# call FilePath.open.
_ = FilePath.open(sudo=False)

```
##### create:
``` python

# call FilePath.create.
_ = FilePath.create(
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

# call FilePath.check.
_ = FilePath.check(
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

# call FilePath.split.
_ = FilePath.split(path)

```
##### count:
``` python

# call FilePath.count.
_ = FilePath.count(path)

```
##### replace:
``` python

# call FilePath.replace.
_ = FilePath.replace(from_, to_)

```
##### lower:
``` python

# call FilePath.lower.
_ = FilePath.lower(path)

```
##### upper:
``` python

# call FilePath.upper.
_ = FilePath.upper(path)

```
##### instance:
``` python

# call FilePath.instance.
_ = FilePath.instance()

```
##### assign:
``` python

# call FilePath.assign.
_ = FilePath.assign(path, load=False)

```
##### raw:
``` python

# call FilePath.raw.
_ = FilePath.raw()

```

## Files:
The files object class.
``` python 

# initialize the Files object class.
files = Files(path=None, name=None, type="")

```

#### Functions:

##### join:
``` python

# call Files.join.
_ = Files.join(path=None, name=None, type="")

```
##### load:
``` python

# call Files.load.
_ = Files.load(path, data="not to be used", format="str", raw=False, sudo=False)

```
##### save:
``` python

# call Files.save.
_ = Files.save(
    # the path (str) (#1).
    path,
    # the data (str, dict, list) (#2).
    data,
    # the file format, options: [str, bytes, json].
    format="str",
    # root permission required.
    sudo=False,
    # json options.
    indent=4,
    ensure_ascii=False,
    # create backups.
    backups=False,
    # warning: safe True keeps infinitely trying to save the doc when an KeyboardInterrupt is raised by the user.
    safe=True,
    # system functions.
    __loader__=None,
    __checks__=True,
    __keyboard_interrupt__=False,
    __attempt__=1,
    __real_path__=None, )

```
##### delete:
``` python

# call Files.delete.
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

# call Files.chmod.
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

# call Files.chown.
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

# call Files.exists.
_ = Files.exists(path=None, sudo=False)

```
##### directory:
``` python

# call Files.directory.
_ = Files.directory(
    # the path (#1).
    path=None,
    # root permission required.
    sudo=False, )

```
##### mounted:
``` python

# call Files.mounted.
_ = Files.mounted(
    # the path (#1).
    path=None, )

```
##### create:
``` python

# call Files.create.
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

# call Files.copy.
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

# call Files.move.
_ = Files.move(
    # the from & to path (#1 & #2).
    from_, to_,
    # root permission required.
    sudo=False,
    # root permission required.
    log_level=0, )

```

## FireWall:
The fire_wall object class.
``` python 

# import the dev0s.network.firewall object class.
from dev0s import dev0s

```

#### Functions:

##### enable:
``` python

# call dev0s.network.firewall.enable.
_ = dev0s.network.firewall.enable()

```
##### disable:
``` python

# call dev0s.network.firewall.disable.
_ = dev0s.network.firewall.disable()

```
##### allow:
``` python

# call dev0s.network.firewall.allow.
_ = dev0s.network.firewall.allow(port)

```
##### deny:
``` python

# call dev0s.network.firewall.deny.
_ = dev0s.network.firewall.deny(port)

```
##### allow_all:
``` python

# call dev0s.network.firewall.allow_all.
_ = dev0s.network.firewall.allow_all()

```
##### deny_all:
``` python

# call dev0s.network.firewall.deny_all.
_ = dev0s.network.firewall.deny_all()

```
##### set_default:
``` python

# call dev0s.network.firewall.set_default.
_ = dev0s.network.firewall.set_default(deny=True)

```
##### info:
``` python

# call dev0s.network.firewall.info.
_ = dev0s.network.firewall.info()

```

## Formats:
The formats object class.
``` python 

# initialize the Formats object class.
formats = Formats(i.upper())

```

#### Functions:

##### check:
``` python

# call Formats.check.
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

# call Formats.get.
_ = Formats.get(value, serialize=False)

```
##### initialize:
``` python

# call Formats.initialize.
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

# call Formats.denitialize.
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

# initialize the Generate object class.
generate = Generate()

```

#### Functions:

##### int:
``` python

# call Generate.int.
_ = Generate.int(length=6)

```
##### string:
``` python

# call Generate.string.
_ = Generate.string(length=6, capitalize=True, digits=True)

```

## Group:
The group object class.
``` python 

# initialize the dev0s.system.Group object class.
group = dev0s.system.Group(
    
    # string format.
    name=None,
    users=[], # all authorized user identifiers.
    # boolean format.
    get_users=False, # (only gets filled if the storages group exists.) )

```

#### Functions:

##### create:
``` python

# call dev0s.system.Group.create.
_ = dev0s.system.Group.create(users=None)

```
##### delete:
``` python

# call dev0s.system.Group.delete.
_ = dev0s.system.Group.delete()

```
##### check:
``` python

# call dev0s.system.Group.check.
_ = dev0s.system.Group.check()

```
##### list_users:
``` python

# call dev0s.system.Group.list_users.
_ = dev0s.system.Group.list_users()

```
##### delete_users:
``` python

# call dev0s.system.Group.delete_users.
_ = dev0s.system.Group.delete_users(users=[])

```
##### add_users:
``` python

# call dev0s.system.Group.add_users.
_ = dev0s.system.Group.add_users(users=[])

```
##### check_users:
``` python

# call dev0s.system.Group.check_users.
_ = dev0s.system.Group.check_users(users=[])

```

## Image:
The image object class.
``` python 

# initialize the Image object class.
image = Image(path=None, image=None, load=False)

```

#### Functions:

##### load:
``` python

# call Image.load.
_ = Image.load(path=None)

```
##### edit_pixel:
``` python

# call Image.edit_pixel.
_ = Image.edit_pixel(pixel=[0, 0], new_pixel_tuple=None)

```
##### convert:
``` python

# call Image.convert.
_ = Image.convert(input='logo.png', output='logo.ico')

```
##### replace_pixels:
``` python

# call Image.replace_pixels.
_ = Image.replace_pixels(input_path=None, output_path=None, input_hex=None, output_hex=None)

```
##### replace_colors:
``` python

# call Image.replace_colors.
_ = Image.replace_colors(input_path=None, output_path=None, hex=None)

```
##### rgb_to_hex:
``` python

# call Image.rgb_to_hex.
_ = Image.rgb_to_hex(tuple)

```
##### hex_to_rgb:
``` python

# call Image.hex_to_rgb.
_ = Image.hex_to_rgb(_hex_)

```
##### instance:
``` python

# call Image.instance.
_ = Image.instance()

```
##### raw:
``` python

# call Image.raw.
_ = Image.raw()

```

## Integer:
The integer object class.
``` python 

# initialize the Integer object class.
integer = Integer(value=0, format="auto")

```

#### Functions:

##### increase_version:
``` python

# call Integer.increase_version.
_ = Integer.increase_version()

```
##### round:
``` python

# call Integer.round.
_ = Integer.round(decimals)

```
##### round_down:
``` python

# call Integer.round_down.
_ = Integer.round_down(decimals)

```
##### generate:
``` python

# call Integer.generate.
_ = Integer.generate(length=6)

```
##### instance:
``` python

# call Integer.instance.
_ = Integer.instance()

```
##### assign:
``` python

# call Integer.assign.
_ = Integer.assign(value)

```
##### raw:
``` python

# call Integer.raw.
_ = Integer.raw()

```

## Loader:
The loader object class.
``` python 

# initialize the Loader object class.
loader = Loader(message, autostart=True, log_level=0, interactive=True)

```

#### Functions:

##### run:
``` python

# call Loader.run.
_ = Loader.run()

```
##### stop:
``` python

# call Loader.stop.
_ = Loader.stop(message=None, success=True, response=None, quiet=False)

```
##### mark:
``` python

# call Loader.mark.
_ = Loader.mark(new_message=None, old_message=None, success=True, response=None)

```
##### hold:
``` python

# call Loader.hold.
_ = Loader.hold()

```
##### release:
``` python

# call Loader.release.
_ = Loader.release()

```

## Network:
The network object class.
``` python 

# import the dev0s.network object class.
from dev0s import dev0s

```

#### Functions:

##### info:
``` python

# call dev0s.network.info.
_ = dev0s.network.info()

```
##### convert_dns:
``` python

# call dev0s.network.convert_dns.
_ = dev0s.network.convert_dns(dns, timeout=1)

```
##### ping:
``` python

# call dev0s.network.ping.
_ = dev0s.network.ping(ip, timeout=1)

```
##### port_in_use:
``` python

# call dev0s.network.port_in_use.
_ = dev0s.network.port_in_use(port, host="127.0.0.1")

```
##### free_port:
``` python

# call dev0s.network.free_port.
_ = dev0s.network.free_port(start=6080)

```

## Object:
The object object class.
``` python 

# initialize the Object object class.
object = Object(
    # attributes (dict) (#1)
    attributes={},
    # the imported traceback.
    traceback="Object",
    # the raw traceback.
    raw_traceback="Object", )

```

#### Functions:

##### items:
``` python

# call Object.items.
_ = Object.items(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### keys:
``` python

# call Object.keys.
_ = Object.keys(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### values:
``` python

# call Object.values.
_ = Object.values()

```
##### assign:
``` python

# call Object.assign.
_ = Object.assign(
    # the dictionary to self assign.
    dictionary,
    # serialize dictionary from str to object.
    serialize=True,
    # the keys to get from the dict (leave default to unpack the present keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### attributes:
``` python

# call Object.attributes.
_ = Object.attributes(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### dict:
``` python

# call Object.dict.
_ = Object.dict(
    # the keys to get (leave default to unpack all keys).
    #    list instance: checks if the key is present if not it throws an error when [safe] is disabled
    #    dict instance: automatically enables [safe] and returns the key's value as default when missing.
    keys=["*"],
    # with safe disabled it throws an error when one of the specified keys does not exist.
    safe=True, )

```
##### unpack:
``` python

# call Object.unpack.
_ = Object.unpack(
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

# initialize the OutputObject object class.
output_object = OutputObject(
    #
    # The return object from function: dec0s.code.execute
    # The OutputObject object is very similair to the ResponseObject.
    #
    # the success message (param #1).
    message=None,
    # the attributes (param #2).
    attributes={},
    # the error message (param #3).
    error=None,
    # the log level.
    log_level=defaults.options.log_level, )

```

#### Functions:

##### instance:
``` python

# call OutputObject.instance.
_ = OutputObject.instance()

```
##### response:
``` python

# call OutputObject.response.
_ = OutputObject.response()

```

## Ownership:
The ownership object class.
``` python 

# initialize the Ownership object class.
ownership = Ownership(path=None, load=False)

```

#### Functions:

##### get:
``` python

# call Ownership.get.
_ = Ownership.get(path=None)

```
##### set:
``` python

# call Ownership.set.
_ = Ownership.set(
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

# call Ownership.check.
_ = Ownership.check(owner=None, group=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

```

## Parameters:
The parameters object class.
``` python 

# import the dev0s.response.parameters object class.
from dev0s import dev0s

```

#### Functions:

##### get:
``` python

# call dev0s.response.parameters.get.
_ = dev0s.response.parameters.get(
    # the django request (1).
    request=None,
    # the identifiers (#2).
    #    str instance: return the parameters value.
    #    list instance: return a parameters object & return an error response when a parameter is undefined.
    #    dict instance: return a parameters object & return the parameter's value from the dict as a default when undefined.
    parameters=[],
    # traceback id.
    traceback=None, )

```
##### check:
``` python

# call dev0s.response.parameters.check.
_ = dev0s.response.parameters.check(
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

# initialize the Permission object class.
permission = Permission(path=None, load=False)

```

#### Functions:

##### get:
``` python

# call Permission.get.
_ = Permission.get(path=None)

```
##### set:
``` python

# call Permission.set.
_ = Permission.set(
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

# call Permission.check.
_ = Permission.check(permission=None, sudo=False, silent=False, iterate=False, recursive=False, path=None)

```

## ProgressLoader:
The progress_loader object class.
``` python 

# initialize the ProgressLoader object class.
progress_loader = ProgressLoader(message, index=0, max=10, log_level=0)

```

#### Functions:

##### next:
``` python

# call ProgressLoader.next.
_ = ProgressLoader.next(count=1, decimals=2)

```
##### stop:
``` python

# call ProgressLoader.stop.
_ = ProgressLoader.stop(message=None, success=True, response=None)

```

## RSA:
The rsa object class.
``` python 

# initialize the dev0s.encryption.RSA object class.
rsa = dev0s.encryption.RSA(
    # option 1:
    #     the key directory.
    directory=None,
    # option 2:
    public_key=None,
    private_key=None,
    memory=False, # enable memory when the keys are not saved.
    # the key's passphrase (Leave None for no passphrase).
    passphrase=None, )

```

#### Functions:

##### generate_keys:
``` python

# call dev0s.encryption.RSA.generate_keys.
_ = dev0s.encryption.RSA.generate_keys(log_level=0)

```
##### load_keys:
``` python

# call dev0s.encryption.RSA.load_keys.
_ = dev0s.encryption.RSA.load_keys()

```
##### load_public_key:
``` python

# call dev0s.encryption.RSA.load_public_key.
_ = dev0s.encryption.RSA.load_public_key()

```
##### load_private_key:
``` python

# call dev0s.encryption.RSA.load_private_key.
_ = dev0s.encryption.RSA.load_private_key()

```
##### edit_passphrase:
``` python

# call dev0s.encryption.RSA.edit_passphrase.
_ = dev0s.encryption.RSA.edit_passphrase(passphrase=None)

```
##### encrypt_string:
``` python

# call dev0s.encryption.RSA.encrypt_string.
_ = dev0s.encryption.RSA.encrypt_string(string, layers=1, decode=True)

```
##### encrypt_file:
``` python

# call dev0s.encryption.RSA.encrypt_file.
_ = dev0s.encryption.RSA.encrypt_file(path, layers=1)

```
##### encrypt_directory:
``` python

# call dev0s.encryption.RSA.encrypt_directory.
_ = dev0s.encryption.RSA.encrypt_directory(path, recursive=False, layers=1)

```
##### decrypt_string:
``` python

# call dev0s.encryption.RSA.decrypt_string.
_ = dev0s.encryption.RSA.decrypt_string(string, layers=1, decode=True)

```
##### decrypt_file:
``` python

# call dev0s.encryption.RSA.decrypt_file.
_ = dev0s.encryption.RSA.decrypt_file(path, layers=1)

```
##### decrypt_directory:
``` python

# call dev0s.encryption.RSA.decrypt_directory.
_ = dev0s.encryption.RSA.decrypt_directory(path, recursive=False, layers=1)

```

#### Properties:
```python

# the encryption property.
encryption = dev0s.encryption.RSA.activated
```
```python

# the encryption property.
encryption = dev0s.encryption.RSA.private_key_activated
```
```python

# the encryption property.
encryption = dev0s.encryption.RSA.public_key_activated
```

## Requests:
The requests object class.
``` python 

# import the dev0s.requests object class.
from dev0s import dev0s

```

#### Functions:

##### encode:
``` python

# call dev0s.requests.encode.
_ = dev0s.requests.encode(data)

```
##### get:
``` python

# call dev0s.requests.get.
_ = dev0s.requests.get(
    # the url (str) (#1).
    url=None,
    # the sended post data (dict) (#2).
    data={},
    # serialize output to dictionary.
    serialize=False, )

```

## Response:
The response object class.
``` python 

# import the dev0s.response object class.
from dev0s import dev0s

```

#### Functions:

##### success:
``` python

# call dev0s.response.success.
_ = dev0s.response.success(
    # the message (must be param #1).
    message,
    # additional returnable functions (must be param #2).
    variables={},
    # log log level of the message (int).
    log_level=None,
    # the required log level for when printed to console (leave None to use response.log_level).
    required_log_level=None,
    # save the error to the logs file.
    save=False,
    # return as a django Jsonresponse.
    django=False, )

```
##### error:
``` python

# call dev0s.response.error.
_ = dev0s.response.error(
    # the error message.
    error="",
    # log log level of the message (int).
    log_level=None,
    # the required log level for when printed to console (leave None to use response.log_level).
    required_log_level=None,
    # save the error to the erros file.
    save=False,
    # return as a django Jsonresponse.
    django=False,
    # raise error for developer traceback.
    traceback=ERROR_TRACEBACK, )

```
##### log:
``` python

# call dev0s.response.log.
_ = dev0s.response.log(
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
    # the required log level for when printed to console (leave None to use response.log_level).
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

# call dev0s.response.load_logs.
_ = dev0s.response.load_logs(format="webserver", options=["webserver", "cli", "array", "string"])

```
##### reset_logs:
``` python

# call dev0s.response.reset_logs.
_ = dev0s.response.reset_logs()

```
##### serialize:
``` python

# call dev0s.response.serialize.
response = dev0s.response.serialize(
    # the response (#1) (dict) (str repr of dict) (ResponseObject) (generator) .
    response={},
    # init to response object.
    init=True, )

```
##### response:
``` python

# call dev0s.response.response.
_ = dev0s.response.response(
    # the blank response (dict, str, generator) (#1).
    response={
        "success":False,
        "message":None,
        "error":None,
    }, )

```
##### log_to_file:
``` python

# call dev0s.response.log_to_file.
_ = dev0s.response.log_to_file(message, raw=False)

```

## ResponseObject:
The response_object object class.
``` python 

# initialize the ResponseObject object class.
response_object = ResponseObject(
    #
    # Should be initialized with response.success or response.error.
    #
    # the response attributes (dict or dict in str format).
    attributes={
        "success":False,
        "message":None,
        "error":None,
    }, )

```

#### Functions:

##### clean:
``` python

# call ResponseObject.clean.
_ = ResponseObject.clean(
    # the clean options, select * for all, options: [traceback].
    options=["*"],
    # serialize to ResponseObject (with serialize False the ResponseObject's values are not updated).
    serialize=True, )

```
##### assign:
``` python

# call ResponseObject.assign.
_ = ResponseObject.assign(dictionary)

```
##### crash:
``` python

# call ResponseObject.crash.
_ = ResponseObject.crash(error="ValueError", traceback=True, json=False, error_only=False)

```
##### unpack:
``` python

# call ResponseObject.unpack.
_ = ResponseObject.unpack(
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

# call ResponseObject.remove.
_ = ResponseObject.remove(keys=[], values=[], save=False)

```
##### iterate:
``` python

# call ResponseObject.iterate.
_ = ResponseObject.iterate(sorted=False, reversed=False)

```
##### items:
``` python

# call ResponseObject.items.
_ = ResponseObject.items(sorted=False, reversed=False, dictionary=None)

```
##### keys:
``` python

# call ResponseObject.keys.
_ = ResponseObject.keys(sorted=False, reversed=False)

```
##### values:
``` python

# call ResponseObject.values.
_ = ResponseObject.values(sorted=False, reversed=False, dictionary=None)

```
##### reversed:
``` python

# call ResponseObject.reversed.
_ = ResponseObject.reversed(dictionary=None)

```
##### sort:
``` python

# call ResponseObject.sort.
_ = ResponseObject.sort(alphabetical=True, ascending=False, reversed=False, dictionary=None)

```
##### dict:
``` python

# call ResponseObject.dict.
_ = ResponseObject.dict(sorted=False, reversed=False, json=False)

```
##### json:
``` python

# call ResponseObject.json.
_ = ResponseObject.json(sorted=False, reversed=False, indent=4, dictionary=None, )

```
##### serialize:
``` python

# call ResponseObject.serialize.
_ = ResponseObject.serialize(sorted=False, reversed=False, json=False, dictionary=None)

```
##### instance:
``` python

# call ResponseObject.instance.
_ = ResponseObject.instance()

```
##### raw:
``` python

# call ResponseObject.raw.
_ = ResponseObject.raw()

```
##### response:
``` python

# call ResponseObject.response.
_ = ResponseObject.response()

```

## RestAPI:
The restapi object class.
``` python 

# initialize the dev0s.requests.RestAPI object class.
restapi = dev0s.requests.RestAPI(
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

# call dev0s.requests.RestAPI.request.
_ = dev0s.requests.RestAPI.request(url="/", data={})

```

## Service:
The service object class.
``` python 

# initialize the dev0s.system.Service object class.
service = dev0s.system.Service(
    # the service id.
    id=None,
    # the user & group on which the service will be run.
    user=None,
    group=None,
    # the start command.
    start=None,
    # the service description.
    description="",
    # restart on crash.
    restart=True,
    # the restart limit.
    restart_limit=5,
    # the restart delay.
    restart_delay=10,
    # the path to the log file.
    logs=None,
    # the path to the error file.
    errors=None,
    # the object's log level.
    log_level=0,
    # the import traceback.
    traceback="dev0s.system.Service", )

```

#### Functions:

##### create:
``` python

# call dev0s.system.Service.create.
_ = dev0s.system.Service.create()

```
##### check:
``` python

# call dev0s.system.Service.check.
_ = dev0s.system.Service.check()

```
##### delete:
``` python

# call dev0s.system.Service.delete.
_ = dev0s.system.Service.delete()

```
##### start:
``` python

# call dev0s.system.Service.start.
_ = dev0s.system.Service.start()

```
##### stop:
``` python

# call dev0s.system.Service.stop.
_ = dev0s.system.Service.stop()

```
##### restart:
``` python

# call dev0s.system.Service.restart.
_ = dev0s.system.Service.restart()

```
##### status:
``` python

# call dev0s.system.Service.status.
_ = dev0s.system.Service.status()

```
##### reset_logs:
``` python

# call dev0s.system.Service.reset_logs.
_ = dev0s.system.Service.reset_logs()

```
##### tail:
``` python

# call dev0s.system.Service.tail.
_ = dev0s.system.Service.tail(global_=False, debug=False)

```

## Spawn:
The spawn object class.
``` python 

# initialize the Spawn object class.
spawn = Spawn(
    #
    # Should be initialized with function: dev0s.code.execute
    #
    # the full command (str) (#1).
    command="ls",
    # asynchronous.
    async_=False,
    # the log level.
    log_level=defaults.options.log_level,
    # additional attributes.
    attributes={},
    # system options.
    response_str=None, )

```

#### Functions:

##### start:
``` python

# call Spawn.start.
_ = Spawn.start()

```
##### expect:
``` python

# call Spawn.expect.
_ = Spawn.expect(
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

# call Spawn.read.
_ = Spawn.read(
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

# call Spawn.kill.
_ = Spawn.kill()

```
##### wait:
``` python

# call Spawn.wait.
_ = Spawn.wait(
    # the live boolean (bool) (prints live logs to console when enabled) (leave None to use spawn.log_level >= 1).
    live=None,
    sleeptime=1,
    # the timeout (leave None to ignore).
    timeout=None, )

```
##### crashed:
``` python

# call Spawn.crashed.
_ = Spawn.crashed()

```

#### Properties:
```python

# the expecting property.
expecting = Spawn.expecting
```
```python

# the running property.
running = Spawn.running
```
```python

# the exit status property.
exit_status = Spawn.exit_status
```
```python

# the output property.
output = Spawn.output
```
```python

# the pid property.
pid = Spawn.pid
```

## String:
The string object class.
``` python 

# initialize the String object class.
string = String(string="")

```

#### Functions:

##### is_numerical:
``` python

# call String.is_numerical.
_ = String.is_numerical()

```
##### bash:
``` python

# call String.bash.
_ = String.bash()

```
##### identifier:
``` python

# call String.identifier.
_ = String.identifier()

```
##### variable_format:
``` python

# call String.variable_format.
_ = String.variable_format(
    exceptions={
        "smart_card":"smartcard",
        "smart_cards":"smartcards" ,
        "web_server":"webserver" ,
    }, )

```
##### class_format:
``` python

# call String.class_format.
_ = String.class_format()

```
##### capitalized_scentence:
``` python

# call String.capitalized_scentence.
_ = String.capitalized_scentence()

```
##### capitalized_word:
``` python

# call String.capitalized_word.
_ = String.capitalized_word()

```
##### generate:
``` python

# call String.generate.
_ = String.generate(
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

# call String.first_occurence.
_ = String.first_occurence(charset=[" ", "\n"], reversed=False, string=None)

```
##### before_after_first_occurence:
``` python

# call String.before_after_first_occurence.
_ = String.before_after_first_occurence(slicer=" ", include=True, include_before=False, include_after=False, string=None)

```
##### before_selected_after_first_occurence:
``` python

# call String.before_selected_after_first_occurence.
_ = String.before_selected_after_first_occurence(slicer=" ", string=None)

```
##### before_after_last_occurence:
``` python

# call String.before_after_last_occurence.
_ = String.before_after_last_occurence(slicer=" ", include=True, include_before=False, include_after=False, string=None)

```
##### before_selected_after_last_occurence:
``` python

# call String.before_selected_after_last_occurence.
_ = String.before_selected_after_last_occurence(slicer=" ", string=None)

```
##### between:
``` python

# call String.between.
_ = String.between(identifiers=["{","}"], depth=1, include=True, string=None)

```
##### increase_version:
``` python

# call String.increase_version.
_ = String.increase_version()

```
##### slice_dict:
``` python

# call String.slice_dict.
_ = String.slice_dict(depth=1)

```
##### slice_array:
``` python

# call String.slice_array.
_ = String.slice_array(depth=1)

```
##### slice_tuple:
``` python

# call String.slice_tuple.
_ = String.slice_tuple(depth=1)

```
##### indent:
``` python

# call String.indent.
_ = String.indent(indent=4)

```
##### line_indent:
``` python

# call String.line_indent.
_ = String.line_indent(line="")

```
##### slice_indent:
``` python

# call String.slice_indent.
_ = String.slice_indent(indent=4, depth=1, string=None, remove_indent=True)

```
##### first:
``` python

# call String.first.
_ = String.first(count)

```
##### last:
``` python

# call String.last.
_ = String.last(count)

```
##### remove_first:
``` python

# call String.remove_first.
_ = String.remove_first(count)

```
##### remove_last:
``` python

# call String.remove_last.
_ = String.remove_last(count)

```
##### split:
``` python

# call String.split.
_ = String.split(string)

```
##### count:
``` python

# call String.count.
_ = String.count(string)

```
##### replace:
``` python

# call String.replace.
_ = String.replace(from_, to_)

```
##### lower:
``` python

# call String.lower.
_ = String.lower(string)

```
##### upper:
``` python

# call String.upper.
_ = String.upper(string)

```
##### instance:
``` python

# call String.instance.
_ = String.instance()

```
##### assign:
``` python

# call String.assign.
_ = String.assign(string)

```
##### raw:
``` python

# call String.raw.
_ = String.raw()

```

## Symbol:
The symbol object class.
``` python 

# import the symbol object class.
from dev0s import symbol

```
## System:
The system object class.
``` python 

# initialize the System object class.
system = System

```
## Thread:
The thread object class.
``` python 

# initialize the Thread object class.
thread = Thread(
    # the threads id (#1).
    id="Thread",
    # the imported traceback.
    traceback="Thread",
    # the raw traceback.
    raw_traceback="Thread",
    # the threads log level.
    log_level=-1, )

```

#### Functions:

##### run:
``` python

# call Thread.run.
_ = Thread.run()

```
##### safe_start:
``` python

# call Thread.safe_start.
_ = Thread.safe_start(timeout=120, sleeptime=1)

```
##### safe_stop:
``` python

# call Thread.safe_stop.
_ = Thread.safe_stop(timeout=120, sleeptime=1)

```
##### send_stop:
``` python

# call Thread.send_stop.
_ = Thread.send_stop(
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
    # the required log level for when to print to console (leave None to use _response_.log_level ; default: 0).
    required_log_level=_response_.log_level, )

```
##### send_crash:
``` python

# call Thread.send_crash.
_ = Thread.send_crash(
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
    # the required log level for when to print to console (leave None to use _response_.log_level ; default: 0).
    required_log_level=_response_.log_level, )

```
##### log:
``` python

# call Thread.log.
_ = Thread.log(
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
run_permission = Thread.run_permission
```
```python

# the running property.
running = Thread.running
```
```python

# the stopped property.
stopped = Thread.stopped
```
```python

# the crashed property.
crashed = Thread.crashed
```
```python

# the response property.
response = Thread.response
```

## Traceback:
The traceback object class.
``` python 

# initialize the Traceback object class.
traceback = Traceback(
    # the imported traceback (#1).
    traceback="Traceback",
    # the raw traceback (#2).
    raw_traceback="Object", )

```
#### Properties:
```python

# the traceback property.
traceback = Traceback.traceback
```

## UnixManager:
The unix_manager object class.
``` python 

# initialize the UnixManager object class.
unix_manager = UnixManager()

```
## User:
The user object class.
``` python 

# initialize the dev0s.system.User object class.
user = dev0s.system.User(
    # the users username.
    username=None, )

```

#### Functions:

##### create:
``` python

# call dev0s.system.User.create.
_ = dev0s.system.User.create()

```
##### delete:
``` python

# call dev0s.system.User.delete.
_ = dev0s.system.User.delete()

```
##### check:
``` python

# call dev0s.system.User.check.
_ = dev0s.system.User.check(silent=False)

```
##### set_password:
``` python

# call dev0s.system.User.set_password.
_ = dev0s.system.User.set_password(password=None)

```
##### add_groups:
``` python

# call dev0s.system.User.add_groups.
_ = dev0s.system.User.add_groups(groups=[])

```
##### delete_groups:
``` python

# call dev0s.system.User.delete_groups.
_ = dev0s.system.User.delete_groups(groups=[])

```

## WebServer:
The webserver object class.
``` python 

# initialize the dev0s.database.WebServer object class.
webserver = dev0s.database.WebServer(
    id="webserver",
    host="127.0.0.1",
    port=52379,
    sleeptime=3,
    log_level=0,
    # do not use.
    serialized={}, )

```

#### Functions:

##### set:
``` python

# call dev0s.database.WebServer.set.
_ = dev0s.database.WebServer.set(group=None, id=None, data=None, timeout=3)

```
##### get:
``` python

# call dev0s.database.WebServer.get.
_ = dev0s.database.WebServer.get(group=None, id=None, timeout=3)

```
##### app:
``` python

# call dev0s.database.WebServer.app.
_ = dev0s.database.WebServer.app()

```
##### run:
``` python

# call dev0s.database.WebServer.run.
_ = dev0s.database.WebServer.run()

```
##### fork:
``` python

# call dev0s.database.WebServer.fork.
_ = dev0s.database.WebServer.fork(timeout=15, sleeptime=1)

```
##### stop:
``` python

# call dev0s.database.WebServer.stop.
_ = dev0s.database.WebServer.stop()

```
##### start_thread:
``` python

# call dev0s.database.WebServer.start_thread.
_ = dev0s.database.WebServer.start_thread(thread, group="daemons", id=None)

```
##### get_thread:
``` python

# call dev0s.database.WebServer.get_thread.
_ = dev0s.database.WebServer.get_thread(group="daemos", id=None)

```

#### Properties:
```python

# the database property.
database = dev0s.database.WebServer.token
```
```python

# the database property.
database = dev0s.database.WebServer.running
```

## Zip:
The zip object class.
``` python 

# initialize the Zip object class.
zip = Zip(path=None, check=False)

```

#### Functions:

##### create:
``` python

# call Zip.create.
_ = Zip.create(
    # source can either be a string or an array.
    source=None,
    # remove the source file(s).
    remove=False,
    # sudo required to move/copy source files.
    sudo=False, )

```
##### extract:
``` python

# call Zip.extract.
_ = Zip.extract(
    # the base extract directory.
    base=None,
    # remove the zip after extraction.
    remove=False,
    # if sudo required for removing file path.
    sudo=False,)

```
##### instance:
``` python

# call Zip.instance.
_ = Zip.instance()

```
##### raw:
``` python

# call Zip.raw.
_ = Zip.raw()

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
#### check_group:
The check_group function.
``` python

# call check_group.
_ = check_group(id, users=[], create=False, overwrite=False)

```
#### check_os:
The check_os function.
``` python

# call check_os.
_ = check_os(supported=["linux"], error=False)

```
#### check_user:
The check_user function.
``` python

# call check_user.
_ = check_user(id, create=False)

```
#### coming_soon:
The coming_soon function.
``` python

# call coming_soon.
_ = coming_soon()

```
#### execute:
The execute function.
``` python

# call execute.
_ = execute(
    # Notes:
    #   returns a dev0s.code.OutputObject object (very similair to ResponseObject).
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
#### input:
The input function.
``` python

# call input.
_ = input(message, yes_no=False, check=False, password=False, default=None)

```
#### kill:
The kill function.
``` python

# call kill.
_ = kill(
    # option 1:
    # the process id.
    pid=None,
    # option 2:
    # all processes that includes.
    includes=None,
    # root permission required.
    sudo=False,
    # loader.
    log_level=0, )

```
#### print_replace:
The print_replace function.
``` python

# call print_replace.
_ = print_replace(msg)

```
#### processes:
The processes function.
``` python

# call processes.
_ = processes(
    # root permission.
    sudo=False,
    # all processes that include a str.
    includes=None,
    # banned process names.
    banned=["grep"], )

```
#### unpack:
The unpack function.
``` python

# call unpack.
_ = unpack(content)

```
