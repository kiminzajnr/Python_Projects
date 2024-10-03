## Taming Bid Data with Apache Spark and Python

## [Friends by Age](./friends-by-age.py)
- Calculate number of friends by age

```
$ spark-submit friends-by-age.py

(33, 325.3333333333333)
(26, 242.05882352941177)
(55, 295.53846153846155)
(40, 250.8235294117647)
(68, 269.6)
(59, 220.0)

...

```

## [Ratings Counter](./ratings-counter.py)
- Generate ratings histogram

```
$ spark-submit ratings-counter.py

1 6110
2 11370
3 27145
4 34174
5 21201
```

## [Minimum Temperature](./min-tempretures.py)
- Minimum temperature by location

```
ITE00100554 	5.36F
EZE00100082 	7.70F
```

## [Maximum Temperature](./max-temperatures.py)
- Maximum temperature by location

```
ITE00100554 	90.14F
EZE00100082 	90.14F
```

## [Count word occurrences](./word-count.py)
- Count word occurrences using `flatMap`