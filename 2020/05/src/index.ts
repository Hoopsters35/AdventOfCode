import { promises as fs } from "fs";

interface BoardingPass {
  row: string;
  column: string;
}

const main = async () => {
  const content = await (
    await fs.readFile("data/boardingpasses.txt")
  ).toString();
  const boardingPasses: Array<BoardingPass> = content
    .split("\n")
    .filter((line) => line.length > 0)
    .map((line) => {
      return {
        row: line.substring(0, 7),
        column: line.substring(7),
      };
    });

  console.log(maxId(boardingPasses));
  // 818
};

const rowToInt = (row: string) =>
  parseInt(row.replace(/F/g, "0").replace(/B/g, "1"), 2);

const columnToInt = (column: string) =>
  parseInt(column.replace(/L/g, "0").replace(/R/g, "1"), 2);

const maxId = (boardingPasses: Array<BoardingPass>): number => {
  const ids = boardingPasses.map((boardingPass) => {
    const row = rowToInt(boardingPass.row);
    const column = columnToInt(boardingPass.column);
    return row * 8 + column;
  });
  return Math.max(...ids);
};

main();
