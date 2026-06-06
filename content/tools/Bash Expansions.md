---
title: Bash Expansions
tags:
  - command_line
  - bash
---
```bash
variable="value"
echo ${variable} # → value
echo $variable # → value
```

Curly braces are used to delimit the variable.

```bash
echo ${variable}_ # → value_
echo $variable_ # → (empty)

set -o nounset
echo $variable_ # exits with error "unbound variable"
```

## Variable indirection

```bash
variable="HOME"
echo ${!variable} # /usr/alpha
```

## Uppercase

```bash
variable="value"

echo ${variable} # → value
echo ${variable^} # → Value
echo ${variable^^} # → VALUE
```

## Lowercase

```bash
variable="VALUE"
echo ${variable} # → VALUE
echo ${variable,} # → vALUE
echo ${variable,,} # → value
```

## Pattern matching

```bash
variable="VALUE"
echo ${variable,,[VAL]} # → valUE
echo ${variable,,[LUE]} # → VAlue

variable="value"
echo ${variable^^[va]} # → VAlue
```

## Arrays

```bash
variables=(one two three)
echo ${variables[@]} # → one two three
echo ${variables[@]^} # → One Two Three
echo ${variables[@]^^} # → ONE TWO THREE
echo ${variables[@]^^[oe]} # → OnE twO thrEE
echo ${variables[*]^^[oe]} # → OnE twO thrEE

echo ${variables[2]^^} # → THREE
```

## Substring removal

### From begginning of string

```bash
variable="value1 value2"
echo ${variable#va} # → lue1 value2
echo ${variable#val} # → ue1 value2
echo ${variable#*l} # → ue1 value2
echo ${variable##val} # → ue1 value2
echo ${variable##*l} # → ue2
```

### From end of string

```bash
variable="value1 value2"
echo ${variable%lue2} # → value1 va
echo ${variable%al*} # → value1 v
echo ${variable%*l*} # → value1 va
```

## String replacement

```bash
echo ${variable/value/example} # → example1 value2
echo ${variable//#value/example} # → example1 example2
echo ${variable/#value/example} # → example1 value2
echo ${variable/value*/example} # → example
echo ${variable/%value2/example} # → value1 example
```

## Substring

```bash
echo ${variable:4} # → e1 value2
echo ${variable:2:3} # → lue
# The space before the - sign is required
echo ${variable: -3} # → ue2
echo ${variable:1: -1} # → alue1 value
echo ${variable: -3: -1} # → ue
```

## Length

```bash
echo ${#variable} # → 13
echo ${#variables[@]} # → 3
echo ${#variables[2]} # → 5
```

[^linuxConfig]: [Introduction to Bash Shell Parameter Expansions](https://linuxconfig.org/introduction-to-bash-shell-parameter-expansions)
