use std::fs;

#[derive(Debug)]
#[derive(PartialEq)]
enum Direction {
    L,
    R,
    U,
    D,
}

#[derive(Debug)]
struct Path {
    direction: Direction,
    distance: i32,
}

impl Path {
    fn from_string(string: &str) -> Path {
        let (dir, dis) = string.split_at(1);
        let direction = match dir {
            "U" => Direction::U,
            "D" => Direction::D,
            "L" => Direction::L,
            _ => Direction::R,
        };
        let distance = dis.parse::<i32>().unwrap();
        return Path {
            direction,
            distance,
        };
    }
}

fn main() {
    let contents = fs::read_to_string("data/data.txt").expect("Error reading file");
    let paths: Vec<Vec<Path>> = contents
        .split("\n")
        .filter(|line| !line.is_empty())
        .map(|line| {
            line.split(",")
                .map(|string| Path::from_string(string))
                .collect()
        })
        .collect();

    let horiz: Vec<i32> = paths[0]
        .iter()
        .map(|path| {
            match path.direction {
                Direction::L => -path.distance,
                Direction::R => path.distance,
                _ => 0
            }
        })
        .collect();
    let mut min = 0;
    let mut max = 0;
    let mut val = 0;
    for dis in horiz {
        val += dis;
        if val < min {
            min = val;
        }
        if val > max {
            max = val;
        }
    }
    println!("min: {:?}, max: {:?}", min, max);
}
