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
  // 1563
  console.log(valueOfFixedInstructions(instructions));
  // 767
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

const valueOfFixedInstructions = (instructions: Array<Instruction>): number => {
  const testIndices = jumpAndNopIndices(instructions);

  for (let testIndex of testIndices) {
    const testInstructions = instructions.map((instruction, index) => {
      if (index != testIndex) {
        return instruction;
      }
      return {
        argument: instruction.argument,
        operation:
          instruction.operation == Operation.JUMP
            ? Operation.NO_OPERATION
            : Operation.JUMP,
      };
    });
    const value = finalValueIfNotInfiniteLoop(testInstructions);
    if (value > 0) {
      return value;
    }
  }
  return 0;
};

const jumpAndNopIndices = (instructions: Array<Instruction>): Array<number> => {
  return instructions
    .map((instruction, i) => {
      return {
        i,
        instruction,
      };
    })
    .filter(({ instruction }) => {
      return (
        instruction.operation == Operation.JUMP ||
        instruction.operation == Operation.NO_OPERATION
      );
    })
    .map(({ i }) => i);
};

const finalValueIfNotInfiniteLoop = (
  instructions: Array<Instruction>
): number => {
  let instructionIndex = 0;
  let value = 0;
  const seenInstructions: Set<number> = new Set();
  while (
    !seenInstructions.has(instructionIndex) &&
    instructionIndex < instructions.length
  ) {
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
  return seenInstructions.has(instructionIndex) ? 0 : value;
};

main();
