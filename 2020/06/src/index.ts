import { promises as fs } from "fs";

const main = async () => {
  const content = await (await fs.readFile("data/customs.txt")).toString();
  const groups = content.split("\n\n").map((group) =>
    group
      .split("\n")
      .filter((line) => line.length > 0)
      .map((string) => new Set(string.split("")))
  );

  console.log(totalLength(groups.map(setUnions)));
  // 6930
  console.log(totalLength(groups.map(setIntersects)));
  // 3585
};

const setUnions = (sets: Array<Set<string>>): Set<string> =>
  sets.reduce((union, set) => new Set([...union, ...set]));

const setIntersects = (sets: Array<Set<string>>): Set<string> =>
  sets.reduce(
    (union, set) => new Set([...union].filter((item) => set.has(item)))
  );

const totalLength = (sets: Array<Set<string>>): number =>
  sets.map((set) => set.size).reduce((total, size) => total + size);

main();
