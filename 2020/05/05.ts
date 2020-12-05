const seatsInput = await Deno.readTextFile("2020/05/input.txt");
const rawSeats = seatsInput.split("\n");

type Seat = { row: number; column: number };

function getSeatPosition(rawSeat: string): Seat {
  const rawRow = rawSeat.match(/[FB]{7}/);
  const row = binaryConvertToNumer(rawRow![0], "B");

  const columnRaw = rawSeat.match(/[LR]{3}/);
  const column = binaryConvertToNumer(columnRaw![0], "R");
  return { row, column };
}

function binaryConvertToNumer(input: string, one: string): number {
  var sum = 0;
  for (let i = 0; i < input.length; i++) {
    sum += input[i] == one ? Math.pow(2, input.length - 1 - i) : 0;
  }
  return sum;
}

function getSeatId(seat: Seat): number {
  return seat.row * 8 + seat.column;
}

function getHighestSeatId(rawSeats: string[]): number {
  var highestID = 0;
  rawSeats.forEach((rawSeat) => {
    var id = getSeatId(getSeatPosition(rawSeat));
    id > highestID ? (highestID = id) : null;
  });
  return highestID;
}

var highestID = getHighestSeatId(rawSeats);

console.log("Part 1: " + highestID);

function getPlaneConfiguration(rawSeats: string[]) {
  var plane: number[][] = [];

  for (let row = 0; row < 128; row++) {
    plane[row] = [0, 0, 0, 0, 0, 0, 0, 0];
  }
  rawSeats.forEach((rawSeat) => {
    const seat = getSeatPosition(rawSeat);
    plane[seat.row][seat.column] = getSeatId(seat);
  });
  return plane!;
}
const plane = getPlaneConfiguration(rawSeats);
console.log(plane);
console.log("Easily find the row in the visual output");
