const forestInput = await Deno.readTextFile("2020/03/input.txt");
const forestlines = forestInput.split("\n");

type direction = {
  down: number;
  right: number;
};

function getForestData(forestLines: string[]): boolean[][] {
  const forestData = forestLines.map((line) => {
    const dataline = [];
    for (const character of line) {
      dataline.push(character == "#" ? true : false);
    }
    return dataline;
  });
  return forestData;
}

function countTreesInDirection(
  forestData: boolean[][],
  direction: direction
): number {
  var position = 0;
  var treesMet = 0;
  forestData?.forEach((line, index) => {
    if (index % direction.down == 0) {
      const currentPosition = position % line.length;
      position += direction.right;
      if (line[currentPosition]) {
        treesMet++;
      }
    }
  });

  return treesMet;
}

const forestData = getForestData(forestlines);
const treesMet = countTreesInDirection(forestData, { down: 2, right: 1 });
console.log("Part 1: " + treesMet);

function calculateSlopeChecksum(
  forestData: boolean[][],
  slopes: direction[]
): number {
  var slopeChecksum = 1;
  slopes.forEach((slope) => {
    slopeChecksum *= countTreesInDirection(forestData, slope);
  });
  return slopeChecksum;
}

const slopes = [
  { down: 1, right: 1 },
  { down: 1, right: 3 },
  { down: 1, right: 5 },
  { down: 1, right: 7 },
  { down: 2, right: 1 },
];

console.log("Part 2: " + calculateSlopeChecksum(forestData, slopes));
