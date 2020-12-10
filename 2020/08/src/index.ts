import { promises as fs } from "fs";

enum Operation {
  ACCUMULATE,
  JUMP,
  NO_OPERATION,
}

interface Instruction {
  operation: Operation;
  argument: number;
}

const main = async () => {
  const content = await (await fs.readFile("data/instructions.txt")).toString();
  const instructions: Array<Instruction> = content
    .split("\n")
    .filter((line) => line.length > 0)
    .map((line) => {
      const [opString, argString] = line.split(" ");
      const operation = strToOperation(opString);
      const argument = parseInt(argString);
      return { operation, argument };
    });

  console.log(valueBeforeInfiniteLoop(instructions));
};

const strToOperation = (string: string): Operation => {
  switch (string) {
    case "acc":
      return Operation.ACCUMULATE;
    case "jmp":
      return Operation.JUMP;
    case "nop":
      return Operation.NO_OPERATION;
    default:
      throw new Error("Bad operation string");
  }
};

const valueBeforeInfiniteLoop = (instructions: Array<Instruction>): number => {
  let instructionIndex = 0;
  let seenInstructions: Set<number> = new Set();
  let value = 0;

  while (!seenInstructions.has(instructionIndex)) {
    seenInstructions.add(instructionIndex);
    const instruction = instructions[instructionIndex];
    switch (instruction.operation) {
      case Operation.ACCUMULATE:
        value += instruction.argument;
        instructionIndex++;
        break;
      case Operation.JUMP:
        instructionIndex += instruction.argument;
        break;
      case Operation.NO_OPERATION:
        instructionIndex++;
        break;
    }
  }

  return value;
};

main();
