const pwInput = await Deno.readTextFile("2020/02/input.txt");
const pwRuleLines = pwInput.split("\n");

type rulePW = {
  min: number;
  max: number;
  letter: string;
  pw: string;
};

function getRulePasswords(rawLines: string[]): rulePW[] | undefined {
  const rulePWs = rawLines.map((line: string) => {
    const min = line.match(/\d+(?=-)/);
    const max = line.match(/(?<=-)\d+/);
    const letter = line.match(/[a-z](?=:)/);
    const pw = line.match(/[a-z]{2,}/);
    return {
      min: Number(min![0]),
      max: Number(max![0]),
      letter: letter![0],
      pw: pw![0],
    };
  });
  return rulePWs;
}

function passwordIsValidOld(passwordWithRules: rulePW): boolean {
  const letterToSearch = new RegExp(passwordWithRules.letter, "g");
  const letters = passwordWithRules.pw.match(letterToSearch);
  if (letters != null) {
    return (
      letters!.length >= passwordWithRules.min &&
      letters!.length <= passwordWithRules.max
    );
  }
  return false;
}

const rulePws = getRulePasswords(pwRuleLines);
const oldValidRulePws = rulePws?.filter((rulePw) => {
  return passwordIsValidOld(rulePw);
});

console.log("Part 1: " + oldValidRulePws?.length);

function passwordIsValidNew(pwRules: rulePW): boolean {
  const charIsInPos1 = pwRules.pw.charAt(pwRules.min - 1) == pwRules.letter;
  const charIsInPos2 = pwRules.pw.charAt(pwRules.max - 1) == pwRules.letter;

  console.log(`1:${charIsInPos1} 2:${charIsInPos2}`);
  return charIsInPos1 ? !charIsInPos2 : charIsInPos2;
}

const newValidRulePws = rulePws?.filter((rulePw) => {
  console.log("\n");
  console.log(rulePw);
  const result = passwordIsValidNew(rulePw);
  console.log(result);

  return result;
});

console.log("Part 2: " + newValidRulePws?.length);
