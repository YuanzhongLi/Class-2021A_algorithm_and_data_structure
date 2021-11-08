const partition = (A, l, r, index = -1) => {
  if (index === -1) {
    index = r;
  }
  const pivot = A[index];

  let i = l - 1;
  for (let j = l; j < r; j += 1) {
    if (A[j] <= pivot) {
      i += 1;
      const ai = A[i];
      A[i] = A[j];
      A[j] = ai;
    }
  }

  const tmp = A[i + 1];
  A[i + 1] = A[r];
  A[r] = tmp;
  return i + 1;
};

/**
 * average O(NlogN), worst O(N^2)
 * in place sort
 */
const QuickSort = (array, l, r) => {
  if (l < r) {
    const pivotIndex = partition(array, l, r);
    QuickSort(array, l, pivotIndex - 1);
    QuickSort(array, pivotIndex + 1, r);
  }
};

/**
 * [min, max) の整数をrandomに取得
 * @returns {Number}
 */
const getRandomInt = (min = 0, max) => {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
};

const measure = (n) => {
  const array = Array(n);
  for (let i = 0; i < n; i += 1) {
    array[i] = getRandomInt(0, n);
  }
  const start = new Date().getTime();
  QuickSort(array, 0, n - 1);
  const end = new Date().getTime();
  console.log(`${n}, ${end - start}`);
};

const ns = [1000000, 2000000, 4000000, 8000000];
console.log("n, 実行時間(ms)");
for (const n of ns) {
  measure(n);
}
