import { promises as fs } from "fs";

interface Rule {
  bagName: string;
  count: number;
}

interface Bag {
  name: string;
  rules: Array<Rule>;
}

const main = async () => {
  const content = await (await fs.readFile("data/rules.txt")).toString();

  const bags: Array<Bag> = content
    .split("\n")
    .filter((bag) => bag.length > 0)
    .map((bag) => {
      const [bagName, ruleStrings] = bag.split(" bags contain ");
      const rules = ruleStrings.startsWith("no other")
        ? []
        : ruleStrings.split(", ").map((ruleString) => {
            const [countString, bagAdjective, bagColor, _] = ruleString.split(
              " "
            );
            const count = parseInt(countString);
            const ruleBagName = `${bagAdjective} ${bagColor}`;

            return {
              count,
              bagName: ruleBagName,
            };
          });
      return {
        name: bagName,
        rules,
      };
    });

  console.log(allBagsContaining(bags, "shiny gold").size);
  // 179
  console.log(totalBags(bags, "shiny gold") - 1);
  // 18925
};

const totalBags = (bags: Array<Bag>, bagName: string): number => {
  const bag = bags.find((b) => b.name == bagName);
  if (!bag) {
    console.log(bagName);
    return 0;
  }
  if (bag.rules.length == 0) {
    return 1;
  }
  return (
    1 +
    bag.rules
      .map((rule) => rule.count * totalBags(bags, rule.bagName))
      .reduce((sum, count) => sum + count)
  );
};

const allBagsContaining = (bags: Array<Bag>, bagName: string): Set<Bag> => {
  return new Set(
    bags.filter((bag) => {
      const nestedNames = allNestedBags(bags, bag.name);
      return nestedNames.has(bagName);
    })
  );
};

const allNestedBags = (bags: Array<Bag>, bagName: string): Set<string> => {
  const bag = bags.find((b) => b.name == bagName)!;
  const ruleBagNames = bag.rules.map((rule) => rule.bagName);
  const descendents = bags.filter((b) => ruleBagNames.includes(b.name));
  const descendentNames = new Set(descendents.map((b) => b.name));

  return unionAll(
    descendentNames,
    ...descendents.map((b) => allNestedBags(bags, b.name))
  );
};

const setUnion = (left: Set<string>, right: Set<string>): Set<string> => {
  return new Set([...left, ...right]);
};

const unionAll = (...sets: Array<Set<string>>): Set<string> => {
  return sets.reduce((union, set) => setUnion(union, set));
};

main();
