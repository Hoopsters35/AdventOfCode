import { promises as fs } from "fs";

const TREE = "#";

interface Slope {
  x: number;
  y: number;
}

const main = async () => {
  const content = await (await fs.readFile("data/map.txt")).toString();
  const map = content.split("\n").filter((line) => line.length > 0);

  const slope: Slope = {
    x: 3,
    y: 1,
  };

  console.log(numTreesEncountered(map, slope));
  // 178

  const slopes: Array<Slope> = [
    {
      x: 1,
      y: 1,
    },
    {
      x: 3,
      y: 1,
    },
    {
      x: 5,
      y: 1,
    },
    {
      x: 7,
      y: 1,
    },
    {
      x: 1,
      y: 2,
    },
  ];

  console.log(
    slopes
      .map((slope) => numTreesEncountered(map, slope))
      .reduce((product, trees) => product * trees)
  );
  // 3492520200
};

const numTreesEncountered = (map: Array<string>, slope: Slope): number => {
  let trees = 0;
  let x = 0;
  let y = 0;
  while (y < map.length) {
    if (map[y].charAt(x) == TREE) {
      trees++;
    }
    x = (x + slope.x) % map[y].length;
    y += slope.y;
  }
  return trees;
};

main();
