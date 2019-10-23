# jisho-py
A simple Python wrapper for the API of [jisho.org](https://jisho.org/)

## Installation
You can install the module with pip:

### NOTE! Pip installation is currently broken. If you wish to install the script, move it to your "site-packages" folder.

Linux:

```
python3 -m pip install jishopy
``` 

Windows:

```
py -m pip install jishopy
``` 

Alternatively you can install the module using the `setup.py` script on Linux with:

```
python3 setup.py
``` 

Or on Windows with:

```
py setup.py
``` 


## Usage
This module is a wrapper of the search api of [jisho.org](https://jisho.org/).
You can search using english or japanese. (romaji is supported)

### Examples
You can import the module with:
```python3
import jisho
```
Look up something with:
```python3
jisho.search("hello")
```
It returns all the search results as objects in an array.
To see a quick translation you can just print the 1st one:
```python3
print(jisho.search("hello")[0])
```
```
> 今日は (こんにちは) = hello
```
You can also just look it up in Japanese with: 
```python3
# NOTE .ja returns an array of all the varities!
print(jisho.search("hello")[0].ja[0])
```
```
> 今日は (こんにちは)
```
If you only want the Japanese word without reading, you can do that with:
```python3
print(jisho.search("hello")[0].ja[0].word)
```
```
> 今日は
```
If you only want the reading of the word, you can get it with:
```python3
print(jisho.search("hello")[0].ja[0].reading)
```
```
> こんにちは
```
If you want to look up if the word you are looking for is common or not, you can do it with:
```python3
print(jisho.search("hello")[0].iscommon)
```
```
> True
```
You can see the difficulty of a kanji (based on the (JLPT)[https://www.jlpt.jp/e/]) with:
```python3
# NOTE this will return an array!
print(jisho.search("hello")[0].jlpt)
```
```
> ['jlpt-n3', 'jlpt-n1']
```
If you only want to see the meaning of a certain word you can do that with:
```python3
# NOTE .en returns an array of all the varities!
print(jisho.search("hello")[0].en[0])
```
```
> hello
```
