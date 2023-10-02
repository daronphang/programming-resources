## Grouping and Partitioning

If you want to group values with the same characteristic, you can use groupingBy() that takes in a classifier function.

If you want to use a predicate function, use partitionBy().

```java
Stream<Locale> locales = Stream.of(Locale.getAvailableLocales());
Map<String, List<Locale>> countryToLocales = locales.collect(
    Collectors.groupingBy(Locale::getCountry)
);
List<Locale> swissLocales = countryToLocales.get("CH");
// Yields locales [it_CH, de_CH, fr_CH]
```

| Method                                                                                                                   | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| static <T,K> Collector<T,?,Map<K,List<T>>> groupingBy(Function<? super T,? extends K> classifier)                        | Yields a collector that produces a map whose keys are the results of applying classifier to all collected elements |
| static <T,K> Collector<T,?,ConcurrentMap<K,List<T>>> groupingByConcurrent(Function<? super T,?<br>extends K> classifier) | Like groupingBy, but with concurrent map                                                                           |
| static <T> Collector<T,?,Map<Boolean,List<T>>> partitioningBy(Predicate<? super T> predicate)                            | Yields a collector that produces a map whose keys are true/false based on the predicate function                   |

### Downstream Collectors

The groupingBy() yields a map whose values are lists. If you want to process those lists in some way, supply a downstream collector.

```java
Map<String, Set<Locale>> countryToLocaleSet = locales.collect(
    groupingBy(Locale::getCountry, toSet())
);

Map<String, Long> countryToLocaleCounts = locales.collect(
    groupingBy(Locale::getCountry, counting())
);

Map<String, Optional<City>> stateToLargestCity = cities.collect(
    groupingBy(
        City::getState,
        maxBy(Comparator.comparing(City::getPopulation))
    )
);
```
