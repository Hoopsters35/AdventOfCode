import { promises as fs } from "fs";

interface PassportField {
  name: string;
  value: string;
}

interface Passport {
  fields: Array<PassportField>;
}

const main = async () => {
  const content = await (await fs.readFile("data/passports.txt")).toString();
  const passports = content
    .split("\n\n")
    .filter((passport) => passport.length > 0)
    .map((passport) => passport.replace(/ /g, "\n"))
    .map((passport) => passport.split("\n"))
    .map((passportList) => {
      const passport: Passport = {
        fields: [],
      };
      passportList.forEach((passportItem) => {
        const [name, value] = passportItem.split(":");
        passport.fields.push({
          name,
          value,
        });
      });
      return passport;
    });

  console.log(passports.filter(hasValidKeys).length);
  // 204
};

const hasValidKeys = (passport: Passport): boolean => {
  const requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
  const keysSeen = requiredKeys.map((key) =>
    passport.fields.map((field) => field.name).includes(key)
  );
  return keysSeen.reduce((allSeen, keySeen) => allSeen && keySeen);
};

main();
