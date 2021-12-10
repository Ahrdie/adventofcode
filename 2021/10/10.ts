type OpenBrackets = "(" | "[" | "{" | "<";
type CloseBrackets = ")" | "]" | "}" | ">";
type Brackets = OpenBrackets | CloseBrackets;

const input = `[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]`;

const bracketPairs: { [key: string]: string } = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">",
};

const illegalBracketValues = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137,
};

const completionBracketValues: { [key: string]: number } = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4,
};

const inputLines = input.split(`\n`);
console.log("Part 1:", countUnexpectedBrackets(inputLines));
console.log("Part 2:", valueCompletionLines(inputLines));

function countUnexpectedBrackets(inputLines: string[]) {
  let sum = 0;
  inputLines.forEach((line) => {
    let illegalCharacterOrFalse = findIllegalCharacterOrNot(line);
    if (
      illegalCharacterOrFalse != false &&
      illegalCharacterOrFalse as CloseBrackets
    ) {
      if (illegalCharacterOrFalse in illegalBracketValues) {
        let value = illegalBracketValues[illegalCharacterOrFalse];
        sum += value;
      }
    }
  });
  return sum;
}

function valueCompletionLines(inputLines: string[]): number {
  let scores: number[] = [];

  const completionLines = inputLines.map(getLineCompletion);

  completionLines.forEach((line) => {
    
    if (line != false) {
			line.reverse()
			
			let linesum = 0;
      for (let i = 0; i < line.length; i++) {
        const symbol: string = line[i];
        if (symbol in completionBracketValues) {
          let value = completionBracketValues[symbol];
          linesum *= 5;
          linesum += value;
        }
      }
			scores.push(linesum);
			
    }
    
  });
	scores = scores.sort((a, b) => a - b);
	return scores[Math.floor(scores.length /2)];
}

function findIllegalCharacterOrNot(line: string): CloseBrackets | false {
  let stack: string[] = [];

  for (let i = 0; i < line.length; i++) {
    if (line[i] in bracketPairs) {
      stack.push(bracketPairs[line[i]]);
    } else if (line[i] == stack[stack.length - 1]) {
      stack.pop();
    } else {
      return line[i] as CloseBrackets;
    }
  }
  return false;
}

function getLineCompletion(line: string): string[] | false {
  let stack: string[] = [];

  for (let i = 0; i < line.length; i++) {
    if (line[i] in bracketPairs) {
      stack.push(bracketPairs[line[i]]);
    } else if (line[i] == stack[stack.length - 1]) {
      stack.pop();
    } else {
      return false;
    }
  }
  return stack;
}
