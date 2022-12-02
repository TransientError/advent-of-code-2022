import b from "benny";
import _ from "lodash";

b.suite(
  "Sorting",

  b.add("native sort 1000 elements", () => {
    const data = [...Array(1000).keys()];

    return () => data.sort((a, b) => b - a);
  }),
  b.add("lodash sort 1000 elements", () => {
    const data = [...Array(1000).keys()];
    return () => _.sortBy(data)
  }),
  b.cycle(),
  b.complete()
);


