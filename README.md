# covid19-polybar
A script that pulls covid19 numbers from the COVID19 API (https://covid19api.com/)

## Dependencies
* Python3

## Usage

## Module

```ini
[module/covid19]
type = custom/script
exec = "~/polybar-scripts/covid19 <country> <attribute>"
interval = 1800
```
