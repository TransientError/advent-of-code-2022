import b from "benny";
import _ from "lodash";

b.suite(
  "Sum 1000 elements",
  b.add("Reduce", () => {
    const reduce_data = [...Array(1000).keys()];
    return () => reduce_data.reduce((a, b) => a + b, 0);
  }),
  // b.add("lodash sum", () => {
  //   const lodash_sum = [...Array(1000).keys()];
  //   return () => _.sum(lodash_sum);
  // }),
  b.add("for of loop", () => {
    const loop_data = [...Array(1000).keys()];
    return () => {
      let sum = 0;
      for (const n of loop_data) {
        sum += n;
      }
    }
  }),
  b.add("for loop", () => {
    const loop_data = [...Array(1000).keys()];
    return () => {
      let sum = 0;
      for (let i = 0; i < 1000; i++) {
        sum += loop_data[i];
      }
    }
  }),
  b.cycle(),
  b.complete()
);
