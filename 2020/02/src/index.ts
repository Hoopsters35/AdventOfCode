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

    // console.log(passwords);
    console.log(validPasswords(passwords).length);
    // 500

    console.log(trulyValidPasswords(passwords).length);
    // 313
    
};

const validPasswords = (passwords: Array<CorporatePassword>): Array<CorporatePassword> => {
    return passwords.filter(password => {
        const letterCount = (password.password.match(new RegExp(password.requirement.character, 'g')) || []).length;
        return letterCount >= password.requirement.minLength && letterCount <= password.requirement.maxLength;
    });
}

const trulyValidPasswords = (passwords: Array<CorporatePassword>): Array<CorporatePassword> => {
    return passwords.filter(password => {
        const ch = password.requirement.character;
        const chAtMin = password.password.charAt(password.requirement.minLength - 1);
        const chAtMax = password.password.charAt(password.requirement.maxLength - 1);
        return (chAtMin == ch && chAtMax != ch) || (chAtMin != ch && chAtMax == ch);
    })
}

main();
