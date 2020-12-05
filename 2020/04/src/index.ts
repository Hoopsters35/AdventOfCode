import { promises as fs } from "fs";

interface PassportField {
  name: string;
  value: string;
}

interface Passport {
  fields: Array<PassportField>;
}

type ValidationFunction = (value: string) => boolean;

const main = async () => {
  const content = await (await fs.readFile("data/passports.txt")).toString();
  const passports = content
    .split("\n\n")
    .filter((passport) => passport.length > 0)
    .map((passport) => passport.replace(/ /g, "\n"))
    .map((passport) => passport.split("\n"))
    .map((passport) => passport.filter((fields) => fields.length > 0))
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

  console.log(passports.filter(passesValidation).length);
  // 179
};

const hasValidKeys = (passport: Passport): boolean => {
  const requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
  const keysSeen = requiredKeys.map((key) =>
    passport.fields.map((field) => field.name).includes(key)
  );
  return keysSeen.reduce((allSeen, keySeen) => allSeen && keySeen);
};

const passesValidation = (passport: Passport): boolean => {
  const validationFunctions: Record<string, ValidationFunction> = {
    byr: (value: string): boolean => {
      const year = parseInt(value);
      return 1920 <= year && year <= 2002;
    },
    iyr: (value: string): boolean => {
      const year = parseInt(value);
      return 2010 <= year && year <= 2020;
    },
    eyr: (value: string): boolean => {
      const year = parseInt(value);
      return 2020 <= year && year <= 2030;
    },
    hgt: (value: string): boolean => {
      const num = parseInt(value.substring(0, value.length - 2));
      if (value.includes("cm")) {
        return 150 <= num && num <= 193;
      } else {
        return 59 <= num && num <= 76;
      }
    },
    hcl: (value: string): boolean => /^#[\da-f]{6}$/.test(value),
    ecl: (value: string): boolean =>
      ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].includes(value),
    pid: (value: string): boolean => /^\d{9}$/.test(value),
    cid: (_: string): boolean => true,
  };

  return (
    hasValidKeys(passport) &&
    passport.fields
      .map((field) => validationFunctions[field.name](field.value))
      .reduce((allValid, fieldValid) => allValid && fieldValid)
  );
};

main();
