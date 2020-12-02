import { promises as fs } from "fs";

const main = async () => {
    const contents = await (await fs.readFile("data/part1.txt")).toString();
    const nums = contents.split("\n")
        .filter(line => line.length > 0)
        .map(str => parseInt(str));
    
    console.log(part1(nums));
    console.log(part2(nums));
}

const findMatch = (nums: Array<number>, target: number): [number, number] => {
    const targets: Set<number> = new Set();
    for (let num of nums) {
        if (targets.has(num)) {
            return [num, target - num];
        } else {
            targets.add(target - num);
        }
    }
    return [-1, -1];
}

const part1 = (nums: Array<number>): number => {
    const [num1, num2] = findMatch(nums, 2020);
    return num1 * num2;
}

const part2 = (nums: Array<number>): number => {
    for (let i = 0; i < nums.length; i++) {
        const firstNum = nums[i];
        const target = 2020 - firstNum;
        const remainingNums = [...nums.slice(0, i), ...nums.slice(i + 1)];
        const [secondNum, thirdNum] = findMatch(remainingNums, target);
        if (secondNum >= 0) {
            return firstNum * secondNum * thirdNum;
        }
    }
    return -1;
}

main();