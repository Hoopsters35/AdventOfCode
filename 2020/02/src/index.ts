import { promises as fs } from "fs";

interface PasswordRequirement {
  character: string;
  minLength: number;
  maxLength: number;
}

interface CorporatePassword {
  password: string;
  requirement: PasswordRequirement;
}

const main = async () => {
  const content = await (await fs.readFile("data/passwords.txt")).toString();
  const passwords: Array<CorporatePassword> = content
    .split("\n")
    .filter((line) => line.length > 0)
    .map((line) => {
        const [min_str, max_str, character, password] = line.match(/^(\d+)-(\d+) (\w): (\w+)$/)!.slice(1, 5);
        const requirement: PasswordRequirement = {
            character,
            minLength: parseInt(min_str),
            maxLength: parseInt(max_str)
        }
        const corp_pass: CorporatePassword = {
            password,
            requirement
        }
        return corp_pass;
    });

    console.log(passwords);
    
    console.log(valid_passwords(passwords).length);
    
};

const valid_passwords = (passwords: Array<CorporatePassword>): Array<CorporatePassword> => {
    return passwords.filter(password => {
        const letterCount = (password.password.match(new RegExp(password.requirement.character, 'g')) || []).length;
        return letterCount >= password.requirement.minLength && letterCount <= password.requirement.maxLength;
    });
}

main();
