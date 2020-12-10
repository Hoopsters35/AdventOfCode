import { promises as fs } from "fs";

const main = async () => {
  const content = await (await fs.readFile("data/numbers.txt")).toString();
  const numbers: Array<number> = content
    .split("\n")
    .filter((line) => line.length > 0)
    .map((line) => parseInt(line));

  console.log(firstInvalid(numbers));
  // 23278925
};

const firstInvalid = (numbers: Array<number>): number => {
  const previous5 = numbers.slice(0, 25);
  for (let num of numbers.slice(25)) {
    if (!sumOfTwo(previous5, num)) {
      return num;
    }
    previous5.shift();
    previous5.push(num);
  }
  return -1;
};

const sumOfTwo = (
  numbers: Array<number>,
  target: number
): [number, number] | null => {
  const targets: Set<number> = new Set();
  for (let num of numbers) {
    if (targets.has(num)) {
      return [num, target - num];
    }
    targets.add(target - num);
  }
  return null;
};

main();
