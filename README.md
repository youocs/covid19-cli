# polybar-covid19

A script that pulls covid19 numbers from the COVID19 API (https://covid19api.com/).

![Alt text](https://i.ibb.co/d70DW32/oie-b-GGpq-RBHARnh.png)

## Dependencies

* Python3

## Usage

Make sure that the file is executable.

```ini
chmod +x ~/polybar-scripts/polybar-covid19
```

Command | Description
---|---
countries  | Lists available countries
attributes | Lists attributes

To execute a command:
 
 ```ini
 ./covid19 <command>
 ```

## Module

```ini
[module/covid19]
type = custom/script
exec = "~/polybar-scripts/covid19 <country> <attribute>"
interval = 1800
```
