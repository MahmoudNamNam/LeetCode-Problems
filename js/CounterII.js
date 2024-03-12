var createCounter = function (init) {
  let cnt = init;

  function increment() {
    return ++cnt;
  }
  function decrement() {
    return --cnt;
  }
  function reset() {
    return (cnt = init);
  }
  return { increment, decrement, reset };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

const counter = createCounter(5);
console.log("counter.increment()", counter.increment()); // 6
console.log("counter.reset()", counter.reset()); // 5
console.log("counter.decrement()", counter.decrement()); // 4
