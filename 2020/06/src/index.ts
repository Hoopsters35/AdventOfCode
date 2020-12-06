import { promises as fs } from "fs";

const main = async() => {
    const content = await (await fs.readFile("data/customs.txt")).toString();
    const groups = content.split("\n\n").map(group => group.split("\n"));
    console.log(groups.map(group => totalYes(group)).reduce((sum, yesses) => sum + yesses));
    // 6930
    
}

const totalYes = (group: Array<string>): number => {
    const letterSets = group.map(personString => new Set(personString.split("")))
    return letterSets.reduce((yesses, currentYesses) => new Set([...yesses, ...currentYesses])).size;
}

main()
