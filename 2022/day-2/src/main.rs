use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {

    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("./input.txt") {
        let mut score_part_1 = 0;
        let mut score_part_2 = 0;

        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(rps_game) = line {
                let mut choices = rps_game.split_whitespace();
                let other_choice = choices.next().unwrap();
                let my_choice = choices.next().unwrap();
                
                match (other_choice, my_choice) {
                    ("A", "X") => score_part_1 += 4,
                    ("A", "Y") => score_part_1 += 8,
                    ("A", "Z") => score_part_1 += 3,
                    ("B", "X") => score_part_1 += 1,
                    ("B", "Y") => score_part_1 += 5,
                    ("B", "Z") => score_part_1 += 9,
                    ("C", "X") => score_part_1 += 7,
                    ("C", "Y") => score_part_1 += 2,
                    ("C", "Z") => score_part_1 += 6,
                    _ => score_part_1 += 0,
                };

                match (other_choice, my_choice) {
                    ("A", "X") => score_part_2 += (0 + 3),
                    ("A", "Y") => score_part_2 += (3 + 1),
                    ("A", "Z") => score_part_2 += (6 + 2),
                    ("B", "X") => score_part_2 += (0 + 1),
                    ("B", "Y") => score_part_2 += (3 + 2),
                    ("B", "Z") => score_part_2 += (6 + 3),
                    ("C", "X") => score_part_2 += (0 + 2),
                    ("C", "Y") => score_part_2 += (3 + 3),
                    ("C", "Z") => score_part_2 += (6 + 1),
                    _ => score_part_2 += 0, 
                }
            }
        }
        println!("Part 1: {}", score_part_1);
        println!("Part 2: {}", score_part_2);
    }

}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}