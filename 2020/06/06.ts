const customsInput = await Deno.readTextFile("2020/06/input.txt");
const rawCustomBlocks = customsInput.split("\n\n");
const rawCustoms = rawCustomBlocks.map((rawCustom) => rawCustom.split("\n"));

type AlphabetForm = { [key: string]: boolean };

function getCDFs(rawCustoms: string[][]) {
  return rawCustoms.map((rawCustom) => {
    return rawCustom.map((formLine) => {
      return parseCustomLine(formLine);
    });
  });
}

function parseCustomLine(customLine: string) {
  const customsForm: AlphabetForm = {
    a: false,
    b: false,
    c: false,
    d: false,
    e: false,
    f: false,
    g: false,
    h: false,
    i: false,
    j: false,
    k: false,
    l: false,
    m: false,
    n: false,
    o: false,
    p: false,
    q: false,
    r: false,
    s: false,
    t: false,
    u: false,
    v: false,
    w: false,
    x: false,
    y: false,
    z: false,
  };
  for (let character = 0; character < customLine.length; character++) {
    const letter: string = customLine[character];
    if (letter in customsForm) {
      customsForm[letter] = true;
    }
  }
  return customsForm;
}

function getGroupUnion(group: AlphabetForm[]) {
  var formUnion: AlphabetForm = {};

  group.forEach((form) => {
    for (const letter in form) {
      form[letter] ? (formUnion[letter] = true) : null;
    }
  });

  return formUnion;
}

function countAnyYesFromGroup(unionForm: AlphabetForm) {
  var count = 0;
  for (const letter in unionForm) {
    unionForm[letter] ? count++ : null;
  }

  return count;
}

function countIntersectingAnswers(group: AlphabetForm[]) {
  const alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];
  var count = 0;
  alphabet.forEach((letter) => {
    var existing = true;
    group.forEach((form) => {
      !form[letter] ? (existing = false) : null;
    });
    existing ? count++ : null;
  });
  return count;
}

function countAnyYesSumFromGroups(unionForms: AlphabetForm[]) {
  var sum = 0;
  unionForms.forEach((form) => {
    sum += countAnyYesFromGroup(form);
  });
  return sum;
}

const groups = getCDFs(rawCustoms);

const formUnions = groups.map(getGroupUnion);
console.log("Part 1 :" + countAnyYesSumFromGroups(formUnions));

const intersections = groups.map(countIntersectingAnswers);
console.log(intersections);
const sum = intersections.reduce(
  (totalValue, currentValue) => totalValue + currentValue,
  0
);
console.log("Part 2: " + sum);

//console.log(cf);
