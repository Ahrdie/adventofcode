const inputText = await Deno.readTextFile("2020/01/input.txt");
const entries = Array.from(inputText.split("\n"), Number);

function findTwo2020Entries(entries: number[]) {
  return entries.filter((entry) => {
    if (entries.includes(2020 - entry)) {
      return true;
    }
  });
}

function findThree2020Entries(entries: number[]): number[] {
  var result: number[] = [];
  entries.forEach((firstElement) => {
    entries.forEach((secondElement) => {
      const thirdElement = 2020 - firstElement - secondElement;
      if (entries.includes(thirdElement)) {
        result = [firstElement, secondElement, thirdElement];
        return;
      }
    });
  });

  return result;
}

const solution = findThree2020Entries(entries);
console.log(solution[0] * solution[1] * solution[2]);
