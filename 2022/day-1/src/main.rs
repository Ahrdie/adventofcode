use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut elves = Vec::new();

    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("./input.txt") {    
        let mut currentelf = Vec::<i32>::new();

        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(calories) = line {
                if calories == "" {
                    elves.push(currentelf);
                    currentelf = Vec::new();
                    // println!("New elf");
                } else {
                    currentelf.push(calories.parse::<i32>().unwrap());
                    // println!("{}", calories);
                }
            }
        }
    }

    let mut calories = Vec::<i32>::new();

    for elf in elves {
        let mut elfCalories = 0;
        for calorie in elf {
            elfCalories += calorie;
        }
        calories.push(elfCalories);
    }

    calories.sort_by(|a, b| b.cmp(a));
    println!("{}", calories[0] + calories[1] + calories[2]);
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}